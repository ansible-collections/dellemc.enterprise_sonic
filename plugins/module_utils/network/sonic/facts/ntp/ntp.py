#
# -*- coding: utf-8 -*-
# Copyright 2022 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic ntp fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import re
from copy import deepcopy

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.ntp.ntp import NtpArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible.module_utils.connection import ConnectionError

GET = "get"


class NtpFacts(object):
    """ The sonic ntp fact class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = NtpArgs.argument_spec
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
        """ Populate the facts for ntp
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        if not data:
            # typically data is populated from the current device configuration
            # data = connection.get('show running-config | section ^interface')
            # using mock data instead
            data = self.get_ntp_configuration()

        obj = self.render_config(self.generated_spec, data)

        ansible_facts['ansible_network_resources'].pop('ntp', None)
        facts = {}
        if obj:
            params = utils.validate_config(self.argument_spec, {'config': obj})
            facts['ntp'] = params['config']

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
        return conf

    def get_ntp_configuration(self):
        """Get all NTP configuration"""

        config_request = [{"path": "data/openconfig-system:system/ntp/config", "method": GET}]
        config_response = []
        try:
            config_response = edit_config(self._module, to_request(self._module, config_request))
        except ConnectionError as exc:
            if re.search("code.*404", str(exc)):
                # Resource not found
                config_response = [(404, {'openconfig-system:config': {}})]
            else:
                self._module.fail_json(msg=str(exc), code=exc.code)

        ntp_global_config = {'source_interfaces': [], 'network-instance': None}
        if 'openconfig-system:config' in config_response[0][1]:
            ntp_global_config = config_response[0][1].get('openconfig-system:config', {})

        servers_request = [{"path": "data/openconfig-system:system/ntp/servers/server", "method": GET}]
        servers_response = []
        try:
            servers_response = edit_config(self._module, to_request(self._module, servers_request))
        except ConnectionError as exc:
            if re.search("code.*404", str(exc)):
                # Resource not found
                servers_response = [(404, {'openconfig-system:server': []})]
            else:
                self._module.fail_json(msg=str(exc), code=exc.code)

        ntp_servers = []
        if 'openconfig-system:server' in servers_response[0][1]:
            ntp_servers = servers_response[0][1].get('openconfig-system:server', {})

        ntp_config_log = dict()
        ntp_config_log['config'] = ntp_global_config
        ntp_config_log['servers'] = ntp_servers

        ntp_config = dict()
        if 'network-instance' in ntp_global_config:
            ntp_config['vrf'] = ntp_global_config['network-instance']
        else:
            ntp_config['vrf'] = None

        if 'source-interface' in ntp_global_config:
            ntp_config['source_interfaces'] = ntp_global_config['source-interface']
        else:
            ntp_config['source_interfaces'] = []

        servers = []
        for ntp_server in ntp_servers:
            if 'config' in ntp_server:
                servers.append(ntp_server['config'])
        ntp_config['servers'] = servers

        return ntp_config
