#
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_mfa class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from copy import deepcopy

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
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
    remove_empties_from_list
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.formatted_diff_utils import (
    __DELETE_CONFIG_IF_NO_SUBCONFIG,
    __DELETE_LEAFS_OR_CONFIG_IF_NO_NON_KEY_LEAF,
    get_new_config,
    get_formatted_config_diff
)
from ansible.module_utils.connection import ConnectionError

PATCH = 'patch'
DELETE = 'delete'

mfa_global_std_paths = {
    'key_seed': 'key-seed',
    'security_profile': 'mfa-security-profile',
    'client_secret': 'client-secret',
}

cac_piv_global_std_paths = {
    'cert_username_field': 'cert-username-field',
    'cert_username_match': 'cert-username-match',
    'security_profile': 'cacpiv-security-profile',
}

MFA_DEFAULTS = {
    'mfa_global': {
        'key_seed_encrypted': True,
        'client_secret_encrypted': True
    },
    'rsa_servers': {
        'client_key_encrypted': True,
        'server_port': 5555,
        'connection_timeout': 20,
        'read_timeout': 120
    },
    'cac_piv_global': {
        'cert_username_field': 'common-name-or-user-principal-name',
        'cert_username_match': 'username-as-is'
    }
}

TEST_KEYS = [
    {'rsa_servers': {'hostname': ''}}
]

TEST_KEYS_formatted_diff = [
    {'config': {'__delete_op': __DELETE_LEAFS_OR_CONFIG_IF_NO_NON_KEY_LEAF}},
    {'rsa_servers': {'hostname': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}},
]

MFA_PATH = 'data/openconfig-mfa:mfa'


