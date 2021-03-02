#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_bgp_neighbors class
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
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.bgp_utils import (
    validate_bgps,
    normalize_neighbors_interface_name,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import to_request
from ansible.module_utils.connection import ConnectionError

PATCH = 'patch'
DELETE = 'delete'

TEST_KEYS = [
    {'config': {'vrf_name': '', 'bgp_as': ''}},
    {'neighbors': {'neighbor': ''}},
    {'peer_group': {'name': ''}},
    {'afis': {'afi': '', 'safi': ''}},
]


class Bgp_neighbors(ConfigBase):
    """
    The sonic_bgp_neighbors class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'bgp_neighbors',
    ]

    network_instance_path = '/data/openconfig-network-instance:network-instances/network-instance'
    protocol_bgp_path = 'protocols/protocol=BGP,bgp/bgp'
    neighbor_path = 'neighbors/neighbor'

    def __init__(self, module):
        super(Bgp_neighbors, self).__init__(module)

    def get_bgp_neighbors_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        bgp_facts = facts['ansible_network_resources'].get('bgp_neighbors')
        if not bgp_facts:
            bgp_facts = []
        return bgp_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = list()
        existing_bgp_facts = self.get_bgp_neighbors_facts()
        commands, requests = self.set_config(existing_bgp_facts)
        if commands and len(requests) > 0:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        changed_bgp_facts = self.get_bgp_neighbors_facts()

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
        normalize_neighbors_interface_name(want, self._module)
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

        diff = get_diff(want, have, TEST_KEYS)

        if state == 'deleted':
            commands, requests = self._state_deleted(want, have, diff)
        elif state == 'merged':
            commands, requests = self._state_merged(want, have, diff)
        return commands, requests

    def _state_merged(self, want, have, diff):
        """ The command generator when state is merged

        :param want: the additive configuration as a dictionary
        :param have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = []
        requests = []
        commands = diff
        validate_bgps(self._module, commands, have)
        requests = self.get_modify_bgp_requests(commands, have)
        if commands and len(requests) > 0:
            commands = update_states(commands, "merged")
        else:
            commands = []
        return commands, requests

    def _state_deleted(self, want, have, diff):
        """ The command generator when state is deleted

        :param want: the objects from which the configuration should be removed
        :param have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        is_delete_all = False
        if not want:
            is_delete_all = True
        if is_delete_all:
            commands = have
            new_have = have
        else:
            new_have = self.remove_default_entries(have)
            d_diff = get_diff(want, new_have, TEST_KEYS, is_skeleton=True)
            delete_diff = get_diff(want, d_diff, TEST_KEYS, is_skeleton=True)
            commands = delete_diff
        requests = self.get_delete_bgp_neighbor_requests(commands, new_have, want, is_delete_all)

        if commands and len(requests) > 0:
            commands = update_states(commands, "deleted")
        else:
            commands = []
        return commands, requests

    def remove_default_entries(self, data):
        new_data = []
        if not data:
            return new_data
        for conf in data:
            new_conf = {}
            as_val = conf['bgp_as']
            vrf_name = conf['vrf_name']
            new_conf['bgp_as'] = as_val
            new_conf['vrf_name'] = vrf_name
            peergroup = conf.get('peer_group', None)
            new_peergroups = []
            if peergroup is not None:
                for pg in peergroup:
                    new_pg = {}
                    pg_val = pg.get('name', None)
                    new_pg['name'] = pg_val
                    remote_as = pg.get('remote_as', None)
                    new_remote = {}
                    if remote_as:
                        peer_as = remote_as.get('peer_as', None)
                        peer_type = remote_as.get('peer_type', None)
                        if peer_as is not None:
                            new_remote['peer_as'] = peer_as
                        if peer_type is not None:
                            new_remote['peer_type'] = peer_type
                    if new_remote:
                        new_pg['remote_as'] = new_remote
                    timers = pg.get('timers', None)
                    new_timers = {}
                    if timers:
                        keepalive = timers.get('keepalive', None)
                        holdtime = timers.get('holdtime', None)
                        if keepalive is not None and keepalive != 60:
                            new_timers['keepalive'] = keepalive
                        if holdtime is not None and holdtime != 180:
                            new_timers['holdtime'] = holdtime
                    if new_timers:
                        new_pg['timers'] = new_timers
                    advertisement_interval = pg.get('advertisement_interval', None)
                    if advertisement_interval is not None and advertisement_interval != 30:
                        new_pg['advertisement_interval'] = advertisement_interval
                    bfd = pg.get('bfd', None)
                    if bfd is not None:
                        new_pg['bfd'] = bfd
                    capability = pg.get('capability', None)
                    if capability is not None:
                        new_pg['capability'] = capability
                    afi = []
                    address_family = pg.get('address_family', None)
                    if address_family:
                        if address_family.get('afis', None):
                            for each in address_family['afis']:
                                if each:
                                    tmp = {}
                                    if each.get('afi', None) is not None:
                                        tmp['afi'] = each['afi']
                                    if each.get('safi', None) is not None:
                                        tmp['safi'] = each['safi']
                                    if each.get('activate', None) is not None and each['activate'] is not False:
                                        tmp['activate'] = each['activate']
                                    if each.get('allowas_in', None) is not None:
                                        tmp['allowas_in'] = each['allowas_in']
                                afi.append(tmp)
                            if afi and len(afi) > 0:
                                afis = {}
                                afis.update({'afis': afi})
                                new_pg['address_family'] = afis
                    if new_pg:
                        new_peergroups.append(new_pg)
            if new_peergroups:
                new_conf['peer_group'] = new_peergroups
            neighbors = conf.get('neighbors', None)
            new_neighbors = []
            if neighbors is not None:
                for neighbor in neighbors:
                    new_neighbor = {}
                    neighbor_val = neighbor.get('neighbor', None)
                    new_neighbor['neighbor'] = neighbor_val
                    remote_as = neighbor.get('remote_as', None)
                    new_remote = {}
                    if remote_as:
                        peer_as = remote_as.get('peer_as', None)
                        peer_type = remote_as.get('peer_type', None)
                        if peer_as is not None:
                            new_remote['peer_as'] = peer_as
                        if peer_type is not None:
                            new_remote['peer_type'] = peer_type
                    if new_remote:
                        new_neighbor['remote_as'] = new_remote
                    peer_group = neighbor.get('peer_group', None)
                    if peer_group:
                        new_neighbor['peer_group'] = peer_group
                    timers = neighbor.get('timers', None)
                    new_timers = {}
                    if timers:
                        keepalive = timers.get('keepalive', None)
                        holdtime = timers.get('holdtime', None)
                        if keepalive is not None and keepalive != 60:
                            new_timers['keepalive'] = keepalive
                        if holdtime is not None and holdtime != 180:
                            new_timers['holdtime'] = holdtime
                    if new_timers:
                        new_neighbor['timers'] = new_timers
                    advertisement_interval = neighbor.get('advertisement_interval', None)
                    if advertisement_interval is not None and advertisement_interval != 30:
                        new_neighbor['advertisement_interval'] = advertisement_interval
                    bfd = neighbor.get('bfd', None)
                    if bfd is not None:
                        new_neighbor['bfd'] = bfd
                    capability = neighbor.get('capability', None)
                    if capability is not None:
                        new_neighbor['capability'] = capability
                    if new_neighbor:
                        new_neighbors.append(new_neighbor)
            if new_neighbors:
                new_conf['neighbors'] = new_neighbors
            if new_conf:
                new_data.append(new_conf)
        return new_data

    def build_bgp_peer_groups_payload(self, cmd, have, bgp_as, vrf_name):
        requests = []
        bgp_peer_group_list = []
        for peer_group in cmd:
            if peer_group:
                bgp_peer_group = {}
                peer_group_cfg = {}
                tmp_timers = {}
                tmp_capability = {}
                tmp_remote = {}
                afi = []
                if peer_group.get('name', None) is not None:
                    peer_group_cfg.update({'peer-group-name': peer_group['name']})
                    bgp_peer_group.update({'peer-group-name': peer_group['name']})
                if peer_group.get('bfd', None) is not None:
                    bgp_peer_group.update({'openconfig-bfd:enable-bfd': {'config': {'enabled': peer_group['bfd']}}})
                if peer_group.get('timers', None) is not None:
                    if peer_group['timers'].get('holdtime', None) is not None:
                        tmp_timers.update({'hold-time': str(peer_group['timers']['holdtime'])})
                    if peer_group['timers'].get('keepalive', None) is not None:
                        tmp_timers.update({'keepalive-interval': str(peer_group['timers']['keepalive'])})
                if peer_group.get('capability', None) is not None:
                    if peer_group['capability'].get('dynamic', None) is not None:
                        tmp_capability.update({'openconfig-bgp-ext:capability-dynamic': peer_group['capability']['dynamic']})
                    if peer_group['capability'].get('extended_nexthop', None) is not None:
                        tmp_capability.update({'openconfig-bgp-ext:capability-extended-nexthop': peer_group['capability']['extended_nexthop']})
                if peer_group.get('advertisement_interval', None) is not None:
                    tmp_timers.update({'minimum-advertisement-interval': str(peer_group['advertisement_interval'])})
                if peer_group.get('remote_as', None) is not None:
                    have_nei = self.find_pg(have, bgp_as, vrf_name, peer_group)
                    if peer_group['remote_as'].get('peer_as', None) is not None:
                        if have_nei:
                            if have_nei.get("remote_as", None) is not None:
                                if have_nei["remote_as"].get("peer_type", None) is not None:
                                    del_nei = {}
                                    del_nei.update({'name': have_nei['name']})
                                    del_nei.update({'remote_as': have_nei['remote_as']})
                                    requests.extend(self.delete_specific_peergroup_param_request(vrf_name, del_nei))
                        tmp_remote.update({'peer-as': peer_group['remote_as']['peer_as']})
                    if peer_group['remote_as'].get('peer_type', None) is not None:
                        if have_nei:
                            if have_nei.get("remote_as", None) is not None:
                                if have_nei["remote_as"].get("peer_as", None) is not None:
                                    del_nei = {}
                                    del_nei.update({'name': have_nei['name']})
                                    del_nei.update({'remote_as': have_nei['remote_as']})
                                    requests.extend(self.delete_specific_peergroup_param_request(vrf_name, del_nei))
                        tmp_remote.update({'peer-type': peer_group['remote_as']['peer_type'].upper()})
                if peer_group.get('address_family', None) is not None:
                    if peer_group['address_family'].get('afis', None) is not None:
                        for each in peer_group['address_family']['afis']:
                            samp = {}
                            if each.get('afi', None) is not None and each.get('safi', None) is not None:
                                afi_safi = each['afi'].upper() + "_" + each['safi'].upper()
                                if afi_safi is not None:
                                    afi_safi_name = 'openconfig-bgp-types:' + afi_safi
                                if afi_safi_name is not None:
                                    samp.update({'afi-safi-name': afi_safi_name})
                                    samp.update({'config': {'afi-safi-name': afi_safi_name}})
                            if each.get('activate', None) is not None:
                                enabled = each['activate']
                                if enabled is not None:
                                    samp.update({'config': {'enabled': enabled}})
                            if each.get('allowas_in', None) is not None:
                                have_pg_af = self.find_af(have, bgp_as, vrf_name, peer_group, each['afi'], each['safi'])
                                if each['allowas_in'].get('origin', None) is not None:
                                    if have_pg_af:
                                        if have_pg_af.get('allowas_in', None) is not None:
                                            if have_pg_af['allowas_in'].get('value', None) is not None:
                                                del_nei = {}
                                                del_nei.update({'name': peer_group['name']})
                                                afis_list = []
                                                temp_cfg = {'afi': each['afi'], 'safi': each['safi']}
                                                temp_cfg['allowas_in'] = {'value': have_pg_af['allowas_in']['value']}
                                                afis_list.append(temp_cfg)
                                                del_nei.update({'address_family': {'afis': afis_list}})
                                                requests.extend(self.delete_specific_peergroup_param_request(vrf_name, del_nei))
                                    origin = each['allowas_in']['origin']
                                    samp.update({'openconfig-bgp-ext:allow-own-as': {'config': {'origin': origin, "enabled": bool("true")}}})
                                if each['allowas_in'].get('value', None) is not None:
                                    if have_pg_af:
                                        if have_pg_af.get('allowas_in', None) is not None:
                                            if have_pg_af['allowas_in'].get('origin', None) is not None:
                                                del_nei = {}
                                                del_nei.update({'name': peer_group['name']})
                                                afis_list = []
                                                temp_cfg = {'afi': each['afi'], 'safi': each['safi']}
                                                temp_cfg['allowas_in'] = {'origin': have_pg_af['allowas_in']['origin']}
                                                afis_list.append(temp_cfg)
                                                del_nei.update({'address_family': {'afis': afis_list}})
                                                requests.extend(self.delete_specific_peergroup_param_request(vrf_name, del_nei))
                                    as_count = each['allowas_in']['value']
                                    samp.update({'openconfig-bgp-ext:allow-own-as': {'config': {'as-count': as_count, "enabled": bool("true")}}})
                            if samp:
                                afi.append(samp)
                if tmp_timers:
                    bgp_peer_group.update({'timers': {'config': tmp_timers}})
                if afi and len(afi) > 0:
                    bgp_peer_group.update({'afi-safis': {'afi-safi': afi}})
                if tmp_capability:
                    peer_group_cfg.update(tmp_capability)
                if tmp_remote:
                    peer_group_cfg.update(tmp_remote)
                if peer_group_cfg:
                    bgp_peer_group.update({'config': peer_group_cfg})
                if bgp_peer_group:
                    bgp_peer_group_list.append(bgp_peer_group)
        payload = {'openconfig-network-instance:peer-groups': {'peer-group': bgp_peer_group_list}}
        return payload, requests

    def find_pg(self, have, bgp_as, vrf_name, peergroup):
        mat_dict = next((m_peer for m_peer in have if m_peer['bgp_as'] == bgp_as and m_peer['vrf_name'] == vrf_name), None)
        if mat_dict and mat_dict.get("peer_group", None) is not None:
            mat_pg = next((m for m in mat_dict['peer_group'] if m["name"] == peergroup['name']), None)
            return mat_pg

    def find_af(self, have, bgp_as, vrf_name, peergroup, afi, safi):
        mat_pg = self.find_pg(have, bgp_as, vrf_name, peergroup)
        if mat_pg and mat_pg['address_family'].get('afis', None) is not None:
            mat_af = next((af for af in mat_pg['address_family']['afis'] if af['afi'] == afi and af['safi'] == safi), None)
            return mat_af

    def find_nei(self, have, bgp_as, vrf_name, neighbor):
        mat_dict = next((m_neighbor for m_neighbor in have if m_neighbor['bgp_as'] == bgp_as and m_neighbor['vrf_name'] == vrf_name), None)
        if mat_dict and mat_dict.get("neighbors", None) is not None:
            mat_neighbor = next((m for m in mat_dict['neighbors'] if m["neighbor"] == neighbor['neighbor']), None)
            return mat_neighbor

    def build_bgp_neighbors_payload(self, cmd, have, bgp_as, vrf_name):
        bgp_neighbor_list = []
        requests = []
        for neighbor in cmd:
            if neighbor:
                bgp_neighbor = {}
                neighbor_cfg = {}
                tmp_timers = {}
                tmp_capability = {}
                tmp_remote = {}
                if neighbor.get('bfd', None) is not None:
                    bgp_neighbor.update({'openconfig-bfd:enable-bfd': {'config': {'enabled': neighbor['bfd']}}})
                if neighbor.get('timers', None) is not None:
                    if neighbor['timers'].get('holdtime', None) is not None:
                        tmp_timers.update({'hold-time': str(neighbor['timers']['holdtime'])})
                    if neighbor['timers'].get('keepalive', None) is not None:
                        tmp_timers.update({'keepalive-interval': str(neighbor['timers']['keepalive'])})
                if neighbor.get('capability', None) is not None:
                    if neighbor['capability'].get('dynamic', None) is not None:
                        tmp_capability.update({'openconfig-bgp-ext:capability-dynamic': neighbor['capability']['dynamic']})
                    if neighbor['capability'].get('extended_nexthop', None) is not None:
                        tmp_capability.update({'openconfig-bgp-ext:capability-extended-nexthop': neighbor['capability']['extended_nexthop']})
                if neighbor.get('advertisement_interval', None) is not None:
                    tmp_timers.update({'minimum-advertisement-interval': str(neighbor['advertisement_interval'])})
                if neighbor.get('neighbor', None) is not None:
                    bgp_neighbor.update({'neighbor-address': neighbor['neighbor']})
                    neighbor_cfg.update({'neighbor-address': neighbor['neighbor']})
                if neighbor.get('peer_group', None) is not None:
                    neighbor_cfg.update({'peer-group': neighbor['peer_group']})
                if neighbor.get('remote_as', None) is not None:
                    have_nei = self.find_nei(have, bgp_as, vrf_name, neighbor)
                    if neighbor['remote_as'].get('peer_as', None) is not None:
                        if have_nei:
                            if have_nei.get("remote_as", None) is not None:
                                if have_nei["remote_as"].get("peer_type", None) is not None:
                                    del_nei = {}
                                    del_nei.update({'neighbor': have_nei['neighbor']})
                                    del_nei.update({'remote_as': have_nei['remote_as']})
                                    requests.extend(self.delete_specific_param_request(vrf_name, del_nei))
                        tmp_remote.update({'peer-as': neighbor['remote_as']['peer_as']})
                    if neighbor['remote_as'].get('peer_type', None) is not None:
                        if have_nei:
                            if have_nei.get("remote_as", None) is not None:
                                if have_nei["remote_as"].get("peer_as", None) is not None:
                                    del_nei = {}
                                    del_nei.update({'neighbor': have_nei['neighbor']})
                                    del_nei.update({'remote_as': have_nei['remote_as']})
                                    requests.extend(self.delete_specific_param_request(vrf_name, del_nei))
                        tmp_remote.update({'peer-type': neighbor['remote_as']['peer_type'].upper()})
                if tmp_timers:
                    bgp_neighbor.update({'timers': {'config': tmp_timers}})
                if tmp_capability:
                    neighbor_cfg.update(tmp_capability)
                if tmp_remote:
                    neighbor_cfg.update(tmp_remote)
                if neighbor_cfg:
                    bgp_neighbor.update({'config': neighbor_cfg})
                if bgp_neighbor:
                    bgp_neighbor_list.append(bgp_neighbor)
        payload = {'openconfig-network-instance:neighbors': {'neighbor': bgp_neighbor_list}}
        return payload, requests

    def get_modify_bgp_requests(self, commands, have):
        requests = []
        if not commands:
            return requests

        for cmd in commands:
            edit_path = '%s=%s/%s' % (self.network_instance_path, cmd['vrf_name'], self.protocol_bgp_path)
            if 'peer_group' in cmd and cmd['peer_group']:
                edit_peer_groups_payload, edit_requests = self.build_bgp_peer_groups_payload(cmd['peer_group'], have, cmd['bgp_as'], cmd['vrf_name'])
                edit_peer_groups_path = edit_path + '/peer-groups'
                if edit_requests:
                    requests.extend(edit_requests)
                requests.append({'path': edit_peer_groups_path, 'method': PATCH, 'data': edit_peer_groups_payload})
            if 'neighbors' in cmd and cmd['neighbors']:
                edit_neighbors_payload, edit_requests = self.build_bgp_neighbors_payload(cmd['neighbors'], have, cmd['bgp_as'], cmd['vrf_name'])
                edit_neighbors_path = edit_path + '/neighbors'
                if edit_requests:
                    requests.extend(edit_requests)
                requests.append({'path': edit_neighbors_path, 'method': PATCH, 'data': edit_neighbors_payload})
        return requests

    def get_delete_specific_bgp_peergroup_param_request(self, vrf_name, cmd, want_match):
        requests = []
        want_peer_group = want_match.get('peer_group', None)
        for each in cmd['peer_group']:
            if each:
                name = each.get('name', None)
                remote_as = each.get('remote_as', None)
                timers = each.get('timers', None)
                advertisement_interval = each.get('advertisement_interval', None)
                bfd = each.get('bfd', None)
                capability = each.get('capability', None)
                address_family = each.get('address_family', None)
                if name and not remote_as and not timers and not advertisement_interval and not bfd and not capability and not address_family:
                    want_pg_match = None
                    if want_peer_group:
                        want_pg_match = next((cfg for cfg in want_peer_group if cfg['name'] == name), None)
                    if want_pg_match:
                        keys = ['remote_as', 'timers', 'advertisement_interval', 'bfd', 'capability', 'address_family']
                        if not any([want_pg_match.get(key, None) for key in keys]):
                            requests.append(self.get_delete_vrf_specific_peergroup_request(vrf_name, name))
                else:
                    requests.extend(self.delete_specific_peergroup_param_request(vrf_name, each))
        return requests

    def delete_specific_peergroup_param_request(self, vrf_name, cmd):
        requests = []
        delete_static_path = '%s=%s/%s' % (self.network_instance_path, vrf_name, self.protocol_bgp_path)
        delete_static_path = delete_static_path + '/peer-groups/peer-group=%s' % (cmd['name'])
        if cmd.get('remote_as', None) is not None:
            if cmd['remote_as'].get('peer_as', None) is not None:
                delete_path = delete_static_path + '/config/peer-as'
                requests.append({'path': delete_path, 'method': DELETE})
            elif cmd['remote_as'].get('peer_type', None) is not None:
                delete_path = delete_static_path + '/config/peer-type'
                requests.append({'path': delete_path, 'method': DELETE})
        if cmd.get('advertisement_interval', None) is not None:
            delete_path = delete_static_path + '/timers/config/minimum-advertisement-interval'
            requests.append({'path': delete_path, 'method': DELETE})
        if cmd.get('timers', None) is not None:
            if cmd['timers'].get('holdtime', None) is not None:
                delete_path = delete_static_path + '/timers/config/hold-time'
                requests.append({'path': delete_path, 'method': DELETE})
            if cmd['timers'].get('keepalive', None) is not None:
                delete_path = delete_static_path + '/timers/config/keepalive-interval'
                requests.append({'path': delete_path, 'method': DELETE})
        if cmd.get('capability', None) is not None:
            if cmd['capability'].get('dynamic', None) is not None:
                delete_path = delete_static_path + '/config/openconfig-bgp-ext:capability-dynamic'
                requests.append({'path': delete_path, 'method': DELETE})
            if cmd['capability'].get('extended_nexthop', None) is not None:
                delete_path = delete_static_path + '/config/openconfig-bgp-ext:capability-extended-nexthop'
                requests.append({'path': delete_path, 'method': DELETE})
        if cmd.get('bfd', None) is not None:
            delete_path = delete_static_path + '/openconfig-bfd:enable-bfd/config/enabled'
            requests.append({'path': delete_path, 'method': DELETE})
        if cmd.get('address_family', None) is not None:
            if cmd['address_family'].get('afis', None) is None:
                delete_path = delete_static_path + '/afi-safis/afi-safi'
                requests.append({'path': delete_path, 'method': DELETE})
            else:
                for each in cmd['address_family']['afis']:
                    afi = each.get('afi', None)
                    safi = each.get('safi', None)
                    activate = each.get('activate', None)
                    allowas_in = each.get('allowas_in', None)
                    afi_safi = afi.upper() + '_' + safi.upper()
                    afi_safi_name = 'openconfig-bgp-types:' + afi_safi
                    if afi and safi and not activate and not allowas_in:
                        delete_path = delete_static_path + '/afi-safis/afi-safi=%s' % (afi_safi_name)
                        requests.append({'path': delete_path, 'method': DELETE})
                    else:
                        if activate:
                            delete_path = delete_static_path + '/afi-safis/afi-safi=%s/config/enabled' % (afi_safi_name)
                            requests.append({'path': delete_path, 'method': DELETE})
                        if allowas_in:
                            if allowas_in.get('origin', None):
                                delete_path = delete_static_path + '/afi-safis/afi-safi=%s/openconfig-bgp-ext:allow-own-as/config/origin' % (afi_safi_name)
                                requests.append({'path': delete_path, 'method': DELETE})
                            if allowas_in.get('value', None):
                                delete_path = delete_static_path + '/afi-safis/afi-safi=%s/openconfig-bgp-ext:allow-own-as/config/as-count' % (afi_safi_name)
                                requests.append({'path': delete_path, 'method': DELETE})

        return requests

    def get_delete_specific_bgp_param_request(self, vrf_name, cmd, want_match):
        requests = []
        want_neighbors = want_match.get('neighbors', None)
        for each in cmd['neighbors']:
            if each:
                neighbor = each.get('neighbor', None)
                remote_as = each.get('remote_as', None)
                peer_group = each.get('peer_group', None)
                timers = each.get('timers', None)
                advertisement_interval = each.get('advertisement_interval', None)
                bfd = each.get('bfd', None)
                capability = each.get('capability', None)
                if neighbor and not remote_as and not peer_group and not timers and not advertisement_interval and not bfd and not capability:
                    want_nei_match = None
                    if want_neighbors:
                        want_nei_match = next(cfg for cfg in want_neighbors if cfg['neighbor'] == neighbor)
                    if want_nei_match:
                        keys = ['remote_as', 'peer_group', 'timers', 'advertisement_interval', 'bfd', 'capability']
                        if not any([want_nei_match.get(key, None) for key in keys]):
                            requests.append(self.delete_neighbor_whole_request(vrf_name, neighbor))
                else:
                    requests.extend(self.delete_specific_param_request(vrf_name, each))
        return requests

    def delete_neighbor_whole_request(self, vrf_name, neighbor):
        requests = []
        url = '%s=%s/%s/%s=%s/' % (self.network_instance_path, vrf_name, self.protocol_bgp_path, self.neighbor_path, neighbor)
        return({'path': url, 'method': DELETE})

    def delete_specific_param_request(self, vrf_name, cmd):
        requests = []
        delete_static_path = '%s=%s/%s' % (self.network_instance_path, vrf_name, self.protocol_bgp_path)
        delete_static_path = delete_static_path + '/neighbors/neighbor=%s' % (cmd['neighbor'])
        if cmd.get('remote_as', None) is not None:
            if cmd['remote_as'].get('peer_as', None) is not None:
                delete_path = delete_static_path + '/config/peer-as'
                requests.append({'path': delete_path, 'method': DELETE})
            elif cmd['remote_as'].get('peer_type', None) is not None:
                delete_path = delete_static_path + '/config/peer-type'
                requests.append({'path': delete_path, 'method': DELETE})
        if cmd.get('peer_group', None) is not None:
            delete_path = delete_static_path + '/config/peer-group'
            requests.append({'path': delete_path, 'method': DELETE})
        if cmd.get('advertisement_interval', None) is not None:
            delete_path = delete_static_path + '/timers/config/minimum-advertisement-interval'
            requests.append({'path': delete_path, 'method': DELETE})
        if cmd.get('timers', None) is not None:
            if cmd['timers'].get('holdtime', None) is not None:
                delete_path = delete_static_path + '/timers/config/hold-time'
                requests.append({'path': delete_path, 'method': DELETE})
            if cmd['timers'].get('keepalive', None) is not None:
                delete_path = delete_static_path + '/timers/config/keepalive-interval'
                requests.append({'path': delete_path, 'method': DELETE})
        if cmd.get('capability', None) is not None:
            if cmd['capability'].get('dynamic', None) is not None:
                delete_path = delete_static_path + '/config/openconfig-bgp-ext:capability-dynamic'
                requests.append({'path': delete_path, 'method': DELETE})
            if cmd['capability'].get('extended_nexthop', None) is not None:
                delete_path = delete_static_path + '/config/openconfig-bgp-ext:capability-extended-nexthop'
                requests.append({'path': delete_path, 'method': DELETE})
        if cmd.get('bfd', None) is not None:
            delete_path = delete_static_path + '/openconfig-bfd:enable-bfd/config/enabled'
            requests.append({'path': delete_path, 'method': DELETE})

        return requests

    def get_delete_vrf_specific_neighbor_request(self, vrf_name, have):
        requests = []
        for each in have:
            if each.get('neighbor', None):
                requests.append(self.delete_neighbor_whole_request(vrf_name, each['neighbor']))
        return requests

    def get_delete_vrf_specific_peergroup_request(self, vrf_name, peergroup_name):
        requests = []
        delete_neighbor_path = '%s=%s/%s/peer-groups/peer-group=%s' % (self.network_instance_path, vrf_name, self.protocol_bgp_path, peergroup_name)
        return ({'path': delete_neighbor_path, 'method': DELETE})

    def get_delete_all_bgp_neighbor_requests(self, commands):
        requests = []
        for cmd in commands:
            if cmd.get('neighbors', None):
                requests.extend(self.get_delete_vrf_specific_neighbor_request(cmd['vrf_name'], cmd['neighbors']))
            if 'peer_group' in cmd and cmd['peer_group']:
                for each in cmd['peer_group']:
                    requests.append(self.get_delete_vrf_specific_peergroup_request(cmd['vrf_name'], each['name']))
        return requests

    def get_delete_bgp_neighbor_requests(self, commands, have, want, is_delete_all):
        requests = []
        if is_delete_all:
            requests = self.get_delete_all_bgp_neighbor_requests(commands)
        else:
            for cmd in commands:
                vrf_name = cmd['vrf_name']
                as_val = cmd['bgp_as']
                neighbors = cmd.get('neighbors', None)
                peer_group = cmd.get('peer_group', None)
                want_match = next((cfg for cfg in want if vrf_name == cfg['vrf_name'] and as_val == cfg['bgp_as']), None)
                want_neighbors = want_match.get('neighbors', None)
                want_peer_group = want_match.get('peer_group', None)
                if neighbors is None and peer_group is None and want_neighbors is None and want_peer_group is None:
                    new_cmd = {}
                    for each in have:
                        if vrf_name == each['vrf_name'] and as_val == each['bgp_as']:
                            new_neighbors = []
                            new_pg = []
                            if each.get('neighbors', None):
                                new_neighbors = [{'neighbor': i['neighbor']} for i in each.get('neighbors', None)]
                            if each.get('peer_group', None):
                                new_pg = [{'name': i['name']} for i in each.get('peer_group', None)]
                            if new_neighbors:
                                new_cmd['neighbors'] = new_neighbors
                                requests.extend(self.get_delete_vrf_specific_neighbor_request(vrf_name, new_cmd['neighbors']))
                            if new_pg:
                                new_cmd['name'] = new_pg
                                for each in new_cmd['name']:
                                    requests.append(self.get_delete_vrf_specific_peergroup_request(vrf_name, each['name']))
                            break
                else:
                    if neighbors:
                        requests.extend(self.get_delete_specific_bgp_param_request(vrf_name, cmd, want_match))
                    if peer_group:
                        requests.extend(self.get_delete_specific_bgp_peergroup_param_request(vrf_name, cmd, want_match))
        return requests
