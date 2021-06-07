#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic bgp_af fact class
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
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.bgp_af.bgp_af import Bgp_afArgs

from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.bgp_utils import (
    get_bgp_af_data,
    get_all_bgp_af_redistribute,
)


class Bgp_afFacts(object):
    """ The sonic bgp_af fact class
    """

    afi_safi_types_map = {
        'openconfig-bgp-types:IPV4_UNICAST': 'ipv4_unicast',
        'openconfig-bgp-types:IPV6_UNICAST': 'ipv6_unicast',
        'openconfig-bgp-types:L2VPN_EVPN': 'l2vpn_evpn',
    }

    af_params_map = {
        'afi': 'afi-safi-name',
        'route_map': 'policy-name',
        'prefix': 'prefix',
        'neighbor': 'neighbor-address',
        'route_reflector_client': 'openconfig-bgp-ext:route-reflector-client',
        'route_server_client': 'openconfig-bgp-ext:route-server-client',
        'next_hop_self': ['openconfig-bgp-ext:next-hop-self', 'enabled'],
        'remove_private_as': ['openconfig-bgp-ext:remove-private-as', 'enabled'],
        'prefix_list_in': ['openconfig-bgp-ext:prefix-list', 'import-policy'],
        'prefix_list_out': ['openconfig-bgp-ext:prefix-list', 'export-policy'],
        'maximum_prefix': ['prefix-limit', 'max-prefixes'],
        'activate': 'enabled',
        'advertise_all_vni': ['l2vpn-evpn', 'openconfig-bgp-evpn-ext:config', 'advertise-all-vni'],
        'advertise_default_gw': ['l2vpn-evpn', 'openconfig-bgp-evpn-ext:config', 'advertise-default-gw'],
        'advertise_list': ['l2vpn-evpn', 'openconfig-bgp-evpn-ext:config', 'advertise-list'],
        'ebgp': ['use-multiple-paths', 'ebgp', 'maximum-paths'],
        'ibgp': ['use-multiple-paths', 'ibgp', 'maximum-paths'],
        'network': ['openconfig-bgp-ext:network-config', 'network'],
        'dampening': ['openconfig-bgp-ext:route-flap-damping', 'config', 'enabled']
    }

    af_redis_params_map = {
        'protocol': 'src-protocol',
        'afi': 'address-family',
        'metric': 'openconfig-network-instance-ext:metric',
        'route_map': 'import-policy'
    }

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = Bgp_afArgs.argument_spec
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
            data = get_bgp_af_data(self._module, self.af_params_map)
            vrf_list = [e_bgp_af['vrf_name'] for e_bgp_af in data]
            self.normalize_af_advertise_prefix(data)
            self.update_max_paths(data)
            self.update_network(data)
            bgp_redis_data = get_all_bgp_af_redistribute(self._module, vrf_list, self.af_redis_params_map)
            self.update_redis_data(data, bgp_redis_data)
            self.update_afis(data)

        # operate on a collection of resource x
        for conf in data:
            if conf:
                obj = self.render_config(self.generated_spec, conf)
        # split the config into instances of the resource
                if obj:
                    objs.append(obj)

        ansible_facts['ansible_network_resources'].pop('bgp_af', None)
        facts = {}
        if objs:
            params = utils.validate_config(self.argument_spec, {'config': remove_empties_from_list(objs)})
            facts['bgp_af'] = params['config']
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

    def check_afi(self, afi, redis_data):
        afi_rhs = afi
        afi_lhs = redis_data.get('afi', None)
        return (afi_lhs and (afi_rhs == afi_lhs))

    def update_redis_data(self, objs, af_redis_data):
        if not (af_redis_data or objs):
            return

        for conf in objs:
            vrf_name = conf['vrf_name']
            raw_af_redis_data = next((e_af_redis for e_af_redis in af_redis_data if vrf_name in e_af_redis), None)
            if not raw_af_redis_data:
                continue
            norm_af_redis_data = self.normalize_af_redis_params(raw_af_redis_data[vrf_name])
            if norm_af_redis_data:
                if 'address_family' in conf:
                    afs = conf['address_family']
                    if not afs:
                        continue
                    for e_af in afs:
                        if 'afi' in e_af:
                            afi = e_af['afi']
                            redis_arr = []
                            for e_redis_data in norm_af_redis_data:
                                if self.check_afi(afi, e_redis_data):
                                    e_redis_data.pop('afi')
                                    redis_arr.append(e_redis_data)
                            e_af.update({'redistribute': redis_arr})
                else:
                    addr_fams = []
                    for e_norm_af_redis in norm_af_redis_data:
                        afi = e_norm_af_redis['afi']
                        e_norm_af_redis.pop('afi')
                        mat_addr_fam = next((each_addr_fam for each_addr_fam in addr_fams if each_addr_fam['afi'] == afi), None)
                        if mat_addr_fam:
                            mat_addr_fam['redistribute'].append(e_norm_af_redis)
                        else:
                            addr_fams.append({'redistribute': [e_norm_af_redis], 'afi': afi})

                    if addr_fams:
                        conf.update({'address_family': addr_fams})

    def update_max_paths(self, data):
        for conf in data:
            afs = conf.get('address_family', [])
            if afs:
                for af in afs:
                    max_path = {}
                    ebgp = af.get('ebgp', None)
                    if ebgp:
                        af.pop('ebgp')
                        max_path['ebgp'] = ebgp
                    ibgp = af.get('ibgp', None)
                    if ibgp:
                        af.pop('ibgp')
                        max_path['ibgp'] = ibgp
                    if max_path:
                        af['max_path'] = max_path

    def update_network(self, data):
        for conf in data:
            afs = conf.get('address_family', [])
            if afs:
                for af in afs:
                    temp = []
                    network = af.get('network', None)
                    if network:
                        for e in network:
                            prefix = e.get('prefix', None)
                            if prefix:
                                temp.append(prefix)
                    af['network'] = temp
                    dampening = af.get('dampening', None)
                    if dampening:
                        af.pop('dampening')
                        af['dampening'] = dampening

    def update_afis(self, data):
        for conf in data:
            if 'address_family' in conf:
                conf['address_family'] = {'afis': conf['address_family']}

    def normalize_af_redis_params(self, af):
        norm_af = list()
        for e_af in af:
            temp = e_af.copy()
            for key, val in e_af.items():
                if 'afi' == key or 'protocol' == key and val:
                    if ':' in val:
                        temp[key] = val.split(':')[1].lower()
                    if '_' in val:
                        temp[key] = val.split('_')[1].lower()
                elif 'route_map' == key and val:
                    temp['route_map'] = val[0]

            norm_af.append(temp)
        return norm_af

    def normalize_af_advertise_prefix(self, data):
        for conf in data:
            afs = conf.get('address_family', [])
            for af in afs:
                advertise_all_vni = af.get('advertise_all_vni', None)
                if advertise_all_vni is None:
                    af['advertise_all_vni'] = False
                advertise_default_gw = af.get('advertise_default_gw', None)
                if advertise_default_gw is None:
                    af['advertise_default_gw'] = False

                if 'advertise_list' not in af:
                    continue
                advertise_list = af.get('advertise_list', [])
                af.pop('advertise_list')
                advertise_prefix_list = []
                for advertise in advertise_list:
                    if advertise in self.afi_safi_types_map:
                        afi_safi = self.afi_safi_types_map[advertise].split('_')
                        advertise_prefix_list.append({'afi': afi_safi[0], 'safi': afi_safi[1]})

                if advertise_prefix_list:
                    af['advertise_prefix'] = advertise_prefix_list
