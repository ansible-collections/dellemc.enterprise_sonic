#
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic fbs_interfaces fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from __future__ import absolute_import, division, print_function
__metaclass__ = type

from copy import deepcopy
from ansible.module_utils.connection import ConnectionError
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    remove_empties_from_list
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.fbs_interfaces.fbs_interfaces import Fbs_interfacesArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)


class Fbs_interfacesFacts(object):
    """ The sonic fbs_interfaces fact class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = Fbs_interfacesArgs.argument_spec
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
        """ Populate the facts for fbs_groups
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        if not data:
            cfg = self.get_config(self._module)
            data = self.render_config(cfg)
        facts = {}
        if data:
            params = utils.validate_config(self.argument_spec, {'config': data})
            facts['fbs_interfaces'] = remove_empties_from_list(params['config'])
        ansible_facts['ansible_network_resources'].update(facts)
        return ansible_facts

    def get_config(self, module):
        """Gets the list of FBS interface configurations if present"""
        cfg = None
        get_path = 'data/openconfig-fbs-ext:fbs/interfaces/interface'
        request = {'path': get_path, 'method': 'get'}

        try:
            response = edit_config(module, to_request(module, request))
            if 'openconfig-fbs-ext:interface' in response[0][1]:
                cfg = response[0][1].get('openconfig-fbs-ext:interface')
        except ConnectionError as exc:
            module.fail_json(msg=str(exc), code=exc.code)

        return cfg

    def render_config(self, cfg):
        """Transform OC data to argspec format"""
        config_list = []

        if cfg:
            for intf in cfg:
                intf_dict = {}
                name = intf.get('id')
                ingress_policies = intf.get('ingress-policies')
                egress_policies = intf.get('egress-policies')

                if name:
                    intf_dict['name'] = name
                if ingress_policies:
                    intf_dict['ingress_policies'] = {}
                    for policy_type in ('forwarding', 'monitoring', 'qos'):
                        if (policy_type in ingress_policies and 'config' in ingress_policies[policy_type]
                                and ingress_policies[policy_type]['config'].get('policy-name')):

                            policy_name = ingress_policies[policy_type]['config']['policy-name']
                            intf_dict['ingress_policies'].update({policy_type: {'policy_name': policy_name}})
                if egress_policies:
                    if ('qos' in egress_policies and 'config' in egress_policies['qos'] and egress_policies['qos']['config'].get('policy-name')):
                        policy_name = egress_policies['qos']['config']['policy-name']
                        intf_dict['egress_policies'] = {'qos': {'policy_name': policy_name}}

                if intf_dict:
                    config_list.append(intf_dict)

        return config_list
