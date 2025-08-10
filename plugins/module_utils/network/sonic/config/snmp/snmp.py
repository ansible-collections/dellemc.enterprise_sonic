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

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import ConfigBase

from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import Facts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import to_list
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    update_states,
    get_diff,
    remove_none,
    remove_empties
)

from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.formatted_diff_utils import (
    __DELETE_CONFIG,
    get_new_config,
    get_formatted_config_diff
)

PATCH = 'patch'
DELETE = 'delete'

TEST_KEYS = [
    {'agentaddress': {'name': ''}},
    {'community': {'name': ''}},
    {'group': {'name': ''}},
    {'access': {'security_model': '', 'security_level': ''}},
    {'host': {'ip': ''}},
    {'user': {'name': ''}},
    {'view': {'name': ''}}
]

TEST_KEYS_formatted_diff = [
    {'agentaddress': {'name': '', '__delete_op': __DELETE_CONFIG}},
    {'community': {'name': '', '__delete_op': __DELETE_CONFIG}},
    {'group': {'name': '', '__delete_op': __DELETE_CONFIG}},
    {'access': {'security_model': '', 'security_level': '', '__delete_op': __DELETE_CONFIG}},
    {'host': {'name': '', '__delete_op': __DELETE_CONFIG}},
    {'user': {'name': '', '__delete_op': __DELETE_CONFIG}},
    {'view': {'name': '', '__delete_op': __DELETE_CONFIG}},
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
        commands = []
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
        result['before'] = existing_snmp_facts
        old_config = existing_snmp_facts

        if self._module.check_mode:
            new_config = get_new_config(commands, existing_snmp_facts, TEST_KEYS_formatted_diff)
            result['after(generated)'] = remove_empties(new_config)
        else:
            new_config = self.get_snmp_facts()
            if result['changed']:
                result['after'] = new_config
        if self._module._diff:
            result['diff'] = get_formatted_config_diff(old_config, new_config, self._module._verbosity)

        return result

    def set_config(self, existing_snmp_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = remove_none(self._module.params['config'])
        have = existing_snmp_facts
        resp = self.set_state(want, have)
        return to_list(resp)

    def fill_in_defaults_and_compare(self, want, have, state):
        """ Fill in the defaults in the agentaddress config
        :param want: the desired configuration as a dictionary
        :rtype: A dictionary
        :returns: the desired configuration with default values filled in
        """
        if 'agentaddress' not in want:
            return want

        for conf in want.get('agentaddress'):
            if 'port' not in conf:
                conf['port'] = 161
            if 'interface_vrf' not in conf:
                conf['interface_vrf'] = 'default'
        want_agentaddresses = want.get('agentaddress')
        self.check_same_agentaddress(want_agentaddresses)
        if 'agentaddress' in have and state == 'merged':
            same = ''
            for want_conf in want_agentaddresses:
                if 'name' in want_conf:
                    for have_conf in have.get('agentaddress'):
                        if have_conf['name'] == want_conf['name']:
                            self.same_name_agents_conflict_check(want_conf, have_conf)
                        else:
                            same_option_conflict = ('ip' in want_conf and 'ip' in have_conf
                                                    and want_conf.get('ip') == have_conf.get('ip')
                                                    and ('port' in want_conf and 'port' in have_conf and
                                                         want_conf.get('port') == have_conf.get('port'))
                                                    and ('interface_vrf' in want_conf
                                                         and 'interface_vrf' in have_conf)
                                                    and want_conf.get('interface_vrf') == have_conf.get('interface_vrf'))
                            if same_option_conflict:
                                same = want_conf['name']
                                same_conflict = have_conf['name']
                                self._module.fail_json(msg="Agentaddress option values for input agentadress entry {}".format(same)
                                                       + " conflict with option values for existing agentaddress entry {}.".format(same_conflict)
                                                       + " Please change the values for agentaddress entry {} or remove it from the play.".format(same))
                else:
                    # Unnamed input agentaddress entry: Determine if it matches an existing
                    # agentaddress and use the name of the matching agentaddress if there is one.
                    for have_conf in have.get('agentaddress'):
                        matched = True
                        for key, value in want_conf.items():
                            if have_conf[key] != value:
                                matched = False
                                break
                        if matched:
                            want_conf['name'] = have_conf.get('name')
                            break

        return want

    def merged_config(self, have_conf, want_conf):
        default_values = {
            'ip': "",
            'port': 161,
            'interface_vrf': 'default'
        }

        merged_conf = {}
        for key, value in have_conf.items():
            merged_conf[key] = have_conf[key]
            if want_conf.get(key) is not None and want_conf.get(key) != default_values[key]:
                merged_conf[key] = want_conf[key]
        return merged_conf

    def same_name_agents_conflict_check(self, want_conf, have_conf):
        """ Check to see if the merged result of an input agentaddress entry with an existing agenteaddress entry having the same
        name conflicts with any other existing agentaddress entry with a different name.
        """
        merged_conf = self.merged_config(have_conf, want_conf)
        for have_conf in have_conf.get('agentaddress'):
            check_same = self.same_agentaddress(merged_conf, have_conf)
            if check_same:
                self._module.fail_json(msg="The specified options are in use for an existing agent.")
                break

    def same_agentaddress(self, merged_conf, have_conf):
        """ Returns true if the wanted agent has the same values and keys as the given agent

        :rtype: boolean
        :returns: True if the keys and values are the same
        """
        for key, value in merged_conf.items():
            if merged_conf[key] != have_conf[key]:
                return False
        return True

    def check_same_agentaddress(self, want_agentaddress):
        """ Check if the agentaddress option values are the same
        :param want_agentaddress: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        """
        same = {}
        want_agentaddresses = want_agentaddress

        for index, want_conf in enumerate(want_agentaddresses, 0):
            for want_conf_2 in want_agentaddresses[index + 1:]:
                if 'name' in want_conf and 'name' in want_conf_2 and want_conf.get('name') == want_conf_2.get('name'):
                    self._module.fail_json(msg="Agentaddress name '{}' is used twice in this play.".format(want_conf['name'])
                                           + " Please consolidate the configuration for this agentaddress entry or use"
                                           + " a different name for the second instance.")
        for index, want_conf in enumerate(want_agentaddresses, 0):
            for want_conf_2 in want_agentaddresses[index + 1:]:
                same_option_conflict = ('ip' in want_conf and 'ip' in want_conf_2
                                        and want_conf.get('ip') == want_conf_2.get('ip')
                                        and ('port' in want_conf and 'port' in want_conf_2 and want_conf.get('port') == want_conf_2.get('port'))
                                        and ('interface_vrf' in want_conf and 'interface_vrf' in want_conf_2)
                                        and want_conf.get('interface_vrf') == want_conf_2.get('interface_vrf'))
                if same_option_conflict:
                    same = {'ip': want_conf.get('ip'), 'port': want_conf.get('port'), 'interface_vrf': want_conf.get('interface_vrf')}
                    break

        if same:
            self._module.fail_json(msg="Agentaddress option values must be unique. Two agentaddress entries are specified in this play with"
                                   + " the same option values. Please change or remove one of the duplicate agentaddress options sets currently"
                                   + " set as follows: {}".format(same))

        return

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
        if state == 'merged' or state == 'overridden' or state == 'replaced':
            want = self.fill_in_defaults_and_compare(want, have, state)
        if state == 'overridden' or state == 'replaced':
            commands, requests = self._state_replaced_or_overridden(want, have, state)
        elif state == 'deleted':
            commands, requests = self._state_deleted(want, have)
        elif state == 'merged':
            commands, requests = self._state_merged(want, have)

        return commands, requests

    def _state_replaced_or_overridden(self, want, have, state):
        """
        The command generator when state is overridden
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        requests = []

        if not want:
            return commands, requests

        diff_want = get_diff(want, have, TEST_KEYS)
        del_commands = get_diff(have, want, TEST_KEYS)
        if not diff_want and not del_commands:
            return commands, requests
        merged_commands = None
        merged_request = None

        if del_commands:
            if state == 'replaced':
                pop_list = []
                for option in del_commands:
                    if not want.get(option):
                        pop_list.append(option)
                for option in pop_list:
                    del_commands.pop(option)
            if 'agentaddress' in del_commands and 'agentaddress' in want:
                for command in del_commands.get('agentaddress'):
                    # If no differences were found other than 'name' (which is auto-generated for the config),
                    # don't delete this entry.
                    if len(command) == 1 and command.get('name'):
                        del_commands['agentaddress'].remove(command)
                if len(del_commands['agentaddress']) == 0:
                    del_commands.pop('agentaddress')
            if 'host' in del_commands and 'host' in want:
                delete_these_hosts = []
                for command in del_commands.get('host'):
                    # If no differences were found other than 'name' (which is auto-generated for the config),
                    # don't delete this entry.
                    new_command = {}
                    if (((len(command) == 1 and 'name' in command) or (len(command) == 2 and 'name' in command and 'ip' in command)
                         or (len(command) == 3 and 'ip' in command and 'port' in command and 'name' in command))):
                        break
                    else:
                        new_command = command

                    if (new_command):
                        delete_these_hosts.append(new_command)

                if len(delete_these_hosts) == 0:
                    del_commands.pop('host')
                else:
                    del_commands['host'] = delete_these_hosts
            if len(del_commands) > 0:
                del_requests = self.get_delete_snmp_request(del_commands, have, False)
                if del_requests:
                    requests.extend(del_requests)
                    commands.extend(update_states(del_commands, "deleted"))

                merged_commands = diff_want
                merged_request = self.get_create_snmp_request(merged_commands, have, True)
                if merged_request:
                    requests.extend(merged_request)
                    commands.extend(update_states(merged_commands, state))

        else:
            merged_request = self.get_create_snmp_request(diff_want, have, True)
            requests.extend(merged_request)
            commands.extend(update_states(diff_want, state))
        return commands, requests

    def _state_merged(self, want, have):
        """ The command generator when state is merged
        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = get_diff(want, have, TEST_KEYS)
        request_commands = commands
        commands_updated = []
        del_commands = {}
        delete_user_requests = []
        requests = []
        new_have = {}
        if 'user' in want:
            delete_user_requests = self.delete_snmp_matched_user_config(commands, have)
            requests = delete_user_requests
            del_commands = {'user': self.get_existing_user(commands, have)}
            new_have = get_diff(have, del_commands)
            request_commands = get_diff(want, new_have, TEST_KEYS)
        else:
            new_have = have

        requests.extend(self.get_create_snmp_request(request_commands, new_have, False))

        if commands and len(requests) > 0:
            if 'user' in del_commands and len(del_commands['user']) > 0:
                commands_updated.extend(update_states(del_commands, "deleted"))
            commands_updated.extend(update_states(request_commands, "merged"))
        else:
            commands_updated = []

        return commands_updated, requests

    def _state_deleted(self, want, have):
        """ The command generator when state is deleted
        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        requests = []
        commands = []

        if not have:
            return commands, requests

        delete_all = False

        if have is None:
            return commands, requests
        if not want or want is None:
            commands = have
            delete_all = True
        else:
            if 'agentaddress' in want:
                for want_agentaddress in want['agentaddress']:
                    if not want_agentaddress.get('name'):
                        self._module.fail_json(msg="An Agent name is required to delete an agentaddress entry.")
            new_want = self.get_configured_option(want, have)
            reverse_diff = get_diff(have, new_want, TEST_KEYS)
            commands = get_diff(have, reverse_diff, TEST_KEYS)

        requests = self.get_delete_snmp_request(commands, have, delete_all)

        if commands and len(requests) > 0:
            commands = update_states(commands, "deleted")
        else:
            commands = []

        return commands, requests

    def get_configured_option(self, want, config):
        """ Gets the already configured option when want contains an empty list

        :rtype: A dict
        :returns: the already configured option
        """
        new_config = {}
        for key, value in want.items():
            name = ''
            if value == [] and key in config:
                new_config[key] = config[key]
            else:
                if isinstance(value, list) and key in config:
                    new_config_value = []
                    for v in value:
                        if 'name' in v and len(v) == 1:
                            name = v['name']
                            matched_v = next((x for x in config[key] if x['name'] == name), None)
                            if matched_v:
                                new_config_value.append(matched_v)
                        else:
                            new_config_value.append(v)
                    new_config[key] = new_config_value
                else:
                    new_config[key] = value

        return new_config

    def get_create_snmp_request(self, config, have, overridden_or_replaced):
        """ Create the requests necessary to create the desired configuration
        :rtype: A list
        :returns: the requests necessary to create the desired configuration
        """
        requests = []
        method = PATCH

        if config.get('agentaddress'):
            agentaddress_path = "data/ietf-snmp:snmp/engine"
            payload_url = self.get_agentaddress_requests(config, have, overridden_or_replaced)
            agentaddress_request = {'path': agentaddress_path, 'method': method, 'data': payload_url}
            requests.append(agentaddress_request)

        if config.get('community'):
            community_requests = self.build_create_community_payload(config, have)
            requests.extend(community_requests)
            group_path = "data/ietf-snmp:snmp/vacm"
            for conf in config['community']:
                requests.append(self.build_create_group_community_request(conf))

        if config.get('contact'):
            contact_path = "data/ietf-snmp:snmp/ietf-snmp-ext:system/contact"
            payload = self.build_create_contact_payload(config)
            contact_request = {'path': contact_path, 'method': method, 'data': payload}
            requests.append(contact_request)

        if config.get('enable_trap'):
            enable_trap_requests = self.build_create_enable_trap_requests(config)
            requests.extend(enable_trap_requests)

        if config.get('engine'):
            engine_path = "data/ietf-snmp:snmp/engine"
            payload = self.build_create_engine_payload(config)
            engine_request = {'path': engine_path, 'method': method, 'data': payload}
            requests.append(engine_request)

        if config.get('group'):
            group_path = "data/ietf-snmp:snmp/vacm"
            payload = self.build_create_group_payload(config)
            group_request = {'path': group_path, 'method': method, 'data': payload}
            requests.append(group_request)

        if config.get('host'):
            config_copy = deepcopy(config)
            target_params_request = self.build_create_enable_target_params_payload(config_copy, have, overridden_or_replaced)
            requests.extend(target_params_request)
            target_path = "data/ietf-snmp:snmp/target"
            payload = self.build_create_enable_target_payload(config_copy)
            target_request = {'path': target_path, 'method': method, 'data': payload}
            requests.append(target_request)

        if config.get('location'):
            location_path = "data/ietf-snmp:snmp/ietf-snmp-ext:system/location"
            payload = self.build_create_location_payload(config)
            location_request = {'path': location_path, 'method': method, 'data': payload}
            requests.append(location_request)

        if config.get('user'):
            user_path = "data/ietf-snmp:snmp/usm/local/user"
            payload = self.build_create_user_payload(config)
            users_request = {'path': user_path, "method": method, 'data': payload}
            requests.append(users_request)

            users = config.get('user')
            for user in users:
                requests.append(self.create_user_group_request(user))

        if config.get('view'):
            views_path = "data/ietf-snmp:snmp/vacm"
            payload = self.build_create_view_payload(config)
            views_request = {'path': views_path, 'method': method, 'data': payload}
            requests.append(views_request)

        return requests

    def get_agentaddress_requests(self, config, have, overridden_or_replaced):
        """ Build the payload for SNMP agentaddress
        :rtype: A dictionary
        :returns: The payload for SNMP agentaddress
        """
        agentaddress = config.get('agentaddress')
        have_agentaddress = have.get('agentaddress')
        have_agentaddress_names = []
        if have_agentaddress and not overridden_or_replaced:
            have_agentaddress_names = [agent_entry.get('name') for agent_entry in have_agentaddress]
        agentaddress_list = []
        agentaddressdict = {}
        payload_url = {}
        for conf in agentaddress:
            name = ""
            agentaddress_dict = {}
            interface = ""
            if 'name' in conf:
                for agent_entry in have_agentaddress:
                    if ((agent_entry.get('ip') == conf.get('ip') and agent_entry.get('port') == conf.get('port')
                         and agent_entry.get('name') != conf['name'] and agent_entry.get('interface_vrf') == conf.get('interface_vrf'))):
                        self._module.fail_json(msg="The specified options are in use for an existing agent.")

                name = conf.get('name')

            else:
                vrf = ""
                # if there is already a matching agent, use that one
                if have_agentaddress:
                    for agent_entry in have_agentaddress:
                        if ((agent_entry.get('ip') == conf.get('ip')
                             and agent_entry.get('port') == conf.get('port') and agent_entry.get('interface_vrf') == conf.get('interface_vrf'))):
                            name = agent_entry.get('name')
                            conf['name'] = name
            if len(name) == 0:
                name = self.get_agententry(have_agentaddress_names)
                conf['name'] = name
            vrf = conf.get('interface_vrf')
            if vrf:
                interface = vrf
            else:
                interface = conf.get('interface')

            udp_dict = {}
            if interface:
                udp_dict['ietf-snmp-ext:interface'] = interface
            agentaddress_dict['name'] = name
            udp_dict['ip'] = conf.get('ip')
            if conf.get('port'):
                udp_dict['port'] = conf['port']
            agentaddress_dict['udp'] = udp_dict
            agentaddress_list.append(agentaddress_dict)

        agentaddressdict['listen'] = agentaddress_list
        payload_url['ietf-snmp:engine'] = agentaddressdict

        return payload_url

    def build_create_community_payload(self, config, have):
        """ Build the payload for SNMP community
        :rtype: A dictionary
        :returns: The list of community requests
        """
        community = config.get('community')
        community_list = []
        payload_url = {}
        community_requests = []
        community_path = "data/ietf-snmp:snmp/community"

        for conf in community:
            community_dict = {}
            community_dict['index'] = conf.get('name')
            community_group_name = conf.get('group')
            if have and len(have) > 0 and have.get('group'):
                for group in have.get('group'):
                    if 'security-name' in group and group['security-name'] == conf.get('name') and group.get('name') != community_group_name:
                        # If this community is already a member of some group other than the new requested group,
                        # remove the "member" entry for this community in the "old" group member list.
                        group_name = group.get('name')
                        group_url = "data/ietf-snmp:snmp/vacm/group={0}/member={1}".format(group_name, group.get('security-name'))
                        group_request = {"path": group_url, "method": DELETE}
                        community_requests.append(group_request)

            community_dict['security-name'] = community_group_name
            community_list.append(community_dict)
        payload_url['community'] = community_list

        community_requests.append({'path': community_path, 'method': PATCH, 'data': payload_url})
        return community_requests

    def build_create_group_community_request(self, conf):
        """ Build the payload for the group associated with SNMP community
        :rtype: A dictionary
        :returns: The payload for the group associated with SNMP community
        """
        community_list = []
        payload_url = {}

        member_dict = {}
        member_dict['security-model'] = ['v2c']
        member_dict['security-name'] = conf.get('name')
        member_dict_list = []
        member_dict_list.append(member_dict)
        group_dict = {}
        group_dict['name'] = conf.get('group')
        group_dict['member'] = member_dict_list

        community_list.append(group_dict)

        group_payload = {'group': community_list}
        payload_url['ietf-snmp:vacm'] = group_payload

        request = {'path': "data/ietf-snmp:snmp/vacm", 'method': PATCH, 'data': payload_url}
        return request

    def build_create_engine_payload(self, config):
        """ Build the payload for SNMP engine
        :rtype: A dictionary
        :returns: The payload for SNMP engine
        """
        engine = str(config.get('engine'))
        payload_url = {}

        payload_url['ietf-snmp:engine'] = {'engine-id': engine}
        return payload_url

    def build_create_user_payload(self, config):
        """ Build the payload for SNMP user
        :rtype: A dictionary
        :returns: The payload for SNMP user
        """
        user = config.get('user')
        user_list = []
        payload_url = {}

        if user is None:
            return payload_url

        for conf in user:
            user_dict = {}
            auth_dict = {}
            priv_dict = {}
            auth_key = {}
            priv_key = {}
            user_dict['name'] = conf.get('name')
            if conf.get('encrypted') is not None:
                user_dict['encrypted'] = conf['encrypted']
            else:
                user_dict['encrypted'] = False

            priv_conf = conf.get('priv')
            auth_conf = conf.get('auth')
            if priv_conf and 'priv_type' in priv_conf and 'key' in priv_conf:
                priv_type = priv_conf['priv_type']
                priv_key['key'] = priv_conf['key']
                priv_dict[priv_type] = priv_key
                user_dict['priv'] = priv_dict
            if auth_conf and 'auth_type' in auth_conf and 'key' in auth_conf:
                auth_type = auth_conf['auth_type']
                auth_key['key'] = auth_conf['key']
                auth_dict[auth_type] = auth_key
                user_dict['auth'] = auth_dict
            if user_dict:
                user_list.append(user_dict)

        payload_url['user'] = user_list
        return payload_url

    def create_user_group_request(self, conf):
        """ Build the payload for SNMP group members based on the given user information
        :rtpe: A dictionary
        :returns: The request for SNMP group members
        """
        group_dict = {}
        group_list = []
        member = {}
        payload_url = {}
        path = "data/ietf-snmp:snmp/vacm"
        if conf.get('group') is not None:
            member['security-model'] = ["usm"]
            member['security-name'] = conf.get('name')
            group_dict['member'] = [member]
            group_dict['name'] = conf.get('group')
            group_list.append(group_dict)

        payload_url['ietf-snmp:vacm'] = {'group': group_list}
        request = {'path': path, 'method': PATCH, 'data': payload_url}
        return request

    def build_create_view_payload(self, config):
        """ Build the payload for SNMP view
        :rtype: A dictonary
        :returns: The payload for SNMP view
        """
        view_list = []
        payload_url = {}
        viewdict = {}
        view = config.get('view')

        for conf in view:
            view_dict = {}
            view_dict['name'] = conf.get('name')
            view_dict['include'] = conf.get('included')
            view_dict['exclude'] = conf.get('excluded')
            view_list.append(view_dict)
        viewdict['view'] = view_list
        payload_url['ietf-snmp:vacm'] = viewdict
        return payload_url

    def build_create_contact_payload(self, config):
        """ Build the payload for SNMP contact
        :rtype: A dictionary
        :returns: The payload for SNMP contact
        """
        payload_url = {}
        contact = config.get('contact')

        payload_url['ietf-snmp-ext:contact'] = str(contact)
        return payload_url

    def build_create_location_payload(self, config):
        """ Build the payload for SNMP location
        :rtype: A dictionary
        :returns: The payload for SNMP location
        """
        payload_url = {}
        location = config.get('location')

        payload_url['ietf-snmp-ext:location'] = location
        return payload_url

    def build_create_enable_trap_requests(self, config):
        """ Build the payload for SNMP enable_trap
        :rtype: A list of requests to patch the desired traps
        :returns: The requests to patch the desired traps
        """
        enable_trap_url = 'data/ietf-snmp:snmp/ietf-snmp-ext:system/notifications'
        enable_trap = config.get('enable_trap')
        method = PATCH
        requests = []
        payload = {}
        enable_trap_dict = {}
        if 'all' in enable_trap and len(enable_trap) != 1:
            self._module.fail_json(msg="enable_trap value 'all' cannot be set together with other enable_trap values.")

        for conf in enable_trap:
            trap_type = conf
            if trap_type:
                if trap_type == 'all':
                    all_traps_url = "data/ietf-snmp:snmp/ietf-snmp-ext:system/trap-enable"
                    enable_trap_dict['trap-enable'] = True
                    trap_enable_request = {'path': all_traps_url, 'method': method, 'data': enable_trap_dict}
                    requests.append(trap_enable_request)
                    return requests
                else:
                    if trap_type == 'auth-fail':
                        enable_trap_dict['authentication-failure-trap'] = True
                    if trap_type == 'bgp':
                        enable_trap_dict['bgp-traps'] = True
                    if trap_type == 'config-change':
                        enable_trap_dict['config-change-trap'] = True
                    if trap_type == 'link-down':
                        enable_trap_dict['link-down-trap'] = True
                    if trap_type == 'link-up':
                        enable_trap_dict['link-up-trap'] = True
                    if trap_type == 'ospf':
                        enable_trap_dict['ospf-traps'] = True

            payload['ietf-snmp-ext:notifications'] = enable_trap_dict
        trap_enable_request = {'path': enable_trap_url, 'method': method, 'data': payload}
        requests.append(trap_enable_request)
        return requests

    def build_create_group_payload(self, config):
        """ Build the payload for SNMP group
        :rtype: A dictionary
        :returns: The payload for SNMP group
        """
        payload_url = {}
        group_list = []
        group = config.get('group')
        group_payload = {}
        for conf in group:
            group_dict = {}
            if conf.get('name') is None:
                break
            group_dict['name'] = conf.get('name')
            group_dict['access'] = self.build_create_group_access_payload(conf)
            group_list.append(group_dict)
        group_payload['group'] = group_list
        payload_url['ietf-snmp:vacm'] = group_payload
        return payload_url

    def build_create_group_access_payload(self, config):
        """ Build the payload for the SNMP group access suboption
        :rtype: A list of dictionaries
        :returns: the list of access
        """
        access_list = []
        access_dicts = config.get('access')
        if access_dicts is None:
            return access_list
        for access in access_dicts:
            access_dict = {}
            access_dict['context'] = 'Default'
            access_dict['notify-view'] = access.get('notify_view')
            access_dict['read-view'] = access.get('read_view')
            access_dict['write-view'] = access.get('write_view')
            security_level = access.get('security_level')
            security_model = access.get('security_model')
            if security_level:
                access_dict['security-level'] = security_level
            access_dict['security-model'] = security_model
            access_list.append(access_dict)

        return access_list

    def build_create_enable_target_payload(self, config):
        """ Build the payload for SNMP target information based on the given host configuration
        :rtype: A dictionary
        :returns: The payload for SNMP target
        """
        payload_url = {}
        target_list = []
        target = config.get('host')

        for conf in target:
            target_dict = {}
            retries = conf.get('retries')

            target_dict['name'] = conf.get('name')
            tag_list = []
            tag = None
            if 'tag' in conf:
                tag = str(conf.get('tag')) + "Notify"
                tag_list.append(tag)
            if conf.get('vrf') and 'tag' in conf:
                tag_list.append(str(conf.get('vrf')))
            if len(tag_list) == 0:
                tag_list = None

            port = conf.get('port')
            if not port:
                port = 162
            target_dict['udp'] = {'ip': conf.get('ip'), 'port': port, 'ietf-snmp-ext:vrf-name': conf.get('vrf')}
            if tag_list:
                target_dict["tag"] = tag_list
            target_dict['timeout'] = conf.get('timeout')
            target_dict['retries'] = retries
            target_dict['target-params'] = conf.get('name')
            if 'source_interface' in conf:
                target_dict['ietf-snmp-ext:source-interface'] = conf.get('source_interface')
            target_list.append(target_dict)

        payload_url['target'] = target_list
        return payload_url

    def build_create_enable_target_params_payload(self, config, have, overridden_or_replaced):
        """ Build the payload for SNMP param information based on the given host configuration
        :rtype: A dictionary
        :returns: The payload for SNMP target
        """
        payload_url = {}
        requests = []
        target_params_list = []

        server = config.get('host')
        have_targetentry = have.get('host')
        have_targetentry_names = []
        if have_targetentry:
            have_targetentry_names = [host_entry.get('name') for host_entry in have_targetentry]
        for conf in server:
            target_params_dict = {}
            target_entry_name = ""
            matched_host = None
            if 'name' in conf:
                target_entry_name = conf['name']
                matched_host = next((x for x in have_targetentry if x.get('name') == target_entry_name), None)
            elif have_targetentry:
                matched_host = next((host for host in have_targetentry if host.get('ip') == conf.get('ip')
                                     and host.get('vrf') == conf.get('vrf')), None)
                if matched_host:
                    target_entry_name = matched_host['name']
            if not target_entry_name:
                target_entry_name = self.get_targetentry(have_targetentry_names)
            conf['name'] = target_entry_name
            if overridden_or_replaced:
                if matched_host and 'community' in conf and 'usm' in matched_host or 'user' in conf and 'v2c' in matched_host:
                    # delete user from matched_host before replacing it with the new community
                    # delete community from matched_host
                    delete_target_path = 'data/ietf-snmp:snmp/target={0}'.format(target_entry_name)
                    target_request = {'path': delete_target_path, 'method': DELETE}
                    requests.append(target_request)
                    delete_target_params_path = 'data/ietf-snmp:snmp/target-params={0}'.format(target_entry_name)
                    target_params_request = {'path': delete_target_params_path, 'method': DELETE}
                    requests.append(target_params_request)
            target_params_dict['name'] = target_entry_name
            type_info = {}
            if conf.get('user') is None:
                if 'community' in conf:
                    if matched_host and 'user' in matched_host:
                        self._module.fail_json(msg="Incompatible configuration: Before adding " +
                                               "'community' configuration for this host, the " +
                                               "existing 'user' configuration must be removed.")
                    type_info['security-name'] = conf.get('community')
                    target_params_dict['v2c'] = type_info
            else:
                if matched_host and 'community' in matched_host:
                    self._module.fail_json(msg="Incompatible configuration: Before adding 'user' " +
                                           "configuration for this host, the existing" +
                                           "'community' configuration must be removed.")

                server_level = conf.get('user').get('security_level')
                if server_level == "auth":
                    type_info['security-level'] = 'auth-no-priv'
                if server_level == "noauth":
                    type_info['security-level'] = 'no-auth-no-priv'
                if server_level == "priv":
                    type_info['security-level'] = 'auth-priv'
                type_info['user-name'] = conf.get('user').get('name')
                target_params_dict['usm'] = type_info

            target_params_list.append(target_params_dict)

        payload_url['target-params'] = target_params_list
        target_params_request = {'path': 'data/ietf-snmp:snmp/target-params', 'method': PATCH, 'data': payload_url}
        requests.append(target_params_request)
        return requests

    def get_existing_user(self, configs, have=None):
        """ Return the users that are in configs and have

        :rtype: A list
        :returns: The list of users that exist in both configs and have
        """
        have_users = have.get('user')
        want_users = configs.get('user')
        matched_users = []
        if want_users and have_users:
            for want in want_users:
                matched_user = next((each_snmp for each_snmp in have_users if each_snmp['name'] == want['name']), None)
                if matched_user:
                    matched_users.append(matched_user)
        return matched_users

    def delete_snmp_matched_user_config(self, configs, have):
        """ Create requests to delete the users in "have" that match users in the playbook input configs parameter
        :rtype: A list
        :returns: The list of requests to delete the users in "configs" from the current configuration
        """
        want_users = configs.get('user')
        requests = []
        user_requests = []
        if have.get('user') is None:
            return requests
        if want_users:
            have_user = have.get('user')
            want_users = configs['user']
            matched_users = []
            if want_users:
                for want in want_users:
                    matched_user = next((each_snmp for each_snmp in have_user if each_snmp['name'] == want['name']), None)
                    if matched_user:
                        matched_users.extend(matched_user)
                        user_url = "data/ietf-snmp:snmp/usm/local/user={}".format(matched_user['name'])
                        user_request = {"path": user_url, "method": DELETE}
                        user_requests.append(user_request)

        return user_requests

    def same_options(self, options_1, options_2):
        """ Determines if the given list of options have the same values

        :rtype: Boolean
        :returns: True if the values are the same
        """
        for key1, value1 in options_1.items():
            for key2, value2 in options_2.items():
                if key1 == key2:
                    if value1 != value2:
                        return False
        return True

    def get_delete_snmp_request(self, configs, have, delete_all):
        """ Create the requests necessary to delete the given configuration
        :rtype: A list
        :returns: The list of requests to delete the users in "configs" from the current configuration
        """
        requests = []
        if not configs:
            return requests

        agentaddress_requests_list = []
        community_requests_list = []
        contact_requests_list = []
        enable_trap_requests_list = []
        engine_requests_list = []
        group_requests_list = []
        host_requests_list = []
        location_requests_list = []
        user_requests_list = []
        view_requests_list = []

        agentaddress = 'agentaddress' in configs
        community = 'community' in configs
        contact = 'contact' in configs
        enable_trap = 'enable_trap' in configs
        engine = 'engine' in configs
        group = 'group' in configs
        host = 'host' in configs
        location = 'location' in configs
        user = 'user' in configs
        view = 'view' in configs

        have_agentaddress = have.get('agentaddress')
        have_community = have.get('community')
        have_contact = have.get('contact')
        have_enable_trap = have.get('enable_trap')
        have_engine = have.get('engine')
        have_group = have.get('group')
        have_host = have.get('host')
        have_location = have.get('location')
        have_user = have.get('user')
        have_view = have.get('view')

        if delete_all or agentaddress:
            if have_agentaddress is not None:
                agentaddress_requests = []
                if delete_all or self.check_dicts_matched(have_agentaddress, configs['agentaddress']):
                    agentaddress_url = "data/ietf-snmp:snmp/engine/listen"
                    agentaddress_request = {"path": agentaddress_url, "method": DELETE}
                    agentaddress_requests.append(agentaddress_request)
                else:
                    after_deletion = get_diff(configs['agentaddress'], have_agentaddress)
                    for want in configs['agentaddress']:
                        matched_agentaddress = next((each_snmp for each_snmp in have_agentaddress if each_snmp['name'] == want['name']), None)
                        if matched_agentaddress:
                            name = matched_agentaddress['name']

                            agentaddress_url = "data/ietf-snmp:snmp/engine/listen={0}".format(name)
                            # Delete the whole agentaddress entry if only 'name' and 'ip' are specified.
                            if want.get('name') and want.get('ip') and len(want) == 2 or len(want) == len(matched_agentaddress):
                                agentaddress_request = {"path": agentaddress_url, "method": DELETE}
                                agentaddress_requests.append(agentaddress_request)
                            else:
                                interface_vrf = want.get('interface_vrf')
                                ip = want.get('ip')
                                port = want.get('port')
                                if port:
                                    if want in after_deletion:
                                        after_deletion.get(want)['port'] = 161
                                if interface_vrf:
                                    if want in after_deletion:
                                        after_deletion.get(want)['interface_vrf'] = 'default'
                                for index, after_want in enumerate(after_deletion, 0):
                                    for after_want_2 in after_deletion[index + 1:]:
                                        if self.same_options(after_want, after_want_2):
                                            self._module.fail_json(msg="Deletion of these options will create a conflict."
                                                                   + " Deleting the entire agent would be better.")

                                # Handle deletion of UDP options.
                                for option in ('interface_vrf', 'port'):
                                    if option not in matched_agentaddress or option in want:
                                        continue
                                    else:
                                        self.check_same_agentaddress(configs['agentaddress'])
                                        break
                                if interface_vrf or port:
                                    add_interface_vrf_list = []
                                    payload_url = {}
                                    agentaddress_dict = {}
                                    agentaddressdict = {}
                                    udp_dict = {}
                                    if interface_vrf:
                                        udp_dict['ietf-snmp-ext:interface'] = 'default'
                                    if port:
                                        udp_dict['port'] = 161

                                    udp_dict['ip'] = ip
                                    agentaddress_dict['udp'] = udp_dict
                                    agentaddress_dict['name'] = name
                                    add_interface_vrf_list.append(agentaddress_dict)
                                    agentaddressdict['listen'] = add_interface_vrf_list
                                    payload_url['ietf-snmp:engine'] = agentaddressdict
                                    request = {'path': 'data/ietf-snmp:snmp/engine', 'method': PATCH, 'data': payload_url}
                                    agentaddress_requests.append(request)

                if agentaddress_requests:
                    agentaddress_requests_list.extend(agentaddress_requests)

        if delete_all or community:
            if have_community is not None:
                community_requests = []
                if delete_all or self.check_dicts_matched(have_community, configs['community']):
                    community_url = "data/ietf-snmp:snmp/community"
                    community_request = {"path": community_url, "method": DELETE}
                    community_requests.append(community_request)
                else:
                    for want in configs['community']:
                        matched_community = next((each_snmp for each_snmp in have_community if each_snmp['name'] == want['name']), None)
                        if matched_community:
                            community_name = matched_community.get('name')
                            group_name = matched_community.get('group')
                            community_url = "data/ietf-snmp:snmp/community={0}".format(community_name)
                            if group_name and community_name:
                                community_sn_url = community_url + "/security-name"
                                security_name_request = {"path": community_sn_url, "method": DELETE}
                                community_requests.append(security_name_request)
                                community_request = {"path": community_url, "method": DELETE}
                                community_requests.append(community_request)
                            else:
                                # Delete this community if only the 'name' is specified
                                community_request = {"path": community_url, "method": DELETE}
                                community_requests.append(community_request)

                if community_requests:
                    community_requests_list.extend(community_requests)

        if delete_all or contact:
            if have_contact is not None:
                contact_url = "data/ietf-snmp:snmp/ietf-snmp-ext:system/contact"
                contact_request = {"path": contact_url, "method": DELETE}
                contact_requests_list.append(contact_request)

        if delete_all or enable_trap:
            if have_enable_trap is not None:
                enable_trap_requests = []
                if configs.get('enable_trap'):
                    enable_trap_url = ""
                    trap_rest_names = {
                        'link-down': 'link-down-trap',
                        'link-up': 'link-up-trap',
                        'config-change': 'config-change-trap',
                        'ospf': 'ospf-traps',
                        'bgp': 'bgp-traps',
                        'auth-fail': 'authentication-failure-trap'
                    }
                    trap_notify_url_base = "data/ietf-snmp:snmp/ietf-snmp-ext:system/notifications/"
                    delete_traps = configs.get('enable_trap')
                    if 'all' in delete_traps:
                        enable_trap_url = "data/ietf-snmp:snmp/ietf-snmp-ext:system/trap-enable"
                        enable_trap_request = {"path": enable_trap_url, "method": DELETE}
                        enable_trap_requests.append(enable_trap_request)
                    else:
                        for delete_trap in delete_traps:
                            enable_trap_url = trap_notify_url_base + trap_rest_names[delete_trap]
                            enable_trap_request = {"path": enable_trap_url, "method": DELETE}
                            enable_trap_requests.append(enable_trap_request)
                if enable_trap_requests:
                    enable_trap_requests_list.extend(enable_trap_requests)

        if delete_all or engine:
            if have_engine is not None:
                engine_url = "data/ietf-snmp:snmp/engine"
                engine_request = {"path": engine_url, "method": DELETE}
                engine_requests_list.append(engine_request)

        if delete_all or group:
            if have_group is not None:
                group_requests = []
                if delete_all or self.check_dicts_matched(have_group, configs['group']):
                    group_url = "data/ietf-snmp:snmp/vacm/group"
                    group_request = {"path": group_url, "method": DELETE}
                    group_requests.append(group_request)
                else:
                    for want in configs['group']:
                        matched_group = next((each_snmp for each_snmp in have_group if each_snmp['name'] == want['name']), None)
                        if matched_group:
                            group_name = matched_group['name']
                            if len(want) == len(matched_group):
                                group_url = "data/ietf-snmp:snmp/vacm/group={0}".format(group_name)
                                group_request = {"path": group_url, "method": DELETE}
                                group_requests.append(group_request)
                            else:
                                if 'access' in want:
                                    for access in want['access']:
                                        matched_access = next(
                                            (each_access for each_access in matched_group['access']
                                             if each_access['security_model'] == access.get('security_model')
                                             and each_access['security_level'] == access.get('security_level')), None)
                                        matched_security_model = ""
                                        if matched_access:
                                            matched_security_model = matched_access['security_model']
                                        if matched_security_model:
                                            security_model = access.get('security_model')
                                            security_level = matched_access.get('security_level')
                                            read_view = access.get('read_view')
                                            write_view = access.get('write_view')
                                            notify_view = access.get('notify_view')
                                            group_access_url = "data/ietf-snmp:snmp/vacm/group={0}/access=Default,{1},{2}".format(
                                                group_name, security_model, security_level)
                                            if not (read_view and write_view and notify_view):
                                                if read_view:
                                                    group_access_url_read_view = group_access_url + "/read-view"
                                                    group_request = {"path": group_access_url_read_view, "method": DELETE}
                                                    group_requests.append(group_request)
                                                if write_view:
                                                    group_access_url_write_view = group_access_url + "/write-view"
                                                    group_request = {"path": group_access_url_write_view, "method": DELETE}
                                                    group_requests.append(group_request)
                                                if notify_view:
                                                    group_access_url_notify_view = group_access_url + "/notify-view"
                                                    group_request = {"path": group_access_url_notify_view, "method": DELETE}
                                                    group_requests.append(group_request)
                                            else:
                                                group_request = {"path": group_access_url, "method": DELETE}
                                                group_requests.append(group_request)
                                else:
                                    if have_community:
                                        community_url = "data/ietf-snmp:snmp/community"
                                        matched_community = next((each_snmp for each_snmp in have_community if 'group' in each_snmp
                                                                  and each_snmp['group'] == want['name']), None)
                                        if matched_community:
                                            index = matched_community.get('name')
                                            community_url = "data/ietf-snmp:snmp/community={0}/security-name".format(index)
                                            community_request = {"path": community_url, "method": DELETE}
                                            group_requests.append(community_request)

                if group_requests:
                    group_requests_list.extend(group_requests)

        if delete_all or host:
            if have_host is not None:
                host_requests = []
                if delete_all or configs['host'] == [] or self.check_dicts_matched(have_host, configs['host']):
                    host_target_url = "data/ietf-snmp:snmp/target"
                    host_request = {"path": host_target_url, "method": DELETE}
                    host_requests.append(host_request)
                    host_target_params_url = "data/ietf-snmp:snmp/target-params"
                    host_request = {"path": host_target_params_url, "method": DELETE}
                    host_requests.append(host_request)
                else:
                    for want in configs['host']:
                        matched_host = self.get_host(want=want, have=have)
                        if matched_host:
                            host_target_url = "data/ietf-snmp:snmp/target={0}".format(matched_host['name'])
                            host_request = {"path": host_target_url, "method": DELETE}
                            host_requests.append(host_request)
                        else:
                            ip = want.get('ip')
                            port = want.get('port')
                            ietf_snmp_ext_vrf_name = want.get('vrf')
                            tag = want.get('tag')
                            timeout = want.get('timeout')
                            retries = want.get('retries')
                            source_interface = want.get('source_interface')
                            if not ((ip and port and ietf_snmp_ext_vrf_name and tag and timeout and retries and source_interface)
                                    or (ip and ietf_snmp_ext_vrf_name and len(want) == 2)):
                                if timeout:
                                    host_tg_url = host_target_url + '/timeout'
                                    host_request = {"path": host_tg_url, "method": DELETE}
                                    host_requests.append(host_request)
                                if retries:
                                    host_tg_url = host_target_url + '/retries'
                                    host_request = {"path": host_tg_url, "method": DELETE}
                                    host_requests.append(host_request)
                                if source_interface:
                                    host_tg_url = host_target_url + '/ietf-snmp-ext:source-interface'
                                    host_request = {"path": host_tg_url, "method": DELETE}
                                    host_requests.append(host_request)
                                if tag:
                                    host_tag_url = host_target_url + '/tag'
                                    host_tag_url += "={0}".format(tag)
                                    host_request = {"path": host_tag_url, "method": DELETE}
                                    host_requests.append(host_request)
                                if port:
                                    host_udp_url = host_target_url + '/udp/port'
                                    host_request = {"path": host_udp_url, "method": DELETE}
                                    host_requests.append(host_request)

                            else:
                                host_request = {"path": host_target_url, "method": DELETE}
                                host_requests.append(host_request)
                                host_target_params_url = "data/ietf-snmp:snmp/target-params={0}".format(matched_host['name'])
                                host_request = {"path": host_target_params_url, "method": DELETE}
                                host_requests.append(host_request)
                                continue

                            security_name = want.get('community')
                            user_name = None
                            security_level = None
                            if 'user' in want:
                                user_name = want.get('user').get('name')
                                security_level = want.get('user').get('security_level')
                            name = want.get('name')
                            host_target_params_url = "data/ietf-snmp:snmp/target-params={0}".format(matched_host['name'])

                            if security_name:
                                host_tp_url = host_target_params_url + '/v2c/security-name'
                                host_request = {"path": host_tp_url, "method": DELETE}
                                host_requests.append(host_request)
                            elif user_name and security_level:
                                host_tp_url = host_target_params_url + '/usm'
                                host_request = {"path": host_tp_url, "method": DELETE}
                                host_requests.append(host_request)
                            elif user_name:
                                host_tp_url = host_target_params_url + '/usm/user-name'
                                host_request = {"path": host_tp_url, "method": DELETE}
                                host_requests.append(host_request)
                            elif security_level:
                                host_tp_url = host_target_params_url + '/usm/security-level'
                                host_request = {"path": host_tp_url, "method": DELETE}
                                host_requests.append(host_request)

                    if configs['host'] == []:
                        host_target_url = "data/ietf-snmp:snmp/target"
                        host_request = {"path": host_target_url, "method": DELETE}
                        host_requests.append(host_request)
                        host_target_params_url = "data/ietf-snmp:snmp/target-params"
                        host_request = {"path": host_target_params_url, "method": DELETE}
                        host_requests.append(host_request)
                if host_requests:
                    host_requests_list.extend(host_requests)

        if have_location and (delete_all or location):
            location_url = "data/ietf-snmp:snmp/ietf-snmp-ext:system/location"
            location_request = {"path": location_url, "method": DELETE}
            location_requests_list.append(location_request)

        if delete_all or user:
            if have_user is not None:
                user_requests = []
                if delete_all or self.check_dicts_matched(have_user, configs['user']):
                    user_url = "data/ietf-snmp:snmp/usm/local/user"
                    user_request = {"path": user_url, "method": DELETE}
                    user_requests.append(user_request)
                else:
                    have_user = have.get('user')
                    user_requests = []
                    for want in configs['user']:
                        matched_user = next((each_snmp for each_snmp in have_user if each_snmp['name'] == want['name']), None)
                        if matched_user:
                            user_name = want['name']
                            user_url = "data/ietf-snmp:snmp/usm/local/user={0}".format(user_name)
                            if len(want) == 1 or len(want) == len(matched_user):
                                user_request = {"path": user_url, "method": DELETE}
                                user_requests.append(user_request)
                            else:
                                auth = None
                                priv = None
                                priv_key = None
                                auth_key = None
                                if auth and auth_key and priv and priv_key and encrypted:
                                    user_request = {"path": user_url, "method": DELETE}
                                    user_requests.append(user_request)
                                else:
                                    if want.get('auth') and 'auth_type' in want.get('auth'):
                                        auth = want.get('auth').get('auth_type')
                                    if want.get('priv') and 'priv_type' in want.get('priv'):
                                        priv = want.get('priv').get('priv_type')
                                    if want.get('auth') and 'key' in want.get('auth'):
                                        auth_key = want.get('auth').get('key')
                                    if want.get('priv') and 'key' in want.get('priv'):
                                        priv_key = want.get('priv').get('key')
                                    encrypted = want.get('encrypted')
                                    if auth and auth_key or auth:
                                        if auth == 'sha2-256':
                                            auth = 'ietf-snmp-ext:sha2-256'
                                        elif auth == 'sha2-384':
                                            auth = 'ietf-snmp-ext:sha2-384'
                                        elif auth == 'sha2-512':
                                            auth = 'ietf-snmp-ext:sha2-512'
                                        auth_url = "{0}/auth/{1}".format(user_url, auth)
                                        user_request = {"path": auth_url, "method": DELETE}
                                        user_requests.append(user_request)
                                    if priv and priv_key or priv:
                                        priv_url = "{0}/priv/{1}".format(user_url, priv)
                                        user_request = {"path": priv_url, "method": DELETE}
                                        user_requests.append(user_request)
                                    if encrypted:
                                        encrypted_url = user_url + "/ietf-snmp-ext:encrypted"
                                        user_request = {"path": encrypted_url, "method": DELETE}
                                        user_requests.append(user_request)

                                group_name = want.get('group')
                                if group_name and have_group:
                                    group_url = "data/ietf-snmp:snmp/vacm/group={0}/member={1}".format(group_name, user_name)
                                    group_request = {"path": group_url, "method": DELETE}
                                    user_requests.append(group_request)

                if user_requests:
                    user_requests_list.extend(user_requests)

        if delete_all or view:
            if have_view is not None:
                view_requests = []
                if delete_all or self.check_dicts_matched(have_view, configs['view']):
                    view_url = "data/ietf-snmp:snmp/vacm/view"
                    view_request = {"path": view_url, "method": DELETE}
                    view_requests.append(view_request)
                else:
                    for want in configs['view']:
                        matched_view = next((each_snmp for each_snmp in have_view if each_snmp['name'] == want['name']), None)
                        if matched_view:
                            view_name = matched_view['name']
                            view_url = "data/ietf-snmp:snmp/vacm/view={0}".format(view_name)
                            # If only the view name is specified, delete this view.
                            if len(want) == 1:
                                view_request = {"path": view_url, "method": DELETE}
                                view_requests.append(view_request)
                                continue
                            include = want.get('included')
                            exclude = want.get('excluded')
                            if include:
                                if len(include) == 0 or len(include) == len(matched_view['included']):
                                    include_url = view_url + "/include"
                                    view_request = {"path": include_url, "method": DELETE}
                                    view_requests.append(view_request)
                                else:
                                    for include_view in include:
                                        include_view_url = view_url + "/include={0}".format(include_view)
                                        view_request = {"path": include_view_url, "method": DELETE}
                                        view_requests.append(view_request)
                            if exclude:
                                if len(exclude) == 0 or len(exclude) == len(matched_view['excluded']):
                                    exclude_url = view_url + "/exclude"
                                    view_request = {"path": exclude_url, "method": DELETE}
                                    view_requests.append(view_request)
                                else:
                                    for exclude_view in exclude:
                                        exclude_view_url = view_url + "/exclude={0}".format(exclude_view)
                                        view_request = {"path": exclude_view_url, "method": DELETE}
                                        view_requests.append(view_request)

                if view_requests:
                    view_requests_list.extend(view_requests)

        if agentaddress_requests_list:
            requests.extend(agentaddress_requests_list)
        if community_requests_list:
            requests.extend(community_requests_list)
        if contact_requests_list:
            requests.extend(contact_requests_list)
        if enable_trap_requests_list:
            requests.extend(enable_trap_requests_list)
        if engine_requests_list:
            requests.extend(engine_requests_list)
        if group_requests_list:
            requests.extend(group_requests_list)
        if host_requests_list:
            requests.extend(host_requests_list)
        if location_requests_list:
            requests.extend(location_requests_list)
        if user_requests_list:
            requests.extend(user_requests_list)
        if view_requests_list:
            requests.extend(view_requests_list)

        return requests

    def check_dicts_matched(self, have_list, config_list):
        """ Checks if all dicts in config_list are in have_list
        rtype: boolean
        returns: True if all dicts in config_list are in have_list
        """
        for option in have_list:
            for config in config_list:
                if isinstance(option, dict) and isinstance(config, dict) and not self.same_options(option, config):
                    return False
                if isinstance(option, str) and isinstance(config, str) and option != config:
                    return False
        return True

    def get_matched_access(self, access_list, want_access):
        """ Finds and returns the access list that matches the wanted access list
        :rtype: A list
        :returns: the access list that matches the wanted access list
        """
        matched_access = []
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
        if 'host' in have:
            for each_host in have.get('host'):
                if each_host['ip'] == want['ip']:
                    return each_host
        return {}

    def get_agententry(self, have_agentaddress):
        """ Get and return the first available agentEntry that is not already taken
        :rtype: str
        :returns: the first available agentEntry that is not already taken
        """
        agent = 1
        current_agententry = "AgentEntry1"
        while current_agententry in have_agentaddress:
            agent = agent + 1
            current_agententry = "AgentEntry" + str(agent)
        have_agentaddress.append(current_agententry)

        return current_agententry

    def get_targetentry(self, have_targetentry):
        """ Get and return the first available targetEntry that is not already taken
        :rtype: str
        :returns: the first available targetEntry that is not already taken
        """
        target = 1
        current_targetentry = "TargetEntry1"
        while current_targetentry in have_targetentry:
            target = target + 1
            current_targetentry = "TargetEntry" + str(target)
        have_targetentry.append(current_targetentry)
        return current_targetentry
