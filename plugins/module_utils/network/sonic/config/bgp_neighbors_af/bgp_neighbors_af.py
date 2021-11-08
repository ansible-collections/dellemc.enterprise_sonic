#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_bgp_neighbors_af class
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
from ansible.module_utils.connection import ConnectionError

PATCH = 'patch'
DELETE = 'delete'
TEST_KEYS = [
    {'config': {'vrf_name': '', 'bgp_as': ''}},
    {'neighbors': {'neighbor': ''}},
    {'address_family': {'afi': '', 'safi': ''}},
    {'route_map': {'name': '', 'direction': ''}},
]


class Bgp_neighbors_af(ConfigBase):
    """
    The sonic_bgp_neighbors_af class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'bgp_neighbors_af',
    ]

    network_instance_path = '/data/openconfig-network-instance:network-instances/network-instance'
    protocol_bgp_path = 'protocols/protocol=BGP,bgp/bgp'
    neighbor_path = 'neighbors/neighbor'
    afi_safi_path = 'afi-safis/afi-safi'
    activate_path = "/config/enabled"
    ref_client_path = "/config/openconfig-bgp-ext:route-reflector-client"
    serv_client_path = "/config/openconfig-bgp-ext:route-server-client"
    allowas_origin_path = "/openconfig-bgp-ext:allow-own-as/config/origin"
    allowas_value_path = "/openconfig-bgp-ext:allow-own-as/config/as-count"
    allowas_enabled_path = "/openconfig-bgp-ext:allow-own-as/config/enabled"

    def __init__(self, module):
        super(Bgp_neighbors_af, self).__init__(module)

    def get_bgp_neighbors_af_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        bgp_neighbors_af_facts = facts['ansible_network_resources'].get('bgp_neighbors_af')
        if not bgp_neighbors_af_facts:
            bgp_neighbors_af_facts = []
        return bgp_neighbors_af_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = list()
        existing_bgp_neighbors_af_facts = self.get_bgp_neighbors_af_facts()
        commands, requests = self.set_config(existing_bgp_neighbors_af_facts)
        if commands and len(requests) > 0:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        changed_bgp_neighbors_af_facts = self.get_bgp_neighbors_af_facts()

        result['before'] = existing_bgp_neighbors_af_facts
        if result['changed']:
            result['after'] = changed_bgp_neighbors_af_facts

        result['warnings'] = warnings
        return result

    def set_config(self, existing_bgp_neighbors_af_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']
        normalize_neighbors_interface_name(want, self._module)
        have = existing_bgp_neighbors_af_facts
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
        validate_bgps(self._module, want, have)
        requests = self.get_modify_bgp_neighbors_af_requests(commands, have)
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
        # if want is none, then delete all the bgp_neighbors_afs
        is_delete_all = False
        if not want:
            commands = have
            is_delete_all = True
        else:
            commands = want

        requests = self.get_delete_bgp_neighbors_af_requests(commands, have, is_delete_all)

        if commands and len(requests) > 0:
            commands = update_states(commands, "deleted")
        else:
            commands = []

        return commands, requests

    def set_val(self, cfg, var, src_key, des_key):
        value = var.get(src_key, None)
        if value is not None:
            cfg[des_key] = value

    def get_allowas_in(self, match, conf_neighbor_val, conf_afi, conf_safi):
        mat_allowas_in = None
        if match:
            mat_neighbors = match.get('neighbors', None)
            if mat_neighbors:
                mat_neighbor = next((nei for nei in mat_neighbors if nei['neighbor'] == conf_neighbor_val), None)
                if mat_neighbor:
                    mat_nei_addr_fams = mat_neighbor.get('address_family', [])
                    if mat_nei_addr_fams:
                        mat_nei_addr_fam = next((af for af in mat_nei_addr_fams if (af['afi'] == conf_afi and af['safi'] == conf_safi)), None)
                        if mat_nei_addr_fam:
                            mat_allowas_in = mat_nei_addr_fam.get('allowas_in', None)
        return mat_allowas_in

    def get_single_neighbors_af_modify_request(self, match, vrf_name, conf_neighbor_val, conf_neighbor):
        requests = []
        conf_nei_addr_fams = conf_neighbor.get('address_family', [])
        url = '%s=%s/%s/%s=%s/afi-safis' % (self.network_instance_path, vrf_name, self.protocol_bgp_path, self.neighbor_path, conf_neighbor_val)
        payload = {}
        afi_safis = []
        if not conf_nei_addr_fams:
            return requests

        for conf_nei_addr_fam in conf_nei_addr_fams:
            afi_safi = {}
            conf_afi = conf_nei_addr_fam.get('afi', None)
            conf_safi = conf_nei_addr_fam.get('safi', None)
            afi_safi_val = ("%s_%s" % (conf_afi, conf_safi)).upper()
            del_url = '%s=%s/%s/%s=%s/' % (self.network_instance_path, vrf_name, self.protocol_bgp_path, self.neighbor_path, conf_neighbor_val)
            del_url += '%s=openconfig-bgp-types:%s' % (self.afi_safi_path, afi_safi_val)

            afi_safi_cfg = {}
            if conf_afi and conf_safi:
                afi_safi_name = ("%s_%s" % (conf_afi, conf_safi)).upper()
                afi_safi['afi-safi-name'] = afi_safi_name
                afi_safi_cfg['afi-safi-name'] = afi_safi_name

                self.set_val(afi_safi_cfg, conf_nei_addr_fam, 'activate', 'enabled')
                self.set_val(afi_safi_cfg, conf_nei_addr_fam, 'route_reflector_client', 'openconfig-bgp-ext:route-reflector-client')
                self.set_val(afi_safi_cfg, conf_nei_addr_fam, 'route_server_client', 'openconfig-bgp-ext:route-server-client')

                if afi_safi_cfg:
                    afi_safi['config'] = afi_safi_cfg

                policy_cfg = {}
                conf_route_map = conf_nei_addr_fam.get('route_map', None)
                if conf_route_map:
                    for route in conf_route_map:
                        policy_key = "import-policy" if "in" == route['direction'] else "export-policy"
                        route_name = route['name']
                        policy_cfg[policy_key] = [route_name]
                if policy_cfg:
                    afi_safi['apply-policy'] = {'config': policy_cfg}

                allowas_in_cfg = {}
                conf_allowas_in = conf_nei_addr_fam.get('allowas_in', None)
                if conf_allowas_in:
                    mat_allowas_in = self.get_allowas_in(match, conf_neighbor_val, conf_afi, conf_safi)
                    origin = conf_allowas_in.get('origin', None)
                    if origin is not None:
                        if mat_allowas_in:
                            mat_value = mat_allowas_in.get('value', None)
                            if mat_value:
                                self.append_delete_request(requests, mat_value, mat_allowas_in, 'value', del_url, self.allowas_value_path)
                        allowas_in_cfg['origin'] = origin
                    else:
                        value = conf_allowas_in.get('value', None)
                        if value is not None:
                            if mat_allowas_in:
                                mat_origin = mat_allowas_in.get('origin', None)
                                if mat_origin:
                                    self.append_delete_request(requests, mat_origin, mat_allowas_in, 'origin', del_url, self.allowas_origin_path)
                            allowas_in_cfg['as-count'] = value
                if allowas_in_cfg:
                    allowas_in_cfg['enabled'] = True
                    afi_safi['openconfig-bgp-ext:allow-own-as'] = {'config': allowas_in_cfg}

            if afi_safi:
                afi_safis.append(afi_safi)

        if afi_safis:
            payload = {"openconfig-network-instance:afi-safis": {"afi-safi": afi_safis}}
            requests.append({'path': url, 'method': PATCH, 'data': payload})

        return requests

    def get_delete_neighbor_af_routemaps_requests(self, vrf_name, conf_neighbor_val, afi, safi, routes):
        requests = []
        for route in routes:
            afi_safi_name = ("%s_%s" % (afi, safi)).upper()
            policy_type = "import-policy" if "in" == route['direction'] else "export-policy"
            url = '%s=%s/%s/%s=%s/' % (self.network_instance_path, vrf_name, self.protocol_bgp_path, self.neighbor_path, conf_neighbor_val)
            url += ('%s=%s/apply-policy/config/%s' % (self.afi_safi_path, afi_safi_name, policy_type))
            requests.append({'path': url, 'method': DELETE})
        return requests

    def get_all_neighbors_af_modify_requests(self, match, conf_neighbors, vrf_name):
        requests = []
        for conf_neighbor in conf_neighbors:
            conf_neighbor_val = conf_neighbor.get('neighbor', None)
            if conf_neighbor_val:
                requests.extend(self.get_single_neighbors_af_modify_request(match, vrf_name, conf_neighbor_val, conf_neighbor))
        return requests

    def get_modify_requests(self, conf, match, vrf_name):
        requests = []
        conf_neighbors = conf.get('neighbors', [])
        mat_neighbors = []
        if match and match.get('neighbors', None):
            mat_neighbors = match.get('neighbors')

        if conf_neighbors:
            for conf_neighbor in conf_neighbors:
                conf_neighbor_val = conf_neighbor.get('neighbor', None)
                if conf_neighbor_val is None:
                    continue

                mat_neighbor = next((e_neighbor for e_neighbor in mat_neighbors if e_neighbor['neighbor'] == conf_neighbor_val), None)
                if mat_neighbor is None:
                    continue

                conf_nei_addr_fams = conf_neighbor.get('address_family', None)
                mat_nei_addr_fams = mat_neighbor.get('address_family', None)
                if conf_nei_addr_fams is None or mat_nei_addr_fams is None:
                    continue

                for conf_nei_addr_fam in conf_nei_addr_fams:
                    afi = conf_nei_addr_fam.get('afi', None)
                    safi = conf_nei_addr_fam.get('safi', None)
                    if afi is None or safi is None:
                        continue

                    mat_nei_addr_fam = next((addr_fam for addr_fam in mat_nei_addr_fams if (addr_fam['afi'] == afi and addr_fam['safi'] == safi)), None)
                    if mat_nei_addr_fam is None:
                        continue

                    conf_route_map = conf_nei_addr_fam.get('route_map', None)
                    mat_route_map = mat_nei_addr_fam.get('route_map', None)
                    if conf_route_map is None or mat_route_map is None:
                        continue

                    del_routes = []
                    for route in conf_route_map:
                        exist_route = next((e_route for e_route in mat_route_map if e_route['direction'] == route['direction']), None)
                        if exist_route:
                            del_routes.append(exist_route)
                    if del_routes:
                        requests.extend(self.get_delete_neighbor_af_routemaps_requests(vrf_name, conf_neighbor_val, afi, safi, del_routes))

            requests.extend(self.get_all_neighbors_af_modify_requests(match, conf_neighbors, vrf_name))
        return requests

    def get_modify_bgp_neighbors_af_requests(self, commands, have):
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

    def append_delete_request(self, requests, cur_var, mat_var, key, url, path):
        ret_value = False
        request = None
        if cur_var is not None and mat_var.get(key, None):
            requests.append({'path': url + path, 'method': DELETE})
            ret_value = True
        return ret_value

    def process_delete_specific_params(self, vrf_name, conf_neighbor_val, conf_nei_addr_fam, conf_afi, conf_safi, matched_nei_addr_fams, url):
        requests = []

        mat_nei_addr_fam = None
        if matched_nei_addr_fams:
            mat_nei_addr_fam = next((e_af for e_af in matched_nei_addr_fams if (e_af['afi'] == conf_afi and e_af['safi'] == conf_safi)), None)

        if mat_nei_addr_fam:
            conf_alllowas_in = conf_nei_addr_fam.get('allowas_in', None)
            conf_activate = conf_nei_addr_fam.get('activate', None)
            conf_route_map = conf_nei_addr_fam.get('route_map', None)
            conf_route_reflector_client = conf_nei_addr_fam.get('route_reflector_client', None)
            conf_route_server_client = conf_nei_addr_fam.get('route_server_client', None)

            var_list = [conf_alllowas_in, conf_activate, conf_route_map, conf_route_reflector_client, conf_route_server_client]
            if len(list(filter(lambda var: (var is None), var_list))) == len(var_list):
                requests.append({'path': url, 'method': DELETE})
            else:
                mat_route_map = mat_nei_addr_fam.get('route_map', None)
                if conf_route_map and mat_route_map:
                    del_routes = []
                    for route in conf_route_map:
                        if any(e_route for e_route in mat_route_map if route['direction'] == e_route['direction']):
                            del_routes.append(route)
                    if del_routes:
                        requests.extend(self.get_delete_neighbor_af_routemaps_requests(vrf_name, conf_neighbor_val, conf_afi, conf_safi, del_routes))

                self.append_delete_request(requests, conf_activate, mat_nei_addr_fam, 'activate', url, self.activate_path)
                self.append_delete_request(requests, conf_route_reflector_client, mat_nei_addr_fam, 'route_reflector_client', url, self.ref_client_path)
                self.append_delete_request(requests, conf_route_server_client, mat_nei_addr_fam, 'route_server_client', url, self.serv_client_path)

                mat_alllowas_in = mat_nei_addr_fam.get('allowas_in', None)
                if conf_alllowas_in is not None and mat_alllowas_in:
                    origin = conf_alllowas_in.get('origin', None)
                    if origin is not None:
                        if self.append_delete_request(requests, origin, mat_alllowas_in, 'origin', url, self.allowas_origin_path):
                            self.append_delete_request(requests, True, {'enabled': True}, 'enabled', url, self.allowas_enabled_path)
                    else:
                        value = conf_alllowas_in.get('value', None)
                        if value is not None:
                            if self.append_delete_request(requests, value, mat_alllowas_in, 'value', url, self.allowas_value_path):
                                self.append_delete_request(requests, True, {'enabled': True}, 'enabled', url, self.allowas_enabled_path)
        return requests

    def process_neighbor_delete_address_families(self, vrf_name, conf_nei_addr_fams, matched_nei_addr_fams, neighbor_val, is_delete_all):
        requests = []

        for conf_nei_addr_fam in conf_nei_addr_fams:
            conf_afi = conf_nei_addr_fam.get('afi', None)
            conf_safi = conf_nei_addr_fam.get('safi', None)
            if not conf_afi or not conf_safi:
                continue
            afi_safi = ("%s_%s" % (conf_afi, conf_safi)).upper()
            url = '%s=%s/%s/%s=%s/' % (self.network_instance_path, vrf_name, self.protocol_bgp_path, self.neighbor_path, neighbor_val)
            url += '%s=openconfig-bgp-types:%s' % (self.afi_safi_path, afi_safi)
            if is_delete_all:
                requests.append({'path': url, 'method': DELETE})
            else:
                requests.extend(self.process_delete_specific_params(vrf_name, neighbor_val, conf_nei_addr_fam, conf_afi, conf_safi, matched_nei_addr_fams, url))

        return requests

    def get_delete_single_bgp_neighbors_af_request(self, conf, is_delete_all, match=None):
        requests = []
        vrf_name = conf['vrf_name']
        conf_neighbors = conf.get('neighbors', [])

        if match and not conf_neighbors:
            conf_neighbors = match.get('neighbors', [])
            if conf_neighbors:
                conf_neighbors = [{'neighbor': nei['neighbor']} for nei in conf_neighbors]

        if not conf_neighbors:
            return requests
        mat_neighbors = None
        if match:
            mat_neighbors = match.get('neighbors', [])

        for conf_neighbor in conf_neighbors:
            conf_neighbor_val = conf_neighbor.get('neighbor', None)
            if not conf_neighbor_val:
                continue

            mat_neighbor = None
            if mat_neighbors:
                mat_neighbor = next((e_nei for e_nei in mat_neighbors if e_nei['neighbor'] == conf_neighbor_val), None)

            conf_nei_addr_fams = conf_neighbor.get('address_family', None)
            if mat_neighbor and not conf_nei_addr_fams:
                conf_nei_addr_fams = mat_neighbor.get('address_family', None)
                if conf_nei_addr_fams:
                    conf_nei_addr_fams = [{'afi': af['afi'], 'safi': af['safi']} for af in conf_nei_addr_fams]

            if not conf_nei_addr_fams:
                continue

            mat_nei_addr_fams = None
            if mat_neighbor:
                mat_nei_addr_fams = mat_neighbor.get('address_family', None)

            requests.extend(self.process_neighbor_delete_address_families(vrf_name, conf_nei_addr_fams, mat_nei_addr_fams, conf_neighbor_val, is_delete_all))

        return requests

    def get_delete_bgp_neighbors_af_requests(self, commands, have, is_delete_all):
        requests = []
        for cmd in commands:
            vrf_name = cmd['vrf_name']
            as_val = cmd['bgp_as']
            match = None
            if not is_delete_all:
                match = next((have_cfg for have_cfg in have if have_cfg['vrf_name'] == vrf_name and have_cfg['bgp_as'] == as_val), None)
            requests.extend(self.get_delete_single_bgp_neighbors_af_request(cmd, is_delete_all, match))
        return requests
