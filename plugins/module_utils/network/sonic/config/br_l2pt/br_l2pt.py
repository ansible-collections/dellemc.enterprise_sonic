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
    remove_empties_from_list,
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

PATCH = 'patch'

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
    br_l2pt_intf_config_path = br_l2pt_intf_path + '/openconfig-interfaces-ext:bridge-l2pt-params/bridge-l2pt-param'
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
        # Add warnings to display commands and requests
        self._module.warn(f"Commands: {commands}")
        self._module.warn(f"Requests: {requests}")
        if commands and len(requests) > 0:
            if not self._module.check_mode:
                try:
                    # write commands/requests to a file
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
            new_config = get_new_config(commands, existing_br_l2pt_facts, TEST_KEYS_generate_config)
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
        want = remove_empties_from_list(self._module.params['config'])
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
        diff = get_diff(want, have, TEST_KEYS)

        if state == 'merged':
            commands, requests = self._state_merged(diff)
        
        return commands, requests

    def _state_merged(self, diff):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = diff
        requests = self.get_modify_br_l2pt_request(commands)
        if commands and len(requests) > 0:
            commands = update_states(commands, 'merged')
        else:
            commands = []        
        return commands, requests
    
    def get_modify_br_l2pt_request(self, commands):
        """
        Get requests to modify specific Bridge L2 Protocol Tunneling configurations
        based on the command.
        """
        requests = []
        for command in commands:
            request= None
            name = command['name']
            payload = {self.payload_header: []}
            
            if re.search('Eth', name):
                proto_config = command['protocol']

                for proto in self.protocols:
                    if proto_config.get(proto, None):
                        temp = {"protocol": proto}
                        temp["config"] = {"protocol": proto, "vlan-ids": self.replace_ranges(proto_config[proto]["vlan_ids"])}
                        payload[self.payload_header].append(temp)
                
                request = {'path': self.br_l2pt_intf_config_path.format(intf_name=name), 'method': PATCH, 'data': payload}
            
            requests.append(request)
        return request
    
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