#
# -*- coding: utf-8 -*-
# Copyright 2022 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic vrrp fact class
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
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils \
    import (
        remove_empties_from_list
    )
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.vrrp.vrrp import VrrpArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible.module_utils.connection import ConnectionError


class VrrpFacts(object):
    """ The sonic vrrp fact class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = VrrpArgs.argument_spec
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
        """ Populate the facts for vrrp
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        objs = []
        if connection:  # just for linting purposes, remove
            pass
        all_vrrp_configs = {}

        if not data:
            vrrp_configs = self.get_vrrp()
            for intf_name, vrrp_conf in vrrp_configs.items():
                vrrp_configs_dict = {}
                vrrp_configs_dict['name'] = intf_name
                vrrp_configs_dict['group'] = vrrp_conf
                all_vrrp_configs[intf_name] = vrrp_configs_dict

        for vrrp_config in all_vrrp_configs.items():
            obj = self.render_config(self.generated_spec, vrrp_config)
            if obj:
                objs.append(obj)

        ansible_facts['ansible_network_resources'].pop('vrrp', None)
        facts = {}
        if objs:
            params = utils.validate_config(self.argument_spec, {'config': objs})
            facts['vrrp'] = params['config']

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
        config['name'] = conf[1]['name']
        config['group'] = conf[1]['group']
        return config

    def get_vrrp(self):
        """Get all VRRP/VRRP6 configurations available in chassis"""
        all_vrrp_path = "data/sonic-vrrp:sonic-vrrp"
        method = "GET"
        request = [{"path": all_vrrp_path, "method": method}]

        try:
            response = edit_config(self._module, to_request(self._module, request))
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)

        vrrp_list = {}
        vrrp6_list = {}
        vrrp_track_list = {}
        vrrp6_track_list = {}

        if "sonic-vrrp:sonic-vrrp" in response[0][1]:
            vrrp_list = response[0][1]["sonic-vrrp:sonic-vrrp"].get("VRRP", {})
            vrrp6_list = response[0][1]["sonic-vrrp:sonic-vrrp"].get("VRRP6", {})
            vrrp_track_list = response[0][1]["sonic-vrrp:sonic-vrrp"].get("VRRP_TRACK", {})
            vrrp6_track_list = response[0][1]["sonic-vrrp:sonic-vrrp"].get("VRRP6_TRACK", {})

        vrrp_configs = {}
        for vrrp in vrrp_list.get("VRRP_LIST", []):
            vrrp_dict = {}
            interface = vrrp.get('ifname', None)

            virtual_router_id = vrrp.get("idkey", None)
            if virtual_router_id:
                vrrp_dict['virtual_router_id'] = virtual_router_id
                vrrp_dict['afi'] = "ipv4"
                vip_addresses = []
                for address in vrrp.get('vip', []):
                    temp = {}
                    temp['address'] = address
                    vip_addresses.append(temp)
                if vip_addresses:
                    vrrp_dict['virtual_address'] = vip_addresses

                if vrrp.get("pre_empt", None):
                    vrrp_dict['preempt'] = vrrp.get("pre_empt")
                if vrrp.get("adv_interval", None):
                    vrrp_dict['advertisement_interval'] = vrrp.get("adv_interval")
                if vrrp.get("priority", None):
                    vrrp_dict['priority'] = vrrp.get("priority")
                if vrrp.get("use_v2_checksum", None):
                    vrrp_dict['use_v2_checksum'] = vrrp.get("use_v2_checksum")
                if vrrp.get("version", None):
                    vrrp_dict['version'] = vrrp.get("version")

                track_interface = []
                for vrrp_track in vrrp_track_list.get("VRRP_TRACK_LIST", []):
                    idkey = vrrp_track.get("idkey", None)
                    ifname = vrrp_track.get("baseifname", None)
                    if idkey is not None and ifname is not None:
                        if idkey == virtual_router_id and interface == ifname:
                            priority_increment = vrrp_track.get("priority_increment", None)
                            trackifname = vrrp_track.get("trackifname", None)
                            if priority_increment and trackifname:
                                track = {"interface": trackifname, "priority_increment": priority_increment}
                                track_interface.append(track)

                if track_interface:
                    vrrp_dict['track_interface'] = track_interface
                if interface in vrrp_configs:
                    vrrp_configs[interface].append(vrrp_dict)
                else:
                    vrrp_configs[interface] = []
                    vrrp_configs[interface].append(vrrp_dict)

        for vrrp6 in vrrp6_list.get("VRRP6_LIST", []):
            vrrp6_dict = {}
            interface = vrrp6.get('ifname', None)

            virtual_router_id = vrrp6.get("idkey", None)
            if virtual_router_id:
                vrrp6_dict['virtual_router_id'] = virtual_router_id
                vrrp6_dict['afi'] = "ipv6"
                vip_addresses = []
                for address in vrrp6.get('vip', []):
                    temp = {}
                    temp['address'] = address
                    vip_addresses.append(temp)
                if vip_addresses:
                    vrrp6_dict['virtual_address'] = vip_addresses

                if vrrp6.get("pre_empt", None):
                    vrrp6_dict['preempt'] = vrrp6.get("pre_empt")
                if vrrp6.get("adv_interval", None):
                    vrrp6_dict['advertisement_interval'] = vrrp6.get("adv_interval")
                if vrrp6.get("priority", None):
                    vrrp6_dict['priority'] = vrrp6.get("priority")

                track_interface = []
                for vrrp6_track in vrrp6_track_list.get("VRRP6_TRACK_LIST", []):
                    idkey = vrrp6_track.get("idkey", None)
                    ifname = vrrp6_track.get("baseifname", None)
                    if idkey is not None and ifname is not None:
                        if idkey == virtual_router_id and interface == ifname:
                            priority_increment = vrrp6_track.get("priority_increment", None)
                            trackifname = vrrp6_track.get("trackifname", None)
                            if priority_increment and trackifname:
                                track = {"interface": trackifname, "priority_increment": priority_increment}
                                track_interface.append(track)

                if track_interface:
                    vrrp6_dict['track_interface'] = track_interface
                if interface in vrrp_configs:
                    vrrp_configs[interface].append(vrrp6_dict)
                else:
                    vrrp_configs[interface] = []
                    vrrp_configs[interface].append(vrrp6_dict)

        return vrrp_configs
