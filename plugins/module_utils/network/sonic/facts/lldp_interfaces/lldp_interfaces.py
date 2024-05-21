#
# -*- coding: utf-8 -*-
# Copyright 2022 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic lldp_interfaces fact class
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
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.lldp_interfaces.lldp_interfaces import Lldp_interfacesArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible.module_utils.connection import ConnectionError

GET = 'GET'


class Lldp_interfacesFacts(object):
    """ The sonic lldp_interfaces fact class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = Lldp_interfacesArgs.argument_spec
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
        """ Populate the facts for lldp_interfaces
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        if connection:  # just for linting purposes, remove
            pass

        obj = self.get_all_lldp_interfaces()
        ansible_facts['ansible_network_resources'].pop('lldp_interfaces', None)
        facts = {}
        if obj:
            params = utils.validate_config(self.argument_spec, {'config': obj})
            facts['lldp_interfaces'] = utils.remove_empties({'config': params['config']})['config']
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

    def get_all_lldp_interfaces(self):
        """Get all LLDP configurations available in chassis"""
        lldp_interfaces_path = 'data/openconfig-lldp:lldp/interfaces/interface'
        request = [{'path': lldp_interfaces_path, 'method': GET}]

        try:
            response = edit_config(self._module, to_request(self._module, request))
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)

        lldp_op = []
        lldp_interface_configs = []
        if (response[0][1].get('openconfig-lldp:interface')):
            lldp_op = response[0][1].get('openconfig-lldp:interface')
            for interface in lldp_op:
                lldp_interface_data = {}
                lldp_interface_data['tlv_set'] = {}
                lldp_interface_data['tlv_select'] = {}
                lldp_interface_data['med_tlv_select'] = {}
                lldp_tlv_dict = {}
                config = interface.get('config', {})
                lldp_interface_data['name'] = interface.get('name', [])
                lldp_interface_data['enable'] = True
                lldp_interface_data['med_tlv_select']['network_policy'] = True
                lldp_interface_data['med_tlv_select']['power_management'] = True
                lldp_interface_data['tlv_select']['power_management'] = True
                if re.search('Eth', interface['name']):
                    if 'openconfig-lldp-ext:mode' in config:
                        lldp_interface_data['mode'] = config.get('openconfig-lldp-ext:mode').lower()
                    if 'enabled' in config:
                        lldp_interface_data['enable'] = config.get('enabled')
                    if 'openconfig-lldp-ext:suppress-tlv-advertisement' in config:
                        if 'openconfig-lldp-ext:MED_NETWORK_POLICY' in config['openconfig-lldp-ext:suppress-tlv-advertisement']:
                            lldp_interface_data['med_tlv_select']['network_policy'] = False
                        if 'openconfig-lldp-ext:MED_EXT_MDI_POWER' in config['openconfig-lldp-ext:suppress-tlv-advertisement']:
                            lldp_interface_data['med_tlv_select']['power_management'] = False
                        if 'openconfig-lldp-ext:MDI_POWER' in config['openconfig-lldp-ext:suppress-tlv-advertisement']:
                            lldp_interface_data['tlv_select']['power_management'] = False
                    if 'openconfig-lldp-ext:management-address-ipv4' in config:
                        lldp_tlv_dict['ipv4_management_address'] = config.get('openconfig-lldp-ext:management-address-ipv4')
                    if 'openconfig-lldp-ext:management-address-ipv6' in config:
                        lldp_tlv_dict['ipv6_management_address'] = config.get('openconfig-lldp-ext:management-address-ipv6')
                    if any(lldp_tlv_dict.values()):
                        lldp_interface_data['tlv_set'] = lldp_tlv_dict
                    lldp_interface_configs.append(lldp_interface_data)
        return lldp_interface_configs
