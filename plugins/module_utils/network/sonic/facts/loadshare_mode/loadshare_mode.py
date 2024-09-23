#
# -*- coding: utf-8 -*-
# Copyright 2024 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic IP ECMP load share mode fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from copy import deepcopy

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    remove_empties
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.loadshare_mode.loadshare_mode import Loadshare_modeArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible.module_utils.connection import ConnectionError

GET = "get"

LOADSHARE_MODE_ATTR_MAP = [
    {
        'ans_attr': 'hash_algorithm',
        'cfg_attr': 'hash-algorithm',
        'cfg_subattr': 'algorithm'
    },
    {
        'hash': {'hash': 'hash'},
        'ans_attr': 'hash_ingress_port',
        'cfg_attr': 'ingress-port',
        'cfg_subattr': 'ingress-port'
    },
    {
        'hash': {'hash': 'hash'},
        'ans_attr': 'hash_roce_qpn',
        'cfg_attr': 'roce-attrs',
        'cfg_subattr': 'qpn'
    },
    {
        'hash': {'hash': 'hash'},
        'ans_attr': 'hash_seed',
        'cfg_attr': 'seed-attrs',
        'cfg_subattr': 'ecmp-hash-seed'
    }
]

LOADSHARE_MODE_DICT_MAP = [
    {
        'hash': {'hash': 'hash'},
        'ans_attr': 'hash_offset',
        'cfg_attr': 'offset-attrs',
        'delete_op': 'DELETE',
        'map_subattrs': [
            {
                'ans_attr': 'offset',
                'cfg_attr': 'ecmp-hash-offset'
            },
            {
                'ans_attr': 'flow_based',
                'cfg_attr': 'ecmp-hash-flow-based'
            }
        ]
    },
    {
        'hash': {'ipv4': 'ipv4'},
        'ans_attr': 'ipv4',
        'cfg_attr': 'ipv4-attrs',
        'delete_op': 'PATCH',
        'map_subattrs': [
            {
                'ans_attr': 'ipv4_dst_ip',
                'cfg_attr': 'ipv4-dst-ip',
                'dft_value': False
            },
            {
                'ans_attr': 'ipv4_src_ip',
                'cfg_attr': 'ipv4-src-ip',
                'dft_value': False
            },
            {
                'ans_attr': 'ipv4_ip_proto',
                'cfg_attr': 'ipv4-ip-proto',
                'dft_value': False
            },
            {
                'ans_attr': 'ipv4_l4_dst_port',
                'cfg_attr': 'ipv4-l4-dst-port',
                'dft_value': False
            },
            {
                'ans_attr': 'ipv4_l4_src_port',
                'cfg_attr': 'ipv4-l4-src-port',
                'dft_value': False
            },
            {
                'ans_attr': 'ipv4_symmetric',
                'cfg_attr': 'ipv4-symmetric',
                'dft_value': False
            }
        ]
    },
    {
        'hash': {'ipv6': 'ipv6'},
        'ans_attr': 'ipv6',
        'cfg_attr': 'ipv6-attrs',
        'delete_op': 'PATCH',
        'map_subattrs': [
            {
                'ans_attr': 'ipv6_dst_ip',
                'cfg_attr': 'ipv6-dst-ip',
                'dft_value': False
            },
            {
                'ans_attr': 'ipv6_src_ip',
                'cfg_attr': 'ipv6-src-ip',
                'dft_value': False
            },
            {
                'ans_attr': 'ipv6_next_hdr',
                'cfg_attr': 'ipv6-next-hdr',
                'dft_value': False
            },
            {
                'ans_attr': 'ipv6_l4_dst_port',
                'cfg_attr': 'ipv6-l4-dst-port',
                'dft_value': False
            },
            {
                'ans_attr': 'ipv6_l4_src_port',
                'cfg_attr': 'ipv6-l4-src-port',
                'dft_value': False
            },
            {
                'ans_attr': 'ipv6_symmetric',
                'cfg_attr': 'ipv6-symmetric',
                'dft_value': False
            }
        ]
    }
]


class Loadshare_modeFacts(object):
    """ The sonic loadshare_mode fact class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = Loadshare_modeArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)

    def get_loadshare_mode_config(self):
        """Get all IP ECMP load share mode configuration in chassis"""
        request = [{"path": "data/openconfig-loadshare-mode-ext:loadshare", "method": GET}]
        try:
            response = edit_config(self._module, to_request(self._module, request))
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)
        if ('openconfig-loadshare-mode-ext:loadshare' in response[0][1]):
            data = response[0][1]['openconfig-loadshare-mode-ext:loadshare']
        else:
            data = {}

        return data

    def populate_facts(self, connection, ansible_facts, data=None):
        """ Populate the facts for mirroring
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        if not data:
            data = self.get_loadshare_mode_config()

        if data:
            loadshare_mode_facts = self.get_loadshare_mode_facts(data)
        else:
            loadshare_mode_facts = {}

        obj = self.render_config(self.generated_spec, loadshare_mode_facts)

        ansible_facts['ansible_network_resources'].pop('loadshare_mode', None)
        facts = {}
        if obj:
            params = utils.validate_config(self.argument_spec, {'config': obj})
            facts['loadshare_mode'] = params['config']

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

    def get_loadshare_mode_facts(self, config):

        lsm_facts = dict()

        for amap in LOADSHARE_MODE_ATTR_MAP:
            ans_attr = amap['ans_attr']
            cfg_attr = amap['cfg_attr']
            cfg_subattr = amap['cfg_subattr']
            lsm_facts[ans_attr] = (config.get(cfg_attr, {})
                                         .get('config', {})
                                         .get(cfg_subattr, None))

        for amap in LOADSHARE_MODE_DICT_MAP:
            ans_attr = amap['ans_attr']
            cfg_attr = amap['cfg_attr']

            amap_subattrs = amap['map_subattrs']
            lsm_subfacts = dict()
            for sub_amap in amap_subattrs:
                ans_subattr = sub_amap['ans_attr']
                cfg_subattr = sub_amap['cfg_attr']
                lsm_subfacts[ans_subattr] = (config.get(cfg_attr, {})
                                                   .get('config', {})
                                                   .get(cfg_subattr, None))
            lsm_facts[ans_attr] = lsm_subfacts

        loadshare_mode_facts = remove_empties(lsm_facts)
        return loadshare_mode_facts
