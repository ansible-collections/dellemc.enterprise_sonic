#
# -*- coding: utf-8 -*-
# Copyright 2023 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_password_complexity class
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


PATCH = 'patch'
DELETE = 'delete'


class Password_complexity(ConfigBase):
    """
    The sonic_password_complexity class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'password_complexity',
    ]

    password_attribute_path = 'data/openconfig-system:system/openconfig-system-ext:login/password-attributes/config'
    password_attribute_config_path = {
        'min_lower_case': password_attribute_path + '/min-lower-case',
        'min_upper_case': password_attribute_path + '/min-upper-case',
        'min_numerals': password_attribute_path + '/min-numerals',
        'min_special_char': password_attribute_path + '/min-special-char',
        'min_length': password_attribute_path + '/min-len',
    }
    default_config_dict = {"min_lower_case": 0, "min_upper_case": 0, "min_numerals": 0, "min_special_char": 0, "min_len": 8}

    def __init__(self, module):
        super(Password_complexity, self).__init__(module)

    def get_password_complexity_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        password_complexity_facts = facts['ansible_network_resources'].get('password_complexity')
        if not password_complexity_facts:
            return []
        return password_complexity_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = list()
        commands = list()

        existing_password_complexity_facts = self.get_password_complexity_facts()
        commands, requests = self.set_config(existing_password_complexity_facts)

        if commands:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        changed_password_complexity_facts = self.get_password_complexity_facts()

        result['before'] = existing_password_complexity_facts
        if result['changed']:
            result['after'] = changed_password_complexity_facts

        result['warnings'] = warnings
        return result

    def set_config(self, existing_password_complexity_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']
        have = existing_password_complexity_facts
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
        if state == 'overridden':
            commands, requests = self._state_replaced_overridden(want, have, diff)
        elif state == 'deleted':
            commands, requests = self._state_deleted(want, have, diff)
        elif state == 'merged':
            commands, requests = self._state_merged(diff)
        elif state == 'replaced':
            commands, requests = self._state_replaced_overridden(want, have, diff)
        return commands, requests

    def _state_replaced_overridden(self, want, have, diff):
        """ The command generator when state is replaced or overridden
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        requests = []
        delete = {}
        state = self._module.params['state']

        for key in have:
            if key in want:
                if want[key] == have[key]:
                    continue
            if key not in diff and have[key] != self.default_config_dict[key]:
                delete[key] = have[key]
        if delete:
            commands = update_states(delete, 'deleted')
            requests.extend(self.get_delete_specific_password_attribute_param_requests(delete))
        if diff:
            commands.extend(update_states(diff, state))
            requests.extend(self.get_modify_specific_password_attribute_param_requests(diff))

        return commands, requests

    def _state_merged(self, diff):
        """ The command generator when state is merged
        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = []
        requests = []

        if diff:
            requests = self.get_modify_specific_password_attribute_param_requests(diff)
            if len(requests) > 0:
                commands = update_states(diff, 'merged')

        return commands, requests

    def _state_deleted(self, want, have, diff):
        """ The command generator when state is deleted
        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        commands = []
        requests = []
        delete = {}

        if not want:
            delete = have.copy()
            delete = {key: value for key, value in delete.items() if key not in self.default_config_dict or self.default_config_dict[key] != value}
            commands = delete
            requests.extend(self.get_delete_specific_password_attribute_param_requests(commands))
        else:
            delete = get_diff(want, diff)
            delete = {key: value for key, value in delete.items() if key not in self.default_config_dict or self.default_config_dict[key] != value}
            commands = delete
            requests.extend(self.get_delete_specific_password_attribute_param_requests(commands))

        if len(requests) == 0:
            commands = []

        if commands:
            commands = update_states(commands, "deleted")

        return commands, requests

    def get_modify_specific_password_attribute_param_requests(self, command):
        """Get requests to modify specific password attribute configurations
        based on the command specified
        """
        requests = []
        config_dict = {}

        if not command:
            return requests

        if 'min_lower_case' in command and command['min_lower_case'] is not None:
            config_dict['min-lower-case'] = int(command['min_lower_case'])

        if 'min_upper_case' in command and command['min_upper_case'] is not None:
            config_dict['min-upper-case'] = int(command['min_upper_case'])

        if 'min_numerals' in command and command['min_numerals'] is not None:
            config_dict['min-numerals'] = int(command['min_numerals'])

        if 'min_special_char' in command and command['min_special_char'] is not None:
            config_dict['min-special-char'] = int(command['min_special_char'])

        if 'min_len' in command and command['min_len'] is not None:
            config_dict['min-len'] = int(command['min_len'])

        payload = {"openconfig-system-ext:config": config_dict}

        requests.append({'path': self.password_attribute_path, 'method': PATCH, 'data': payload})

        return requests

    def get_delete_specific_password_attribute_param_requests(self, command):
        """Get requests to delete specific password attribute configurations
        based on the command specified
        """
        requests = []

        if not command:
            return requests

        if 'min_lower_case' in command:
            url = self.password_attribute_config_path['min_lower_case']
            requests.append({'path': url, 'method': DELETE})

        if 'min_upper_case' in command:
            url = self.password_attribute_config_path['min_upper_case']
            requests.append({'path': url, 'method': DELETE})

        if 'min_numerals' in command:
            url = self.password_attribute_config_path['min_numerals']
            requests.append({'path': url, 'method': DELETE})

        if 'min_special_char' in command:
            url = self.password_attribute_config_path['min_special_char']
            requests.append({'path': url, 'method': DELETE})

        if 'min_len' in command:
            url = self.password_attribute_config_path['min_length']
            requests.append({'path': url, 'method': DELETE})

        return requests
