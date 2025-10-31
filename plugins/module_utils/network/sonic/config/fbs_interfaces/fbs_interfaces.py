#
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_fbs_interfaces class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from __future__ import absolute_import, division, print_function
__metaclass__ = type

from copy import deepcopy
from ansible.module_utils.connection import ConnectionError
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import Facts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    get_diff,
    remove_empties_from_list,
    update_states
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    edit_config,
    to_request
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.formatted_diff_utils import (
    __DELETE_OP_DEFAULT,
    get_new_config,
    get_formatted_config_diff
)

delete_all = False
FBS_INTERFACE_URL = 'data/openconfig-fbs-ext:fbs/interfaces/interface'
PATCH = 'patch'
DELETE = 'delete'
TEST_KEYS = [
    {'config': {'name': ''}},
]


def __derive_fbs_interfaces_delete_op(key_set, command, exist_conf):
    if delete_all or (len(command) == 1) or (command == exist_conf):
        return True, []

    return __DELETE_OP_DEFAULT(key_set, command, exist_conf)


TEST_KEYS_generate_config = [
    {'config': {'name': '', '__delete_op': __derive_fbs_interfaces_delete_op}},
]


class Fbs_interfaces(ConfigBase):
    """
    The sonic_fbs_interfaces class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'fbs_interfaces',
    ]

    def __init__(self, module):
        super(Fbs_interfaces, self).__init__(module)

    def get_fbs_interfaces_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        fbs_interfaces_facts = facts['ansible_network_resources'].get('fbs_interfaces')
        if not fbs_interfaces_facts:
            return []
        return fbs_interfaces_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        commands = []

        existing_fbs_interfaces_facts = self.get_fbs_interfaces_facts()
        commands, requests = self.set_config(existing_fbs_interfaces_facts)
        if commands and requests:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True

        result['commands'] = commands
        result['before'] = existing_fbs_interfaces_facts
        old_config = existing_fbs_interfaces_facts

        if self._module.check_mode:
            new_config = get_new_config(commands, existing_fbs_interfaces_facts, TEST_KEYS_generate_config)
            self.sort_lists_in_config(new_config)
            result['after(generated)'] = new_config
        else:
            new_config = self.get_fbs_interfaces_facts()
            if result['changed']:
                result['after'] = new_config
        if self._module._diff:
            self.sort_lists_in_config(new_config)
            self.sort_lists_in_config(old_config)
            result['diff'] = get_formatted_config_diff(old_config, new_config, self._module._verbosity)

        return result

    def set_config(self, existing_fbs_interfaces_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = remove_empties_from_list(self._module.params['config'])
        have = existing_fbs_interfaces_facts
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
        commands, requests = [], []
        state = self._module.params['state']
        diff = get_diff(want, have, TEST_KEYS)

        if state == 'merged':
            commands, requests = self._state_merged(diff)
        elif state == 'replaced':
            commands, requests = self._state_replaced(want, have, diff)
        elif state == 'overridden':
            commands, requests = self._state_overridden(want, have, diff)
        elif state == 'deleted':
            commands, requests = self._state_deleted(want, have, diff)
        return commands, requests

    def _state_merged(self, diff):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = diff
        requests = self.get_modify_fbs_interfaces_request(commands)

        if commands and requests:
            commands = update_states(commands, 'merged')
        else:
            commands = []

        return commands, requests

    def _state_replaced(self, want, have, diff):
        """ The command generator when state is replaced

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands, mod_commands = [], []
        replaced_config, requests = self.get_replaced_config(want, have)

        if replaced_config:
            commands.extend(update_states(replaced_config, 'deleted'))
            mod_commands = want
        else:
            mod_commands = diff

        if mod_commands:
            mod_request = self.get_modify_fbs_interfaces_request(mod_commands)

            if mod_request:
                requests.append(mod_request)
                commands.extend(update_states(mod_commands, 'replaced'))

        return commands, requests

    def _state_overridden(self, want, have, diff):
        """ The command generator when state is overridden

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        global delete_all
        delete_all = False
        commands, requests = [], []
        mod_commands, mod_request = None, None
        del_commands = get_diff(have, want, TEST_KEYS)

        if del_commands:
            delete_all = True
            del_requests = self.get_delete_fbs_interfaces_requests(del_commands, delete_all)
            requests.extend(del_requests)
            commands.extend(update_states(have, 'deleted'))
            mod_commands = want
            mod_request = self.get_modify_fbs_interfaces_request(mod_commands)
        elif diff:
            mod_commands = diff
            mod_request = self.get_modify_fbs_interfaces_request(mod_commands)

        if mod_request:
            requests.append(mod_request)
            commands.extend(update_states(mod_commands, 'overridden'))

        return commands, requests

    def _state_deleted(self, want, have, diff):
        """ The command generator when state is deleted
        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        global delete_all
        delete_all = False
        requests = []

        if not want:
            commands = deepcopy(have)
            delete_all = True
        else:
            commands = get_diff(want, diff, TEST_KEYS)

        if commands:
            requests = self.get_delete_fbs_interfaces_requests(commands, delete_all)
            if requests:
                commands = update_states(commands, 'deleted')
        else:
            commands = []

        return commands, requests

    def get_modify_fbs_interfaces_request(self, commands):
        """ Returns a patch request to modify the FBS interfaces configuration"""
        request = None
        intf_list = []

        for intf in commands:
            name = intf['name']
            intf_dict = {'id': name, 'config': {'id': name}}
            ingress_policies = intf.get('ingress_policies')
            egress_policies = intf.get('egress_policies')

            if ingress_policies:
                ingress_dict = {}
                for policy_type in ('forwarding', 'monitoring', 'qos'):
                    if ingress_policies.get(policy_type) and ingress_policies[policy_type].get('policy_name'):
                        policy_name = ingress_policies[policy_type]['policy_name']
                        ingress_dict[policy_type] = {'config': {'policy-name': policy_name}}

                if ingress_dict:
                    intf_dict['ingress-policies'] = ingress_dict

            if egress_policies:
                if egress_policies.get('qos') and egress_policies['qos'].get('policy_name'):
                    policy_name = egress_policies['qos']['policy_name']
                    intf_dict['egress-policies'] = {'qos': {'config': {'policy-name': policy_name}}}

            intf_list.append(intf_dict)

        if intf_list:
            payload = {'openconfig-fbs-ext:interface': intf_list}
            request = {'path': FBS_INTERFACE_URL, 'method': PATCH, 'data': payload}

        return request

    def get_delete_fbs_interfaces_requests(self, commands, is_delete_all):
        """Returns a list of delete requests to delete the specified FBS interfaces configuration"""
        requests = []

        if is_delete_all:
            requests.append(self.get_delete_fbs_interfaces_request())
            return requests

        for intf in commands:
            name = intf['name']
            if len(intf) == 1:
                requests.append(self.get_delete_fbs_interfaces_request(name))
                continue

            ingress_policies = intf.get('ingress_policies')
            egress_policies = intf.get('egress_policies')

            if ingress_policies:
                for policy_type in ('forwarding', 'monitoring', 'qos'):
                    if ingress_policies.get(policy_type) and ingress_policies[policy_type].get('policy_name'):
                        requests.append(self.get_delete_fbs_interfaces_request(name, 'ingress-policies', policy_type))

            if egress_policies:
                if egress_policies.get('qos') and egress_policies['qos'].get('policy_name'):
                    requests.append(self.get_delete_fbs_interfaces_request(name, 'egress-policies', 'qos'))

        return requests

    @staticmethod
    def get_delete_fbs_interfaces_request(name=None, policies=None, policy_type=None):
        """Returns a delete request to delete the specified FBS interfaces configuration"""
        url = FBS_INTERFACE_URL

        if name:
            url += f'={name}'
        if policies:
            url += f'/{policies}'
        if policy_type:
            url += f'/{policy_type}'

        request = {'path': url, 'method': DELETE}

        return request

    def get_replaced_config(self, want, have):
        """Returns the replaced FBS interfaces configuration and the corresponding delete requests"""
        config_list, requests = [], []
        self.sort_lists_in_config(want)
        self.sort_lists_in_config(have)

        if not want or not have:
            return config_list

        cfg_intf_dict = {intf.get('name'): intf for intf in have}
        for intf in want:
            name = intf['name']
            cfg_intf = cfg_intf_dict.get(name)

            if not cfg_intf:
                continue
            if intf != cfg_intf:
                requests.append(self.get_delete_fbs_interfaces_request(name))
                config_list.append(cfg_intf)

        return config_list, requests

    @staticmethod
    def sort_lists_in_config(config):
        """Sorts the lists in the FBS interfaces configuration"""
        if config:
            config.sort(key=lambda x : x['name'])
