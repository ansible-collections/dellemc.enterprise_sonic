#
# -*- coding: utf-8 -*-
# Copyright 2022 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_static_routes class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import Facts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    update_states,
    get_diff,
)

network_instance_path = '/data/openconfig-network-instance:network-instances/network-instance'
protocol_static_routes_path = 'protocols/protocol=STATIC,static/static-routes'

PATCH = 'patch'
DELETE = 'delete'
TEST_KEYS = [
    {'config': {'vrf_name': ''}},
    {'static_list': {'prefix': ''}},
    {'next_hops': {'index': ''}},
]


class Static_routes(ConfigBase):
    """
    The sonic_static_routes class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'static_routes',
    ]

    def __init__(self, module):
        super(Static_routes, self).__init__(module)

    def get_static_routes_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        static_routes_facts = facts['ansible_network_resources'].get('static_routes')
        if not static_routes_facts:
            return []
        return static_routes_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = []
        commands = []
        existing_static_routes_facts = self.get_static_routes_facts()
        commands, requests = self.set_config(existing_static_routes_facts)
        if commands and len(requests) > 0:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        changed_static_routes_facts = self.get_static_routes_facts()

        result['before'] = existing_static_routes_facts
        if result['changed']:
            result['after'] = changed_static_routes_facts

        result['warnings'] = warnings
        return result

    def set_config(self, existing_static_routes_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']
        have = existing_static_routes_facts
        resp = self.set_state(want, have)
        return to_list(resp)

    def set_state(self, want, have):
        """ Select the appropriate function based on the state provided

        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """

        commands = []
        requests = []
        state = self._module.params['state']

        diff = get_diff(want, have, TEST_KEYS)

        if state == 'deleted':
            commands, requests = self._state_deleted(want, have, diff)
        elif state == 'merged':
            commands, requests = self._state_merged(want, have, diff)
        return commands, requests

    def _state_merged(self, want, have, diff):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = diff
        requests = self.get_modify_static_routes_requests(commands, have)

        if commands and len(requests) > 0:
            commands = update_states(commands, "merged")
        else:
            commands = []

        return commands, requests

    def _state_deleted(self, want, have, diff):
        """ The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        is_delete_all = False
        # if want is none, then delete ALL
        if not want:
            commands = have
            is_delete_all = True
        else:
            commands = want

        requests = self.get_delete_static_routes_requests(commands, have, is_delete_all)

        if commands and len(requests) > 0:
            commands = update_states(commands, "deleted")
        else:
            commands = []

        return commands, requests

    def get_modify_static_routes_requests(self, commands, have):
        requests = []

        if not commands:
            return requests

        for conf in commands:
            vrf_name = conf.get('vrf_name', None)
            static_list = conf.get('static_list', [])
            for static in static_list:
                prefix = static.get('prefix', None)
                next_hops = static.get('next_hops', [])
                if next_hops:
                    for next_hop in next_hops:
                        requests.append(self.get_modify_static_route_request(vrf_name, prefix, next_hop))

        return requests

    def get_modify_static_route_request(self, vrf_name, prefix, next_hop):
        request = None
        next_hop_cfg = {}
        index = next_hop.get('index', {})
        blackhole = index.get('blackhole', None)
        interface = index.get('interface', None)
        nexthop_vrf = index.get('nexthop_vrf', None)
        next_hop_attr = index.get('next_hop', None)
        metric = next_hop.get('metric', None)
        track = next_hop.get('track', None)
        tag = next_hop.get('tag', None)
        idx = self.generate_index(index)
        if idx:
            next_hop_cfg['index'] = idx
            if blackhole:
                next_hop_cfg['blackhole'] = blackhole
            if nexthop_vrf:
                next_hop_cfg['network-instance'] = nexthop_vrf
            if next_hop:
                next_hop_cfg['next-hop'] = next_hop_attr
            if metric:
                next_hop_cfg['metric'] = metric
            if track:
                next_hop_cfg['track'] = track
            if tag:
                next_hop_cfg['tag'] = tag

        url = '%s=%s/%s' % (network_instance_path, vrf_name, protocol_static_routes_path)
        next_hops_cfg = {'next-hop': [{'index': idx, 'config': next_hop_cfg}]}
        if interface:
            next_hops_cfg['next-hop'][0]['interface-ref'] = {'config': {'interface': interface}}
        payload = {'openconfig-network-instance:static-routes': {'static': [{'prefix': prefix, 'config': {'prefix': prefix}, 'next-hops': next_hops_cfg}]}}
        request = {'path': url, 'method': PATCH, 'data': payload}

        return request

    def generate_index(self, index):
        idx = None
        blackhole = index.get('blackhole', None)
        interface = index.get('interface', None)
        nexthop_vrf = index.get('nexthop_vrf', None)
        next_hop = index.get('next_hop', None)

        if blackhole is True:
            idx = 'DROP'
        else:
            if interface:
                if not next_hop and not nexthop_vrf:
                    idx = interface
                elif next_hop and not nexthop_vrf:
                    idx = interface + '_' + next_hop
                elif nexthop_vrf and not next_hop:
                    idx = interface + '_' + nexthop_vrf
                else:
                    idx = interface + '_' + next_hop + '_' + nexthop_vrf
            else:
                if next_hop and not nexthop_vrf:
                    idx = next_hop
                elif next_hop and nexthop_vrf:
                    idx = next_hop + '_' + nexthop_vrf

        return idx

    def get_delete_static_routes_requests(self, commands, have, is_delete_all):
        requests = []
        if is_delete_all:
            for cmd in commands:
                vrf_name = cmd.get('vrf_name', None)
                if vrf_name:
                    requests.append(self.get_delete_static_routes_for_vrf(vrf_name))
        else:
            for cmd in commands:
                vrf_name = cmd.get('vrf_name', None)
                static_list = cmd.get('static_list', [])
                for cfg in have:
                    cfg_vrf_name = cfg.get('vrf_name', None)
                    if vrf_name == cfg_vrf_name:
                        if not static_list:
                            requests.append(self.get_delete_static_routes_for_vrf(vrf_name))
                        else:
                            for static in static_list:
                                prefix = static.get('prefix', None)
                                next_hops = static.get('next_hops', [])
                                cfg_static_list = cfg.get('static_list', [])
                                for cfg_static in cfg_static_list:
                                    cfg_prefix = cfg_static.get('prefix', None)
                                    if prefix == cfg_prefix:
                                        if prefix and not next_hops:
                                            requests.append(self.get_delete_static_routes_prefix_request(vrf_name, prefix))
                                        else:
                                            for next_hop in next_hops:
                                                index = next_hop.get('index', {})
                                                idx = self.generate_index(index)
                                                metric = next_hop.get('metric', None)
                                                track = next_hop.get('track', None)
                                                tag = next_hop.get('tag', None)

                                                cfg_next_hops = cfg_static.get('next_hops', [])
                                                if cfg_next_hops:
                                                    for cfg_next_hop in cfg_next_hops:
                                                        cfg_index = cfg_next_hop.get('index', {})
                                                        cfg_idx = self.generate_index(cfg_index)
                                                        if idx == cfg_idx:
                                                            cfg_metric = cfg_next_hop.get('metric', None)
                                                            cfg_track = cfg_next_hop.get('track', None)
                                                            cfg_tag = cfg_next_hop.get('tag', None)
                                                            if not metric and not track and not tag:
                                                                requests.append(self.get_delete_static_routes_next_hop_request(vrf_name, prefix, idx))
                                                            else:
                                                                if metric == cfg_metric:
                                                                    requests.append(self.get_delete_next_hop_config_attr_request(vrf_name, prefix, idx,
                                                                                                                                 'metric'))
                                                                if track == cfg_track:
                                                                    requests.append(self.get_delete_next_hop_config_attr_request(vrf_name, prefix, idx,
                                                                                                                                 'track'))
                                                                if tag == cfg_tag:
                                                                    requests.append(self.get_delete_next_hop_config_attr_request(vrf_name, prefix, idx, 'tag'))

        return requests

    def get_delete_static_routes_for_vrf(self, vrf_name):
        url = '%s=%s/%s' % (network_instance_path, vrf_name, protocol_static_routes_path)
        request = {'path': url, 'method': DELETE}

        return request

    def get_delete_static_routes_prefix_request(self, vrf_name, prefix):
        prefix = prefix.replace('/', '%2F')
        url = '%s=%s/%s/static=%s' % (network_instance_path, vrf_name, protocol_static_routes_path, prefix)
        request = {'path': url, 'method': DELETE}

        return request

    def get_delete_static_routes_next_hop_request(self, vrf_name, prefix, index):
        prefix = prefix.replace('/', '%2F')
        url = '%s=%s/%s/static=%s' % (network_instance_path, vrf_name, protocol_static_routes_path, prefix)
        url += '/next-hops/next-hop=%s' % (index)
        request = {'path': url, 'method': DELETE}

        return request

    def get_delete_next_hop_config_attr_request(self, vrf_name, prefix, index, attr):
        prefix = prefix.replace('/', '%2F')
        url = '%s=%s/%s/static=%s' % (network_instance_path, vrf_name, protocol_static_routes_path, prefix)
        url += '/next-hops/next-hop=%s/config/%s' % (index, attr)
        request = {'path': url, 'method': DELETE}

        return request
