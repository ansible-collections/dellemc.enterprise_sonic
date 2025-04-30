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

        ansible_facts['ansible_network_resources'].pop('mfa', None)
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
        return utils.remove_empties(conf)

    def get_all_mfa_configs(self, module):
        """Get all MFA configurations available in chassis"""

        request = {'path': '/data/openconfig-mfa:mfa', 'method': 'get'}
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

        mfa_global = data.get('mfa-global', {})
        mfa_global_config = mfa_global.get('config', {})
        mfa_global_dict['client_secret'] = mfa_global_config.get('client-secret')
        mfa_global_dict['client_secret_encrypted'] = mfa_global_config.get('client-secret-encrypted')
        mfa_global_dict['key_seed'] = mfa_global_config.get('key-seed')
        mfa_global_dict['key_seed_encrypted'] = mfa_global_config.get('key-seed-encrypted')
        mfa_global_dict['security_profile'] = mfa_global_config.get('mfa-security-profile')

        return mfa_global_dict

    def update_rsa_global(self, data):
        rsa_global_dict = {}

        rsa_global = data.get('rsa-global', {})
        rsa_global_config = rsa_global.get('config', {})
        rsa_global_dict['security_profile'] = rsa_global_config.get('rsa-security-profile')

        return rsa_global_dict

    def get_rsa_server_data(self, data):
        rsa_server_list = []

        for rsa_server in data:
            rsa_server_dict = {}
            rsa_server_config = rsa_server.get('config', {})
            rsa_server_dict['hostname'] = rsa_server.get('hostname')
            rsa_server_dict['server_port'] = rsa_server_config.get('port-number')
            rsa_server_dict['client_id'] = rsa_server_config.get('client-id')
            rsa_server_dict['client_key'] = rsa_server_config.get('client-key')
            rsa_server_dict['client_key_encrypted'] = rsa_server_config.get('client-key-encrypted')
            rsa_server_dict['connection_timeout'] = rsa_server_config.get('connection-timeout')
            rsa_server_dict['read_timeout'] = rsa_server_config.get('read-timeout')
            rsa_server_list.append(rsa_server_dict)

        return rsa_server_list

    def update_rsa_servers(self, data):
        rsa_servers_list = []

        rsa_servers = data.get('rsa-servers', {})
        rsa_server = rsa_servers.get('rsa-server', {})
        rsa_server_list = self.get_rsa_server_data(rsa_server)
        rsa_servers_list = rsa_server_list

        return rsa_servers_list

    def update_cac_piv_global(self, data):
        cac_piv_global_dict = {}

        cac_piv_global = data.get('cac-piv-global', {})
        cac_piv_global_config = cac_piv_global.get('config', {})
        cac_piv_global_dict['security_profile'] = cac_piv_global_config.get('cacpiv-security-profile')
        cac_piv_global_dict['cert_username_field'] = cac_piv_global_config.get('cert-username-field')
        cac_piv_global_dict['cert_username_match'] = cac_piv_global_config.get('cert-username-match')

        return cac_piv_global_dict
