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
    remove_empties,
    send_requests
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
            new_config = get_new_config(commands, existing_snmp_facts)
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
        replaced_config = get_replaced_config(want, have)

        if replaced_config:
            is_delete_all = replaced_config == have
            if is_delete_all:
                del_commands, del_requests = self.get_delete_all_snmp_request(have)
            else:
                del_commands, del_requests = self.get_delete_snmp_request(replaced_config, have)
            requests = del_requests
            commands =update_states(del_commands, 'deleted')

        add_commands = get_diff(want, have)
        if add_commands:
            commands.extend(update_states(add_commands, 'replaced'))
            requests.extend(self.get_create_snmp_request(have))

        return commands, requests

    def _state_overridden(self, want, have):
        """ The command generator when state is overridden

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """

        if have and have != want:
            requests = self.get_delete_all_snmp_request(have)
            send_requests(self._module, requests)
            have = []

        commands, requests = [], []

        if not have and want:
            commands = want
            requests =self.get_create_snmp_request(have)

            if len(requests) > 0:
                commands = update_states(commands, 'overridden')
            else:
                commands = []
        
        
        return commands, requests


    def _state_merged(self, want, have):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = get_diff(want, have)
        requests = self.get_create_snmp_request(have)

        if len(have) == 0:
            commands = []
        
        if commands:
            commands = update_states(commands, 'merged')

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
            commands = deepcopy(want)
            
        new_have = remove_empties(new_have)
        new_want = remove_empties(new_want)

        diff_conf = get_diff(new_want, new_have)

        if is_delete_all:
            requests = self.get_delete_all_snmp_request(new_have)
        else:
            requests = self.get_delete_snmp_request(diff_conf, new_have)

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

        return replaced_config


    def get_create_snmp_request(self, config):
        requests = []

        # Create URL and payload
        method = PATCH
        url = 'data/sonic-snmp:sonic-snmp'
        payload = {'sonic-snmp:sonic-snmp': config}
        request = {'path': url, 'method': method, 'data': payload}
        requests.append(request)

        if config.get('agentaddress'):
            agentaddress_path = 'data/sonic-snmp:sonic-snmp/SNMP_AGENT_ADDRESS_CONFIG/SNMP_AGENT_ADDRESS_CONFIG_LIST'
            agentaddress_request = {'path': agentaddress_path, 'method': method, 'data': config.get('agentaddress')}
            requests.append(agentaddress_request)

        if config.get('community'):
            community_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_COMMUNITY/SNMP_SERVER_COMMUNITY_LIST'
            community_request = {'path': community_path, 'method': method, 'data': config.get('community')}
            requests.append(community_request)
        
        if  config.get('engine'):
            engine_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_ENGINE/SNMP_SERVER_ENGINE_LIST'
            engine_request = {'path': engine_path, 'method': method, 'data': config.get('engine')}
            requests.append(engine_request)

        if config.get('user'):
            users_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_USER/SNMP_SERVER_USER_LIST'
            users_request = {'path': users_path, "method": method, 'data': config.get('user')}
            requests.append(users_request)

        if config.get('view'):
            views_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_GROUP_MEMBER/SNMP_SERVER_GROUP_MEMBER_LIST'
            views_request = {'path': views_path, 'method': method, 'data': config.get('view')}
            requests.append(views_request)
        
        if config.get('contact'):
            contact_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER/SNMP_SERVER_LIST'
            contact_request = {'path': contact_path, 'method': method, 'data': config.get('contact')['sysContact']}
            requests.append(contact_request)

        if config.get('location'):
            location_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER/SNMP_SERVER_LIST'
            location_request = {'path': location_path, 'method': method, 'data': config.get('location')}
            requests.append(location_request)
        
        if config.get('enable_trap'):
            enable_trap_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER/SNMP_SERVER_LIST'
            enable_trap_request = {'path': enable_trap_path, 'method': method, 'data': config.get('enable_trap')}
            requests.append(enable_trap_request)

        if config.get('group'):
            group_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_GROUP_ACCESS/SNMP_SERVER_GROUP_ACCESS_LIST'
            group_request = {'path': group_path, 'method': method, 'data': config.get('group')}
            requests.append(group_request)

        return requests


    def get_delete_all_snmp_request(self, have):
        requests = []
        

        agentaddress_requests = []
        community_requests = []
        contact_request = ''
        enable_trap_request = []
        engine_request = ''
        group_requests = []
        host_requests = []
        location_request = ''
        user_requests = []
        view_requests = []

        for conf in have:
            agent_address = conf.get('agentaddress', None)
            community = conf.get('community', None)
            contact = conf.get('contact', None)
            enable_trap = conf.get('enable_trap', None)
            engine = conf.get('engine', None)
            group = conf.get('group', None)
            host = conf.get('host', None)
            location = conf.get('location', None)
            user = conf.get('user', None)
            view = conf.get('view', None)



            matched_agentaddress = next((each_snm for each_snmp in have if each_snmp.get('agentaddress', None)['ip'] == agent_address['id']), None)
            matched_community = next((each_snmp for each_snmp in have if each_snmp.get('community', None)['name'] == community['name']), None)
            matched_contact = next((each_snmp for each_snmp in have if each_snmp.get('contact', None) == contact), None)
            matched_enable_trap = next((each_snmp for each_snmp in have if each_snmp.get('enable_trap', None) == enable_trap), None)
            matched_engine = next((each_snmp for each_snmp in have if each_snmp.get('engine', None) == engine['id']), None)
            matched_group = next((each_snmp for each_snmp in have if each_snmp.get('group', None)['name'] == group['name']), None)
            matched_host = next((each_snmp for each_snmp in have if each_snmp.get('host', None)['ip'] == host['ip']), None)
            matched_location = next((each_snmp for each_snmp in have if each_snmp.get('location', None) == location), None)
            matched_user = next((each_snmp for each_snmp in have if each_snmp.get('user', None)['name'] == user['name']), None)
            matched_view = next((each_snmp for each_snmp in have if each_snmp.get('view', None)['name'] == view['name']), None)

            if matched_agentaddress:
                agentaddress_ip = agentaddress['ip']
                agentaddress_port = agentaddress['port']
                agentaddress_interface = agentaddress['interface']
                agentaddress_url = 'data/sonic-snmp:sonic-snmp/SNMP_AGENT_ADDRESS_CONFIG/SNMP_AGENT_ADDRESS_CONFIG_LIST={agentaddress_ip},{agentaddress_port},{agentaddress_interface}'
                agentaddress_request = {'path': agentaddress_url, 'method': DELETE}
                agentaddress_requests.append(agentaddress_request)
            
            if matched_community:
                community_name=community['name']
                community_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_COMMUNITY/SNMP_SERVER_COMMUNITY_LIST={community_name}'
                community_request = {'path': community_url, 'method': DELETE}
                community_requests.append(community_request)
            
            if matched_contact:##need index
                contact_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER/SNMP_SERVER_LIST/sysContact={contact}'
                contact_request = {'path': contact_url, 'method': DELETE}
                contact_request['data'] = contact
            
            if matched_enable_trap:## need index
                enable_trap_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER/SNMP_SERVER_LIST/enable_trap={enable_trap}'
                enable_trap_request = {'path': enable_trap_url, 'method': DELETE}
                enable_trap_request['data'] = enable_trap
            
            if matched_engine:
                engine_id = engine['id']
                engine_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_ENGINE/SNMP_SERVER_ENGINE_LIST={engine_id}'
                engine_request = {'path': engine_url, 'method': DELETE}
                engine_request['data'] = engine
            
            if matched_group:
                group_name = group['name']
                group_context = group['access'].get('context')
                group_security_model = group['access'].get('securityModel')
                group_security_level = group['access'].get('securityLevel')
                group_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_GROUP_ACCESS/SNMP_SERVER_GROUP_ACCESS_LIST={group_name},{group_context},{group_security_model},{group_security_level}'
                group_request = {'path': group_url, 'method': DELETE}
                group_request['data'] = group
            
            if matched_host:
                host_name = host['user'].get('name')
                host_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_TARGET/SNMP_SERVER_TARGET_LIST={host_name}'
                host_request = {'path': host_url, 'method': DELETE}
                host_request['data'] = host
            
            if matched_location: # need index
                location_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER/SNMP_SERVER_LIST/location={location}'
                location_request = {'path': location_url, 'method': DELETE}
                location_request['data'] = location
            
            if matched_user: # need index
                user_name = user['name']
                user_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_USER/SNMP_SERVER_USER_LIST/user={user_name}'
                user_request = {'path': user_url, 'method': DELETE}
                user_request['data'] = user
            
            if matched_view:
                view_name = view['name']
                view_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_GROUP_MEMBER/SNMP_SERVER_GROUP_MEMBER_LIST/name={view_name}'
                view_request = {'path': view_url, 'method': DELETE}
                view_request['data'] = view

        if agentaddress_requests:
            requests.extend(agentaddress_requests)
        if community_requests:
            requests.extend(community_requests)
        if contact_requests:
            requests.extend(contact_requests)
        if enable_trap_requests:
            requests.extend(enable_trap_requests)
        if engine_requests:
            requests.extend(engine_requests)
        if group_requests:
            requests.extend(group_requests)
        if host_requests:
            requests.extend(host_requests)
        if location_requests:
            requests.extend(location_requests)
        if user_requests:
            requests.extend(user_requests)
        if view_requests:
            requests.extend(view_requests)

        return requests

    def get_delete_snmp_request(self, configs, have):
        requests = []

        if not configs:
            return requests
        

        agentaddress_requests = []
        community_requests = []
        contact_request = ''
        enable_trap_request = []
        engine_request = ''
        group_requests = []
        host_requests = []
        location_request = ''
        user_requests = []
        view_requests = []

        for conf in configs:
            agent_address = conf.get('agentaddress', None)
            community = conf.get('community', None)
            contact = conf.get('contact', None)
            enable_trap = conf.get('enable_trap', None)
            engine = conf.get('engine', None)
            group = conf.get('group', None)
            host = conf.get('host', None)
            location = conf.get('location', None)
            user = conf.get('user', None)
            view = conf.get('view', None)



            matched_agentaddress = next((each_snm for each_snmp in have if each_snmp.get('agentaddress', None)['ip'] == agent_address['id']), None)
            matched_community = next((each_snmp for each_snmp in have if each_snmp.get('community', None)['name'] == community['name']), None)
            matched_contact = next((each_snmp for each_snmp in have if each_snmp.get('contact', None) == contact), None)
            matched_enable_trap = next((each_snmp for each_snmp in have if each_snmp.get('enable_trap', None) == enable_trap), None)
            matched_engine = next((each_snmp for each_snmp in have if each_snmp.get('engine', None) == engine['id']), None)
            matched_group = next((each_snmp for each_snmp in have if each_snmp.get('group', None)['name'] == group['name']), None)
            matched_host = next((each_snmp for each_snmp in have if each_snmp.get('host', None)['ip'] == host['ip']), None)
            matched_location = next((each_snmp for each_snmp in have if each_snmp.get('location', None) == location), None)
            matched_user = next((each_snmp for each_snmp in have if each_snmp.get('user', None)['name'] == user['name']), None)
            matched_view = next((each_snmp for each_snmp in have if each_snmp.get('view', None)['name'] == view['name']), None)

            if matched_agentaddress:
                agentaddress_ip = agentaddress['ip']
                agentaddress_port = agentaddress['port']
                agentaddress_interface = agentaddress['interface']
                agentaddress_url = 'data/sonic-snmp:sonic-snmp/SNMP_AGENT_ADDRESS_CONFIG/SNMP_AGENT_ADDRESS_CONFIG_LIST={agentaddress_ip},{agentaddress_port},{agentaddress_interface}'
                agentaddress_request = {'path': agentaddress_url, 'method': DELETE}
                agentaddress_requests.append(agentaddress_request)
            
            if matched_community:
                community_name=community['name']
                community_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_COMMUNITY/SNMP_SERVER_COMMUNITY_LIST={community_name}'
                community_request = {'path': community_url, 'method': DELETE}
                community_requests.append(community_request)
            
            if matched_contact:##need index
                contact_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER/SNMP_SERVER_LIST/sysContact={contact}'
                contact_request = {'path': contact_url, 'method': DELETE}
                contact_request['data'] = contact
            
            if matched_enable_trap:## need index
                enable_trap_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER/SNMP_SERVER_LIST/enable_trap={enable_trap}'
                enable_trap_request = {'path': enable_trap_url, 'method': DELETE}
                enable_trap_request['data'] = enable_trap
            
            if matched_engine:
                engine_id = engine['id']
                engine_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_ENGINE/SNMP_SERVER_ENGINE_LIST={engine_id}'
                engine_request = {'path': engine_url, 'method': DELETE}
                engine_request['data'] = engine
            
            if matched_group:
                group_name = group['name']
                group_context = group['access'].get('context')
                group_security_model = group['access'].get('securityModel')
                group_security_level = group['access'].get('securityLevel')
                group_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_GROUP_ACCESS/SNMP_SERVER_GROUP_ACCESS_LIST={group_name},{group_context},{group_security_model},{group_security_level}'
                group_request = {'path': group_url, 'method': DELETE}
                group_request['data'] = group
            
            if matched_host:
                host_name = host['user'].get('name')
                host_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_TARGET/SNMP_SERVER_TARGET_LIST={host_name}'
                host_request = {'path': host_url, 'method': DELETE}
                host_request['data'] = host
            
            if matched_location: # need index
                location_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER/SNMP_SERVER_LIST/location={location}'
                location_request = {'path': location_url, 'method': DELETE}
                location_request['data'] = location
            
            if matched_user: # need index
                user_name = user['name']
                user_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_USER/SNMP_SERVER_USER_LIST/user={user_name}'
                user_request = {'path': user_url, 'method': DELETE}
                user_request['data'] = user
            
            if matched_view:
                view_name = view['name']
                view_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_GROUP_MEMBER/SNMP_SERVER_GROUP_MEMBER_LIST/name={view_name}'
                view_request = {'path': view_url, 'method': DELETE}
                view_request['data'] = view

        if agentaddress_requests:
            requests.extend(agentaddress_requests)
        if community_requests:
            requests.extend(community_requests)
        if contact_requests:
            requests.extend(contact_requests)
        if enable_trap_requests:
            requests.extend(enable_trap_requests)
        if engine_requests:
            requests.extend(engine_requests)
        if group_requests:
            requests.extend(group_requests)
        if host_requests:
            requests.extend(host_requests)
        if location_requests:
            requests.extend(location_requests)
        if user_requests:
            requests.extend(user_requests)
        if view_requests:
            requests.extend(view_requests)

        return requests


