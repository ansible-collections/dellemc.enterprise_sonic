#
# -*- coding: utf-8 -*-
# Copyright 2024 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_copp class
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
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    get_diff,
    get_replaced_config,
    remove_empties,
    update_states,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import Facts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.formatted_diff_utils import (
    __DELETE_CONFIG_IF_NO_NON_KEY_LEAF_OR_SUBCONFIG,
    __DELETE_LEAFS_THEN_CONFIG_IF_NO_NON_KEY_LEAF,
    get_new_config,
    get_formatted_config_diff
)


COPP_PATH = '/data/openconfig-copp-ext:copp'
PATCH = 'patch'
DELETE = 'delete'
TEST_KEYS = [
    {'copp_groups': {'copp_name': ''}},
    {'copp_traps': {'name': ''}}
]


def __derive_copp_delete_op(key_set, command, exist_conf):
    new_conf = exist_conf
    done, new_conf = __DELETE_CONFIG_IF_NO_NON_KEY_LEAF_OR_SUBCONFIG(key_set, command, exist_conf)
    if done:
        return done, new_conf
    return __DELETE_LEAFS_THEN_CONFIG_IF_NO_NON_KEY_LEAF(key_set, command, new_conf)


TEST_KEYS_generate_config = [
    {'copp_groups': {'copp_name': '', '__delete_op': __derive_copp_delete_op}},
    {'copp_traps': {'name': '', '__delete_op': __derive_copp_delete_op}}
]
reserved_copp_names = [
    'copp-system-arp',
    'copp-system-bfd',
    'copp-system-bgp',
    'copp-system-cdp',
    'copp-system-default',
    'copp-system-dhcp',
    'copp-system-dhcpl2',
    'copp-system-iccp',
    'copp-system-icmp',
    'copp-system-igmp',
    'copp-system-ip2me',
    'copp-system-lacp',
    'copp-system-lldp',
    'copp-system-mtu',
    'copp-system-nat',
    'copp-system-ospf',
    'copp-system-pim',
    'copp-system-ptp',
    'copp-system-sflow',
    'copp-system-stp',
    'copp-system-subnet',
    'copp-system-suppress',
    'copp-system-ttl',
    'copp-system-udld',
    'copp-system-vrrp',
    'default'
]


