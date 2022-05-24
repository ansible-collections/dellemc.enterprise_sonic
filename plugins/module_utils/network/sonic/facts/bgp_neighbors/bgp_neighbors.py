#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic bgp_neighbors fact class
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
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.bgp_neighbors.bgp_neighbors import Bgp_neighborsArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.bgp_utils import (
    get_all_bgp_neighbors,
    get_from_params_map,
    get_peergroups,
)


class Bgp_neighborsFacts(object):
    """ The sonic bgp_neighbors fact class
    """

    neighbor_params_map = {
        'neighbor': 'neighbor-address',
        'peer_as': 'peer-as',
        'peer_type': 'peer-type',
        'peer_group': 'peer-group',
        'keepalive': 'keepalive-interval',
        'holdtime': 'hold-time',
        'advertisement_interval': 'minimum-advertisement-interval',
        'bfd': ['openconfig-bfd:enable-bfd', 'enabled'],
        'dynamic': 'openconfig-bgp-ext:capability-dynamic',
        'extended_nexthop': 'openconfig-bgp-ext:capability-extended-nexthop',
        'pwd': ['openconfig-bgp-ext:auth-password', 'password'],
        'encrypted': ['openconfig-bgp-ext:auth-password', 'encrypted'],
        'nbr_description': 'description',
    }

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = Bgp_neighborsArgs.argument_spec
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

        if not data:
            data = get_all_bgp_neighbors(self._module)
            filtered_data = self.filter_neighbors_data(data)
            if filtered_data:
                data = filtered_data

        for conf in data:
            if conf:
                obj = self.render_config(self.generated_spec, conf)
                if obj:
                    objs.append(obj)

        ansible_facts['ansible_network_resources'].pop('bgp_neighbors', None)
        facts = {}
        if objs:
            params = utils.validate_config(self.argument_spec, {'config': remove_empties_from_list(objs)})
            facts['bgp_neighbors'] = params['config']
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

    def filter_neighbors_data(self, data):
        filtered_data = []
        for conf in data:
            vrf_name = conf['vrf_name']
            tmp = {}
            bgp_as = conf['bgp_as']
            val = None
            if 'neighbors' in conf and 'neighbor' in conf['neighbors']:
                val = conf['neighbors']['neighbor']

            tmp['vrf_name'] = vrf_name
            tmp['bgp_as'] = bgp_as
            peergroup = get_peergroups(self._module, vrf_name)
            if peergroup:
                tmp['peer_group'] = peergroup
            fil_neighbors = []
            if val:
                for neighbor in val:
                    fil_neighbor = get_from_params_map(self.neighbor_params_map, neighbor)
                    capability = {}
                    capability_dynamic = fil_neighbor.get('dynamic', None)
                    if capability_dynamic is not None:
                        capability['dynamic'] = capability_dynamic
                        fil_neighbor.pop('dynamic')
                    capability_extended_nexthop = fil_neighbor.get('extended_nexthop', None)
                    if capability_extended_nexthop is not None:
                        capability['extended_nexthop'] = capability_extended_nexthop
                        fil_neighbor.pop('extended_nexthop')
                    if capability:
                        fil_neighbor['capability'] = capability
                    remote = {}
                    peer_as = fil_neighbor.get('peer_as', None)
                    if peer_as is not None:
                        remote['peer_as'] = peer_as
                        fil_neighbor.pop('peer_as')
                    peer_type = fil_neighbor.get('peer_type', None)
                    if peer_type is not None:
                        remote['peer_type'] = peer_type.lower()
                        fil_neighbor.pop('peer_type')
                    if remote:
                        fil_neighbor['remote_as'] = remote
                    auth_pwd = {}
                    pwd = fil_neighbor.get('pwd', None)
                    if pwd is not None:
                        auth_pwd['pwd'] = pwd
                        fil_neighbor.pop('pwd')
                    encrypted = fil_neighbor.get('encrypted', None)
                    if encrypted is not None:
                        auth_pwd['encrypted'] = encrypted
                        fil_neighbor.pop('encrypted')
                    if auth_pwd:
                        fil_neighbor['auth_pwd'] = auth_pwd
                    if fil_neighbor:
                        fil_neighbors.append(fil_neighbor)
            if fil_neighbors:
                tmp['neighbors'] = fil_neighbors
            filtered_data.append(tmp)
        return filtered_data
