#
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_dcbx_interfaces class
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
from ansible.module_utils.connection import ConnectionError
import re
import copy


PATCH = 'patch'
DELETE = 'delete'

TEST_KEYS = [
    {'config': {'name': ''}}
]

TEST_KEYS_formatted_diff_for_merged = [
    {'config': {'name': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}}
]


def __derive_dcbx_delete_op(key_set, command, exist_conf):
    key = command['name']
    length = len(command)
    if 'enabled' in command or length == 1:
        exist_conf[key]['enabled'] = True
    if 'pfc_tlv_enabled' in command or length == 1:
        exist_conf[key]['pfc_tlv_enabled'] = True
    if 'ets_configuration_tlv_enabled' in command or length == 1:
        exist_conf[key]['ets_configuration_tlv_enabled'] = True
    if 'ets_recommendation_tlv_enabled' in command or length == 1:
        exist_conf[key]['ets_recommendation_tlv_enabled'] = True

    return True, exist_conf


TEST_KEYS_formatted_diff_for_merged = [
    {'config': {'name': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}}
]

TEST_KEYS_formatted_diff_for_deleted = [
    {'config': {'__delete_op': __derive_dcbx_delete_op}}
]


class Dcbx_interfaces(ConfigBase):
    """
    The sonic_dcbx_interfaces class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'dcbx_interfaces',
    ]

    dcbx_interfaces_path = 'data/openconfig-dcbx:dcbx/interfaces'

    dcbx_intf_path = 'data/openconfig-dcbx:dcbx/interfaces/interface={intf_name}'

    dcbx_intf_config_path = {
        'enabled': dcbx_intf_path + '/config/enabled',
        'pfc-tlv-enabled': dcbx_intf_path + '/config/pfc-tlv-enabled',
        'ets-configuration-tlv-enabled': dcbx_intf_path + '/config/ets-configuration-tlv-enabled',
        'ets-recommendation-tlv-enabled': dcbx_intf_path + '/config/ets-recommendation-tlv-enabled'
    }

    def __init__(self, module):
        super(Dcbx_interfaces, self).__init__(module)

    def get_dcbx_interfaces_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        dcbx_interfaces_facts = facts['ansible_network_resources'].get('dcbx_interfaces')
        if not dcbx_interfaces_facts:
            return []
        return dcbx_interfaces_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = []
        commands = []

        existing_dcbx_interfaces_facts = self.get_dcbx_interfaces_facts()
        commands, requests = self.set_config(existing_dcbx_interfaces_facts)
        if commands and len(requests) > 0:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True

        result['commands'] = commands
        result['before'] = existing_dcbx_interfaces_facts

        new_config = []
        if self._module.check_mode:
            state = self._module.params['state']
            if state == "merged":
                new_config = get_new_config(commands, existing_dcbx_interfaces_facts,
                                            TEST_KEYS_formatted_diff_for_merged)
            elif state == "deleted":
                existing_dcbx_interfaces_facts_dict = {item['name']: item for item in existing_dcbx_interfaces_facts}
                new_config = get_new_config(commands, existing_dcbx_interfaces_facts_dict,
                                            TEST_KEYS_formatted_diff_for_deleted)

            result['after(generated)'] = [new_config]
        else:
            new_config = self.get_dcbx_interfaces_facts()
            result['after'] = new_config

        if self._module._diff:
            result['diff'] = get_formatted_config_diff(existing_dcbx_interfaces_facts,
                                                       new_config,
                                                       self._module._verbosity)

        result['warnings'] = warnings
        return result

    def set_config(self, existing_dcbx_interfaces_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = remove_empties_from_list(self._module.params['config'])
        have = existing_dcbx_interfaces_facts
        resp = self.set_state(want, have)
        lista = to_list(resp)
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
        diff = get_diff(want, have, TEST_KEYS)
        if state == 'deleted':
            commands, requests = self._state_deleted(want, have, diff)
        elif state == 'merged':
            commands, requests = self._state_merged(diff)
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
            requests.extend(self.get_modify_specific_dcbx_interfaces_param_requests(command))
        if commands and len(requests) > 0:
            commands = update_states(commands, 'merged')
        else:
            commands = []
        return commands, requests

    def get_length(self, obj):
        if isinstance(obj, list):
            if obj and isinstance(obj[0], dict):
                return len(obj[0])
            else:
                return 0
        elif isinstance(obj, dict):
            return len(obj)
        else:
            return 0

    def remove_default_entries(self, data):
        pop_list = []

        for item in data:
            pop_item = False

            if 'pfc_tlv_enabled' in item and item['pfc_tlv_enabled'] is True:
                item.pop('pfc_tlv_enabled')
                pop_item = True
            if 'ets_configuration_tlv_enabled' in item and item['ets_configuration_tlv_enabled'] is True:
                item.pop('ets_configuration_tlv_enabled')
                pop_item = True
            if 'ets_recommendation_tlv_enabled' in item and item['ets_recommendation_tlv_enabled'] is True:
                item.pop('ets_recommendation_tlv_enabled')
                pop_item = True
            if 'enabled' in item and item['enabled'] is True:
                item.pop('enabled')
                pop_item = True

            if 'name' in item and len(item) == 1 and pop_item:
                idx = data.index(item)
                pop_list.insert(0, idx)

        for idx in pop_list:
            data.pop(idx)

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
            requests.extend(self.get_delete_dcbx_interfaces_complete_requests(commands))
        else:
            commands = get_diff(want, diff, TEST_KEYS)
            self.remove_default_entries(commands)
            for command in commands:
                requests.extend(self.get_delete_specific_dcbx_interfaces_param_requests(command, have))

        if len(requests) == 0:
            commands = []

        if commands:
            commands = update_states(commands, "deleted")

        return commands, requests

    def get_delete_dcbx_interfaces_complete_requests(self, have):
        """Get requests to delete all existing DCBx global
        configurations in the chassis
        """
        default_dict = {'pfc_tlv_enabled': True, 'ets_configuration_tlv_enabled': True, 'ets_recommendation_tlv_enabled': True, 'enabled': True}
        requests = []
        conf = copy.deepcopy(have)
        for cfg in conf:
            del cfg['name']
            if default_dict != cfg:
                return [{'path': self.dcbx_interfaces_path, 'method': DELETE}]
        return requests

    def get_modify_specific_dcbx_interfaces_param_requests(self, command):
        """Get requests to modify specific DCBx Global configurations
        based on the command specified for the interface
        """
        requests = []

        if not command:
            return requests
        name = command['name']
        if re.search('Eth', name):
            if 'enabled' in command:
                url = self.dcbx_intf_config_path['enabled'].format(intf_name=name)
                if command['enabled'] is True:
                    requests.append({'path': url, 'method': DELETE})
                else:
                    payload = {'enabled': command['enabled']}
                    requests.append({'path': url, 'method': PATCH, 'data': payload})

            if 'pfc_tlv_enabled' in command:
                url = self.dcbx_intf_config_path['pfc-tlv-enabled'].format(intf_name=name)
                if command['pfc_tlv_enabled'] is True:
                    requests.append({'path': url, 'method': DELETE})
                else:
                    payload = {'pfc-tlv-enabled': command['pfc_tlv_enabled']}
                    requests.append({'path': url, 'method': PATCH, 'data': payload})

            if 'ets_configuration_tlv_enabled' in command:
                url = self.dcbx_intf_config_path['ets-configuration-tlv-enabled'].format(intf_name=name)
                if command['ets_configuration_tlv_enabled'] is True:
                    requests.append({'path': url, 'method': DELETE})
                else:
                    payload = {'ets-configuration-tlv-enabled': command['ets_configuration_tlv_enabled']}
                    requests.append({'path': url, 'method': PATCH, 'data': payload})

            if 'ets_recommendation_tlv_enabled' in command:
                url = self.dcbx_intf_config_path['ets-recommendation-tlv-enabled'].format(intf_name=name)
                if command['ets_recommendation_tlv_enabled'] is True:
                    requests.append({'path': url, 'method': DELETE})
                else:
                    payload = {'ets-recommendation-tlv-enabled': command['ets_recommendation_tlv_enabled']}
                    requests.append({'path': url, 'method': PATCH, 'data': payload})

        return requests

    def get_delete_specific_dcbx_interfaces_param_requests(self, command, config):
        """Get requests to delete specific DCBx global configurations
        based on the command specified for the interface
        """
        requests = []
        conf = copy.deepcopy(config)

        if not command:
            return requests

        name = command['name']

        if re.search('Eth', name):
            if self.get_length(command) == 1:
                url = self.dcbx_intf_path.format(intf_name=name)
                return [{'path': url, 'method': DELETE}]

            if 'enabled' in command:
                url = self.dcbx_intf_config_path['enabled'].format(intf_name=name)
                requests.append({'path': url, 'method': DELETE})

            if 'pfc_tlv_enabled' in command:
                url = self.dcbx_intf_config_path['pfc-tlv-enabled'].format(intf_name=name)
                requests.append({'path': url, 'method': DELETE})

            if 'ets_configuration_tlv_enabled' in command:
                url = self.dcbx_intf_config_path['ets-configuration-tlv-enabled'].format(intf_name=name)
                requests.append({'path': url, 'method': DELETE})

            if 'ets_recommendation_tlv_enabled' in command:
                url = self.dcbx_intf_config_path['ets-recommendation-tlv-enabled'].format(intf_name=name)
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
