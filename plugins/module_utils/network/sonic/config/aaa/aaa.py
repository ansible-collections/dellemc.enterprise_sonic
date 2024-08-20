#
# -*- coding: utf-8 -*-
# Copyright 2024 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_aaa class
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
    remove_empties,
    update_states
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    edit_config,
    to_request
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.formatted_diff_utils import (
    get_new_config,
    get_formatted_config_diff
)

AAA_AUTHENTICATION_PATH = '/data/openconfig-system:system/aaa/authentication/config'
AAA_AUTHORIZATION_PATH = '/data/openconfig-system:system/aaa/authorization'
AAA_NAME_SERVICE_PATH = '/data/openconfig-system:system/aaa/openconfig-aaa-ext:name-service/config'
PATCH = 'patch'
DELETE = 'delete'


class Aaa(ConfigBase):
    """
    The sonic_aaa class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'aaa',
    ]

    def __init__(self, module):
        super(Aaa, self).__init__(module)

    def get_aaa_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        aaa_facts = facts['ansible_network_resources'].get('aaa')
        if not aaa_facts:
            return {}
        return aaa_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = []
        commands = []

        existing_aaa_facts = self.get_aaa_facts()
        commands, requests = self.set_config(existing_aaa_facts)
        if commands and len(requests) > 0:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        changed_aaa_facts = self.get_aaa_facts()

        result['before'] = existing_aaa_facts
        if result['changed']:
            result['after'] = changed_aaa_facts

        new_config = changed_aaa_facts
        old_config = existing_aaa_facts
        if self._module.check_mode:
            result.pop('after', None)
            new_config = get_new_config(commands, existing_aaa_facts)
            self.post_process_generated_config(new_config)
            result['after(generated)'] = new_config
        if self._module._diff:
            result['diff'] = get_formatted_config_diff(old_config,
                                                       new_config,
                                                       self._module._verbosity)
        result['warnings'] = warnings
        return result

    def set_config(self, existing_aaa_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = remove_empties(self._module.params['config'])
        have = existing_aaa_facts
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
        diff = self.get_diff_aaa(want, have)

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
        requests = self.get_modify_aaa_requests(commands)

        if commands and len(requests) > 0:
            commands = update_states(commands, 'merged')
        else:
            commands = []

        return commands, requests

    def _state_replaced(self, want, have, diff):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = []
        mod_commands = []
        requests = []
        replaced_config = self.get_replaced_config(want, have)

        if replaced_config:
            is_delete_all = replaced_config == have
            del_requests = self.get_delete_aaa_requests(replaced_config, have, is_delete_all)
            requests.extend(del_requests)
            commands.extend(update_states(replaced_config, 'deleted'))
            mod_commands = want
        else:
            mod_commands = diff

        if mod_commands:
            mod_requests = self.get_modify_aaa_requests(mod_commands)
            if mod_requests:
                requests.extend(mod_requests)
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
        commands = []
        requests = []

        if have and have != want:
            is_delete_all = True
            del_requests = self.get_delete_aaa_requests(have, None, is_delete_all)
            requests.extend(del_requests)
            commands.extend(update_states(have, 'deleted'))
            have = []

        if not have and want:
            mod_commands = want
            mod_requests = self.get_modify_aaa_requests(mod_commands)

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

        if not want:
            commands = deepcopy(have)
            is_delete_all = True
        else:
            commands = deepcopy(want)

        requests = self.get_delete_aaa_requests(commands, have, is_delete_all)

        if commands and len(requests) > 0:
            commands = update_states(commands, 'deleted')
        else:
            commands = []

        return commands, requests

    def get_modify_aaa_requests(self, commands):
        requests = []

        if commands:
            # Authentication modification handling
            authentication = commands.get('authentication')
            if authentication:
                authentication_cfg_dict = {}
                auth_method = authentication.get('auth_method')
                console_auth_local = authentication.get('console_auth_local')
                failthrough = authentication.get('failthrough')

                if auth_method:
                    authentication_cfg_dict['authentication-method'] = auth_method
                if console_auth_local is not None:
                    authentication_cfg_dict['console-authentication-local'] = console_auth_local
                if failthrough is not None:
                    authentication_cfg_dict['failthrough'] = str(failthrough)
                if authentication_cfg_dict:
                    payload = {'openconfig-system:config': authentication_cfg_dict}
                    requests.append({'path': AAA_AUTHENTICATION_PATH, 'method': PATCH, 'data': payload})

            # Authorization modification handling
            authorization = commands.get('authorization')
            if authorization:
                authorization_dict = {}
                commands_auth_method = authorization.get('commands_auth_method')
                login_auth_method = authorization.get('login_auth_method')

                if commands_auth_method:
                    authorization_dict['openconfig-aaa-tacacsplus-ext:commands'] = {'config': {'authorization-method': commands_auth_method}}
                if login_auth_method:
                    authorization_dict['openconfig-aaa-ext:login'] = {'config': {'authorization-method': login_auth_method}}
                if authorization_dict:
                    payload = {'openconfig-system:authorization': authorization_dict}
                    requests.append({'path': AAA_AUTHORIZATION_PATH, 'method': PATCH, 'data': payload})

            # Name-service modification handling
            name_service = commands.get('name_service')
            if name_service:
                name_service_cfg_dict = {}
                group = name_service.get('group')
                netgroup = name_service.get('netgroup')
                passwd = name_service.get('passwd')
                shadow = name_service.get('shadow')
                sudoers = name_service.get('sudoers')

                if group:
                    name_service_cfg_dict['group-method'] = group
                if netgroup:
                    name_service_cfg_dict['netgroup-method'] = netgroup
                if passwd:
                    name_service_cfg_dict['passwd-method'] = passwd
                if shadow:
                    name_service_cfg_dict['shadow-method'] = shadow
                if sudoers:
                    name_service_cfg_dict['sudoers-method'] = sudoers
                if name_service_cfg_dict:
                    payload = {'openconfig-aaa-ext:config': name_service_cfg_dict}
                    requests.append({'path': AAA_NAME_SERVICE_PATH, 'method': PATCH, 'data': payload})

        return requests

    def get_delete_aaa_requests(self, commands, have, is_delete_all):
        requests = []

        if not commands:
            return requests

        if is_delete_all:
            requests.append(self.get_delete_request(AAA_AUTHENTICATION_PATH, None))
            requests.append(self.get_delete_request(AAA_AUTHORIZATION_PATH, None))
            requests.append(self.get_delete_request(AAA_NAME_SERVICE_PATH, None))
            return requests

        config_dict = {}
        # Authentication deletion handling
        authentication = commands.get('authentication')
        if authentication:
            auth_method = authentication.get('auth_method')
            console_auth_local = authentication.get('console_auth_local')
            failthrough = authentication.get('failthrough')

            cfg_authentication = have.get('authentication')
            if cfg_authentication:
                authentication_dict = {}
                cfg_auth_method = cfg_authentication.get('auth_method')
                cfg_console_auth_local = cfg_authentication.get('console_auth_local')
                cfg_failthrough = cfg_authentication.get('failthrough')

                # Current SONiC behavior doesn't support single list item deletion
                if auth_method and auth_method == cfg_auth_method:
                    requests.append(self.get_delete_request(AAA_AUTHENTICATION_PATH, 'authentication-method'))
                    authentication_dict['auth_method'] = auth_method
                if console_auth_local is not None and console_auth_local == cfg_console_auth_local:
                    requests.append(self.get_delete_request(AAA_AUTHENTICATION_PATH, 'console-authentication-local'))
                    authentication_dict['console_auth_local'] = console_auth_local
                if failthrough is not None and failthrough == cfg_failthrough:
                    requests.append(self.get_delete_request(AAA_AUTHENTICATION_PATH, 'failthrough'))
                    authentication_dict['failthrough'] = failthrough
                if authentication_dict:
                    config_dict['authentication'] = authentication_dict

        # Authorization deletion handling
        authorization = commands.get('authorization')
        if authorization:
            commands_auth_method = authorization.get('commands_auth_method')
            login_auth_method = authorization.get('login_auth_method')

            cfg_authorization = have.get('authorization')
            if cfg_authorization:
                authorization_dict = {}
                cfg_commands_auth_method = cfg_authorization.get('commands_auth_method')
                cfg_login_auth_method = cfg_authorization.get('login_auth_method')

                # Current SONiC behavior doesn't support single list item deletion
                if commands_auth_method and commands_auth_method == cfg_commands_auth_method:
                    requests.append(self.get_delete_request(AAA_AUTHORIZATION_PATH,
                                                            'openconfig-aaa-tacacsplus-ext:commands/config/authorization-method'))
                    authorization_dict['commands_auth_method'] = commands_auth_method
                if login_auth_method and login_auth_method == cfg_login_auth_method:
                    requests.append(self.get_delete_request(AAA_AUTHORIZATION_PATH, 'openconfig-aaa-ext:login/config/authorization-method'))
                    authorization_dict['login_auth_method'] = login_auth_method
                if authorization_dict:
                    config_dict['authorization'] = authorization_dict

        # Name-service deletion handling
        name_service = commands.get('name_service')
        if name_service:
            group = name_service.get('group')
            netgroup = name_service.get('netgroup')
            passwd = name_service.get('passwd')
            shadow = name_service.get('shadow')
            sudoers = name_service.get('sudoers')

            cfg_name_service = have.get('name_service')
            if cfg_name_service:
                name_service_dict = {}
                cfg_group = cfg_name_service.get('group')
                cfg_netgroup = cfg_name_service.get('netgroup')
                cfg_passwd = cfg_name_service.get('passwd')
                cfg_shadow = cfg_name_service.get('shadow')
                cfg_sudoers = cfg_name_service.get('sudoers')

                # Current SONiC behavior doesn't support single list item deletion
                if group and group == cfg_group:
                    requests.append(self.get_delete_request(AAA_NAME_SERVICE_PATH, 'group-method'))
                    name_service_dict['group'] = group
                if netgroup and netgroup == cfg_netgroup:
                    requests.append(self.get_delete_request(AAA_NAME_SERVICE_PATH, 'netgroup-method'))
                    name_service_dict['netgroup'] = netgroup
                if passwd and passwd == cfg_passwd:
                    requests.append(self.get_delete_request(AAA_NAME_SERVICE_PATH, 'passwd-method'))
                    name_service_dict['passwd'] = passwd
                if shadow and shadow == cfg_shadow:
                    requests.append(self.get_delete_request(AAA_NAME_SERVICE_PATH, 'shadow-method'))
                    name_service_dict['shadow'] = shadow
                if sudoers and sudoers == cfg_sudoers:
                    requests.append(self.get_delete_request(AAA_NAME_SERVICE_PATH, 'sudoers-method'))
                    name_service_dict['sudoers'] = sudoers
                if name_service_dict:
                    config_dict['name_service'] = name_service_dict
        commands = config_dict

        return requests

    def get_delete_request(self, url, attr):
        if attr:
            url += '/%s' % (attr)
        request = {'path': url, 'method': DELETE}
        return request

    def get_diff_aaa(self, want, have):
        """AAA module requires custom diff method due to overwritting of list in SONiC"""
        if not have:
            return want

        cfg_dict = {}
        # Authentication diff handling
        authentication = want.get('authentication')
        if authentication:
            auth_method = authentication.get('auth_method')
            console_auth_local = authentication.get('console_auth_local')
            failthrough = authentication.get('failthrough')

            cfg_authentication = have.get('authentication')
            if cfg_authentication:
                authentication_dict = {}
                cfg_auth_method = cfg_authentication.get('auth_method')
                cfg_console_auth_local = cfg_authentication.get('console_auth_local')
                cfg_failthrough = cfg_authentication.get('failthrough')

                if auth_method and auth_method != cfg_auth_method:
                    authentication_dict['auth_method'] = auth_method
                if console_auth_local is not None and console_auth_local != cfg_console_auth_local:
                    authentication_dict['console_auth_local'] = console_auth_local
                if failthrough is not None and failthrough != cfg_failthrough:
                    authentication_dict['failthrough'] = failthrough
                if authentication_dict:
                    cfg_dict['authentication'] = authentication_dict
            else:
                cfg_dict['authentication'] = authentication

        # Authorization diff handling
        authorization = want.get('authorization')
        if authorization:
            commands_auth_method = authorization.get('commands_auth_method')
            login_auth_method = authorization.get('login_auth_method')

            cfg_authorization = have.get('authorization')
            if cfg_authorization:
                authorization_dict = {}
                cfg_commands_auth_method = cfg_authorization.get('commands_auth_method')
                cfg_login_auth_method = cfg_authorization.get('login_auth_method')

                if commands_auth_method and commands_auth_method != cfg_commands_auth_method:
                    authorization_dict['commands_auth_method'] = commands_auth_method
                if login_auth_method and login_auth_method != cfg_login_auth_method:
                    authorization_dict['login_auth_method'] = login_auth_method
                if authorization_dict:
                    cfg_dict['authorization'] = authorization_dict
            else:
                cfg_dict['authorization'] = authorization

        # Name-service diff handling
        name_service = want.get('name_service')
        if name_service:
            group = name_service.get('group')
            netgroup = name_service.get('netgroup')
            passwd = name_service.get('passwd')
            shadow = name_service.get('shadow')
            sudoers = name_service.get('sudoers')

            cfg_name_service = have.get('name_service')
            if cfg_name_service:
                name_service_dict = {}
                cfg_group = cfg_name_service.get('group')
                cfg_netgroup = cfg_name_service.get('netgroup')
                cfg_passwd = cfg_name_service.get('passwd')
                cfg_shadow = cfg_name_service.get('shadow')
                cfg_sudoers = cfg_name_service.get('sudoers')

                if group and group != cfg_group:
                    name_service_dict['group'] = group
                if netgroup and netgroup != cfg_netgroup:
                    name_service_dict['netgroup'] = netgroup
                if passwd and passwd != cfg_passwd:
                    name_service_dict['passwd'] = passwd
                if shadow and shadow != cfg_shadow:
                    name_service_dict['shadow'] = shadow
                if sudoers and sudoers != cfg_sudoers:
                    name_service_dict['sudoers'] = sudoers
                if name_service_dict:
                    cfg_dict['name_service'] = name_service_dict
            else:
                cfg_dict['name_service'] = name_service

        return cfg_dict

    def get_replaced_config(self, want, have):
        config_dict = {}
        authentication = want.get('authentication')
        authorization = want.get('authorization')
        name_service = want.get('name_service')
        cfg_authentication = have.get('authentication')
        cfg_authorization = have.get('authorization')
        cfg_name_service = have.get('name_service')

        if authentication and cfg_authentication and authentication != cfg_authentication:
            config_dict['authentication'] = cfg_authentication
        if authorization and cfg_authorization and authorization != cfg_authorization:
            config_dict['authorization'] = cfg_authorization
        if name_service and cfg_name_service and name_service != cfg_name_service:
            config_dict['name_service'] = cfg_name_service

        return config_dict

    def post_process_generated_config(self, data):
        if data:
            authentication = data.get('authentication')
            authorization = data.get('authorization')
            name_service = data.get('name_service')

            if authentication:
                if 'auth_method' in authentication and not authentication['auth_method']:
                    data['authentication'].pop('auth_method')
                if not data['authentication']:
                    data.pop('authentication')
            if authorization:
                if 'commands_auth_method' in authorization and not authorization['commands_auth_method']:
                    data['authorization'].pop('commands_auth_method')
                if 'login_auth_method' in authorization and not authorization['login_auth_method']:
                    data['authorization'].pop('login_auth_method')
                if not data['authorization']:
                    data.pop('authorization')
            if name_service:
                for method in ('group', 'netgroup', 'passwd', 'shadow', 'sudoers'):
                    if method in name_service and not name_service[method]:
                        data['name_service'].pop(method)
                    if not data['name_service']:
                        data.pop('name_service')
