#
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic qos_maps fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from copy import deepcopy

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible.module_utils.connection import ConnectionError
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    remove_empties
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.qos_maps.qos_maps import Qos_mapsArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)

QOS_PATH = '/data/openconfig-qos:qos/'

OC_MAP_DATA = [
    {
        'map': 'dscp-map',
        'attr1': 'dscp',
        'attr2': 'fwd-group'
    },
    {
        'map': 'dot1p-map',
        'attr1': 'dot1p',
        'attr2': 'fwd-group'
    },
    {
        'map': 'forwarding-group-queue-map',
        'attr1': 'fwd-group',
        'attr2': 'output-queue-index'
    },
    {
        'map': 'forwarding-group-dscp-map',
        'attr1': 'fwd-group',
        'attr2': 'dscp'
    },
    {
        'map': 'forwarding-group-dot1p-map',
        'attr1': 'fwd-group',
        'attr2': 'dot1p'
    },
    {
        'map': 'forwarding-group-priority-group-map',
        'attr1': 'fwd-group',
        'attr2': 'priority-group-index'
    },
    {
        'map': 'pfc-priority-queue-map',
        'attr1': 'dot1p',
        'attr2': 'output-queue-index'
    },
    {
        'map': 'pfc-priority-priority-group-map',
        'attr1': 'dot1p',
        'attr2': 'priority-group-index'
    }
]

ANS_ATTR_MAP = {
    'dot1p': 'dot1p',
    'dot1p-map': 'dot1p_maps',
    'dscp': 'dscp',
    'dscp-map': 'dscp_maps',
    'forwarding-group-dot1p-map': 'fwd_group_dot1p_maps',
    'forwarding-group-dscp-map': 'fwd_group_dscp_maps',
    'forwarding-group-priority-group-map': 'fwd_group_pg_maps',
    'forwarding-group-queue-map': 'fwd_group_queue_maps',
    'fwd-group': 'fwd_group',
    'output-queue-index': 'queue_index',
    'pfc-priority-priority-group-map': 'pfc_priority_pg_maps',
    'pfc-priority-queue-map': 'pfc_priority_queue_maps',
    'priority-group-index': 'pg_index'
}


class Qos_mapsFacts(object):
    """ The sonic qos_maps fact class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = Qos_mapsArgs.argument_spec
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
        """ Populate the facts for qos_maps
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        if not data:
            data = self.render_config(self._module)
        facts = {}
        if data:
            params = utils.validate_config(self.argument_spec, {'config': data})
            facts['qos_maps'] = remove_empties(params['config'])
        ansible_facts['ansible_network_resources'].update(facts)
        return ansible_facts

    def render_config(self, module):
        """Transform OC data to argspec format"""
        config_dict = {}

        for map_dict in OC_MAP_DATA:
            oc_map_name = map_dict['map']
            oc_map_list = self.get_config(module, oc_map_name)

            if oc_map_list:
                config_maps_list = []
                for oc_map_dict in oc_map_list:
                    config_maps_dict = {'name': oc_map_dict['name']}
                    oc_entries_name = f'{oc_map_name}-entries'
                    oc_entries_dict = oc_map_dict.get(oc_entries_name)

                    if oc_entries_dict:
                        oc_entry_name = f'{oc_map_name}-entry'
                        oc_entry_list = oc_entries_dict.get(oc_entry_name)

                        if oc_entry_list:
                            config_entries_list = []
                            for oc_entry_dict in oc_entry_list:
                                config_entries_dict = {}
                                attr1 = map_dict['attr1']
                                attr2 = map_dict['attr2']
                                val1 = oc_entry_dict['config'].get(attr1)
                                val2 = oc_entry_dict['config'].get(attr2)

                                if val1 is not None:
                                    config_entries_dict[ANS_ATTR_MAP[attr1]] = val1
                                if val2 is not None:
                                    config_entries_dict[ANS_ATTR_MAP[attr2]] = val2
                                if config_entries_dict:
                                    config_entries_list.append(config_entries_dict)

                            if config_entries_list:
                                config_maps_dict['entries'] = config_entries_list
                    if config_maps_dict:
                        config_maps_list.append(config_maps_dict)
                if config_maps_list:
                    config_dict[ANS_ATTR_MAP[oc_map_name]] = config_maps_list

        return config_dict

    def get_config(self, module, map_name):
        """Gets the list of configurations for the specified QoS map if present"""
        cfg = None
        get_path = f'{QOS_PATH}openconfig-qos-maps-ext:{map_name}s/{map_name}'
        request = {'path': get_path, 'method': 'get'}
        map_list_name = f'openconfig-qos-maps-ext:{map_name}'

        try:
            response = edit_config(module, to_request(module, request))
            if map_list_name in response[0][1]:
                cfg = response[0][1].get(map_list_name)
        except ConnectionError as exc:
            module.fail_json(msg=str(exc), code=exc.code)

        return cfg
