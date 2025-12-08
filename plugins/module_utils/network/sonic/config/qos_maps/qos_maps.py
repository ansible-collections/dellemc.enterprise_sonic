#
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_qos_maps class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from copy import deepcopy
from ansible.module_utils.connection import ConnectionError
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
    remove_empties,
    update_states
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import Facts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.formatted_diff_utils import (
    get_new_config,
    get_formatted_config_diff
)


delete_all = False
QOS_PATH = '/data/openconfig-qos:qos'
PATCH = 'patch'
DELETE = 'delete'
ANS_MAP_DATA = [
    {
        'map': 'dscp_maps',
        'attr1': 'dscp',
        'attr2': 'fwd_group'
    },
    {
        'map': 'dot1p_maps',
        'attr1': 'dot1p',
        'attr2': 'fwd_group'
    },
    {
        'map': 'fwd_group_queue_maps',
        'attr1': 'fwd_group',
        'attr2': 'queue_index'
    },
    {
        'map': 'fwd_group_dscp_maps',
        'attr1': 'fwd_group',
        'attr2': 'dscp'
    },
    {
        'map': 'fwd_group_dot1p_maps',
        'attr1': 'fwd_group',
        'attr2': 'dot1p'
    },
    {
        'map': 'fwd_group_pg_maps',
        'attr1': 'fwd_group',
        'attr2': 'pg_index'
    },
    {
        'map': 'pfc_priority_queue_maps',
        'attr1': 'dot1p',
        'attr2': 'queue_index'
    },
    {
        'map': 'pfc_priority_pg_maps',
        'attr1': 'dot1p',
        'attr2': 'pg_index'
    }
]

OC_ATTR_MAP = {
    'dot1p': 'dot1p',
    'dot1p_maps': 'dot1p-map',
    'dscp': 'dscp',
    'dscp_maps': 'dscp-map',
    'fwd_group_dot1p_maps': 'forwarding-group-dot1p-map',
    'fwd_group_dscp_maps': 'forwarding-group-dscp-map',
    'fwd_group_pg_maps': 'forwarding-group-priority-group-map',
    'fwd_group_queue_maps': 'forwarding-group-queue-map',
    'fwd_group': 'fwd-group',
    'queue_index': 'output-queue-index',
    'pfc_priority_pg_maps': 'pfc-priority-priority-group-map',
    'pfc_priority_queue_maps': 'pfc-priority-queue-map',
    'pg_index': 'priority-group-index'
}


