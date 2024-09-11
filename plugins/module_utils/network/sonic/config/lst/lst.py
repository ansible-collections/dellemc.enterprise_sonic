#
# -*- coding: utf-8 -*-
# Copyright 2024 Dell Inc. or its subsidiaries. All Rights Reserved.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_lst class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from __future__ import absolute_import, division, print_function
__metaclass__ = type

from copy import deepcopy
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import Facts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    get_diff,
    remove_empties,
    update_states
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    edit_config,
    to_request
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.formatted_diff_utils import (
    __DELETE_CONFIG_IF_NO_SUBCONFIG,
    get_new_config,
    get_formatted_config_diff
)

LST_PATH = 'data/openconfig-lst-ext:lst'
PATCH = 'patch'
DELETE = 'delete'
TEST_KEYS = [
    {'lst_groups': {'name': ''}},
    {'interfaces': {'id': ''}},
    {'upstream_groups': {'group_name': ''}}
]
TEST_KEYS_generate_config = [
    {'lst_groups': {'name': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}},
    {'interfaces': {'id': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}},
    {'upstream_groups': {'group_name': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}}
]


class Lst(ConfigBase):
    """
    The sonic_lst class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'lst',
    ]

    def __init__(self, module):
        super(Lst, self).__init__(module)

    def get_lst_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        lst_facts = facts['ansible_network_resources'].get('lst')
        if not lst_facts:
            return {}
        return lst_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = []
        commands = []

        existing_lst_facts = self.get_lst_facts()
        commands, requests = self.set_config(existing_lst_facts)
        if commands and len(requests) > 0:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        changed_lst_facts = self.get_lst_facts()

        result['before'] = existing_lst_facts
        if result['changed']:
            result['after'] = changed_lst_facts

        new_config = changed_lst_facts
        old_config = existing_lst_facts
        if self._module.check_mode:
            result.pop('after', None)
            new_config = get_new_config(commands, existing_lst_facts, TEST_KEYS_generate_config)
            self.post_process_generated_config(new_config)
            result['after(generated)'] = new_config
        if self._module._diff:
            self.sort_lists_in_config(new_config)
            self.sort_lists_in_config(old_config)
            result['diff'] = get_formatted_config_diff(old_config,
                                                       new_config,
                                                       self._module._verbosity)

        result['warnings'] = warnings
        return result

    def set_config(self, existing_lst_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = remove_empties(self._module.params['config'])
        have = existing_lst_facts
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
        elif state == 'replaced':
            commands, requests = self._state_replaced(want, have, diff)
        elif state == 'overridden':
            commands, requests = self._state_overridden(want, have)
        elif state == 'deleted':
            commands, requests = self._state_deleted(want, have)
        return commands, requests

    def _state_merged(self, diff):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = diff
        requests = self.get_modify_lst_request(commands)

        if commands and len(requests) > 0:
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
        commands = []
        mod_commands = []
        replaced_config, requests = self.get_replaced_config(want, have)

        if replaced_config:
            commands.extend(update_states(replaced_config, 'deleted'))
            mod_commands = want
        else:
            mod_commands = diff

        if mod_commands:
            mod_request = self.get_modify_lst_request(mod_commands)

            if mod_request:
                requests.append(mod_request)
                commands.extend(update_states(mod_commands, 'replaced'))

        return commands, requests

    def _state_overridden(self, want, have):
        """ The command generator when state is overridden

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        requests = []
        del_commands = get_diff(have, want, TEST_KEYS)
        self.remove_default_entries(del_commands)

        if del_commands:
            is_delete_all = True
            del_requests = self.get_delete_lst_requests(del_commands, have, is_delete_all)
            requests.extend(del_requests)
            commands.extend(update_states(have, 'deleted'))
            have = {}

        if not have and want:
            mod_commands = want
            mod_request = self.get_modify_lst_request(mod_commands)

            if len(mod_request) > 0:
                requests.append(mod_request)
                commands.extend(update_states(mod_commands, 'overridden'))

        return commands, requests

    def _state_deleted(self, want, have):
        """ The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        is_delete_all = False

        if not want:
            commands = deepcopy(have)
            is_delete_all = True
        else:
            commands = deepcopy(want)

        self.remove_default_entries(commands)
        requests = self.get_delete_lst_requests(commands, have, is_delete_all)

        if commands and len(requests) > 0:
            commands = update_states(commands, 'deleted')
        else:
            commands = []

        return commands, requests

    def get_modify_lst_request(self, commands):
        request = None
        enum_dict = {'l3': 'GROUP_L3', 'percentage': 'ONLINE_PERCENTAGE'}

        if commands:
            # Handle lst_groups modification
            lst_dict = {}
            lst_groups = commands.get('lst_groups')
            if lst_groups:
                lst_group_list = []
                for group in lst_groups:
                    cfg_dict = {}
                    all_evpn_es_downstream = group.get('all_evpn_es_downstream')
                    all_mclags_downstream = group.get('all_mclags_downstream')
                    group_description = group.get('group_description')
                    group_type = group.get('group_type')
                    name = group.get('name')
                    threshold_down = group.get('threshold_down')
                    threshold_type = group.get('threshold_type')
                    threshold_up = group.get('threshold_up')
                    timeout = group.get('timeout')

                    if all_evpn_es_downstream is not None:
                        cfg_dict['all-evpn-es-downstream'] = all_evpn_es_downstream
                    if all_mclags_downstream is not None:
                        cfg_dict['all-mclags-downstream'] = all_mclags_downstream
                    if group_description:
                        cfg_dict['description'] = group_description
                    if group_type:
                        cfg_dict['type'] = enum_dict[group_type]
                    if name:
                        cfg_dict['name'] = name
                    if threshold_down is not None:
                        cfg_dict['threshold-down'] = str(threshold_down)
                    if threshold_type:
                        cfg_dict['threshold-type'] = enum_dict[threshold_type]
                    if threshold_up is not None:
                        cfg_dict['threshold-up'] = str(threshold_up)
                    if timeout:
                        cfg_dict['timeout'] = timeout
                    if cfg_dict:
                        lst_group_list.append({'name': name, 'config': cfg_dict})
                if lst_group_list:
                    lst_dict['lst-groups'] = {'lst-group': lst_group_list}

            # Handle interfaces modification
            interfaces = commands.get('interfaces')
            if interfaces:
                interface_list = []
                for intf in interfaces:
                    intf_dict = {}
                    intf_id = intf.get('id')
                    downstream_group = intf.get('downstream_group')
                    upstream_groups = intf.get('upstream_groups')

                    if intf_id:
                        intf_dict.update({'id': intf_id, 'config': {'id': intf_id}})
                    if downstream_group:
                        intf_dict['downstream-group'] = {'config': {'group-name': downstream_group}}
                    if upstream_groups:
                        group_list = []
                        for group in upstream_groups:
                            group_name = group.get('group_name')
                            if group_name:
                                group_list.append({'group-name': group_name, 'config': {'group-name': group_name}})
                        if group_list:
                            intf_dict['upstream-groups'] = {'upstream-group': group_list}
                    if intf_dict:
                        interface_list.append(intf_dict)
                if interface_list:
                    lst_dict['interfaces'] = {'interface': interface_list}
            if lst_dict:
                payload = {'openconfig-lst-ext:lst': lst_dict}
                request = {'path': LST_PATH, 'method': PATCH, 'data': payload}

        return request

    def get_delete_lst_requests(self, commands, have, is_delete_all):
        requests = []

        if not commands or not have:
            return requests
        if is_delete_all:
            requests.append({'path': LST_PATH, 'method': DELETE})
            return requests

        config_dict = {}
        # Handle lst_groups deletion
        lst_groups = commands.get('lst_groups')
        cfg_lst_groups = have.get('lst_groups')
        if lst_groups and cfg_lst_groups:
            lst_groups_list = []
            cfg_group_dict = {cfg_group.get('name'): cfg_group for cfg_group in cfg_lst_groups}

            for group in lst_groups:
                name = group.get('name')
                cfg_group = cfg_group_dict.get(name)

                if not cfg_group:
                    continue
                lst_group_dict = {}
                all_evpn_es_downstream = group.get('all_evpn_es_downstream')
                all_mclags_downstream = group.get('all_mclags_downstream')
                group_description = group.get('group_description')
                group_type = group.get('group_type')
                threshold_down = group.get('threshold_down')
                threshold_type = group.get('threshold_type')
                threshold_up = group.get('threshold_up')
                timeout = group.get('timeout')
                cfg_all_evpn_es_downstream = cfg_group.get('all_evpn_es_downstream')
                cfg_all_mclags_downstream = cfg_group.get('all_mclags_downstream')
                cfg_group_description = cfg_group.get('group_description')
                cfg_group_type = cfg_group.get('group_type')
                cfg_threshold_down = cfg_group.get('threshold_down')
                cfg_threshold_type = cfg_group.get('threshold_type')
                cfg_threshold_up = cfg_group.get('threshold_up')
                cfg_timeout = cfg_group.get('timeout')

                if all_evpn_es_downstream is not None and all_evpn_es_downstream == cfg_all_evpn_es_downstream:
                    requests.append(self.get_delete_lst_groups_request(name, 'all-evpn-es-downstream'))
                    lst_group_dict.update({'name': name, 'all_evpn_es_downstream': all_evpn_es_downstream})

                if all_mclags_downstream is not None and all_mclags_downstream == cfg_all_mclags_downstream:
                    requests.append(self.get_delete_lst_groups_request(name, 'all-mclags-downstream'))
                    lst_group_dict.update({'name': name, 'all_mclags_downstream': all_mclags_downstream})

                if group_description and group_description == cfg_group_description:
                    requests.append(self.get_delete_lst_groups_request(name, 'description'))
                    lst_group_dict.update({'name': name, 'group_description': group_description})

                if group_type and group_type == cfg_group_type:
                    requests.append(self.get_delete_lst_groups_request(name, 'type'))
                    lst_group_dict.update({'name': name, 'group_type': group_type})

                if threshold_down is not None and threshold_down == cfg_threshold_down:
                    requests.append(self.get_delete_lst_groups_request(name, 'threshold-down'))
                    lst_group_dict.update({'name': name, 'threshold_down': threshold_down})

                if threshold_type and threshold_type == cfg_threshold_type:
                    requests.append(self.get_delete_lst_groups_request(name, 'threshold-type'))
                    lst_group_dict.update({'name': name, 'threshold_type': threshold_type})

                if threshold_up is not None and threshold_up == cfg_threshold_up:
                    requests.append(self.get_delete_lst_groups_request(name, 'threshold-up'))
                    lst_group_dict.update({'name': name, 'threshold_up': threshold_up})

                if timeout and timeout == cfg_timeout:
                    requests.append(self.get_delete_lst_groups_request(name, 'timeout'))
                    lst_group_dict.update({'name': name, 'timeout': timeout})

                if (all_evpn_es_downstream is None and all_mclags_downstream is None and not group_description and not group_type and threshold_down
                        is None and not threshold_type and threshold_up is None and not timeout):
                    requests.append(self.get_delete_lst_groups_request(name, None))
                    lst_group_dict['name'] = name
                if lst_group_dict:
                    lst_groups_list.append(lst_group_dict)
            if lst_groups_list:
                config_dict['lst_groups'] = lst_groups_list

        # Handle interfaces deletion
        interfaces = commands.get('interfaces')
        cfg_interfaces = have.get('interfaces')
        if interfaces and cfg_interfaces:
            interfaces_list = []
            cfg_intf_dict = {cfg_intf.get('id'): cfg_intf for cfg_intf in cfg_interfaces}

            for intf in interfaces:
                intf_id = intf.get('id')
                cfg_intf = cfg_intf_dict.get(intf_id)

                if not cfg_intf:
                    continue

                intf_dict = {}
                downstream_group = intf.get('downstream_group')
                upstream_groups = intf.get('upstream_groups')
                cfg_downstream_group = cfg_intf.get('downstream_group')
                cfg_upstream_groups = cfg_intf.get('upstream_groups')

                if downstream_group and downstream_group == cfg_downstream_group:
                    requests.append(self.get_delete_interfaces_request(intf_id, 'downstream-group'))
                    intf_dict.update({'id': intf_id, 'downstream_group': downstream_group})
                if upstream_groups and cfg_upstream_groups:
                    upstream_groups_list = []
                    for group in upstream_groups:
                        if group in cfg_upstream_groups:
                            group_name = group.get('group_name')
                            attr = f'upstream-groups/upstream-group={group_name}'
                            requests.append(self.get_delete_interfaces_request(intf_id, attr))
                            upstream_groups_list.append(group)
                    if upstream_groups_list:
                        intf_dict.update({'id': intf_id, 'upstream_groups': upstream_groups_list})
                if not downstream_group and not upstream_groups:
                    requests.append(self.get_delete_interfaces_request(intf_id, None))
                    intf_dict['id'] = intf_id
                if intf_dict:
                    interfaces_list.append(intf_dict)
            if interfaces_list:
                config_dict['interfaces'] = interfaces_list

        commands = config_dict
        return requests

    def get_delete_lst_groups_request(self, name, attr):
        url = f'{LST_PATH}/lst-groups/lst-group={name}'
        if attr:
            url += f'/config/{attr}'
        request = {'path': url, 'method': DELETE}
        return request

    def get_delete_interfaces_request(self, intf_id, attr):
        url = f'{LST_PATH}/interfaces/interface={intf_id}'
        if attr:
            url += f'/{attr}'
        request = {'path': url, 'method': DELETE}
        return request

    def remove_default_entries(self, data):
        lst_groups = data.get('lst_groups')

        if lst_groups:
            pop_list = []
            for group in lst_groups:
                pop_group = False

                if 'all_evpn_es_downstream' in group and group['all_evpn_es_downstream'] is False:
                    group.pop('all_evpn_es_downstream')
                    pop_group = True
                if 'all_mclags_downstream' in group and group['all_mclags_downstream'] is False:
                    group.pop('all_mclags_downstream')
                    pop_group = True
                if 'group_type' in group and group['group_type'] == 'l3':
                    group.pop('group_type')
                    pop_group = True
                if 'timeout' in group and group['timeout'] == 60:
                    group.pop('timeout')
                    pop_group = True
                if 'name' in group and len(group) == 1 and pop_group:
                    idx = lst_groups.index(group)
                    pop_list.insert(0, idx)
            for idx in pop_list:
                lst_groups.pop(idx)
            if not lst_groups:
                data.pop('lst_groups')

    def sort_lists_in_config(self, config):
        if config:
            if 'lst_groups' in config and config['lst_groups']:
                config['lst_groups'].sort(key=lambda x: x['name'])
            if 'interfaces' in config and config['interfaces']:
                config['interfaces'].sort(key=lambda x: x['id'])

    def get_replaced_config(self, want, have):
        config_dict = {}
        requests = []
        new_have = deepcopy(have)
        self.remove_default_entries(new_have)
        lst_groups = want.get('lst_groups')
        interfaces = want.get('interfaces')
        cfg_lst_groups = new_have.get('lst_groups')
        cfg_interfaces = new_have.get('interfaces')

        # Handle lst_groups replacement
        if lst_groups and cfg_lst_groups:
            lst_groups_list = []
            cfg_group_dict = {cfg_group.get('name'): cfg_group for cfg_group in cfg_lst_groups}

            for group in lst_groups:
                name = group.get('name')
                cfg_group = cfg_group_dict.get(name)

                if not cfg_group:
                    continue
                if group != cfg_group:
                    lst_groups_list.append(cfg_group)
                    requests.append(self.get_delete_lst_groups_request(name, None))
            if lst_groups_list:
                config_dict['lst_groups'] = lst_groups_list

        # Handle interfaces replacement
        if interfaces and cfg_interfaces:
            interfaces_list = []
            cfg_intf_dict = {cfg_intf.get('id'): cfg_intf for cfg_intf in cfg_interfaces}

            for intf in interfaces:
                intf_id = intf.get('id')
                cfg_intf = cfg_intf_dict.get(intf_id)

                if not cfg_intf:
                    continue
                if intf != cfg_intf:
                    interfaces_list.append(cfg_intf)
                    requests.append(self.get_delete_interfaces_request(intf_id, None))
            if interfaces_list:
                config_dict['interfaces'] = interfaces_list

        return config_dict, requests

    def post_process_generated_config(self, config):
        if 'lst_groups' in config and not config['lst_groups']:
            config.pop('lst_groups')

        interfaces = config.get('interfaces')
        if interfaces:
            pop_list = []
            for intf in interfaces:
                if 'upstream_groups' in intf and not intf['upstream_groups']:
                    intf.pop('upstream_groups')
                if 'id' in intf and len(intf) == 1:
                    idx = interfaces.index(intf)
                    pop_list.insert(0, idx)
            for idx in pop_list:
                interfaces.pop(idx)
            if not interfaces:
                config.pop('interfaces')
