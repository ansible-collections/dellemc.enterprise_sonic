#
# -*- coding: utf-8 -*-
# Copyright 2024 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic ip_neighbor fact class
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
    remove_empties
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.ip_neighbor.ip_neighbor import Ip_neighborArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)

INTF_PATH = 'data/openconfig-interfaces:interfaces/interface'


class Ip_neighborFacts(object):
    """ The sonic ip_neighbor fact class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = Ip_neighborArgs.argument_spec
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
        """ Populate the facts for ip_neighbor
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        objs = []

        if not data:
            data = self.update_ip_neighbor(self._module)
        objs = data
        facts = {}
        if objs:
            params = utils.validate_config(self.argument_spec, {'config': objs})
            facts['ip_neighbor'] = remove_empties(params['config'])
        ansible_facts['ansible_network_resources'].update(facts)
        return ansible_facts

    def update_ip_neighbor(self, module):
        config_dict = {}

        # Global IP neighbor attributes parsing
        path = 'data/openconfig-neighbor:neighbor-globals/neighbor-global=Values/config'
        nbr_global_cfg = self.get_config(module, path, 'openconfig-neighbor:config')
        if nbr_global_cfg:
            if 'ipv4-arp-timeout' in nbr_global_cfg:
                config_dict['ipv4_arp_timeout'] = nbr_global_cfg['ipv4-arp-timeout']
            if 'ipv4-drop-neighbor-aging-time' in nbr_global_cfg:
                config_dict['ipv4_drop_neighbor_aging_time'] = nbr_global_cfg['ipv4-drop-neighbor-aging-time']
            if 'ipv6-drop-neighbor-aging-time' in nbr_global_cfg:
                config_dict['ipv6_drop_neighbor_aging_time'] = nbr_global_cfg['ipv6-drop-neighbor-aging-time']
            if 'ipv6-nd-cache-expiry' in nbr_global_cfg:
                config_dict['ipv6_nd_cache_expiry'] = nbr_global_cfg['ipv6-nd-cache-expiry']
            if 'num-local-neigh' in nbr_global_cfg:
                config_dict['num_local_neigh'] = nbr_global_cfg['num-local-neigh']

        # Interface IPv6 neighbors attributes parsing
        path = 'data/openconfig-interfaces:interfaces/interface'
        intf_data = self.get_config(module, path, 'openconfig-interfaces:interface')
        if not intf_data:
            return config_dict
        ipv6_nbrs_list = []
        for intf in intf_data:
            ipv6_nbr_dict = {}
            interface = intf.get('name')
            is_vlan = 'Vlan' in interface
            ipv6_data = None

            if is_vlan:
                if 'openconfig-vlan:routed-vlan' in intf and 'openconfig-if-ip:ipv6' in intf['openconfig-vlan:routed-vlan']:
                    ipv6_data = intf['openconfig-vlan:routed-vlan']['openconfig-if-ip:ipv6']
            else:
                if 'subinterfaces' in intf and intf['subinterfaces'] and 'subinterface' in intf['subinterfaces']:
                    for subintf in intf['subinterfaces']['subinterface']:
                        if subintf.get('index') == 0 and 'openconfig-if-ip:ipv6' in subintf:
                            ipv6_data = subintf['openconfig-if-ip:ipv6']

            if ipv6_data:
                rt_adv = ipv6_data.get('router-advertisement')
                if rt_adv:
                    if 'config' in rt_adv:
                        self.parse_rt_adv_cfg(ipv6_nbr_dict, rt_adv['config'])
                    if ('openconfig-interfaces-ext:dns-search-names' in rt_adv and 'dns-search-name' in
                            rt_adv['openconfig-interfaces-ext:dns-search-names']):
                        self.parse_dns_search_names(ipv6_nbr_dict, rt_adv['openconfig-interfaces-ext:dns-search-names']['dns-search-name'])
                    if 'openconfig-interfaces-ext:ra-prefixes' in rt_adv and 'ra-prefix' in rt_adv['openconfig-interfaces-ext:ra-prefixes']:
                        self.parse_ra_prefixes(ipv6_nbr_dict, rt_adv['openconfig-interfaces-ext:ra-prefixes']['ra-prefix'])
                    if ('openconfig-interfaces-ext:rdnss-addresses' in rt_adv and 'rdnss-address' in
                            rt_adv['openconfig-interfaces-ext:rdnss-addresses']):
                        self.parse_rdnss_addresses(ipv6_nbr_dict, rt_adv['openconfig-interfaces-ext:rdnss-addresses']['rdnss-address'])
                if 'config' in ipv6_data and 'ipv6_dad' in ipv6_data['config']:
                    ipv6_nbr_dict['dad'] = ipv6_data['config']['ipv6_dad'].lower()
                if 'neighbors' in ipv6_data and 'neighbor' in ipv6_data['neighbors']:
                    self.parse_nbr(ipv6_nbr_dict, ipv6_data['neighbors']['neighbor'])
            if ipv6_nbr_dict:
                ipv6_nbr_dict['interface'] = interface
                ipv6_nbrs_list.append(ipv6_nbr_dict)
        if ipv6_nbrs_list:
            config_dict['intf_ipv6_neighbors'] = ipv6_nbrs_list

        return config_dict

    def parse_rt_adv_cfg(self, ipv6_nbr_dict, data):
        rt_lookup = {'openconfig-interfaces-ext:LOW': 'low', 'openconfig-interfaces-ext:MEDIUM': 'medium', 'openconfig-interfaces-ext:HIGH': 'high'}

        if 'openconfig-interfaces-ext:adv-interval-option' in data:
            ipv6_nbr_dict['adv_interval_option'] = data['openconfig-interfaces-ext:adv-interval-option']
        if 'openconfig-interfaces-ext:home-agent-config' in data:
            ipv6_nbr_dict['home_agent_config'] = data['openconfig-interfaces-ext:home-agent-config']
        if 'openconfig-interfaces-ext:home-agent-lifetime' in data:
            ipv6_nbr_dict['home_agent_lifetime'] = data['openconfig-interfaces-ext:home-agent-lifetime']
        if 'openconfig-interfaces-ext:home-agent-preference' in data:
            ipv6_nbr_dict['home_agent_preference'] = data['openconfig-interfaces-ext:home-agent-preference']
        if 'interval' in data:
            ipv6_nbr_dict['interval'] = data['interval']
        if 'lifetime' in data:
            ipv6_nbr_dict['lifetime'] = data['lifetime']
        if 'openconfig-interfaces-ext:managed-config' in data:
            ipv6_nbr_dict['managed_config'] = data['openconfig-interfaces-ext:managed-config']
        if 'openconfig-interfaces-ext:min-ra-interval' in data:
            ipv6_nbr_dict['min_ra_interval'] = data['openconfig-interfaces-ext:min-ra-interval']
        if 'openconfig-interfaces-ext:min-ra-interval-msec' in data:
            ipv6_nbr_dict['min_ra_interval_msec'] = data['openconfig-interfaces-ext:min-ra-interval-msec']
        if 'openconfig-interfaces-ext:mtu' in data:
            ipv6_nbr_dict['mtu'] = data['openconfig-interfaces-ext:mtu']
        if 'openconfig-interfaces-ext:other-config' in data:
            ipv6_nbr_dict['other_config'] = data['openconfig-interfaces-ext:other-config']
        if 'openconfig-interfaces-ext:ra-fast-retrans' in data:
            ipv6_nbr_dict['ra_fast_retrans'] = data['openconfig-interfaces-ext:ra-fast-retrans']
        if 'openconfig-interfaces-ext:ra-hop-limit' in data:
            ipv6_nbr_dict['ra_hop_limit'] = data['openconfig-interfaces-ext:ra-hop-limit']
        if 'openconfig-interfaces-ext:ra-interval-msec' in data:
            ipv6_nbr_dict['ra_interval_msec'] = data['openconfig-interfaces-ext:ra-interval-msec']
        if 'openconfig-interfaces-ext:ra-retrans-interval' in data:
            ipv6_nbr_dict['ra_retrans_interval'] = data['openconfig-interfaces-ext:ra-retrans-interval']
        if 'openconfig-interfaces-ext:reachable-time' in data:
            ipv6_nbr_dict['reachable_time'] = data['openconfig-interfaces-ext:reachable-time']
        if 'openconfig-interfaces-ext:router-preference' in data:
            rt_pref = data['openconfig-interfaces-ext:router-preference']
            ipv6_nbr_dict['router_preference'] = rt_lookup[rt_pref]
        if 'suppress' in data:
            ipv6_nbr_dict['suppress'] = data['suppress']

    def parse_dns_search_names(self, ipv6_nbr_dict, data):
        dnssl_list = []
        for dns in data:
            dns_dict = {}
            if 'dnssl-name' in dns:
                dns_dict['name'] = dns['dnssl-name']
            if 'config' in dns and 'valid-lifetime' in dns['config']:
                dns_dict['valid_lifetime'] = dns['config']['valid-lifetime']
            if dns_dict:
                dnssl_list.append(dns_dict)
        if dnssl_list:
            ipv6_nbr_dict['dnssl'] = dnssl_list

    def parse_nbr(self, ipv6_nbr_dict, data):
        nbrs_list = []
        for nbr in data:
            nbr_dict = {}
            if 'ip' in nbr:
                nbr_dict['ip'] = nbr['ip']
            if 'config' in nbr and 'link-layer-address' in nbr['config']:
                nbr_dict['link_layer_address'] = nbr['config']['link-layer-address']
            if nbr_dict:
                nbrs_list.append(nbr_dict)
        if nbrs_list:
            ipv6_nbr_dict['neighbors'] = nbrs_list

    def parse_ra_prefixes(self, ipv6_nbr_dict, data):
        ra_prefixes_list = []
        for pfx in data:
            pfx_dict = {}
            if 'prefix' in pfx:
                pfx_dict['prefix'] = pfx['prefix']
            if 'config' in pfx:
                if 'no-autoconfig' in pfx['config']:
                    pfx_dict['no_autoconfig'] = pfx['config']['no-autoconfig']
                if 'off-link' in pfx['config']:
                    pfx_dict['off_link'] = pfx['config']['off-link']
                if 'preferred-lifetime' in pfx['config']:
                    pfx_dict['preferred_lifetime'] = pfx['config']['preferred-lifetime']
                if 'router-address' in pfx['config']:
                    pfx_dict['router_address'] = pfx['config']['router-address']
                if 'valid-lifetime' in pfx['config']:
                    pfx_dict['valid_lifetime'] = pfx['config']['valid-lifetime']
            if pfx_dict:
                ra_prefixes_list.append(pfx_dict)
        if ra_prefixes_list:
            ipv6_nbr_dict['ra_prefixes'] = ra_prefixes_list

    def parse_rdnss_addresses(self, ipv6_nbr_dict, data):
        rdnss_list = []
        for addr in data:
            addr_dict = {}
            if 'address' in addr:
                addr_dict['address'] = addr['address']
            if 'config' in addr and 'valid-lifetime' in addr['config']:
                addr_dict['valid_lifetime'] = addr['config']['valid-lifetime']
            if addr_dict:
                rdnss_list.append(addr_dict)
        if rdnss_list:
            ipv6_nbr_dict['rdnss'] = rdnss_list

    def get_config(self, module, path, key_name):
        """Retrieve OC configuration from device"""
        cfg = None
        request = {'path': path, 'method': 'get'}

        try:
            response = edit_config(module, to_request(module, request))
            if key_name in response[0][1]:
                cfg = response[0][1].get(key_name)
        except Exception as exc:
            # Avoid raising error when there is no configuration
            if re.search("code.*404|500", str(exc)):
                pass
            else:
                module.fail_json(msg=str(exc), code=exc.code)

        return cfg
