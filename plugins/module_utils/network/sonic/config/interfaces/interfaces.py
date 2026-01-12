#
# -*- coding: utf-8 -*-
# © Copyright 2026 Dell Inc. or its subsidiaries. All Rights Reserved.
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


import re
import traceback
from copy import deepcopy
try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote
from ansible.module_utils._text import to_native
from ansible.module_utils.connection import ConnectionError
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
    retrieve_default_intf_speed,
    retrieve_port_group_info,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    get_diff,
    update_states,
    normalize_interface_name,
    remove_empties_from_list
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.formatted_diff_utils import (
    get_new_config,
    get_formatted_config_diff
)

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
eth_conf_url = "/openconfig-if-ethernet:ethernet/config"

port_num_regex = re.compile(r'[\d]{1,4}$')
loopback_attribute = ('description', 'enabled')
subintf_attribute = ('description', 'mtu', 'enabled', 'encapsulation')
non_eth_attribute = ('description', 'mtu', 'enabled')
eth_attribute = ('description', 'mtu', 'enabled', 'auto_negotiate', 'speed', 'fec', 'advertised_speed', 'unreliable_los', 'autoneg_mode')

subintf_attributes_default_value = {
    "enabled": True
}
non_eth_attributes_default_value = {
    "mtu": 9100,
    "enabled": True
}
eth_attributes_default_value = {
    "mtu": 9100,
    "enabled": False,
    "auto_negotiate": False,
    "fec": 'FEC_DISABLED',
    "unreliable_los": "UNRELIABLE_LOS_MODE_AUTO",
    "autoneg_mode": "AUTONEG_MODE_BAM"
}
default_intf_speeds = {}
port_group_interfaces = None


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
        warnings = []

        existing_interfaces_facts = self.get_interfaces_facts()
        commands, requests = self.set_config(existing_interfaces_facts, warnings)
        if commands and requests:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True

        result['commands'] = commands
        result['before'] = existing_interfaces_facts
        old_config = existing_interfaces_facts

        if self._module.check_mode:
            new_config = self.get_new_config(commands, existing_interfaces_facts)
            result['after_generated'] = new_config
        else:
            new_config = self.get_interfaces_facts()
            if result['changed']:
                result['after'] = new_config
        if self._module._diff:
            result['diff'] = get_formatted_config_diff(old_config, new_config, self._module._verbosity)

        return result

    def set_config(self, existing_interfaces_facts, warnings):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = remove_empties_from_list(self._module.params['config'])
        have = existing_interfaces_facts
        self.filter_out_mgmt_interface(want, have)

        new_want, new_have = self.validate_config(want, have, warnings)
        resp = self.set_state(new_want, new_have)
        return to_list(resp)

    def validate_config(self, want, have, warnings):
        new_want = deepcopy(want)
        new_have = deepcopy(have)
        normalize_interface_name(new_want, self._module)
        for cmd in new_have:
            # If auto_neg is true, ignore speed
            if cmd.get('auto_negotiate') is True:
                if cmd.get('speed'):
                    cmd.pop('speed')
            elif cmd.get('advertised_speed'):
                cmd.pop('advertised_speed')

        if new_want:
            for cmd in new_want:
                intf = next((cfg for cfg in new_have if cfg['name'] == cmd['name']), None)
                state = self._module.params['state']

                # Validate subinterface configuration
                cmd_keys_set = set(cmd.keys())
                diff_set = cmd_keys_set.difference(subintf_attribute).discard('name')
                subintf = self.get_subintf(cmd['name'])

                if subintf:
                    if diff_set:
                        self._module.fail_json(msg=f"Subinterface {cmd['name']} only supports the configuration "
                                               "of description, enabled, encapsulation, and mtu attributes.")
                elif cmd.get('encapsulation'):
                    self._module.fail_json(msg=f"Interface {cmd['name']} does not support the configuration of "
                                           "encapsulation. Configuration of encapsulation is only supported for subinterfaces.")

                if cmd.get('advertised_speed'):
                    cmd['advertised_speed'].sort()

                # Eth/VLAN/PortChannel
                if intf is None and not cmd['name'].startswith('Loopback') and not subintf:
                    self._module.fail_json(msg=f"Interface {cmd['name']} not found")

                if cmd['name'].startswith('Loopback'):
                    for attr in set(eth_attribute).difference(loopback_attribute):
                        cmd.pop(attr, None)
                elif not cmd['name'].startswith('Eth') and not subintf:
                    for attr in set(eth_attribute).difference(non_eth_attribute):
                        cmd.pop(attr, None)

                if state != "deleted":
                    if intf:
                        want_autoneg = cmd.get('auto_negotiate')
                        have_autoneg = intf.get('auto_negotiate')
                        want_speed = cmd.get('speed')
                        want_ads = cmd.get('advertised_speed')

                        if want_speed is not None:
                            if want_autoneg or (want_ads and have_autoneg):
                                warnings.append("Speed cannot be configured when autoneg is enabled")
                                cmd.pop('speed')

                        if want_ads is not None:
                            if ((not want_autoneg and state != 'merged')
                                    or (want_autoneg is False or (not want_autoneg and not have_autoneg))):
                                warnings.append("Advertised speed cannot be configured when autoneg is disabled")
                                cmd.pop('advertised_speed')

        return new_want, new_have

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
            commands, requests = self._state_merged(have, diff)
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
        commands, requests = self.get_replaced_overridden_config(want, have, "overridden")

        return commands, requests

    def _state_merged(self, have, diff):
        """ The command generator when state is merged

        :param want: the additive configuration as a dictionary
        :param obj_in_have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = self.filter_commands_to_change(diff, have)
        requests = self.get_interface_requests(commands, have)
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

    def filter_commands_to_change(self, configs, have):
        commands = []
        if configs:
            for conf in configs:
                if self.is_this_change_required(conf, have):
                    commands.append(conf)
        return commands

    def is_this_change_required(self, conf, have):
        intf = next((e_intf for e_intf in have if conf['name'] == e_intf['name']), None)
        if intf:
            # Check all parameter if any one is different from existing
            for param in eth_attribute:
                if conf.get(param) is not None and conf.get(param) != intf.get(param):
                    return True
        else:
            # if given interface is not present
            return True

        return False

    def get_interface_requests(self, configs, have):
        requests = []
        if not configs:
            return requests

        # Create URL and payload
        for conf in configs:
            name = conf['name']
            have_conf = next((cfg for cfg in have if cfg['name'] == name), {})

            # Create subinterface if it doesn't exist
            subintf = self.get_subintf(name)
            if subintf:
                attribute = subintf_attribute
                if not have_conf:
                    requests.append(self.build_create_subinterface_request(subintf[0], subintf[1]))
            # Create Loopback incase if not available in have
            elif name.startswith('Loopback'):
                attribute = loopback_attribute
                if not have_conf:
                    loopback_create_request = build_interfaces_create_request(name)
                    requests.append(loopback_create_request)
            else:
                attribute = eth_attribute if name.startswith('Eth') else non_eth_attribute

            for attr in attribute:
                if attr in conf:
                    c_attr = conf.get(attr)
                    h_attr = have_conf.get(attr)
                    attr_request = self.build_create_request(c_attr, h_attr, name, attr)
                    if attr_request:
                        requests.append(attr_request)
        return requests

    @staticmethod
    def get_subintf(intf_name):
        """This method returns the base interface and subinterface number if applicable"""
        subinterface_pattern = r"^([a-zA-Z0-9/\-]+)\.(\d+)$"
        match = re.match(subinterface_pattern, intf_name)
        if match:
            base_interface = match.group(1)
            subinterface_id = int(match.group(2))
            return base_interface, subinterface_id
        return []

    def build_create_subinterface_request(self, base_intf, subintf_id, c_attr=None, attr=None):
        """This method builds the subinterface request for modifcation"""
        subintf_url = (url + '/subinterfaces') % quote(base_intf, safe='')
        payload = {}

        if not attr:
            payload = {'openconfig-interfaces:subinterfaces': {'subinterface': [{'index': subintf_id, 'config': {'index': subintf_id}}]}}
        if attr:
            subintf_url += f'/subinterface={subintf_id}/'

            if attr in ('description', 'enabled', 'mtu'):
                subintf_url += 'config/'
                if attr == 'mtu':
                    subintf_url += 'openconfig-interfaces-ext:mtu'
                    payload = {'openconfig-interfaces-ext:mtu': c_attr}
                else:
                    subintf_url += attr
                    payload = {f'openconfig-interfaces:{attr}': c_attr}

            if attr == 'encapsulation':
                subintf_url += 'openconfig-vlan:vlan/config/vlan-id'
                vlan_id = c_attr.get('vlan_id')
                payload = {'openconfig-vlan:vlan-id': vlan_id}

        return {'path': subintf_url, 'method': PATCH, 'data': payload}

    def build_create_request(self, c_attr, h_attr, intf_name, attr):
        attributes_payload = {
            "speed": 'port-speed',
            "auto_negotiate": 'auto-negotiate',
            "fec": 'openconfig-if-ethernet-ext2:port-fec',
            "advertised_speed": 'openconfig-if-ethernet-ext2:advertised-speed',
            "unreliable_los": 'openconfig-if-ethernet-ext2:unreliable-los',
            "autoneg_mode": 'openconfig-if-ethernet-ext2:autoneg-mode'
        }

        config_url = (url + eth_conf_url) % quote(intf_name, safe='')
        payload = {'openconfig-if-ethernet:config': {}}
        payload_attr = attributes_payload.get(attr, attr)
        method = PATCH
        subintf = self.get_subintf(intf_name)

        # Handle attribute configuration for a subinterface
        if subintf:
            return self.build_create_subinterface_request(subintf[0], subintf[1], c_attr, attr)

        if attr in ('description', 'mtu', 'enabled'):
            config_url = (url + '/config') % quote(intf_name, safe='')
            payload = {'openconfig-interfaces:config': {}}
            payload['openconfig-interfaces:config'][payload_attr] = c_attr
            return {"path": config_url, "method": method, "data": payload}

        if attr in ('fec'):
            payload['openconfig-if-ethernet:config'][payload_attr] = 'openconfig-platform-types:' + c_attr
            return {"path": config_url, "method": method, "data": payload}

        if attr in ('autoneg_mode'):
            payload['openconfig-if-ethernet:config'][payload_attr] = 'openconfig-if-ethernet-ext2:' + c_attr
            return {"path": config_url, "method": method, "data": payload}

        payload['openconfig-if-ethernet:config'][payload_attr] = c_attr
        if attr == 'speed':
            port_group_info = retrieve_port_group_info(self._module, intf_name)
            if port_group_info.get('port_group_id'):
                port_group_id = port_group_info['port_group_id']
                valid_speeds = port_group_info['valid_speeds']
                self._module.fail_json(msg=("Please use the sonic_port_group module to change the speed. "
                                            f"Interface {intf_name} is in port-group ID {port_group_id}. The valid speeds "
                                            f"for port-group ID {port_group_id} are {valid_speeds}."))
            payload['openconfig-if-ethernet:config'][payload_attr] = 'openconfig-if-ethernet:' + c_attr
        if attr == 'advertised_speed':
            c_ads = c_attr if c_attr else []
            h_ads = h_attr if h_attr else []
            new_ads = list(set(h_ads).union(c_ads))
            if new_ads:
                payload['openconfig-if-ethernet:config'][payload_attr] = ','.join(new_ads)

        return {"path": config_url, "method": method, "data": payload}

    def handle_delete_interface_config(self, commands, have, delete_all=False):
        if not commands:
            return [], []

        commands_del, requests = [], []
        # Create URL and payload
        for conf in commands:
            name = conf['name']
            subintf = self.get_subintf(name)
            have_conf = next((cfg for cfg in have if cfg['name'] == name), None)
            if have_conf:
                lp_key_set = set(conf.keys())
                if delete_all or len(lp_key_set) == 1:
                    if name.startswith('Loopback'):
                        lpbk_url = url % quote(name, safe='')
                        request = {"path": lpbk_url, "method": DELETE}
                        requests.append(request)

                        commands_del.append({'name': name})
                        continue

                    # Subinterface 0 cannot be deleted
                    if subintf and subintf[1] != 0:
                        subintf_url = (url + f'/subinterfaces/subinterface={subintf[1]}') % quote(subintf[0], safe='')
                        requests.append({'path': subintf_url, 'method': DELETE})

                        commands_del.append({'name': name})
                        continue

                if len(lp_key_set) == 1:
                    conf = deepcopy(have_conf)

                del_cmd = {'name': name}
                if subintf:
                    attribute = subintf_attribute
                elif name.startswith('Eth'):
                    attribute = eth_attribute
                else:
                    attribute = non_eth_attribute

                for attr in attribute:
                    if attr in conf:
                        c_attr = conf.get(attr)
                        h_attr = have_conf.get(attr)
                        default_val = self.get_default_value(attr, h_attr, name)
                        if c_attr is not None and h_attr is not None and h_attr != default_val:
                            if attr == 'advertised_speed':
                                c_ads = c_attr if c_attr else []
                                h_ads = h_attr if h_attr else []
                                new_ads = list(set(h_attr).intersection(c_attr))
                                if new_ads:
                                    del_cmd.update({attr: new_ads})
                                    requests.append(self.build_delete_request(c_ads, h_ads, name, attr))
                            else:
                                del_cmd.update({attr: h_attr})
                                requests.append(self.build_delete_request(c_attr, h_attr, name, attr))
                if requests:
                    commands_del.append(del_cmd)

        return commands_del, requests

    def get_replaced_overridden_config(self, want, have, cur_state):
        commands, requests = [], []
        commands_add, commands_del = [], []
        requests_add, requests_del = [], []

        for conf in want:
            name = conf['name']
            intf = next((e_intf for e_intf in have if name == e_intf['name']), {})
            subintf = self.get_subintf(name)
            create_loopback, create_subintf = False, False

            if subintf:
                attribute = subintf_attribute
                if not intf:
                    create_subintf = True
                    requests.append(self.build_create_subinterface_request(subintf[0], subintf[1]))
            elif name.startswith('Loopback'):
                attribute = loopback_attribute
                if not intf:
                    create_loopback = True
                    requests.append(build_interfaces_create_request(name))
            else:
                attribute = eth_attribute if name.startswith('Eth') else non_eth_attribute

            add_conf, del_conf = {}, {}
            for attr in attribute:
                c_attr = conf.get(attr)
                h_attr = intf.get(attr)
                default_val = self.get_default_value(attr, h_attr, name)
                if attr != 'advertised_speed':
                    if c_attr is None and h_attr is not None and h_attr != default_val:
                        del_conf[attr] = h_attr
                        requests_del.append(self.build_delete_request(c_attr, h_attr, name, attr))
                    if c_attr is not None and c_attr != h_attr:
                        add_conf[attr] = c_attr
                        requests_add.append(self.build_create_request(c_attr, h_attr, name, attr))
                else:
                    c_ads = c_attr if c_attr else []
                    h_ads = h_attr if h_attr else []
                    new_ads = list(set(c_ads).difference(h_ads))
                    delete_ads = list(set(h_ads).difference(c_ads))
                    if new_ads:
                        add_conf[attr] = new_ads
                        requests_add.append(self.build_create_request(new_ads, h_attr, name, attr))
                    if delete_ads:
                        del_conf[attr] = delete_ads
                        requests_del.append(self.build_delete_request(delete_ads, h_attr, name, attr))

            if add_conf or create_loopback or create_subintf:
                add_conf['name'] = name
                commands_add.append(add_conf)

            if del_conf:
                del_conf['name'] = name
                commands_del.append(del_conf)

        if cur_state == "overridden":
            for have_conf in have:
                name = have_conf['name']
                in_want = next((conf for conf in want if conf['name'] == name), None)
                if not in_want:
                    del_conf = {}
                    delete_loopback, delete_subintf = False, False
                    subintf = self.get_subintf(name)

                    if name.startswith('Loopback'):
                        delete_loopback = True
                        lpbk_url = url % quote(name, safe='')
                        requests_del.append({'path': lpbk_url, "method": DELETE})
                    # Subinterface 0 cannot be deleted
                    elif subintf and subintf[1] != 0:
                        delete_subintf = True
                        subintf_url = (url + f'/subinterfaces/subinterface={subintf[1]}') % quote(subintf[0], safe='')
                        requests_del.append({'path': subintf_url, 'method': DELETE})
                    else:
                        attribute = eth_attribute if name.startswith('Eth') else non_eth_attribute
                        for attr in attribute:
                            h_attr = have_conf.get(attr)
                            if h_attr is not None and h_attr != self.get_default_value(attr, h_attr, name):
                                del_conf[attr] = h_attr
                                requests_del.append(self.build_delete_request([], h_attr, name, attr))

                    if del_conf or delete_loopback or delete_subintf:
                        del_conf['name'] = name
                        commands_del.append(del_conf)

        if len(requests_del) > 0:
            commands.extend(update_states(commands_del, "deleted"))
            requests.extend(requests_del)

        if len(requests_add) > 0:
            commands.extend(update_states(commands_add, cur_state))
            requests.extend(requests_add)

        return commands, requests

    def build_delete_subinterface_request(self, base_intf, subintf_id, attr):
        """This method builds the subinterface request for deletion"""
        subintf_url = (url + f'/subinterfaces/subinterface={subintf_id}/') % quote(base_intf, safe='')

        if attr in ('description', 'enabled', 'mtu'):
            subintf_url += 'config/'
            if attr == 'description':
                subintf_url += attr
            if attr == 'mtu':
                subintf_url += 'openconfig-interfaces-ext:mtu'
            elif attr == 'enabled':
                subintf_url += attr
                payload = {f'openconfig-interfaces:{attr}': True}
                return {'path': subintf_url, 'method': PATCH, 'data': payload}

        if attr == 'encapsulation':
            subintf_url += 'openconfig-vlan:vlan/config/vlan-id'

        return {'path': subintf_url, 'method': DELETE}

    def build_delete_request(self, c_attr, h_attr, intf_name, attr):
        method = DELETE
        attributes_payload = {
            "speed": 'port-speed',
            "auto_negotiate": 'auto-negotiate',
            "fec": 'openconfig-if-ethernet-ext2:port-fec',
            "advertised_speed": 'openconfig-if-ethernet-ext2:advertised-speed',
            "unreliable_los": 'openconfig-if-ethernet-ext2:unreliable-los',
            "autoneg_mode": 'openconfig-if-ethernet-ext2:autoneg-mode'
        }

        config_url = (url + eth_conf_url) % quote(intf_name, safe='')
        payload = {'openconfig-if-ethernet:config': {}}
        payload_attr = attributes_payload.get(attr, attr)
        subintf = self.get_subintf(intf_name)

        # Handle attribute deletion for a subinterface
        if subintf:
            return self.build_delete_subinterface_request(subintf[0], subintf[1], attr)

        if attr in ('description', 'mtu'):
            attr_url = "/config/" + payload_attr
            config_url = (url + attr_url) % quote(intf_name, safe='')
            return {"path": config_url, "method": method}

        if attr in ('enabled'):
            attr_url = "/config/" + payload_attr
            config_url = (url + attr_url) % quote(intf_name, safe='')
            attributes_default_value = eth_attributes_default_value if intf_name.startswith('Eth') \
                else non_eth_attributes_default_value
            ena_payload = {}
            ena_payload[attr] = attributes_default_value[attr]
            return {"path": config_url, "method": PATCH, "data": ena_payload}

        if attr in ('fec'):
            payload_attr = attributes_payload[attr]
            payload['openconfig-if-ethernet:config'][payload_attr] = 'FEC_DISABLED'
            return {"path": config_url, "method": PATCH, "data": payload}

        if attr in ('unreliable_los'):
            payload_attr = attributes_payload[attr]
            payload['openconfig-if-ethernet:config'][payload_attr] = 'UNRELIABLE_LOS_MODE_AUTO'
            return {"path": config_url, "method": PATCH, "data": payload}

        if attr in ('autoneg_mode'):
            payload_attr = attributes_payload[attr]
            config_url = config_url + "/" + payload_attr
            return {"path": config_url, "method": method}

        payload_attr = attributes_payload[attr]
        if attr == 'auto_negotiate':
            # For auto-negotiate, we assign value to False since deleting the attribute will become None if deleted
            # In case, if auto-negotiate is disabled, both speed and advertised_speed will have default value.
            payload['openconfig-if-ethernet:config'][payload_attr] = False
            return {"path": config_url, "method": PATCH, "data": payload}

        if attr == 'speed':
            attr_url = eth_conf_url + "/" + attributes_payload[attr]
            del_config_url = (url + attr_url) % quote(intf_name, safe='')
            return {"path": del_config_url, "method": method}

        if attr == 'advertised_speed':
            new_ads = list(set(h_attr).difference(c_attr))
            if new_ads:
                payload['openconfig-if-ethernet:config'][payload_attr] = ','.join(new_ads)
                return {"path": config_url, "method": PATCH, "data": payload}

            attr_url = eth_conf_url + "/" + attributes_payload[attr]
            del_config_url = (url + attr_url) % quote(intf_name, safe='')
            return {"path": del_config_url, "method": method}

        return {}

    # Utils
    def get_default_value(self, attr, h_attr, intf_name):
        if attr == 'speed':
            default_val = self._retrieve_default_intf_speed(intf_name)
            if default_val == 'SPEED_DEFAULT':
                # Incase if the port belongs to port-group, we can not able to delete the speed
                default_val = h_attr
            return default_val
        if self.get_subintf(intf_name) or intf_name.startswith('Loopback'):
            attributes_default_value = subintf_attributes_default_value
        elif intf_name.startswith('Eth'):
            attributes_default_value = eth_attributes_default_value
        else:
            attributes_default_value = non_eth_attributes_default_value
        return attributes_default_value.get(attr)

    def filter_out_mgmt_interface(self, want, have):
        if want:
            mgmt_intf = next((intf for intf in want if intf['name'] == 'Management0'), None)
            if mgmt_intf:
                self._module.fail_json(msg='Management interface should not be configured.')

        for intf in have:
            if intf['name'] == 'Management0':
                have.remove(intf)
                break

    def _retrieve_default_intf_speed(self, intf_name):
        # To avoid multiple get requests
        port_group_info = retrieve_port_group_info(self._module, intf_name)
        # Check if interface is in a port-group
        if port_group_info.get('port_group_id'):
            return "SPEED_DEFAULT"

        if default_intf_speeds.get(intf_name) is None:
            default_intf_speeds[intf_name] = retrieve_default_intf_speed(self._module, intf_name)
        return default_intf_speeds[intf_name]

    def post_process_generated_config(self, config):
        """Handle post processing for generated configuration"""
        for intf in config:
            intf_name = intf['name']
            subintf = self.get_subintf(intf_name)

            if subintf or intf_name.startswith('Loopback'):
                attributes_default_value = subintf_attributes_default_value
            elif intf_name.startswith('Eth'):
                attributes_default_value = eth_attributes_default_value
            else:
                attributes_default_value = non_eth_attributes_default_value

            for attr in attributes_default_value:
                if attr not in intf:
                    intf[attr] = attributes_default_value[attr]

        return config

    def __derive_interface_config_delete_op(self, key_set, command, exist_conf):
        """Returns new interface configuration for delete operation"""
        new_conf = exist_conf
        intf_name = command['name']
        subintf = self.get_subintf(intf_name)

        if len(command) == 1 and (subintf or intf_name.startswith('Loopback')):
            return True, []
        for attr in command:
            if attr == 'name':
                continue
            if attr == "speed":
                new_conf[attr] = default_intf_speeds[intf_name]
            elif attr == "advertised_speed":
                if new_conf.get("advertised_speed") is not None:
                    new_conf[attr] = list(set(new_conf[attr]).difference(command[attr]))
                    if not new_conf[attr]:
                        new_conf.pop(attr)
            elif attr == "auto_negotiate":
                new_conf[attr] = False
                if new_conf.get('advertised_speed') is not None:
                    new_conf.pop('advertised_speed')
            else:
                if subintf or intf_name.startswith('Loopback'):
                    attributes_default_value = subintf_attributes_default_value
                elif intf_name.startswith('Eth'):
                    attributes_default_value = eth_attributes_default_value
                else:
                    attributes_default_value = non_eth_attributes_default_value
                if attributes_default_value.get(attr) is not None:
                    new_conf[attr] = attributes_default_value.get(attr)
                else:
                    new_conf.pop(attr, None)

        return True, new_conf

    @staticmethod
    def interface_sort_key(item):
        """Splits interface name for numeric comparison"""
        name = item.get("name", "")
        return [int(c) if c.isdigit() else c.lower() for c in re.split(r'(\d+)', name)]

    def get_new_config(self, commands, have):
        """Returns generated configuration based on commands and
            existing configuration"""
        key_set = [
            {'config': {'name': '', '__delete_op': self.__derive_interface_config_delete_op}}
        ]
        new_config = self.post_process_generated_config(get_new_config(commands, have, key_set))
        new_config.sort(key=self.interface_sort_key)

        return new_config
