#
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic mfa fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from copy import deepcopy

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.mfa.mfa import MfaArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)


class MfaFacts(object):
    """ The sonic mfa fact class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = MfaArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)

    def populate_facts(self, connection, ansible_facts, data=None):
        """ Populate the facts for mfa
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        objs = []

        if connection:  # just for linting purposes, remove
            pass

        if not data:
            mfa_cfg = self.get_all_mfa_configs(self._module)
            data = self.update_mfa(mfa_cfg)

        objs = self.render_config(self.generated_spec, data)
        facts = {}
        if objs:
            params = utils.validate_config(self.argument_spec, {'config': objs})
            facts['mfa'] = utils.remove_empties(params['config'])
        ansible_facts['ansible_network_resources'].update(facts)

        return ansible_facts

    def render_config(self, spec, conf):
        """
        Render config as dictionary structure and delete keys
          from spec for null values

        :param spec: The facts tree, generated from the argspec
        :param conf: The configuration
        :rtype: dictionary
        :returns: The generated config
        """
        config = self.parse_sonic_mfa(spec, conf)
        return config

    def parse_sonic_mfa(self, spec, conf):
        config = deepcopy(spec)
        if conf:
            if ('mfa_global' in conf) and (conf['mfa_global']):
                config['mfa_global'] = conf['mfa_global']
            if ('rsa_global' in conf) and (conf['rsa_global']):
                config['rsa_global'] = conf['rsa_global']
            if ('rsa_servers' in conf) and (conf['rsa_servers']):
                config['rsa_servers'] = conf['rsa_servers']
            if ('cac_piv_global' in conf) and (conf['cac_piv_global']):
                config['cac_piv_global'] = conf['cac_piv_global']

        return utils.remove_empties(config)

    def get_all_mfa_configs(self, module):
        """Get all MFA configurations available in chassis"""

        mfa_cfg = None
        get_mfa_path = '/data/openconfig-mfa:mfa'
        request = {'path': get_mfa_path, 'method': 'get'}

        try:
            response = edit_config(module, to_request(module, request))
            mfa_cfg = response[0][1].get('openconfig-mfa:mfa', None)
        except ConnectionError as exc:
            module.fail_json(msg=str(exc), code=exc.code)

        return mfa_cfg

    def update_mfa(self, data):
        config_dict = {}
        if data:
            config_dict['mfa_global'] = self.update_mfa_global(data)
            config_dict['rsa_global'] = self.update_rsa_global(data)
            config_dict['rsa_servers'] = self.update_rsa_servers(data)
            config_dict['cac_piv_global'] = self.update_cac_piv_global(data)

        return config_dict

    def update_mfa_global(self, data):
        mfa_global_dict = {}

        mfa_global = data.get('mfa-global')
        if mfa_global:
            mfa_global_config = mfa_global.get('config')
            if mfa_global_config:
                client_secret = mfa_global_config.get('client-secret')
                client_secret_encrypted = mfa_global_config.get('client-secret-encrypted')
                key_seed = mfa_global_config.get('key-seed')
                key_seed_encrypted = mfa_global_config.get('key-seed-encrypted')
                security_profile = mfa_global_config.get('mfa-security-profile')

                if client_secret:
                    mfa_global_dict['client_secret'] = client_secret
                if client_secret_encrypted:
                    mfa_global_dict['client_secret_encrypted'] = client_secret_encrypted
                if key_seed:
                    mfa_global_dict['key_seed'] = key_seed
                if key_seed_encrypted:
                    mfa_global_dict['key_seed_encrypted'] = key_seed_encrypted
                if security_profile:
                    mfa_global_dict['security_profile'] = security_profile

        return mfa_global_dict

    def update_rsa_global(self, data):
        rsa_global_dict = {}

        rsa_global = data.get('rsa-global')
        if rsa_global:
            rsa_global_config = rsa_global.get('config')
            if rsa_global_config:
                security_profile = rsa_global_config.get('rsa-security-profile')
                if security_profile:
                    rsa_global_dict['security_profile'] = security_profile

        return rsa_global_dict

    def get_rsa_server_data(self, data):
        rsa_server_list = []

        for rsa_server in data:
            rsa_server_dict = {}
            hostname = rsa_server.get('hostname')
            rsa_server_config = rsa_server.get('config')

            if hostname:
                rsa_server_dict['hostname'] = hostname
            if rsa_server_config:
                server_port = rsa_server_config.get('port-number')
                client_id = rsa_server_config.get('client-id')
                client_key = rsa_server_config.get('client-key')
                client_key_encrypted = rsa_server_config.get('client-key-encrypted')
                connection_timeout = rsa_server_config.get('connection-timeout')
                read_timeout = rsa_server_config.get('read-timeout')

                if server_port:
                    rsa_server_dict['server_port'] = server_port
                if client_id:
                    rsa_server_dict['client_id'] = client_id
                if client_key:
                    rsa_server_dict['client_key'] = client_key
                if client_key_encrypted:
                    rsa_server_dict['client_key_encrypted'] = client_key_encrypted
                if connection_timeout:
                    rsa_server_dict['connection_timeout'] = connection_timeout
                if read_timeout:
                    rsa_server_dict['read_timeout'] = read_timeout

            if rsa_server_dict:
                rsa_server_list.append(rsa_server_dict)

        return rsa_server_list

    def update_rsa_servers(self, data):
        rsa_servers_list = []

        rsa_servers = data.get('rsa-servers')
        if rsa_servers:
            rsa_server = rsa_servers.get('rsa-server')
            if rsa_server:
                rsa_server_list = self.get_rsa_server_data(rsa_server)
                if rsa_server_list:
                    rsa_servers_list = rsa_server_list

        return rsa_servers_list

    def update_cac_piv_global(self, data):
        cac_piv_global_dict = {}

        cac_piv_global = data.get('cac-piv-global')
        if cac_piv_global:
            cac_piv_global_config = cac_piv_global.get('config')
            if cac_piv_global_config:
                security_profile = cac_piv_global_config.get('cacpiv-security-profile')
                cert_username_field = cac_piv_global_config.get('cert-username-field')
                cert_username_match = cac_piv_global_config.get('cert-username-match')

                if security_profile:
                    cac_piv_global_dict['security_profile'] = security_profile
                if cert_username_field:
                    cac_piv_global_dict['cert_username_field'] = cert_username_field
                if cert_username_match:
                    cac_piv_global_dict['cert_username_match'] = cert_username_match

        return cac_piv_global_dict
