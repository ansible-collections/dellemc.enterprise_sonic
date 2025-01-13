#
# -*- coding: utf-8 -*-
# Copyright 2024 Dell Inc. or its subsidiaries. All Rights Reserved.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_snmp class
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
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    get_diff,
    update_states,
    get_replaced_config,
    remove_empties_from_list,
    send_requests
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.formatted_diff_utils import (
    __DELETE_CONFIG_IF_NO_SUBCONFIG,
    get_new_config,
    get_formatted_config_diff
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import Facts

PATCH = 'patch'
DELETE = 'delete'
test_keys = [
    {'user':},
    {'host':},
]
test_keys_generate_config = [
    {'config': {'__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}},
    {'user': {'__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}},
    {'host': {'__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}},
]
class Snmp(ConfigBase):
    """
    The sonic_snmp class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'snmp',
    ]

    def __init__(self, module):
        super(Snmp, self).__init__(module)

    def get_snmp_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        snmp_facts = facts['ansible_network_resources'].get('snmp')
        if not snmp_facts:
            return []
        return snmp_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = list()
        commands = list()

        existing_snmp_facts = self.get_snmp_facts()
        commands, requests = self.set_config(existing_snmp_facts)
        #commands.extend(self.set_config(existing_snmp_facts))

        if commands and requests:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
                #self._connection.edit_config(commands)
            result['changed'] = True
        result['commands'] = commands

        changed_snmp_facts = self.get_snmp_facts()

        result['before'] = existing_snmp_facts
        if result['changed']:
            result['after'] = changed_snmp_facts

        new_config = changed_snmp_facts
        old_config - existing_snmp_facts
        if self._module.check_mode:
            result.pop('after', None)
            existing_snmp_facts = remove_empties_from_list(existing_snmp_facts)
            new_config = get_new_config(commands, existing_snmp_facts, test_keys_generate_config)
            new_config = self.post_process_generated_config(new_config)
            new_config = remove_empties_from_list(new_config)
            result['after(generated)'] = new_config
            self.sort_lists_in_config(result['after(generated)'])

        if self._module_diff:
            result['diff'] = get_formatted_config_diff(old_config, new_config, self._module._verbosity)

        result['warnings'] = warnings
        return result

    def set_config(self, existing_snmp_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']
        have = existing_snmp_facts
        want = remove_empties_from_list(want)
        new_want, new_have =self.validate_and_normalize_config(want, have)
        self.sort_lists_in_config(new_want)
        self.sort_lists_in_config(new_have)
        resp = self.set_state(new_want, new_have)
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
        diff = get_diff(want, have, test_keys)

        if state == 'overridden':
            kwargs = {}
            commands, requests = self._state_overridden(want, have)
        elif state == 'deleted':
            kwargs = {}
            commands, requests = self._state_deleted(want, have, diff)
        elif state == 'merged':
            kwargs = {}
            commands, requests = self._state_merged(want, have, diff)
        elif state == 'replaced':
            kwargs = {}
            commands, requests = self._state_replaced(want, have, diff)
        
        return commands, requests

    def _state_replaced(self, want, have, diff):
        """ The command generator when state is replaced

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands, requests = [], []
        add_config, delete_config = self._get_replaced_config(want, have)
        if del_config:
            del_commands, del_requests = self.get_delete_snmp_request(del_config, have)
            if len(del_requests) > 0:
                requests.extend(del_requests)
                commands.extend(update_states(del_commands, 'deleted'))
        if add_config:
            new_requests = self.get_create_snmp_request(add_config, have)
            if len(new_requests) > 0:
                requests.extend(new_requests)
                commands.extend(update_states(add_config, 'replaced'))
        return commands, requests


    def _state_overridden(self, want, have):
        """ The command generator when state is overridden

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands, requests = [], []
        diff = get_diff(want, have, TEST_KEYS)
        diff2 = get_diff(have, want, TEST_KEYS)
        if diff or diff2:
            del_commands, del_requests = self.get_delete_snmp_request(have, have)
            if len(del_requests) > 0:
                requests.extend(del_requests)
                commands.extend(update_states(have, 'deleted'))
            new_requests = self.get_create_snmp_request(want)
            if len(new_requests) > 0:
                requests.extend(new_requests)
                commands.extend(update_states(want, 'overridden'))
        return commands, requests


    def _state_merged(self, want, have, diff):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = diff
        requests = self.get_create_snmp_request(commands, have)

        if commands and len(requests) > 0:
            commands = update_states(commands, "merged")

        return commands, requests

    def _state_deleted(self, want, have, diff):
        """ The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        commands, requests = [], []
        is_delete_all = False
        if not want or len(have) == 0:
            commands = have
            is_delete_all = True
        else:
            self.sort_lists_in_config(want)
            self.sort_lists_in_config(have)
            new_want = deepcopy(want)
            new_have = deepcopy(have)
            for default_entry in DEFAULT_ENTREES:
                remove_matching_defaults(new_have, default_entry)
            new_have = remove_empties_from_list(new_have)
            new_want = remove_empties_from_list(new_want)
        commands, requests = self.get_delete_snmp_request(new_want, have is_delete_all)

        if is_delete_all:
            requests = self.get_delete_all_snmp_request(have)
        else:
            requests = self.get_delete_snmp_request(commands, have)

        if commands:
            commands = update_states(commands, "deleted")
        else:
            commands = []

        return commands, requests

    def _get_replaced_config(self, want, have):
        adda_config, del_config = [], []
        for conf in want:
            is_change = False


    def get_create_snmp_request(self, config, have):
        requests = []
    
        for cmd in config:
            requests.append(cmd)


    def get_delete_all_snmp_request(self, have):
        requests = []

        users_requests = []
        hosts_requests = []

        for conf in configs:

            host = conf.get('host', None)
            user = conf.get('user', None)

            matched 

    def get_delete_snmp_request(self, configs, have):
        requests = []

        if not configs:
            return requests
