#
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic dcbx_interfaces fact class
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

from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    remove_empties_from_list
)

from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.dcbx_interfaces.dcbx_interfaces import Dcbx_interfacesArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible.module_utils.connection import ConnectionError

GET = 'GET'

class Dcbx_interfacesFacts(object):
    """ The sonic dcbx_interfaces fact class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = Dcbx_interfacesArgs.argument_spec
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
        """ Populate the facts for dcbx_interfaces
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        if connection:
            pass

        obj = self.get_all_dcbx_interfaces()

        ansible_facts['ansible_network_resources'].pop('dcbx_interfaces', None)
        facts = {}
        if obj:
            params = utils.validate_config(self.argument_spec, {'config': obj})
            facts['dcbx_interfaces'] = remove_empties_from_list(params['config'])
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

    def get_all_dcbx_interfaces(self):
        """Get all DCBx configurations available in chassis"""
        dcbx_interfaces_path = 'data/openconfig-dcbx:dcbx/interfaces/interface'
        request = [{'path': dcbx_interfaces_path, 'method': GET}]

        try:
            response = edit_config(self._module, to_request(self._module, request))
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)

        dcbx_op = []
        dcbx_interface_configs = []
        if (response[0][1].get('openconfig-dcbx:interface')):
            dcbx_op = response[0][1].get('openconfig-dcbx:interface')

            for interface in dcbx_op:
                dcbx_interface_data = {}
                config = interface.get('config', {})

                dcbx_interface_data['name'] = interface.get('name', [])
                if re.search('Eth', interface['name']):
                    if 'name' in config:
                        dcbx_interface_data['name'] = config.get('name')
                    if 'enabled' in config:
                        dcbx_interface_data['enabled'] = config.get('enabled')
                    if 'pfc-tlv-enabled' in config:
                        dcbx_interface_data['pfc_tlv_enabled'] = config.get('pfc-tlv-enabled')
                    if 'ets-configuration-tlv-enabled' in config:
                        dcbx_interface_data['ets_configuration_tlv_enabled'] = config.get('ets-configuration-tlv-enabled')
                    if 'ets-recommendation-tlv-enabled' in config:
                        dcbx_interface_data['ets_recommendation_tlv_enabled'] = config.get('ets-recommendation-tlv-enabled')
                    dcbx_interface_configs.append(dcbx_interface_data)
            return dcbx_interface_configs
