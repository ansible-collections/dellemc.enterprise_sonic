#
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic radius_server fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from __future__ import absolute_import, division, print_function
__metaclass__ = type
from copy import deepcopy

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    remove_empties
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.radius_server.radius_server import Radius_serverArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible.module_utils.connection import ConnectionError


class Radius_serverFacts(object):
    """ The sonic radius_server fact class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = Radius_serverArgs.argument_spec
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
        """ Populate the facts for radius_server
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        facts = {}

        if not data:
            cfg = self.get_config(self._module)
            data = self.render_config(cfg)

        if data:
            params = utils.validate_config(self.argument_spec, {'config': data})
            facts['radius_server'] = remove_empties(params['config'])
        ansible_facts['ansible_network_resources'].update(facts)

        return ansible_facts

    def get_config(self, module):
        """Gets the list of RADIUS server configuration configured on the device"""
        cfg = None
        get_path = 'data/openconfig-system:system/aaa/server-groups/server-group=RADIUS'
        request = {'path': get_path, 'method': 'get'}

        try:
            response = edit_config(module, to_request(module, request))
            if 'openconfig-system:server-group' in response[0][1]:
                cfg = response[0][1].get('openconfig-system:server-group')
        except ConnectionError as exc:
            module.fail_json(msg=str(exc), code=exc.code)

        return cfg

    def render_config(self, cfg):
        """Transform OC data to argspec format"""
        radius_server_data = {}

        if cfg:
            if cfg[0].get('config'):
                raw_radius_global_data = cfg[0]['config']

                if 'auth-type' in raw_radius_global_data:
                    radius_server_data['auth_type'] = raw_radius_global_data['auth-type']
                if 'secret-key' in raw_radius_global_data and raw_radius_global_data['secret-key']:
                    radius_server_data['key'] = raw_radius_global_data['secret-key']
                if 'timeout' in raw_radius_global_data:
                    radius_server_data['timeout'] = raw_radius_global_data['timeout']

            if cfg[0].get('openconfig-aaa-radius-ext:radius') and cfg[0]['openconfig-aaa-radius-ext:radius'].get('config'):
                raw_radius_ext_global_data = cfg[0]['openconfig-aaa-radius-ext:radius']['config']

                if 'nas-ip-address' in raw_radius_ext_global_data:
                    radius_server_data['nas_ip'] = raw_radius_ext_global_data['nas-ip-address']
                if 'retransmit-attempts' in raw_radius_ext_global_data:
                    radius_server_data['retransmit'] = raw_radius_ext_global_data['retransmit-attempts']
                if 'statistics' in raw_radius_ext_global_data:
                    radius_server_data['statistics'] = raw_radius_ext_global_data['statistics']

            if cfg[0].get('servers') and cfg[0]['servers'].get('server'):
                raw_radius_server_list = cfg[0]['servers']['server']
                hosts = []

                for radius_host in raw_radius_server_list:
                    host_data = {}
                    if 'address' in radius_host:
                        host_data['name'] = radius_host['address']
                        server_cfg = radius_host.get('config')
                        if server_cfg:
                            if 'auth-type' in server_cfg:
                                host_data['auth_type'] = server_cfg['auth-type']
                            if 'priority' in server_cfg:
                                host_data['priority'] = server_cfg['priority']
                            if 'vrf' in server_cfg:
                                host_data['vrf'] = server_cfg['vrf']
                            if 'timeout' in server_cfg:
                                host_data['timeout'] = server_cfg['timeout']
                        if radius_host.get('radius') and radius_host['radius'].get('config'):
                            radius_cfg = radius_host['radius']['config']
                            if radius_cfg.get('auth-port'):
                                host_data['port'] = radius_cfg['auth-port']
                            if radius_cfg.get('secret-key'):
                                host_data['key'] = radius_cfg['secret-key']
                            if radius_cfg.get('openconfig-aaa-radius-ext:source-interface'):
                                host_data['source_interface'] = radius_cfg['openconfig-aaa-radius-ext:source-interface']
                            if radius_cfg.get('retransmit-attempts') is not None:
                                host_data['retransmit'] = radius_cfg['retransmit-attempts']
                            if radius_cfg.get('protocol'):
                                host_data['protocol'] = radius_cfg['protocol']
                            if radius_cfg.get('security-profile'):
                                host_data['security_profile'] = radius_cfg['security-profile']
                    if host_data:
                        hosts.append(host_data)
                if hosts:
                    radius_server_data['servers'] = {'host': hosts}

        return radius_server_data
