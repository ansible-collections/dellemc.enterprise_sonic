#
# -*- coding: utf-8 -*-
# Copyright 2024 Dell Inc. or its subsidiaries. All Rights Reserved.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_snmp class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
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
    update_states,
    get_replaced_config,
    remove_empties_from_list,
    send_requests
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.formatted_diff_utils import (
    __DELETE_CONFIG_IF_NO_SUBCONFIG,
    get_new_config,
    get_formatted_config_diff
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import Facts

PATCH = 'patch'
DELETE = 'delete'
test_keys = [
    {'agentaddress': {'ip': ''}},
    {'community': {'name': ''}},
    {'access': {'security_model': ''}},
    {'group': {'name': ''}},
    {'host': {'ip': ''}},
    {'user': {'name': ''}},
    {'view': {'name': ''}}
]
test_keys_generate_config = [
    {'agentaddress': {'ip': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}},
    {'community': {'name': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}},
    {'access': {'security_model': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}},
    {'group': {'name': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}},
    {'host': {'ip': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}},
    {'user': {'name': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}},
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
            return []
        return snmp_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = list()

        existing_snmp_facts = self.get_snmp_facts()
        commands, requests = self.set_config(existing_snmp_facts)
        #commands.extend(self.set_config(existing_snmp_facts))

        if commands and requests:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
                #self._connection.edit_config(commands)
            result['changed'] = True
        result['commands'] = commands

        changed_snmp_facts = self.get_snmp_facts()

        result['before'] = existing_snmp_facts
        if result['changed']:
            result['after'] = changed_snmp_facts

        new_config = changed_snmp_facts
        old_config - existing_snmp_facts
        if self._module.check_mode:
            result.pop('after', None)
            existing_snmp_facts = remove_empties_from_list(existing_snmp_facts)
            is_overridden = False
            for cmd in commands:
                if cmd['state'] == 'overridden':
                    is_overridden = True
                    break
            if is_overridden:
                new_config = get_new_config(commands, existing_snmp_facts, TEST_KEYS_overriddens)
            else:
                new_config = get_new_config(commands, existing_snmp_facts, TEST_KEYS_diff)

            #new_config = get_new_config(commands, existing_snmp_facts, test_keys_generate_config)
            #new_config = self.post_process_generated_config(new_config)
            new_config = remove_empties_from_list(new_config)
            #result['after(generated)'] = new_config
            result['after(generated)'] = self._post_process_generated_output(new_config)
            self.sort_lists_in_config(result['after(generated)'])

        if self._module_diff:
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
        want = self._module.params['config']
        have = existing_snmp_facts
        want = remove_empties_from_list(want)
        new_want, new_have =self.validate_and_normalize_config(want, have)
        self.sort_lists_in_config(new_want)
        self.sort_lists_in_config(new_have)
        resp = self.set_state(new_want, new_have)
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
        diff = get_diff(want, have, test_keys)

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
            self.sort_lists_in_config(replaced_config)
            self.sort_lists_in_config(have)
            is_delete_all = replaced_config == have
            del_commands, del_requests = self.get_delete_snmp_request(replaced_config, have, is_delete_all)
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
            self.sort_lists_in_config(replaced_config)
            self.sort_lists_in_config(have)
            is_delete_all = replaced_config == have
            del_commands, del_requests = self.get_delete_snmp_request(replaced_config, have, is_delete_all)
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
        commands, requests = [], []
        replaced_config = get_replaced_config(want, have, TEST_KEYS)

        if replaced_config:
            self.sort_lists_in_config(replaced_config)
            self.sort_lists_in_config(have)
            is_delete_all = replaced_config == have
            del_commands, del_requests = self.get_delete_snmp_request(replaced_config, have, is_delete_all)
            requests.extend(del_requests)
            commands.extend(update_states(del_commands, 'deleted'))

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
            new_have = remove_empties_from_list(new_have)
            new_want = remove_empties_from_list(new_want)
        commands, requests = self.get_delete_snmp_request(new_want, have is_delete_all)

        if is_delete_all:
            requests = self.get_delete_all_snmp_request(commands)
        else:
            requests = self.get_delete_snmp_request(commands, have)

        if commands:
            commands = update_states(commands, "deleted")
        else:
            commands = []

        return commands, requests

    def _get_replaced_config(self, want, have):
        replaced_config = dict()

        # Compare the 'agentaddress' configuration
        if 'agentaddress' in want and 'agentaddress' in have:
            want_agentaddress = want.get('agentaddress')
            have_agentaddress = have.get('agentaddress')

            if want_agentaddress != have_agentaddress:
                replaced_config['agentaddress'] = have_agentaddress

        # Compare the 'community' configuration
        if 'community' in want and 'community' in have:
            want_community = want.get('community')
            have_community = have.get('community')

            if want_community != have_community:
                replaced_config['community'] = have_community

        # Compare the 'users' configuration
        if 'user' in want and 'user' in have:
            want_users = want.get('users')
            have_users = have.get('users')

            replaced_users = []
            for want_user in want_users:
                have_user = next((u for u in have_users if u['name'] == want_user['name']), None)
                if have_user and want_user != have_user:
                    replaced_users.append(have_user)

            if replaced_users:
                replaced_config['users'] = replaced_users

        # Compare the 'views' configuration
        if 'view' in want and 'view' in have:
            want_views = want.get('views')
            have_views = have.get('views')

            replaced_views = []
            for want_view in want_views:
                have_view = next((v for v in have_views if v['name'] == want_view['name']), None)
                if have_view and want_view != have_view:
                    replaced_views.append(have_view)

            if replaced_views:
                replaced_config['views'] = replaced_views

        return replaced_config


    def get_create_snmp_request(self, commands):
        requests = []

        # Create URL and payload
        method = PATCH
        url = 'data/sonic-snmp:sonic-snmp'
        payload = {"sonic-snmp:sonic-snmp": config}
        request = {"path": url, "method": method, "data": payload}
        requests.append(request)

        if config.get('agentaddress'):
            agentaddress_payload = self.build_create_agentaddress_payload(config)
            if agentaddress_payload:
                agentaddress_path = 'data/sonic-snmp:sonic-snmp/SNMP_AGENT_ADDRESS_CONFIG/SNMP_AGENT_ADDRESS_CONFIG_LIST'
                agentaddress_method = PATCH
                agentaddress_request = {"path": agentaddress_path, "method": agentaddress_method, "data": agentaddress_payload}
                requests.append(agentaddress_request)

        if config.get('community'):
            community_payload = self.build_create_community_payload(config)
            if community_payload:
                community_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_COMMUNITY/SNMP_SERVER_COMMUNITY_LIST'
                community_method = PATCH
                community_request = {"path": community_path, "method": community_method, "data": community_payload}
                requests.append(community_request)
        
        if  config.get('engine'):
            engine_payload = self.build_create_engine_payload(config)
            if engine_payload:
                engine_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_ENGINE/SNMP_SERVER_ENGINE_LIST'
                engine_method = PATCH
                engine_request = {"path": engine_path, "method": engine_method, "data": engine_payload}
                requests.append(engine_request)

        if config.get('user'):
            users_payload = self.build_create_users_payload(config)
            if users_payload:
                users_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_USER/SNMP_SERVER_USER_LIST'
                users_method = PATCH
                users_request = {"path": users_path, "method": users_method, "data": users_payload}
                requests.append(users_request)

        if config.get('view'):
            views_payload = self.build_create_views_payload(config)
            if views_payload:
                views_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_GROUP_MEMBER/SNMP_SERVER_GROUP_MEMBER_LIST'
                views_method = PATCH
                views_request = {"path": views_path, "method": views_method, "data": views_payload}
                requests.append(views_request)
        
        if config.get('contact'):
            contact_payload = self.build_create_contact_payload(config)
            if contact_payload:
                contact_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER/SNMP_SERVER_LIST'
                contact_method = PATCH
                contact_request = {"path": contact_path, "method": contact_method, "data": contact_payload}
                requests.append(contact_request)

        if config.get('location'):
            location_payload = self.build_create_location_payload(config)
            if location_payload:
                location_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER/SNMP_SERVER_LIST'
                location_method = PATCH
                location_request = {"path": location_path, "method": location_method, "data": location_payload}
                requests.append(location_request)
        
        if config.get('enable_trap'):
            enable_trap_payload = self.build_create_enable_trap_payload(config)
            if enable_trap_payload:
                enable_trap_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER/SNMP_SERVER_LIST'
                enable_trap_method = PATCH
                enable_trap_request = {"path": enable_trap_path, "method": enable_trap_method, "data": enable_trap_payload}
                requests.append(enable_trap_request)

        if config.get('group'):
            group_payload = self.build_create_group_payload(config)
            if group_payload:
                group_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_GROUP_ACCESS/SNMP_SERVER_GROUP_ACCESS_LIST'
                group_method = PATCH
                group_request = {"path": group_path, "method": group_method, "data": group_payload}
                requests.append(group_request)
        
        if config.get('host'):
            host_payload = self.build_create_host_payload(config)
            if host_payload:
                host_path1 = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_PARAMS/SNMP_SERVER_PARAMS_LIST'
                host_path2 = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_TARGET/SNMP_SERVER_TARGET_LIST'
                host_method = PATCH
                host_request = {"path": host_path, "method": host_method, "data": host_payload}
                requests.append(host_request)

        return requests


    def get_delete_all_snmp_request(self, configs):
        requests = []

        for conf in configs:
            request = self.get_delete_snmp_request(conf)
            requests.append(request)

        return requests

    def get_delete_snmp_request(self, configs, have):
        requests = []

        if not configs:
            return requests
        
        for conf in configs:
            request = self.get_delete_snmp_request(conf)
            requests.append(request)
        
        return requests
