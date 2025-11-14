#
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_qos_wred class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from copy import deepcopy
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)
from ansible.module_utils.connection import ConnectionError
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    get_diff,
    remove_empties_from_list,
    update_states
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.formatted_diff_utils import (
    __DELETE_OP_DEFAULT,
    get_new_config,
    get_formatted_config_diff
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import Facts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)


delete_all = False
QOS_WRED_PATH = '/data/openconfig-qos:qos/wred-profiles/wred-profile'
PATCH = 'patch'
DELETE = 'delete'
TEST_KEYS = [
    {'config': {'name': ''}}
]


def __derive_delete_op(key_set, command, exist_conf):
    """Returns new QoS WRED configuration for delete operation"""
    if delete_all:
        return True, {}

    return __DELETE_OP_DEFAULT(key_set, command, exist_conf)


TEST_KEYS_generate_config = [
    {'config': {'name': '', '__delete_op': __derive_delete_op}}
]
enum_dict = {
    'all': 'ECN_ALL',
    'none': 'ECN_NONE'
}


class Qos_wred(ConfigBase):
    """
    The sonic_qos_wred class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'qos_wred',
    ]

    def __init__(self, module):
        super(Qos_wred, self).__init__(module)

    def get_qos_wred_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A list
        :returns: The current configuration as a list
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        qos_wred_facts = facts['ansible_network_resources'].get('qos_wred')
        if not qos_wred_facts:
            return []
        return qos_wred_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        commands = []

        existing_qos_wred_facts = self.get_qos_wred_facts()
        commands, requests = self.set_config(existing_qos_wred_facts)
        if commands and requests:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True

        result['commands'] = commands
        result['before'] = existing_qos_wred_facts
        old_config = existing_qos_wred_facts

        if self._module.check_mode:
            new_config = get_new_config(commands, existing_qos_wred_facts, TEST_KEYS_generate_config)
            self.sort_lists_in_config(new_config)
            result['after(generated)'] = new_config
        else:
            new_config = self.get_qos_wred_facts()
            if result['changed']:
                result['after'] = new_config
        if self._module._diff:
            self.sort_lists_in_config(new_config)
            self.sort_lists_in_config(old_config)
            result['diff'] = get_formatted_config_diff(old_config, new_config, self._module._verbosity)

        return result

    def set_config(self, existing_qos_wred_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a list from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = remove_empties_from_list(self._module.params['config'])
        have = existing_qos_wred_facts
        self.sort_lists_in_config(want)
        self.sort_lists_in_config(have)
        resp = self.set_state(want, have)
        return to_list(resp)

    def set_state(self, want, have):
        """ Select the appropriate function based on the state provided

        :param want: the desired configuration as a list
        :param have: the current configuration as a list
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
        requests = self.get_modify_qos_wred_request(commands)

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
            mod_request = self.get_modify_qos_wred_request(mod_commands)

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
            del_requests = self.get_delete_qos_wred_requests(del_commands, delete_all)
            requests.extend(del_requests)
            commands.extend(update_states(have, 'deleted'))
            mod_commands = want
            mod_request = self.get_modify_qos_wred_request(mod_commands)
        elif diff:
            mod_commands = diff
            mod_request = self.get_modify_qos_wred_request(mod_commands)

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
        commands, requests = [], []

        if not want:
            commands = deepcopy(have)
            delete_all = True
        else:
            commands = get_diff(want, diff, TEST_KEYS)

        if commands:
            requests = self.get_delete_qos_wred_requests(commands, delete_all)
            if requests:
                commands = update_states(commands, 'deleted')
        else:
            commands = []

        return commands, requests

    def get_modify_qos_wred_request(self, commands):
        """ Returns a patch request to modify the QoS WRED configuration"""
        request = None

        if commands:
            wred_list = []
            for wred in commands:
                config_dict = {}
                name = wred.get('name')
                ecn = wred.get('ecn')
                colors = ['green', 'red', 'yellow']

                for color in colors:
                    color_dict = wred.get(color)
                    if color_dict:
                        enable = color_dict.get('enable')
                        min_threshold = color_dict.get('min_threshold')
                        max_threshold = color_dict.get('max_threshold')
                        drop_probability = color_dict.get('drop_probability')

                        if enable is not None:
                            config_dict[f'wred-{color}-enable'] = enable
                        if min_threshold:
                            config_dict[f'{color}-min-threshold'] = str(min_threshold)
                        if max_threshold:
                            config_dict[f'{color}-max-threshold'] = str(max_threshold)
                        if drop_probability is not None:
                            config_dict[f'{color}-drop-probability'] = str(drop_probability)
                if ecn:
                    config_dict['ecn'] = enum_dict[ecn]
                if name:
                    config_dict['name'] = name
                    wred_list.append({'name': name, 'config': config_dict})
            if wred_list:
                payload = {'openconfig-qos:wred-profile': wred_list}
                request = {'path': QOS_WRED_PATH, 'method': PATCH, 'data': payload}

        return request

    def get_delete_qos_wred_requests(self, commands, is_delete_all):
        """Returns a list of delete requests to delete the specified QoS WRED configuration"""
        requests = []

        if not commands:
            return requests

        if is_delete_all:
            requests.append(self.get_delete_qos_wred_request())
            return requests

        colors = ('green', 'red', 'yellow')
        attributes = ('enable', 'min_threshold', 'max_threshold', 'drop_probability')

        for wred in commands:
            name = wred.get('name')
            if len(wred) == 1:
                requests.append(self.get_delete_qos_wred_request(name))
                continue

            ecn = wred.get('ecn')
            if ecn:
                requests.append(self.get_delete_qos_wred_request(name, 'ecn'))
            for color in colors:
                color_dict = wred.get(color)
                if color_dict:
                    for attr in attributes:
                        val = color_dict.get(attr)
                        if val is not None:
                            oc_attr = None
                            if attr == 'enable':
                                oc_attr = f'wred-{color}-{attr}'
                            else:
                                oc_attr = f'{color}-{attr.replace("_", "-")}'
                            requests.append(self.get_delete_qos_wred_request(name, oc_attr))

        return requests

    @staticmethod
    def sort_lists_in_config(config):
        """Sorts the lists in QoS WRED configuration"""
        if config:
            config.sort(key=lambda x: x['name'])

    @staticmethod
    def get_delete_qos_wred_request(name=None, attr=None):
        """Returns a delete request to delete the specified QoS WRED configuration"""
        url = QOS_WRED_PATH
        if name:
            url += f'={name}'
        if attr:
            url += f'/config/{attr}'
        request = {'path': url, 'method': DELETE}

        return request

    def get_replaced_config(self, want, have):
        """Returns the replaced QoS WRED configuration and the corresponding delete requests"""
        config_list, requests = [], []

        if not want or not have:
            return config_list, requests

        cfg_wred_dict = {wred.get('name'): wred for wred in have}
        for wred in want:
            name = wred.get('name')
            cfg_wred = cfg_wred_dict.get(name)

            if not cfg_wred:
                continue

            if wred != cfg_wred:
                requests.append(self.get_delete_qos_wred_request(name))
                config_list.append(cfg_wred)

        return config_list, requests
