#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic bgp fact class
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
from ansible_collections.dellemc.sonic.plugins.module_utils.network.sonic.argspec.bgp.bgp import BgpArgs
from ansible_collections.dellemc.sonic.plugins.module_utils.network.sonic.sonic import send_requests

GET = "get"


class BgpFacts(object):
    """ The sonic bgp fact class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = BgpArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)

    def get_all_bgp_af_network(self):
        """Get all BGP Global Address Family Network configurations available in chassis"""
        all_bgp_globals_af_ntw = []
        request = {"path": "data/sonic-bgp-global:sonic-bgp-global/BGP_GLOBALS_AF_NETWORK", "method": GET}
        try:
            response = send_requests(self._module, requests=request)
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)
        for resp in response:
            if "sonic-bgp-global:BGP_GLOBALS_AF_NETWORK" in resp[1]:
                all_bgp_globals_af_ntw = resp[1].get("sonic-bgp-global:BGP_GLOBALS_AF_NETWORK", [])
                ret = all_bgp_globals_af_ntw['BGP_GLOBALS_AF_NETWORK_LIST']
            else:
                ret = []
        return ret

    def get_all_bgp_af_redistribute(self, vrf_name):
        """Get all BGP Global Address Family Redistribute configurations available in chassis"""
        all_bgp_globals_af_redis = []
        request_path = "data/openconfig-network-instance:network-instances/network-instance=%s/table-connections" % (vrf_name)
        request = {"path": request_path, "method": GET}
        try:
            response = send_requests(self._module, requests=request)
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)

        for resp in response:
            if "openconfig-network-instance:table-connections" in resp[1]:
                all_bgp_globals_af_redis = resp[1].get("openconfig-network-instance:table-connections", [])
                ret = all_bgp_globals_af_redis['table-connection']
            else:
                ret = []
        return ret

    def get_all_bgp_af_neighbor(self):
        """Get all BGP Global Address Family Neighbor configurations available in chassis"""
        all_bgp_globals_af_nei = []
        request = {"path": "data/sonic-bgp-neighbor:sonic-bgp-neighbor/BGP_NEIGHBOR_AF", "method": GET}
        try:
            response = send_requests(self._module, requests=request)
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)
        for resp in response:
            if "sonic-bgp-neighbor:BGP_NEIGHBOR_AF" in resp[1]:
                all_bgp_globals_af_nei = resp[1].get("sonic-bgp-neighbor:BGP_NEIGHBOR_AF", [])
                ret = all_bgp_globals_af_nei['BGP_NEIGHBOR_AF_LIST']
            else:
                ret = []
        return ret

    def get_all_bgp_globals_af(self):
        """Get all BGP Global Address Family configurations available in chassis"""
        all_bgp_globals_af = []
        request = {"path": "data/sonic-bgp-global:sonic-bgp-global/BGP_GLOBALS_AF", "method": GET}
        try:
            response = send_requests(self._module, requests=request)
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)
        for resp in response:
            if "sonic-bgp-global:BGP_GLOBALS_AF" in resp[1]:
                all_bgp_globals_af = resp[1].get("sonic-bgp-global:BGP_GLOBALS_AF", [])
                ret = all_bgp_globals_af['BGP_GLOBALS_AF_LIST']
            else:
                ret = []
        return ret

    def get_all_bgp_globals(self):
        """Get all BGP Global configurations available in chassis"""
        all_bgp_globals = []
        request = {"path": "data/sonic-bgp-global:sonic-bgp-global/BGP_GLOBALS", "method": GET}
        try:
            response = send_requests(self._module, requests=request)
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)
        for resp in response:
            if "sonic-bgp-global:BGP_GLOBALS" in resp[1]:
                all_bgp_globals = resp[1].get("sonic-bgp-global:BGP_GLOBALS", [])
                ret = all_bgp_globals['BGP_GLOBALS_LIST']
            else:
                ret = []
        return ret

    def get_all_bgp_peer_groups(self):
        """Get all BGP Peer Group configurations available in chassis"""
        all_bgp_peer_groups = []
        request = {"path": "data/sonic-bgp-peergroup:sonic-bgp-peergroup/BGP_PEER_GROUP/BGP_PEER_GROUP_LIST", "method": GET}
        try:
            response = send_requests(self._module, requests=request)
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)
        for resp in response:
            if "sonic-bgp-peergroup:BGP_PEER_GROUP_LIST" in resp[1]:
                all_bgp_peer_groups = resp[1].get("sonic-bgp-peergroup:BGP_PEER_GROUP_LIST", [])
                ret = all_bgp_peer_groups
            else:
                ret = []
        return ret

    def get_all_bgp_neighbors(self):
        """Get all BGP Neighbor configurations available in chassis"""
        all_bgp_neighbors = []
        request = {"path": "data/sonic-bgp-neighbor:sonic-bgp-neighbor/BGP_NEIGHBOR/BGP_NEIGHBOR_LIST", "method": GET}
        try:
            response = send_requests(self._module, requests=request)
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)
        for resp in response:
            if "sonic-bgp-neighbor:BGP_NEIGHBOR_LIST" in resp[1]:
                all_bgp_neighbors = resp[1].get("sonic-bgp-neighbor:BGP_NEIGHBOR_LIST", [])
                ret = all_bgp_neighbors
            else:
                ret = []
        return ret

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
            # typically data is populated from the current device configuration
            # data = connection.get('show running-config | section ^e')
            # using mock data instead
            data = self.get_all_bgp_globals()
            neighbors_data = self.get_all_bgp_neighbors()
            peergroups_data = self.get_all_bgp_peer_groups()
            af_data = self.get_all_bgp_globals_af()
            af_ntw_data = self.get_all_bgp_af_network()
            af_nei_data = self.get_all_bgp_af_neighbor()
            if data:
                for item in data:
                    neighbor_list = list()
                    peergroup_list = list()
                    af_list = list()
                    af_redis_data = self.get_all_bgp_af_redistribute(item['vrf_name'])
                    # Neighbors
                    for neighbor in neighbors_data:
                        if ('vrf_name' in item) and (item['vrf_name'] == neighbor['vrf_name']):
                            neighbor_list.append(neighbor)
                    if neighbor_list:
                        item.update({'neighbors': neighbor_list})
                    # PeerGroups
                    for peergroup in peergroups_data:
                        if ('vrf_name' in item) and (item['vrf_name'] == peergroup['vrf_name']):
                            peergroup_list.append(peergroup)
                    if peergroup_list:
                        item.update({'peer_groups': peergroup_list})
                    # Address Family
                    for af in af_data:
                        if ('vrf_name' in item) and (item['vrf_name'] == af['vrf_name']):
                            # Address Family Networks
                            af_ntw_list = []
                            for af_ntw in af_ntw_data:
                                if (item['vrf_name'] == af_ntw['vrf_name']) and (af['afi_safi'] == af_ntw['afi_safi']):
                                    af_ntw_list.append(af_ntw)
                            if af_ntw_list:
                                af.update({'networks': af_ntw_list})

                            # Address Family Neighbors
                            af_nei_list = []
                            for af_nei in af_nei_data:
                                if (item['vrf_name'] == af_nei['vrf_name']) and (af['afi_safi'] == af_nei['afi_safi']):
                                    af_nei_list.append(af_nei)
                            if af_nei_list:
                                af.update({'neighbors': af_nei_list})

                            # Address Family Redistribute
                            af_redis_list = []
                            for af_redis in af_redis_data:
                                af_redis_afi_safi = af_redis['address-family'].split(':')
                                af_redis['afi_safi'] = af_redis_afi_safi[1].lower() + "_unicast"
                                if af['afi_safi'] == af_redis['afi_safi']:
                                    af_redis_list.append(af_redis)
                            if af_redis_list:
                                af.update({'redistribute': af_redis_list})
                            af_list.append(af)
                    if af_list:
                        item.update({'address_family': af_list})
        # operate on a collection of resource x
        for conf in data:
            if conf:
                obj = self.render_config(self.generated_spec, conf)
        # split the config into instances of the resource
                if obj:
                    objs.append(obj)

        ansible_facts['ansible_network_resources'].pop('bgp', None)
        facts = {}
        if objs:
            params = utils.validate_config(self.argument_spec, {'config': remove_empties_from_list(objs)})
            facts['bgp'] = params['config']
        ansible_facts['ansible_network_resources'].update(facts)
        return ansible_facts

    def normalize_peer_group_params(self, peer_groups):
        ret = list()
        peer_group_params_map = {'peer_group_name': 'peer_group_name'}
        for peer_group in peer_groups:
            temp = dict()
            for key, val in peer_group_params_map.items():
                if val in peer_group and peer_group[val]:
                    temp.update({key: peer_group[val]})
            ret.append(temp)
        return ret

    def normalize_af_params(self, afs):
        ret = list()
        af_params_map = {'afi': 'afi',
                         'safi': 'safi',
                         'networks': 'networks',
                         'neighbors': 'neighbors',
                         'redistribute': 'redistribute'}
        for af in afs:
            temp = dict()
            if 'afi_safi' in af:
                af_key = af['afi_safi'].split('_')
                temp.update({'afi': af_key[0]})
                temp.update({'safi': af_key[1]})
            if 'networks' in af:
                temp.update({'networks': self.normalize_af_network_params(af)})
            if 'neighbors' in af:
                temp.update({'neighbors': self.normalize_af_neighbor_params(af)})
            if 'redistribute' in af:
                temp.update({'redistribute': self.normalize_af_redis_params(af)})
            ret.append(temp)
        return ret

    def normalize_af_redis_params(self, af):
        ret = list()
        af_redis_params_map = {
            'protocol': 'src-protocol',
            'metric': ['config', 'openconfig-network-instance-ext:metric'],
            'route_map': ['config', 'import-policy']}

        for af_redis in af['redistribute']:
            temp = dict()
            for key, val in af_redis_params_map.items():
                if key == 'protocol' and val in af_redis:
                    af_redis_protocol = af_redis['src-protocol'].split(':')
                    temp.update({'protocol': af_redis_protocol[1].lower()})
                elif isinstance(val, list):
                    if val[1] in af_redis[val[0]] and af_redis[val[0]][val[1]]:
                        if key == 'route_map':
                            value = af_redis[val[0]][val[1]]
                            temp.update({key: value[0]})
                        else:
                            temp.update({key: af_redis[val[0]][val[1]]})
            ret.append(temp)
        return ret

    def normalize_af_network_params(self, af):
        ret = list()
        af_ntw_params_map = {
            'prefix': 'ip_prefix',
            'route_map': 'policy'}

        for af_ntw in af['networks']:
            temp = dict()
            for key, val in af_ntw_params_map.items():
                if val == 'ip_prefix' and val in af_ntw:
                    af_ntw_prefix = af_ntw['ip_prefix'].split('/')
                    temp.update({'prefix': af_ntw_prefix[0]})
                    temp.update({'masklen': af_ntw_prefix[1]})
                elif val in af_ntw and af_ntw[val]:
                    temp.update({key: af_ntw[val]})
            ret.append(temp)
        return ret

    def normalize_af_neighbor_params(self, af):
        ret = list()
        af_nei_params_map = {
            'route_reflector_client': 'rrclient',
            'route_server_client': 'route_server_client',
            'activate': 'admin_status',
            'neighbor': 'neighbor',
            'remove_private_as': 'remove_private_as_enabled',
            'next_hop_self': 'nhself',
            'maximum_prefix': 'max_prefix_limit',
            'prefix_list_in': 'prefix_list_in',
            'prefix_list_out': 'prefix_list_out'}

        for af_nei in af['neighbors']:
            temp = dict()
            for key, val in af_nei_params_map.items():
                if val in af_nei and af_nei[val]:
                    temp.update({key: af_nei[val]})

            ret.append(temp)
        return ret

    def normalize_neighbor_params(self, neighbors):
        ret = list()
        neighbor_params_map = {
            'neighbor': 'neighbor',
            'remote_as': 'asn',
            'update_source': 'local_addr',
            'password': 'auth_password',
            'enabled': 'admin_status',
            'description': 'name',
            'ebgp_multihop': 'ebgp_multihop_ttl',
            'peer_group': 'peer_group_name',
            'timers': ['keepalive', 'holdtime'],
            'local_as': 'local_asn',
            'advertisement_interval': 'min_adv_interval'}

        for neighbor in neighbors:
            temp = dict()
            for key, val in neighbor_params_map.items():
                if key == 'timers':
                    temp_timer = dict()
                    for timer_key in val:
                        if timer_key in neighbor and neighbor[timer_key]:
                            temp_timer.update({timer_key: neighbor[timer_key]})
                    if temp_timer:
                        temp.update({key: temp_timer})
                elif val in neighbor and neighbor[val]:
                    temp.update({key: neighbor[val]})
            ret.append(temp)
        return ret

    def render_config(self, spec, conf):
        """
        Render config as dictionary structure and delete keys
          from spec for null values

        :param spec: The facts tree, generated from the argspec
        :param conf: The configuration
        :rtype: dictionary
        :returns: The generated config
        """

        config = self.parse_sonic_rest(spec, conf)
        return config

    def parse_sonic_rest(self, spec, conf):
        config = deepcopy(spec)
        config['vrf_name'] = conf['vrf_name']
        config['bgp_as'] = conf['local_asn'] if 'local_asn' in conf else ""
        config['router_id'] = conf['router_id'] if 'router_id' in conf else ""
        config['log_neighbor_changes'] = conf['log_nbr_state_changes'] if 'log_nbr_state_changes' in conf else ""
        config['neighbors'] = self.normalize_neighbor_params(conf['neighbors']) if 'neighbors' in conf else ""
        config['address_family'] = self.normalize_af_params(conf['address_family']) if 'address_family' in conf else ""
        config['peer_groups'] = self.normalize_peer_group_params(conf['peer_groups']) if 'peer_groups' in conf else ""
        return utils.remove_empties(config)