class Mfa(ConfigBase):
    """
    The sonic_mfa class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'mfa',
    ]

    def __init__(self, module):
        super(Mfa, self).__init__(module)

    def get_mfa_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        mfa_facts = facts['ansible_network_resources'].get('mfa')
        if not mfa_facts:
            return []
        return mfa_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = []
        commands = []

        existing_mfa_facts = self.get_mfa_facts()
        commands, requests = self.set_config(existing_mfa_facts)
        if commands and len(requests) > 0:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        result['before'] = existing_mfa_facts
        old_config = existing_mfa_facts

        if self._module.check_mode:
            new_commands = deepcopy(commands)
            new_config = get_new_config(new_commands, old_config, TEST_KEYS_formatted_diff)
            result['after(generated)'] = self._post_process_generated_output(new_config)
        else:
            new_config = self.get_mfa_facts()
            if result['changed']:
                result['after'] = new_config

        if self._module._diff:
            self.sort_lists_in_config(old_config)
            self.sort_lists_in_config(new_config)
            result['diff'] = get_formatted_config_diff(old_config, new_config, self._module._verbosity)

        result['warnings'] = warnings
        return result

    def set_config(self, existing_mfa_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']
        if want:
            want = remove_empties(want)
        have = existing_mfa_facts
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
        want = self.validate_want(want, have, state)

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
        commands, mod_commands, requests = [], [], []

        replaced_config, requests = self.get_replaced_config(want, have)
        if replaced_config:
            commands.extend(update_states(replaced_config, "deleted"))
            mod_commands = want
        else:
            diff = get_diff(want, have, TEST_KEYS)
            mod_commands = diff

        if mod_commands:
            mod_requests = self.get_modify_mfa_requests(mod_commands, have)
            if len(mod_requests) > 0:
                requests.extend(mod_requests)
                commands.extend(update_states(mod_commands, "replaced"))

        return commands, requests

    def _state_overridden(self, want, have):
        """ The command generator when state is overridden

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands, requests = [], []

        del_commands = get_diff(have, want, TEST_KEYS)
        self.remove_default_entries(del_commands)

        if del_commands:
            is_delete_all = True
            have, del_requests = self.get_delete_mfa_requests(want, have, is_delete_all)
            requests.extend(del_requests)
            commands.extend(update_states(have, "deleted"))
            have = {}

        diff = get_diff(want, have, TEST_KEYS)
        if diff:
            mod_commands = diff
            mod_requests = self.get_modify_mfa_requests(mod_commands, have)

            if len(mod_requests) > 0:
                requests.extend(mod_requests)
                commands.extend(update_states(mod_commands, "overridden"))

        return commands, requests

    def _state_merged(self, want, have):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands, requests = [], []

        commands = get_diff(want, have, TEST_KEYS)
        # Prevent diff from removing user-set encrypted True
        if have:
            mfa_global_have = have.get('mfa_global', {})
            mfa_global_want = want.get('mfa_global', {})
            if commands and mfa_global_have and mfa_global_want:
                for key in ['key_seed_encrypted', 'client_secret_encrypted']:
                    if key in mfa_global_have and mfa_global_want.get(key):
                        commands['mfa_global'].update({key: True})

            rsa_servers_have = have.get('rsa_servers', {})
            rsa_servers_want = want.get('rsa_servers', {})
            if commands and rsa_servers_have and rsa_servers_want:
                if 'client_key_encrypted' in rsa_servers_have and rsa_servers_want.get('client_key_encrypted'):
                    commands['rsa_servers'].update({'client_key_encrypted': True})

        requests = self.get_modify_mfa_requests(commands, have)
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
        commands, requests = [], []
        is_delete_all = False

        if not have:
            return commands, requests
        elif not want:
            new_have = deepcopy(have)
            new_want = want
            is_delete_all = True
            if new_have:
                self.remove_default_entries(new_have)
        else:
            new_have = deepcopy(have)
            new_want = deepcopy(want)
            self.remove_default_entries(new_want)
            self.remove_default_entries(new_have)

        commands, requests = self.get_delete_mfa_requests(new_want, new_have, is_delete_all)

        if commands and len(requests) > 0:
            commands = update_states(commands, "deleted")
        else:
            commands = []

        return commands, requests

    def validate_want(self, want, have, state):
        if state != "deleted":
            mfa_global = want.get('mfa_global')
            if mfa_global:
                required_pairs = [('key_seed_encrypted', 'key_seed'), ('client_secret_encrypted', 'client_secret')]
                for encrypted, plain in required_pairs:
                    if encrypted in mfa_global and plain not in mfa_global:
                        self._module.fail_json(msg=f"For {state}, '{plain}' and '{encrypted}' are required together.")
            if 'rsa_servers' not in have:
                rsa_servers = want.get('rsa_servers')
                if rsa_servers:
                    for server in rsa_servers:
                        required_fields = ['hostname', 'client_id', 'client_key']
                        if not all(server.get(field) for field in required_fields):
                            self._module.fail_json(msg=f"For new hosts, 'hostname', 'client_id', and 'client_key' are required together in {state}")
        return want

    def get_modify_mfa_requests(self, commands, have):
        """Get requests to modify MFA configurations"""
        requests = []

        if not commands:
            return requests

        mfa_global_request = self.get_modify_mfa_global_request(commands)
        rsa_global_request = self.get_modify_rsa_global_request(commands)
        rsa_servers_request = self.get_modify_rsa_servers_request(commands)
        cac_piv_global_request = self.get_modify_cac_piv_global_request(commands, have)
        requests.extend(filter(None, [mfa_global_request, rsa_global_request, cac_piv_global_request]))
        requests.extend(rsa_servers_request)

        return requests

    def get_modify_mfa_global_request(self, commands):
        """Get request to modify MFA Global configurations"""
        request = None

        mfa_global = commands.get('mfa_global')
        if mfa_global:
            config_dict = {}
            for key, value in mfa_global.items():
                if value is not None:
                    if key == 'security_profile':
                        config_dict['mfa-security-profile'] = value
                        continue
                    config_key = key.replace('_', '-')
                    config_dict[config_key] = value
            if config_dict:
                payload = {'openconfig-mfa:mfa-global': {'config': config_dict}}
                request = {'path': f"{MFA_PATH}/mfa-global", 'method': PATCH, 'data': payload}
        return request

    def get_modify_rsa_global_request(self, commands):
        """Get request to modify RSA Global configuration"""
        request = None

        rsa_global = commands.get('rsa_global')
        if rsa_global and (security_profile := rsa_global.get('security_profile')):
            payload = {'openconfig-mfa:rsa-global': {'config': {'rsa-security-profile': security_profile}}}
            request = {'path': f"{MFA_PATH}/rsa-global", 'method': PATCH, 'data': payload}
        return request

    def get_modify_rsa_servers_request(self, commands):
        """Get request to modify RSA Server configurations"""

        requests = []

        rsa_servers = commands.get('rsa_servers')
        if rsa_servers:
            rsa_server_list = self.get_rsa_server_list(rsa_servers)
            for server in rsa_server_list:
                url = f"{MFA_PATH}/rsa-servers/rsa-server={server['hostname']}"
                payload = {'openconfig-mfa:rsa-server': [server]}
                requests.append({'path': url, 'method': PATCH, 'data': payload})

        return requests

    def get_rsa_server_list(self, data):
        rsa_server_list = []

        for server in data:
            rsa_server_dict = {}
            config_dict = {}
            hostname = None
            for key, value in server.items():
                if value is not None:
                    if key == 'hostname':
                        config_dict['hostname'] = value
                        hostname = value
                        continue
                    elif key == 'server_port':
                        config_dict['port-number'] = value
                        continue
                    else:
                        config_key = key.replace('_', '-')
                        default_val = MFA_DEFAULTS['rsa_servers'].get(key)
                        if key != 'client_key_encrypted' and default_val is not None and value == default_val:
                            continue
                        config_dict[config_key] = value
            if config_dict:
                rsa_server_dict['hostname'] = hostname
                rsa_server_dict['config'] = config_dict
                rsa_server_list.append(rsa_server_dict)
        return rsa_server_list

    def get_modify_cac_piv_global_request(self, commands, have):
        """Get request to modify CAC-PIV Global configurations"""
        request = None

        cac_piv_global = commands.get('cac_piv_global')
        if cac_piv_global:
            config_dict = {}
            for key, value in cac_piv_global.items():
                if value is not None:
                    if key == 'security_profile':
                        config_dict['cacpiv-security-profile'] = value
                        continue
                    elif key in ['cert_username_field', 'cert_username_match']:
                        config_key = key.replace('_', '-')
                        if value != MFA_DEFAULTS['cac_piv_global'].get(key) or not have:
                            config_dict[config_key] = value
            if config_dict:
                payload = {'openconfig-mfa:cac-piv-global': {'config': config_dict}}
                request = {'path': f"{MFA_PATH}/cac-piv-global", 'method': PATCH, 'data': payload}
        return request

    def get_delete_mfa_requests(self, want, have, is_delete_all=False):
        """Get requests to delete MFA configurations"""
        commands, requests = [], []

        if not have:
            return commands, requests

        if is_delete_all:
            commands = have
            requests.extend(self.get_delete_all_mfa_global_requests(commands))
            requests.extend(self.get_delete_all_rsa_global_requests(commands))
            requests.extend(self.get_delete_all_rsa_servers_requests(commands))
            requests.extend(self.get_delete_all_cac_piv_global_requests(commands))
            return commands, requests

        cmd, requests_mfa_global_del, requests_rsa_global_del, requests_rsa_servers_del, requests_cac_piv_global_del = {}, [], [], [], []

        mfa_global = want.get('mfa_global')
        rsa_global = want.get('rsa_global')
        rsa_servers = want.get('rsa_servers')
        cac_piv_global = want.get('cac_piv_global')

        have_conf = have
        if have_conf:
            if have_conf.get('mfa_global') and mfa_global:
                commands_del = []
                commands_del, requests_mfa_global_del = self.get_delete_mfa_global_requests(mfa_global, have_conf['mfa_global'])
                if commands_del and len(requests_mfa_global_del) > 0:
                    cmd['mfa_global'] = commands_del

            if have_conf.get('rsa_global') and rsa_global:
                commands_del = []
                commands_del, requests_rsa_global_del = self.get_delete_rsa_global_requests(rsa_global, have_conf['rsa_global'])
                if commands_del and len(requests_rsa_global_del) > 0:
                    cmd['rsa_global'] = commands_del

            if have_conf.get('rsa_servers') and rsa_servers:
                commands_del = []
                commands_del, requests_rsa_servers_del = self.get_delete_rsa_servers_requests(rsa_servers, have_conf['rsa_servers'])
                if commands_del and len(requests_rsa_servers_del) > 0:
                    cmd['rsa_servers'] = commands_del

            if have_conf.get('cac_piv_global') and cac_piv_global:
                commands_del = []
                commands_del, requests_cac_piv_global_del = self.get_delete_cac_piv_global_requests(cac_piv_global, have_conf['cac_piv_global'])
                if commands_del and len(requests_cac_piv_global_del) > 0:
                    cmd['cac_piv_global'] = commands_del

            if cmd:
                commands.append(cmd)
                requests.extend(requests_mfa_global_del)
                requests.extend(requests_rsa_global_del)
                requests.extend(requests_rsa_servers_del)
                requests.extend(requests_cac_piv_global_del)

        return commands, requests

    def get_delete_all_mfa_global_requests(self, commands):
        """Get requests to delete all MFA Global configurations"""
        requests = []

        mfa_global = commands.get('mfa_global')
        if mfa_global:
            for mfa_global_option in mfa_global_std_paths:
                if mfa_global.get(mfa_global_option):
                    requests.append(self.get_delete_attr_request(mfa_global_std_paths[mfa_global_option], 'mfa-global'))
        return requests

    def get_delete_all_rsa_global_requests(self, commands):
        """Get request to delete all RSA Global configuration"""
        requests = []

        if commands.get('rsa_global'):
            request = {'path': f"{MFA_PATH}/rsa-global", 'method': DELETE}
            requests.append(request)
        return requests

    def get_delete_all_rsa_servers_requests(self, commands):
        """Get request to delete all RSA Server configurations"""
        requests = []

        rsa_servers = commands.get('rsa_servers', [])
        for rsa_server in rsa_servers:
            requests.append(self.get_delete_attr_request(rsa_server['hostname'], 'rsa-servers'))
        return requests

    def get_delete_all_cac_piv_global_requests(self, commands):
        """Get request to delete all CAC-PIV Global configurations"""
        requests = []

        if commands.get('cac_piv_global'):
            request = {'path': f"{MFA_PATH}/cac-piv-global", 'method': DELETE}
            requests.append(request)
        return requests

    def get_delete_mfa_global_requests(self, want_mfa_global, have_mfa_global):
        """Get requests to delete specific MFA Global configurations"""
        commands, requests = {}, []

        for mfa_global_option in mfa_global_std_paths:
            if mfa_global_option in want_mfa_global:
                if (want_mfa_global.get(mfa_global_option) and want_mfa_global.get(mfa_global_option) == have_mfa_global.get(mfa_global_option)):
                    commands[mfa_global_option] = have_mfa_global.get(mfa_global_option)
                    requests.append(self.get_delete_attr_request(mfa_global_std_paths[mfa_global_option], 'mfa-global'))
                else:
                    want_mfa_global.pop(mfa_global_option)
        return commands, requests

    def get_delete_rsa_global_requests(self, want_rsa_global, have_rsa_global):
        """Get request to delete specific RSA Global configuration"""
        commands, requests = [], []

        security_profile = want_rsa_global.get('security_profile')
        if security_profile and security_profile == have_rsa_global.get('security_profile'):
            commands.append({'security_profile': have_rsa_global.get('security_profile')})
            requests.append(self.get_delete_attr_request('rsa-security-profile', 'rsa-global'))
        return commands, requests

    def get_delete_rsa_servers_requests(self, want_rsa_servers, have_rsa_servers):
        """Get requests to delete specific RSA server configurations"""
        commands, requests = [], []

        want_rsa_servers = remove_empties_from_list(want_rsa_servers)
        if want_rsa_servers and have_rsa_servers:
            for rsa_server in want_rsa_servers:
                matching_rsa_server = next((rs for rs in have_rsa_servers if rs.get("hostname") == rsa_server.get("hostname")), None)
                if matching_rsa_server:
                    cmd = {}
                    for attr in ["connection_timeout", "read_timeout", "server_port"]:
                        if rsa_server.get(attr) and rsa_server.get(attr) == matching_rsa_server.get(attr):
                            cmd[attr] = matching_rsa_server.get(attr)
                            if attr == "server_port":
                                requests.append(self.get_delete_attr_request(rsa_server["hostname"], 'rsa-servers', 'port-number'))
                            else:
                                requests.append(self.get_delete_attr_request(rsa_server["hostname"], 'rsa-servers', attr.replace('_', '-')))
                    if cmd:
                        cmd["hostname"] = matching_rsa_server.get("hostname")
                        commands.append(cmd)
                    if len(rsa_server) == 1 and "hostname" in rsa_server:
                        cmd["hostname"] = matching_rsa_server.get("hostname")
                        commands.append(cmd)
                        requests.append(self.get_delete_attr_request(rsa_server["hostname"], 'rsa-servers'))
        return commands, requests

    def get_delete_cac_piv_global_requests(self, want_cac_piv_global, have_cac_piv_global):
        """Get requests to delete specific CAC-PIV Global configurations"""
        commands, requests = {}, []

        for cac_piv_global_option in cac_piv_global_std_paths:
            if cac_piv_global_option in want_cac_piv_global:
                want_value = want_cac_piv_global.get(cac_piv_global_option)
                have_value = have_cac_piv_global.get(cac_piv_global_option)
                if want_value and want_value == have_value:
                    commands[cac_piv_global_option] = have_cac_piv_global.get(cac_piv_global_option)
                    requests.append(self.get_delete_attr_request(cac_piv_global_std_paths[cac_piv_global_option], 'cac-piv-global'))
                else:
                    want_cac_piv_global.pop(cac_piv_global_option)
        return commands, requests

    def get_delete_attr_request(self, attr, module, sub_attr=''):
        if module == 'rsa-servers':
            url = f"{MFA_PATH}/{module}/rsa-server={attr}"
            if sub_attr:
                url = url + f"/config/{sub_attr}"
        else:
            url = f"{MFA_PATH}/{module}/config/{attr}"
        return {'path': url, 'method': DELETE}

    def remove_default_entries(self, data):
        for section, defaults in MFA_DEFAULTS.items():
            if section in data:
                if section == 'rsa_servers':
                    for rsa_server in data[section]:
                        for key, default_val in defaults.items():
                            if rsa_server.get(key) == default_val:
                                rsa_server.pop(key)
                    if not any(data[section]):
                        data.pop(section)
                else:
                    for key, default_val in defaults.items():
                        if data[section].get(key) == default_val:
                            data[section].pop(key)
                    if not data[section]:
                        data.pop(section)

    def get_replaced_config(self, want, have):
        config_dict = {}
        requests = []

        if not have:
            return config_dict, requests

        rsa_servers = want.get('rsa_servers')
        cfg_rsa_servers = have.get('rsa_servers')

        if rsa_servers and cfg_rsa_servers:
            rsa_servers_list, rsa_servers_requests = self.get_replaced_rsa_servers_list(rsa_servers, cfg_rsa_servers)
            if rsa_servers_list:
                config_dict['rsa_servers'] = rsa_servers_list
                requests.extend(rsa_servers_requests)

        return config_dict, requests

    def get_replaced_rsa_servers_list(self, want_data, have_data):
        rsa_servers_list = []
        requests = []

        for rsa_server in want_data:
            hostname = rsa_server.get('hostname')
            server_port = rsa_server.get('server_port')
            connection_timeout = rsa_server.get('connection_timeout')
            read_timeout = rsa_server.get('read_timeout')

            for cfg_rsa_server in have_data:
                cfg_hostname = cfg_rsa_server.get('hostname')
                cfg_server_port = cfg_rsa_server.get('server_port')
                cfg_connection_timeout = cfg_rsa_server.get('connection_timeout')
                cfg_read_timeout = cfg_rsa_server.get('read_timeout')

                if hostname == cfg_hostname:
                    del_command = {}
                    if server_port and server_port != cfg_server_port:
                        del_command['server_port'] = cfg_server_port
                        requests.append(self.get_delete_attr_request(hostname, 'rsa-servers', 'port-number'))
                    if connection_timeout and connection_timeout != cfg_connection_timeout:
                        del_command['connection_timeout'] = cfg_connection_timeout
                        requests.append(self.get_delete_attr_request(hostname, 'rsa-servers', 'connection-timeout'))
                    if read_timeout and read_timeout != cfg_read_timeout:
                        del_command['read_timeout'] = cfg_read_timeout
                        requests.append(self.get_delete_attr_request(hostname, 'rsa-servers', 'read-timeout'))
                    if del_command:
                        rsa_servers_list.append(del_command)

        return rsa_servers_list, requests

    def sort_lists_in_config(self, config):
        if config:
            rsa_servers = config.get('rsa_servers', None)
            if rsa_servers:
                rsa_servers.sort(key=lambda x: x['hostname'])

    def _post_process_generated_output(self, config):
        if "mfa_global" in config:
            for key, default_val in MFA_DEFAULTS['mfa_global'].items():
                config["mfa_global"].setdefault(key, default_val)

        if "rsa_servers" in config:
            for server in config["rsa_servers"]:
                for key, default_val in MFA_DEFAULTS['rsa_servers'].items():
                    server.setdefault(key, default_val)
            if not config["rsa_servers"]:
                config.pop("rsa_servers")

        if "cac_piv_global" in config:
            for key, default_val in MFA_DEFAULTS['cac_piv_global'].items():
                config["cac_piv_global"].setdefault(key, default_val)

        return config
