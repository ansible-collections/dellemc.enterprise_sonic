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
import sys
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
    edit_config,
    get_connection
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    update_states,
    get_diff,
    get_replaced_config,
    remove_empties_from_list,
    send_requests
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.sort_config_util import (
    sort_config,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.formatted_diff_utils import (
    __DELETE_CONFIG_IF_NO_SUBCONFIG,
    get_new_config,
    get_formatted_config_diff
)

PATCH = 'patch'
DELETE = 'delete'
TEST_KEYS = [
    {'agentaddress': {'ip': ''}},
    {'community': {'name': ''}},
    {'group': {'name': ''}},
    {'user': {'name': ''}},
    {'view': {'name': ''}},
]
test_keys_generate_config = [
    {'agentaddress': {'ip': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}},
    {'community': {'name': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}},
    {'group': {'name': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}},
    {'user': {'name': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}},
    {'view': {'name': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}},
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
       
        if commands and requests:
            if not self._module.check_mode:
                try:
                    list_requests = []
                    #for item in requests:
                        #print("\n item =\n {0}\n".format(dict(item)['path']),   file=open('snmp_facts.txt', 'a')) 
                        #item = dict(item[0])
                        #list_requests.extend(dict(item))
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
                
            result['changed'] = True
        result['commands'] = commands

        changed_snmp_facts = self.get_snmp_facts()
        result['before'] = existing_snmp_facts
        if result['changed']:
            result['after'] = changed_snmp_facts

        new_config = changed_snmp_facts    
        old_config = existing_snmp_facts
        if self._module.check_mode:
            result.pop('after', None)
            new_config = get_new_config(commands, existing_snmp_facts, test_keys_generate_config)
            result['after(generated)'] = new_config
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
        want = self._module.params['config']
        have = existing_snmp_facts
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

        if state == 'overridden':
            commands, requests = self._state_overridden(want, have)
        elif state == 'deleted':
            commands, requests = self._state_deleted(want, have)
        elif state == 'merged':
            commands, requests = self._state_merged(want, have)
        elif state == 'replaced':
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
            is_delete_all = (replaced_config == have)
            if is_delete_all:
                requests = self.get_delete_all_snmp_request(have)
            else:
                requests = self.get_delete_snmp_request(replaced_config, have)

            send_requests(self._module, requests)
            commands = want
        else:
            commands = get_diff(want, have, TEST_KEYS)

        requests = []
        if commands:
            requests = self.get_create_snmp_request(dict(commands))
            if len(requests) > 0:
                commands = update_states(commands, "replaced")
            else:
                commands = []
        else:
            commands = []

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
            requests =self.get_create_snmp_request(dict(commands))

            if len(requests) > 0:
                commands = update_states(commands, "overridden")
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
        requests = self.get_create_snmp_request(commands)
        
        if commands and requests:
            commands = update_states(commands, "merged")
        else:
            commands = []

        #print("\nrequests =\n {0}\n".format(requests),   file=open('snmp_facts.txt', 'a'))   
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
            
        new_have = remove_empties_from_list(have)
        new_want = remove_empties_from_list(want)

        if is_delete_all:
            requests = self.get_delete_all_snmp_request(new_have)
        else:
            requests = self.get_delete_snmp_request(commands, new_have)

        if len(requests) == 0:
            commands = []

        if commands:
            commands = update_states(commands, "deleted")

        return commands, requests

    def get_create_snmp_request(self, config):
        requests = []
        method = PATCH

        if config.get('agentaddress'):
            agentaddress_path = 'data/sonic-snmp:sonic-snmp/SNMP_AGENT_ADDRESS_CONFIG/SNMP_AGENT_ADDRESS_CONFIG_LIST'
            payload = self.build_create_agentaddress_payload(config)
            agentaddress_request = {'path': agentaddress_path, 'method': method, 'data': payload}
            requests.append(agentaddress_request)

        if config.get('community'):
            community_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_COMMUNITY/SNMP_SERVER_COMMUNITY_LIST'
            payload = self.build_create_community_payload(config)
            community_request = {'path': community_path, 'method': method, 'data': payload}
            requests.append(community_request)
        
        if  config.get('engine'):
            engine_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_ENGINE/SNMP_SERVER_ENGINE_LIST'
            payload = self.build_create_engine_payload(config)
            engine_request = {'path': engine_path, 'method': method, 'data': payload}
            requests.append(engine_request)

        if config.get('user'):
            users_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_USER/SNMP_SERVER_USER_LIST'
            payload = self.build_create_user_payload(config)
            users_request = {'path': users_path, "method": method, 'data': payload}
            requests.append(users_request)

        if config.get('view'):
            views_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_GROUP_MEMBER/SNMP_SERVER_GROUP_MEMBER_LIST'
            payload = self.build_create_view_payload(config)
            views_request = {'path': views_path, 'method': method, 'data': payload}
            requests.append(views_request)
        
        if config.get('contact'):
            contact_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER/SNMP_SERVER_LIST'
            payload = self.build_create_contact_payload(config)
            contact_request = {'path': contact_path, 'method': method, 'data': payload}
            requests.append(contact_request)

        if config.get('location'):
            location_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER/SNMP_SERVER_LIST'
            payload = self.build_create_location_payload(config)
            location_request = {'path': location_path, 'method': method, 'data':payload}
            requests.append(location_request)
        
        if config.get('enable_trap'):
            enable_trap_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER/SNMP_SERVER_LIST'
            payload = self.build_create_enable_trap_payload(config)
            enable_trap_request = {'path': enable_trap_path, 'method': method, 'data': payload}
            requests.append(enable_trap_request)

        if config.get('group'):
            group_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_GROUP_ACCESS/SNMP_SERVER_GROUP_ACCESS_LIST'
            payload = self.build_create_group_payload(config)
            group_request = {'path': group_path, 'method': method, 'data': payload}
            requests.append(group_request)

        return requests

    def build_create_agentaddress_payload(self, config):
        agentaddress_payload = {'sonic-snmp:SNMP_AGENT_ADDRESS_CONFIG/SNMP_AGENT_ADDRESS_CONFIG_LIST': config.get('agentaddress')}
       
        return agentaddress_payload

    def build_create_community_payload(self, config):
        community_payload = {'sonic-snmp:SNMP_SERVER_COMMUNITY_LIST': config.get('community')}
        return community_payload

    def build_create_engine_payload(self, config):
        engine_payload = {'sonic-snmp:SNMP_SERVER_ENGINE_LIST': config.get('engine')}
        return engine_payload

    def build_create_user_payload(self, config):
        user_payload = {'sonic-snmp:SNMP_SERVER_USER_LIST': config.get('user')}
        return user_payload

    def build_create_view_payload(self, config):
        view_payload = {'sonic-snmp:SNMP_SERVER_GROUP_MEMBER_LIST': config.get('view')}
        return view_payload

    def build_create_contact_payload(self, config):
        contact_payload = {'sonic-snmp:SNMP_SERVER_LIST': config.get('contact')}
        return contact_payload

    def build_create_location_payload(self, config):
        location_payload = {'sonic-snmp:SNMP_SERVER_LIST': config.get('location')}
        return location_payload

    def build_create_enable_trap_payload(self, config):
        enable_trap_payload = {'sonic_snmp:SNMP_SERVER_LIST', config.get('enable-trap')}
        return enable_trap_payload

    def build_create_group_payload(self, config):
        payload_url = dict()
        group_list = []
        group = config.get('group', None)
        for conf in group:
            group_dict = dict()
            group_dict['groupName'] = conf.get('name')
            #group_dict['context'] = 'Default'
            group_dict['securityModel'] = conf.get('access')[0].get('security_model')
            group_dict['securityLevel'] = conf.get('access')[0].get('security_level')
            group_dict['readView'] = conf.get('access')[0].get('read_view')
            group_dict['writeView'] = conf.get('access')[0].get('write_view')
            group_dict['notifyView'] = conf.get('access')[0].get('notify_view')
            group_list.append(group_dict)

        payload_url['sonic-snmp:SNMP_SERVER_GROUP_ACCESS'] = {'SNMP_SERVER_GROUP_ACCESS_LIST': group_list}
        return payload_url
    
    def get_delete_all_snmp_request(self, have):
        requests = []

        agentaddress_requests = []
        community_requests = []
        contact_request = ''
        enable_trap_requests = []
        engine_request = ''
        group_requests = []
        host_requests = []
        location_request = ''
        user_requests = []
        view_requests = []

        agentaddress = have.get('agentaddress', None)
        community = have.get('community', None)
        contact = have.get('contact', None)
        enable_trap = have.get('enable_trap', None)
        engine = have.get('engine', None)
        group = have.get('group', None)
        host = have.get('host', None)
        location = have.get('location', None)
        user = have.get('user', None)
        view = have.get('view', None)

        if agentaddress:
            matched_agentaddress = next((each_snmp for each_snmp in have if each_snmp.get('agentaddress', None)['ip'] == agentaddress['id']), None)

            if matched_agentaddress:
                agentaddress_ip = agentaddress['ip']
                agentaddress_port = agentaddress['port']
                agentaddress_interface = agentaddress['interface']
                agentaddress_url = 'data/sonic-snmp:sonic-snmp/SNMP_AGENT_ADDRESS_CONFIG/SNMP_AGENT_ADDRESS_CONFIG_LIST={agentaddress_ip},{agentaddress_port},{agentaddress_interface}'
                agentaddress_request = {'path': agentaddress_url, 'method': DELETE}
                agentaddress_requests.append(agentaddress_request)
        if community:
            matched_community = next((each_snmp for each_snmp in have if each_snmp.get('community', None)['name'] == community['name']), None)
            if matched_community:
                community_name = community['name']
                community_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_COMMUNITY/SNMP_SERVER_COMMUNITY_LIST={community_name}'
                community_request = {'path': community_url, 'method': DELETE}
                community_requests.append(community_request)
        if contact:
            matched_contact = next((each_snmp for each_snmp in have if each_snmp.get('contact', None) == contact), None)
            if matched_contact:
                contact_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER/SNMP_SERVER_LIST=SYSTEM/sysContact'
                contact_request = {'path': contact_url, 'method': DELETE}
                contact_request['data'] = contact
        if enable_trap:
            matched_enable_trap = next((each_snmp for each_snmp in have if each_snmp.get('enable_trap', None) == enable_trap), None)
            if matched_enable_trap:
                enable_trap_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER/SNMP_SERVER_LIST=SYSTEM/{enable_trap}'
                enable_trap_request = {'path': enable_trap_url, 'method': DELETE}
                enable_trap_request['data'] = enable_trap
                enable_trap_requests.append(enable_trap_request)
        if engine:
            matched_engine = next((each_snmp for each_snmp in have if each_snmp.get('engine', None) == engine['id']), None)
            if matched_engine:
                engine_id = engine['id']
                engine_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_ENGINE/SNMP_SERVER_ENGINE_LIST={engine_id}'
                engine_request = {'path': engine_url, 'method': DELETE}
                engine_request['data'] = engine
        if group:
            matched_group = next((each_snmp for each_snmp in have if each_snmp.get('group', None)['name'] == group['name']), None)
            if matched_group:
                group_name = group['name']
                group_context = group['access'].get('context')
                group_security_model = group['access'].get('securityModel')
                group_security_level = group['access'].get('securityLevel')
                group_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_GROUP_ACCESS/SNMP_SERVER_GROUP_ACCESS_LIST={group_name},{group_context},{group_security_model},{group_security_level}'
                group_request = {'path': group_url, 'method': DELETE}
                group_request['data'] = group
                group_requests.append(group_request)
        if host:
            matched_host = next((each_snmp for each_snmp in have if each_snmp.get('host', None)['ip'] == host['ip']), None)
            if matched_host:
                host_name = host['user'].get('name')
                host_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_TARGET/SNMP_SERVER_TARGET_LIST={host_name}'
                host_request = {'path': host_url, 'method': DELETE}
                host_request['data'] = host
                host_requests.append(host_request)
        if location:
            matched_location = next((each_snmp for each_snmp in have if each_snmp.get('location', None) == location), None)
            if matched_location: # 
                location_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER/SNMP_SERVER_LIST=SYSTEM/syslocation'
                location_request = {'path': location_url, 'method': DELETE}
                location_request['data'] = location
        if user:
            matched_user = next((each_snmp for each_snmp in have if each_snmp.get('user', None)['name'] == user['name']), None)
            if matched_user: 
                user_name = user['name']
                user_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_USER/SNMP_SERVER_USER_LIST={user_name}'
                user_request = {'path': user_url, 'method': DELETE}
                user_request['data'] = user
                user_requests.append(user_request)
        if view:
            matched_view = next((each_snmp for each_snmp in have if each_snmp.get('view', None)['name'] == view['name']), None)
            if matched_view:
                view_name = view['name']
                view_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_VIEW/SNMP_SERVER_VIEW_LIST={view_name}'
                view_request = {'path': view_url, 'method': DELETE}
                view_request['data'] = view
                view_requests.append(view_request)


        if agentaddress_requests:
            requests.extend(agentaddress_requests)
        if community_requests:
            requests.extend(community_requests)
        if contact_request:
            requests.extend(contact_request)
        if enable_trap_requests:
            requests.extend(enable_trap_requests)
        if engine_request:
            requests.extend(engine_request)
        if group_requests:
            requests.extend(group_requests)
        if host_requests:
            requests.extend(host_requests)
        if location_request:
            requests.extend(location_request)
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
        enable_trap_requests = []
        engine_request = ''
        group_requests = []
        host_requests = []
        location_request = ''
        user_requests = []
        view_requests = []

        agentaddress = configs.get('agentaddress', None)
        community = configs.get('community', None)
        contact = configs.get('contact', None)
        enable_trap = configs.get('enable_trap', None)
        engine = configs.get('engine', None)
        group = configs.get('group', None)
        host = configs.get('host', None)
        location = configs.get('location', None)
        user = configs.get('user', None)
        view = configs.get('view', None)

        if agentaddress:
            matched_agentaddress = next((each_snmp for each_snmp in have if each_snmp.get('agentaddress', None)['ip'] == agentaddress['id']), None)

            if matched_agentaddress:
                agentaddress_ip = agentaddress['ip']
                agentaddress_port = agentaddress['port']
                agentaddress_interface = agentaddress['interface']
                agentaddress_url = 'data/sonic-snmp:sonic-snmp/SNMP_AGENT_ADDRESS_CONFIG/SNMP_AGENT_ADDRESS_CONFIG_LIST={agentaddress_ip},{agentaddress_port},{agentaddress_interface}'
                agentaddress_request = {'path': agentaddress_url, 'method': DELETE}
                agentaddress_requests.append(agentaddress_request)
        if community:
            matched_community = next((each_snmp for each_snmp in have if each_snmp.get('community', None)['name'] == community['name']), None)
            if matched_community:
                community_name = community['name']
                community_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_COMMUNITY/SNMP_SERVER_COMMUNITY_LIST={community_name}'
                community_request = {'path': community_url, 'method': DELETE}
                community_requests.append(community_request)
        if contact:
            matched_contact = next((each_snmp for each_snmp in have if each_snmp.get('contact', None) == contact), None)
            if matched_contact:
                contact_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER/SNMP_SERVER_LIST=SYSTEM/sysContact'
                contact_request = {'path': contact_url, 'method': DELETE}
                contact_request['data'] = contact
        if enable_trap:
            matched_enable_trap = next((each_snmp for each_snmp in have if each_snmp.get('enable_trap', None) == enable_trap), None)
            if matched_enable_trap:
                enable_trap_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER/SNMP_SERVER_LIST=SYSTEM/{enable_trap}'
                enable_trap_request = {'path': enable_trap_url, 'method': DELETE}
                enable_trap_request['data'] = enable_trap
                enable_trap_requests.append(enable_trap_request)
        if engine:
            matched_engine = next((each_snmp for each_snmp in have if each_snmp.get('engine', None) == engine['id']), None)
            if matched_engine:
                engine_id = engine['id']
                engine_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_ENGINE/SNMP_SERVER_ENGINE_LIST={engine_id}'
                engine_request = {'path': engine_url, 'method': DELETE}
                engine_request['data'] = engine
        if group:
            matched_group = next((each_snmp for each_snmp in have if each_snmp.get('group', None)['name'] == group['name']), None)
            if matched_group:
                group_name = group['name']
                group_context = group['access'].get('context')
                group_security_model = group['access'].get('securityModel')
                group_security_level = group['access'].get('securityLevel')
                group_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_GROUP_ACCESS/SNMP_SERVER_GROUP_ACCESS_LIST={group_name},{group_context},{group_security_model},{group_security_level}'
                group_request = {'path': group_url, 'method': DELETE}
                group_request['data'] = group
                group_requests.append(group_request)
        if host:
            matched_host = next((each_snmp for each_snmp in have if each_snmp.get('host', None)['ip'] == host['ip']), None)
            if matched_host:
                host_name = host['user'].get('name')
                host_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_TARGET/SNMP_SERVER_TARGET_LIST={host_name}'
                host_request = {'path': host_url, 'method': DELETE}
                host_request['data'] = host
                host_requests.append(host_request)
        if location:
            matched_location = next((each_snmp for each_snmp in have if each_snmp.get('location', None) == location), None)
            if matched_location: # 
                location_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER/SNMP_SERVER_LIST=SYSTEM/syslocation'
                location_request = {'path': location_url, 'method': DELETE}
                location_request['data'] = location
        if user:
            matched_user = next((each_snmp for each_snmp in have if each_snmp.get('user', None)['name'] == user['name']), None)
            if matched_user: 
                user_name = user['name']
                user_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_USER/SNMP_SERVER_USER_LIST={user_name}'
                user_request = {'path': user_url, 'method': DELETE}
                user_request['data'] = user
                user_requests.append(user_request)
        if view:
            matched_view = next((each_snmp for each_snmp in have if each_snmp.get('view', None)['name'] == view['name']), None)
            if matched_view:
                view_name = view['name']
                view_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_VIEW/SNMP_SERVER_VIEW_LIST={view_name}'
                view_request = {'path': view_url, 'method': DELETE}
                view_request['data'] = view
                view_requests.append(view_request)

        if agentaddress_requests:
            requests.extend(agentaddress_requests)
        if community_requests:
            requests.extend(community_requests)
        if contact_request:
            requests.extend(contact_request)
        if enable_trap_requests:
            requests.extend(enable_trap_requests)
        if engine_request:
            requests.extend(engine_request)
        if group_requests:
            requests.extend(group_requests)
        if host_requests:
            requests.extend(host_requests)
        if location_request:
            requests.extend(location_request)
        if user_requests:
            requests.extend(user_requests)
        if view_requests:
            requests.extend(view_requests)

        return requests
    