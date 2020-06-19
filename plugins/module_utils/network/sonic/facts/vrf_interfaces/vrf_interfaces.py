#
# -*- coding: utf-8 -*-
# © Copyright 2020 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic vrf_interfaces fact class
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
from ansible_collections.dellemc.sonic.plugins.module_utils.network.sonic.argspec.vrf_interfaces.vrf_interfaces import Vrf_interfacesArgs
from ansible_collections.dellemc.sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)

GET = "get"


class Vrf_interfacesFacts(object):
    """ The sonic vrf_interfaces fact class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = Vrf_interfacesArgs.argument_spec
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
        """ Populate the facts for vrf_interfaces
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        if connection:  # just for linting purposes, remove
            pass

        if not data:
            # typically data is populated from the current device configuration
            # data = connection.get('show running-config | section ^interface')
            # using mock data instead
            data = self.get_all_vrf_interfaces()

        objs = list()
        for conf in data:
            if conf:
                obj = self.render_config(self.generated_spec, conf)
                if obj:
                    objs.append(obj)

        ansible_facts['ansible_network_resources'].pop('vrf_interfaces', None)
        facts = {}
        if objs:
            facts['vrf_interfaces'] = []
            params = utils.validate_config(self.argument_spec, {'config': objs})
            if params:
                facts['vrf_interfaces'].extend(params['config'])
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

    def get_all_vrf_interfaces(self):
        """Get all the interfaces available in chassis"""
        all_network_instatnces = {}
        request = [{"path": "data/openconfig-network-instance:network-instances", "method": GET}]
        try:
            response = edit_config(self._module, to_request(self._module, request))
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)

        if "openconfig-network-instance:network-instances" in response[0][1]:
            all_network_instatnces = response[0][1].get("openconfig-network-instance:network-instances", {})
        return self.get_vrf_interfaces_from_network_instances(all_network_instatnces['network-instance'])

    def get_vrf_interfaces_from_network_instances(self, network_instances):
        vrf_interfaces = []

        for each_ins in network_instances:
            vrf_interface = dict()
            name = each_ins['name']
            if name.startswith('Vrf'):
                vrf_interface['name'] = name
                if each_ins.get("interfaces"):
                    members = [intf.get("id") for intf in each_ins["interfaces"]["interface"]]
                    vrf_interface.update({"members": members})

                vrf_interfaces.append(vrf_interface)
        return vrf_interfaces
