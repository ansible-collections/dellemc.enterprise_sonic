#
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The arg spec for the sonic facts module.
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class FactsArgs(object):  # pylint: disable=R0903

    """ The arg spec for the sonic facts module
    """

    def __init__(self, **kwargs):
        pass

    choices = [
        'all',
        'aaa',
        'acl_interfaces',
        'dcbx',
        'bfd',
        'bgp',
        'bgp_af',
        'bgp_as_paths',
        'bgp_communities',
        'bgp_ext_communities',
        'bgp_neighbors',
        'bgp_neighbors_af',
        'br_l2pt',
        'copp',
        'dhcp_relay',
        'dhcp_snooping',
        'evpn_esi_multihome',
        'fbs_classifiers',
        'fips',
        'interfaces',
        'ip_neighbor',
        'ipv6_router_advertisement',
        'lag_interfaces',
        'ldap',
        'lldp_global',
        'lldp_interfaces',
        'logging',
        'login_lockout',
        'lst',
        'l2_acls',
        'l3_acls',
        'l2_interfaces',
        'l3_interfaces',
        'mac',
        'mclag',
        'mgmt_servers',
        'mirroring',
        'ntp',
        'ospf_area',
        'ospfv2',
        'ospfv2_interfaces',
        'pim_global',
        'pim_interfaces',
        'pki',
        'poe',
        'port_breakout',
        'port_group',
        'prefix_lists',
        'qos_buffer',
        'qos_interfaces',
        'qos_maps',
        'qos_pfc',
        'qos_scheduler',
        'qos_wred',
        'radius_server',
        'roce',
        'route_maps',
        'sflow',
        'snmp',
        'ssh',
        'ssh_server',
        'static_routes',
        'stp',
        'system',
        'tacacs_server',
        'users',
        'vlans',
        'vlan_mapping',
        'vrfs',
        'vrrp',
        'vxlans
    ]

    argument_spec = {
        'gather_subset': dict(default=['!config'], type='list', elements='str'),
        'gather_network_resources': dict(choices=choices, type='list', elements='str'),
    }
