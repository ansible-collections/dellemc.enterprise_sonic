#
# -*- coding: utf-8 -*-
# Copyright 2024 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The facts class for sonic
this file validates each subset of facts and selectively
calls the appropriate facts gathering function
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.facts.facts import FactsArgs
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.facts.facts import (
    FactsBase,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.vlans.vlans import VlansFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.interfaces.interfaces import InterfacesFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.l2_interfaces.l2_interfaces import L2_interfacesFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.l3_interfaces.l3_interfaces import L3_interfacesFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.lag_interfaces.lag_interfaces import Lag_interfacesFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.bgp.bgp import BgpFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.bgp_af.bgp_af import Bgp_afFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.bgp_neighbors.bgp_neighbors import Bgp_neighborsFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.bgp_neighbors_af.bgp_neighbors_af import Bgp_neighbors_afFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.bgp_as_paths.bgp_as_paths import Bgp_as_pathsFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.bgp_communities.bgp_communities import Bgp_communitiesFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.bgp_ext_communities.bgp_ext_communities import (
    Bgp_ext_communitiesFacts,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.ospfv2_interfaces.ospfv2_interfaces import Ospfv2_interfacesFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.ospfv2.ospfv2 import Ospfv2Facts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.mclag.mclag import MclagFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.prefix_lists.prefix_lists import Prefix_listsFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.vlan_mapping.vlan_mapping import Vlan_mappingFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.vrfs.vrfs import VrfsFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.vrrp.vrrp import VrrpFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.vxlans.vxlans import VxlansFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.users.users import UsersFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.port_breakout.port_breakout import Port_breakoutFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.aaa.aaa import AaaFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.ldap.ldap import LdapFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.tacacs_server.tacacs_server import Tacacs_serverFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.system.system import SystemFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.radius_server.radius_server import Radius_serverFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.static_routes.static_routes import Static_routesFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.ntp.ntp import NtpFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.logging.logging import LoggingFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.pki.pki import PkiFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.ip_neighbor.ip_neighbor import Ip_neighborFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.port_group.port_group import Port_groupFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.dhcp_relay.dhcp_relay import Dhcp_relayFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.dhcp_snooping.dhcp_snooping import Dhcp_snoopingFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.acl_interfaces.acl_interfaces import Acl_interfacesFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.l2_acls.l2_acls import L2_aclsFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.l3_acls.l3_acls import L3_aclsFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.lldp_global.lldp_global import Lldp_globalFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.mac.mac import MacFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.bfd.bfd import BfdFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.copp.copp import CoppFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.route_maps.route_maps import Route_mapsFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.lldp_interfaces.lldp_interfaces import Lldp_interfacesFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.stp.stp import StpFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.sflow.sflow import SflowFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.fips.fips import FipsFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.roce.roce import RoceFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.qos_buffer.qos_buffer import Qos_bufferFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.qos_pfc.qos_pfc import Qos_pfcFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.qos_maps.qos_maps import Qos_mapsFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.qos_scheduler.qos_scheduler import Qos_schedulerFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.qos_wred.qos_wred import Qos_wredFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.qos_interfaces.qos_interfaces import Qos_interfacesFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.pim_global.pim_global import Pim_globalFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.pim_interfaces.pim_interfaces import Pim_interfacesFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.login_lockout.login_lockout import Login_lockoutFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.poe.poe import PoeFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.mgmt_servers.mgmt_servers import Mgmt_serversFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.ospf_area.ospf_area import Ospf_areaFacts

FACT_LEGACY_SUBSETS = {}
FACT_RESOURCE_SUBSETS = dict(
    vlans=VlansFacts,
    interfaces=InterfacesFacts,
    l2_interfaces=L2_interfacesFacts,
    l3_interfaces=L3_interfacesFacts,
    lag_interfaces=Lag_interfacesFacts,
    bgp=BgpFacts,
    bgp_af=Bgp_afFacts,
    bgp_neighbors=Bgp_neighborsFacts,
    bgp_neighbors_af=Bgp_neighbors_afFacts,
    bgp_as_paths=Bgp_as_pathsFacts,
    bgp_communities=Bgp_communitiesFacts,
    bgp_ext_communities=Bgp_ext_communitiesFacts,
    ospfv2_interfaces=Ospfv2_interfacesFacts,
    ospfv2=Ospfv2Facts,
    mclag=MclagFacts,
    prefix_lists=Prefix_listsFacts,
    vlan_mapping=Vlan_mappingFacts,
    vrfs=VrfsFacts,
    vrrp=VrrpFacts,
    vxlans=VxlansFacts,
    users=UsersFacts,
    system=SystemFacts,
    port_breakout=Port_breakoutFacts,
    aaa=AaaFacts,
    ldap=LdapFacts,
    tacacs_server=Tacacs_serverFacts,
    radius_server=Radius_serverFacts,
    static_routes=Static_routesFacts,
    ntp=NtpFacts,
    logging=LoggingFacts,
    pki=PkiFacts,
    ip_neighbor=Ip_neighborFacts,
    port_group=Port_groupFacts,
    dhcp_relay=Dhcp_relayFacts,
    dhcp_snooping=Dhcp_snoopingFacts,
    acl_interfaces=Acl_interfacesFacts,
    l2_acls=L2_aclsFacts,
    l3_acls=L3_aclsFacts,
    lldp_global=Lldp_globalFacts,
    mac=MacFacts,
    bfd=BfdFacts,
    copp=CoppFacts,
    route_maps=Route_mapsFacts,
    lldp_interfaces=Lldp_interfacesFacts,
    stp=StpFacts,
    sflow=SflowFacts,
    fips=FipsFacts,
    roce=RoceFacts,
    qos_buffer=Qos_bufferFacts,
    qos_pfc=Qos_pfcFacts,
    qos_maps=Qos_mapsFacts,
    qos_scheduler=Qos_schedulerFacts,
    qos_wred=Qos_wredFacts,
    qos_interfaces=Qos_interfacesFacts,
    pim_global=Pim_globalFacts,
    pim_interfaces=Pim_interfacesFacts,
    login_lockout=Login_lockoutFacts,
    poe=PoeFacts,
    mgmt_servers=Mgmt_serversFacts,
    ospf_area=Ospf_areaFacts
)


class Facts(FactsBase):
    """ The fact class for sonic
    """

    VALID_LEGACY_GATHER_SUBSETS = frozenset(FACT_LEGACY_SUBSETS.keys())
    VALID_RESOURCE_SUBSETS = frozenset(FACT_RESOURCE_SUBSETS.keys())

    def __init__(self, module):
        super(Facts, self).__init__(module)

    def get_facts(self, legacy_facts_type=None, resource_facts_type=None, data=None):
        """ Collect the facts for sonic

        :param legacy_facts_type: List of legacy facts types
        :param resource_facts_type: List of resource fact types
        :param data: previously collected conf
        :rtype: dict
        :return: the facts gathered
        """
        netres_choices = FactsArgs.argument_spec['gather_network_resources'].get('choices', [])
        if self.VALID_RESOURCE_SUBSETS:
            self.get_network_resources_facts(FACT_RESOURCE_SUBSETS, resource_facts_type, data)

        if self.VALID_LEGACY_GATHER_SUBSETS:
            self.get_network_legacy_facts(FACT_LEGACY_SUBSETS, legacy_facts_type)

        return self.ansible_facts, self._warnings
