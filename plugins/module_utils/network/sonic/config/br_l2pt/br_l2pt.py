#
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_br_l2pt class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    get_diff,
    remove_none,
    get_ranges_in_list,
    update_states
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.formatted_diff_utils import (
    __DELETE_CONFIG_IF_NO_SUBCONFIG,
    get_new_config,
    get_formatted_config_diff
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import Facts
from ansible.module_utils.connection import ConnectionError
import re
from copy import deepcopy

PATCH = 'patch'
PUT = 'put'
DELETE = 'delete'

TEST_KEYS = [
    {'config': {'name': ''}}
]

TEST_KEYS_generate_config_merged = [
    {'config': {'name': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}}
]

class Br_l2pt(ConfigBase):
    """
    The sonic_br_l2pt class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'br_l2pt',
    ]

    all_interfaces_path = 'data/openconfig-interfaces:interfaces'
    br_l2pt_intf_path = all_interfaces_path + '/interface={intf_name}'
    br_l2pt_intf_config_params_path = br_l2pt_intf_path + '/openconfig-interfaces-ext:bridge-l2pt-params'
    br_l2pt_intf_config_path = br_l2pt_intf_path + '/openconfig-interfaces-ext:bridge-l2pt-params/bridge-l2pt-param'
    br_l2pt_intf_proto_path = br_l2pt_intf_path + '/openconfig-interfaces-ext:bridge-l2pt-params/bridge-l2pt-param={protocol}'
    br_l2pt_intf_vlan_id_path = br_l2pt_intf_path + '/openconfig-interfaces-ext:bridge-l2pt-params/bridge-l2pt-param={protocol}/config/vlan-ids={vlan_ids}'
    payload_header = "openconfig-interfaces-ext:bridge-l2pt-param"
    protocols = ['LLDP', 'LACP', 'STP', 'CDP']

    def __init__(self, module):
        super(Br_l2pt, self).__init__(module)

    def get_br_l2pt_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        br_l2pt_facts = facts['ansible_network_resources'].get('br_l2pt')
        if not br_l2pt_facts:
            return []
        return br_l2pt_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = list()
        commands = list()

        existing_br_l2pt_facts = self.get_br_l2pt_facts()
        commands, requests = self.set_config(existing_br_l2pt_facts)
        # # Add warnings to display commands and requests
        # self._module.warn(f"Commands: {commands}")
        # self._module.warn(f"Requests: {requests}")
        if commands and len(requests) > 0:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        changed_br_l2pt_facts = self.get_br_l2pt_facts()

        result['before'] = existing_br_l2pt_facts
        if result['changed']:
            result['after'] = changed_br_l2pt_facts
        
        # # TODO: verify correct check_mode support
        old_config = existing_br_l2pt_facts
        new_config = changed_br_l2pt_facts
        if self._module.check_mode:
            result.pop('after', None)
            new_config = get_new_config(commands, existing_br_l2pt_facts, TEST_KEYS_generate_config_merged)
            result['after(generated'] = [new_config]
        
        new_config = changed_br_l2pt_facts
        if self._module._diff:
            result['diff'] = get_formatted_config_diff(old_config,
                                                       new_config,
                                                       self._module._verbosity)

        result['warnings'] = warnings
        return result

    def set_config(self, existing_br_l2pt_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = remove_none(self._module.params['config'])
        have = existing_br_l2pt_facts
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
        commands = []
        requests = []
        state = self._module.params['state']

        if state == 'merged':
            commands, requests = self._state_merged(want, have)
        elif state == 'deleted':
            commands, requests = self._state_deleted(want, have)
        elif state == 'replaced':
            commands, requests = self._state_replaced(want, have)
        elif state == 'overridden':
            commands, requests = self._state_overridden(want, have)

        return commands, requests

    def _state_merged(self, want, have):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = self.get_modify_br_l2pt_commands(want, have)
        requests = self.get_modify_br_l2pt_requests(commands)

        if commands and len(requests) > 0:
            commands = update_states(commands, 'merged')
        else:
            commands = []        
        return commands, requests

    def _state_deleted(self, want, have):
        """ The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        delete_all = False
        requests = []
        if not want:
            commands = deepcopy(have)
            delete_all = True
        else:
            commands = self.get_delete_br_l2pt_commands(want, have)

        if commands:
            requests = self.get_delete_br_l2pt_requests(commands, delete_all)
            if len(requests) > 0:
                commands = update_states(commands, 'deleted')
        else:
            commands = []
    
        return commands, requests

    def _state_replaced(self, want, have):
        """ The command generator when state is overridden

        :rtype: A list
        :returns: the commands necessary to replace the current configuration
                  of the provided objects
        """
        commands = []
        requests = []
        # del_commands = self.get_delete_br_l2pt_replace_commands(want, have)
        # del_requests = self.get_delete_br_l2pt_requests(del_commands, False)

        # new_have = have
        # if del_commands:
        #     new_have = get_diff(have, del_commands, TEST_KEYS)
        #     commands = update_states(del_commands,'deleted')
        #     requests = del_requests
        
        diff = get_diff(want, have, TEST_KEYS)
        if diff:
            commands.extend(update_states(want, 'replaced'))
            requests.extend(self.get_modify_br_l2pt_requests(want, replace=True))
        
        self._module.warn(f"Commands: {commands}")
        self._module.warn(f"Requests: {requests}")

        return commands, requests

    def _state_overridden(self, want, have):
        """ The command generator when state is overridden 

        :rtype: A list
        :returns: the commands necessary to replace the current configuration
                  of the provided objects
        """
        commands = []
        requests = []

        # If "want" omits any interfaces, delete configs
        if not want:
            del_commands = deepcopy(have)
        else:
            del_commands = self.get_delete_br_l2pt_overridden_commands(want, have)
        del_requests = self.get_delete_br_l2pt_requests(del_commands, True)
        
        if del_commands:
            commands = update_states(del_commands, 'deleted')
            requests = del_requests

        diff = get_diff(want, have, TEST_KEYS)
        if diff:
            # Add override requests
            commands.extend(update_states(want, 'overridden'))
            requests.extend(self.get_modify_br_l2pt_requests(want, replace=True))

        return commands, requests
    
    def get_modify_br_l2pt_commands(self, want, have):
        """
        Get commands to modify or replace specific Bridge L2 Protocol Tunneling configurations
        based on the command. Only include new changes.
        """
        # If no config exists, modify everything
        if not have:
            return get_diff(want, have, TEST_KEYS)
        
        commands = []
        for intf in want:
            name = intf['name']
            want_proto_config = intf['protocol']
            have_proto_config = next((h['protocol'] for h in have if h['name'] == name), [])
            if have_proto_config:
                command_dict = {'name': name, 'protocol': {}}
                for proto, vlan_data in want_proto_config.items():
                    if have_proto_config.get(proto, None):
                        want_vlans = self.get_vlan_id_set(vlan_data['vlan_ids'])
                        have_vlans = self.get_vlan_id_set(have_proto_config[proto]['vlan_ids'])
                        # If config actually adds new VLAN IDs to existing
                        if not want_vlans.issubset(have_vlans):
                            command_dict['protocol'][proto] = vlan_data
                # Add commands for this interface
                if command_dict['protocol']:
                    commands.append(command_dict)
        return commands

    def get_modify_br_l2pt_requests(self, commands, replace=False):
        """
        Get requests to modify or replace specific Bridge L2 Protocol Tunneling configurations
        based on the command.
        """
        requests = []

        for command in commands:
            request= None
            name = command['name']
            payload = {self.payload_header: []}
            
            if re.search('Eth', name):
                proto_config = command['protocol']

                # For each protocol, check if modify request has configs for it
                for proto in self.protocols:
                    if proto_config.get(proto, None):
                        temp = {"protocol": proto}
                        temp["config"] = {"protocol": proto, "vlan-ids": self.replace_ranges(proto_config[proto]["vlan_ids"])}
                        payload[self.payload_header].append(temp)
                
                if replace:
                    request = {'path': self.br_l2pt_intf_config_path.format(intf_name=name), 'method': PUT, 'data': payload}
                else:
                    request = {'path': self.br_l2pt_intf_config_path.format(intf_name=name), 'method': PATCH, 'data': payload}
            
            requests.append(request)
        
        return requests

    def replace_ranges(self, vlan_ids):
        """
        Replace ranges that use a dash with two dots for REST request format.
        """
        new_vlan_ids = []
        for vid in vlan_ids:
            if "-" in vid:
                temp = vid.replace("-","..")
            else:
                temp = int(vid)
            new_vlan_ids.append(temp)            
        return new_vlan_ids

    def get_delete_br_l2pt_commands(self, want, have):
        """
        Get commands to delete Bridge L2 Protocol Tunneling configurations
        based on the existing config and requested deletions.
        """
        commands = []
        for intf in want:
            name = intf['name']
            want_proto_config = intf['protocol']
            have_proto_config = next((h['protocol'] for h in have if h['name'] == name), [])
            # If VLAN IDs will change for this interface
            if have_proto_config:
                command_dict = {'name': name, 'protocol': {}}
                for proto, vlan_data in want_proto_config.items():
                    if have_proto_config.get(proto, None):
                        if not vlan_data:
                            # Delete all VLAN IDs for protocol
                            command_dict['protocol'][proto] = {}
                        else:
                            # Get VLAN IDs, flatten ranges, find intersection
                            want_vlans = self.get_vlan_id_set(vlan_data['vlan_ids'])
                            have_vlans = self.get_vlan_id_set(have_proto_config[proto]['vlan_ids'])
                            vlans_to_delete = sorted(list(want_vlans.intersection(have_vlans)))
                            # Convert single IDs back to ranges in command dict
                            if vlans_to_delete:
                                command_dict['protocol'][proto] = {'vlan_ids':[str(vrng[0]) if len(vrng) == 1 else f"{vrng[0]}-{vrng[-1]}" for vrng in get_ranges_in_list(vlans_to_delete)]}
                # Add commands for this interface
                if command_dict['protocol']:
                    commands.append(command_dict)
        
        return commands

    def get_delete_br_l2pt_requests(self, commands, delete_all):
        """
        Get requests to delete Bridge L2 Protocol Tunneling configurations
        based on the command.
        """
        requests = []

        for command in commands:
            name = command['name']
            if delete_all:
                requests.append({'path': self.br_l2pt_intf_config_params_path.format(intf_name=name), 'method': DELETE})
            elif re.search('Eth', name):
                proto_config = command['protocol']
                for proto in proto_config.keys():
                    if not proto_config[proto]:
                        uri = self.br_l2pt_intf_proto_path.format(intf_name=name, protocol=proto)
                        requests.append({'path': uri, 'method': DELETE})
                    else:
                        for vrng in proto_config[proto]['vlan_ids']:
                            uri = self.br_l2pt_intf_vlan_id_path.format(intf_name=name, protocol=proto, vlan_ids=vrng.replace("-","..")) 
                            requests.append({'path': uri, 'method': DELETE})

        return requests

    def get_vlan_id_set(self, vlan_range_list):
        """Convert a list of strings specifying single VLANs and VLAN
        ranges to a new set containing integer values and return."""
        vlan_id_set = set()
        if vlan_range_list:
            for vrng in vlan_range_list:
                if '-' in vrng:
                    start, end = vrng.split('-')
                    vlan_id_set.update(range(int(start), int(end) + 1))
                else:
                    # Single VLAN ID
                    vlan_id_set.add(int(vrng))

        return vlan_id_set
    
    def get_delete_br_l2pt_replace_commands(self, want, have):
        """
        Get commands to delete Bridge L2 Protocol Tunneling configurations
        based on what is being replaced in the existing config.
        """
        commands = []
        for intf in want:
            name = intf['name']
            want_proto_config = intf['protocol']
            have_proto_config = next((h['protocol'] for h in have if h['name'] == name), [])
            if have_proto_config:
                command_dict = {'name': name, 'protocol': {}}
                for proto, vlan_data in have_proto_config.items():
                    if not want_proto_config.get(proto, None):
                        # Replace request does not include this protocol, delete
                        command_dict['protocol'][proto] = vlan_data
                # Add commands for this interface
                if command_dict['protocol']:
                    commands.append(command_dict)
        
        return commands

    def get_delete_br_l2pt_overridden_commands(self, want, have):
        """
        Get commands to delete Bridge L2 Protocol Tunneling configurations
        based on what is being overridden in the existing config.
        """
        commands = []
        for intf in have:
            name = intf['name']
            want_proto_config = next((w['protocol'] for w in want if w['name'] == name), [])
            if not want_proto_config:
                commands.append({'name': name, 'protocol': {}})
        return commands
    