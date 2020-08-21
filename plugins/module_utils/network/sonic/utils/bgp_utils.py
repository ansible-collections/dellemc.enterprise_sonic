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


afi_safi_types_map = {
    'openconfig-bgp-types:IPV4_UNICAST': 'ipv4_unicast',
    'openconfig-bgp-types:IPV6_UNICAST': 'ipv6_unicast',
    'openconfig-bgp-types:L2VPN_EVPN': 'l2vpn_evpn',
}
GET = "get"
network_instance_path = '/data/openconfig-network-instance:network-instances/network-instance'
protocol_bgp_path = 'protocols/protocol=BGP,bgp/bgp'


def get_all_vrfs(module):
    """Get all VRF configurations available in chassis"""
    all_vrfs = []
    ret = []
    request = {"path": "data/sonic-vrf:sonic-vrf/VRF/VRF_LIST", "method": GET}
    try:
        response = send_requests(module, requests=request)
    except ConnectionError as exc:
        module.fail_json(msg=str(exc), code=exc.code)

    if 'sonic-vrf:VRF_LIST' in response[0][1]:
        all_vrf_data = response[0][1].get('sonic-vrf:VRF_LIST', [])
        if all_vrf_data:
            for vrf_data in all_vrf_data:
                all_vrfs.append(vrf_data['vrf_name'])

    return all_vrfs


def get_peergroups(module, vrf_name):
    peer_groups = []
    request_path = '%s=%s/protocols/protocol=BGP,bgp/bgp/peer-groups' % (network_instance_path, vrf_name)
    request = {"path": request_path, "method": GET}
    try:
        response = send_requests(module, requests=request)
    except ConnectionError as exc:
        module.fail_json(msg=str(exc), code=exc.code)

    resp = response[0][1]
    if 'openconfig-network-instance:peer-groups' in resp:
        data = resp['openconfig-network-instance:peer-groups']
        if 'peer-group' in data:
            for peer_group in data['peer-group']:
                if 'config' in peer_group and 'peer-group-name' in peer_group['config']:
                    peer_groups.append({'name': peer_group['config']['peer-group-name']})

    return peer_groups


def get_all_bgp_af_redistribute(module, vrfs, af_redis_params_map):
    """Get all BGP Global Address Family Redistribute configurations available in chassis"""
    all_af_redis_data = []
    ret_redis_data = []
    for vrf_name in vrfs:
        af_redis_data = {}
        request_path = '%s=%s/table-connections' % (network_instance_path, vrf_name)
        request = {"path": request_path, "method": GET}
        try:
            response = send_requests(module, requests=request)
        except ConnectionError as exc:
            module.fail_json(msg=str(exc), code=exc.code)

        if "openconfig-network-instance:table-connections" in response[0][1]:
            af_redis_data.update({vrf_name: response[0][1]['openconfig-network-instance:table-connections']})

        if af_redis_data:
            all_af_redis_data.append(af_redis_data)

    if all_af_redis_data:
        for vrf_name in vrfs:
            key = vrf_name
            val = next((af_redis_data for af_redis_data in all_af_redis_data if vrf_name in af_redis_data), None)
            if not val:
                continue

            val = val[vrf_name]
            redis_data = val.get('table-connection', [])
            if not redis_data:
                continue
            filtered_redis_data = []
            for e_cfg in redis_data:
                af_redis_data = get_from_params_map(af_redis_params_map, e_cfg)
                if af_redis_data:
                    filtered_redis_data.append(af_redis_data)

            if filtered_redis_data:
                ret_redis_data.append({key: filtered_redis_data})

    return ret_redis_data


def get_all_bgp_globals(module, vrfs):
    """Get all BGP configurations available in chassis"""
    all_bgp_globals = []
    for vrf_name in vrfs:
        get_path = '%s=%s/%s/global' % (network_instance_path, vrf_name, protocol_bgp_path)
        request = {"path": get_path, "method": GET}
        try:
            response = send_requests(module, requests=request)
        except ConnectionError as exc:
            module.fail_json(msg=str(exc), code=exc.code)
        for resp in response:
            if "openconfig-network-instance:global" in resp[1]:
                bgp_data = {'global': resp[1].get("openconfig-network-instance:global", {})}
                bgp_data.update({'vrf_name': vrf_name})
                all_bgp_globals.append(bgp_data)
    return all_bgp_globals


def get_bgp_global_af_data(data, af_params_map):
    ret_af_data = {}
    for key, val in data.items():
        if key == 'global':
            if 'afi-safis' in val and 'afi-safi' in val['afi-safis']:
                global_af_data = []
                raw_af_data = val['afi-safis']['afi-safi']
                for each_af_data in raw_af_data:
                    af_data = get_from_params_map(af_params_map, each_af_data)
                    if af_data:
                        global_af_data.append(af_data)
                ret_af_data.update({'address_family': global_af_data})
            if 'config' in val and 'as' in val['config']:
                as_val = val['config']['as']
                ret_af_data.update({'bgp_as': as_val})
        if key == 'vrf_name':
            ret_af_data.update({'vrf_name': val})
    return ret_af_data


