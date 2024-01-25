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
    remove_matching_defaults,
    update_dict,
    remove_empties,
    remove_empties_from_list
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.bgp_utils import (
    validate_bgps,
    normalize_neighbors_interface_name,
    get_ip_afi_cfg_payload,
    get_prefix_limit_payload
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import to_request
from ansible.module_utils.connection import ConnectionError

from copy import deepcopy

PATCH = 'patch'
DELETE = 'delete'

TEST_KEYS = [
    {'config': {'vrf_name': '', 'bgp_as': ''}},
    {'neighbors': {'neighbor': ''}},
    {'peer_group': {'name': ''}},
    {'afis': {'afi': '', 'safi': ''}},
]

default_entries = [
    [
        {'name': 'peer_group'},
        {'name': 'timers'},
        {'name': 'keepalive', 'default': 60}
    ],
    [
        {'name': 'peer_group'},
        {'name': 'timers'},
        {'name': 'holdtime', 'default': 180}
    ],
    [
        {'name': 'peer_group'},
        {'name': 'timers'},
        {'name': 'connect_retry', 'default': 30}
    ],
    [
        {'name': 'peer_group'},
        {'name': 'advertisement_interval', 'default': 30}
    ],
    [
        {'name': 'peer_group'},
        {'name': 'auth_pwd'},
        {'name': 'encrypted', 'default': False}
    ],
    [
        {'name': 'peer_group'},
        {'name': 'ebgp_multihop'},
        {'name': 'enabled', 'default': False}
    ],
    [
        {'name': 'peer_group'},
        {'name': 'passive', 'default': False}
    ],
    [
        {'name': 'peer_group'},
        {'name': 'address_family'},
        {'name': 'afis'},
        {'name': 'ip_afi'},
        {'name': 'send_default_route', 'default': False}
    ],
    [
        {'name': 'peer_group'},
        {'name': 'address_family'},
        {'name': 'afis'},
        {'name': 'activate', 'default': False}
    ],
    [
        {'name': 'peer_group'},
        {'name': 'address_family'},
        {'name': 'afis'},
        {'name': 'prefix_limit'},
        {'name': 'prevent_teardown', 'default': False}
    ],
    [
        {'name': 'neighbors'},
        {'name': 'timers'},
        {'name': 'keepalive', 'default': 60}
    ],
    [
        {'name': 'neighbors'},
        {'name': 'timers'},
        {'name': 'holdtime', 'default': 180}
    ],
    [
        {'name': 'neighbors'},
        {'name': 'timers'},
        {'name': 'connect_retry', 'default': 30}
    ],
    [
        {'name': 'neighbors'},
        {'name': 'advertisement_interval', 'default': 30}
    ],
    [
        {'name': 'neighbors'},
        {'name': 'auth_pwd'},
        {'name': 'encrypted', 'default': False}
    ],
    [
        {'name': 'neighbors'},
        {'name': 'ebgp_multihop'},
        {'name': 'enabled', 'default': False}
    ],
    [
        {'name': 'neighbors'},
        {'name': 'passive', 'default': False}
    ],
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
            commands, requests = self._state_deleted(want, have)
        elif state == 'merged':
            commands, requests = self._state_merged(want, have, diff)
        elif state == 'replaced':
            commands, requests = self._state_replaced(want, have, diff)
        elif state == 'overridden':
            commands, requests = self._state_overridden(want, have, diff)
        return commands, requests

    def _state_replaced(self, want, have, diff):
        commands, requests = [], []

        commands, requests = self.get_replaced_overridden_config(want, have, "replaced")

        return commands, requests

    def _state_overridden(self, want, have, diff):
        commands, requests = [], []
        commands, requests = self.get_replaced_overridden_config(want, have, "overridden")

        return commands, requests

    def _state_merged(self, want, have, diff):
        """ The command generator when state is merged

        :param want: the additive configuration as a dictionary
        :param have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        requests = []
        commands = diff
        validate_bgps(self._module, commands, have)
        requests = self.get_modify_bgp_requests(commands, have)
        if commands and len(requests) > 0:
            commands = update_states(commands, "merged")
        else:
            commands = []
        return commands, requests

    def _state_deleted(self, want, have):
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
            new_want = want
        else:
            new_have = deepcopy(have)
            new_want = deepcopy(want)
            for default_entry in default_entries:
                remove_matching_defaults(new_have, default_entry)
                remove_matching_defaults(new_want, default_entry)
            d_diff = get_diff(new_want, new_have, TEST_KEYS)
            delete_diff = get_diff(new_want, d_diff, TEST_KEYS)
            commands = delete_diff
        requests = self.get_delete_bgp_neighbor_requests(commands, new_have, new_want, is_delete_all)

        if commands and len(requests) > 0:
            commands = update_states(commands, "deleted")
        else:
            commands = []
        return commands, requests

    def get_replaced_overridden_config(self, want, have, cur_state):
        commands, requests = [], []

        commands_del, requests_del = [], []
        commands_add, requests_add = [], []

        for conf in want:
            bgp_as = conf.get('bgp_as')
            vrf_name = conf.get('vrf_name')
            have_conf = next((h_conf for h_conf in have if h_conf['bgp_as'] == bgp_as and h_conf['vrf_name'] == vrf_name), None)

            if not have_conf:
                commands_add.append(conf)
            else:
                conf = remove_empties(conf)
                have_conf = remove_empties(have_conf)
                add_conf, delete_conf = {}, {}
                non_peer_group_specified = non_neighbor_specified = False
                if cur_state == 'replaced':
                    for attr in conf:
                        if attr not in ['bgp_as', 'vrf_name'] and conf.get(attr) is not None:
                            if attr != 'peer_group':
                                non_peer_group_specified = True
                            elif attr != 'neighbors':
                                non_neighbor_specified = True
                else:
                    non_peer_group_specified = non_neighbor_specified = True

                replace_pg_alone = replace_nbr_alone = False

                if non_peer_group_specified and not non_neighbor_specified:
                    replace_nbr_alone = True
                elif not non_peer_group_specified and non_neighbor_specified:
                    replace_pg_alone = True
                elif non_peer_group_specified and non_neighbor_specified:
                    replace_pg_alone = replace_nbr_alone = True

                want_pg = conf.get('peer_group', [])
                have_pg = have_conf.get('peer_group', [])
                want_nbr = conf.get('neighbors', [])
                have_nbr = have_conf.get('neighbors', [])

                if replace_pg_alone:
                    PEER_TEST_KEYS = [{'name': ''}, {'afis': {'afi': '', 'safi': ''}}]
                    pg_add = get_diff(want_pg, have_pg, PEER_TEST_KEYS)
                    pg_delete = get_diff(have_pg, want_pg, PEER_TEST_KEYS)
                    if pg_add:
                        add_conf['peer_group'] = pg_add
                    if pg_delete:
                        delete_conf['peer_group'] = pg_delete
                if replace_nbr_alone:
                    NBR_TEST_KEYS = [{'neighbor': ''}]
                    nbr_add = get_diff(want_nbr, have_nbr, NBR_TEST_KEYS)
                    nbr_delete = get_diff(have_nbr, want_nbr, NBR_TEST_KEYS)
                    if nbr_add:
                        add_conf['neighbors'] = nbr_add
                    if nbr_delete:
                        delete_conf['neighbors'] = nbr_delete
                if add_conf:
                    add_conf['bgp_as'] = bgp_as
                    add_conf['vrf_name'] = vrf_name
                    commands_add.append(add_conf)
                if delete_conf:
                    delete_conf['bgp_as'] = bgp_as
                    delete_conf['vrf_name'] = vrf_name
                    commands_del.append(delete_conf)

        if cur_state == "overridden":
            for have_conf in have:
                in_want = next((conf for conf in want if conf['bgp_as'] == have_conf['bgp_as'] and conf['vrf_name'] == have_conf['vrf_name']), None)
                if not in_want:
                    commands_del.append(have_conf)
        if commands_del:
            new_commands_del = deepcopy(commands_del)
            for default_entry in default_entries:
                remove_matching_defaults(new_commands_del, default_entry)

            d_diff = get_diff(new_commands_del, have, TEST_KEYS)
            delete_diff = get_diff(new_commands_del, d_diff, TEST_KEYS)
            commands_del = delete_diff
            if commands_del:
                requests_del = self.get_delete_bgp_neighbor_requests(delete_diff, have, new_commands_del, True)

                if len(requests_del) > 0:
                    commands.extend(update_states(commands_del, "deleted"))
                    requests.extend(requests_del)

        if commands_add:
            validate_bgps(self._module, commands_add, have)
            requests_add = self.get_modify_bgp_requests(commands_add, [])

            if len(requests_add) > 0:
                commands.extend(update_states(commands_add, cur_state))
                requests.extend(requests_add)

        return commands, requests

    def build_bgp_peer_groups_payload(self, cmd, have, bgp_as, vrf_name):
        requests = []
        bgp_peer_group_list = []
        for peer_group in cmd:
            if peer_group:
                bgp_peer_group, peer_group_cfg = {}, {}
                tmp_bfd, tmp_ebgp, tmp_capability = {}, {}, {}
                tmp_transport, tmp_timers, tmp_remote = {}, {}, {}
                afi = []

                update_dict(peer_group, peer_group_cfg, 'name', 'peer-group-name')
                update_dict(peer_group, bgp_peer_group, 'name', 'peer-group-name')

                if peer_group.get('bfd') is not None:
                    update_dict(peer_group['bfd'], tmp_bfd, 'enabled', 'enabled')
                    update_dict(peer_group['bfd'], tmp_bfd, 'check_failure', 'check-control-plane-failure')
                    update_dict(peer_group['bfd'], tmp_bfd, 'profile', 'bfd-profile')

                if peer_group.get('auth_pwd') is not None:
                    if (peer_group['auth_pwd'].get('pwd') is not None and peer_group['auth_pwd'].get('encrypted') is not None):
                        bgp_peer_group.update({'auth-password': {'config': {'password': peer_group['auth_pwd']['pwd'],
                                                                            'encrypted': peer_group['auth_pwd']['encrypted']}}})

                if peer_group.get('ebgp_multihop') is not None:
                    update_dict(peer_group['ebgp_multihop'], tmp_ebgp, 'enabled', 'enabled')
                    update_dict(peer_group['ebgp_multihop'], tmp_ebgp, 'multihop_ttl', 'multihop-ttl')

                if peer_group.get('timers') is not None:
                    update_dict(peer_group['timers'], tmp_timers, 'holdtime', 'hold-time')
                    update_dict(peer_group['timers'], tmp_timers, 'keepalive', 'keepalive-interval')
                    update_dict(peer_group['timers'], tmp_timers, 'connect_retry', 'connect-retry')

                if peer_group.get('capability') is not None:
                    update_dict(peer_group['capability'], tmp_capability, 'dynamic', 'capability-dynamic')
                    update_dict(peer_group['capability'], tmp_capability, 'extended_nexthop', 'capability-extended-nexthop')

                update_dict(peer_group, peer_group_cfg, 'pg_description', 'description')
                update_dict(peer_group, peer_group_cfg, 'disable_connected_check', 'disable-ebgp-connected-route-check')
                update_dict(peer_group, peer_group_cfg, 'dont_negotiate_capability', 'dont-negotiate-capability')
                update_dict(peer_group, peer_group_cfg, 'enforce_first_as', 'enforce-first-as')
                update_dict(peer_group, peer_group_cfg, 'enforce_multihop', 'enforce-multihop')
                update_dict(peer_group, peer_group_cfg, 'override_capability', 'override-capability')
                update_dict(peer_group, peer_group_cfg, 'shutdown_msg', 'shutdown-message')
                update_dict(peer_group, peer_group_cfg, 'solo', 'solo-peer')
                update_dict(peer_group, peer_group_cfg, 'strict_capability_match', 'strict-capability-match')
                update_dict(peer_group, peer_group_cfg, 'ttl_security', 'ttl-security-hops')

                if peer_group.get('local_as') is not None:
                    update_dict(peer_group['local_as'], peer_group_cfg, 'as', 'local-as')
                    update_dict(peer_group['local_as'], peer_group_cfg, 'no_prepend', 'local-as-no-prepend')
                    update_dict(peer_group['local_as'], peer_group_cfg, 'replace_as', 'local-as-replace-as')

                update_dict(peer_group, tmp_transport, 'local_address', 'local-address')
                update_dict(peer_group, tmp_transport, 'passive', 'passive-mode')
                update_dict(peer_group, tmp_timers, 'advertisement_interval', 'minimum-advertisement-interval')

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
                            afi_safi_cfg = {}
                            pfx_lmt_cfg = {}
                            pfx_lst_cfg = {}
                            ip_dict = {}
                            if each.get('afi', None) is not None and each.get('safi', None) is not None:
                                afi_safi = each['afi'].upper() + "_" + each['safi'].upper()
                                if afi_safi is not None:
                                    afi_safi_name = 'openconfig-bgp-types:' + afi_safi
                                if afi_safi_name is not None:
                                    samp.update({'afi-safi-name': afi_safi_name})
                                    samp.update({'config': {'afi-safi-name': afi_safi_name}})
                            if each.get('prefix_limit', None) is not None:
                                pfx_lmt_cfg = get_prefix_limit_payload(each['prefix_limit'])
                            if pfx_lmt_cfg and afi_safi == 'L2VPN_EVPN':
                                self._module.fail_json('Prefix limit configuration not supported for l2vpn evpn')
                            else:
                                if each.get('ip_afi', None) is not None:
                                    afi_safi_cfg = get_ip_afi_cfg_payload(each['ip_afi'])
                                    if afi_safi_cfg:
                                        ip_dict.update({'config': afi_safi_cfg})
                                if pfx_lmt_cfg:
                                    ip_dict.update({'prefix-limit': {'config': pfx_lmt_cfg}})
                                if ip_dict and afi_safi == 'IPV4_UNICAST':
                                    samp.update({'ipv4-unicast': ip_dict})
                                elif ip_dict and afi_safi == 'IPV6_UNICAST':
                                    samp.update({'ipv6-unicast': ip_dict})
                            if each.get('activate') is not None:
                                samp.update({'config': {'enabled': each['activate']}})
                            if each.get('allowas_in') is not None:
                                have_pg_af = self.find_af(have, bgp_as, vrf_name, peer_group, each['afi'], each['safi'])
                                if each['allowas_in'].get('origin') is not None:
                                    if have_pg_af:
                                        if have_pg_af.get('allowas_in') is not None:
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
                                    samp.update({'allow-own-as': {'config': {'origin': origin, "enabled": bool("true")}}})
                                if each['allowas_in'].get('value') is not None:
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
                                    samp.update({'allow-own-as': {'config': {'as-count': as_count, "enabled": bool("true")}}})
                            if each.get('prefix_list_in', None) is not None:
                                prefix_list_in = each['prefix_list_in']
                                if prefix_list_in is not None:
                                    pfx_lst_cfg.update({'import-policy': prefix_list_in})
                            if each.get('prefix_list_out', None) is not None:
                                prefix_list_out = each['prefix_list_out']
                                if prefix_list_out is not None:
                                    pfx_lst_cfg.update({'export-policy': prefix_list_out})
                            if pfx_lst_cfg:
                                samp.update({'prefix-list': {'config': pfx_lst_cfg}})
                            if samp:
                                afi.append(samp)

                update_dict(tmp_timers, bgp_peer_group, '', '', {'timers': {'config': tmp_timers}})
                update_dict(tmp_bfd, bgp_peer_group, '', '', {'enable-bfd': {'config': tmp_bfd}})
                update_dict(tmp_ebgp, bgp_peer_group, '', '', {'ebgp-multihop': {'config': tmp_ebgp}})
                update_dict(tmp_capability, peer_group_cfg, '', '', tmp_capability)
                update_dict(tmp_transport, bgp_peer_group, '', '', {'transport': {'config': tmp_transport}})
                update_dict(tmp_remote, peer_group_cfg, '', '', tmp_remote)
                update_dict(peer_group_cfg, bgp_peer_group, '', '', {'config': peer_group_cfg})
                if afi and len(afi) > 0:
                    bgp_peer_group.update({'afi-safis': {'afi-safi': afi}})
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
                bgp_neighbor, neighbor_cfg = {}, {}
                tmp_bfd, tmp_ebgp, tmp_capability = {}, {}, {}
                tmp_transport, tmp_timers, tmp_remote = {}, {}, {}

                update_dict(neighbor, bgp_neighbor, 'neighbor', 'neighbor-address')
                update_dict(neighbor, neighbor_cfg, 'neighbor', 'neighbor-address')

                if neighbor.get('bfd') is not None:
                    update_dict(neighbor['bfd'], tmp_bfd, 'enabled', 'enabled')
                    update_dict(neighbor['bfd'], tmp_bfd, 'check_failure', 'check-control-plane-failure')
                    update_dict(neighbor['bfd'], tmp_bfd, 'profile', 'bfd-profile')

                if neighbor.get('auth_pwd') is not None:
                    if (neighbor['auth_pwd'].get('pwd') is not None and neighbor['auth_pwd'].get('encrypted') is not None):
                        bgp_neighbor.update({'auth-password': {'config': {'password': neighbor['auth_pwd']['pwd'], 'encrypted': neighbor['auth_pwd']['encrypted']}}})

                if neighbor.get('ebgp_multihop') is not None:
                    update_dict(neighbor['ebgp_multihop'], tmp_ebgp, 'enabled', 'enabled')
                    update_dict(neighbor['ebgp_multihop'], tmp_ebgp, 'multihop_ttl', 'multihop-ttl')

                if neighbor.get('timers') is not None:
                    update_dict(neighbor['timers'], tmp_timers, 'holdtime', 'hold-time')
                    update_dict(neighbor['timers'], tmp_timers, 'keepalive', 'keepalive-interval')
                    update_dict(neighbor['timers'], tmp_timers, 'connect_retry', 'connect-retry')

                if neighbor.get('capability') is not None:
                    update_dict(neighbor['capability'], tmp_capability, 'dynamic', 'capability-dynamic')
                    update_dict(neighbor['capability'], tmp_capability, 'extended_nexthop', 'capability-extended-nexthop')

                update_dict(neighbor, neighbor_cfg, 'peer_group', 'peer-group')
                update_dict(neighbor, neighbor_cfg, 'nbr_description', 'description')
                update_dict(neighbor, neighbor_cfg, 'disable_connected_check', 'disable-ebgp-connected-route-check')
                update_dict(neighbor, neighbor_cfg, 'dont_negotiate_capability', 'dont-negotiate-capability')
                update_dict(neighbor, neighbor_cfg, 'enforce_first_as', 'enforce-first-as')
                update_dict(neighbor, neighbor_cfg, 'enforce_multihop', 'enforce-multihop')
                update_dict(neighbor, neighbor_cfg, 'override_capability', 'override-capability')
                update_dict(neighbor, neighbor_cfg, 'shutdown_msg', 'shutdown-message')
                update_dict(neighbor, neighbor_cfg, 'solo', 'solo-peer')
                update_dict(neighbor, neighbor_cfg, 'port', 'peer-port')
                update_dict(neighbor, neighbor_cfg, 'v6only', 'openconfig-bgp-ext:v6only')
                update_dict(neighbor, neighbor_cfg, 'strict_capability_match', 'strict-capability-match')
                update_dict(neighbor, neighbor_cfg, 'ttl_security', 'ttl-security-hops')

                if neighbor.get('local_as') is not None:
                    update_dict(neighbor['local_as'], neighbor_cfg, 'as', 'local-as')
                    update_dict(neighbor['local_as'], neighbor_cfg, 'no_prepend', 'local-as-no-prepend')
                    update_dict(neighbor['local_as'], neighbor_cfg, 'replace_as', 'local-as-replace-as')

                update_dict(neighbor, tmp_transport, 'local_address', 'local-address')
                update_dict(neighbor, tmp_transport, 'passive', 'passive-mode')
                update_dict(neighbor, tmp_timers, 'advertisement_interval', 'minimum-advertisement-interval')

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

                update_dict(tmp_timers, bgp_neighbor, '', '', {'timers': {'config': tmp_timers}})
                update_dict(tmp_bfd, bgp_neighbor, '', '', {'enable-bfd': {'config': tmp_bfd}})
                update_dict(tmp_ebgp, bgp_neighbor, '', '', {'ebgp-multihop': {'config': tmp_ebgp}})
                update_dict(tmp_capability, neighbor_cfg, '', '', tmp_capability)
                update_dict(tmp_transport, bgp_neighbor, '', '', {'transport': {'config': tmp_transport}})
                update_dict(tmp_remote, neighbor_cfg, '', '', tmp_remote)
                update_dict(neighbor_cfg, bgp_neighbor, '', '', {'config': neighbor_cfg})

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
                auth_pwd = each.get('auth_pwd', None)
                pg_description = each.get('pg_description', None)
                disable_connected_check = each.get('disable_connected_check', None)
                dont_negotiate_capability = each.get('dont_negotiate_capability', None)
                ebgp_multihop = each.get('ebgp_multihop', None)
                enforce_first_as = each.get('enforce_first_as', None)
                enforce_multihop = each.get('enforce_multihop', None)
                local_address = each.get('local_address', None)
                local_as = each.get('local_as', None)
                override_capability = each.get('override_capability', None)
                passive = each.get('passive', None)
                shutdown_msg = each.get('shutdown_msg', None)
                solo = each.get('solo', None)
                strict_capability_match = each.get('strict_capability_match', None)
                ttl_security = each.get('ttl_security', None)
                address_family = each.get('address_family', None)
                if (name and not remote_as and not timers and not advertisement_interval and not bfd and not capability and not auth_pwd and not
                        pg_description and disable_connected_check is None and dont_negotiate_capability is None and not ebgp_multihop and
                        enforce_first_as is None and enforce_multihop is None and not local_address and not local_as and override_capability
                        is None and passive is None and not shutdown_msg and solo is None and strict_capability_match is None and not ttl_security and
                        not address_family):
                    want_pg_match = None
                    if want_peer_group:
                        want_pg_match = next((cfg for cfg in want_peer_group if cfg['name'] == name), None)
                    if want_pg_match:
                        keys = ['remote_as', 'timers', 'advertisement_interval', 'bfd', 'capability', 'auth_pwd', 'pg_description',
                                'disable_connected_check', 'dont_negotiate_capability', 'ebgp_multihop', 'enforce_first_as', 'enforce_multihop',
                                'local_address', 'local_as', 'override_capability', 'passive', 'shutdown_msg', 'solo', 'strict_capability_match',
                                'ttl_security', 'address_family']
                        if not any(want_pg_match.get(key, None) for key in keys):
                            requests.append(self.get_delete_vrf_specific_peergroup_request(vrf_name, name))
                else:
                    requests.extend(self.delete_specific_peergroup_param_request(vrf_name, each))
        return requests

    def delete_specific_peergroup_param_request(self, vrf_name, cmd):
        requests = []
        delete_static_path = '%s=%s/%s' % (self.network_instance_path, vrf_name, self.protocol_bgp_path)
        delete_static_path = delete_static_path + '/peer-groups/peer-group=%s' % (cmd['name'])
        peergroup_request_path = {
            'remote_as': '',
            'advertisement_interval': '/timers/config/minimum-advertisement-interval',
            'timers': {
                'holdtime': '/timers/config/hold-time',
                'keepalive': '/timers/config/keepalive-interval',
                'connect_retry': '/timers/config/connect-retry'
            },
            'capability': {
                'dynamic': '/config/capability-dynamic',
                'extended_nexthop': '/config/capability-extended-nexthop'
            },
            'pg_description': '/config/description',
            'disable_connected_check': '/config/disable-ebgp-connected-route-check',
            'dont_negotiate_capability': '/config/dont-negotiate-capability',
            'enforce_first_as': '/config/enforce-first-as',
            'enforce_multihop': '/config/enforce-multihop',
            'override_capability': '/config/override-capability',
            'shutdown_msg': '/config/shutdown-message',
            'solo': '/config/solo-peer',
            'strict_capability_match': '/config/strict-capability-match',
            'ttl_security': '/config/ttl-security-hops',
            'local_as': {
                'as': '/config/local-as',
                'no_prepend': '/config/local-as-no-prepend',
                'replace_as': '/config/local-as-replace-as'
            },
            'local_address': '/transport/config/local-address',
            'passive': '/transport/config/passive-mode',
            'bfd': {
                'enabled': '/enable-bfd/config/enabled',
                'check_failure': '/enable-bfd/config/check-control-plane-failure',
                'profile': '/enable-bfd/config/bfd-profile'
            },
            'auth_pwd': {
                'pwd': '/auth-password/config/password',
                'encrypted': '/auth-password/config/encrypted'
            },
            'ebgp_multihop': {
                'enabled': '/ebgp-multihop/config/enabled',
                'multihop_ttl': '/ebgp-multihop/config/multihop-ttl'
            }
        }

        for attr in peergroup_request_path:
            if cmd.get(attr, None) is not None:
                if attr == 'remote_as':
                    if cmd['remote_as'].get('peer_as', None) is not None:
                        delete_path = delete_static_path + '/config/peer-as'
                        requests.append({'path': delete_path, 'method': DELETE})
                    elif cmd['remote_as'].get('peer_type', None) is not None:
                        delete_path = delete_static_path + '/config/peer-type'
                        requests.append({'path': delete_path, 'method': DELETE})
                elif isinstance(peergroup_request_path[attr], dict):
                    for dict_attr in peergroup_request_path[attr]:
                        if cmd[attr].get(dict_attr, None) is not None:
                            delete_path = delete_static_path + peergroup_request_path[attr][dict_attr]
                            requests.append({'path': delete_path, 'method': DELETE})
                else:
                    delete_path = delete_static_path + peergroup_request_path[attr]
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
                    ip_afi = each.get('ip_afi', None)
                    prefix_limit = each.get('prefix_limit', None)
                    prefix_list_in = each.get('prefix_list_in', None)
                    prefix_list_out = each.get('prefix_list_out', None)
                    afi_safi = afi.upper() + '_' + safi.upper()
                    afi_safi_name = 'openconfig-bgp-types:' + afi_safi
                    if (afi and safi and not activate and not allowas_in and not ip_afi and not prefix_limit and not prefix_list_in
                            and not prefix_list_out):
                        delete_path = delete_static_path + '/afi-safis/afi-safi=%s' % (afi_safi_name)
                        requests.append({'path': delete_path, 'method': DELETE})
                    else:
                        if activate:
                            delete_path = delete_static_path + '/afi-safis/afi-safi=%s/config/enabled' % (afi_safi_name)
                            requests.append({'path': delete_path, 'method': DELETE})
                        if allowas_in:
                            if allowas_in.get('origin', None):
                                delete_path = delete_static_path + '/afi-safis/afi-safi=%s/allow-own-as/config/origin' % (afi_safi_name)
                                requests.append({'path': delete_path, 'method': DELETE})
                            if allowas_in.get('value', None):
                                delete_path = delete_static_path + '/afi-safis/afi-safi=%s/allow-own-as/config/as-count' % (afi_safi_name)
                                requests.append({'path': delete_path, 'method': DELETE})
                        if prefix_list_in:
                            delete_path = delete_static_path + '/afi-safis/afi-safi=%s/prefix-list/config/import-policy' % (afi_safi_name)
                            requests.append({'path': delete_path, 'method': DELETE})
                        if prefix_list_out:
                            delete_path = delete_static_path + '/afi-safis/afi-safi=%s/prefix-list/config/export-policy' % (afi_safi_name)
                            requests.append({'path': delete_path, 'method': DELETE})
                        if afi_safi == 'IPV4_UNICAST':
                            if ip_afi:
                                requests.extend(self.delete_ip_afi_requests(ip_afi, afi_safi_name, 'ipv4-unicast', delete_static_path))
                            if prefix_limit:
                                requests.extend(self.delete_prefix_limit_requests(prefix_limit, afi_safi_name, 'ipv4-unicast', delete_static_path))
                        elif afi_safi == 'IPV6_UNICAST':
                            if ip_afi:
                                requests.extend(self.delete_ip_afi_requests(ip_afi, afi_safi_name, 'ipv6-unicast', delete_static_path))
                            if prefix_limit:
                                requests.extend(self.delete_prefix_limit_requests(prefix_limit, afi_safi_name, 'ipv6-unicast', delete_static_path))

        return requests

    def delete_ip_afi_requests(self, ip_afi, afi_safi_name, afi_safi, delete_static_path):
        requests = []
        default_policy_name = ip_afi.get('default_policy_name', None)
        send_default_route = ip_afi.get('send_default_route', None)
        if default_policy_name:
            delete_path = delete_static_path + '/afi-safis/afi-safi=%s/%s/config/default-policy-name' % (afi_safi_name, afi_safi)
            requests.append({'path': delete_path, 'method': DELETE})
        if send_default_route:
            delete_path = delete_static_path + '/afi-safis/afi-safi=%s/%s/config/send_default_route' % (afi_safi_name, afi_safi)
            requests.append({'path': delete_path, 'method': DELETE})

        return requests

    def delete_prefix_limit_requests(self, prefix_limit, afi_safi_name, afi_safi, delete_static_path):
        requests = []
        max_prefixes = prefix_limit.get('max_prefixes', None)
        prevent_teardown = prefix_limit.get('prevent_teardown', None)
        warning_threshold = prefix_limit.get('warning_threshold', None)
        restart_timer = prefix_limit.get('restart_timer', None)
        if max_prefixes:
            delete_path = delete_static_path + '/afi-safis/afi-safi=%s/%s/prefix-limit/config/max-prefixes' % (afi_safi_name, afi_safi)
            requests.append({'path': delete_path, 'method': DELETE})
        if prevent_teardown:
            delete_path = delete_static_path + '/afi-safis/afi-safi=%s/%s/prefix-limit/config/prevent-teardown' % (afi_safi_name, afi_safi)
            requests.append({'path': delete_path, 'method': DELETE})
        if warning_threshold:
            delete_path = delete_static_path + '/afi-safis/afi-safi=%s/%s/prefix-limit/config/warning-threshold-pct' % (afi_safi_name, afi_safi)
            requests.append({'path': delete_path, 'method': DELETE})
        if restart_timer:
            delete_path = delete_static_path + '/afi-safis/afi-safi=%s/%s/prefix-limit/config/restart-timer' % (afi_safi_name, afi_safi)
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
                auth_pwd = each.get('auth_pwd', None)
                nbr_description = each.get('nbr_description', None)
                disable_connected_check = each.get('disable_connected_check', None)
                dont_negotiate_capability = each.get('dont_negotiate_capability', None)
                ebgp_multihop = each.get('ebgp_multihop', None)
                enforce_first_as = each.get('enforce_first_as', None)
                enforce_multihop = each.get('enforce_multihop', None)
                local_address = each.get('local_address', None)
                local_as = each.get('local_as', None)
                override_capability = each.get('override_capability', None)
                passive = each.get('passive', None)
                port = each.get('port', None)
                shutdown_msg = each.get('shutdown_msg', None)
                solo = each.get('solo', None)
                strict_capability_match = each.get('strict_capability_match', None)
                ttl_security = each.get('ttl_security', None)
                v6only = each.get('v6only', None)
                if (neighbor and not remote_as and not peer_group and not timers and not advertisement_interval and not bfd and not capability and not
                        auth_pwd and not nbr_description and disable_connected_check is None and dont_negotiate_capability is None and not
                        ebgp_multihop and enforce_first_as is None and enforce_multihop is None and not local_address and not local_as and
                        override_capability is None and not passive and not port and not shutdown_msg and solo is None and strict_capability_match
                        is None and not ttl_security and v6only is None):
                    want_nei_match = None
                    if want_neighbors:
                        want_nei_match = next((cfg for cfg in want_neighbors if cfg['neighbor'] == neighbor), None)
                    if want_nei_match:
                        keys = ['remote_as', 'peer_group', 'timers', 'advertisement_interval', 'bfd', 'capability', 'auth_pwd', 'nbr_description',
                                'disable_connected_check', 'dont_negotiate_capability', 'ebgp_multihop', 'enforce_first_as', 'enforce_multihop',
                                'local_address', 'local_as', 'override_capability', 'passive', 'port', 'shutdown_msg', 'solo',
                                'strict_capability_match', 'ttl_security', 'v6only']
                        if not any(want_nei_match.get(key, None) for key in keys):
                            requests.append(self.delete_neighbor_whole_request(vrf_name, neighbor))
                else:
                    requests.extend(self.delete_specific_param_request(vrf_name, each))
        return requests

    def delete_neighbor_whole_request(self, vrf_name, neighbor):
        requests = []
        url = '%s=%s/%s/%s=%s/' % (self.network_instance_path, vrf_name, self.protocol_bgp_path, self.neighbor_path, neighbor)
        return ({'path': url, 'method': DELETE})

    def delete_specific_param_request(self, vrf_name, cmd):
        requests = []
        delete_static_path = '%s=%s/%s' % (self.network_instance_path, vrf_name, self.protocol_bgp_path)
        delete_static_path = delete_static_path + '/neighbors/neighbor=%s' % (cmd['neighbor'])
        nbr_request_path = {
            'remote_as': '',
            'peer_group': '/config/peer-group',
            'advertisement_interval': '/timers/config/minimum-advertisement-interval',
            'timers': {
                'holdtime': '/timers/config/hold-time',
                'keepalive': '/timers/config/keepalive-interval',
                'connect_retry': '/timers/config/connect-retry'
            },
            'capability': {
                'dynamic': '/config/capability-dynamic',
                'extended_nexthop': '/config/capability-extended-nexthop'
            },
            'nbr_description': '/config/description',
            'disable_connected_check': '/config/disable-ebgp-connected-route-check',
            'dont_negotiate_capability': '/config/dont-negotiate-capability',
            'enforce_first_as': '/config/enforce-first-as',
            'enforce_multihop': '/config/enforce-multihop',
            'override_capability': '/config/override-capability',
            'shutdown_msg': '/config/shutdown-message',
            'solo': '/config/solo-peer',
            'port': '/config/peer-port',
            'strict_capability_match': '/config/strict-capability-match',
            'ttl_security': '/config/ttl-security-hops',
            'v6only': '/config/openconfig-bgp-ext:v6only',
            'local_as': {
                'as': '/config/local-as',
                'no_prepend': '/config/local-as-no-prepend',
                'replace_as': '/config/local-as-replace-as'
            },
            'local_address': '/transport/config/local-address',
            'passive': '/transport/config/passive-mode',
            'bfd': {
                'enabled': '/enable-bfd/config/enabled',
                'check_failure': '/enable-bfd/config/check-control-plane-failure',
                'profile': '/enable-bfd/config/bfd-profile'
            },
            'auth_pwd': {
                'pwd': '/auth-password/config/password',
                'encrypted': '/auth-password/config/encrypted'
            },
            'ebgp_multihop': {
                'enabled': '/ebgp-multihop/config/enabled',
                'multihop_ttl': '/ebgp-multihop/config/multihop-ttl'
            }
        }

        for attr in nbr_request_path:
            if cmd.get(attr, None) is not None:
                if attr == 'remote_as':
                    if cmd['remote_as'].get('peer_as', None) is not None:
                        delete_path = delete_static_path + '/config/peer-as'
                        requests.append({'path': delete_path, 'method': DELETE})
                    elif cmd['remote_as'].get('peer_type', None) is not None:
                        delete_path = delete_static_path + '/config/peer-type'
                        requests.append({'path': delete_path, 'method': DELETE})
                elif isinstance(nbr_request_path[attr], dict):
                    for dict_attr in nbr_request_path[attr]:
                        if cmd[attr].get(dict_attr, None) is not None:
                            delete_path = delete_static_path + nbr_request_path[attr][dict_attr]
                            requests.append({'path': delete_path, 'method': DELETE})
                else:
                    delete_path = delete_static_path + nbr_request_path[attr]
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
