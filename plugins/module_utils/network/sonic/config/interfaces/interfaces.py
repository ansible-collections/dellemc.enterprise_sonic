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
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    get_diff,
    update_states,
    normalize_interface_name
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
        normalize_interface_name(want, self._module)
        have = existing_interfaces_facts

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
            have = [each_intf for each_intf in have if each_intf['name'].startswith('Ethernet')]
            commands, requests = self._state_overridden(want, have, diff)
        elif state == 'deleted':
            commands, requests = self._state_deleted(want, have, diff)
        elif state == 'merged':
            commands, requests = self._state_merged(want, have, diff)
        elif state == 'replaced':
            commands, requests = self._state_replaced(want, have, diff)

        return commands, requests

    def _state_replaced(self, want, have, diff):
        """ The command generator when state is replaced

        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :param interface_type: interface type
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = self.filter_comands_to_change(diff, have)
        commands_del = self.filter_comands_to_delete(commands, have)
        requests = self.get_delete_interface_requests(commands_del, have)
        commands_mer = self.filter_comands_to_change(commands, have)
        requests.extend(self.get_modify_interface_requests(commands_mer, have))
        if commands and len(requests) > 0:
            commands_dlt, commands_rep = self.classify_delete_commands(commands_del)
            commands = []
            if commands_dlt:
                commands.extend(update_states(commands_dlt, "deleted"))
            if commands_rep:
                commands.extend(update_states(commands_rep, "replaced"))
            if commands_mer:
                commands.extend(update_states(commands_mer, "replaced"))
        else:
            commands = []

        return commands, requests

    def _state_overridden(self, want, have, diff):
        """ The command generator when state is overridden

        :param want: the desired configuration as a dictionary
        :param obj_in_have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        commands_chg = self.filter_comands_to_change(want, have)
        commands_del = self.filter_comands_to_delete(commands_chg, have)
        requests = self.get_delete_interface_requests(commands_del, have)
        del_req_count = len(requests)
        if commands_del and del_req_count > 0:
            commands_dlt, commands_ovr = self.classify_delete_commands(commands_del)
            if commands_dlt:
                commands.extend(update_states(commands_dlt, "deleted"))
            if commands_ovr:
                commands.extend(update_states(commands_ovr, "overridden"))

        commands_over = self.filter_comands_to_change(diff, have)
        requests.extend(self.get_modify_interface_requests(commands_over, have))
        if commands_over and len(requests) > del_req_count:
            commands_over = update_states(commands_over, "overridden")
            commands.extend(commands_over)

        return commands, requests

    def _state_merged(self, want, have, diff):
        """ The command generator when state is merged

        :param want: the additive configuration as a dictionary
        :param obj_in_have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = self.filter_comands_to_change(diff, have)
        requests = self.get_modify_interface_requests(commands, have)
        if commands and len(requests) > 0:
            commands = update_states(commands, "merged")
        else:
            commands = []

        return commands, requests

    def _state_deleted(self, want, have, diff):
        """ The command generator when state is deleted

        :param want: the objects from which the configuration should be removed
        :param obj_in_have: the current configuration as a dictionary
        :param interface_type: interface type
        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        # if want is none, then delete all the interfaces
        if not want:
            commands = have
        else:
            commands = want

        commands_del = self.filter_comands_to_delete(commands, have)
        requests = self.get_delete_interface_requests(commands_del, have)

        if commands_del and len(requests) > 0:
            commands_dlt, commands_mer = self.classify_delete_commands(commands_del)
            commands = []
            if commands_dlt:
                commands.extend(update_states(commands_dlt, "deleted"))
            if commands_mer:
                commands.extend(update_states(commands_mer, "merged"))
        else:
            commands = []

        return commands, requests

    def filter_comands_to_delete(self, configs, have):
        commands = []

        for conf in configs:
            if self.is_this_delete_required(conf, have):
                intf_name = conf['name']

                temp_conf = dict()
                temp_conf['name'] = conf['name']
                if intf_name == 'Management0':
                    temp_conf['description'] = 'Management0'
                    temp_conf['mtu'] = 1500
                    temp_conf['enabled'] = True
                    temp_conf['speed'] = None
                    temp_conf['auto_negotiate'] = None
                    temp_conf['fec'] = None
                else:
                    temp_conf['description'] = ''
                    temp_conf['mtu'] = 9100
                    temp_conf['enabled'] = False
                    if intf_name.startswith('Eth'):
                        temp_conf['speed'] = self.retrieve_default_intf_speed(conf['name'])
                        temp_conf['auto_negotiate'] = False
                        temp_conf['fec'] = 'FEC_DISABLED'
                    else:
                        temp_conf['speed'] = None
                        temp_conf['auto_negotiate'] = None
                        temp_conf['fec'] = None
                temp_conf['advertised_speed'] = None
                commands.append(temp_conf)
        return commands

    def filter_comands_to_change(self, configs, have):
        commands = []
        if configs:
            for conf in configs:
                if self.is_this_change_required(conf, have):
                    commands.append(conf)
        return commands

    def get_modify_interface_requests(self, configs, have):
        self.delete_flag = False
        return self.get_interface_requests(configs, have)

    def get_delete_interface_requests(self, configs, have):
        self.delete_flag = True
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
                if name.startswith('Loopback'):
                    have_conf = next((cfg for cfg in have if cfg['name'] == name), None)
                    if not have_conf:
                        loopback_create_request = build_interfaces_create_request(name)
                        requests.append(loopback_create_request)

                config_request = self.build_create_common_config_request(conf)
                if config_request:
                    requests.append(config_request)

                fec_request = self.build_create_fec_request(conf)
                if fec_request:
                    requests.append(fec_request)

                speed_request = self.build_create_speed_request(conf)
                if speed_request:
                    requests.append(speed_request)

                autoneg_request = self.build_create_autoneg_request(conf)
                if autoneg_request:
                    requests.append(autoneg_request)

        return requests

    def retrieve_default_intf_speed(self, intf_name):

        eth_url = (url + '/openconfig-if-ethernet:ethernet/config/port-speed') % quote(intf_name, safe='')

        # Delete the speed
        method = DELETE
        request = {"path": eth_url, "method": method}
        if not self._module.check_mode:
            try:
                edit_config(self._module, to_request(self._module, request))
            except ConnectionError as exc:
                self._module.fail_json(msg=str(exc), code=exc.code)

        # Read the speed
        method = GET
        request = {"path": eth_url, "method": method}
        try:
            response = edit_config(self._module, to_request(self._module, request))
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)

        intf_speed = 'SPEED_DEFAULT'
        try:
            speed_str = response[0][1]["openconfig-if-ethernet:port-speed"]
        except Exception:
            raise Exception("The response from getting interfaces facts not formed as expected")

        intf_speed = speed_str.split(":", 1)[-1]

        return intf_speed

    def is_this_delete_required(self, conf, have):
        if conf['name'] == "eth0":
            return False
        intf = next((e_intf for e_intf in have if conf['name'] == e_intf['name']), None)
        if intf:
            if (intf['name'].startswith('Loopback') or
                not ((intf.get('description') is None or intf.get('description') == '') and
                     (intf.get('enabled') is None or intf.get('enabled') is False) and
                     (intf.get('mtu') is None or intf.get('mtu') == 9100) and
                     (intf.get('fec') is None or intf.get('fec') == 'FEC_DISABLED') and
                     (intf.get('speed') is None or
                         intf.get('speed') == self.retrieve_default_intf_speed(intf['name'])) and
                     (intf.get('auto_negotiate') is None or intf.get('auto_negotiate') is False) and
                     (intf.get('advertised_speed') is None or not intf.get('advertised_speed')))):
                return True
        return False

    def is_this_change_required(self, conf, have):
        if conf['name'] == "eth0":
            return False
        ret_flag = False
        intf = next((e_intf for e_intf in have if conf['name'] == e_intf['name']), None)
        if intf:
            # Check all parameter if any one is differen from existing
            for param in self.params:
                if conf.get(param) is not None and conf.get(param) != intf.get(param):
                    ret_flag = True
                    break
        # if given interface is not present
        else:
            ret_flag = True

        return ret_flag

    def build_create_common_config_request(self, conf):
        intf_name = conf['name']
        intf_conf = dict()
        request = dict()
        method = PATCH

        if not conf['name'].startswith('Loopback'):
            if conf.get('enabled') is not None:
                if conf.get('enabled'):
                    intf_conf['enabled'] = True
                else:
                    intf_conf['enabled'] = False
            if conf.get('description') is not None:
                intf_conf['description'] = conf['description']
            if conf.get('mtu') is not None:
                intf_conf['mtu'] = conf['mtu']

        if intf_conf:
            config_url = (url + '/config') % quote(intf_name, safe='')
            payload = {'openconfig-interfaces:config': intf_conf}
            request = {"path": config_url, "method": method, "data": payload}

        return request

    def build_create_fec_request(self, conf):
        intf_name = conf['name']
        eth_conf = dict()
        request = dict()
        method = PATCH

        if intf_name.startswith('Ethernet') and conf.get('fec') is not None:
            eth_conf['openconfig-if-ethernet-ext2:port-fec'] = 'openconfig-platform-types:' + conf['fec']
            eth_url = (url + '/openconfig-if-ethernet:ethernet/config') % quote(intf_name, safe='')
            payload = {'openconfig-if-ethernet:config': eth_conf}
            request = {"path": eth_url, "method": method, "data": payload}

        return request

    def build_create_speed_request(self, conf):
        intf_name = conf['name']
        eth_conf = dict()
        request = dict()

        if intf_name.startswith('Ethernet') and conf.get('speed') is not None:
            if conf.get('speed') == 'SPEED_DEFAULT':
                method = DELETE
                eth_url = (url + '/openconfig-if-ethernet:ethernet/config/port-speed') % quote(intf_name, safe='')
                request = {"path": eth_url, "method": method}
            else:
                method = PATCH
                eth_conf['port-speed'] = 'openconfig-if-ethernet:' + conf['speed']
                eth_url = (url + '/openconfig-if-ethernet:ethernet/config') % quote(intf_name, safe='')
                payload = {'openconfig-if-ethernet:config': eth_conf}
                request = {"path": eth_url, "method": method, "data": payload}

        return request

    def build_create_autoneg_request(self, conf):
        intf_name = conf['name']
        eth_conf = dict()
        request = dict()
        method = PATCH

        if intf_name.startswith('Ethernet'):
            eth_conf = dict()
            if conf.get('auto_negotiate') is not None:
                if conf.get('auto_negotiate'):
                    eth_conf['auto-negotiate'] = True
                else:
                    eth_conf['auto-negotiate'] = False
            if conf.get('advertised_speed') is not None:
                eth_conf['openconfig-if-ethernet-ext2:advertised-speed'] = ','.join(conf['advertised_speed'])

            if eth_conf:
                eth_url = (url + '/openconfig-if-ethernet:ethernet/config') % quote(intf_name, safe='')
                payload = {'openconfig-if-ethernet:config': eth_conf}
                request = {"path": eth_url, "method": method, "data": payload}

        return request

    def classify_delete_commands(self, configs):
        commands_del = []
        commands_mer = []

        if not configs:
            return commands_del, commands_mer

        for conf in configs:
            name = conf["name"]
            if name.startswith('Loopback'):
                commands_del.append(conf)
            else:
                commands_mer.append(conf)

        return commands_del, commands_mer