class Qos_maps(ConfigBase):
    """
    The sonic_qos_maps class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'qos_maps',
    ]

    def __init__(self, module):
        super(Qos_maps, self).__init__(module)

    def get_qos_maps_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        qos_maps_facts = facts['ansible_network_resources'].get('qos_maps')
        if not qos_maps_facts:
            return {}
        return qos_maps_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        commands = []

        existing_qos_maps_facts = self.get_qos_maps_facts()
        commands, requests = self.set_config(existing_qos_maps_facts)
        if commands and requests:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True

        result['commands'] = commands
        result['before'] = existing_qos_maps_facts
        old_config = existing_qos_maps_facts

        if self._module.check_mode:
            new_config = self.get_new_config(commands, existing_qos_maps_facts)
            self.sort_lists_in_config(new_config)
            result['after_generated'] = new_config
        else:
            new_config = self.get_qos_maps_facts()
            if result['changed']:
                result['after'] = new_config
        if self._module._diff:
            self.sort_lists_in_config(new_config)
            self.sort_lists_in_config(old_config)
            result['diff'] = get_formatted_config_diff(old_config, new_config, self._module._verbosity)

        return result

    def set_config(self, existing_qos_maps_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = remove_empties(self._module.params['config'])
        have = existing_qos_maps_facts
        self.sort_lists_in_config(want)
        self.sort_lists_in_config(have)
        resp = self.set_state(want, have)
        return to_list(resp)

    def get_diff(self, base_data, compare_data):
        """This method calculates the diff between base_data and compare_data.
           Due to ambiguous 'entries' keys, the diff must be calculated by map then combined."""
        diff = {}
        maps_test_keys = {
            map_dict['map']: [{map_dict['map']: {'name': ''}}, {'entries': {map_dict['attr1']: ''}}] for map_dict in ANS_MAP_DATA
        }
        maps_compare_data = {key: {key: value} for key, value in compare_data.items()}

        for key, value in base_data.items():
            map_base_data = {key: value}
            map_compare_data = maps_compare_data.get(key)

            if map_compare_data:
                map_test_keys = maps_test_keys[key]
                map_diff = get_diff(map_base_data, map_compare_data, map_test_keys)

                if map_diff:
                    diff.update(map_diff)
            else:
                diff.update(map_base_data)

        return diff

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
        diff = self.get_diff(want, have)

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
        requests = self.get_modify_qos_maps_request(commands)

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
            mod_request = self.get_modify_qos_maps_request(mod_commands)

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
        del_commands = self.get_diff(have, want)

        if del_commands:
            delete_all = True
            del_requests = self.get_delete_qos_maps_requests(del_commands, delete_all)
            requests.extend(del_requests)
            commands.extend(update_states(have, 'deleted'))
            mod_commands = want
            mod_request = self.get_modify_qos_maps_request(mod_commands)
        elif diff:
            mod_commands = diff
            mod_request = self.get_modify_qos_maps_request(mod_commands)

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
            commands = self.get_diff(want, diff)

        if commands:
            requests = self.get_delete_qos_maps_requests(commands, delete_all)
            if requests:
                commands = update_states(commands, 'deleted')
        else:
            commands = []

        return commands, requests

    def get_modify_qos_maps_request(self, commands):
        """ Returns a patch request to modify the QoS maps configuration"""
        request = None

        if commands:
            qos_dict = {}

            for map_dict in ANS_MAP_DATA:
                ans_map_name = map_dict['map']
                map_cfg = commands.get(ans_map_name)

                if map_cfg:
                    oc_map_list = []
                    oc_map_name = OC_ATTR_MAP[ans_map_name]

                    for cfg in map_cfg:
                        oc_map_dict = {'name': cfg['name'], 'config': {'name': cfg['name']}}
                        entries = cfg.get('entries')

                        if entries:
                            oc_entry_list = []

                            for entry in entries:
                                attr1 = map_dict['attr1']
                                attr2 = map_dict['attr2']
                                val1 = entry.get(attr1)
                                val2 = entry.get(attr2)
                                oc_attr1 = OC_ATTR_MAP[attr1]
                                oc_entry_dict = {oc_attr1: val1, 'config': {oc_attr1: val1}}

                                if val2 is not None:
                                    oc_attr2 = OC_ATTR_MAP[attr2]
                                    oc_entry_dict['config'][oc_attr2] = val2
                                if oc_entry_dict:
                                    oc_entry_list.append(oc_entry_dict)
                            if oc_entry_list:
                                oc_entries_name = f'{oc_map_name}-entries'
                                oc_entry_name = f'{oc_map_name}-entry'
                                oc_map_dict[oc_entries_name] = {oc_entry_name: oc_entry_list}
                        if oc_map_dict:
                            oc_map_list.append(oc_map_dict)
                    if oc_map_list:
                        qos_dict[f'openconfig-qos-maps-ext:{oc_map_name}s'] = {oc_map_name: oc_map_list}
            if qos_dict:
                payload = {'openconfig-qos:qos': qos_dict}
                request = {'path': QOS_PATH, 'method': PATCH, 'data': payload}

        return request

    @staticmethod
    def get_delete_qos_maps_request(oc_map_name, name=None, val1=None, attr2=None):
        """Returns a delete request to delete the specified QoS maps configuration"""
        url = f'{QOS_PATH}/openconfig-qos-maps-ext:{oc_map_name}s'

        if name:
            url += f'/{oc_map_name}={name}'
        if val1 is not None:
            url += f'/{oc_map_name}-entries/{oc_map_name}-entry={val1}'
        if attr2:
            url += f'/config/{attr2}'

        request = {'path': url, 'method': DELETE}

        return request

    def get_delete_qos_maps_requests(self, commands, is_delete_all):
        """Returns a list of delete requests to delete the specified QoS maps configuration"""
        requests = []

        for map_dict in ANS_MAP_DATA:
            ans_map_name = map_dict['map']
            map_cfg = commands.get(ans_map_name)
            oc_map_name = OC_ATTR_MAP[ans_map_name]

            if map_cfg:
                if is_delete_all:
                    requests.append(self.get_delete_qos_maps_request(oc_map_name))
                    continue

                for cfg in map_cfg:
                    name = cfg['name']
                    if len(cfg) == 1:
                        requests.append(self.get_delete_qos_maps_request(oc_map_name, name))
                        continue

                    entries = cfg.get('entries')

                    if entries:
                        for entry in entries:
                            attr1 = map_dict['attr1']
                            val1 = entry.get(attr1)

                            if len(entry) == 1:
                                requests.append(self.get_delete_qos_maps_request(oc_map_name, name, val1))
                                continue

                            attr2 = map_dict['attr2']
                            val2 = entry.get(attr2)

                            if val2 is not None:
                                oc_attr2 = OC_ATTR_MAP[attr2]
                                requests.append(self.get_delete_qos_maps_request(oc_map_name, name, val1, oc_attr2))

        return requests

    @staticmethod
    def sort_lists_in_config(config):
        """Sorts the lists in QoS maps configuration"""
        if config:
            for map_dict in ANS_MAP_DATA:
                ans_map_name = map_dict['map']
                attr1 = map_dict['attr1']
                if config.get(ans_map_name):
                    config[ans_map_name].sort(key=lambda x: x['name'])
                    for cfg in config[ans_map_name]:
                        if cfg.get('entries'):
                            cfg['entries'].sort(key=lambda x: x[attr1])

    def get_replaced_config(self, want, have):
        """Returns the replaced QoS maps configuration and the corresponding delete requests"""
        config_dict = {}
        requests = []

        if not want or not have:
            return config_dict, requests

        for map_dict in ANS_MAP_DATA:
            ans_map_name = map_dict['map']
            map_cfg = want.get(ans_map_name)

            if map_cfg:
                map_list = []
                have_map_cfg = have.get(ans_map_name, [])
                have_cfg_dict = {cfg.get('name'): cfg for cfg in have_map_cfg}
                oc_map_name = OC_ATTR_MAP[ans_map_name]

                for cfg in map_cfg:
                    name = cfg['name']
                    have_cfg = have_cfg_dict.get(name)

                    if not have_cfg:
                        continue

                    entries = cfg.get('entries')
                    have_entries = have_cfg.get('entries')

                    if (entries and have_entries) and (entries != have_entries):
                        map_list.append(have_cfg)
                        requests.append(self.get_delete_qos_maps_request(oc_map_name, name))
                if map_list:
                    config_dict[ans_map_name] = map_list

        return config_dict, requests

    def __derive_merge_op(self, key_set, command, exist_conf):
        """Returns new QoS map configuration for merge operation"""
        if not command:
            return True, exist_conf

        if not exist_conf:
            return True, command

        new_conf = deepcopy(exist_conf)
        for map_dict in ANS_MAP_DATA:
            ans_map_name = map_dict['map']
            attr1 = map_dict['attr1']
            attr2 = map_dict['attr2']
            map_cfg = command.get(ans_map_name)

            if map_cfg:
                new_map_cfg = new_conf.get(ans_map_name)
                if not new_map_cfg:
                    new_conf[ans_map_name] = map_cfg
                    continue

                new_cfg_dict = {cfg.get('name'): cfg for cfg in new_map_cfg}
                for cfg in map_cfg:
                    name = cfg['name']
                    new_cfg = new_cfg_dict.get(name)
                    if not new_cfg:
                        new_conf[ans_map_name].append(cfg)
                        continue

                    entries = cfg.get('entries')
                    if entries:
                        new_entries = new_cfg.get('entries')
                        if not new_entries:
                            new_cfg['entries'] = entries
                            continue

                        new_entry_dict = {entry.get(attr1): entry for entry in new_entries}
                        for entry in entries:
                            val1 = entry.get(attr1)
                            new_entry = new_entry_dict.get(val1)
                            if not new_entry:
                                new_entries.append(entry)
                                continue

                            val2 = entry.get(attr2)
                            if val2:
                                new_entry[attr2] = val2

        return True, new_conf

    def __derive_delete_op(self, key_set, command, exist_conf):
        """Returns new QoS map configuration for delete operation"""
        if delete_all:
            return True, {}

        new_conf = deepcopy(exist_conf)
        for map_dict in ANS_MAP_DATA:
            ans_map_name = map_dict['map']
            attr1 = map_dict['attr1']
            map_cfg = command.get(ans_map_name)

            if map_cfg:
                new_map_cfg = new_conf.get(ans_map_name)
                new_cfg_dict = {cfg.get('name'): idx for idx, cfg in enumerate(new_map_cfg)}
                # Loop over reversed list to avoid index out of range when using del
                for cfg in map_cfg[::-1]:
                    name = cfg['name']
                    new_cfg = new_cfg_dict.get(name)
                    if len(cfg) == 1:
                        del new_map_cfg[new_cfg]
                        continue

                    entries = cfg.get('entries')
                    if entries:
                        new_entries = new_map_cfg[new_cfg].get('entries')
                        new_entry_dict = {entry.get(attr1): idx for idx, entry in enumerate(new_entries)}
                        # Loop over reversed list to avoid index out of range when using del
                        for entry in entries[::-1]:
                            val1 = entry.get(attr1)
                            new_entry = new_entry_dict.get(val1)
                            del new_entries[new_entry]
                        if not new_entries:
                            del new_map_cfg[new_cfg]['entries']

                if not new_map_cfg:
                    del new_conf[ans_map_name]

        return True, new_conf

    def get_new_config(self, commands, have):
        """Returns generated configuration based on commands and
           existing configuration"""
        key_set = [
            {'config': {'__merge_op': self.__derive_merge_op, '__delete_op': self.__derive_delete_op}},
        ]
        new_config = get_new_config(commands, have, key_set)

        return new_config
