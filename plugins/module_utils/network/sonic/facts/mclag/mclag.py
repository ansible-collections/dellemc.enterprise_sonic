#
# -*- coding: utf-8 -*-
# Copyright 2020 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic mclag fact class
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
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.mclag.mclag import MclagArgs
from ansible.module_utils.connection import ConnectionError

GET = "get"


class MclagFacts(object):
    """ The sonic mclag fact class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = MclagArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)

    def get_all_mclag(self):
        """Get all the mclag available in chassis"""
        request = [{"path": "data/openconfig-mclag:mclag", "method": GET}]
        try:
            response = edit_config(self._module, to_request(self._module, request))
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)
        if ('openconfig-mclag:mclag' in response[0][1]):
            data = response[0][1]['openconfig-mclag:mclag']
        else:
            data = {}
        return data

    def populate_facts(self, connection, ansible_facts, data=None):
        """ Populate the facts for mclag
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        objs = None
        if not data:
            data = self.get_all_mclag()
        if data:
            objs = self.render_config(self.generated_spec, data)
        facts = {}
        if objs:
            params = utils.validate_config(self.argument_spec, {'config': objs})
            facts['mclag'] = params['config']

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
        config = self.parse_sonic_mclag(spec, conf)
        return config

    def parse_sonic_mclag(self, spec, conf):
        config = {}
        portchannels_list = []
        if conf:
            domain_data = None
            if conf.get('mclag-domains', None) and conf['mclag-domains'].get('mclag-domain', None):
                domain_data = conf['mclag-domains']['mclag-domain'][0]
            if domain_data:
                domain_id = domain_data['domain-id']
                config['domain_id'] = domain_id
                domain_config = domain_data.get('config', None)
                if domain_config:
                    if domain_config.get('session-timeout', None):
                        config['session_timeout'] = domain_config['session-timeout']
                    if domain_config.get('keepalive-interval', None):
                        config['keepalive'] = domain_config['keepalive-interval']
                    if domain_config.get('source-address', None):
                        config['source_address'] = domain_config['source-address']
                    if domain_config.get('peer-address', None):
                        config['peer_address'] = domain_config['peer-address']
                    if domain_config.get('peer-link', None):
                        config['peer_link'] = domain_config['peer-link']
                    if domain_config.get('mclag-system-mac', None):
                        config['system_mac'] = domain_config['mclag-system-mac']

                if conf.get('vlan-interfaces', None) and conf['vlan-interfaces'].get('vlan-interface', None):
                    vlans_list = []
                    vlan_data = conf['vlan-interfaces']['vlan-interface']
                    for vlan in vlan_data:
                        vlans_list.append({'vlan': vlan['name']})
                    if vlans_list:
                        config['unique_ip'] = {'vlans': vlans_list}

                if conf.get('interfaces', None) and conf['interfaces'].get('interface', None):
                    portchannels_list = []
                    po_data = conf['interfaces']['interface']
                    for po in po_data:
                        if po.get('config', None) and po['config'].get('mclag-domain-id', None) and domain_id == domain_data['domain-id']:
                            portchannels_list.append({'lag': po['name']})
                    if portchannels_list:
                        config['members'] = {'portchannels': portchannels_list}

        return config
