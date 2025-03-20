#
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic vlans fact class
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
    remove_empties_from_list,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.vlans.vlans import VlansArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible.module_utils.connection import ConnectionError

GET = "get"


class VlansFacts(object):
    """ The sonic vlans fact class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = VlansArgs.argument_spec
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
        """ Populate the facts for vlans
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        if connection:  # just for linting purposes, remove
            pass

        if not data:
            vlans = self.get_vlans()
        objs = []
        for vlan_id, vlan_config in vlans.items():
            obj = self.render_config(self.generated_spec, vlan_config)
            if obj:
                objs.append(obj)
        ansible_facts['ansible_network_resources'].pop('vlans', None)
        facts = {}
        if objs:
            params = utils.validate_config(self.argument_spec, {'config': objs})
            facts['vlans'] = remove_empties_from_list(params.get("config"))
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
        config = deepcopy(spec)
        try:
            if conf.get('vlan_id') is not None:
                config['vlan_id'] = int(conf.get('vlan_id'))
            config['description'] = conf.get('description')
            config['autostate'] = conf.get('autostate')
        except TypeError:
            config['vlan_id'] = None
            config['description'] = None
            config['autostate'] = None
        return utils.remove_empties(config)

    def get_vlans(self):
        """Get all the l2_interfaces available in chassis"""
        # Grab description data from the openconfig-interfaces endpoint
        request = [{"path": "data/openconfig-interfaces:interfaces", "method": GET}]
        try:
            response = edit_config(self._module, to_request(self._module, request))
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)

        interfaces = {}
        if "openconfig-interfaces:interfaces" in response[0][1]:
            interfaces = response[0][1].get("openconfig-interfaces:interfaces", {})
            if interfaces.get("interface"):
                interfaces = interfaces['interface']

        ret_vlan_configs = {}

        for interface in interfaces:
            if interface.get("config") is None:
                continue
            interface_name = interface["config"].get("name")
            description = interface["config"].get("description", "")
            if "Vlan" in interface_name:
                vlan_id = interface_name.split("Vlan")[1]
                vlan_configs = {"vlan_id": vlan_id,
                                "name": interface_name,
                                "description": description
                                }
                ret_vlan_configs.update({vlan_id: vlan_configs})

        # Grabbing autostate data from the sonic-vlan endpoint
        request = [{"path": "data/sonic-vlan:sonic-vlan", "method": GET}]
        try:
            response = edit_config(self._module, to_request(self._module, request))
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)

        interface_dict = {}
        # Need to check for response
        if response:
            if len(response) >= 1:
                if len(response[0]) >= 1:
                    if "sonic-vlan:sonic-vlan" in response[0][1]:
                        interfaces = response[0][1].get("sonic-vlan:sonic-vlan", {})
                        if interfaces:
                            if interfaces.get("VLAN"):
                                if interfaces.get("VLAN").get("VLAN_LIST"):
                                    interface_dict = interfaces['VLAN']["VLAN_LIST"]
        
                    for interface in interface_dict:
                        vlan_name = interface.get("name")
                        autostate = bool(interface.get("autostate", None) == "enable")
                        vlan_id = str(interface.get("vlanid"))
                        vlan_configs = {"vlan_id": vlan_id,
                                        "name": vlan_name,
                                        "autostate": autostate
                                        }
                        if vlan_id in ret_vlan_configs:
                            ret_vlan_configs[vlan_id]["autostate"] = autostate
                        else:
                            ret_vlan_configs.update({vlan_id: vlan_configs})
        
            return ret_vlan_configs
