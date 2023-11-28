#
# -*- coding: utf-8 -*-
# © Copyright 2020 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_interfaces class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from __future__ import absolute_import, division, print_function
__metaclass__ = type

try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote

"""
The use of natsort causes sanity error due to it is not available in python version currently used.
When natsort becomes available, the code here and below using it will be applied.
from natsort import (
    natsorted,
    ns
)
"""
from copy import deepcopy
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import (
    Facts,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.interfaces_util import (
    build_interfaces_create_request,
    retrieve_default_intf_speed
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    get_diff,
    update_states,
    normalize_interface_name,
    remove_empties_from_list
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.formatted_diff_utils import (
    __DELETE_CONFIG_IF_NO_SUBCONFIG,
    get_new_config,
    get_formatted_config_diff
)
from ansible.module_utils._text import to_native
from ansible.module_utils.connection import ConnectionError
import traceback

TEST_KEYS_formatted_diff = [
    {'config': {'name': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}},
]

LIB_IMP_ERR = None
ERR_MSG = None
try:
    import requests
    HAS_LIB = True
except Exception as e:
    HAS_LIB = False
    ERR_MSG = to_native(e)
    LIB_IMP_ERR = traceback.format_exc()

GET = 'get'
PATCH = 'patch'
DELETE = 'delete'
url = 'data/openconfig-interfaces:interfaces/interface=%s'

attributes_default_value = {
    "description": '',
    "mtu": 9100,
    "enabled": False,
    "speed": 'SPEED_DEFAULT',
    "auto_negotiate": False,
    "fec": 'FEC_DISABLED',
    "advertised_speed": ''
}


class Interfaces(ConfigBase):
    """
    The sonic_interfaces class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'interfaces',
    ]

    params = ('description', 'mtu', 'enabled', 'speed', 'auto_negotiate', 'advertised_speed', 'fec')
    delete_flag = False

    def __init__(self, module):
        super(Interfaces, self).__init__(module)

    def get_interfaces_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        interfaces_facts = facts['ansible_network_resources'].get('interfaces')
        if not interfaces_facts:
            return []

        return interfaces_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = list()

        existing_interfaces_facts = self.get_interfaces_facts()
        commands, requests = self.set_config(existing_interfaces_facts)
        if commands and len(requests) > 0:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        changed_interfaces_facts = self.get_interfaces_facts()

        result['before'] = existing_interfaces_facts
        if result['changed']:
            result['after'] = changed_interfaces_facts

        new_config = changed_interfaces_facts
        old_config = existing_interfaces_facts
        if self._module.check_mode:
            result.pop('after', None)
            new_config = get_new_config(commands, existing_interfaces_facts,
                                        TEST_KEYS_formatted_diff)
            # See the above comment about natsort module
            # new_config = natsorted(new_config, key=lambda x: x['name'])
            # For time-being, use simple "sort"
            new_config.sort(key=lambda x: x['name'])
            result['after(generated)'] = new_config
            old_config.sort(key=lambda x: x['name'])

        if self._module._diff:
            result['config_diff'] = get_formatted_config_diff(old_config,
                                                              new_config)
        result['warnings'] = warnings
        return result

    def set_config(self, existing_interfaces_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']
        have = existing_interfaces_facts
        self.filter_out_mgmt_interface(want, have)

        normalize_interface_name(want, self._module)
        resp = self.set_state(want, have)
        return to_list(resp)

    def set_state(self, want, have):
        """ Select the appropriate function based on the state provided

        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        state = self._module.params['state']
        # diff method works on dict, so creating temp dict
        diff = get_diff(want, have)
        # removing the dict in case diff found

        if state == 'overridden':
            commands, requests = self._state_overridden(want, have)
        elif state == 'deleted':
            commands, requests = self._state_deleted(want, have)
        elif state == 'merged':
            commands, requests = self._state_merged(want, have, diff)
        elif state == 'replaced':
            commands, requests = self._state_replaced(want, have)

        return commands, requests

    def _state_replaced(self, want, have):
        """ The command generator when state is replaced

        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :param interface_type: interface type
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        requests = []

        commands, requests = self.get_replaced_overridden_config(want, have, "replaced")

        return commands, requests

    def _state_overridden(self, want, have):
        """ The command generator when state is overridden

        :param want: the desired configuration as a dictionary
        :param obj_in_have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        requests = []

        commands, requests = self.get_replaced_overridden_config(want, have, "overridden")

        return commands, requests

    def _state_merged(self, want, have, diff):
        """ The command generator when state is merged

        :param want: the additive configuration as a dictionary
        :param obj_in_have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = self.filter_commands_to_change(diff, have)
        requests = self.get_modify_interface_requests(commands, have)
        if commands and len(requests) > 0:
            commands = update_states(commands, "merged")
        else:
            commands = []

        return commands, requests

    def _state_deleted(self, want, have):
        """ The command generator when state is deleted

        :param want: the objects from which the configuration should be removed
        :param obj_in_have: the current configuration as a dictionary
        :param interface_type: interface type
        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        # if want is none, then delete all the interfaces

        want = remove_empties_from_list(want)
        delete_all = False
        if not want:
            commands = have
            delete_all = True
        else:
            commands = want

        commands_del, requests = self.handle_delete_interface_config(commands, have, delete_all)
        commands = []
        if commands_del:
            commands.extend(update_states(commands_del, "deleted"))

        return commands, requests

    def build_request(self, conf, have_conf, intf_name, attr):
        eth_conf = dict()
        request = dict()
        commands = {}
        method = PATCH

        attributes_payload = {
            "description": 'description',
            "mtu": 'mtu',
            "enabled": 'enabled',
            "speed": 'port-speed',
            "auto_negotiate": 'auto-negotiate'
        }

        if not conf['name'].startswith('Loopback'):
            c_attr = conf.get(attr, None)
            h_attr = have_conf.get(attr, None)
            if self.delete_flag:
                default_val = attributes_default_value[attr]
                if attr == 'speed':
                    default_val = retrieve_default_intf_speed(self._module, intf_name)

                if c_attr and h_attr and h_attr != default_val:
                    if attr == "auto_negotiate" and c_attr:
                        # For auto-negotiate, we assign value to False since deleting the attribute will become None
                        config_url = (url + '/openconfig-if-ethernet:ethernet/config') % quote(intf_name, safe='')
                        eth_conf['auto-negotiate'] = False
                        payload = {'openconfig-if-ethernet:config': eth_conf}
                        request = {"path": config_url, "method": method, "data": payload}
                    else:
                        method = DELETE
                        attr_url = "/openconfig-if-ethernet:ethernet/config/" + attributes_payload[attr]
                        if attr in ('description', 'mtu', 'enabled'):
                            attr_url = "/config/" + attributes_payload[attr]
                        config_url = (url + attr_url) % quote(intf_name, safe='')
                        request = {"path": config_url, "method": method}
                    commands[attr] = h_attr

            elif c_attr is not None:
                if attr == 'speed' and c_attr == 'SPEED_DEFAULT':
                    method = DELETE
                    attr_url = "/openconfig-if-ethernet:ethernet/config/" + attributes_payload[attr]
                    config_url = (url + attr_url) % quote(intf_name, safe='')
                    request = {"path": config_url, "method": method}
                else:
                    payload_attr = attributes_payload[attr]
                    config_url = (url + '/openconfig-if-ethernet:ethernet/config') % quote(intf_name, safe='')
                    if attr == 'enabled' or attr == "auto_negotiate":
                        eth_conf[payload_attr] = True if c_attr else False
                    elif attr == 'speed':
                        eth_conf[payload_attr] = 'openconfig-if-ethernet:' + c_attr
                    else:
                        eth_conf[payload_attr] = c_attr
                    payload = {'openconfig-if-ethernet:config': eth_conf}
                    if attr in ('description', 'mtu', 'enabled'):
                        config_url = (url + '/config') % quote(intf_name, safe='')
                        payload = {'openconfig-interfaces:config': eth_conf}
                    request = {"path": config_url, "method": method, "data": payload}

        return commands, request

    def build_fec_request(self, conf, have_conf, intf_name):
        eth_conf = dict()
        request = dict()
        commands = {}
        method = PATCH

        if intf_name.startswith('Eth'):
            c_fec = conf.get('fec', None)
            if c_fec:
                if self.delete_flag:
                    h_fec = have_conf.get('fec', None)
                    if h_fec and h_fec != 'FEC_DISABLED':
                        eth_conf['openconfig-if-ethernet-ext2:port-fec'] = 'FEC_DISABLED'
                        commands['fec'] = h_fec
                else:
                    eth_conf['openconfig-if-ethernet-ext2:port-fec'] = 'openconfig-platform-types:' + conf['fec']

                if eth_conf:
                    eth_url = (url + '/openconfig-if-ethernet:ethernet/config') % quote(intf_name, safe='')
                    payload = {'openconfig-if-ethernet:config': eth_conf}
                    request = {"path": eth_url, "method": method, "data": payload}

        return commands, request

    def build_advertise_speed_request(self, conf, have_conf, intf_name):
        request = dict()
        eth_conf = dict()
        commands = {}
        method = PATCH

        if intf_name.startswith('Eth'):
            c_ads = conf.get('advertised_speed', [])
            h_ads = have_conf.get('advertised_speed', [])
            c_ads = [] if c_ads is None else c_ads
            h_ads = [] if h_ads is None else h_ads
            if c_ads:
                if self.delete_flag:
                    new_ads = list(set(h_ads).difference(c_ads))
                    if new_ads:
                        eth_conf['openconfig-if-ethernet-ext2:advertised-speed'] = ','.join(new_ads)
                    else:
                        method = DELETE
                    commands['advertised_speed'] = c_ads
                else:
                    new_ads = h_ads + c_ads
                    if new_ads:
                        eth_conf['openconfig-if-ethernet-ext2:advertised-speed'] = ','.join(new_ads)

                if method == DELETE:
                    ads_url = '/openconfig-if-ethernet-ext2:advertised-speed'
                    eth_url = '/openconfig-if-ethernet:ethernet/config'
                    config_url = (url + eth_url + ads_url) % quote(intf_name, safe='')
                    request = {"path": config_url, "method": method}
                else:
                    eth_url = (url + '/openconfig-if-ethernet:ethernet/config') % quote(intf_name, safe='')
                    payload = {'openconfig-if-ethernet:config': eth_conf}
                    request = {"path": eth_url, "method": method, "data": payload}

        return commands, request

    def handle_delete_interface_config(self, commands, have, delete_all=False):
        requests = []
        del_commands = []
        if not commands:
            return del_commands, requests

        # Create URL and payload
        for cmd in commands:
            name = cmd['name']
            have_conf = next((cfg for cfg in have if cfg['name'] == name), None)
            if have_conf:
                lp_key_set = set(cmd.keys())
                if name.startswith('Loopback'):
                    if delete_all or len(lp_key_set) == 1:
                        method = DELETE
                        lpbk_url = url % quote(name, safe='')
                        request = {"path": lpbk_url, "method": method}
                        requests.append(request)

                        del_commands.append({'name': name})

                        continue

                if len(lp_key_set) == 1:
                    conf = deepcopy(have_conf)
                else:
                    conf = deepcopy(cmd)

                del_cmd = {'name': name}
                non_eth_attribute = ('description', 'mtu', 'enabled')
                eth_attribute = ('description', 'mtu', 'enabled', 'auto_negotiate', 'speed')
                self.delete_flag = True
                attribute = eth_attribute

                if not name.startswith('Eth'):
                    attribute = non_eth_attribute

                for attr in attribute:
                    cmd_attr, attr_request = self.build_request(conf, have_conf, name, attr)
                    if attr_request:
                        requests.append(attr_request)
                        del_cmd.update(cmd_attr)

                cmd_fec, fec_request = self.build_fec_request(conf, have_conf, name)
                if fec_request:
                    requests.append(fec_request)
                    del_cmd.update(cmd_fec)

                cmd_ads, advertise_speed_request = self.build_advertise_speed_request(conf, have_conf, name)
                if advertise_speed_request:
                    requests.append(advertise_speed_request)
                    del_cmd.update(cmd_ads)

            if requests:
                del_commands.append(del_cmd)

        return del_commands, requests

    def filter_commands_to_change(self, configs, have):
        commands = []
        if configs:
            for conf in configs:
                if self.is_this_change_required(conf, have):
                    commands.append(conf)
        return commands

    def get_modify_interface_requests(self, configs, have):
        self.delete_flag = False
        return self.get_interface_requests(configs, have)

    def get_interface_requests(self, configs, have):
        requests = []
        if not configs:
            return requests

        # Create URL and payload
        for conf in configs:
            name = conf["name"]

            if self.delete_flag and name.startswith('Loopback'):
                method = DELETE
                lpbk_url = url % quote(name, safe='')
                request = {"path": lpbk_url, "method": method}
                requests.append(request)
            else:
                # Create Loopback in case not availble in have
                have_conf = next((cfg for cfg in have if cfg['name'] == name), None)
                if name.startswith('Loopback'):
                    if not have_conf:
                        loopback_create_request = build_interfaces_create_request(name)
                        requests.append(loopback_create_request)

                non_eth_attribute = ('description', 'mtu', 'enabled')
                eth_attribute = ('description', 'mtu', 'enabled', 'auto_negotiate', 'speed')
                attribute = eth_attribute

                if not name.startswith('Eth'):
                    attribute = non_eth_attribute

                for attr in attribute:
                    commands, attr_request = self.build_request(conf, have_conf, name, attr)
                    if attr_request:
                        requests.append(attr_request)

                commands, fec_request = self.build_fec_request(conf, have_conf, name)
                if fec_request:
                    requests.append(fec_request)

                commands, advertise_speed_request = self.build_advertise_speed_request(conf, have_conf, name)
                if advertise_speed_request:
                    requests.append(advertise_speed_request)

                have_conf = next((cfg for cfg in have if cfg['name'] == name), None)

        return requests

    def is_this_change_required(self, conf, have):
        ret_flag = False
        intf = next((e_intf for e_intf in have if conf['name'] == e_intf['name']), None)
        if intf:
            # Check all parameter if any one is different from existing
            for param in self.params:
                if conf.get(param) is not None and conf.get(param) != intf.get(param):
                    ret_flag = True
                    break
        else:
            # if given interface is not present
            ret_flag = True

        return ret_flag

    def filter_out_mgmt_interface(self, want, have):
        if want:
            mgmt_intf = next((intf for intf in want if intf['name'] == 'Management0'), None)
            if mgmt_intf:
                self._module.fail_json(msg='Management interface should not be configured.')

        for intf in have:
            if intf['name'] == 'Management0':
                have.remove(intf)
                break

    def get_replaced_overridden_config(self, want, have, cur_state):
        commands, requests = [], []

        commands_del, requests_del = [], []
        commands_add, requests_add = [], []

        delete_all = False

        for conf in want:
            name = conf['name']
            intf = next((e_intf for e_intf in have if name == e_intf['name']), None)
            if name.startswith('Loopback'):
                if not intf:
                    commands_add.append({'name': name})

            temp_conf = dict()

            temp_conf['name'] = conf['name']
            non_eth_attribute = ('description', 'mtu', 'enabled')
            eth_attribute = ('description', 'mtu', 'enabled', 'auto_negotiate', 'speed', 'advertised_speed', 'fec')
            attribute = eth_attribute

            if not name.startswith('Eth'):
                attribute = non_eth_attribute
            for attr in attribute:
                default_val = attributes_default_value[attr]
                if attr == 'speed':
                    default_val = retrieve_default_intf_speed(self._module, conf['name'])
                temp_conf[attr] = default_val if conf.get(attr, None) is None else conf[attr]

            if not intf:
                commands_add.append(temp_conf)
                if cur_state == "overridden":
                    delete_all = True
            else:
                is_change = False
                for attr in temp_conf:
                    if attr == "advertised_speed" and temp_conf[attr]:
                        temp_conf[attr].sort()

                    if intf[attr] and intf[attr] != temp_conf[attr]:
                        is_change = True

                if is_change:
                    commands_add.append(temp_conf)
                    if cur_state == "overridden":
                        delete_all = True
                    else:
                        commands_del.append(intf)

        if delete_all:
            commands_del.extend(have)

        if commands_del:
            commands_del, requests_del = self.handle_delete_interface_config(commands_del, have, delete_all)

            if len(requests_del) > 0:
                commands.extend(update_states(commands_del, "deleted"))
                requests.extend(requests_del)

        if commands_add:
            requests_add = self.get_modify_interface_requests(commands_add, have)

            if len(requests_add) > 0:
                commands.extend(update_states(commands_add, cur_state))
                requests.extend(requests_add)

        return commands, requests
