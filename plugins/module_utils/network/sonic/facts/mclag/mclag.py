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
        request = [{"path": "data/openconfig-mclag:mclag/mclag-domains", "method": GET}]
        try:
            response = edit_config(self._module, to_request(self._module, request))
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)
        if ('openconfig-mclag:mclag-domains' in response[0][1]):
            data = response[0][1]['openconfig-mclag:mclag-domains']
        else:
            data = {}
        if data:
            data = data['mclag-domain'][0]['state']
        return data

    def get_all_mclag_unique_ip(self):
        """Get all the mclag unique ip available in chassis"""
        request = [{"path": "data/openconfig-mclag:mclag/vlan-interfaces", "method": GET}]
        try:
            response = edit_config(self._module, to_request(self._module, request))
        except ConnectionError as exc:
            self.module.fail_json(msg=str(exc), code=exc.code)
        if ('openconfig-mclag:vlan-interfaces' in response[0][1]):
            data = response[0][1]['openconfig-mclag:vlan-interfaces']
        else:
            data = {}
        return data

    def get_all_mclag_portchannel_members(self):
        """Get all the mclag portchannel members for the domain available in chassis"""
        request = [{"path": "data/openconfig-mclag:mclag/interfaces", "method": GET}]
        try:
            response = edit_config(self._module, to_request(self._module, request))
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)
        if ('openconfig-mclag:interfaces' in response[0][1]):
            data = response[0][1]['openconfig-mclag:interfaces']
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
        if not data:
            data = self.get_all_mclag()
        if data:
            unique_ip = self.get_all_mclag_unique_ip()
            if unique_ip:
                data.update(unique_ip)
            portchannel_members = self.get_all_mclag_portchannel_members()
            if portchannel_members:
                data.update(portchannel_members)
        objs = []
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
        config = deepcopy(spec)
        vlans_list = []
        portchannels_list = []
        if conf:
            if ('domain-id' in conf) and (conf['domain-id']):
                config['domain_id'] = conf['domain-id']
            if ('session-timeout' in conf) and (conf['session-timeout']):
                config['session_timeout'] = conf['session-timeout']
            if ('keepalive-interval' in conf) and (conf['keepalive-interval']):
                config['keepalive'] = conf['keepalive-interval']
            if ('source-address' in conf) and (conf['source-address']):
                config['source_address'] = conf['source-address']
            if ('peer-address' in conf) and (conf['peer-address']):
                config['peer_address'] = conf['peer-address']
            if ('peer-link' in conf) and (conf['peer-link']):
                config['peer_link'] = conf['peer-link']
            if ('vlan-interface' in conf) and (conf['vlan-interface']):
                for each in conf['vlan-interface']:
                    vlans_list.append({'vlan': each['name']})
                if vlans_list:
                    config['unique_ip']['vlans'] = vlans_list
            if ('interface' in conf) and (conf['interface']):
                for each in conf['interface']:
                    portchannels_list.append({'lag': each['name']})
                if portchannels_list:
                    config['members']['portchannels'] = portchannels_list
        return utils.remove_empties(config)
