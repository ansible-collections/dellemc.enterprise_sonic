#
# -*- coding: utf-8 -*-
# © Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_vxlans class
It is in this file where the current configuration (as list)
is compared to the provided configuration (as list) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from __future__ import absolute_import, division, print_function
__metaclass__ = type

from copy import deepcopy
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
    get_diff,
    update_states,
    get_replaced_config,
    remove_empties_from_list,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.formatted_diff_utils import (
    __DELETE_OP_DEFAULT,
    __DELETE_CONFIG_IF_NO_SUBCONFIG,
    get_new_config,
    get_formatted_config_diff
)
from ansible.module_utils.connection import ConnectionError

delete_all = False
VXLAN_PATH = 'data/sonic-vxlan:sonic-vxlan'
PATCH = 'patch'
DELETE = 'delete'
TEST_KEYS = [
    {'config': {'name': ''}},
    {'vlan_map': {'vlan': '', 'vni': ''}},
    {'vrf_map': {'vni': '', 'vrf': ''}},
    {'suppress_vlan_neigh': {'vlan_name': ''}},
]


def __derive_config_delete_op(key_set, command, exist_conf):
    if delete_all:
        return True, []
    else:
        return __DELETE_OP_DEFAULT(key_set, command, exist_conf)


test_keys_generate_config = [
    {'config': {'name': '', '__delete_op': __derive_config_delete_op}},
    {'vlan_map': {'vlan': '', 'vni': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}},
    {'vrf_map': {'vni': '', 'vrf': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}},
    {'suppress_vlan_neigh': {'vlan_name': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}},
]


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

        :rtype: A list
        :returns: The current configuration as a list
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
        result['before'] = existing_vxlans_facts
        old_config = existing_vxlans_facts

        if self._module.check_mode:
            new_config = self.post_process_generated_config(get_new_config(commands, existing_vxlans_facts, test_keys_generate_config))
            self.sort_lists_in_config(new_config)
            result['after_generated'] = new_config
        else:
            new_config = self.get_vxlans_facts()
            if result['changed']:
                result['after'] = new_config
        if self._module._diff:
            self.sort_lists_in_config(new_config)
            self.sort_lists_in_config(old_config)
            result['diff'] = get_formatted_config_diff(old_config, new_config, self._module._verbosity)
        return result

    def set_config(self, existing_vxlans_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = remove_empties_from_list(self._module.params['config'])
        have = existing_vxlans_facts
        resp = self.set_state(want, have)
        return to_list(resp)

    def set_state(self, want, have):
        """ Select the appropriate function based on the state provided

        :param want: the desired configuration as a list
        :param have: the current configuration as a list
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        state = self._module.params['state']
        diff = get_diff(want, have, TEST_KEYS)

        if state == 'overridden':
            commands, requests = self._state_overridden(want, have, diff)
        elif state == 'deleted':
            commands, requests = self._state_deleted(want, have, diff)
        elif state == 'merged':
            commands, requests = self._state_merged(have, diff)
        elif state == 'replaced':
            commands, requests = self._state_replaced(want, have, diff)

        return commands, requests

    def _state_replaced(self, want, have, diff):
        """ The command generator when state is replaced

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands, requests, mod_commands = [], [], []
        cp_want = deepcopy(want)
        cp_have = deepcopy(have)
        self.remove_default_entries(cp_want)
        self.remove_default_entries(cp_have)
        replaced_config = get_replaced_config(cp_want, cp_have, TEST_KEYS)

        if replaced_config:
            requests.extend(self.get_delete_vxlan_requests(replaced_config, False))
            commands.extend(update_states(replaced_config, 'deleted'))
            mod_commands = want
        else:
            mod_commands = diff

        if mod_commands:
            mod_requests = self.get_create_vxlans_requests(mod_commands, have)

            if mod_requests:
                requests.extend(mod_requests)
                commands.extend(update_states(mod_commands, 'replaced'))

        return commands, requests

    def _state_overridden(self, want, have, diff):
        """ The command generator when state is overridden

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        global delete_all
        delete_all = False
        commands, requests = [], []
        mod_commands, mod_requests = None, None
        del_commands = get_diff(have, want, TEST_KEYS)
        self.remove_default_entries(del_commands)

        if del_commands:
            delete_all = True
            del_requests = self.get_delete_vxlan_requests(del_commands, delete_all)
            requests.extend(del_requests)
            commands.extend(update_states(have, 'deleted'))
            have = []
            mod_commands = want
            mod_requests = self.get_create_vxlans_requests(mod_commands, have)
        elif diff:
            mod_commands = diff
            mod_requests = self.get_create_vxlans_requests(mod_commands, have)

        if mod_requests:
            requests.extend(mod_requests)
            commands.extend(update_states(mod_commands, 'overridden'))

        return commands, requests

    def _state_merged(self, have, diff):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = diff
        requests = self.get_create_vxlans_requests(commands, have)

        if commands and requests:
            commands = update_states(commands, 'merged')
        else:
            commands = []

        return commands, requests

    def _state_deleted(self, want, have, diff):
        """ The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        global delete_all
        delete_all = False
        commands, requests = [], []

        if not have:
            return commands, requests

        if not want:
            commands = deepcopy(have)
            delete_all = True
        else:
            commands = get_diff(want, diff, TEST_KEYS)
            self.remove_default_entries(commands)

        if commands:
            requests = self.get_delete_vxlan_requests(commands, delete_all)
            if len(requests) > 0:
                commands = update_states(commands, 'deleted')
        else:
            commands = []

        return commands, requests

    def get_create_vxlans_requests(self, configs, have):
        """Returns patch requests to modify VXLANs configuration"""
        requests = []

        if not configs:
            return requests

        tunnel_requests = self.get_create_tunnel_requests(configs, have)
        vlan_map_requests = self.get_create_vlan_map_requests(configs)
        vrf_map_requests = self.get_create_vrf_map_requests(configs)
        suppress_vlan_neigh_requests = self.get_create_suppress_vlan_neigh_requests(configs)

        if tunnel_requests:
            requests.extend(tunnel_requests)
        if vlan_map_requests:
            requests.extend(vlan_map_requests)
        if vrf_map_requests:
            requests.extend(vrf_map_requests)
        if suppress_vlan_neigh_requests:
            requests.extend(suppress_vlan_neigh_requests)

        return requests

    def get_delete_vxlan_requests(self, configs, is_delete_all):
        requests = []

        if not configs:
            return requests

        if is_delete_all:
            for conf in configs:
                if conf.get('vrf_map'):
                    requests.extend(self.get_delete_vrf_map_requests(conf['vrf_map']))
            requests.append({'path': VXLAN_PATH, 'method': DELETE})
            return requests

        # Need to delete in the reverse order of creation.
        # vrf_map needs to be cleared before vlan_map
        # vlan_map needs to be cleared before tunnel(source-ip)
        for conf in configs:
            name = conf['name']
            if len(conf) == 1:
                requests.append(self.get_delete_tunnel_request(name))
                continue

            src_ip = conf.get('source_ip')
            evpn_nvo = conf.get('evpn_nvo')
            primary_ip = conf.get('primary_ip')
            external_ip = conf.get('external_ip')
            qos_mode = conf.get('qos_mode')
            dscp = conf.get('dscp')
            vlan_map_list = conf.get('vlan_map')
            vrf_map_list = conf.get('vrf_map')
            suppress_vlan_neigh_list = conf.get('suppress_vlan_neigh')

            if suppress_vlan_neigh_list:
                requests.extend(self.get_delete_suppress_vlan_neigh_requests(suppress_vlan_neigh_list))
            if vrf_map_list:
                requests.extend(self.get_delete_vrf_map_requests(vrf_map_list))
            if vlan_map_list:
                requests.extend(self.get_delete_vlan_map_requests(name, vlan_map_list))
            if src_ip:
                requests.append(self.get_delete_tunnel_request(name, 'src_ip'))
            if evpn_nvo:
                requests.append(self.get_delete_evpn_request(evpn_nvo))
            if primary_ip:
                requests.append(self.get_delete_tunnel_request(name, 'primary_ip'))
            if external_ip:
                requests.append(self.get_delete_tunnel_request(name, 'external_ip'))
            if qos_mode:
                requests.append(self.get_delete_tunnel_request(name, 'qos-mode'))
            if dscp:
                requests.append(self.get_delete_tunnel_request(name, 'dscp'))

        return requests

    def get_create_evpn_request(self, evpn_nvo, name):
        """Returns a patch request to modify evpn_nvo configuration"""
        url = f'{VXLAN_PATH}/VXLAN_EVPN_NVO/VXLAN_EVPN_NVO_LIST'
        evpn_nvo_list = [{'name': evpn_nvo, 'source_vtep': name}]
        payload = {'sonic-vxlan:VXLAN_EVPN_NVO_LIST': evpn_nvo_list}
        request = {'path': url, 'method': PATCH, 'data': payload}

        return request

    def get_create_tunnel_requests(self, configs, have):
        """Returns patch requests to modify tunnel configuration"""
        requests = []
        url = f'{VXLAN_PATH}/VXLAN_TUNNEL'
        have_evpn_nvo_dict = {conf.get('name'): conf['evpn_nvo'] for conf in have if conf.get('evpn_nvo')}

        for conf in configs:
            vtep_ip_dict = {}
            vtep_ip_dict['name'] = conf['name']

            if conf.get('source_ip'):
                vtep_ip_dict['src_ip'] = conf['source_ip']
            if conf.get('primary_ip'):
                vtep_ip_dict['primary_ip'] = conf['primary_ip']
            if conf.get('external_ip'):
                vtep_ip_dict['external_ip'] = conf['external_ip']
            if conf.get('qos_mode'):
                vtep_ip_dict['qos-mode'] = conf['qos_mode']
                if conf['qos_mode'] == 'uniform':
                    vtep_ip_dict['dscp'] = 0
            if conf.get('dscp') is not None:
                if conf.get('qos_mode') == 'uniform':
                    self._module.fail_json(msg='DSCP is only configurable when qos_mode is pipe.')
                vtep_ip_dict['dscp'] = conf['dscp']
            if vtep_ip_dict:
                payload = {'sonic-vxlan:VXLAN_TUNNEL': {'VXLAN_TUNNEL_LIST': [vtep_ip_dict]}}
                request = {'path': url, 'method': PATCH, 'data': payload}
                requests.append(request)
            if conf.get('evpn_nvo'):
                requests.append(self.get_create_evpn_request(conf['evpn_nvo'], conf['name']))
            # Create evpn_nvo if not specified or not already configured when source_ip is specified
            elif conf.get('source_ip') and not have_evpn_nvo_dict.get(conf['name']):
                requests.append(self.get_create_evpn_request('nvo1', conf['name']))

        return requests

    def get_create_vlan_map_requests(self, configs):
        """Returns patch requests to modify vlan_map configuration"""
        requests = []

        for conf in configs:
            new_vlan_map_list = conf.get('vlan_map')

            if new_vlan_map_list:
                for vlan_map in new_vlan_map_list:
                    payload = self.build_create_vlan_map_payload(conf, vlan_map)
                    url = f'{VXLAN_PATH}/VXLAN_TUNNEL_MAP'
                    request = {'path': url, 'method': PATCH, 'data': payload}
                    requests.append(request)

        return requests

    def build_create_vlan_map_payload(self, conf, vlan_map):
        """Returns vlan_map payload"""
        payload_url, vlan_map_dict = {}, {}
        vlan_map_dict['name'] = conf['name']
        vlan_map_dict['mapname'] = f"map_{vlan_map['vni']}_Vlan{vlan_map['vlan']}"
        vlan_map_dict['vlan'] = f"Vlan{vlan_map['vlan']}"
        vlan_map_dict['vni'] = vlan_map['vni']

        payload_url['sonic-vxlan:VXLAN_TUNNEL_MAP'] = {'VXLAN_TUNNEL_MAP_LIST': [vlan_map_dict]}

        return payload_url

    def get_create_vrf_map_requests(self, configs):
        """Returns patch requests to modify vrf_map configuration"""
        requests = []

        for conf in configs:
            new_vrf_map_list = conf.get('vrf_map')

            if new_vrf_map_list:
                for vrf_map in new_vrf_map_list:
                    vrf = vrf_map.get('vrf')
                    payload = self.build_create_vrf_map_payload(vrf_map)
                    url = f'data/sonic-vrf:sonic-vrf/VRF/VRF_LIST={vrf}/vni'
                    request = {'path': url, 'method': PATCH, 'data': payload}
                    requests.append(request)

        return requests

    def build_create_vrf_map_payload(self, vrf_map):
        """Returns vrf_map payload"""
        payload_url = {'sonic-vrf:vni': vrf_map['vni']}
        return payload_url

    def get_create_suppress_vlan_neigh_requests(self, configs):
        """Returns patch requests to modify suppress_vlan_neigh configuration"""
        requests, vlan_list = [], []
        payload = {}

        for conf in configs:
            new_suppress_vlan_neigh_list = conf.get('suppress_vlan_neigh', [])
            if new_suppress_vlan_neigh_list:
                for each_suppress_vlan_neigh in new_suppress_vlan_neigh_list:
                    vlan_name = each_suppress_vlan_neigh.get('vlan_name')
                    vlan_list.append(vlan_name)

                payload.update(self.build_create_suppress_vlan_neigh_payload(vlan_list))
                url = f'{VXLAN_PATH}/SUPPRESS_VLAN_NEIGH'
                request = {'path': url, 'method': PATCH, 'data': payload}
                requests.append(request)

        return requests

    def build_create_suppress_vlan_neigh_payload(self, vlan_list):
        """Returns suppress_vlan_neigh payload"""
        payload_url = {}
        vlans = []

        for vlan in vlan_list:
            suppress_vlan_neigh_dict = {}
            suppress_vlan_neigh_dict['name'] = vlan
            suppress_vlan_neigh_dict['suppress'] = 'on'
            vlans.append(suppress_vlan_neigh_dict)
        payload_url['sonic-vxlan:SUPPRESS_VLAN_NEIGH'] = {'SUPPRESS_VLAN_NEIGH_LIST': vlans}
        return payload_url

    @staticmethod
    def get_delete_evpn_request(evpn_nvo):
        """Returns a delete request to delete the specified evpn_nvo configuration"""
        url = f'{VXLAN_PATH}/VXLAN_EVPN_NVO/VXLAN_EVPN_NVO_LIST={evpn_nvo}'
        request = {'path': url, 'method': DELETE}

        return request

    @staticmethod
    def get_delete_tunnel_request(name, attr=None):
        """Returns a delete request to delete the specified tunnel configuration"""
        url = f'{VXLAN_PATH}/VXLAN_TUNNEL/VXLAN_TUNNEL_LIST={name}'
        if attr:
            url += f'/{attr}'
        request = {'path': url, 'method': DELETE}

        return request

    @staticmethod
    def get_delete_vlan_map_requests(name, vlan_map_list):
        """Returns delete requests to delete the specified vlan_map configuration"""
        requests = []

        for vlan_map in vlan_map_list:
            vlan = vlan_map.get('vlan')
            vni = vlan_map.get('vni')
            map_name = f'map_{vni}_Vlan{vlan}'
            url = f'{VXLAN_PATH}/VXLAN_TUNNEL_MAP/VXLAN_TUNNEL_MAP_LIST={name},{map_name}'
            requests.append({'path': url, 'method': DELETE})

        return requests

    @staticmethod
    def get_delete_vrf_map_requests(vrf_map_list):
        """Returns delete requests to delete the specified vrf_map configuration"""
        requests = []

        for vrf_map in vrf_map_list:
            vrf = vrf_map.get('vrf')
            url = f'data/sonic-vrf:sonic-vrf/VRF/VRF_LIST={vrf}/vni'
            requests.append({'path': url, 'method': DELETE})

        return requests

    @staticmethod
    def get_delete_suppress_vlan_neigh_requests(suppress_vlan_neigh_list):
        """Returns delete requests to delete the specified suppress_vlan_neigh configuration"""
        requests = []

        for suppress_vlan_neigh in suppress_vlan_neigh_list:
            vlan_name = suppress_vlan_neigh.get('vlan_name')
            url = f'{VXLAN_PATH}/SUPPRESS_VLAN_NEIGH/SUPPRESS_VLAN_NEIGH_LIST={vlan_name}'
            requests.append({'path': url, 'method': DELETE})

        return requests

    @staticmethod
    def sort_lists_in_config(config):
        """Sorts the lists in VXLANs configuration"""
        if config:
            config.sort(key=lambda x: x['name'])
            for cfg in config:
                if 'vlan_map' in cfg and cfg['vlan_map']:
                    cfg['vlan_map'].sort(key=lambda x: x['vni'])
                if 'vrf_map' in cfg and cfg['vrf_map']:
                    cfg['vrf_map'].sort(key=lambda x: x['vni'])
                if 'suppress_vlan_neigh' in cfg and cfg['suppress_vlan_neigh']:
                    cfg['suppress_vlan_neigh'].sort(key=lambda x: x['vlan_name'])

    def remove_default_entries(self, data):
        """Removes the default entries from data"""
        if data:
            pop_list = []
            for idx, conf in enumerate(data):
                popped = False
                if conf.get('qos_mode') == 'pipe':
                    conf.pop('qos_mode')
                    popped = True
                if conf.get('dscp') == 0:
                    conf.pop('dscp')
                    popped = True
                if len(conf) == 1 and popped:
                    pop_list.insert(0, idx)
            for idx in pop_list:
                data.pop(idx)

    def post_process_generated_config(self, configs):
        """Handle post processing for generated configuration"""
        confs = remove_empties_from_list(configs)
        if confs:
            for conf in confs:
                if 'name' in conf:
                    # Add defaults
                    if 'qos_mode' not in conf:
                        conf['qos_mode'] = 'pipe'
                    if 'dscp' not in conf:
                        conf['dscp'] = 0

        return confs
