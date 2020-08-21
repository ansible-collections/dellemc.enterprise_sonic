#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_bgp_af class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from __future__ import absolute_import, division, print_function
__metaclass__ = type

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
from ansible_collections.dellemc.sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible_collections.dellemc.sonic.plugins.module_utils.network.sonic.utils.utils import (
    dict_to_set,
    update_states,
    get_diff,
    remove_empties_from_list,
)
from ansible_collections.dellemc.sonic.plugins.module_utils.network.sonic.sonic import to_request

PATCH = 'patch'
DELETE = 'delete'
test_keys = [
    {'config': {'vrf_name', 'bgp_as'}},
    {'address_family': {'afi', 'safi'}},
    {'redistribute': {'protocol'}},
    {'advertise_prefix': {'afi', 'safi'}},
]


class Bgp_af(ConfigBase):
    """
    The sonic_bgp_af class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'bgp_af',
    ]

    network_instance_path = '/data/openconfig-network-instance:network-instances/network-instance'
    protocol_bgp_path = 'protocols/protocol=BGP,bgp/bgp'
    l2vpn_evpn_config_path = 'l2vpn-evpn/openconfig-bgp-evpn-ext:config'
    afi_safi_path = 'global/afi-safis/afi-safi'
    table_connection_path = 'table-connections/table-connection'

    def __init__(self, module):
        super(Bgp_af, self).__init__(module)

    def get_bgp_af_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        bgp_af_facts = facts['ansible_network_resources'].get('bgp_af')
        if not bgp_af_facts:
            bgp_af_facts = []
        return bgp_af_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = list()
        existing_bgp_af_facts = self.get_bgp_af_facts()
        commands, requests = self.set_config(existing_bgp_af_facts)
        if commands and len(requests) > 0:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        changed_bgp_af_facts = self.get_bgp_af_facts()

        result['before'] = existing_bgp_af_facts
        if result['changed']:
            result['after'] = changed_bgp_af_facts

        result['warnings'] = warnings
        return result

    def set_config(self, existing_bgp_af_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']
        have = existing_bgp_af_facts
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

        diff = get_diff(want, have, test_keys)

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
        commands = diff
        requests = self.get_modify_bgp_af_requests(commands, have)
        if commands and len(requests) > 0:
            commands = update_states(commands, "merged")
        else:
            commands = []

        return commands, requests

    def _state_deleted(self, want, have, diff):
        """ The command generator when state is deleted

        :param want: the objects from which the configuration should be removed
        :param obj_in_have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        # if want is none, then delete all the bgp_afs
        is_delete_all = False
        if not want:
            commands = have
            is_delete_all = True
        else:
            commands = want

        requests = self.get_delete_bgp_af_requests(commands, have, is_delete_all)

        if commands and len(requests) > 0:
            commands = update_states(commands, "deleted")
        else:
            commands = []

        return commands, requests

    def get_address_family_modify_request(self, vrf_name, conf_afi, conf_safi):
        afi_safi = ("%s_%s" % (conf_afi, conf_safi)).upper()
        url = '%s=%s/%s/global' % (self.network_instance_path, vrf_name, self.protocol_bgp_path)
        afi_safi_load = {'afi-safi-name': ("openconfig-bgp-types:%s" % (afi_safi))}
        afi_safis_load = {'afi-safis': {'afi-safi': [afi_safi_load]}}
        pay_load = {'openconfig-network-instance:global': afi_safis_load}

        return({"path": url, "method": PATCH, "data": pay_load})

    def get_advertise_modify_request(self, vrf_name, conf_afi, conf_safi, conf_addr_fam):
        request = None
        conf_advertise_all_vni = conf_addr_fam.get('advertise_all_vni', None)
        conf_advertise_default_gw = conf_addr_fam.get('advertise_default_gw', None)
        conf_advt_list = conf_addr_fam.get('advertise_prefix', None)
        afi_safi = ("%s_%s" % (conf_afi, conf_safi)).upper()
        evpn_cfg = {}
        if conf_advertise_all_vni:
            evpn_cfg['advertise-all-vni'] = conf_advertise_all_vni

        if conf_advertise_default_gw:
            evpn_cfg['advertise-default-gw'] = conf_advertise_default_gw

        advertise_prefix_cfg = []
        if conf_advt_list is not None:
            for advertise_prefix in conf_advt_list:
                advertise_prefix_cfg.append("openconfig-bgp-types:" + ("%s_%s" % (advertise_prefix['afi'], advertise_prefix['safi'])).upper())
            if advertise_prefix_cfg:
                evpn_cfg['advertise-list'] = advertise_prefix_cfg

        if evpn_cfg:
            url = '%s=%s/%s/global' % (self.network_instance_path, vrf_name, self.protocol_bgp_path)
            afi_safi_load = {'afi-safi-name': ("openconfig-bgp-types:%s" % (afi_safi))}
            afi_safi_load['l2vpn-evpn'] = {'openconfig-bgp-evpn-ext:config': evpn_cfg}
            afi_safis_load = {'afi-safis': {'afi-safi': [afi_safi_load]}}
            pay_load = {'openconfig-network-instance:global': afi_safis_load}
            request = {"path": url, "method": PATCH, "data": pay_load}

        return request

    def get_redistribute_modify_requests(self, vrf_name, conf_afi, conf_safi, conf_redis_arr):
        requests = []
        url = "%s=%s/table-connections" % (self.network_instance_path, vrf_name)
        cfgs = []
        for conf_redis in conf_redis_arr:
            conf_metric = conf_redis.get('metric', None)
            if conf_metric is not None:
                conf_metric = float(conf_redis['metric'])

            afi_cfg = "openconfig-types:%s" % (conf_afi.upper())
            cfg_data = {'address-family': afi_cfg}
            cfg_data['dst-protocol'] = "openconfig-policy-types:BGP"
            conf_protocol = conf_redis['protocol'].upper()
            if conf_protocol == 'CONNECTED':
                conf_protocol = "DIRECTLY_CONNECTED"
            cfg_data['src-protocol'] = "openconfig-policy-types:%s" % (conf_protocol)
            if conf_metric is not None:
                config = {'address-family': afi_cfg}
                config['openconfig-network-instance-ext:metric'] = conf_metric
                cfg_data['config'] = config

            conf_route_map = conf_redis.get('route_map', None)
            if conf_route_map:
                config = cfg_data.get('config', {})
                if not config:
                    config = {'address-family': afi_cfg}
                config['import-policy'] = [conf_route_map]
                cfg_data['config'] = config

            cfgs.append(cfg_data)

        if cfgs:
            pay_load = {'openconfig-network-instance:table-connections': {'table-connection': cfgs}}
            requests.append({"path": url, "method": PATCH, "data": pay_load})
        return requests

    def get_single_af_modify_request(self, vrf_name, conf_afi, conf_safi, conf_addr_fam):
        requests = []
        conf_redis_arr = conf_addr_fam.get('redistribute', [])

        requests.append(self.get_address_family_modify_request(vrf_name, conf_afi, conf_safi))
        if conf_afi in ['ipv4', 'ipv6'] and conf_safi == 'unicast':
            if conf_redis_arr:
                requests.extend(self.get_redistribute_modify_requests(vrf_name, conf_afi, conf_safi, conf_redis_arr))
        elif conf_afi == "l2vpn" and conf_safi == 'evpn':
            advertise_req = self.get_advertise_modify_request(vrf_name, conf_afi, conf_safi, conf_addr_fam)
            if advertise_req:
                requests.append(advertise_req)

        return requests

    def get_all_af_modify_requests(self, conf_addr_fams, vrf_name):
        requests = []
        for conf_addr_fam in conf_addr_fams:
            conf_afi = conf_addr_fam.get('afi', None)
            conf_safi = conf_addr_fam.get('safi', None)
            if conf_afi and conf_safi:
                requests.extend(self.get_single_af_modify_request(vrf_name, conf_afi, conf_safi, conf_addr_fam))
        return requests

    def get_modify_requests(self, conf, match, vrf_name):
        requests = []
        payload = {}
        conf_addr_fams = conf.get('address_family', [])
        mat_addr_fams = []
        if match:
            mat_addr_fams = match.get('address_family', [])

        if conf_addr_fams and not mat_addr_fams:
            requests.extend(self.get_all_af_modify_requests(conf_addr_fams, vrf_name))
        else:
            for conf_addr_fam in conf_addr_fams:
                conf_afi = conf_addr_fam.get('afi', None)
                conf_safi = conf_addr_fam.get('safi', None)

                if conf_afi is None or conf_safi is None:
                    continue

                mat_addr_fam = next((e_addr_fam for e_addr_fam in mat_addr_fams if (e_addr_fam['afi'] == conf_afi and e_addr_fam['safi'] == conf_safi)), None)

                if mat_addr_fam is None:
                    requests.extend(self.get_single_af_modify_request(vrf_name, conf_afi, conf_safi, conf_addr_fam))
                    continue

                if conf_afi == "l2vpn" and conf_safi == "evpn":
                    advertise_req = self.get_advertise_modify_request(vrf_name, conf_afi, conf_safi, conf_addr_fam)
                    if advertise_req:
                        requests.append(advertise_req)
                elif conf_afi in ["ipv4", "ipv6"] and conf_safi == "unicast":
                    conf_redis_arr = conf_addr_fam.get('redistribute', [])
                    if not conf_redis_arr:
                        continue

                    url = "%s=%s/table-connections" % (self.network_instance_path, vrf_name)
                    pay_loads = []
                    modify_redis_arr = []
                    for conf_redis in conf_redis_arr:
                        conf_metric = conf_redis.get('metric', None)
                        if conf_metric is not None:
                            conf_metric = float(conf_redis['metric'])

                        conf_route_map = conf_redis.get('route_map', None)

                        have_redis_arr = mat_addr_fam.get('redistribute', [])
                        have_redis = None
                        have_route_map = None
                        # Check the route_map, if existing route_map is different from required route_map, delete the existing route map
                        if conf_route_map and have_redis_arr:
                            have_redis = next((redis_cfg for redis_cfg in have_redis_arr if conf_redis['protocol'] == redis_cfg['protocol']), None)
                            if have_redis:
                                have_route_map = have_redis.get('route_map', None)
                                if have_route_map and have_route_map != conf_route_map:
                                    requests.append(self.get_delete_route_map_request(vrf_name, conf_afi, have_redis, have_route_map))

                        modify_redis = {}
                        if conf_metric is not None:
                            modify_redis['metric'] = conf_metric
                        if conf_route_map:
                            modify_redis['route_map'] = conf_route_map

                        if modify_redis:
                            modify_redis['protocol'] = conf_redis['protocol']
                            modify_redis_arr.append(modify_redis)

                    if modify_redis_arr:
                        requests.extend(self.get_redistribute_modify_requests(vrf_name, conf_afi, conf_safi, modify_redis_arr))

        return requests

    def get_modify_bgp_af_requests(self, commands, have):
        requests = []
        if not commands:
            return requests

        # Create URL and payload
        for conf in commands:
            vrf_name = conf['vrf_name']
            as_val = conf['bgp_as']

            match = next((cfg for cfg in have if (cfg['vrf_name'] == vrf_name and (cfg['bgp_as'] == as_val))), None)
            modify_reqs = self.get_modify_requests(conf, match, vrf_name)
            if modify_reqs:
                requests.extend(modify_reqs)

        return requests

    def get_advertise_list_delete_request(self, vrf_name, conf_afi, conf_safi, conf_advt_list=None, mat_advt_list=None):
        requests = []
        afi_safi = ("%s_%s" % (conf_afi, conf_safi)).upper()
        url = '%s=%s/%s' % (self.network_instance_path, vrf_name, self.protocol_bgp_path)
        url += '/%s=%s/%s/advertise-list' % (self.afi_safi_path, afi_safi, self.l2vpn_evpn_config_path)

        if conf_advt_list and mat_advt_list:
            del_advertise_list = []
            existing_list_len = len(mat_advt_list)
            for advertise in conf_advt_list:
                diff = get_diff({'advertise_prefix': [advertise]}, {'advertise_prefix': mat_advt_list}, [{'advertise_prefix': {'afi', 'safi'}}])
                if not diff:
                    del_advertise_list.append(advertise)
            del_advertise_list_len = len(del_advertise_list)
            if existing_list_len > 0 and existing_list_len == del_advertise_list_len:
                requests.append({"path": url, "method": DELETE})
            else:
                for del_advertise in del_advertise_list:
                    del_afi_safi = ("=%s_%s" % (del_advertise['afi'], del_advertise['safi'])).upper()
                    url += del_afi_safi
                    requests.append({"path": url, "method": DELETE})
        else:
            requests.append({"path": url, "method": DELETE})

        return requests

    def get_advertise_default_gw_delete_request(self, vrf_name, conf_afi, conf_safi):
        afi_safi = ("%s_%s" % (conf_afi, conf_safi)).upper()
        url = '%s=%s/%s' % (self.network_instance_path, vrf_name, self.protocol_bgp_path)
        url += '/%s=%s/%s/advertise-default-gw' % (self.afi_safi_path, afi_safi, self.l2vpn_evpn_config_path)

        return({"path": url, "method": DELETE})

    def get_advertise_all_vni_delete_request(self, vrf_name, conf_afi, conf_safi):
        afi_safi = ("%s_%s" % (conf_afi, conf_safi)).upper()
        url = '%s=%s/%s' % (self.network_instance_path, vrf_name, self.protocol_bgp_path)
        url += '/%s=%s/%s/advertise-all-vni' % (self.afi_safi_path, afi_safi, self.l2vpn_evpn_config_path)

        return({"path": url, "method": DELETE})

    def get_address_family_delete_request(self, vrf_name, conf_afi, conf_safi):
        request = None
        if conf_afi != "l2vpn":
            afi_safi = ("%s_%s" % (conf_afi, conf_safi)).upper()
            url = '%s=%s/%s' % (self.network_instance_path, vrf_name, self.protocol_bgp_path)
            url += '/%s=openconfig-bgp-types:%s' % (self.afi_safi_path, afi_safi)
            request = {"path": url, "method": DELETE}

        return request

    def get_delete_single_bgp_af_request(self, conf, is_delete_all, match=None):
        requests = []
        vrf_name = conf['vrf_name']

        conf_addr_fams = conf.get('address_family', [])

        if not conf_addr_fams:
            return requests

        for conf_addr_fam in conf_addr_fams:
            conf_afi = conf_addr_fam.get('afi', None)
            conf_safi = conf_addr_fam.get('safi', None)
            if not conf_afi or not conf_safi:
                continue
            conf_redis_arr = conf_addr_fam.get('redistribute', [])
            conf_advertise_all_vni = conf_addr_fam.get('advertise_all_vni', None)
            conf_advertise_default_gw = conf_addr_fam.get('advertise_default_gw', None)
            conf_advt_list = conf_addr_fam.get('advertise_prefix', [])
            if is_delete_all:
                if conf_advertise_all_vni:
                    requests.append(self.get_advertise_all_vni_delete_request(vrf_name, conf_afi, conf_safi))
                if conf_advertise_default_gw:
                    requests.append(self.get_advertise_default_gw_delete_request(vrf_name, conf_afi, conf_safi))
                if conf_advt_list:
                    requests.extend(self.get_advertise_list_delete_request(vrf_name, conf_afi, conf_safi))
                if conf_redis_arr:
                    requests.extend(self.get_redistribute_delete_requests(vrf_name, conf_afi, conf_safi, conf_redis_arr, is_delete_all, None))
                addr_family_del_req = self.get_address_family_delete_request(vrf_name, conf_afi, conf_safi)
                if addr_family_del_req:
                    requests.append(addr_family_del_req)
            elif match:
                match_addr_fams = match.get('address_family', [])
                if not match_addr_fams:
                    continue
                for match_addr_fam in match_addr_fams:
                    mat_afi = match_addr_fam.get('afi', None)
                    mat_safi = match_addr_fam.get('safi', None)
                    if mat_afi and mat_safi and mat_afi == conf_afi and mat_safi == conf_safi:
                        mat_advt_all_vni = match_addr_fam.get('advertise_all_vni', None)
                        mat_redis_arr = match_addr_fam.get('redistribute', [])
                        mat_advt_defaut_gw = match_addr_fam.get('advertise_default_gw', None)
                        mat_advt_list = match_addr_fam.get('advertise_prefix', [])
                        if conf_advertise_all_vni is None and conf_redis_arr is None and conf_advertise_default_gw is None and conf_advt_list is None:
                            if mat_advt_all_vni is not None:
                                requests.append(self.get_advertise_all_vni_delete_request(vrf_name, conf_afi, conf_safi))
                            if mat_advt_defaut_gw:
                                requests.append(self.get_advertise_default_gw_delete_request(vrf_name, conf_afi, conf_safi))
                            if mat_advt_list:
                                requests.extend(self.get_advertise_list_delete_request(vrf_name, conf_afi, conf_safi))
                            if mat_redis_arr:
                                requests.extend(self.get_redistribute_delete_requests(vrf_name, conf_afi, conf_safi, mat_redis_arr, False, mat_redis_arr))
                            addr_family_del_req = self.get_address_family_delete_request(vrf_name, conf_afi, conf_safi)
                            if addr_family_del_req:
                                requests.append(addr_family_del_req)
                        else:
                            if conf_advertise_all_vni and mat_advt_all_vni:
                                requests.append(self.get_advertise_all_vni_delete_request(vrf_name, conf_afi, conf_safi))
                            if conf_advertise_default_gw and mat_advt_defaut_gw:
                                requests.append(self.get_advertise_default_gw_delete_request(vrf_name, conf_afi, conf_safi))
                            if conf_advt_list is not None and mat_advt_list is not None:
                                requests.extend(self.get_advertise_list_delete_request(vrf_name, conf_afi, conf_safi, conf_advt_list, mat_advt_list))
                            if conf_redis_arr and mat_redis_arr:
                                requests.extend(self.get_redistribute_delete_requests(vrf_name, conf_afi, conf_safi, conf_redis_arr, False, mat_redis_arr))
                        break

        return requests

    def get_delete_route_map_request(self, vrf_name, conf_afi, conf_redis, conf_route_map):
        addr_family = "openconfig-types:%s" % (conf_afi.upper())
        conf_protocol = conf_redis['protocol'].upper()
        if conf_protocol == 'CONNECTED':
            conf_protocol = "DIRECTLY_CONNECTED"
        src_protocol = "openconfig-policy-types:%s" % (conf_protocol)
        dst_protocol = "openconfig-policy-types:BGP"
        url = '%s=%s/%s=' % (self.network_instance_path, vrf_name, self.table_connection_path)
        url += '%s,%s,%s/config/import-policy=%s' % (src_protocol, dst_protocol, addr_family, conf_route_map)
        return({'path': url, 'method': DELETE})

    def get_redistribute_delete_requests(self, vrf_name, conf_afi, conf_safi, conf_redis_arr, is_delete_all, mat_redis_arr):
        requests = []
        for conf_redis in conf_redis_arr:
            addr_family = "openconfig-types:%s" % (conf_afi.upper())
            conf_protocol = conf_redis['protocol'].upper()

            ext_metric_flag = False
            ext_route_flag = False
            mat_redis = None
            mat_metric = None
            mat_route_map = None
            if not is_delete_all:
                mat_redis = next((redis_cfg for redis_cfg in mat_redis_arr if redis_cfg['protocol'].upper() == conf_protocol), None)
                if mat_redis:
                    mat_metric = mat_redis.get('metric', None)
                    mat_route_map = mat_redis.get('route_map', None)
                    if mat_metric:
                        ext_metric_flag = True
                    if mat_route_map:
                        ext_route_flag = True

            if conf_protocol == 'CONNECTED':
                conf_protocol = "DIRECTLY_CONNECTED"

            src_protocol = "openconfig-policy-types:%s" % (conf_protocol)
            dst_protocol = "openconfig-policy-types:BGP"

            conf_route_map = conf_redis.get('route_map', None)
            conf_metric = conf_redis.get('metric', None)
            if conf_metric is not None:
                conf_metric = float(conf_redis['metric'])

            url = '%s=%s/%s=' % (self.network_instance_path, vrf_name, self.table_connection_path)

            new_metric_flag = conf_metric is not None
            new_route_flag = conf_route_map is not None
            is_delete_protocol = False
            if is_delete_all:
                is_delete_protocol = conf_metric is not None or conf_route_map
            else:
                is_delete_protocol = (new_metric_flag == ext_metric_flag) and (new_route_flag == ext_route_flag)

            if is_delete_protocol:
                url += '%s,%s,%s' % (src_protocol, dst_protocol, addr_family)
                requests.append({'path': url, 'method': DELETE})
                continue

            if new_metric_flag and ext_metric_flag:
                url += '%s,%s,%s/config/openconfig-network-instance-ext:metric' % (src_protocol, dst_protocol, addr_family)
                requests.append({'path': url, 'method': DELETE})

            if new_route_flag and ext_route_flag:
                url += '%s,%s,%s/config/import-policy=%s' % (src_protocol, dst_protocol, addr_family, conf_route_map)
                requests.append({'path': url, 'method': DELETE})

        return requests

    def get_delete_bgp_af_requests(self, commands, have, is_delete_all):
        requests = []
        for cmd in commands:
            vrf_name = cmd['vrf_name']
            as_val = cmd['bgp_as']
            match_cfg = None
            if not is_delete_all:
                match_cfg = next((have_cfg for have_cfg in have if have_cfg['vrf_name'] == vrf_name and have_cfg['bgp_as'] == as_val), None)
            requests.extend(self.get_delete_single_bgp_af_request(cmd, is_delete_all, match_cfg))
        return requests
