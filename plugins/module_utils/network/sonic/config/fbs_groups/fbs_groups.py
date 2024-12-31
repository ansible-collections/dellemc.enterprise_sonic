#
# -*- coding: utf-8 -*-
# Copyright 2024 Dell Inc. or its subsidiaries. All Rights Reserved.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_fbs_groups class
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
    __DELETE_LEAFS_OR_CONFIG_IF_NO_NON_KEY_LEAF,
    get_new_config,
    get_formatted_config_diff
)

FBS_PATH = 'data/openconfig-fbs-ext:fbs'
PATCH = 'patch'
DELETE = 'delete'
TEST_KEYS = [
    {'next_hop_groups': {'group_name': ''}},
    {'replication_groups': {'group_name': ''}},
    {'next_hops': {'entry_id': ''}},
]
TEST_KEYS_generate_config = [
    {'next_hop_groups': {'group_name': '', '__delete_op': __DELETE_LEAFS_OR_CONFIG_IF_NO_NON_KEY_LEAF}},
    {'replication_groups': {'group_name': '', '__delete_op': __DELETE_LEAFS_OR_CONFIG_IF_NO_NON_KEY_LEAF}},
    {'next_hops': {'entry_id': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}}
]


class Fbs_groups(ConfigBase):
    """
    The sonic_fbs_groups class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'fbs_groups',
    ]

    def __init__(self, module):
        super(Fbs_groups, self).__init__(module)

    def get_fbs_groups_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        fbs_groups_facts = facts['ansible_network_resources'].get('fbs_groups')
        if not fbs_groups_facts:
            return {}
        return fbs_groups_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = []
        commands = []

        existing_fbs_groups_facts = self.get_fbs_groups_facts()
        commands, requests = self.set_config(existing_fbs_groups_facts)
        if commands and len(requests) > 0:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        changed_fbs_groups_facts = self.get_fbs_groups_facts()

        result['before'] = existing_fbs_groups_facts
        if result['changed']:
            result['after'] = changed_fbs_groups_facts

        new_config = changed_fbs_groups_facts
        old_config = existing_fbs_groups_facts
        if self._module.check_mode:
            result.pop('after', None)
            new_config = get_new_config(commands, existing_fbs_groups_facts, TEST_KEYS_generate_config)
            self.post_process_generated_config(new_config)
            result['after(generated)'] = new_config
        if self._module._diff:
            result['diff'] = get_formatted_config_diff(old_config,
                                                       new_config,
                                                       self._module._verbosity)
        result['warnings'] = warnings
        return result

    def set_config(self, existing_fbs_groups_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = remove_empties(self._module.params['config'])
        have = existing_fbs_groups_facts
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
        diff = get_diff(want, have)

        if state == 'merged':
            commands, requests = self._state_merged(diff)
        elif state == 'replaced':
            commands, requests = self._state_replaced(want, have, diff)
        elif state == 'overridden':
            commands, requests = self._state_overridden(want, have, diff)
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
        requests = self.get_modify_fbs_groups_requests(commands)

        if commands and len(requests) > 0:
            commands = update_states(commands, 'merged')
        else:
            commands = []

        return commands, requests

    def _state_overridden(self, want, have, diff):
        """ The command generator when state is overridden

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        requests = []
        mod_commands = None
        mod_requests = None
        del_commands = get_diff(have, want, TEST_KEYS)

        if not del_commands and diff:
            mod_commands = diff
            mod_requests = self.get_modify_fbs_groups_requests(mod_commands)

        if del_commands:
            is_delete_all = True
            del_requests = self.get_delete_fbs_groups_requests(del_commands, is_delete_all)
            requests.extend(del_requests)
            commands.extend(update_states(have, 'deleted'))
            mod_commands = want
            mod_requests = self.get_modify_fbs_groups_requests(mod_commands)

        if mod_requests:
            requests.extend(mod_requests)
            commands.extend(update_states(mod_commands, 'overridden'))

        return commands, requests

    def _state_deleted(self, want, have):
        """ The command generator when state is deleted
        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        is_delete_all = False
        requests = []
        diff = get_diff(want, have, TEST_KEYS)

        if not want:
            commands = deepcopy(have)
            is_delete_all = True
        else:
            commands = get_diff(want, diff, TEST_KEYS)

        if commands:
            requests = self.get_delete_fbs_groups_requests(commands, is_delete_all)
            if len(requests) > 0:
                commands = update_states(commands, 'deleted')
        else:
            commands = []

        return commands, requests

    def get_modify_fbs_groups_requests(self, commands):
        """Returns a single OC patch request constructed from commands"""
        requests = []
        fbs_dict = {}

        if commands:
            next_hop_groups = commands.get('next_hop_groups')
            replication_groups = commands.get('replication_groups')

            if next_hop_groups:
                next_hop_group_list = self.get_group_list_payload(next_hop_groups, 'next_hop_group_', requests)
                fbs_dict['next-hop-groups'] = {'next-hop-group': next_hop_group_list}
            if replication_groups:
                replication_group_list = self.get_group_list_payload(replication_groups, 'replication_group_', requests)
                fbs_dict['replication-groups'] = {'replication-group': replication_group_list}
            if fbs_dict:
                payload = {'openconfig-fbs-ext:fbs': fbs_dict}
                requests.append({'path': FBS_PATH, 'method': PATCH, 'data': payload})

        return requests

    def get_group_list_payload(self, groups_cfg, enum_prefix, requests):
        """Returns OC formatted list constructed from groups_cfg that will
        be a part of request payload"""
        group_list = []
        enum_dict = {
            'next_hop_group_ipv4': 'NEXT_HOP_GROUP_TYPE_IPV4',
            'next_hop_group_ipv6': 'NEXT_HOP_GROUP_TYPE_IPV6',
            'replication_group_ipv4': 'REPLICATION_GROUP_TYPE_IPV4',
            'replication_group_ipv6': 'REPLICATION_GROUP_TYPE_IPV6',
            'non_recursive': 'NEXT_HOP_TYPE_NON_RECURSIVE',
            'overlay': 'NEXT_HOP_TYPE_OVERLAY',
            'recursive': 'NEXT_HOP_TYPE_RECURSIVE'
        }

        for group in groups_cfg:
            group_dict = {}
            group_name = group.get('group_name')
            group_description = group.get('group_description')
            group_type = group.get('group_type')
            next_hops = group.get('next_hops')

            if group_name:
                group_dict.update({'group-name': group_name, 'config': {'name': group_name}})
            if group_description:
                group_dict['config']['description'] = group_description
            if group_type:
                enum_key = enum_prefix + group_type
                group_dict['config']['group-type'] = enum_dict[enum_key]
            else:
                self._module.fail_json(msg='group_type is required')
            if next_hops:
                next_hop_list = []
                for hop in next_hops:
                    hop_dict = {}
                    entry_id = hop.get('entry_id')
                    ip_address = hop.get('ip_address')
                    network_instance = hop.get('network_instance')
                    next_hop_type = hop.get('next_hop_type')
                    single_copy = hop.get('single_copy')

                    if entry_id:
                        hop_dict.update({'entry-id': entry_id, 'config': {'entry-id': entry_id}})
                    if ip_address:
                        hop_dict['config']['ip-address'] = ip_address
                    else:
                        self._module.fail_json(msg='ip_address required for next-hop entry')
                    if network_instance:
                        hop_dict['config']['network-instance'] = network_instance
                    if next_hop_type:
                        hop_dict['config']['next-hop-type'] = enum_dict[next_hop_type]
                    if single_copy:
                        hop_dict['config']['single-copy'] = single_copy
                    elif single_copy is False:
                        requests.append(self.get_delete_next_hops_request('replication-group', group_name, entry_id, 'single-copy'))
                    if hop_dict:
                        next_hop_list.append(hop_dict)
                if next_hop_list:
                    group_dict['next-hops'] = {'next-hop': next_hop_list}
            if group_dict:
                group_list.append(group_dict)

        return group_list

    def get_delete_fbs_groups_requests(self, commands, is_delete_all):
        """Returns OC delete requests"""
        requests = []

        if not commands:
            return requests
        if is_delete_all:
            requests.append(self.get_delete_groups_request('next-hop-group', None, None))
            requests.append(self.get_delete_groups_request('replication-group', None, None))
            return requests

        next_hop_groups = commands.get('next_hop_groups')
        if next_hop_groups:
            self.update_delete_fbs_groups_data(requests, next_hop_groups, 'next-hop-group')

        replication_groups = commands.get('replication_groups')
        if replication_groups:
            self.update_delete_fbs_groups_data(requests, replication_groups, 'replication-group')

        return requests

    def update_delete_fbs_groups_data(self, requests, groups, oc_group):
        """Updates requests for deletion"""

        for group in groups:
            group_name = group.get('group_name')
            group_description = group.get('group_description')
            group_type = group.get('group_type')
            next_hops = group.get('next_hops')

            if group_description:
                requests.append(self.get_delete_groups_request(oc_group, group_name, 'description'))
            if group_type:
                self._module.fail_json(msg='Deletion of group_type not supported')
            if next_hops:
                for hop in next_hops:
                    entry_id = hop.get('entry_id')
                    ip_address = hop.get('ip_address')
                    network_instance = hop.get('network_instance')
                    next_hop_type = hop.get('next_hop_type')
                    single_copy = hop.get('single_copy')

                    if ip_address:
                        self._module.fail_json(msg='Deletion of ip_address not supported')
                    if network_instance:
                        requests.append(self.get_delete_next_hops_request(oc_group, group_name, entry_id, 'network-instance'))
                    if next_hop_type:
                        requests.append(self.get_delete_next_hops_request(oc_group, group_name, entry_id, 'next-hop-type'))
                    if single_copy is not None:
                        requests.append(self.get_delete_next_hops_request(oc_group, group_name, entry_id, 'single-copy'))
                    if not ip_address and not network_instance and not next_hop_type and single_copy is None:
                        requests.append(self.get_delete_next_hops_request(oc_group, group_name, entry_id, None))
            if not group_type and not next_hops:
                requests.append(self.get_delete_groups_request(oc_group, group_name, None))

    def get_delete_groups_request(self, group, group_name, attr):
        url = '%s/%ss' % (FBS_PATH, group)

        if group_name:
            url += '/%s=%s' % (group, group_name)
        if attr:
            url += '/config/%s' % (attr)
        request = {'path': url, 'method': DELETE}
        return request

    def get_delete_next_hops_request(self, group, group_name, entry_id, attr):
        url = '%s/%ss/%s=%s/next-hops/next-hop=%s' % (FBS_PATH, group, group, group_name, entry_id)

        if attr:
            url += '/config/%s' % (attr)
        request = {'path': url, 'method': DELETE}
        return request

    def sort_lists_in_config(self, config):
        if config:
            if config.get('next_hop_groups'):
                config['next_hop_groups'].sort(key=lambda x: x['group_name'])
                for group in config['next_hop_groups']:
                    if group.get('next_hops'):
                        group['next_hops'].sort(key=lambda x: x['entry_id'])
            if config.get('replication_groups'):
                config['replication_groups'].sort(key=lambda x: x['group_name'])
                for group in config['replication_groups']:
                    if group.get('next_hops'):
                        group['next_hops'].sort(key=lambda x: x['entry_id'])

    def post_process_generated_config(self, config):
        fbs_groups = ['next_hop_groups', 'replication_groups']

        for groups in fbs_groups:
            pop_list = []
            if config.get(groups):
                for group in config[groups]:
                    if 'next_hops' in group and not group['next_hops']:
                        group.pop('next_hops')
                    if 'group_name' in group and len(group) == 1:
                        pop_list.insert(0, config[groups].index(group))
                for idx in pop_list:
                    config[groups].pop(idx)
                    if not config[groups]:
                        config.pop(groups)
