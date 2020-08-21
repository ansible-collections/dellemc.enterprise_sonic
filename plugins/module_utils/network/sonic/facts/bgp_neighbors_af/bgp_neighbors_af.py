#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic bgp_neighbors_af fact class
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
from ansible_collections.dellemc.sonic.plugins.module_utils.network.sonic.utils.utils import (
    remove_empties_from_list
)
from ansible_collections.dellemc.sonic.plugins.module_utils.network.sonic.argspec.bgp_neighbors_af.bgp_neighbors_af import Bgp_neighbors_afArgs
from ansible_collections.dellemc.sonic.plugins.module_utils.network.sonic.sonic import send_requests
from ansible_collections.dellemc.sonic.plugins.module_utils.network.sonic.utils.bgp_utils import (
    get_bgp_af_data,
    get_bgp_neighbors,
    get_peergroups,
    get_from_params_map,
)


class Bgp_neighbors_afFacts(object):
    """ The sonic bgp_neighbors_af fact class
    """

    neighbor_af_af_params_map = {
        'afi': 'afi-safi-name',
    }
    neighbor_af_afi_safi_param_map = {
        'afi': 'afi-safi-name',
        'maximum_prefix': ['ipv4-unicast', 'prefix-limit', 'max-prefixes'],
        'next_hop_self': ['openconfig-bgp-ext:next-hop-self', 'enabled'],
        'route_reflector_client': 'openconfig-bgp-ext:route-reflector-client',
        'route_server_client': 'openconfig-bgp-ext:route-server-client',
        'remove_private_as': ['openconfig-bgp-ext:remove-private-as', 'enabled'],
        'origin': ['openconfig-bgp-ext:allow-own-as', 'origin'],
        'value': ['openconfig-bgp-ext:allow-own-as', 'enabled'],
        'in_route_name': ['apply-policy', 'import-policy'],
        'out_route_name': ['apply-policy', 'export-policy'],
        'activate': ['state', 'active'],
    }
    neighbor_af_nei_params_map = {
        'neighbor': 'neighbor-address',
        'prefix_list_in': ['openconfig-bgp-ext:prefix-list', 'import-policy'],
        'prefix_list_out': ['openconfig-bgp-ext:prefix-list', 'export-policy'],
    }

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = Bgp_neighbors_afArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)

    def fill_route_map(self, afi_safi):
        for route_map_key in ['out_route_name', 'in_route_name']:
            if route_map_key in afi_safi:
                route_map = afi_safi['route_map']
                for e_route in afi_safi[route_map_key]:
                    direction = route_map_key.split('_')[0].capitalize()  # 'Out' if 'out' in route_map_key.lower() else 'In'
                    route_map.append({'name': e_route, 'direction': direction})
                afi_safi.pop(route_map_key)

    def filter_neighbors_data(self, af_data, nei_data):
        if nei_data and 'neighbor' in nei_data:
            fil_neighbors = []
            for e_nei in nei_data['neighbor']:
                afi_safi = get_from_params_map(self.neighbor_af_afi_safi_param_map, e_nei['afi-safis']['afi-safi'][0])
                fil_nei_data = get_from_params_map(self.neighbor_af_nei_params_map, e_nei)
                addr_fam = []
                if afi_safi:
                    afi = afi_safi['afi']
                    safi = afi_safi['safi']
                    if 'activate' not in afi_safi:
                        afi_safi['activate'] = False

                    afi_safi['route_map'] = []
                    self.fill_route_map(afi_safi)
                    """
                    if 'out_route_name' in afi_safi:
                        rout_map = afi_safi['route_map']
                        for e_route in afi_safi['out_route_name']:
                            rout_map.append({'name': e_route, 'direction': 'Out'})
                        afi_safi.pop('out_route_name')

                    if 'in_route_name' in afi_safi:
                        rout_map = afi_safi['route_map']
                        for e_route in afi_safi['in_route_name']:
                            rout_map.append({'name': e_route, 'direction': 'In'})
                        afi_safi.pop('in_route_name')
                    """

                    if 'origin' in afi_safi:
                        afi_safi['allowas_in'] = {'origin': afi_safi['origin']}
                        afi_safi.pop('origin')
                        if 'value' in afi_safi:
                            val = 1 if afi_safi['value'] else 0
                            afi_safi['allowas_in'].update({'value': val})
                            afi_safi.pop('value')

                    if 'address_family' in af_data:
                        addr_fam = next((e_af for e_af in af_data['address_family'] if(e_af['afi'] == afi and e_af['safi'] == safi)), [])
                    if fil_nei_data:
                        afi_safi.pop('afi')
                        afi_safi.pop('safi')
                        fil_nei_data.update(afi_safi)

                if fil_nei_data and addr_fam:
                    if 'neighbors' in addr_fam:
                        addr_fam['neighbors'].append(fil_nei_data)
                    else:
                        addr_fam['neighbors'] = [fil_nei_data]

    def populate_facts(self, connection, ansible_facts, data=None):
        """ Populate the facts for BGP
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        objs = list()
        if connection:  # just for linting purposes, remove
            pass

        if not data:
            af_data = get_bgp_af_data(self._module, self.neighbor_af_af_params_map)

            for cfg in af_data:
                vrf_name = cfg['vrf_name']
                nei_data = get_bgp_neighbors(self._module, vrf_name)
                if nei_data:
                    self.filter_neighbors_data(cfg, nei_data)

            data = af_data

        # operate on a collection of resource x
        for conf in data:
            if conf:
                obj = self.render_config(self.generated_spec, conf)
        # split the config into instances of the resource
                if obj:
                    objs.append(obj)

        ansible_facts['ansible_network_resources'].pop('bgp_neighbors_af', None)
        facts = {}
        if objs:
            params = utils.validate_config(self.argument_spec, {'config': remove_empties_from_list(objs)})
            facts['bgp_neighbors_af'] = params['config']
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
