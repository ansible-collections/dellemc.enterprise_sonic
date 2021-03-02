#
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
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
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.mclag.mclag import MclagFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.vrfs.vrfs import VrfsFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.vxlans.vxlans import VxlansFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.users.users import UsersFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.port_breakout.port_breakout import Port_breakoutFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.aaa.aaa import AaaFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.tacacs_server.tacacs_server import Tacacs_serverFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.system.system import SystemFacts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.radius_server.radius_server import Radius_serverFacts

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
    mclag=MclagFacts,
    vrfs=VrfsFacts,
    vxlans=VxlansFacts,
    users=UsersFacts,
    system=SystemFacts,
    port_breakout=Port_breakoutFacts,
    aaa=AaaFacts,
    tacacs_server=Tacacs_serverFacts,
    radius_server=Radius_serverFacts,
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
