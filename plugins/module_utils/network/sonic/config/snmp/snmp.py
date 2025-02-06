#
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_snmp class
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
    ConfigBase
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import Facts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    update_states,
    get_diff,
    remove_empties
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.formatted_diff_utils import (
    get_new_config,
    get_formatted_config_diff
)

PATCH = 'patch'
DELETE = 'delete'
TEST_KEYS = [
    {'agentaddress': {'ip': ''}},
    {'community': {'name': ''}},
    {'group': {'name': ''}},
    {'view': {'name': ''}}
]
TEST_KEYS_generate_config = [
    {'agentaddress': {'ip': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}},
    {'community': {'name': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}},
    {'group': {'name': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}},
    {'view': {'name': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}}
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
            return {}
        return snmp_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = []
        commands = []

        existing_snmp_facts = self.get_snmp_facts()
        commands, requests = self.set_config(existing_snmp_facts)

        if commands and len(requests) > 0:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        result['before'] = existing_snmp_facts
        old_config = existing_snmp_facts
        if self._module.check_mode:
            new_config = get_new_config(commands, existing_snmp_facts, TEST_KEYS_generate_config)
            result['after(generated)'] = new_config
        else:
            new_config = self.get_snmp_facts()
            if result['changed']:
                result['after'] = new_config

        if self._module._diff:
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
        have = existing_snmp_facts
        want = remove_empties(self._module.params['config'])
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
        diff = get_diff(want, have, TEST_KEYS)

        if state == 'overridden':
            kwargs = {}
            commands, requests = self._state_overridden(want, have)
        elif state == 'deleted':
            kwargs = {}
            commands, requests = self._state_deleted(want, have)
        elif state == 'merged':
            kwargs = {}
            commands, requests = self._state_merged(want, have)
        elif state == 'replaced':
            kwargs = {}
            commands, requests = self._state_replaced(want, have)
        
        return commands, requests

    def _state_replaced(self, want, have):
        """ The command generator when state is replaced
        
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands, requests = [], []
        replaced_config = get_replaced_config(want, have, TEST_KEYS)

        if replaced_config:
            is_delete_all = replaced_config == have
            if is_delete_all:
                del_commands, del_requests = self.get_delete_all_snmp_request(replaced_config)
            else:
                del_commands, del_requests = self.get_delete_snmp_request(replaced_config)
            requests.extend(del_requests)
            commands.extend(update_states(del_commands, 'deleted'))

        if want:
            new_requests = self.get_create_snmp_request(want)
            if len(new_requests) > 0:
                requests.extend(new_requests)
                commands.extend(update_states(want, 'replaced'))

        return commands, requests

    def _state_overridden(self, want, have):
        """ The command generator when state is overridden

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands, requests = [], []
        replaced_config = get_replaced_config(want, have, TEST_KEYS)

        if replaced_config:
            is_delete_all = replaced_config == have
            if is_delete_all:
                del_commands, del_requests = self.get_delete_all_snmp_request(replaced_config)
            else:
                del_commands, del_requests = self.get_delete_snmp_request(replaced_config)
            requests.extend(del_requests)
            commands.extend(update_states(del_commands, 'deleted'))

        if want:
            new_requests = self.get_create_snmp_request(want)
            if len(new_requests) > 0:
                requests.extend(new_requests)
                commands.extend(update_states(want, 'overridden'))

        return commands, requests


    def _state_merged(self, want, have):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = get_diff(want, have)
        requests = []

        if want:
            new_requests = self.get_create_snmp_request(want)
            if len(new_requests) > 0:
                requests.extend(new_requests)
                commands.extend(update_states(want, 'merged'))

        return commands, requests

    def _state_deleted(self, want, have):
        """ The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        commands, requests = [], []
        is_delete_all = False

        if not want:
            commands = deepcopy(have)
            is_delete_all = True
        else:
            commands - deepcopy(want)

        new_have = remove_empties(new_have)
        new_want = remove_empties(new_want)


        if is_delete_all:
            requests = self.get_delete_all_snmp_request(commands)
        else:
            requests = self.get_delete_snmp_request(new_want)

        if commands:
            commands = update_states(commands, 'deleted')
        else:
            commands = []

        return commands, requests

    def _get_replaced_config(self, want, have):
        replaced_config = dict()

        # Compare the 'agentaddress' configuration
        if 'agentaddress' in want and 'agentaddress' in have:
            want_agentaddresses = want.get('agentaddress')
            have_agentaddresses = have.get('agentaddress')

            replaced_agentaddress = []
            for want_agentaddress in want_agentaddresses:
                have_agentaddress = next((h for h in have_agentaddresses if h['ip'] == want_agentaddress['ip']), None)

                if have_agentaddress and want_agentaddress != have_agentaddress:
                    replaced_agentaddress.append(have_agentaddress)
            
            if replaced_agentaddress:
                replaced_config['agentaddress'] = replaced_agentaddress

        # Compare the 'community' configuration
        if 'community' in want and 'community' in have:
            want_communities = want.get('community')
            have_communities = have.get('community')

            replaced_community = []
            for want_community in want_communities:
                have_community = next((c for c in have_communities if c['name'] == want_community['name']), None)
                if have_community and want_community != have_community:
                    replaced_community.append(have_community)

            if replaced_community:
                replaced_config['community'] = replaced_community 

        # Compare the 'users' configuration
        if 'user' in want and 'user' in have:
            want_users = want.get('user')
            have_users = have.get('user')

            replaced_users = []
            for want_user in want_users:
                have_user = next((u for u in have_users if u['name'] == want_user['name']), None)
                if have_user and want_user != have_user:
                    replaced_users.append(have_user)

            if replaced_users:
                replaced_config['user'] = replaced_users

        # Compare the 'views' configuration
        if 'view' in want and 'view' in have:
            want_views = want.get('view')
            have_views = have.get('view')

            replaced_views = []
            for want_view in want_views:
                have_view = next((v for v in have_views if v['name'] == want_view['name']), None)
                if have_view and want_view != have_view:
                    replaced_views.append(have_view)

            if replaced_views:
                replaced_config['view'] = replaced_views
        
        # Compare the 'group' configuration
        if 'group' in want and 'group' in have:
            want_groups = want.get('group')
            have_groups = have.get('group')

            replaced_groups = []
            for want_group in want_groups:
                have_group = next((g for g in have_groups if g['name'] == want_group['name']), None)
                if have_group and want_group != have_group:
                    replaced_groups.append(have_group)
            
            if replaced_groups:
                replaced_config['group'] = replaced_groups

        # Compare the 'host' configuration
        if 'host' in want and 'host' in have:
            want_hosts = want.get('host')
            have_hosts = have.get('host')

            replaced_hosts = []
            for want_host in want_hosts:
                have_host = next((h for h in have_hosts if h['ip'] == want_host['ip']), None)
                if have_host and want_host != have_host:
                    replaced_hosts.append(have_host)
            
            if replaced_hosts:
                replaced_config['host'] = replaced_hosts

        return replaced_config


    def get_create_snmp_request(self, config):
        requests = []

        # Create URL and payload
        method = PATCH
        url = 'data/ietf-snmp:snmp/'
        payload = {'sonic-snmp:sonic-snmp': config}
        request = {'path': url, 'method': method, 'data': payload}
        requests.append(request)

        if config.get('agentaddress'):
            agentaddress_path = 'data/ietf-snmp:snmp/engine'
            agentaddress_request = {'path': agentaddress_path, 'method': method, 'data': config.get('agentaddress')}
            requests.append(agentaddress_request)

        if config.get('community'):
            community_path = 'data/ietf-snmp:snmp/community'
            community_request = {'path': community_path, 'method': method, 'data': config.get('community')}
            requests.append(community_request)
        
        if  config.get('engine'):
            engine_path = 'data/ietf-snmp:snmp/engine'
            engine_request = {'path': engine_path, 'method': method, 'data': config.get('engine')}
            requests.append(engine_request)

        if config.get('user'):
            users_path = 'data/ietf-snmp:snmp/usm/local/user'
            users_request = {'path': users_path, "method": method, 'data': config.get('user')}
            requests.append(users_request)

        if config.get('view'):
            views_path = 'data/ietf-snmp:snmp/view'
            views_request = {'path': views_path, 'method': method, 'data': config.get('view')}
            requests.append(views_request)
        
        if config.get('contact'):
            contact_path = 'data/ietf-snmp:snmp/ietf-snmp-ext:system/contact'
            contact_request = {'path': contact_path, 'method': method, 'data': config.get('contact')}
            requests.append(contact_request)

        if config.get('location'):
            location_path = 'data/ietf-snmp:snmp/ietf-snmp-ext:system/location'
            location_request = {'path': location_path, 'method': method, 'data': config.get('location')}
            requests.append(location_request)
        
        if config.get('enable_trap'):
            enable_trap_path = 'data/ietf-snmp:snmp/ietf-snmp-ext:system/notifications'
            enable_trap_request = {'path': enable_trap_path, 'method': method, 'data': config.get('enable_trap')}
            requests.append(enable_trap_request)

        if config.get('group'):
            group_path = 'data/ietf-snmp:snmp/vacm/group'
            group_request = {'path': group_path, 'method': method, 'data': config.get('group')}
            requests.append(group_request)
        
        if config.get('host'):
            target_path = 'data/ietf-snmp:snmp/target'
            target_params_path = 'data/ietf-snmp:snmp/target-params'
            target_request = {'path': target_path, 'method': method, 'data': config.get('host')}
            target_params_path = {'path': target_params_path, 'method': method, 'data': config.get('host')}
            requests.append(target_request)
            requests.append(target_params_path)

        return requests


    def get_delete_all_snmp_request(self, configs):
        requests = []

        for conf in configs:
            request = self.get_delete_snmp_request(conf)
            requests.append(request)

        return requests

    def get_delete_snmp_request(self, want):
        delete_path = 'data/ietf-snmp:snmp/%s' % (want)
        return (('path': delete_path, 'method': DELETE))