class Copp(ConfigBase):
    """
    The sonic_copp class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'copp',
    ]

    def __init__(self, module):
        super(Copp, self).__init__(module)

    def get_copp_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        copp_facts = facts['ansible_network_resources'].get('copp')
        if not copp_facts:
            return {}
        return copp_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = []
        commands = []

        existing_copp_facts = self.get_copp_facts()
        commands, requests = self.set_config(existing_copp_facts)
        if commands and len(requests) > 0:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        changed_copp_facts = self.get_copp_facts()

        result['before'] = existing_copp_facts
        if result['changed']:
            result['after'] = changed_copp_facts

        new_config = changed_copp_facts
        old_config = existing_copp_facts
        if self._module.check_mode:
            result.pop('after', None)
            new_config = get_new_config(commands, existing_copp_facts,
                                        TEST_KEYS_generate_config)
            self.sort_lists_in_config(new_config)
            result['after(generated)'] = new_config

        if self._module._diff:
            self.sort_lists_in_config(new_config)
            self.sort_lists_in_config(old_config)
            result['diff'] = get_formatted_config_diff(old_config,
                                                       new_config,
                                                       self._module._verbosity)
        result['warnings'] = warnings
        return result

    def set_config(self, existing_copp_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = remove_empties(self._module.params['config'])
        have = existing_copp_facts
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

        if state == 'overridden':
            commands, requests = self._state_overridden(want, have)
        elif state == 'deleted':
            commands, requests = self._state_deleted(want, have)
        elif state == 'merged':
            commands, requests = self._state_merged(diff)
        elif state == 'replaced':
            commands, requests = self._state_replaced(want, have, diff)
        return commands, requests

    def _state_replaced(self, want, have, diff):
        """ The command generator when state is replaced
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        self.validate_want_for_replaced_overridden(want, 'Replaced')
        commands = []
        mod_commands = []
        requests = []
        replaced_config = get_replaced_config(want, have, TEST_KEYS)

        if replaced_config:
            self.sort_lists_in_config(replaced_config)
            self.sort_lists_in_config(have)
            is_delete_all = replaced_config == have

            # trap_action cannot be deleted
            copp_groups = replaced_config.get('copp_groups', [])
            for group in copp_groups:
                if 'trap_action' in group and group['trap_action']:
                    group.pop('trap_action')

            del_requests = self.get_delete_copp_requests(replaced_config, have, is_delete_all)
            requests.extend(del_requests)
            commands.extend(update_states(replaced_config, 'deleted'))
            mod_commands = want
        else:
            mod_commands = diff

        if mod_commands:
            mod_request = self.get_modify_copp_groups_request(mod_commands)

            if mod_request:
                requests.append(mod_request)
                commands.extend(update_states(mod_commands, 'replaced'))

        return commands, requests

    def _state_overridden(self, want, have):
        """ The command generator when state is overridden
        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :param diff: the difference between want and have
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        self.validate_want_for_replaced_overridden(want, 'Overridden')
        commands = []
        requests = []
        self.sort_lists_in_config(want)
        self.sort_lists_in_config(have)
        new_have = deepcopy(have)
        new_have = self.filter_copp(new_have)

        if new_have and new_have != want:
            is_delete_all = True
            del_requests = self.get_delete_copp_requests(new_have, None, is_delete_all)
            requests.extend(del_requests)
            commands.extend(update_states(new_have, 'deleted'))
            new_have = []

        if not new_have and want:
            mod_commands = want
            mod_request = self.get_modify_copp_groups_request(mod_commands)

            if mod_request:
                requests.append(mod_request)
                commands.extend(update_states(mod_commands, 'overridden'))

        return commands, requests

    def _state_merged(self, diff):
        """ The command generator when state is merged
        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = diff
        requests = self.get_modify_copp_groups_request(commands)

        if commands and len(requests) > 0:
            commands = update_states(commands, "merged")
        else:
            commands = []

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
            commands = self.filter_copp(commands)
        else:
            commands = deepcopy(want)

        requests = self.get_delete_copp_requests(commands, have, is_delete_all)
        if commands and len(requests) > 0:
            commands = update_states(commands, "deleted")
        else:
            commands = []

        return commands, requests

    def get_modify_copp_groups_request(self, commands):
        request = None
        copp_dict = {}

        copp_groups = commands.get('copp_groups')
        if copp_groups:
            group_list = []
            for group in copp_groups:
                config_dict = {}
                group_dict = {}
                copp_name = group.get('copp_name')
                trap_priority = group.get('trap_priority')
                trap_action = group.get('trap_action')
                queue = group.get('queue')
                cir = group.get('cir')
                cbs = group.get('cbs')

                if copp_name:
                    config_dict['name'] = copp_name
                    group_dict['name'] = copp_name
                if trap_priority:
                    config_dict['trap-priority'] = trap_priority
                if trap_action:
                    config_dict['trap-action'] = trap_action.upper()
                if queue:
                    config_dict['queue'] = queue
                if cir:
                    config_dict['cir'] = cir
                if cbs:
                    config_dict['cbs'] = cbs
                if config_dict:
                    group_dict['config'] = config_dict
                    group_list.append(group_dict)
            if group_list:
                copp_dict['copp-groups'] = {'copp-group': group_list}

        copp_traps = commands.get('copp_traps')
        if copp_traps:
            trap_list = []
            for trap in copp_traps:
                config_dict = {}
                trap_dict = {}
                name = trap.get('name')
                trap_ids = trap.get('trap_ids')
                trap_group = trap.get('trap_group')

                if name:
                    config_dict['name'] = name
                    trap_dict['name'] = name
                if trap_ids:
                    config_dict['trap-ids'] = trap_ids
                if trap_group:
                    config_dict['trap-group'] = trap_group
                if config_dict:
                    trap_dict['config'] = config_dict
                    trap_list.append(trap_dict)
            if trap_list:
                copp_dict['copp-traps'] = {'copp-trap': trap_list}

        if copp_dict:
            payload = {'openconfig-copp-ext:copp': copp_dict}
            request = {'path': COPP_PATH, 'method': PATCH, 'data': payload}

        return request

    def get_delete_copp_requests(self, commands, have, is_delete_all):
        requests = []

        if is_delete_all:
            copp_traps = commands.get('copp_traps')
            if copp_traps:
                for trap in copp_traps:
                    name = trap.get('name')
                    trap_group = trap.get('trap_group')

                    # Must unbound trap before deleting i.e delete trap_group
                    if trap_group:
                        requests.append(self.get_delete_copp_trap_request(name, 'trap-group'))
                    requests.append(self.get_delete_copp_trap_request(name, None))

            copp_groups = commands.get('copp_groups')
            if copp_groups:
                for group in copp_groups:
                    copp_name = group.get('copp_name')
                    requests.append(self.get_delete_copp_group_request(copp_name, None))

            return requests

        config_dict = {}
        # Handle copp_traps deletion
        copp_traps = commands.get('copp_traps')
        cfg_copp_traps = have.get('copp_traps')
        if copp_traps and cfg_copp_traps:
            traps_list = []
            cfg_trap_dict = {cfg_trap.get('name'): cfg_trap for cfg_trap in cfg_copp_traps}

            for trap in copp_traps:
                name = trap.get('name')
                cfg_trap = cfg_trap_dict.get(name)

                if not cfg_trap:
                    continue
                trap_dict = {}
                trap_ids = trap.get('trap_ids')
                trap_group = trap.get('trap_group')
                cfg_trap_ids = cfg_trap.get('trap_ids')
                cfg_trap_group = cfg_trap.get('trap_group')

                if trap_ids and trap_ids == cfg_trap_ids:
                    requests.append(self.get_delete_copp_trap_request(name, 'trap-ids'))
                    trap_dict.update({'name': name, 'trap_ids': trap_ids})
                if trap_group and trap_group == cfg_trap_group:
                    requests.append(self.get_delete_copp_trap_request(name, 'trap-group'))
                    trap_dict.update({'name': name, 'trap_group': trap_group})
                if not trap_ids and not trap_group:
                    requests.append(self.get_delete_copp_trap_request(name, None))
                    trap_dict['name'] = name
                if trap_dict:
                    traps_list.append(trap_dict)
            if traps_list:
                config_dict['copp_traps'] = traps_list

        # Handle copp_groups deletion
        copp_groups = commands.get('copp_groups')
        cfg_copp_groups = have.get('copp_groups')
        if copp_groups and cfg_copp_groups:
            groups_list = []
            cfg_group_dict = {cfg_group.get('copp_name'): cfg_group for cfg_group in cfg_copp_groups}

            for group in copp_groups:
                copp_name = group.get('copp_name')
                cfg_group = cfg_group_dict.get(copp_name)

                if not cfg_group:
                    continue
                group_dict = {}
                trap_priority = group.get('trap_priority')
                trap_action = group.get('trap_action')
                queue = group.get('queue')
                cir = group.get('cir')
                cbs = group.get('cbs')
                cfg_trap_priority = cfg_group.get('trap_priority')
                cfg_trap_action = cfg_group.get('trap_action')
                cfg_queue = cfg_group.get('queue')
                cfg_cir = cfg_group.get('cir')
                cfg_cbs = cfg_group.get('cbs')

                if trap_priority and trap_priority == cfg_trap_priority:
                    requests.append(self.get_delete_copp_group_request(copp_name, 'trap-priority'))
                    group_dict.update({'copp_name': copp_name, 'trap_priority': trap_priority})
                if trap_action and trap_action == cfg_trap_action:
                    self._module.fail_json(msg='Deletion of trap-action attribute is not supported.')
                if queue and queue == cfg_queue:
                    requests.append(self.get_delete_copp_group_request(copp_name, 'queue'))
                    group_dict.update({'copp_name': copp_name, 'queue': queue})
                if cir and cir == cfg_cir:
                    requests.append(self.get_delete_copp_group_request(copp_name, 'cir'))
                    group_dict.update({'copp_name': copp_name, 'cir': cir})
                if cbs and cbs == cfg_cbs:
                    requests.append(self.get_delete_copp_group_request(copp_name, 'cbs'))
                    group_dict.update({'copp_name': copp_name, 'cbs': cbs})
                if not trap_priority and not trap_action and not queue and not cir and not cbs:
                    requests.append(self.get_delete_copp_group_request(copp_name, None))
                    group_dict['copp_name'] = copp_name
                if group_dict:
                    groups_list.append(group_dict)
            if groups_list:
                config_dict['copp_groups'] = groups_list

        commands = config_dict
        return requests

    def get_delete_copp_group_request(self, copp_name, attr):
        url = '%s/copp-groups/copp-group=%s' % (COPP_PATH, copp_name)
        if attr:
            url += '/config/%s' % (attr)
        request = {'path': url, 'method': DELETE}
        return request

    def get_delete_copp_trap_request(self, name, attr):
        url = '%s/copp-traps/copp-trap=%s' % (COPP_PATH, name)
        if attr:
            url += '/config/%s' % (attr)
        request = {'path': url, 'method': DELETE}
        return request

    def filter_copp(self, commands):
        cfg_dict = {}

        if commands:
            copp_groups = commands.get('copp_groups')
            if copp_groups:
                copp_groups_list = []
                for group in copp_groups:
                    copp_name = group.get('copp_name')
                    if copp_name not in reserved_copp_names:
                        copp_groups_list.append(group)
                if copp_groups_list:
                    cfg_dict['copp_groups'] = copp_groups_list

            copp_traps = commands.get('copp_traps')
            if copp_traps:
                copp_traps_list = []
                for trap in copp_traps:
                    name = trap.get('name')
                    if name not in reserved_copp_names:
                        copp_traps_list.append(trap)
                if copp_traps_list:
                    cfg_dict['copp_traps'] = copp_traps_list

        return cfg_dict

    def sort_lists_in_config(self, config):
        if 'copp_groups' in config and config['copp_groups'] is not None:
            config['copp_groups'].sort(key=lambda x: x['copp_name'])
        if 'copp_traps' in config and config['copp_traps'] is not None:
            config['copp_traps'].sort(key=lambda x: x['name'])

    def validate_want_for_replaced_overridden(self, want, state):
        if want:
            copp_groups = want.get('copp_groups')
            if copp_groups:
                for group in copp_groups:
                    copp_name = group.get('copp_name')
                    if copp_name in reserved_copp_names:
                        self._module.fail_json(msg=state + ' not supported for reserved CoPP classifier. Use merged and/or deleted state(s).')

            copp_traps = want.get('copp_traps')
            if copp_traps:
                for trap in copp_traps:
                    name = trap.get('name')
                    if name in reserved_copp_names:
                        self._module.fail_json(msg=state + ' not supported for reserved CoPP classifier. Use merged and/or deleted state(s).')