def get_bgp_global_data(data, global_params_map):
    bgp_data = {}
    for key, val in data.items():
        if key == 'global':
            global_data = get_from_params_map(global_params_map, val)
            bgp_data.update(global_data)
        if key == 'vrf_name':
            bgp_data.update({'vrf_name': val})
    return bgp_data


def get_from_params_map(params_map, data):
    ret_data = {}
    for want_key, config_key in params_map.items():
        tmp_data = {}
        for key, val in data.items():
            if key == 'config':
                for k, v in val.items():
                    if k == config_key:
                        val_data = val[config_key]
                        ret_data.update({want_key: val_data})
                        if config_key == 'afi-safi-name':
                            ret_data.pop(want_key)
                            for type_k, type_val in afi_safi_types_map.items():
                                if type_k == val_data:
                                    afi_safi = type_val.split('_')
                                    val_data = afi_safi[0]
                                    ret_data.update({'safi': afi_safi[1]})
                                    ret_data.update({want_key: val_data})
                                    break
            else:
                if key == 'timers' and ('config' in val or 'state' in val):
                    tmp = {}
                    if key in ret_data:
                        tmp = ret_data[key]
                    cfg = val['config'] if 'config' in val else val['state']
                    for k, v in cfg.items():
                        if k == config_key:
                            if k != 'minimum-advertisement-interval':
                                tmp.update({want_key: cfg[config_key]})
                            else:
                                ret_data.update({want_key: cfg[config_key]})
                    if tmp:
                        ret_data.update({key: tmp})

                elif isinstance(config_key, list):
                    i = 0
                    if key == config_key[0]:
                        if key == 'afi-safi':
                            cfg_data = config_key[1]
                            for itm in afi_safi_types_map:
                                if cfg_data in itm:
                                    afi_safi = itm[cfg_data].split('_')
                                    cfg_data = afi_safi[0]
                                    ret_data.update({'safi': afi_safi[1]})
                                    ret_data.update({want_key: cfg_data})
                                    break
                        else:
                            cfg_data = {key: val}
                            for cfg_key in config_key:
                                if cfg_key == 'config':
                                    continue
                                if 'config' in cfg_data:
                                    cfg_data = cfg_data['config']
                                if cfg_key in cfg_data:
                                    cfg_data = cfg_data[cfg_key]
                                else:
                                    break
                            else:
                                ret_data.update({want_key: cfg_data})
                else:
                    if key == config_key and val:
                        if config_key != 'afi-safi-name' and config_key != 'timers':
                            cfg_data = val
                            ret_data.update({want_key: cfg_data})

    return ret_data


def get_bgp_data(module, global_params_map):
    vrf_list = get_all_vrfs(module)
    data = get_all_bgp_globals(module, vrf_list)

    objs = []
    # operate on a collection of resource x
    for conf in data:
        if conf:
            obj = get_bgp_global_data(conf, global_params_map)
            if obj:
                objs.append(obj)
    return objs


def get_bgp_af_data(module, af_params_map):
    vrf_list = get_all_vrfs(module)
    data = get_all_bgp_globals(module, vrf_list)

    objs = []
    # operate on a collection of resource x
    for conf in data:
        if conf:
            obj = get_bgp_global_af_data(conf, af_params_map)
            if obj:
                objs.append(obj)

    return objs


def get_bgp_as(module, vrf_name):
    as_val = None
    get_path = '%s=%s/%s/global/config' % (network_instance_path, vrf_name, protocol_bgp_path)
    request = {"path": get_path, "method": GET}
    try:
        response = send_requests(module, requests=request)
    except ConnectionError as exc:
        module.fail_json(msg=str(exc), code=exc.code)

    resp = response[0][1]
    if "openconfig-network-instance:config" in resp and 'as' in resp['openconfig-network-instance:config']:
        as_val = resp['openconfig-network-instance:config']['as']
    return as_val


def get_bgp_neighbors(module, vrf_name):
    neighbors_data = None
    get_path = '%s=%s/%s/neighbors' % (network_instance_path, vrf_name, protocol_bgp_path)
    request = {"path": get_path, "method": GET}
    try:
        response = send_requests(module, requests=request)
    except ConnectionError as exc:
        module.fail_json(msg=str(exc), code=exc.code)

    resp = response[0][1]
    if "openconfig-network-instance:neighbors" in resp:
        neighbors_data = resp['openconfig-network-instance:neighbors']

    return neighbors_data


def get_all_bgp_neighbors(module):
    vrf_list = get_all_vrfs(module)
    """Get all BGP neighbor configurations available in chassis"""
    all_bgp_neighbors = []

    for vrf_name in vrf_list:
        neighbors_cfg = {}

        bgp_as = get_bgp_as(module, vrf_name)
        if bgp_as:
            neighbors_cfg['bgp_as'] = bgp_as
            neighbors_cfg['vrf_name'] = vrf_name
        else:
            continue

        neighbors = get_bgp_neighbors(module, vrf_name)
        if neighbors:
            neighbors_cfg['neighbors'] = neighbors

        if neighbors_cfg:
            all_bgp_neighbors.append(neighbors_cfg)

    return all_bgp_neighbors
