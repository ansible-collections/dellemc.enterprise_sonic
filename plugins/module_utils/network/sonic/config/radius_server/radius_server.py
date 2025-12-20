#
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_radius_server class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
from copy import deepcopy

from ansible.module_utils.connection import ConnectionError
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import \
    ConfigBase
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import \
    to_list
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import \
    Facts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    edit_config, to_request
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.formatted_diff_utils import (
    get_formatted_config_diff,
    get_new_config
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    get_diff,
    normalize_interface_name,
    remove_empties,
    update_states
)

PATCH = 'patch'
DELETE = 'delete'
RADIUS_SERVER_PATH = 'data/openconfig-system:system/aaa/server-groups/server-group=RADIUS'
TEST_KEYS = [
    {'host': {'name': ''}},
]


class Radius_server(ConfigBase):
    """
    The sonic_radius_server class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'radius_server',
    ]

    def __init__(self, module):
        super(Radius_server, self).__init__(module)
        self._delete_all = False

    def get_radius_server_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        radius_server_facts = facts['ansible_network_resources'].get('radius_server')
        if not radius_server_facts:
            return {}
        return radius_server_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        existing_radius_server_facts = self.get_radius_server_facts()
        commands, requests = self.set_config(existing_radius_server_facts)
        if commands and requests:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True

        result['commands'] = commands
        result['before'] = existing_radius_server_facts
        old_config = existing_radius_server_facts

        if self._module.check_mode:
            new_config = self.get_new_config(commands, existing_radius_server_facts)
            result['after_generated'] = new_config
        else:
            new_config = self.get_radius_server_facts()
            if result['changed']:
                result['after'] = new_config
        if self._module._diff:
            self.sort_lists_in_config(new_config)
            self.sort_lists_in_config(old_config)
            result['diff'] = get_formatted_config_diff(old_config, new_config, self._module._verbosity)

        return result

    def set_config(self, existing_radius_server_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = remove_empties(self._module.params['config'])

        if want and want.get('servers') and want['servers'].get('host'):
            normalize_interface_name(want['servers']['host'], self._module, 'source_interface')

        have = existing_radius_server_facts
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
        commands, requests = [], []
        state = self._module.params['state']
        diff = get_diff(want, have, TEST_KEYS)

        if state == 'overridden':
            commands, requests = self._state_overridden(want, have, diff)
        elif state == 'deleted':
            commands, requests = self._state_deleted(want, have, diff)
        elif state == 'merged':
            commands, requests = self._state_merged(diff)
        elif state == 'replaced':
            commands, requests = self._state_replaced(want, have, diff)
        return commands, requests

    def _state_merged(self, diff):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = diff
        requests = self.get_modify_radius_server_requests(commands)

        if commands and requests:
            commands = update_states(commands, 'merged')
        else:
            commands = []

        return commands, requests

    def _state_deleted(self, want, have, diff):
        """ The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        delete_all = False
        commands, requests = [], []

        if not want:
            commands = deepcopy(have)
            delete_all = True
        else:
            commands = get_diff(want, diff, TEST_KEYS)
            self.remove_default_entries(commands)

        if commands:
            requests = self.get_delete_radius_server_requests(commands, delete_all)
            if requests:
                commands = update_states(commands, 'deleted')
        else:
            commands = []

        return commands, requests

    def _state_replaced(self, want, have, diff):
        """ The command generator when state is replaced

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands, mod_commands = [], []
        replaced_config, requests = self.get_replaced_config(want, have)

        if replaced_config:
            commands.extend(update_states(replaced_config, 'deleted'))
            mod_commands = want
        else:
            mod_commands = diff

        if mod_commands:
            mod_requests = self.get_modify_radius_server_requests(mod_commands)

            if mod_requests:
                requests.extend(mod_requests)
                commands.extend(update_states(mod_commands, 'replaced'))

        return commands, requests

    def _state_overridden(self, want, have, diff):
        """ The command generator when state is overridden

        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :param diff: the difference between want and have
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands, requests = [], []
        mod_commands, mod_requests = None, None
        del_commands = get_diff(have, want, TEST_KEYS)
        self.remove_default_entries(del_commands)

        if del_commands:
            del_requests = self.get_delete_radius_server_requests(have, True)
            requests.extend(del_requests)
            commands.extend(update_states(have, 'deleted'))
            have = []
            mod_commands = want
            mod_requests = self.get_modify_radius_server_requests(mod_commands)
        elif diff:
            mod_commands = diff
            mod_requests = self.get_modify_radius_server_requests(mod_commands)

        if mod_requests:
            requests.extend(mod_requests)
            commands.extend(update_states(mod_commands, 'overridden'))

        return commands, requests

    def get_radius_global_payload(self, conf):
        """This method returns the patch payload for the global configuration"""
        payload, global_cfg = {}, {}

        if conf.get('auth_type', None):
            global_cfg['auth-type'] = conf['auth_type']
        if conf.get('key', None):
            global_cfg['secret-key'] = conf['key']
        if conf.get('timeout', None):
            global_cfg['timeout'] = conf['timeout']

        if global_cfg:
            payload = {'openconfig-system:config': global_cfg}

        return payload

    def get_radius_global_ext_payload(self, conf):
        """This method returns the patch payload for the global ext configuration"""
        payload, global_ext_cfg = {}, {}

        if conf.get('nas_ip'):
            global_ext_cfg['nas-ip-address'] = conf['nas_ip']
        if conf.get('retransmit') is not None:
            global_ext_cfg['retransmit-attempts'] = conf['retransmit']
        if conf.get('statistics'):
            global_ext_cfg['statistics'] = conf['statistics']
        if global_ext_cfg:
            payload = {'openconfig-aaa-radius-ext:config': global_ext_cfg}

        return payload

    def get_radius_server_payload(self, hosts):
        """This method returns the patch payload for the servers configuration"""
        payload = {}
        servers_load = []

        for host in hosts:
            if host.get('name'):
                host_cfg = {'address': host['name']}
                if host.get('auth_type'):
                    host_cfg['auth-type'] = host['auth_type']
                if host.get('priority'):
                    host_cfg['priority'] = host['priority']
                if host.get('vrf'):
                    host_cfg['vrf'] = host['vrf']
                if host.get('timeout'):
                    host_cfg['timeout'] = host['timeout']

                radius_port_key_cfg = {}
                if host.get('port'):
                    radius_port_key_cfg['auth-port'] = host['port']
                if host.get('key'):
                    radius_port_key_cfg['secret-key'] = host['key']
                if host.get('retransmit') is not None:
                    radius_port_key_cfg['retransmit-attempts'] = host['retransmit']
                if host.get('source_interface'):
                    radius_port_key_cfg['openconfig-aaa-radius-ext:source-interface'] = host['source_interface']
                if host.get('protocol'):
                    radius_port_key_cfg['protocol'] = host['protocol']
                if host.get('security_profile'):
                    radius_port_key_cfg['security-profile'] = host['security_profile']

                if radius_port_key_cfg:
                    consolidated_load = {'address': host['name']}
                    consolidated_load['config'] = host_cfg
                    consolidated_load['radius'] = {'config': radius_port_key_cfg}
                    servers_load.append(consolidated_load)

        if servers_load:
            payload = {'openconfig-system:servers': {'server': servers_load}}

        return payload

    def get_modify_servers_request(self, conf):
        """This method formulates the URL and returns a patch request for the servers configuration"""
        request = None

        if conf.get('servers') and conf['servers'].get('host'):
            hosts = conf['servers']['host']
            if hosts:
                url = f'{RADIUS_SERVER_PATH}/servers'
                payload = self.get_radius_server_payload(hosts)
                if payload:
                    request = {'path': url, 'method': PATCH, 'data': payload}

        return request

    def get_modify_global_config_request(self, conf):
        """This method formulates the URL and returns a patch request for the global configuration"""
        request = None
        url = f'{RADIUS_SERVER_PATH}/config'
        payload = self.get_radius_global_payload(conf)

        if payload:
            request = {'path': url, 'method': PATCH, 'data': payload}

        return request

    def get_modify_global_ext_config_request(self, conf):
        """This method formulates the URL and returns a patch request for the global ext configuration"""
        request = None
        url = f'{RADIUS_SERVER_PATH}/openconfig-aaa-radius-ext:radius/config'
        payload = self.get_radius_global_ext_payload(conf)

        if payload:
            request = {'path': url, 'method': PATCH, 'data': payload}

        return request

    def get_modify_radius_server_requests(self, commands):
        """This method returns a list of patch requests generated from commands"""
        requests = []
        if not commands:
            return requests

        request = self.get_modify_global_config_request(commands)
        if request:
            requests.append(request)

        request = self.get_modify_global_ext_config_request(commands)
        if request:
            requests.append(request)

        request = self.get_modify_servers_request(commands)
        if request:
            requests.append(request)

        return requests

    def get_delete_global_ext_params(self, conf):
        """
        This method formulates the URL and returns a list of delete requests for
        the global ext params configuration
        """
        requests = []
        url = f'{RADIUS_SERVER_PATH}/openconfig-aaa-radius-ext:radius/config/'

        if conf.get('nas_ip'):
            requests.append({'path': url + 'nas-ip-address', 'method': DELETE})
        if conf.get('retransmit') is not None:
            requests.append({'path': url + 'retransmit-attempts', 'method': DELETE})
        if conf.get('statistics'):
            requests.append({'path': url + 'statistics', 'method': DELETE})

        return requests

    def get_delete_global_params(self, conf):
        """
        This method formulates the URL and returns a list of delete requests for
        the global params configuration
        """
        requests = []
        url = f'{RADIUS_SERVER_PATH}/config/'

        if conf.get('auth_type'):
            requests.append({'path': url + 'auth-type', 'method': DELETE})
        if conf.get('key'):
            requests.append({'path': url + 'secret-key', 'method': DELETE})
        if conf.get('timeout'):
            requests.append({'path': url + 'timeout', 'method': DELETE})

        return requests

    def get_delete_servers(self, conf):
        """This method formulates the URL and returns a list of delete requests for the servers configuration"""
        requests = []

        if conf.get('servers') and conf['servers'].get('host'):
            hosts = conf['servers']['host']
            for host in hosts:
                url = f'{RADIUS_SERVER_PATH}/servers/server={host["name"]}'

                if len(host) == 1:
                    requests.append({'path': url, 'method': DELETE})
                    continue
                if host.get('auth_type'):
                    requests.append({'path': url + '/config/auth-type', 'method': DELETE})
                if host.get('key'):
                    requests.append({'path': url + '/radius/config/secret-key', 'method': DELETE})
                if host.get('priority'):
                    requests.append({'path': url + '/config/priority', 'method': DELETE})
                # Security profile is dependent on protocol so delete it first
                if host.get('security_profile'):
                    requests.append({'path': url + '/radius/config/security-profile', 'method': DELETE})
                if host.get('protocol'):
                    requests.append({'path': url + '/radius/config/protocol', 'method': DELETE})
                if host.get('port'):
                    requests.append({'path': url + '/radius/config/auth-port', 'method': DELETE})
                if host.get('timeout'):
                    requests.append({'path': url + '/config/timeout', 'method': DELETE})
                if host.get('retransmit') is not None:
                    requests.append({'path': url + '/radius/config/retransmit-attempts', 'method': DELETE})
                if host.get('source_interface'):
                    requests.append({'path': url + '/radius/config/openconfig-aaa-radius-ext:source-interface', 'method': DELETE})
                if host.get('vrf'):
                    requests.append({'path': url + '/config/vrf', 'method': DELETE})

        return requests

    def get_delete_radius_server_requests(self, commands, is_delete_all):
        """This method returns a list of delete requests generated from commands"""
        requests = []

        if not commands:
            return requests

        if is_delete_all:
            requests.append({'path': RADIUS_SERVER_PATH, 'method': DELETE})
            self._delete_all = True
            return requests

        requests.extend(self.get_delete_global_params(commands))
        requests.extend(self.get_delete_global_ext_params(commands))
        requests.extend(self.get_delete_servers(commands))

        return requests

    @staticmethod
    def sort_lists_in_config(config):
        """This method sorts the lists in the radius server configuration"""
        if config and config.get('servers') and config['servers'].get('host'):
            config['servers']['host'].sort(key=lambda x: x['name'])

    def remove_default_entries(self, data):
        """This method removes default entries from the radius server configuration"""
        if data:
            if data.get('auth_type') == 'pap':
                data.pop('auth_type')
            if data.get('timeout') == 5:
                data.pop('timeout')
            if data.get('servers') and data['servers'].get('host'):
                pop_list = []
                for idx, host in enumerate(data['servers']['host']):
                    if len(host) == 1:
                        continue
                    if host.get('protocol') == 'UDP':
                        host.pop('protocol')
                    if host.get('port') == 1812:
                        host.pop('port')
                    if len(host) == 1:
                        pop_list.insert(0, idx)

                for idx in pop_list:
                    data['servers']['host'].pop(idx)

                if not data['servers']['host']:
                    data.pop('servers')

    def get_replaced_config(self, want, have):
        """This method returns the radius server configuration to be replaced and the respective delete requests"""
        config_dict = {}
        requests = []
        cp_want = deepcopy(want)
        cp_have = deepcopy(have)
        self.remove_default_entries(cp_want)
        self.remove_default_entries(cp_have)
        self.sort_lists_in_config(cp_want)
        self.sort_lists_in_config(cp_have)

        if not cp_want or not cp_have:
            return config_dict, requests

        # Handle host level replacement
        if cp_want.get('servers') and len(cp_want) == 1:
            if not cp_have.get('servers'):
                return config_dict, requests

            cfg_host_dict = {host['name']: host for host in cp_have['servers']['host']}
            host_list = []
            for host in cp_want['servers']['host']:
                name = host['name']
                cfg_host = cfg_host_dict.get(name)

                if not cfg_host:
                    continue
                if host != cfg_host:
                    url = f'{RADIUS_SERVER_PATH}/servers/server={cfg_host["name"]}'
                    requests.append({'path': url, 'method': DELETE})
                    host_list.append(cfg_host)
            if host_list:
                config_dict['servers'] = {'host': host_list}

        # Handle config top level replacement
        elif cp_want != cp_have:
            requests.append({'path': RADIUS_SERVER_PATH, 'method': DELETE})
            config_dict = cp_have
            self._delete_all = True

        return config_dict, requests

    def post_process_generated_config(self, config):
        """Handle post processing for generated configuration"""
        if config:
            if 'auth_type' not in config:
                config['auth_type'] = 'pap'
            if 'timeout' not in config:
                config['timeout'] = 5
            if config.get('servers') and config['servers'].get('host'):
                for host in config['servers']['host']:
                    if 'protocol' not in host:
                        host['protocol'] = 'UDP'
                    if 'port' not in host:
                        host['port'] = 1812

        return config

    def __derive_config_delete_op(self, key_set, command, exist_conf):
        """Returns new global configuration for delete operation"""
        if self._delete_all:
            return True, {}

        new_conf = exist_conf
        for k in command:
            if k == 'auth_type':
                new_conf['auth_type'] = 'pap'
            elif k == 'timeout':
                new_conf['timeout'] = 5
            elif k != 'servers':
                new_conf.pop(k)

        return False, new_conf

    def __derive_host_delete_op(self, key_set, command, exist_conf):
        """Returns new host configuration for delete operation"""
        if self._delete_all or len(command) == 1:
            return True, {}

        new_conf = exist_conf
        for k in command:
            if k == 'port':
                new_conf['port'] = 1812
            elif k == 'protocol':
                new_conf['protocol'] = 'UDP'
            elif k != 'name':
                new_conf.pop(k)

        return True, new_conf

    def get_new_config(self, commands, have):
        """Returns generated configuration based on commands and
            existing configuration"""
        key_set = [
            {'config': {'__delete_op': self.__derive_config_delete_op}},
            {'host': {'name': '', '__delete_op': self.__derive_host_delete_op}}
        ]
        new_config = self.post_process_generated_config(get_new_config(commands, have, key_set))
        self.sort_lists_in_config(new_config)

        return new_config
