#
# -*- coding: utf-8 -*-
# Copyright 2022 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_lldp_interfaces class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from __future__ import absolute_import, division, print_function
__metaclass__ = type
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import Facts

from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    get_diff,
    update_states
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible.module_utils.connection import ConnectionError
import re
import copy

PATCH = 'patch'
DELETE = 'delete'

TEST_KEYS = [
    {'config': {'name': ''}}
]


class Lldp_interfaces(ConfigBase):
    """
    The sonic_lldp_interfaces class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'lldp_interfaces',
    ]
    lldp_interfaces_path = 'data/openconfig-lldp:lldp/interfaces'

    lldp_intf_path = 'data/openconfig-lldp:lldp/interfaces/interface={intf_name}'
    lldp_intf_config_path = {
        'enable': lldp_intf_path + '/config/enabled',
        'ipv4_management_address': lldp_intf_path + '/config/openconfig-lldp-ext:management-address-ipv4',
        'ipv6_management_address': lldp_intf_path + '/config/openconfig-lldp-ext:management-address-ipv6',
        'mode': lldp_intf_path + '/config/openconfig-lldp-ext:mode',
        'suppress_tlv': lldp_intf_path + '/config/openconfig-lldp-ext:suppress-tlv-advertisement',
        'allowed_vlan': lldp_intf_path + '/config/openconfig-lldp-ext:allowed-vlans',
        'vlan_name_tlv_count': lldp_intf_path + '/config/openconfig-lldp-ext:vlan-name-tlv-count',
        'suppress_tlv_delete': lldp_intf_path + '/config/openconfig-lldp-ext:suppress-tlv-advertisement={med_tlv_select}'
    }

    def __init__(self, module):
        super(Lldp_interfaces, self).__init__(module)

    def get_lldp_interfaces_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        lldp_interfaces_facts = facts['ansible_network_resources'].get('lldp_interfaces')
        if not lldp_interfaces_facts:
            return []
        return lldp_interfaces_facts

    def convert_vlan_list(self, vlan_lst):
        """
        Convert a list of VLANs to a new list.
        :rtype: vlan_lst (list): A list of VLANs.
        :returns:A new list containing the converted VLANs.
        """
        result = []
        for vlan in vlan_lst:
            try:
                result.append(int(vlan))
            except ValueError:
                result.append(vlan)
        return result

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """

        result = {'changed': False}
        warnings = []

        existing_lldp_interfaces_facts = self.get_lldp_interfaces_facts()
        commands, requests = self.set_config(existing_lldp_interfaces_facts)
        if commands:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True

        changed_lldp_interfaces_facts = self.get_lldp_interfaces_facts()

        result['before'] = existing_lldp_interfaces_facts
        if result['changed']:
            result['after'] = changed_lldp_interfaces_facts

        result['commands'] = commands
        result['warnings'] = warnings
        return result

    def set_config(self, existing_lldp_interfaces_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']
        have = existing_lldp_interfaces_facts
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
        diff = get_diff(want, have)
        if state == 'deleted':
            commands, requests = self._state_deleted(want, have, diff)
        elif state == 'merged':
            commands, requests = self._state_merged(diff)
        elif state == 'replaced':
            commands, requests = self._state_replaced(diff, want, have)
        elif state == 'overridden':
            commands, requests = self._state_overridden(want, have, diff)
        return commands, requests

    def _state_merged(self, diff):
        """ The command generator when state is merged
        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = diff
        requests = []
        for command in commands:
            requests.extend(self.get_modify_specific_lldp_interfaces_param_requests(command))
        if commands and len(requests) > 0:
            commands = update_states(commands, 'merged')
        else:
            commands = []

        return commands, requests

    def _state_deleted(self, want, have, diff):
        """ The command generator when state is deleted
        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        commands = []
        requests = []
        if not want:
            commands = have
            requests.extend(self.get_delete_lldp_interfaces_complete_requests(commands))
        else:
            commands = get_diff(want, diff)
            for command in commands:
                requests.extend(self.get_delete_specific_lldp_interfaces_param_requests(command, have))

        if len(requests) == 0:
            commands = []

        if commands:
            commands = update_states(commands, "deleted")

        return commands, requests

    def _state_replaced(self, diff, want, have):
        """ The command generator when state is replaced

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        requests = []
        del_commands = []
        add_commands = []

        have_interfaces = self.get_interface_names(have)
        want_interfaces = self.get_interface_names(want)
        interfaces_to_replace = have_interfaces.intersection(want_interfaces)

        del_diff = get_diff(self.remove_default_entries(have), want, TEST_KEYS)
        for cmd in del_diff:
            if cmd['name'] in interfaces_to_replace:
                del_commands.append(cmd)

        if del_commands:
            commands = update_states(del_commands, 'deleted')
            for cmd in del_commands:
                requests.extend(self.get_delete_specific_lldp_interfaces_param_requests(cmd, have))

        add_diff = get_diff(want, have, TEST_KEYS)
        for cmd in add_diff:
            add_commands.append(cmd)

        if add_commands:
            commands.extend(update_states(add_commands, 'replaced'))
            for cmd in add_commands:
                requests.extend(self.get_modify_specific_lldp_interfaces_param_requests(cmd))

        return commands, requests

    def _state_overridden(self, want, have, diff):
        """ The command generator when state is overridden

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        requests = []
        del_commands = []
        have_interfaces = self.get_interface_names(have)
        want_interfaces = self.get_interface_names(want)
        interfaces_to_delete = have_interfaces.difference(want_interfaces)
        interfaces_to_override = have_interfaces.intersection(want_interfaces)
        del_diff = get_diff(self.remove_default_entries(have), want, TEST_KEYS)
        for cmd in del_diff:
            if cmd['name'] in interfaces_to_delete:
                del_commands.append({'name': cmd['name']})
            elif cmd['name'] in interfaces_to_override:
                del_commands.append(cmd)
        if del_commands:
            commands = update_states(del_commands, 'deleted')
            for cmd in del_commands:
                requests.extend(self.get_delete_specific_lldp_interfaces_param_requests(cmd, have))

        diff = get_diff(want, have)
        if diff:
            commands.extend(update_states(diff, 'overridden'))
            for cmd in diff:
                requests.extend(self.get_modify_specific_lldp_interfaces_param_requests(cmd))

        return commands, requests

    def get_delete_lldp_interfaces_complete_requests(self, have):
        """Get requests to delete all existing LLDP global
        configurations in the chassis
        """
        default_dict = {
            'tlv_select':
            {
                'power_management': True,
                'port_vlan_id': True,
                'vlan_name': True,
                'link_aggregation': True,
                'max_frame_size': True
            },
            'med_tlv_select':
            {
                'network_policy': True,
                'power_management': True
            },
            'vlan_name_tlv':
            {
                'max_tlv_count': 10
            },
            'enable': True
        }
        requests = []
        conf = copy.deepcopy(have)
        for cfg in conf:
            del cfg['name']
            if default_dict != cfg:
                return [{'path': self.lldp_interfaces_path, 'method': DELETE}]
        return requests

    def get_modify_specific_lldp_interfaces_param_requests(self, command):
        """Get requests to modify specific LLDP Global configurations
        based on the command specified for the interface
        """
        requests = []

        if not command:
            return requests
        name = command['name']
        ipv6_mgmt_addr = ''
        ipv4_mgmt_addr = ''
        allowed_vlan = ''
        max_tlv_count = ''
        if re.search('Eth', name):
            if 'mode' in command and command['mode'] is not None:
                payload = {'openconfig-lldp-ext:mode': command['mode'].upper()}
                url = self.lldp_intf_config_path['mode'].format(intf_name=name)
                requests.append({'path': url, 'method': PATCH, 'data': payload})
            if 'enable' in command and command['enable'] is not None:
                payload = {'openconfig-lldp:enabled': command['enable']}
                url = self.lldp_intf_config_path['enable'].format(intf_name=name)
                requests.append({'path': url, 'method': PATCH, 'data': payload})
            if 'tlv_set' in command and command['tlv_set'] is not None:
                if 'ipv4_management_address' in command['tlv_set'] and command['tlv_set']['ipv4_management_address'] is not None:
                    ipv4_mgmt_addr = command['tlv_set']['ipv4_management_address']
                if 'ipv6_management_address' in command['tlv_set'] and command['tlv_set']['ipv6_management_address'] is not None:
                    ipv6_mgmt_addr = command['tlv_set']['ipv6_management_address']
                if ipv4_mgmt_addr:
                    payload = {'openconfig-lldp-ext:management-address-ipv4': ipv4_mgmt_addr}
                    url = self.lldp_intf_config_path['ipv4_management_address'].format(intf_name=name)
                    requests.append({'path': url, 'method': PATCH, 'data': payload})
                if ipv6_mgmt_addr:
                    payload = {'openconfig-lldp-ext:management-address-ipv6': ipv6_mgmt_addr}
                    url = self.lldp_intf_config_path['ipv6_management_address'].format(intf_name=name)
                    requests.append({'path': url, 'method': PATCH, 'data': payload})
            if 'vlan_name_tlv' in command and command['vlan_name_tlv'] is not None:
                if 'allowed_vlans' in command['vlan_name_tlv'] and command['vlan_name_tlv']['allowed_vlans'] is not None:
                    allowed_vlan = command['vlan_name_tlv']['allowed_vlans']
                    if allowed_vlan:
                        payload = {'openconfig-lldp-ext:allowed-vlans': self.convert_vlan_list(allowed_vlan)}
                        url = self.lldp_intf_config_path['allowed_vlan'].format(intf_name=name)
                        requests.append({'path': url, 'method': PATCH, 'data': payload})
                if 'max_tlv_count' in command['vlan_name_tlv'] and command['vlan_name_tlv']['max_tlv_count'] is not None:
                    max_tlv_count = command['vlan_name_tlv']['max_tlv_count']
                    if max_tlv_count:
                        payload = {'openconfig-lldp-ext:vlan-name-tlv-count': max_tlv_count}
                        url = self.lldp_intf_config_path['vlan_name_tlv_count'].format(intf_name=name)
                        requests.append({'path': url, 'method': PATCH, 'data': payload})
            if 'tlv_select' in command and command['tlv_select'] is not None:
                if 'power_management' in command['tlv_select'] and command['tlv_select']['power_management'] is not None:
                    tlv1 = command['tlv_select']['power_management']
                    if tlv1:
                        url = self.lldp_intf_config_path['suppress_tlv_delete'].format(intf_name=name, med_tlv_select="MDI_POWER")
                        requests.append({'path': url, 'method': DELETE})
                    elif tlv1 is False:
                        payload = {"openconfig-lldp-ext:suppress-tlv-advertisement": ["MDI_POWER"]}
                        url = self.lldp_intf_config_path['suppress_tlv'].format(intf_name=name)
                        requests.append({'path': url, 'method': PATCH, 'data': payload})
                if 'port_vlan_id' in command['tlv_select'] and command['tlv_select']['port_vlan_id'] is not None:
                    tlv2 = command['tlv_select']['port_vlan_id']
                    if tlv2:
                        url = self.lldp_intf_config_path['suppress_tlv_delete'].format(intf_name=name, med_tlv_select="PORT_VLAN_ID")
                        requests.append({'path': url, 'method': DELETE})
                    elif tlv2 is False:
                        payload = {"openconfig-lldp-ext:suppress-tlv-advertisement": ["PORT_VLAN_ID"]}
                        url = self.lldp_intf_config_path['suppress_tlv'].format(intf_name=name)
                        requests.append({'path': url, 'method': PATCH, 'data': payload})
                if 'vlan_name' in command['tlv_select'] and command['tlv_select']['vlan_name'] is not None:
                    tlv3 = command['tlv_select']['vlan_name']
                    if tlv3:
                        url = self.lldp_intf_config_path['suppress_tlv_delete'].format(intf_name=name, med_tlv_select="VLAN_NAME")
                        requests.append({'path': url, 'method': DELETE})
                    elif tlv3 is False:
                        payload = {"openconfig-lldp-ext:suppress-tlv-advertisement": ["VLAN_NAME"]}
                        url = self.lldp_intf_config_path['suppress_tlv'].format(intf_name=name)
                        requests.append({'path': url, 'method': PATCH, 'data': payload})
                if 'link_aggregation' in command['tlv_select'] and command['tlv_select']['link_aggregation'] is not None:
                    tlv4 = command['tlv_select']['link_aggregation']
                    if tlv4:
                        url = self.lldp_intf_config_path['suppress_tlv_delete'].format(intf_name=name, med_tlv_select="LINK_AGGREGATION")
                        requests.append({'path': url, 'method': DELETE})
                    elif tlv4 is False:
                        payload = {"openconfig-lldp-ext:suppress-tlv-advertisement": ["LINK_AGGREGATION"]}
                        url = self.lldp_intf_config_path['suppress_tlv'].format(intf_name=name)
                        requests.append({'path': url, 'method': PATCH, 'data': payload})
                if 'max_frame_size' in command['tlv_select'] and command['tlv_select']['max_frame_size'] is not None:
                    tlv5 = command['tlv_select']['max_frame_size']
                    if tlv5:
                        url = self.lldp_intf_config_path['suppress_tlv_delete'].format(intf_name=name, med_tlv_select="MAX_FRAME_SIZE")
                        requests.append({'path': url, 'method': DELETE})
                    elif tlv5 is False:
                        payload = {"openconfig-lldp-ext:suppress-tlv-advertisement": ["MAX_FRAME_SIZE"]}
                        url = self.lldp_intf_config_path['suppress_tlv'].format(intf_name=name)
                        requests.append({'path': url, 'method': PATCH, 'data': payload})
            if 'med_tlv_select' in command and command['med_tlv_select'] is not None:
                if 'power_management' in command['med_tlv_select'] and command['med_tlv_select']['power_management'] is not None:
                    med_tlv1 = command['med_tlv_select']['power_management']
                    if med_tlv1 is True:
                        url = self.lldp_intf_config_path['suppress_tlv_delete'].format(intf_name=name, med_tlv_select="MED_EXT_MDI_POWER")
                        requests.append({'path': url, 'method': DELETE})
                    elif med_tlv1 is False:
                        payload = {"openconfig-lldp-ext:suppress-tlv-advertisement": ["MED_EXT_MDI_POWER"]}
                        url = self.lldp_intf_config_path['suppress_tlv'].format(intf_name=name)
                        requests.append({'path': url, 'method': PATCH, 'data': payload})
                if 'network_policy' in command['med_tlv_select'] and command['med_tlv_select']['network_policy'] is not None:
                    med_tlv2 = command['med_tlv_select']['network_policy']
                    if med_tlv2 is True:
                        url = self.lldp_intf_config_path['suppress_tlv_delete'].format(intf_name=name, med_tlv_select="MED_NETWORK_POLICY")
                        requests.append({'path': url, 'method': DELETE})
                    elif med_tlv2 is False:
                        payload = {"openconfig-lldp-ext:suppress-tlv-advertisement": ["MED_NETWORK_POLICY"]}
                        url = self.lldp_intf_config_path['suppress_tlv'].format(intf_name=name)
                        requests.append({'path': url, 'method': PATCH, 'data': payload})
        return requests

    def get_delete_specific_lldp_interfaces_param_requests(self, command, config):
        """Get requests to delete specific LLDP global configurations
        based on the command specified for the interface
        """
        requests = []
        conf = copy.deepcopy(config)

        default_dict = {'tlv_select': {'power_management': True}, 'med_tlv_select': {'network_policy': True, 'power_management': True}, 'enable': True}

        if not command:
            return requests
        name = command['name']

        if 'mode' in command and command['mode'] is not None:
            url = self.lldp_intf_config_path['mode'].format(intf_name=name)
            requests.append({'path': url, 'method': DELETE})

        if re.search('Eth', name):
            if 'enable' in command and command['enable'] is not None:
                if command['enable']:
                    payload = {'openconfig-lldp:enabled': False}
                else:
                    payload = {'openconfig-lldp:enabled': True}
                url = self.lldp_intf_config_path['enable'].format(intf_name=name)
                requests.append({'path': url, 'method': PATCH, 'data': payload})
            if 'tlv_set' in command and command['tlv_set'] is not None:
                if command['tlv_set'].get('ipv4_management_address') is not None:
                    url = self.lldp_intf_config_path['ipv4_management_address'].format(intf_name=name)
                    requests.append({'path': url, 'method': DELETE})
                if command['tlv_set'].get('ipv6_management_address') is not None:
                    url = self.lldp_intf_config_path['ipv6_management_address'].format(intf_name=name)
                    requests.append({'path': url, 'method': DELETE})
            if 'vlan_name_tlv' in command and command['vlan_name_tlv'] is not None:
                if 'allowed_vlans' in command['vlan_name_tlv'] and command['vlan_name_tlv']['allowed_vlans'] is not None:
                    allowed_vlan = command['vlan_name_tlv']['allowed_vlans']
                    url = self.lldp_intf_config_path['allowed_vlan'].format(intf_name=name)
                    if len(allowed_vlan) > 0:
                        # Append vlan list to url, if allowed_vlan list is not
                        url += '={allowed_vlan}'.format(allowed_vlan='%2C'.join(allowed_vlan))
                    requests.append({'path': url, 'method': DELETE})
                if command['vlan_name_tlv'].get('max_tlv_count') is not None:
                    url = self.lldp_intf_config_path['vlan_name_tlv_count'].format(intf_name=name)
                    requests.append({'path': url, 'method': DELETE})
            if 'tlv_select' in command and command['tlv_select'] is not None:
                if 'power_management' in command['tlv_select'] and command['tlv_select']['power_management'] is not None:
                    tlv1 = command['tlv_select']['power_management']
                    if tlv1:
                        payload = {"openconfig-lldp-ext:suppress-tlv-advertisement": ["MDI_POWER"]}
                        url = self.lldp_intf_config_path['suppress_tlv'].format(intf_name=name)
                        requests.append({'path': url, 'method': PATCH, 'data': payload})
                    elif tlv1 is False:
                        url = self.lldp_intf_config_path['suppress_tlv_delete'].format(intf_name=name, med_tlv_select="MDI_POWER")
                        requests.append({'path': url, 'method': DELETE})
                if 'port_vlan_id' in command['tlv_select'] and command['tlv_select']['port_vlan_id'] is not None:
                    tlv2 = command['tlv_select']['port_vlan_id']
                    if tlv2:
                        payload = {"openconfig-lldp-ext:suppress-tlv-advertisement": ["PORT_VLAN_ID"]}
                        url = self.lldp_intf_config_path['suppress_tlv'].format(intf_name=name)
                        requests.append({'path': url, 'method': PATCH, 'data': payload})
                    elif tlv2 is False:
                        url = self.lldp_intf_config_path['suppress_tlv_delete'].format(intf_name=name, med_tlv_select="PORT_VLAN_ID")
                        requests.append({'path': url, 'method': DELETE})
                if 'vlan_name' in command['tlv_select'] and command['tlv_select']['vlan_name'] is not None:
                    tlv3 = command['tlv_select']['vlan_name']
                    if tlv3:
                        payload = {"openconfig-lldp-ext:suppress-tlv-advertisement": ["VLAN_NAME"]}
                        url = self.lldp_intf_config_path['suppress_tlv'].format(intf_name=name)
                        requests.append({'path': url, 'method': PATCH, 'data': payload})
                    elif tlv3 is False:
                        url = self.lldp_intf_config_path['suppress_tlv_delete'].format(intf_name=name, med_tlv_select="VLAN_NAME")
                        requests.append({'path': url, 'method': DELETE})
                if 'link_aggregation' in command['tlv_select'] and command['tlv_select']['link_aggregation'] is not None:
                    tlv4 = command['tlv_select']['link_aggregation']
                    if tlv4:
                        payload = {"openconfig-lldp-ext:suppress-tlv-advertisement": ["LINK_AGGREGATION"]}
                        url = self.lldp_intf_config_path['suppress_tlv'].format(intf_name=name)
                        requests.append({'path': url, 'method': PATCH, 'data': payload})
                    elif tlv4 is False:
                        url = self.lldp_intf_config_path['suppress_tlv_delete'].format(intf_name=name, med_tlv_select="LINK_AGGREGATION")
                        requests.append({'path': url, 'method': DELETE})
                if 'max_frame_size' in command['tlv_select'] and command['tlv_select']['max_frame_size'] is not None:
                    tlv5 = command['tlv_select']['max_frame_size']
                    if tlv5:
                        payload = {"openconfig-lldp-ext:suppress-tlv-advertisement": ["MAX_FRAME_SIZE"]}
                        url = self.lldp_intf_config_path['suppress_tlv'].format(intf_name=name)
                        requests.append({'path': url, 'method': PATCH, 'data': payload})
                    elif tlv5 is False:
                        url = self.lldp_intf_config_path['suppress_tlv_delete'].format(intf_name=name, med_tlv_select="MAX_FRAME_SIZE")
                        requests.append({'path': url, 'method': DELETE})
            if 'med_tlv_select' in command and command['med_tlv_select'] is not None:
                if 'power_management' in command['med_tlv_select'] and command['med_tlv_select']['power_management'] is not None:
                    med_tlv1 = command['med_tlv_select']['power_management']
                    if med_tlv1 is True:
                        payload = {"openconfig-lldp-ext:suppress-tlv-advertisement": ["MED_EXT_MDI_POWER"]}
                        url = self.lldp_intf_config_path['suppress_tlv'].format(intf_name=name)
                        requests.append({'path': url, 'method': PATCH, 'data': payload})
                    elif med_tlv1 is False:
                        url = self.lldp_intf_config_path['suppress_tlv_delete'].format(intf_name=name, med_tlv_select="MED_EXT_MDI_POWER")
                        requests.append({'path': url, 'method': DELETE})
                if 'network_policy' in command['med_tlv_select'] and command['med_tlv_select']['network_policy'] is not None:
                    med_tlv2 = command['med_tlv_select']['network_policy']
                    if med_tlv2 is True:
                        payload = {"openconfig-lldp-ext:suppress-tlv-advertisement": ["MED_NETWORK_POLICY"]}
                        url = self.lldp_intf_config_path['suppress_tlv'].format(intf_name=name)
                        requests.append({'path': url, 'method': PATCH, 'data': payload})
                    elif med_tlv2 is False:
                        url = self.lldp_intf_config_path['suppress_tlv_delete'].format(intf_name=name, med_tlv_select="MED_NETWORK_POLICY")
                        requests.append({'path': url, 'method': DELETE})
            if len(requests) == 0 and command['name'] is not None:
                for line in conf:
                    if line['name'] == name:
                        del line['name']
                        if default_dict != line:
                            url = self.lldp_intf_path.format(intf_name=name)
                            requests.append({'path': url, 'method': DELETE})
        return requests

    @staticmethod
    def get_interface_names(config_list):
        """Get a set of interface names available in the given
        config_list dict
        """
        interface_names = set()
        for config in config_list:
            interface_names.add(config['name'])

        return interface_names

    def remove_default_entries(self, data):
        new_data = []
        if data:
            default_val_dict = {
                'enable': True,
                'med_tlv_select': {'network_policy': True, 'power_management': True},
                'tlv_select': {'power_management': True, 'port_vlan_id': True, 'vlan_name': True, 'link_aggregation': True, 'max_frame_size': True},
                'vlan_name_tlv': {'max_tlv_count': 10}
            }
            for intf_conf in data:
                default_val_dict['name'] = intf_conf['name']
                diff = get_diff(intf_conf, default_val_dict)
                if diff:
                    new_data.append(diff)
        return new_data
