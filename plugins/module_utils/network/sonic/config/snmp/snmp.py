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
import base64
import secrets
import string
__metaclass__ = type

from copy import deepcopy
from ansible.module_utils.connection import ConnectionError

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import ConfigBase

from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import Facts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    update_states,
    get_diff,
    get_replaced_config,
    send_requests
)

from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.formatted_diff_utils import (
    __DELETE_CONFIG_IF_NO_SUBCONFIG,
    get_new_config,
    get_formatted_config_diff
)

PATCH = 'patch'
DELETE = 'delete'
target_entry = int(1)
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
        return resp

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
        replaced_config = get_replaced_config(want, have)

        if replaced_config:
            requests = self.get_delete_snmp_request(replaced_config, have, False)

            send_requests(self._module, requests)
            commands = want
        else:
            commands = get_diff(want, have, TEST_KEYS)

        requests = []
        if commands:
            requests = self.get_create_snmp_request(commands)
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
            requests = self.get_delete_snmp_request(have, have, False)
            send_requests(self._module, requests)
            have = []

        commands, requests = [], []

        if not have and want:
            commands = want
            requests = self.get_create_snmp_request(commands)

            if requests:
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

        return commands, requests

    def _state_deleted(self, want, have):
        """ The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        commands, requests = [], []
        delete_all = False

        if not want:
            commands = deepcopy(have)
            delete_all = True
        else:
            commands = deepcopy(want)

        requests = self.get_delete_snmp_request(commands, dict(have), delete_all)

        if commands and requests:
            commands = update_states(commands, 'deleted')
        else:
            commands = []

        return commands, requests

    def get_create_snmp_request(self, config):
        """ Create the requests necessary to create the desired configuration

        :rtype: A list
        :returns: the requests necessary to create the desired configuration
        """
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

        if config.get('contact'):
            contact_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER/SNMP_SERVER_LIST'
            payload = self.build_create_contact_payload(config)
            contact_request = {'path': contact_path, 'method': method, 'data': payload}
            requests.append(contact_request)

        if config.get('enable_trap'):
            enable_trap_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER/SNMP_SERVER_LIST'
            payload = self.build_create_enable_trap_payload(config)
            enable_trap_request = {'path': enable_trap_path, 'method': method, 'data': payload}
            requests.append(enable_trap_request)

        if config.get('engine'):
            engine_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_ENGINE/SNMP_SERVER_ENGINE_LIST'
            payload = self.build_create_engine_payload(config)
            engine_request = {'path': engine_path, 'method': method, 'data': payload}
            requests.append(engine_request)

        if config.get('group'):
            group_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_GROUP_ACCESS/SNMP_SERVER_GROUP_ACCESS_LIST'
            payload = self.build_create_group_payload(config)
            group_request = {'path': group_path, 'method': method, 'data': payload}
            requests.append(group_request)

        if config.get('host'):
            target_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_TARGET/SNMP_SERVER_TARGET_LIST'
            server_params_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_PARAMS/SNMP_SERVER_PARAMS_LIST'
            payload = self.build_create_enable_target_payload(config)
            target_request = {'path': target_path, 'method': method, 'data': payload}
            requests.append(target_request)
            payload1, target_e = self.build_create_enable_server_payload(config)
            server_params_request = {'path': server_params_path, 'method': method, 'data': payload1}
            requests.append(server_params_request)
            global target_entry
            target_entry = target_e + 1

        if config.get('location'):
            location_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER/SNMP_SERVER_LIST'
            payload = self.build_create_location_payload(config)
            location_request = {'path': location_path, 'method': method, 'data': payload}
            requests.append(location_request)

        if config.get('user'):
            users_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_USER/SNMP_SERVER_USER_LIST'
            payload = self.build_create_user_payload(config)
            users_request = {'path': users_path, "method": method, 'data': payload}
            requests.append(users_request)
            user_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_GROUP_MEMBER/SNMP_SERVER_GROUP_MEMBER_LIST'
            payload = self.build_create_group_member_payload(config)
            users_request = {'path': user_path, "method": method, 'data': payload}
            requests.append(users_request)
            group_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_GROUP/SNMP_SERVER_GROUP_LIST'
            payload = self.build_create_group_name_payload(config)
            if len(payload) > 0:
                users_request = {'path': group_path, "method": method, 'data': payload}
                requests.append(users_request)

        if config.get('view'):
            views_path = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_VIEW/SNMP_SERVER_VIEW_LIST'
            payload = self.build_create_view_payload(config)
            views_request = {'path': views_path, 'method': method, 'data': payload}
            requests.append(views_request)

        return requests

    def build_create_agentaddress_payload(self, config):
        """ Build the payload for SNMP agentaddress

        :rtype: A dictionary
        :returns: The payload for SNMP agentaddress
        """
        agentaddress = config.get('agentaddress', None)
        agentaddress_list = list()
        payload_url = dict()
        for conf in agentaddress:
            agentaddress_dict = dict()
            agentaddress_dict['ip'] = conf.get('ip')
            agentaddress_dict['port'] = conf.get('port')
            agentaddress_dict['interface'] = conf.get('interface')
            agentaddress_list.append(agentaddress_dict)

        payload_url['SNMP_AGENT_ADDRESS_CONFIG_LIST'] = agentaddress_list
        return payload_url

    def build_create_community_payload(self, config):
        """ Build the payload for SNMP community

        :rtype: A dictionary
        :returns: The payload for SNMP community
        """
        community = config.get('community', None)
        community_list = list()
        payload_url = dict()

        for conf in community:
            community_dict = dict()
            community_dict['index'] = conf.get('name')
            community_dict['securityName'] = conf.get('group')
            community_list.append(community_dict)
        payload_url['SNMP_SERVER_COMMUNITY_LIST'] = community_list
        return payload_url

    def build_create_engine_payload(self, config):
        """ Build the payload for SNMP engine

        :rtype: A dictionary
        :returns: The payload for SNMP engine
        """
        engine = config.get('engine', None)
        engine_list = list()
        payload_url = dict()

        for conf in engine:
            engine_dict = dict()
            engine_dict['engine-id'] = conf
            engine_dict['id'] = "GLOBAL"
            engine_list.append(engine_dict)

        payload_url['SNMP_SERVER_ENGINE_LIST'] = engine_list
        return payload_url

    def build_create_user_payload(self, config):
        """ Build the payload for SNMP user

        :rtype: A dictionary
        :returns: The payload for SNMP user
        """
        user = config.get('user', None)
        user_list = list()
        payload_url = dict()

        for conf in user:
            user_dict = dict()

            characters = string.ascii_letters + string.digits
            random_auth_key = ''.join(secrets.choice(characters) for a in range(55))
            encoded_auth_key = base64.b64encode(random_auth_key.encode()).decode()

            characters = string.ascii_letters + string.digits
            random_priv_key = ''.join(secrets.choice(characters) for a in range(55))
            encoded_priv_key = base64.b64encode(random_priv_key.encode()).decode()

            auth_key = conf['auth'].get('auth_type') + "Key"
            priv_key = conf['priv'].get('priv_type') + "Key"
            user_dict[priv_key] = encoded_priv_key
            user_dict[auth_key] = encoded_auth_key
            user_dict['name'] = conf.get('name')
            user_list.append(user_dict)

        payload_url['SNMP_SERVER_USER_LIST'] = user_list
        return payload_url

    def build_create_group_member_payload(self, config):
        """ Build the payload for SNMP group members based on the given user information

        :rtpe: A dictionary
        :returns: The payload for SNMP group members
        """
        group_list = list()
        group = config.get('user', None)

        payload_url = dict()

        for conf in group:
            group_dict = dict()
            group_dict['groupName'] = conf.get('group')
            group_dict['securityName'] = conf.get('name')
            group_list.append(group_dict)
        payload_url['SNMP_SERVER_GROUP_MEMBER_LIST'] = group_list
        return payload_url

    def build_create_group_name_payload(self, config):
        """ Build the payload for SNMP group name based on the given user information

        :rtype: A dictionary
        :Returns: The payload for SNMP group
        """
        group_list = list()
        group = config.get('user', None)

        payload_url = dict()

        for conf in group:
            group_dict = dict()
            group_dict['name'] = conf.get('group')
            group_list.append(group_dict)

        if group_list == []:
            return dict()
        payload_url['SNMP_SERVER_GROUP_LIST'] = group_list
        return payload_url

    def build_create_view_payload(self, config):
        """ Build the payload for SNMP view

        :rtype: A dictonary
        :returns: The payload for SNMP view
        """
        view_list = list()
        payload_url = dict()
        view = config.get('view', None)

        for conf in view:
            view_dict = dict()
            view_dict['name'] = conf.get('name')
            view_dict['include'] = conf.get('included')
            view_dict['exclude'] = conf.get('excluded')
            view_list.append(view_dict)
        payload_url['SNMP_SERVER_VIEW_LIST'] = view_list
        return payload_url

    def build_create_contact_payload(self, config):
        """ Build the payload for SNMP contact

        :rtype: A dictionary
        :returns: The payload for SNMP contact
        """
        payload_url = dict()
        contact = config.get('contact', None)
        contact_list = list()

        contact_list.append({'index': 'SYSTEM', 'sysContact': contact})
        payload_url['SNMP_SERVER_LIST'] = contact_list
        return payload_url

    def build_create_location_payload(self, config):
        """ Build the payload for SNMP location

        :rtype: A dictionary
        :returns: The payload for SNMP location
        """
        payload_url = dict()
        location = config.get('location', None)
        location_list = list()

        location_list.append({'index': 'SYSTEM', 'sysLocation': location})
        payload_url['SNMP_SERVER_LIST'] = location_list
        return payload_url

    def build_create_enable_trap_payload(self, config):
        """ Build the payload for SNMP enable_trap

        :rtype: A dictionary
        :returns: The payload for SNMP enable_trap
        """
        payload_url = dict()
        enable_trap = config.get('enable_trap', None)
        enable_trap_list = list()

        for conf in enable_trap:
            enable_trap_dict = dict()
            trap_type = conf
            if trap_type:
                trap_type = trap_type[0]
                if trap_type == 'auth-fail':
                    enable_trap_dict['authenticationFailureTrap'] = trap_type
                if trap_type == 'bgp':
                    enable_trap_dict['bgpTraps'] = 'true'
                if trap_type == 'config-change':
                    enable_trap_dict['configChangeTrap'] = 'true'
                if trap_type == 'link-down':
                    enable_trap_dict['linkDownTrap'] = 'true'
                if trap_type == 'link-up':
                    enable_trap_dict['linkUpTrap'] = 'true'
                if trap_type == 'ospf':
                    enable_trap_dict['ospfTraps'] = 'true'
                if trap_type == 'all':
                    enable_trap_dict['traps'] = 'true'
            enable_trap_list.append(enable_trap_dict)
        payload_url['SNMP_SERVER_LIST'] = enable_trap_list
        return payload_url

    def build_create_group_payload(self, config):
        """ Build the payload for SNMP group

        :rtype: A dictionary
        :returns: The payload for SNMP group
        """
        payload_url = dict()
        group_list = []
        target_e = 0
        group = config.get('group', None)
        for conf in group:
            group_dict = dict()
            group_dict['context'] = 'Default'
            group_dict['contextMatch'] = "exact"
            group_dict['groupName'] = conf.get('name')
            group_dict['notifyView'] = conf.get('access')[target_e].get('notify_view')
            group_dict['readView'] = conf.get('access')[target_e].get('read_view')
            group_dict['securityLevel'] = conf.get('access')[target_e].get('security_level')
            group_dict['securityModel'] = conf.get('access')[target_e].get('security_model')
            group_dict['writeView'] = conf.get('access')[target_e].get('write_view')
            group_list.append(group_dict)

            target_e = target_e + 1

        payload_url['SNMP_SERVER_GROUP_ACCESS_LIST'] = group_list
        return payload_url

    def build_create_enable_target_payload(self, config):
        """ Build the payload for SNMP target information based on the given host configuration

        :rtype: A dictionary
        :returns: The payload for SNMP target
        """
        payload_url = dict()
        target_list = []
        global target_entry
        target = config.get('host', None)

        for conf in target:
            target_dict = dict()
            target_entry_name = 'targetEntry' + str(target_entry)
            target_dict['ip'] = conf.get('ip')
            target_dict['name'] = target_entry_name
            target_dict['port'] = conf.get('port')
            target_dict['retries'] = conf.get('retries')
            target_dict['timeout'] = conf.get('timeout')
            tag_list = list()
            if conf.get('tag'):
                tag_list.append(str(conf.get('tag')) + "Notify")
            target_dict["tag"] = tag_list
            target_dict['targetParams'] = target_entry_name

            target_entry = target_entry + 1
            target_list.append(target_dict)

        payload_url['SNMP_SERVER_TARGET_LIST'] = target_list

        return payload_url

    def build_create_enable_server_payload(self, config):
        """ Build the payload for SNMP param information based on the given host configuration

        :rtype: A dictionary
        :returns: The payload for SNMP target
        """
        payload_url = dict()
        server_list = []
        global target_entry
        server = config.get('host', None)

        for conf in server:
            server_dict = dict()
            target_entry_name = 'targetEntry' + str(target_entry)
            if conf.get('user') is None:
                server_dict['name'] = target_entry_name
                server_dict['securityNameV2'] = conf.get('community')
            else:
                server_dict['name'] = target_entry_name
                server_level = conf.get('user').get('security_level', None)
                if server_level == "auth":
                    server_dict['security-level'] = 'auth-no-priv'
                if server_level == "noauth":
                    server_dict['security-level'] = 'no-auth-no-priv'
                if server_level == "priv":
                    server_dict['security-level'] = 'auth-priv'

            target_entry = target_entry + 1
            server_list.append(server_dict)

        payload_url['SNMP_SERVER_PARAMS_LIST'] = server_list

        return payload_url, target_entry

    def get_delete_snmp_request(self, configs, have, delete_all):
        """ Create the requests necessary to delete the given configuration

        :rtype: A list
        :returns: The list of requests to delete the given configuration
        """
        requests = []

        if not configs:
            return requests

        agentaddress_requests = []
        community_requests = []
        contact_requests = []
        enable_trap_requests = []
        engine_requests = []
        group_requests = []
        host_requests = []
        location_requests = []
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

        if have.get('agentaddress') is not None and (delete_all or agentaddress):
            for want in agentaddress:
                matched_agentaddress = next((each_snmp for each_snmp in have.get('agentaddress') if each_snmp['ip'] == want['id']), None)
                if matched_agentaddress:
                    agentaddress_ip = matched_agentaddress['ip']
                    agentaddress_port = matched_agentaddress['port']
                    agentaddress_interface = matched_agentaddress['interface']
                    agentaddress_url = 'data/sonic-snmp:sonic-snmp/SNMP_AGENT_ADDRESS_CONFIG/SNMP_AGENT_ADDRESS_CONFIG_LIST={0},{1},{2}'.format(
                        agentaddress_ip, agentaddress_port, agentaddress_interface)
                    agentaddress_request = {'path': agentaddress_url, 'method': DELETE}
                    agentaddress_requests.append(agentaddress_request)
        if have.get('community') is not None and (delete_all or community):
            for want in community:
                matched_community = next((each_snmp for each_snmp in have.get('community') if each_snmp['name'] == want['name']), None)
                if matched_community:
                    community_name = matched_community['name']
                    community_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_COMMUNITY/SNMP_SERVER_COMMUNITY_LIST={0}'.format(community_name)
                    community_request = {'path': community_url, 'method': DELETE}
                    community_requests.append(community_request)
        if delete_all or contact:
            if have.get('contact') is not None:
                contact_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER/SNMP_SERVER_LIST=SYSTEM'
                contact_request = {'path': contact_url, 'method': DELETE}
                contact_request['data'] = contact
        if have.get('enable_trap') is not None and (delete_all or enable_trap):
            for want in enable_trap:
                matched_enable_trap = next((each_snmp for each_snmp in have.get('enable_trap') if each_snmp[0] == want[0]), None)
                if matched_enable_trap:
                    enable_trap_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER/SNMP_SERVER_LIST=SYSTEM'
                    enable_trap_request = {'path': enable_trap_url, 'method': DELETE}
                    enable_trap_requests.append(enable_trap_request)
        if have.get('engine') is not None and (delete_all or engine):
            matched_engine = next((each_snmp for each_snmp in have.get('engine') if each_snmp['id'] == engine['id']), None)
            if matched_engine:
                engine_id = matched_engine['id']
                engine_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_ENGINE/SNMP_SERVER_ENGINE_LIST={0}'.format(engine_id)
                engine_request = {'path': engine_url, 'method': DELETE}
                engine_requests.append(engine_request)
        if have.get('group') is not None and (delete_all or group):
            for want in group:
                matched_group = next((each_snmp for each_snmp in have.get('group') if each_snmp['name'] == want['name']), None)
                if matched_group:
                    group_name = matched_group['name']
                    matched_access = self.get_matched_access(matched_group['access'], want['access'])[0]
                    group_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_GROUP_ACCESS/SNMP_SERVER_GROUP_ACCESS_LIST={0},{1},{2},{3}'.format(
                        group_name, "Default", matched_access['security_model'], matched_access['security_level'])
                    group_request = {'path': group_url, 'method': DELETE}
                    group_requests.append(group_request)
        if have.get('host') is not None and (delete_all or host):
            for want in host:
                matched_host, name = self.get_host(want=want, have=have)
                if matched_host is not None:
                    host_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_TARGET/SNMP_SERVER_TARGET_LIST={0}'.format(name)
                    host_request = {'path': host_url, 'method': DELETE}
                    host_requests.append(host_request)
                    host_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_PARAMS/SNMP_SERVER_PARAMS_LIST={0}'.format(name)
                    host_request = {'path': host_url, 'method': DELETE}
                    host_requests.append(host_request)
        if delete_all or location:
            if have.get('location') is not None:
                location_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER/SNMP_SERVER_LIST=SYSTEM'
                location_request = {'path': location_url, 'method': DELETE}
                location_requests.append(location_request)
        if have.get('user') is not None and (delete_all or user):
            for want in user:
                matched_user = next((each_snmp for each_snmp in have.get('user') if each_snmp['name'] == want['name']), None)
                if matched_user:
                    user_name = matched_user['name']
                    user_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_USER/SNMP_SERVER_USER_LIST={0}'.format(user_name)
                    user_request = {'path': user_url, 'method': DELETE}
                    user_requests.append(user_request)
        if have.get('view') is not None and (delete_all or view):
            for want in view:
                matched_view = next((each_snmp for each_snmp in have.get('view') if each_snmp['name'] == want['name']), None)
                if matched_view:
                    view_name = matched_view['name']
                    view_url = 'data/sonic-snmp:sonic-snmp/SNMP_SERVER_VIEW/SNMP_SERVER_VIEW_LIST={0}'.format(view_name)
                    view_request = {'path': view_url, 'method': DELETE}
                    view_requests.append(view_request)

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

    def get_matched_access(self, access_list, want_access):
        """ Finds and returns the access list that matches the wanted access list

        :rtype: A list
        :returns: the access list that matches the wanted access list
        """
        matched_access = list()
        for want in want_access:
            matched_want = next((each_access for each_access in access_list
                                 if each_access['security_model'] == want['security_model']
                                 and each_access['security_level'] == want['security_level']
                                 and each_access['read_view'] == want['read_view']
                                 and each_access['write_view'] == want['write_view']
                                 and each_access['notify_view'] == want['notify_view']), None)
            matched_access.append(matched_want)
        return matched_access

    def get_host(self, want, have):
        """ Finds and returns the host that matches the wanted host

        :rtype: A list
        :returns: the host that matches the wanted host
        """
        entry = 1
        for each_host in have:
            if each_host['ip'] == want['ip']:
                return each_host, "targetEntry" + str(entry)
            entry = entry + 1
        return {}, ""
