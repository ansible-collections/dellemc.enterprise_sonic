#
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic fbs_groups fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from __future__ import absolute_import, division, print_function
__metaclass__ = type

from copy import deepcopy
from ansible.module_utils.connection import ConnectionError
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    remove_empties
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.fbs_groups.fbs_groups import Fbs_groupsArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)


enum_dict = {
    'openconfig-fbs-ext:NEXT_HOP_GROUP_TYPE_IPV4': 'ipv4',
    'openconfig-fbs-ext:NEXT_HOP_GROUP_TYPE_IPV6': 'ipv6',
    'openconfig-fbs-ext:NEXT_HOP_TYPE_NON_RECURSIVE': 'non_recursive',
    'openconfig-fbs-ext:NEXT_HOP_TYPE_OVERLAY': 'overlay',
    'openconfig-fbs-ext:NEXT_HOP_TYPE_RECURSIVE': 'recursive',
    'openconfig-fbs-ext:REPLICATION_GROUP_TYPE_IPV4': 'ipv4',
    'openconfig-fbs-ext:REPLICATION_GROUP_TYPE_IPV6': 'ipv6'
}


class Fbs_groupsFacts(object):
    """ The sonic fbs_groups fact class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = Fbs_groupsArgs.argument_spec
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
        """ Populate the facts for fbs_groups
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        objs = []

        if not data:
            cfg = self.get_config(self._module)
            data = self.update_fbs_groups(cfg)
        objs = data
        facts = {}
        if objs:
            params = utils.validate_config(self.argument_spec, {'config': objs})
            facts['fbs_groups'] = remove_empties(params['config'])
        ansible_facts['ansible_network_resources'].update(facts)
        return ansible_facts

    def get_config(self, module):
        cfg = None
        get_path = 'data/openconfig-fbs-ext:fbs'
        request = {'path': get_path, 'method': 'get'}

        try:
            response = edit_config(module, to_request(module, request))
            if 'openconfig-fbs-ext:fbs' in response[0][1]:
                cfg = response[0][1].get('openconfig-fbs-ext:fbs')
        except ConnectionError as exc:
            module.fail_json(msg=str(exc), code=exc.code)

        return cfg

    def update_fbs_groups(self, cfg):
        config_dict = {}

        if cfg:
            if 'next-hop-groups' in cfg and 'next-hop-group' in cfg['next-hop-groups']:
                next_hop_group = cfg['next-hop-groups']['next-hop-group']
                next_hop_groups_list = self.get_groups_list(next_hop_group)

                if next_hop_groups_list:
                    config_dict['next_hop_groups'] = next_hop_groups_list

            if 'replication-groups' in cfg and 'replication-group' in cfg['replication-groups']:
                replication_group = cfg['replication-groups']['replication-group']
                replication_groups_list = self.get_groups_list(replication_group, True)

                if replication_groups_list:
                    config_dict['replication_groups'] = replication_groups_list

        return config_dict

    def get_groups_list(self, group_cfg, is_replication=False):
        groups_list = []

        for group in group_cfg:
            group_dict = {}
            group_name = group.get('group-name')
            config = group.get('config')
            next_hops = group.get('next-hops')

            if group_name:
                group_dict['group_name'] = group_name
            if config:
                group_description = config.get('description')
                group_type = config.get('group-type')

                if group_description:
                    group_dict['group_description'] = group_description
                if group_type:
                    group_dict['group_type'] = enum_dict[group_type]
            if next_hops:
                next_hop = next_hops.get('next-hop')
                if next_hop:
                    next_hops_list = []
                    for hop in next_hop:
                        hop_dict = {}
                        entry_id = hop.get('entry-id')
                        config = hop.get('config')

                        if entry_id:
                            hop_dict['entry_id'] = entry_id
                        if config:
                            ip_address = config.get('ip-address')
                            network_instance = config.get('network-instance')
                            next_hop_type = config.get('next-hop-type')
                            single_copy = config.get('single-copy')

                            if ip_address:
                                hop_dict['ip_address'] = ip_address
                            if network_instance:
                                hop_dict['network_instance'] = network_instance
                            if next_hop_type:
                                hop_dict['next_hop_type'] = enum_dict[next_hop_type]
                            if single_copy:
                                hop_dict['single_copy'] = single_copy
                        if hop_dict:
                            next_hops_list.append(hop_dict)
                    if next_hops_list:
                        group_dict['next_hops'] = next_hops_list
            if group_dict:
                groups_list.append(group_dict)

        return groups_list
