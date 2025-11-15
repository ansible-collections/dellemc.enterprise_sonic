#
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_roce class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.connection import ConnectionError
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    get_diff,
    remove_empties,
    update_states
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import Facts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config_reboot
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.formatted_diff_utils import (
    __MERGE_OP_DEFAULT,
    get_new_config,
    get_formatted_config_diff
)


ROCE_PATH = '/operations/openconfig-qos-private:qos-roce-config'
POST = 'post'


def __derive_roce_merge_op(key_set, command, exist_conf):
    if command.get('roce_enable') is False:
        exist_conf.pop('pfc_priority', None)

    return __MERGE_OP_DEFAULT(key_set, command, exist_conf)


TEST_KEYS_generate_config = [
    {'config': {'__merge_op': __derive_roce_merge_op}}
]


class Roce(ConfigBase):
    """
    The sonic_roce class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'roce',
    ]

    def __init__(self, module):
        super(Roce, self).__init__(module)

    def get_roce_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        roce_facts = facts['ansible_network_resources'].get('roce')
        if not roce_facts:
            return {}
        return roce_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        commands = []

        existing_roce_facts = self.get_roce_facts()
        commands, requests = self.set_config(existing_roce_facts)
        if commands and len(requests) > 0:
            if not self._module.check_mode:
                try:
                    edit_config_reboot(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    pass
            result['changed'] = True

        result['commands'] = commands
        result['before'] = existing_roce_facts
        old_config = existing_roce_facts

        if self._module.check_mode:
            new_config = get_new_config(commands, existing_roce_facts, TEST_KEYS_generate_config)
            result['after(generated)'] = new_config
        else:
            new_config = self.get_roce_facts()
            if result['changed']:
                result['after'] = new_config
        if self._module._diff:
            result['diff'] = get_formatted_config_diff(old_config, new_config, self._module._verbosity)

        return result

    def set_config(self, existing_roce_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = remove_empties(self._module.params['config'])
        have = existing_roce_facts
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
        diff = get_diff(want, have)

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
        requests = self.get_modify_roce_request(commands)

        if commands and len(requests) > 0:
            commands = update_states(commands, 'merged')
        else:
            commands = []

        return commands, requests

    def get_modify_roce_request(self, commands):
        """ Returns a post request to modify the RoCE configuration"""
        request = None

        if commands:
            input_dict = {}
            bool_dict = {True: 'ENABLE', False: 'DISABLE'}
            roce_enable = commands.get('roce_enable')
            pfc_priority = commands.get('pfc_priority')

            if roce_enable is False and pfc_priority:
                self._module.fail_json(msg='PFC priority is only configurable when RoCE is enabled.')
            if roce_enable is not None:
                input_dict['operation'] = bool_dict[roce_enable]
            if pfc_priority:
                input_dict['pfc-priority'] = pfc_priority
            if input_dict:
                payload = {'openconfig-qos-private:input': input_dict}
                request = {'path': ROCE_PATH, 'method': POST, 'data': payload}

        return request
