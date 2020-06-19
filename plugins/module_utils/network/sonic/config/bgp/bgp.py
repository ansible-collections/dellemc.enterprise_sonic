#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_bgp class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from __future__ import absolute_import, division, print_function
__metaclass__ = type

import requests

try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
    search_obj_in_list,
    remove_empties
)
from ansible_collections.dellemc.sonic.plugins.module_utils.network.sonic.facts.facts import Facts

from ansible_collections.dellemc.sonic.plugins.module_utils.network.sonic.utils.utils import (
    dict_to_set,
    update_states,
    get_diff,
    remove_empties_from_list
)
from ansible_collections.dellemc.sonic.plugins.module_utils.network.sonic.sonic import to_request

PATCH = 'patch'
POST = 'post'
DELETE = 'delete'
PUT = 'put'


class Bgp(ConfigBase):
    """
    The sonic_bgp class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'bgp',
    ]

    global_params = ('bgp_as', 'router_id', 'log_neighbor_changes', 'vrf_name', 'neighbors')
    neighbor_params = ('neighbor', 'remote_as', 'update_source', 'password', 'enabled', 'description',
                       'ebgp_multihop', 'peer_group', 'timers', 'local_as', 'advertisement_interval')
    af_params = ('afi', 'safi', 'redistribute', 'networks', 'neighbors')

    network_instance_path = '/data/openconfig-network-instance:network-instances/network-instance'
    protocol_bgp_path = 'protocols/protocol=BGP,bgp/bgp'

    afi_safi_types_map = {
        'ipv4_unicast': 'openconfig-bgp-types:IPV4_UNICAST',
        'ipv6_unicast': 'openconfig-bgp-types:IPV6_UNICAST',
    }

    global_params_map = {
        'bgp_as': 'as',
        'router_id': 'router-id',
        'log_neighbor_changes': ['openconfig-bgp-ext:logging-options', 'log-neighbor-state-changes'],
        'peer_group_name': 'peer-group-name'
    }

    af_params_map = {
        'route_map': 'policy-name',
        'prefix': 'prefix',
        'neighbor': 'neighbor-address',
        'route_reflector_client': 'openconfig-bgp-ext:route-reflector-client',
        'route_server_client': 'openconfig-bgp-ext:route-server-client',
        'next_hop_self': ['openconfig-bgp-ext:next-hop-self', 'enabled'],
        'remove_private_as': ['openconfig-bgp-ext:remove-private-as', 'enabled'],
        'prefix_list_in': ['openconfig-bgp-ext:prefix-list', 'import-policy'],
        'prefix_list_out': ['openconfig-bgp-ext:prefix-list', 'export-policy'],
        'maximum_prefix': ['prefix-limit', 'max-prefixes'],
        'activate': 'enabled'
    }

    af_redistribute_params_map = {
        'protocol': ['dst-protocol', 'src-protocol'],
        'metric': 'openconfig-network-instance-ext:metric',
        'route_map': 'import-policy'
    }

    af_redistribute_types_map = {
        'openconfig-bgp-types:IPV4_UNICAST': 'openconfig-types:IPV4',
        'openconfig-bgp-types:IPV6_UNICAST': 'openconfig-types:IPV6'
    }

    af_redistribute_policy_types_map = {
        'bgp': 'openconfig-policy-types:BGP',
        'ospf': 'openconfig-policy-types:OSPF',
        'connected': 'openconfig-policy-types:DIRECTLY_CONNECTED',
        'static': 'openconfig-policy-types:STATIC',
    }

    neighbor_params_map = {
        'neighbor': 'neighbor-address',
        'remote_as': 'peer-as',
        'update_source': ['transport', 'local-address'],
        'password': ['openconfig-bgp-ext:auth-password', 'password'],
        'enabled': 'enabled',
        'description': 'description',
        'ebgp_multihop': ['ebgp-multihop', 'multihop-ttl'],
        'peer_group': 'peer-group',
        'timers': 'timers',
        'keepalive': 'keepalive-interval',
        'holdtime': 'hold-time',
        'local_as': 'local-as',
        'advertisement_interval': 'minimum-advertisement-interval'
    }

    def __init__(self, module):
        super(Bgp, self).__init__(module)

    def get_bgp_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        bgp_facts = facts['ansible_network_resources'].get('bgp')
        if not bgp_facts:
            return []
        return bgp_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = list()
        commands = list()
        requests = list()
        existing_bgp_facts = self.get_bgp_facts()
        commands, requests = self.set_config(existing_bgp_facts)
        if requests:
            if not self._module.check_mode:
                try:
                    self._connection.edit_config(to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        changed_bgp_facts = self.get_bgp_facts()

        result['before'] = existing_bgp_facts
        if result['changed']:
            result['after'] = changed_bgp_facts

        result['warnings'] = warnings
        return result

    def set_config(self, existing_bgp_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']
        have = existing_bgp_facts
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
        if state in ('overridden', 'merged', 'replaced') and not want:
            self._module.fail_json(msg='value of config parameter must not be empty for state {0}'.format(state))

        diff = get_diff(want, have, ['vrf_name', 'neighbor', 'peer_group_name', {'afi', 'safi'}, {'prefix', 'masklen'}, 'protocol'])
        if state == 'overridden':
            commands, requests = self._state_overridden(want, have, diff)
        elif state == 'deleted':
            commands, requests = self._state_deleted(want, have, diff)
        elif state == 'merged':
            commands, requests = self._state_merged(want, have, diff)
        elif state == 'replaced':
            commands, requests = self._state_replaced(want, have, diff)
        return commands, requests

    def _state_merged(self, want, have, diff):
        """ The command generator when state is merged

        :param want: the additive configuration as a dictionary
        :param obj_in_have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = []
        requests = []

        commands = update_states(diff, 'merged')
        requests = self.get_edit_bgp_requests(commands)

        return remove_empties_from_list(commands), requests

    def _state_deleted(self, want, have, diff):
        """ The command generator when state is deleted

        :param want: the objects from which the configuration should be removed
        :param obj_in_have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        commands = []
        requests = []
        if not want:
            commands = have
            requests = self.get_delete_bgp_requests(commands)
        else:
            for bgp_want in want:
                delete_item = search_obj_in_list(bgp_want['vrf_name'], have, 'vrf_name')
                if delete_item:
                    bgp_want = remove_empties(bgp_want)
                    commands.extend([bgp_want])
                if len(bgp_want.keys()) == 1 and bgp_want['vrf_name']:
                    requests.extend(self.get_delete_bgp_requests(commands))
                elif len(bgp_want.keys()) == 2 and all(key in bgp_want for key in ['bgp_as', 'vrf_name']):
                    requests.extend(self.get_delete_bgp_requests(commands))

        commands = update_states(commands, 'deleted')
        return remove_empties_from_list(commands), requests

    def build_bgp_peer_groups_payload(self, cmd):
        bgp_peer_group_list = []
        if 'peer_groups' in cmd and cmd['peer_groups']:
            for peer_group in cmd['peer_groups']:
                bgp_peer_group = {}
                peer_group_cfg = {}
                for key, val in peer_group.items():
                    for want_key, config_key in self.global_params_map.items():
                        if key == want_key and val:
                            peer_group_cfg.update({config_key: val})
                            bgp_peer_group.update({config_key: val})
                if peer_group_cfg:
                    bgp_peer_group.update({'config': peer_group_cfg})
                if bgp_peer_group:
                    bgp_peer_group_list.append(bgp_peer_group)
        payload = {'openconfig-network-instance:peer-groups': {'peer-group': bgp_peer_group_list}}
        return payload

    def build_bgp_neighbors_create_payload(self, cmd):
        bgp_neighbor_list = []
        if 'neighbors' in cmd and cmd['neighbors']:
            for neighbor in cmd['neighbors']:
                bgp_neighbor = {}
                neighbor_cfg = {}
                for key, val in neighbor.items():
                    for want_key, config_key in self.neighbor_params_map.items():
                        if key == 'neighbor' and (key == want_key and val):
                            bgp_neighbor.update({config_key: val})
                            neighbor_cfg.update({config_key: val})
                if neighbor_cfg:
                    bgp_neighbor.update({'config': neighbor_cfg})
                if bgp_neighbor:
                    bgp_neighbor_list.append(bgp_neighbor)
        payload = {'openconfig-network-instance:neighbors': {'neighbor': bgp_neighbor_list}}
        return payload

    def build_bgp_neighbors_payload(self, cmd):
        bgp_neighbor_list = []
        if 'neighbors' in cmd and cmd['neighbors']:
            for neighbor in cmd['neighbors']:
                bgp_neighbor = {}
                neighbor_cfg = {}
                tmp_timers = {}
                for key, val in neighbor.items():
                    for want_key, config_key in self.neighbor_params_map.items():
                        if key == want_key and val:
                            if isinstance(config_key, list):
                                bgp_neighbor.update({config_key[0]: {'config': {config_key[1]: val}}})
                            elif key == 'timers':
                                for want_k, want_v in val.items():
                                    for k, v in self.neighbor_params_map.items():
                                        if k == want_k:
                                            tmp_timers.update({v: str(want_v)})
                            elif key == 'advertisement_interval':
                                tmp_timers.update({config_key: str(val)})
                            elif key == 'neighbor':
                                bgp_neighbor.update({config_key: val})
                                neighbor_cfg.update({config_key: val})
                            else:
                                neighbor_cfg.update({config_key: val})
                if tmp_timers:
                    bgp_neighbor.update({'timers': {'config': tmp_timers}})
                if neighbor_cfg:
                    bgp_neighbor.update({'config': neighbor_cfg})

                if bgp_neighbor:
                    bgp_neighbor_list.append(bgp_neighbor)
        payload = {'openconfig-network-instance:neighbors': {'neighbor': bgp_neighbor_list}}
        return payload

    def build_bgp_af_payload(self, cmd):
        bgp_afi_safi_list = []
        for af in cmd['address_family']:
            bgp_afi_safis = {}
            bgp_afi_safis_nei = {}
            if all(key in af for key in ['afi', 'safi']):
                afi_safi_type = self.afi_safi_types_map[af['afi'] + '_' + af['safi']]
                bgp_afi_safis.update({'afi-safi-name': afi_safi_type})
                bgp_afi_safis.update({'config': {'afi-safi-name': afi_safi_type}})
            if 'networks' in af and af['networks']:
                bgp_afi_safis.update(self.build_bgp_af_ntw_payload(af))

            if bgp_afi_safis:
                bgp_afi_safi_list.extend([bgp_afi_safis])
        payload = {'openconfig-network-instance:afi-safis': {'afi-safi': bgp_afi_safi_list}}
        return payload

    def build_bgp_af_redis_payload(self, af):
        afi_redis_list = []
        payload = {}
        for af_redis in af['redistribute']:
            cfg = {}
            redis_cfg = {}

            afi_safi_type = self.afi_safi_types_map[af['afi'] + '_' + af['safi']]
            for want_key, config_key in self.af_redistribute_types_map.items():
                if want_key == afi_safi_type:
                    redis_type_key = config_key
                    break

            for key, val in af_redis.items():
                for want_key, config_key in self.af_redistribute_params_map.items():
                    if key == want_key and val:
                        if key == 'route_map':
                            cfg.update({config_key: [val]})
                        elif not key == 'protocol':
                            cfg.update({config_key: val})
                        else:
                            if isinstance(config_key, list):
                                for type_key, type_val in self.af_redistribute_policy_types_map.items():
                                    if type_key == val:
                                        redis_ptype_key = type_val
                                    if type_key == 'bgp':
                                        redis_bgp_ptype_key = type_val
                                redis_cfg.update({config_key[0]: redis_bgp_ptype_key})
                                redis_cfg.update({config_key[1]: redis_ptype_key})
            if redis_cfg and redis_type_key:
                redis_cfg.update({'address-family': redis_type_key})
                cfg.update({'address-family': redis_type_key})
                if cfg:
                    redis_cfg.update({'config': cfg})
                afi_redis_list.extend([redis_cfg])

        if afi_redis_list:
            payload = {'openconfig-network-instance:table-connections': {'table-connection': afi_redis_list}}
        return payload

    def build_bgp_af_nei_payload(self, af):
        afi_neighbor_list = []
        bgp_neighbor_list = []
        payload = {}
        for neighbor in af['neighbors']:
            cfg = {}
            neighbor_cfg = {}
            tmp_prefix_cfg = {}
            for key, val in neighbor.items():
                for want_key, config_key in self.af_params_map.items():
                    if key == want_key and val:
                        if isinstance(config_key, list):
                            if key == 'maximum_prefix':
                                tmp_key = af['afi'] + '-' + af['safi']
                                tmp_cfg = {tmp_key: {config_key[0]: {'config': {config_key[1]: val}}}}
                                neighbor_cfg.update(tmp_cfg)
                            elif key.startswith('prefix_list'):
                                tmp_prefix_cfg.update({config_key[1]: val})
                            else:
                                neighbor_cfg.update({config_key[0]: {'config': {config_key[1]: val}}})
                        elif not key == 'neighbor':
                            cfg.update({config_key: val})

            if cfg or neighbor_cfg or tmp_prefix_cfg:
                if all(key in af for key in ['afi', 'safi']):
                    afi_safi_type = self.afi_safi_types_map[af['afi'] + '_' + af['safi']]
                    neighbor_cfg.update({'afi-safi-name': afi_safi_type})
                if cfg:
                    neighbor_cfg.update({'config': cfg})
                if tmp_prefix_cfg:
                    neighbor_cfg.update({'openconfig-bgp-ext:prefix-list': {'config': tmp_prefix_cfg}})
                afi_neighbor_list.extend([neighbor_cfg])

            if afi_neighbor_list:
                af_nei_payload = {'afi-safis': {'afi-safi': afi_neighbor_list}}
                af_nei_payload.update({'neighbor-address': neighbor['neighbor']})
                bgp_neighbor_list.extend([af_nei_payload])

        if bgp_neighbor_list:
            payload = {'openconfig-network-instance:neighbors': {'neighbor': bgp_neighbor_list}}
        return payload

    def build_bgp_af_ntw_payload(self, af):
        bgp_afi_network_list = []
        payload = {}
        for network in af['networks']:
            cfg = {}
            network_cfg = {}
            for key, val in network.items():
                for want_key, config_key in self.af_params_map.items():
                    if key == 'prefix' and all(tmp_key in network for tmp_key in ['prefix', 'masklen']) and (key == want_key):
                        network_prefix = network['prefix'] + '/' + str(network['masklen'])
                        cfg.update({config_key: network_prefix})
                        network_cfg.update({config_key: network_prefix})
                    if key == 'route_map' and val and (key == want_key):
                        cfg.update({config_key: val})

            if cfg:
                network_cfg.update({'config': cfg})
                bgp_afi_network_list.extend([network_cfg])

        if bgp_afi_network_list:
            payload = {'openconfig-bgp-ext:network-config': {'network': bgp_afi_network_list}}
        return payload

    def build_bgp_globals_payload(self, cmd):
        bgp_globals = {}
        for key in cmd.keys():
            for want_key, config_key in self.global_params_map.items():
                if key in self.global_params and key == want_key:
                    if isinstance(config_key, list):
                        bgp_globals.update({config_key[0]: {'config': {config_key[1]: cmd[key]}}})
                    else:
                        bgp_globals.update({'config': {config_key: cmd[key]}})

        payload = {'openconfig-network-instance:global': bgp_globals}
        return payload

    def get_delete_bgp_requests(self, commands):
        requests = []
        for cmd in commands:
            if 'vrf_name' in cmd and cmd['vrf_name']:
                delete_path = '%s=%s/%s/global' % (self.network_instance_path, cmd['vrf_name'], self.protocol_bgp_path)
                requests.append({'path': delete_path, 'method': DELETE})
        return requests

    def get_delete_bgp_neighbor_requests(self, commands):
        requests = []
        for cmd in commands:
            if 'neighbors' in cmd and cmd['neighbors']:
                for neighbor in cmd['neighbors']:
                    delete_path = '%s=%s/%s/neighbors/neighbor=%s' % (self.network_instance_path, cmd['vrf_name'], self.protocol_bgp_path, neighbor['neighbor'])
                    requests.append({'path': delete_path, 'method': DELETE})
        return requests

    def get_delete_bgp_params_requests(self, commands):
        requests = []
        delete_path = '%s=%s/%s' % (self.network_instance_path, cmd['vrf_name'], self.protocol_bgp_path)
        for cmd in commands:
            # Neighbor Params
            if 'neighbors' in cmd and cmd['neighbors']:
                for neighbor in cmd['neighbors']:
                    delete_path = delete_path + '/neighbors/neighbor=%s' % (neighbor['neighbor'])
                    for key, val in neighbor.items():
                        tmp_path = list()
                        for want_key, config_key in self.params_map.items():
                            if key == want_key:
                                if isinstance(config_key, list):
                                    tmp_path.append('/' + config_key[0] + '/config/' + config_key[1])
                                    if key == 'timers':
                                        for want_k in val.keys():
                                            for k, v in self.params_map.items():
                                                if k == want_k:
                                                    tmp_path.append('/timers/config/' + v)
                                else:
                                    tmp_path.append('/config/' + config_key)
                        delete_path = delete_path + tmp_path
                        requests.extend([{'path': delete_path, 'method': DELETE}])
            # Global params
            else:
                delete_path = delete_path + '/global'
                for key in cmd.keys():
                    for want_key, config_key in self.params_map.items():
                        if key in self.global_params and key not in ['vrf_name', 'neighbors']:
                            tmp_path.append('/config/' + config_key)
        return requests

    def get_edit_bgp_requests(self, commands, method=PATCH):
        requests = []
        for cmd in commands:
            edit_path = '%s=%s/%s' % (self.network_instance_path, cmd['vrf_name'], self.protocol_bgp_path)
            base_path = '%s=%s' % (self.network_instance_path, cmd['vrf_name'])
            global_cmd = False

            for key in cmd:
                if key in self.global_params:
                    if key not in ['vrf_name', 'neighbors', 'peer_groups', 'address_family']:
                        global_cmd = True

            if global_cmd:
                edit_globals_payload = self.build_bgp_globals_payload(cmd)
                edit_globals_path = edit_path + '/global'
                requests.append({'path': edit_globals_path, 'method': method, 'data': edit_globals_payload})

            if 'peer_groups' in cmd and cmd['peer_groups']:
                edit_peer_groups_payload = self.build_bgp_peer_groups_payload(cmd)
                edit_peer_groups_path = edit_path + '/peer-groups'
                requests.append({'path': edit_peer_groups_path, 'method': method, 'data': edit_peer_groups_payload})

            if 'neighbors' in cmd and cmd['neighbors']:
                create_neighbors_payload = self.build_bgp_neighbors_create_payload(cmd)
                create_neighbors_path = edit_path + '/neighbors'
                requests.append({'path': create_neighbors_path, 'method': method, 'data': create_neighbors_payload})

                edit_neighbors_payload = self.build_bgp_neighbors_payload(cmd)
                edit_neighbors_path = edit_path + '/neighbors'
                requests.append({'path': edit_neighbors_path, 'method': method, 'data': edit_neighbors_payload})

            if 'address_family' in cmd and cmd['address_family']:
                edit_af_payload = self.build_bgp_af_payload(cmd)
                edit_af_path = edit_path + '/global/afi-safis'
                requests.append({'path': edit_af_path, 'method': method, 'data': edit_af_payload})
                for cmd_af in cmd['address_family']:
                    if 'redistribute' in cmd_af and cmd_af['redistribute']:
                        edit_redis_af_payload = self.build_bgp_af_redis_payload(cmd_af)
                        edit_redis_af_path = base_path + '/table-connections'
                        if edit_redis_af_payload:
                            requests.append({'path': edit_redis_af_path, 'method': method, 'data': edit_redis_af_payload})

                    if 'neighbors' in cmd_af and cmd_af['neighbors']:
                        edit_neighbors_af_payload = self.build_bgp_af_nei_payload(cmd_af)
                        edit_neighbors_af_path = edit_path + '/neighbors'
                        if edit_neighbors_af_payload:
                            requests.append({'path': edit_neighbors_af_path, 'method': method, 'data': edit_neighbors_af_payload})
        return requests
