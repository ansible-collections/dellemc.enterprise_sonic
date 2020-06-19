#
# -*- coding: utf-8 -*-
# © Copyright 2020 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_vxlans class
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
from ansible_collections.dellemc.sonic.plugins.module_utils.network.sonic.facts.facts import Facts
from ansible_collections.dellemc.sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible_collections.dellemc.sonic.plugins.module_utils.network.sonic.utils.utils import (
    get_diff,
    update_states
)

PATCH = 'patch'
DELETE = 'DELETE'


class Vxlans(ConfigBase):
    """
    The sonic_vxlans class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'vxlans',
    ]

    def __init__(self, module):
        super(Vxlans, self).__init__(module)

    def get_vxlans_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        vxlans_facts = facts['ansible_network_resources'].get('vxlans')
        if not vxlans_facts:
            return []
        return vxlans_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = list()

        existing_vxlans_facts = self.get_vxlans_facts()
        commands, requests = self.set_config(existing_vxlans_facts)

        if commands and requests:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        changed_vxlans_facts = self.get_vxlans_facts()

        result['before'] = existing_vxlans_facts
        if result['changed']:
            result['after'] = changed_vxlans_facts

        result['warnings'] = warnings
        return result

    def set_config(self, existing_vxlans_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']
        have = existing_vxlans_facts
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
        state = self._module.params['state']

        diff = get_diff(want, have, ["name", "vni"])

        if state == 'overridden':
            commands, requests = self._state_overridden(want, have, diff)
        elif state == 'deleted':
            commands, requests = self._state_deleted(want, have, diff)
        elif state == 'merged':
            commands, requests = self._state_merged(want, have, diff)
        elif state == 'replaced':
            commands, requests = self._state_replaced(want, have, diff)

        return commands, requests

    def _state_replaced(self, want, have, diff):
        """ The command generator when state is replaced

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """

        requests = []
        commands = []

        commands_del = get_diff(have, want, ["name", "vni"])
        requests_del = []
        if commands_del:
            requests_del = self.get_delete_vxlan_request(commands_del, have)
        if requests_del:
            requests.extend(requests_del)
            commands_del = update_states(commands_del, "deleted")
            commands.extend(commands_del)

        commands_rep = diff
        requests_rep = []
        if commands_rep:
            requests_rep = self.get_create_vxlans_request(commands_rep, have)
        if requests_rep:
            requests.extend(requests_rep)
            commands_rep = update_states(commands_rep, "replaced")
            commands.extend(commands_rep)

        return commands, requests

    def _state_overridden(self, want, have, diff):
        """ The command generator when state is overridden

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        requests = []
        commands = []

        commands_del = get_diff(have, want, ["name", "vni"])
        requests_del = []
        if commands_del:
            requests_del = self.get_delete_vxlan_request(commands_del, have)
        if requests_del:
            requests.extend(requests_del)
            commands_del = update_states(commands_del, "deleted")
            commands.extend(commands_del)

        commands_over = diff
        requests_over = []
        if commands_over:
            requests_over = self.get_create_vxlans_request(commands_over, have)
        if requests_over:
            requests.extend(requests_over)
            commands_over = update_states(commands_over, "overridden")
            commands.extend(commands_over)

        return commands, requests

    def _state_merged(self, want, have, diff):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration at position-0
                  Requests necessary to merge to the current configuration
                  at position-1
        """
        commands = diff
        requests = self.get_create_vxlans_request(commands, have)

        if len(requests) == 0:
            commands = []

        if commands:
            commands = update_states(commands, "merged")

        return commands, requests

    def _state_deleted(self, want, have, diff):
        """ The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """

        # if want is none, then delete all the vlans
        if not want or len(have) == 0:
            commands = have
        else:
            commands = want

        requests = self.get_delete_vxlan_request(commands, have)
        if len(requests) == 0:
            commands = []

        if commands:
            commands = update_states(commands, "deleted")

        return commands, requests

    def get_create_vxlans_request(self, configs, have):
        requests = []

        if not configs:
            return requests

        tunnel_requests = self.get_create_tunnel_request(configs, have)
        vlan_map_requests = self.get_create_vlan_map_request(configs, have)
        vrf_map_requests = self.get_create_vrf_map_request(configs, have)

        if tunnel_requests:
            requests.extend(tunnel_requests)
        if vlan_map_requests:
            requests.extend(vlan_map_requests)
        if vrf_map_requests:
            requests.extend(vrf_map_requests)

        return requests

    def get_delete_vxlan_request(self, configs, have):
        requests = []

        if not configs:
            return requests

        vrf_map_requests = []
        vlan_map_requests = []
        tunnel_requests = []

        # Need to delette the in reverse order of creation.
        # vrfmap needs to be cleared before vlanmap
        # vlanmap needs to be cleared before tunnet(source-ip)
        for conf in configs:

            name = conf['name']
            src_ip = conf.get('source_ip', None)
            vlanmap_list = conf.get('vlanmap', [])
            vrfmap_list = conf.get('vrfmap', [])

            have_vlanmap_count = 0
            have_vrfmap_count = 0
            matched = next((each_vxlan for each_vxlan in have if each_vxlan['name'] == name), None)
            if matched:
                have_vlanmap = matched.get('vlanmap', [])
                have_vrfmap = matched.get('vrfmap', [])
                if have_vlanmap:
                    have_vlanmap_count = len(have_vlanmap)
                if have_vrfmap:
                    have_vrfmap_count = len(have_vrfmap)

            is_delete_all = (name and not vlanmap_list and not vrfmap_list and not src_ip)
            if is_delete_all:
                vrfmap_list = matched.get("vrfmap", [])
                vlanmap_list = matched.get("vlanmap", [])
                src_ip = matched.get("source_ip", None)

            if vrfmap_list:
                temp_vrf_map_requests = self.get_delete_vrf_map_request(conf, matched, name, vrfmap_list)
                if temp_vrf_map_requests:
                    vrf_map_requests.extend(temp_vrf_map_requests)
                    have_vrfmap_count -= len(temp_vrf_map_requests)
            if vlanmap_list:
                temp_vlan_map_requests = self.get_delete_vlan_map_request(conf, matched, name, vlanmap_list)
                if temp_vlan_map_requests:
                    vlan_map_requests.extend(temp_vlan_map_requests)
                    have_vlanmap_count -= len(temp_vlan_map_requests)
            if (src_ip or is_delete_all) and have_vlanmap_count == 0:
                tunnel_requests.extend(self.get_delete_tunnel_request(conf, matched, name, src_ip))

        if vrf_map_requests:
            requests.extend(vrf_map_requests)
        if vlan_map_requests:
            requests.extend(vlan_map_requests)
        if tunnel_requests:
            requests.extend(tunnel_requests)

        return requests

    def get_create_tunnel_request(self, configs, have):
        # Create URL and payload
        requests = []
        url = "data/sonic-vxlan:sonic-vxlan/VXLAN_TUNNEL/VXLAN_TUNNEL_LIST={}"
        method = PATCH
        for conf in configs:
            new_source_ip = conf.get('source_ip', None)
            if new_source_ip:
                name = conf.get('name')
                matched = next((each_vxlan for each_vxlan in have if each_vxlan['name'] == name), None)
                is_change_needed = True
                if matched:
                    matched_source_ip = matched.get('source_ip', None)
                    if matched_source_ip and matched_source_ip == new_source_ip:
                        is_change_needed = False

                if is_change_needed:
                    payload = self.build_create_tunnel_payload(conf)
                    request = {"path": url.format(name),
                               "method": method,
                               "data": payload
                               }
                    requests.append(request)

        return requests

    def build_create_tunnel_payload(self, conf):
        payload_url = dict()

        vtep_src_ip_dict = dict()
        vtep_src_ip_dict['name'] = conf['name']
        vtep_src_ip_dict['src_ip'] = conf['source_ip']

        payload_url['sonic-vxlan:VXLAN_TUNNEL_LIST'] = [vtep_src_ip_dict]

        return payload_url

    def get_create_vlan_map_request(self, configs, have):
        # Create URL and payload
        requests = []
        method = PATCH
        for conf in configs:
            new_vlan_map_list = conf.get('vlanmap', [])
            if new_vlan_map_list:
                for each_vlan_map in new_vlan_map_list:
                    name = conf['name']
                    vlan = each_vlan_map.get('vlan')
                    vni = each_vlan_map.get('vni')
                    matched = next((each_vxlan for each_vxlan in have if each_vxlan['name'] == name), None)

                    is_change_needed = True
                    if matched:
                        matched_vlan_map_list = matched.get('vlanmap', [])
                        if matched_vlan_map_list:
                            matched_vlan_map = next((e_vlan_map for e_vlan_map in matched_vlan_map_list if e_vlan_map['vni'] == vni), None)
                            if matched_vlan_map:
                                if matched_vlan_map['vlan'] == vlan:
                                    is_change_needed = False

                    if is_change_needed:
                        map_name = "map_{0}_Vlan{1}".format(vni, vlan)
                        payload = self.build_create_vlan_map_payload(conf, each_vlan_map)
                        url = "data/sonic-vxlan:sonic-vxlan/VXLAN_TUNNEL_MAP/VXLAN_TUNNEL_MAP_LIST={0},{1}".format(name, map_name)
                        request = {"path": url, "method": method, "data": payload}
                        requests.append(request)

        return requests

    def build_create_vlan_map_payload(self, conf, vlan_map):
        payload_url = dict()

        vlan_map_dict = dict()
        vlan_map_dict['name'] = conf['name']
        vlan_map_dict['mapname'] = "map_{0}_Vlan{1}".format(vlan_map['vni'], vlan_map['vlan'])
        vlan_map_dict['vlan'] = "Vlan{0}".format(vlan_map['vlan'])
        vlan_map_dict['vni'] = vlan_map['vni']

        payload_url['sonic-vxlan:VXLAN_TUNNEL_MAP_LIST'] = [vlan_map_dict]

        return payload_url

    def get_create_vrf_map_request(self, configs, have):
        # Create URL and payload
        requests = []
        method = PATCH
        for conf in configs:
            new_vrf_map_list = conf.get('vrfmap', [])
            if new_vrf_map_list:
                for each_vrf_map in new_vrf_map_list:
                    name = conf['name']
                    vrf = each_vrf_map.get('vrf')
                    vni = each_vrf_map.get('vni')
                    matched = next((each_vxlan for each_vxlan in have if each_vxlan['name'] == name), None)

                    is_change_needed = True
                    if matched:
                        matched_vrf_map_list = matched.get('vrfmap', [])
                        if matched_vrf_map_list:
                            matched_vrf_map = next((e_vrf_map for e_vrf_map in matched_vrf_map_list if e_vrf_map['vni'] == vni), None)
                            if matched_vrf_map:
                                if matched_vrf_map['vrf'] == vrf:
                                    is_change_needed = False

                    if is_change_needed:
                        payload = self.build_create_vrf_map_payload(conf, each_vrf_map)
                        url = "data/sonic-vrf:sonic-vrf/VRF/VRF_LIST={0}/vni".format(vrf)
                        request = {"path": url, "method": method, "data": payload}
                        requests.append(request)

        return requests

    def build_create_vrf_map_payload(self, conf, vrf_map):

        payload_url = dict({"sonic-vrf:vni": vrf_map['vni']})
        return payload_url

    def get_delete_tunnel_request(self, conf, matched, name, del_source_ip):
        # Create URL and payload
        requests = []

        url = "data/sonic-vxlan:sonic-vxlan/VXLAN_TUNNEL/VXLAN_TUNNEL_LIST={}"
        method = DELETE

        is_change_needed = False
        if matched:
            matched_source_ip = matched.get('source_ip', None)
            if matched_source_ip and matched_source_ip == del_source_ip:
                is_change_needed = True

        # tunnel is to be removed in delete all case
        if is_change_needed or not del_source_ip:
            request = {"path": url.format(name), "method": method}
            requests.append(request)

        return requests

    def get_delete_vlan_map_request(self, conf, matched, name, del_vlan_map_list):
        # Create URL and payload
        requests = []
        method = DELETE

        for each_vlan_map in del_vlan_map_list:
            vlan = each_vlan_map.get('vlan')
            vni = each_vlan_map.get('vni')

            is_change_needed = False
            if matched:
                matched_vlan_map_list = matched.get('vlanmap', None)
                if matched_vlan_map_list:
                    matched_vlan_map = next((e_vlan_map for e_vlan_map in matched_vlan_map_list if e_vlan_map['vni'] == vni), None)
                    if matched_vlan_map:
                        if matched_vlan_map['vlan'] == vlan:
                            is_change_needed = True

            if is_change_needed:
                map_name = "map_{0}_Vlan{1}".format(vni, vlan)
                url = "data/sonic-vxlan:sonic-vxlan/VXLAN_TUNNEL_MAP/VXLAN_TUNNEL_MAP_LIST={0},{1}".format(name, map_name)
                request = {"path": url, "method": method}
                requests.append(request)

        return requests

    def get_delete_vrf_map_request(self, conf, matched, name, del_vrf_map_list):
        # Create URL and payload
        requests = []
        method = DELETE

        for each_vrf_map in del_vrf_map_list:
            vrf = each_vrf_map.get('vrf')
            vni = each_vrf_map.get('vni')

            is_change_needed = False
            if matched:
                matched_vrf_map_list = matched.get('vrfmap', None)
                if matched_vrf_map_list:
                    matched_vrf_map = next((e_vrf_map for e_vrf_map in matched_vrf_map_list if e_vrf_map['vni'] == vni), None)
                    if matched_vrf_map:
                        if matched_vrf_map['vrf'] == vrf:
                            is_change_needed = True

            if is_change_needed:
                url = "data/sonic-vrf:sonic-vrf/VRF/VRF_LIST={0}/vni".format(vrf)
                request = {"path": url, "method": method}
                requests.append(request)

        return requests
