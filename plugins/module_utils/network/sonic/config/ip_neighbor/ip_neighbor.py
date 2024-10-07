#
# -*- coding: utf-8 -*-
# Copyright 2024 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_ip_neighbor class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from __future__ import absolute_import, division, print_function
__metaclass__ = type

from copy import deepcopy
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
    remove_empties
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import (
    Facts
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    get_diff,
    update_states
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.formatted_diff_utils import (
    __DELETE_CONFIG_IF_NO_SUBCONFIG,
    get_key_sets,
    get_new_config,
    get_formatted_config_diff
)
from urllib.parse import quote


INTF_PATH = 'data/openconfig-interfaces:interfaces/interface'
NBR_GLOBALS_PATH = 'data/openconfig-neighbor:neighbor-globals'
PATCH = 'patch'
DELETE = 'delete'
TEST_KEYS = [
    {'intf_ipv6_neighbors': {'interface': ''}},
    {'dnssl': {'name': ''}},
    {'neighbors': {'ip': ''}},
    {'ra_prefixes': {'prefix': ''}},
    {'rdnss': {'address': ''}},
]


def __derive_ip_neighbor_config_delete_op(key_set, command, exist_conf):
    new_conf = exist_conf

    ipv4_arp_timeout = command.get('ipv4_arp_timeout')
    ipv6_nd_cache_expiry = command.get('ipv6_nd_cache_expiry')
    num_local_neigh = command.get('num_local_neigh')
    ipv4_drop_neighbor_aging_time = command.get('ipv4_drop_neighbor_aging_time')
    ipv6_drop_neighbor_aging_time = command.get('ipv6_drop_neighbor_aging_time')
    cfg_ipv4_arp_timeout = new_conf.get('ipv4_arp_timeout')
    cfg_ipv6_nd_cache_expiry = new_conf.get('ipv6_nd_cache_expiry')
    cfg_num_local_neigh = new_conf.get('num_local_neigh')
    cfg_ipv4_drop_neighbor_aging_time = new_conf.get('ipv4_drop_neighbor_aging_time')
    cfg_ipv6_drop_neighbor_aging_time = new_conf.get('ipv6_drop_neighbor_aging_time')

    if ipv4_arp_timeout and ipv4_arp_timeout == cfg_ipv4_arp_timeout:
        new_conf['ipv4_arp_timeout'] = 180
    if ipv6_nd_cache_expiry and ipv6_nd_cache_expiry == cfg_ipv6_nd_cache_expiry:
        new_conf['ipv6_nd_cache_expiry'] = 180
    if num_local_neigh and num_local_neigh == cfg_num_local_neigh:
        new_conf['num_local_neigh'] = 0
    if ipv4_drop_neighbor_aging_time and ipv4_drop_neighbor_aging_time == cfg_ipv4_drop_neighbor_aging_time:
        new_conf['ipv4_drop_neighbor_aging_time'] = 300
    if ipv6_drop_neighbor_aging_time and ipv6_drop_neighbor_aging_time == cfg_ipv6_drop_neighbor_aging_time:
        new_conf['ipv6_drop_neighbor_aging_time'] = 300

    return False, new_conf


def __derive_ipv6_neighbors_delete_op(key_set, command, exist_conf):
    new_conf = exist_conf
    trival_cmd_key_set, dict_list_cmd_key_set = get_key_sets(command)

    if (len(key_set) == len(trival_cmd_key_set)) and \
       (len(dict_list_cmd_key_set) == 0):
        new_conf = []
        return True, new_conf

    trival_cmd_key_not_key_set = trival_cmd_key_set.difference(key_set)
    for key in trival_cmd_key_not_key_set:
        command_val = command.get(key, None)
        new_conf_val = new_conf.get(key, None)
        if command_val == new_conf_val:
            if key == 'dad':
                new_conf['dad'] = 'disable'
            else:
                new_conf.pop(key, None)

    return False, new_conf


TEST_KEYS_formatted_diff = [
    {'config': {'__delete_op': __derive_ip_neighbor_config_delete_op}},
    {'intf_ipv6_neighbors': {'interface': '', '__delete_op': __derive_ipv6_neighbors_delete_op}},
    {'dnssl': {'name': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}},
    {'neighbors': {'ip': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}},
    {'ra_prefixes': {'prefix': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}},
    {'rdnss': {'address': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}}
]


class Ip_neighbor(ConfigBase):
    """
    The sonic_ip_neighbor class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'ip_neighbor',
    ]

    def __init__(self, module):
        super(Ip_neighbor, self).__init__(module)

    def get_ip_neighbor_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        ip_neighbor_facts = facts['ansible_network_resources'].get('ip_neighbor')
        if not ip_neighbor_facts:
            return {}
        return ip_neighbor_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = []
        commands = []

        existing_ip_neighbor_facts = self.get_ip_neighbor_facts()
        commands, requests = self.set_config(existing_ip_neighbor_facts)
        if commands and len(requests) > 0:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        changed_ip_neighbor_facts = self.get_ip_neighbor_facts()

        result['before'] = existing_ip_neighbor_facts
        if result['changed']:
            result['after'] = changed_ip_neighbor_facts

        new_config = changed_ip_neighbor_facts
        old_config = existing_ip_neighbor_facts
        if self._module.check_mode:
            result.pop('after', None)
            new_config = get_new_config(commands, existing_ip_neighbor_facts,
                                        TEST_KEYS_formatted_diff)
            self.post_process_generated_config(new_config)
            result['after(generated)'] = new_config
        if self._module._diff:
            self.sort_lists_in_config(new_config)
            self.sort_lists_in_config(old_config)
            result['diff'] = get_formatted_config_diff(old_config,
                                                       new_config,
                                                       self._module._verbosity)

        result['warnings'] = warnings
        return result

    def set_config(self, existing_ip_neighbor_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = remove_empties(self._module.params['config'])
        have = existing_ip_neighbor_facts
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

        if state == 'merged':
            commands, requests = self._state_merged(diff)
        elif state == 'replaced':
            commands, requests = self._state_replaced(want, have, diff)
        elif state == 'overridden':
            commands, requests = self._state_overridden(want, have)
        elif state == 'deleted':
            commands, requests = self._state_deleted(want, have)
        return commands, requests

    def _state_merged(self, diff):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = diff
        requests = self.get_modify_ip_neighbor_requests(commands)

        if commands and len(requests) > 0:
            commands = update_states(commands, 'merged')
        else:
            commands = []
        return commands, requests

    def _state_deleted(self, want, have):
        """ The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        is_delete_all = False

        if not want:
            commands = deepcopy(have)
            is_delete_all = True
        else:
            commands = deepcopy(want)

        self.remove_default_entries(commands)
        requests = self.get_delete_ip_neighbor_requests(commands, have, is_delete_all)

        if commands and len(requests) > 0:
            commands = update_states(commands, 'deleted')
        else:
            commands = []
        return commands, requests

    def _state_replaced(self, want, have, diff):
        """ The command generator when state is replaced

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        mod_commands = []
        replaced_config, requests = self.get_replaced_config(want, have)

        if replaced_config:
            commands.extend(update_states(replaced_config, 'deleted'))
            mod_commands = want
        else:
            mod_commands = diff

        if mod_commands:
            mod_requests = self.get_modify_ip_neighbor_requests(mod_commands)

            if mod_requests:
                requests.extend(mod_requests)
                commands.extend(update_states(mod_commands, 'replaced'))
        return commands, requests

    def _state_overridden(self, want, have):
        """ The command generator when state is overridden

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        requests = []
        new_have = deepcopy(have)
        self.remove_default_entries(new_have)
        self.sort_lists_in_config(new_have)
        self.sort_lists_in_config(want)

        if new_have and new_have != want:
            del_requests = self.get_delete_all_requests(new_have)
            requests.extend(del_requests)
            commands.extend(update_states(new_have, 'deleted'))
            new_have = []

        if not new_have and want:
            mod_commands = want
            mod_requests = self.get_modify_ip_neighbor_requests(mod_commands)

            if mod_requests:
                requests.extend(mod_requests)
                commands.extend(update_states(mod_commands, 'overridden'))
        return commands, requests

    def get_modify_ip_neighbor_requests(self, commands):
        requests = []

        if commands:
            nbr_cfg_dict = {}
            ipv4_arp_timeout = commands.get('ipv4_arp_timeout')
            ipv6_nd_cache_expiry = commands.get('ipv6_nd_cache_expiry')
            num_local_neigh = commands.get('num_local_neigh')
            ipv4_drop_neighbor_aging_time = commands.get('ipv4_drop_neighbor_aging_time')
            ipv6_drop_neighbor_aging_time = commands.get('ipv6_drop_neighbor_aging_time')
            intf_ipv6_neighbors = commands.get('intf_ipv6_neighbors')

            # Handle merge for neighbor-global config
            if ipv4_arp_timeout:
                nbr_cfg_dict['ipv4-arp-timeout'] = ipv4_arp_timeout
            if ipv6_nd_cache_expiry:
                nbr_cfg_dict['ipv6-nd-cache-expiry'] = ipv6_nd_cache_expiry
            if num_local_neigh is not None:
                nbr_cfg_dict['num-local-neigh'] = num_local_neigh
            if ipv4_drop_neighbor_aging_time:
                nbr_cfg_dict['ipv4-drop-neighbor-aging-time'] = ipv4_drop_neighbor_aging_time
            if ipv6_drop_neighbor_aging_time:
                nbr_cfg_dict['ipv6-drop-neighbor-aging-time'] = ipv6_drop_neighbor_aging_time
            if nbr_cfg_dict:
                nbr_cfg_dict['name'] = 'Values'
                payload = {
                    'openconfig-neighbor:neighbor-globals': {
                        'neighbor-global': [
                            {
                                'name': 'Values',
                                'config': nbr_cfg_dict
                            }
                        ]
                    }
                }
                requests.append({'path': NBR_GLOBALS_PATH, 'method': PATCH, 'data': payload})

            if intf_ipv6_neighbors:
                for nbr in intf_ipv6_neighbors:
                    ipv6_dict = {}
                    rt_adv_dict = {}
                    rt_adv_cfg_dict = {}
                    interface = nbr.get('interface')
                    is_vlan = 'Vlan' in interface
                    adv_interval_option = nbr.get('adv_interval_option')
                    dad = nbr.get('dad')
                    dnssl = nbr.get('dnssl')
                    home_agent_config = nbr.get('home_agent_config')
                    home_agent_lifetime = nbr.get('home_agent_lifetime')
                    home_agent_preference = nbr.get('home_agent_preference')
                    interval = nbr.get('interval')
                    lifetime = nbr.get('lifetime')
                    managed_config = nbr.get('managed_config')
                    min_ra_interval = nbr.get('min_ra_interval')
                    min_ra_interval_msec = nbr.get('min_ra_interval_msec')
                    mtu = nbr.get('mtu')
                    neighbors = nbr.get('neighbors')
                    other_config = nbr.get('other_config')
                    ra_fast_retrans = nbr.get('ra_fast_retrans')
                    ra_hop_limit = nbr.get('ra_hop_limit')
                    ra_interval_msec = nbr.get('ra_interval_msec')
                    ra_prefixes = nbr.get('ra_prefixes')
                    ra_retrans_interval = nbr.get('ra_retrans_interval')
                    rdnss = nbr.get('rdnss')
                    reachable_time = nbr.get('reachable_time')
                    router_preference = nbr.get('router_preference')
                    suppress = nbr.get('suppress')

                    # Handle router-advertisement config attributes
                    if adv_interval_option is not None:
                        rt_adv_cfg_dict['openconfig-interfaces-ext:adv-interval-option'] = adv_interval_option
                    if home_agent_config is not None:
                        rt_adv_cfg_dict['openconfig-interfaces-ext:home-agent-config'] = home_agent_config
                    if home_agent_lifetime is not None:
                        rt_adv_cfg_dict['openconfig-interfaces-ext:home-agent-lifetime'] = home_agent_lifetime
                    if home_agent_preference is not None:
                        rt_adv_cfg_dict['openconfig-interfaces-ext:home-agent-preference'] = home_agent_preference
                    if interval:
                        rt_adv_cfg_dict['interval'] = interval
                    if lifetime:
                        rt_adv_cfg_dict['lifetime'] = lifetime
                    if managed_config is not None:
                        rt_adv_cfg_dict['openconfig-interfaces-ext:managed-config'] = managed_config
                    if min_ra_interval:
                        rt_adv_cfg_dict['openconfig-interfaces-ext:min-ra-interval'] = min_ra_interval
                    if min_ra_interval_msec:
                        rt_adv_cfg_dict['openconfig-interfaces-ext:min-ra-interval-msec'] = min_ra_interval_msec
                    if mtu is not None:
                        rt_adv_cfg_dict['openconfig-interfaces-ext:mtu'] = mtu
                    if other_config is not None:
                        rt_adv_cfg_dict['openconfig-interfaces-ext:other-config'] = other_config
                    if ra_fast_retrans is not None:
                        rt_adv_cfg_dict['openconfig-interfaces-ext:ra-fast-retrans'] = ra_fast_retrans
                    if ra_hop_limit is not None:
                        rt_adv_cfg_dict['openconfig-interfaces-ext:ra-hop-limit'] = ra_hop_limit
                    if ra_interval_msec is not None:
                        rt_adv_cfg_dict['openconfig-interfaces-ext:ra-interval-msec'] = ra_interval_msec
                    if ra_retrans_interval is not None:
                        rt_adv_cfg_dict['openconfig-interfaces-ext:ra-retrans-interval'] = ra_retrans_interval
                    if reachable_time is not None:
                        rt_adv_cfg_dict['openconfig-interfaces-ext:reachable-time'] = reachable_time
                    if router_preference:
                        rt_adv_cfg_dict['openconfig-interfaces-ext:router-preference'] = router_preference.upper()
                    if suppress is not None:
                        rt_adv_cfg_dict['suppress'] = suppress
                    if rt_adv_cfg_dict:
                        rt_adv_dict['config'] = rt_adv_cfg_dict

                    # Handle router-advertisement attributes
                    if dnssl:
                        dnssl_list = []
                        for dns in dnssl:
                            cfg_dict = {}
                            name = dns.get('name')
                            valid_lifetime = dns.get('valid_lifetime')

                            if name:
                                cfg_dict['dnssl-name'] = name
                            if valid_lifetime is not None:
                                cfg_dict['valid-lifetime'] = valid_lifetime
                            if cfg_dict:
                                dnssl_list.append({'dnssl-name': name, 'config': cfg_dict})
                        if dnssl_list:
                            rt_adv_dict['openconfig-interfaces-ext:dns-search-names'] = {'dns-search-name': dnssl_list}

                    if ra_prefixes:
                        pfx_list = []
                        for pfx in ra_prefixes:
                            cfg_dict = {}
                            prefix = pfx.get('prefix')
                            no_autoconfig = pfx.get('no_autoconfig')
                            off_link = pfx.get('off_link')
                            preferred_lifetime = pfx.get('preferred_lifetime')
                            router_address = pfx.get('router_address')
                            valid_lifetime = pfx.get('valid_lifetime')

                            if prefix:
                                cfg_dict['prefix'] = prefix
                            if no_autoconfig is not None:
                                cfg_dict['no-autoconfig'] = no_autoconfig
                            if off_link is not None:
                                cfg_dict['off-link'] = off_link
                            if preferred_lifetime is not None:
                                cfg_dict['preferred-lifetime'] = preferred_lifetime
                            if router_address is not None:
                                cfg_dict['router-address'] = router_address
                            if valid_lifetime is not None:
                                cfg_dict['valid-lifetime'] = valid_lifetime
                            if cfg_dict:
                                pfx_list.append({'prefix': prefix, 'config': cfg_dict})
                        if pfx_list:
                            rt_adv_dict['openconfig-interfaces-ext:ra-prefixes'] = {'ra-prefix': pfx_list}

                    if rdnss:
                        rdnss_list = []
                        for addr in rdnss:
                            cfg_dict = {}
                            address = addr.get('address')
                            valid_lifetime = addr.get('valid_lifetime')

                            if address:
                                cfg_dict['address'] = address
                            if valid_lifetime is not None:
                                cfg_dict['valid-lifetime'] = valid_lifetime
                            if cfg_dict:
                                rdnss_list.append({'address': address, 'config': cfg_dict})
                        if rdnss_list:
                            rt_adv_dict['openconfig-interfaces-ext:rdnss-addresses'] = {'rdnss-address': rdnss_list}

                    if rt_adv_dict:
                        ipv6_dict['router-advertisement'] = rt_adv_dict

                    # Handle openconfig-if-ip:ipv6 attributes
                    if neighbors:
                        neighbor_list = []
                        for neighbor in neighbors:
                            cfg_dict = {}
                            ip = neighbor.get('ip')
                            link_layer_address = neighbor.get('link_layer_address')

                            if ip:
                                cfg_dict['ip'] = ip
                            if link_layer_address:
                                cfg_dict['link-layer-address'] = link_layer_address
                            if cfg_dict:
                                neighbor_list.append({'ip': ip, 'config': cfg_dict})
                        if neighbor_list:
                            ipv6_dict['neighbors'] = {'neighbor': neighbor_list}

                    if dad:
                        ipv6_dict['config'] = {'ipv6_dad': dad.upper()}

                    # Create payload
                    if ipv6_dict:
                        payload = None
                        if is_vlan:
                            payload = {
                                'openconfig-interfaces:interface': [
                                    {
                                        'name': interface,
                                        'openconfig-vlan:routed-vlan': {
                                            'openconfig-if-ip:ipv6': ipv6_dict
                                        }
                                    }
                                ]
                            }
                        else:
                            payload = {
                                'openconfig-interfaces:interface': [
                                    {
                                        'name': interface,
                                        'subinterfaces': {
                                            'subinterface': [
                                                {
                                                    'index': 0,
                                                    'openconfig-if-ip:ipv6': ipv6_dict
                                                }
                                            ]
                                        }
                                    }
                                ]
                            }
                        path = f'{INTF_PATH}={interface}'
                        requests.append({'path': path, 'method': PATCH, 'data': payload})

        return requests

    def get_delete_ip_neighbor_requests(self, commands, have, is_delete_all):
        requests = []

        if not commands or not have:
            return requests
        if is_delete_all:
            return self.get_delete_all_requests(commands)

        config_dict = {}
        ipv4_arp_timeout = commands.get('ipv4_arp_timeout')
        ipv6_nd_cache_expiry = commands.get('ipv6_nd_cache_expiry')
        num_local_neigh = commands.get('num_local_neigh')
        ipv4_drop_neighbor_aging_time = commands.get('ipv4_drop_neighbor_aging_time')
        ipv6_drop_neighbor_aging_time = commands.get('ipv6_drop_neighbor_aging_time')
        intf_ipv6_neighbors = commands.get('intf_ipv6_neighbors')
        cfg_ipv4_arp_timeout = have.get('ipv4_arp_timeout')
        cfg_ipv6_nd_cache_expiry = have.get('ipv6_nd_cache_expiry')
        cfg_num_local_neigh = have.get('num_local_neigh')
        cfg_ipv4_drop_neighbor_aging_time = have.get('ipv4_drop_neighbor_aging_time')
        cfg_ipv6_drop_neighbor_aging_time = have.get('ipv6_drop_neighbor_aging_time')
        cfg_intf_ipv6_neighbors = have.get('intf_ipv6_neighbors')

        if ipv4_arp_timeout and ipv4_arp_timeout == cfg_ipv4_arp_timeout:
            requests.append(self.get_delete_nbr_global_cfg_attr_req('ipv4-arp-timeout'))
            config_dict['ipv4_arp_timeout'] = ipv4_arp_timeout
        if ipv6_nd_cache_expiry and ipv6_nd_cache_expiry == cfg_ipv6_nd_cache_expiry:
            requests.append(self.get_delete_nbr_global_cfg_attr_req('ipv6-nd-cache-expiry'))
            config_dict['ipv6_nd_cache_expiry'] = ipv6_nd_cache_expiry
        if num_local_neigh is not None and num_local_neigh == cfg_num_local_neigh:
            requests.append(self.get_delete_nbr_global_cfg_attr_req('num-local-neigh'))
            config_dict['num_local_neigh'] = num_local_neigh
        if ipv4_drop_neighbor_aging_time and ipv4_drop_neighbor_aging_time == cfg_ipv4_drop_neighbor_aging_time:
            requests.append(self.get_delete_nbr_global_cfg_attr_req('ipv4-drop-neighbor-aging-time'))
            config_dict['ipv4_drop_neighbor_aging_time'] = ipv4_drop_neighbor_aging_time
        if ipv6_drop_neighbor_aging_time and ipv6_drop_neighbor_aging_time == cfg_ipv6_drop_neighbor_aging_time:
            requests.append(self.get_delete_nbr_global_cfg_attr_req('ipv6-drop-neighbor-aging-time'))
            config_dict['ipv6_drop_neighbor_aging_time'] = ipv6_drop_neighbor_aging_time

        if intf_ipv6_neighbors and cfg_intf_ipv6_neighbors:
            cfg_nbr_dict = {cfg_nbr.get('interface'): cfg_nbr for cfg_nbr in cfg_intf_ipv6_neighbors}
            for nbr in intf_ipv6_neighbors:
                ipv6_nbr_dict = {}
                interface = nbr.get('interface')
                is_vlan = 'Vlan' in interface
                adv_interval_option = nbr.get('adv_interval_option')
                dad = nbr.get('dad')
                dnssl = nbr.get('dnssl')
                home_agent_config = nbr.get('home_agent_config')
                home_agent_lifetime = nbr.get('home_agent_lifetime')
                home_agent_preference = nbr.get('home_agent_preference')
                interval = nbr.get('interval')
                lifetime = nbr.get('lifetime')
                managed_config = nbr.get('managed_config')
                min_ra_interval = nbr.get('min_ra_interval')
                min_ra_interval_msec = nbr.get('min_ra_interval_msec')
                mtu = nbr.get('mtu')
                neighbors = nbr.get('neighbors')
                other_config = nbr.get('other_config')
                ra_fast_retrans = nbr.get('ra_fast_retrans')
                ra_hop_limit = nbr.get('ra_hop_limit')
                ra_interval_msec = nbr.get('ra_interval_msec')
                ra_prefixes = nbr.get('ra_prefixes')
                ra_retrans_interval = nbr.get('ra_retrans_interval')
                rdnss = nbr.get('rdnss')
                reachable_time = nbr.get('reachable_time')
                router_preference = nbr.get('router_preference')
                suppress = nbr.get('suppress')

                cfg_nbr = cfg_nbr_dict.get(interface)
                if cfg_nbr is None:
                    continue
                cfg_adv_interval_option = cfg_nbr.get('adv_interval_option')
                cfg_dad = cfg_nbr.get('dad')
                cfg_dnssl = cfg_nbr.get('dnssl')
                cfg_home_agent_config = cfg_nbr.get('home_agent_config')
                cfg_home_agent_lifetime = cfg_nbr.get('home_agent_lifetime')
                cfg_home_agent_preference = cfg_nbr.get('home_agent_preference')
                cfg_interval = cfg_nbr.get('interval')
                cfg_lifetime = cfg_nbr.get('lifetime')
                cfg_managed_config = cfg_nbr.get('managed_config')
                cfg_min_ra_interval = cfg_nbr.get('min_ra_interval')
                cfg_min_ra_interval_msec = cfg_nbr.get('min_ra_interval_msec')
                cfg_mtu = cfg_nbr.get('mtu')
                cfg_neighbors = cfg_nbr.get('neighbors')
                cfg_other_config = cfg_nbr.get('other_config')
                cfg_ra_fast_retrans = cfg_nbr.get('ra_fast_retrans')
                cfg_ra_hop_limit = cfg_nbr.get('ra_hop_limit')
                cfg_ra_interval_msec = cfg_nbr.get('ra_interval_msec')
                cfg_ra_prefixes = cfg_nbr.get('ra_prefixes')
                cfg_ra_retrans_interval = cfg_nbr.get('ra_retrans_interval')
                cfg_rdnss = cfg_nbr.get('rdnss')
                cfg_reachable_time = cfg_nbr.get('reachable_time')
                cfg_router_preference = cfg_nbr.get('router_preference')
                cfg_suppress = cfg_nbr.get('suppress')

                if adv_interval_option is not None and adv_interval_option == cfg_adv_interval_option:
                    requests.append(self.get_delete_rt_adv_attr_req(interface, is_vlan, '/config/openconfig-interfaces-ext:adv-interval-option'))
                    ipv6_nbr_dict.update({'interface': interface, 'adv_interval_option': adv_interval_option})
                if dad and dad == cfg_dad:
                    requests.append(self.get_delete_ipv6_cfg_attr_req(interface, is_vlan, '/ipv6_dad'))
                    ipv6_nbr_dict.update({'interface': interface, 'dad': dad})
                if dnssl and cfg_dnssl:
                    cfg_dns_dict = {cfg_dns.get('name'): cfg_dns for cfg_dns in cfg_dnssl}
                    dnssl_list = []
                    for dns in dnssl:
                        dns_dict = {}
                        name = dns.get('name')
                        valid_lifetime = dns.get('valid_lifetime')

                        cfg_dns = cfg_dns_dict.get(name)
                        if cfg_dns is None:
                            continue
                        cfg_valid_lifetime = cfg_dns.get('valid_lifetime')
                        encoded_name = quote(name, safe='')
                        path = f'/openconfig-interfaces-ext:dns-search-names/dns-search-name={encoded_name}'

                        if valid_lifetime is not None and valid_lifetime == cfg_valid_lifetime:
                            attr = f'{path}/config/valid-lifetime'
                            requests.append(self.get_delete_rt_adv_attr_req(interface, is_vlan, attr))
                            dns_dict.update({'name': name, 'valid_lifetime': valid_lifetime})
                        elif valid_lifetime is None:
                            requests.append(self.get_delete_rt_adv_attr_req(interface, is_vlan, path))
                            dns_dict['name'] = name
                        if dns_dict:
                            dnssl_list.append(dns_dict)
                    if dnssl_list:
                        ipv6_nbr_dict.update({'interface': interface, 'dnssl': dnssl_list})
                if home_agent_config is not None and home_agent_config == cfg_home_agent_config:
                    requests.append(self.get_delete_rt_adv_attr_req(interface, is_vlan, '/config/openconfig-interfaces-ext:home-agent-config'))
                    ipv6_nbr_dict.update({'interface': interface, 'home_agent_config': home_agent_config})
                if home_agent_lifetime is not None and home_agent_lifetime == cfg_home_agent_lifetime:
                    requests.append(self.get_delete_rt_adv_attr_req(interface, is_vlan, '/config/openconfig-interfaces-ext:home-agent-lifetime'))
                    ipv6_nbr_dict.update({'interface': interface, 'home_agent_lifetime': home_agent_lifetime})
                if home_agent_preference is not None and home_agent_preference == cfg_home_agent_preference:
                    requests.append(self.get_delete_rt_adv_attr_req(interface, is_vlan, '/config/openconfig-interfaces-ext:home-agent-preference'))
                    ipv6_nbr_dict.update({'interface': interface, 'home_agent_preference': home_agent_preference})
                if interval and interval == cfg_interval:
                    requests.append(self.get_delete_rt_adv_attr_req(interface, is_vlan, '/config/interval'))
                    ipv6_nbr_dict.update({'interface': interface, 'interval': interval})
                if min_ra_interval and min_ra_interval == cfg_min_ra_interval:
                    requests.append(self.get_delete_rt_adv_attr_req(interface, is_vlan, '/config/openconfig-interfaces-ext:min-ra-interval'))
                    ipv6_nbr_dict.update({'interface': interface, 'min_ra_interval': min_ra_interval})
                if min_ra_interval_msec and min_ra_interval_msec == cfg_min_ra_interval_msec:
                    requests.append(self.get_delete_rt_adv_attr_req(interface, is_vlan, '/config/openconfig-interfaces-ext:min-ra-interval-msec'))
                    ipv6_nbr_dict.update({'interface': interface, 'min_ra_interval_msec': min_ra_interval_msec})
                if lifetime and lifetime == cfg_lifetime:
                    requests.append(self.get_delete_rt_adv_attr_req(interface, is_vlan, '/config/lifetime'))
                    ipv6_nbr_dict.update({'interface': interface, 'lifetime': lifetime})
                if managed_config is not None and managed_config == cfg_managed_config:
                    requests.append(self.get_delete_rt_adv_attr_req(interface, is_vlan, '/config/openconfig-interfaces-ext:managed-config'))
                    ipv6_nbr_dict.update({'interface': interface, 'managed_config': managed_config})
                if mtu is not None and mtu == cfg_mtu:
                    requests.append(self.get_delete_rt_adv_attr_req(interface, is_vlan, '/config/openconfig-interfaces-ext:mtu'))
                    ipv6_nbr_dict.update({'interface': interface, 'mtu': mtu})
                if neighbors and cfg_neighbors:
                    cfg_neighbor_dict = {cfg_neighbor.get('ip'): cfg_neighbor for cfg_neighbor in cfg_neighbors}
                    neighbors_list = []
                    for neighbor in neighbors:
                        neighbor_dict = {}
                        ip = neighbor.get('ip')
                        link_layer_address = neighbor.get('link_layer_address')

                        cfg_neighbor = cfg_neighbor_dict.get(ip)
                        if cfg_neighbor is None:
                            continue
                        cfg_link_layer_address = cfg_neighbor.get('link_layer_address')
                        encoded_ip = quote(ip, safe='')
                        path = f'/neighbor={encoded_ip}'

                        if link_layer_address and link_layer_address == cfg_link_layer_address:
                            attr = f'{path}/config/link-layer-address'
                            requests.append(self.get_delete_ipv6_nbr_attr_req(interface, is_vlan, attr))
                            neighbor_dict.update({'ip': ip, 'link_layer_address': link_layer_address})
                        elif not link_layer_address:
                            requests.append(self.get_delete_ipv6_nbr_attr_req(interface, is_vlan, path))
                            neighbor_dict['ip'] = ip
                        if neighbor_dict:
                            neighbors_list.append(neighbor_dict)
                    if neighbors_list:
                        ipv6_nbr_dict.update({'interface': interface, 'neighbors': neighbors_list})
                if other_config is not None and other_config == cfg_other_config:
                    requests.append(self.get_delete_rt_adv_attr_req(interface, is_vlan, '/config/openconfig-interfaces-ext:other-config'))
                    ipv6_nbr_dict.update({'interface': interface, 'other_config': other_config})
                if ra_fast_retrans is not None and ra_fast_retrans == cfg_ra_fast_retrans:
                    requests.append(self.get_delete_rt_adv_attr_req(interface, is_vlan, '/config/openconfig-interfaces-ext:ra-fast-retrans'))
                    ipv6_nbr_dict.update({'interface': interface, 'ra_fast_retrans': ra_fast_retrans})
                if ra_hop_limit is not None and ra_hop_limit == cfg_ra_hop_limit:
                    requests.append(self.get_delete_rt_adv_attr_req(interface, is_vlan, '/config/openconfig-interfaces-ext:ra-hop-limit'))
                    ipv6_nbr_dict.update({'interface': interface, 'ra_hop_limit': ra_hop_limit})
                if ra_interval_msec is not None and ra_interval_msec == cfg_ra_interval_msec:
                    requests.append(self.get_delete_rt_adv_attr_req(interface, is_vlan, '/config/openconfig-interfaces-ext:ra-interval-msec'))
                    ipv6_nbr_dict.update({'interface': interface, 'ra_interval_msec': ra_interval_msec})
                if ra_prefixes and cfg_ra_prefixes:
                    cfg_pfx_dict = {cfg_pfx.get('prefix'): cfg_pfx for cfg_pfx in cfg_ra_prefixes}
                    ra_prefixes_list = []
                    for pfx in ra_prefixes:
                        pfx_dict = {}
                        prefix = pfx.get('prefix')
                        no_autoconfig = pfx.get('no_autoconfig')
                        off_link = pfx.get('off_link')
                        preferred_lifetime = pfx.get('preferred_lifetime')
                        router_address = pfx.get('router_address')
                        valid_lifetime = pfx.get('valid_lifetime')

                        cfg_pfx = cfg_pfx_dict.get(prefix)
                        if cfg_pfx is None:
                            continue
                        cfg_no_autoconfig = cfg_pfx.get('no_autoconfig')
                        cfg_off_link = cfg_pfx.get('off_link')
                        cfg_preferred_lifetime = cfg_pfx.get('preferred_lifetime')
                        cfg_router_address = cfg_pfx.get('router_address')
                        cfg_valid_lifetime = cfg_pfx.get('valid_lifetime')
                        encoded_pfx = quote(prefix, safe='')
                        path = f'/openconfig-interfaces-ext:ra-prefixes/ra-prefix={encoded_pfx}'

                        if no_autoconfig is not None and no_autoconfig == cfg_no_autoconfig:
                            attr = f'{path}/config/no-autoconfig'
                            requests.append(self.get_delete_rt_adv_attr_req(interface, is_vlan, attr))
                            pfx_dict.update({'prefix': prefix, 'no_autoconfig': no_autoconfig})
                        if off_link is not None and off_link == cfg_off_link:
                            attr = f'{path}/config/off-link'
                            requests.append(self.get_delete_rt_adv_attr_req(interface, is_vlan, attr))
                            pfx_dict.update({'prefix': prefix, 'off_link': off_link})
                        if preferred_lifetime is not None and preferred_lifetime == cfg_preferred_lifetime:
                            attr = f'{path}/config/preferred-lifetime'
                            requests.append(self.get_delete_rt_adv_attr_req(interface, is_vlan, attr))
                            pfx_dict.update({'prefix': prefix, 'preferred_lifetime': preferred_lifetime})
                        if router_address is not None and router_address == cfg_router_address:
                            attr = f'{path}/config/router-address'
                            requests.append(self.get_delete_rt_adv_attr_req(interface, is_vlan, attr))
                            pfx_dict.update({'prefix': prefix, 'router_address': router_address})
                        if valid_lifetime is not None and valid_lifetime == cfg_valid_lifetime:
                            attr = f'{path}/config/valid-lifetime'
                            requests.append(self.get_delete_rt_adv_attr_req(interface, is_vlan, attr))
                            pfx_dict.update({'prefix': prefix, 'valid_lifetime': valid_lifetime})
                        if (no_autoconfig is None and off_link is None and preferred_lifetime is None and router_address is None and valid_lifetime
                                is None):
                            requests.append(self.get_delete_rt_adv_attr_req(interface, is_vlan, path))
                            pfx_dict['prefix'] = prefix
                        if pfx_dict:
                            ra_prefixes_list.append(pfx_dict)
                    if ra_prefixes_list:
                        ipv6_nbr_dict.update({'interface': interface, 'ra_prefixes': ra_prefixes_list})
                if ra_retrans_interval is not None and ra_retrans_interval == cfg_ra_retrans_interval:
                    requests.append(self.get_delete_rt_adv_attr_req(interface, is_vlan, '/config/openconfig-interfaces-ext:ra-retrans-interval'))
                    ipv6_nbr_dict.update({'interface': interface, 'ra_retrans_interval': ra_retrans_interval})
                if rdnss and cfg_rdnss:
                    cfg_addr_dict = {cfg_addr.get('address'): cfg_addr for cfg_addr in cfg_rdnss}
                    rdnss_list = []
                    for addr in rdnss:
                        addr_dict = {}
                        address = addr.get('address')
                        valid_lifetime = addr.get('valid_lifetime')

                        cfg_addr = cfg_addr_dict.get(address)
                        if cfg_addr is None:
                            continue
                        cfg_valid_lifetime = cfg_addr.get('valid_lifetime')
                        encoded_addr = quote(address, safe='')
                        path = f'/openconfig-interfaces-ext:rdnss-addresses/rdnss-address={encoded_addr}'

                        if valid_lifetime is not None and valid_lifetime == cfg_valid_lifetime:
                            attr = f'{path}/config/valid-lifetime'
                            requests.append(self.get_delete_rt_adv_attr_req(interface, is_vlan, attr))
                            addr_dict.update({'address': address, 'valid_lifetime': valid_lifetime})
                        elif valid_lifetime is None:
                            requests.append(self.get_delete_rt_adv_attr_req(interface, is_vlan, path))
                            addr_dict['address'] = address
                        if addr_dict:
                            rdnss_list.append(addr_dict)
                    if rdnss_list:
                        ipv6_nbr_dict.update({'interface': interface, 'rdnss': rdnss_list})
                if reachable_time is not None and reachable_time == cfg_reachable_time:
                    requests.append(self.get_delete_rt_adv_attr_req(interface, is_vlan, '/config/openconfig-interfaces-ext:reachable-time'))
                    ipv6_nbr_dict.update({'interface': interface, 'reachable_time': reachable_time})
                if router_preference and router_preference == cfg_router_preference:
                    requests.append(self.get_delete_rt_adv_attr_req(interface, is_vlan, '/config/openconfig-interfaces-ext:router-preference'))
                    ipv6_nbr_dict.update({'interface': interface, 'router_preference': router_preference})
                if suppress is not None and suppress == cfg_suppress:
                    requests.append(self.get_delete_rt_adv_attr_req(interface, is_vlan, '/config/suppress'))
                    ipv6_nbr_dict.update({'interface': interface, 'suppress': suppress})

        commands = config_dict
        return requests

    def get_delete_all_requests(self, have):
        requests = []
        ipv4_arp_timeout = have.get('ipv4_arp_timeout')
        ipv6_nd_cache_expiry = have.get('ipv6_nd_cache_expiry')
        num_local_neigh = have.get('num_local_neigh')
        ipv4_drop_neighbor_aging_time = have.get('ipv4_drop_neighbor_aging_time')
        ipv6_drop_neighbor_aging_time = have.get('ipv6_drop_neighbor_aging_time')
        intf_ipv6_neighbors = have.get('intf_ipv6_neighbors')

        # Handle deletion for neighbor-global config
        if ipv4_arp_timeout or ipv6_nd_cache_expiry or num_local_neigh is not None or ipv4_drop_neighbor_aging_time or ipv6_drop_neighbor_aging_time:
            requests.append(self.get_delete_nbr_global_cfg_attr_req(None))

        if intf_ipv6_neighbors:
            for nbr in intf_ipv6_neighbors:
                interface = nbr.get('interface')
                is_vlan = 'Vlan' in interface
                adv_interval_option = nbr.get('adv_interval_option')
                dad = nbr.get('dad')
                dnssl = nbr.get('dnssl')
                home_agent_config = nbr.get('home_agent_config')
                home_agent_lifetime = nbr.get('home_agent_lifetime')
                home_agent_preference = nbr.get('home_agent_preference')
                interval = nbr.get('interval')
                lifetime = nbr.get('lifetime')
                managed_config = nbr.get('managed_config')
                min_ra_interval = nbr.get('min_ra_interval')
                min_ra_interval_msec = nbr.get('min_ra_interval_msec')
                mtu = nbr.get('mtu')
                neighbors = nbr.get('neighbors')
                other_config = nbr.get('other_config')
                ra_fast_retrans = nbr.get('ra_fast_retrans')
                ra_hop_limit = nbr.get('ra_hop_limit')
                ra_interval_msec = nbr.get('ra_interval_msec')
                ra_prefixes = nbr.get('ra_prefixes')
                ra_retrans_interval = nbr.get('ra_retrans_interval')
                rdnss = nbr.get('rdnss')
                reachable_time = nbr.get('reachable_time')
                router_preference = nbr.get('router_preference')
                suppress = nbr.get('suppress')

                # Handle deletion for router-advertisement
                if (adv_interval_option is not None or dnssl or home_agent_config is not None or home_agent_lifetime is not None or
                    home_agent_preference is not None or interval or lifetime or managed_config is not None or min_ra_interval or
                    min_ra_interval_msec or mtu is not None or other_config is not None or ra_fast_retrans is not None or ra_hop_limit is not None
                    or ra_interval_msec is not None or ra_prefixes or ra_retrans_interval is not None or rdnss or reachable_time is not None or
                        router_preference or suppress):

                    requests.append(self.get_delete_rt_adv_attr_req(interface, is_vlan, None))

                # Handle deletion for ipv6_dad
                if dad:
                    requests.append(self.get_delete_ipv6_cfg_attr_req(interface, is_vlan, '/ipv6_dad'))

                # Handle deletion for neighbors
                if neighbors:
                    requests.append(self.get_delete_ipv6_nbr_attr_req(interface, is_vlan, None))
        return requests

    def get_delete_nbr_global_cfg_attr_req(self, attr):
        url = NBR_GLOBALS_PATH
        if attr:
            url = f'{url}/neighbor-global=Values/config/{attr}'
        request = {'path': url, 'method': DELETE}

        return request

    def get_delete_rt_adv_attr_req(self, interface, is_vlan, attr):
        url = None
        if is_vlan:
            url = f'{INTF_PATH}={interface}/openconfig-vlan:routed-vlan/openconfig-if-ip:ipv6/router-advertisement'
        else:
            url = f'{INTF_PATH}={interface}/subinterfaces/subinterface=0/openconfig-if-ip:ipv6/router-advertisement'
        if attr:
            url += attr
        request = {'path': url, 'method': DELETE}

        return request

    def get_delete_ipv6_cfg_attr_req(self, interface, is_vlan, attr):
        url = None
        if is_vlan:
            url = f'{INTF_PATH}={interface}/openconfig-vlan:routed-vlan/openconfig-if-ip:ipv6/config'
        else:
            url = f'{INTF_PATH}={interface}/subinterfaces/subinterface=0/openconfig-if-ip:ipv6/config'
        if attr:
            url += attr
        request = {'path': url, 'method': DELETE}

        return request

    def get_delete_ipv6_nbr_attr_req(self, interface, is_vlan, attr):
        url = None
        if is_vlan:
            url = f'{INTF_PATH}={interface}/openconfig-vlan:routed-vlan/openconfig-if-ip:ipv6/neighbors'
        else:
            url = f'{INTF_PATH}={interface}/subinterfaces/subinterface=0/openconfig-if-ip:ipv6/neighbors'
        if attr:
            url += attr
        request = {'path': url, 'method': DELETE}

        return request

    def get_replaced_config(self, want, have):
        config_dict = {}
        requests = []
        new_have = deepcopy(have)
        self.remove_default_entries(new_have)

        if not want or not new_have:
            return config_dict, requests

        # Handle replacement at global level
        ipv4_arp_timeout = want.get('ipv4_arp_timeout')
        ipv6_nd_cache_expiry = want.get('ipv6_nd_cache_expiry')
        num_local_neigh = want.get('num_local_neigh')
        ipv4_drop_neighbor_aging_time = want.get('ipv4_drop_neighbor_aging_time')
        ipv6_drop_neighbor_aging_time = want.get('ipv6_drop_neighbor_aging_time')
        cfg_ipv4_arp_timeout = new_have.get('ipv4_arp_timeout')
        cfg_ipv6_nd_cache_expiry = new_have.get('ipv6_nd_cache_expiry')
        cfg_num_local_neigh = new_have.get('num_local_neigh')
        cfg_ipv4_drop_neighbor_aging_time = new_have.get('ipv4_drop_neighbor_aging_time')
        cfg_ipv6_drop_neighbor_aging_time = new_have.get('ipv6_drop_neighbor_aging_time')

        if ((ipv4_arp_timeout and cfg_ipv4_arp_timeout and ipv4_arp_timeout != cfg_ipv4_arp_timeout) or
                (ipv6_nd_cache_expiry and cfg_ipv6_nd_cache_expiry and ipv6_nd_cache_expiry != cfg_ipv6_nd_cache_expiry) or
                (num_local_neigh is not None and cfg_num_local_neigh is not None and num_local_neigh != cfg_num_local_neigh) or
                (ipv4_drop_neighbor_aging_time and cfg_ipv4_drop_neighbor_aging_time and ipv4_drop_neighbor_aging_time !=
                 cfg_ipv4_drop_neighbor_aging_time) or
                (ipv6_drop_neighbor_aging_time and cfg_ipv6_drop_neighbor_aging_time and ipv6_drop_neighbor_aging_time !=
                 cfg_ipv6_drop_neighbor_aging_time)):
            requests.extend(self.get_delete_all_requests(new_have))
            return new_have, requests

        # Handle replacement at IPv6 interface level
        intf_ipv6_neighbors = want.get('intf_ipv6_neighbors')
        cfg_intf_ipv6_neighbors = new_have.get('intf_ipv6_neighbors')
        if not intf_ipv6_neighbors or not cfg_intf_ipv6_neighbors:
            return config_dict, requests

        cfg_nbr_dict = {cfg_nbr.get('interface'): cfg_nbr for cfg_nbr in cfg_intf_ipv6_neighbors}
        ipv6_nbr_list = []
        for nbr in intf_ipv6_neighbors:
            interface = nbr.get('interface')
            is_vlan = 'Vlan' in interface
            adv_interval_option = nbr.get('adv_interval_option')
            dad = nbr.get('dad')
            home_agent_config = nbr.get('home_agent_config')
            home_agent_lifetime = nbr.get('home_agent_lifetime')
            home_agent_preference = nbr.get('home_agent_preference')
            interval = nbr.get('interval')
            lifetime = nbr.get('lifetime')
            managed_config = nbr.get('managed_config')
            min_ra_interval = nbr.get('min_ra_interval')
            min_ra_interval_msec = nbr.get('min_ra_interval_msec')
            mtu = nbr.get('mtu')
            other_config = nbr.get('other_config')
            ra_fast_retrans = nbr.get('ra_fast_retrans')
            ra_hop_limit = nbr.get('ra_hop_limit')
            ra_interval_msec = nbr.get('ra_interval_msec')
            ra_retrans_interval = nbr.get('ra_retrans_interval')
            reachable_time = nbr.get('reachable_time')
            router_preference = nbr.get('router_preference')
            suppress = nbr.get('suppress')

            cfg_nbr = cfg_nbr_dict.get(interface)
            if cfg_nbr is None:
                continue
            cfg_adv_interval_option = cfg_nbr.get('adv_interval_option')
            cfg_dad = cfg_nbr.get('dad')
            cfg_home_agent_config = cfg_nbr.get('home_agent_config')
            cfg_home_agent_lifetime = cfg_nbr.get('home_agent_lifetime')
            cfg_home_agent_preference = cfg_nbr.get('home_agent_preference')
            cfg_interval = cfg_nbr.get('interval')
            cfg_lifetime = cfg_nbr.get('lifetime')
            cfg_managed_config = cfg_nbr.get('managed_config')
            cfg_min_ra_interval = cfg_nbr.get('min_ra_interval')
            cfg_min_ra_interval_msec = cfg_nbr.get('min_ra_interval_msec')
            cfg_mtu = cfg_nbr.get('mtu')
            cfg_other_config = cfg_nbr.get('other_config')
            cfg_ra_fast_retrans = cfg_nbr.get('ra_fast_retrans')
            cfg_ra_hop_limit = cfg_nbr.get('ra_hop_limit')
            cfg_ra_interval_msec = cfg_nbr.get('ra_interval_msec')
            cfg_ra_retrans_interval = cfg_nbr.get('ra_retrans_interval')
            cfg_reachable_time = cfg_nbr.get('reachable_time')
            cfg_router_preference = cfg_nbr.get('router_preference')
            cfg_suppress = cfg_nbr.get('suppress')

            if ((adv_interval_option is not None and cfg_adv_interval_option is not None and adv_interval_option != cfg_adv_interval_option) or
                    (dad and cfg_dad and dad != cfg_dad) or
                    (home_agent_config is not None and cfg_home_agent_config is not None and home_agent_config != cfg_home_agent_config) or
                    (home_agent_lifetime is not None and cfg_home_agent_lifetime is not None and home_agent_lifetime != cfg_home_agent_lifetime) or
                    (home_agent_preference is not None and cfg_home_agent_preference is not None and home_agent_preference !=
                     cfg_home_agent_preference) or
                    (interval and cfg_interval and interval != cfg_interval) or
                    (lifetime and cfg_lifetime and lifetime != cfg_lifetime) or
                    (managed_config is not None and cfg_managed_config is not None and managed_config != cfg_managed_config) or
                    (min_ra_interval and cfg_min_ra_interval and min_ra_interval != cfg_min_ra_interval) or
                    (min_ra_interval_msec and cfg_min_ra_interval_msec and min_ra_interval_msec != cfg_min_ra_interval_msec) or
                    (mtu is not None and cfg_mtu is not None and mtu != cfg_mtu) or
                    (other_config is not None and cfg_other_config is not None and other_config != cfg_other_config) or
                    (ra_fast_retrans is not None and cfg_ra_fast_retrans is not None and ra_fast_retrans != cfg_ra_fast_retrans) or
                    (ra_hop_limit is not None and cfg_ra_hop_limit is not None and ra_hop_limit != cfg_ra_hop_limit) or
                    (ra_interval_msec is not None and cfg_ra_interval_msec is not None and ra_interval_msec != cfg_ra_interval_msec) or
                    (ra_retrans_interval is not None and cfg_ra_retrans_interval is not None and ra_retrans_interval != cfg_ra_retrans_interval) or
                    (reachable_time is not None and cfg_reachable_time is not None and reachable_time != cfg_reachable_time) or
                    (router_preference and cfg_router_preference and router_preference != cfg_router_preference) or
                    (suppress is not None and cfg_suppress is not None and suppress != cfg_suppress)):

                ipv6_nbr_list.append(cfg_nbr)
                requests.append(self.get_delete_rt_adv_attr_req(interface, is_vlan, None))
                requests.append(self.get_delete_ipv6_cfg_attr_req(interface, is_vlan, '/ipv6_dad'))
                requests.append(self.get_delete_ipv6_nbr_attr_req(interface, is_vlan, None))
                continue

            ipv6_nbr_dict = {}
            dnssl = nbr.get('dnssl')
            neighbors = nbr.get('neighbors')
            ra_prefixes = nbr.get('ra_prefixes')
            rdnss = nbr.get('rdnss')
            cfg_dnssl = cfg_nbr.get('dnssl')
            cfg_neighbors = cfg_nbr.get('neighbors')
            cfg_ra_prefixes = cfg_nbr.get('ra_prefixes')
            cfg_rdnss = cfg_nbr.get('rdnss')

            # Handle replacement at dnssl level
            if dnssl and cfg_dnssl:
                cfg_dns_dict = {cfg_dns.get('name'): cfg_dns for cfg_dns in cfg_dnssl}
                dnssl_list = []
                for dns in dnssl:
                    name = dns.get('name')
                    cfg_dns = cfg_dns_dict.get(name)
                    if cfg_dns is None:
                        continue
                    if dns != cfg_dns:
                        cfg_name = cfg_dns['name']
                        dnssl_list.append(cfg_dns)
                        attr = f'/openconfig-interfaces-ext:dns-search-names/dns-search-name={cfg_name}'
                        requests.append(self.get_delete_rt_adv_attr_req(interface, is_vlan, attr))
                if dnssl_list:
                    ipv6_nbr_dict.update({'interface': interface, 'dnssl': dnssl_list})

            # Handle replacement at neighbors level
            if neighbors and cfg_neighbors:
                cfg_neighbor_dict = {cfg_neighbor.get('ip'): cfg_neighbor for cfg_neighbor in cfg_neighbors}
                neighbors_list = []
                for neighbor in neighbors:
                    ip = neighbor.get('ip')
                    cfg_neighbor = cfg_neighbor_dict.get(ip)
                    if cfg_neighbor is None:
                        continue
                    if neighbor != cfg_neighbor:
                        neighbors_list.append(cfg_neighbor)
                        encoded_ip = quote(cfg_neighbor['ip'], '')
                        attr = f'/neighbor={encoded_ip}'
                        requests.append(self.get_delete_ipv6_nbr_attr_req(interface, is_vlan, attr))
                if neighbors_list:
                    ipv6_nbr_dict.update({'interface': interface, 'neighbors': neighbors_list})

            # Handle replacement at ra_prefixes level
            if ra_prefixes and cfg_ra_prefixes:
                cfg_pfx_dict = {cfg_pfx.get('prefix'): cfg_pfx for cfg_pfx in cfg_ra_prefixes}
                ra_prefixes_list = []
                for pfx in ra_prefixes:
                    prefix = pfx.get('prefix')
                    cfg_pfx = cfg_pfx_dict.get(prefix)
                    if cfg_pfx is None:
                        continue
                    if pfx != cfg_pfx:
                        ra_prefixes_list.append(cfg_pfx)
                        encoded_pfx = quote(cfg_pfx['prefix'], '')
                        attr = f'/openconfig-interfaces-ext:ra-prefixes/ra-prefix={encoded_pfx}'
                        requests.append(self.get_delete_rt_adv_attr_req(interface, is_vlan, attr))
                if ra_prefixes_list:
                    ipv6_nbr_dict.update({'interface': interface, 'ra_prefixes': ra_prefixes_list})

            # Handle replacement at rdnss level
            if rdnss and cfg_rdnss:
                cfg_addr_dict = {cfg_addr.get('address'): cfg_addr for cfg_addr in cfg_rdnss}
                rdnss_list = []
                for addr in rdnss:
                    address = addr.get('address')
                    cfg_addr = cfg_addr_dict.get(address)
                    if cfg_addr is None:
                        continue
                    if addr != cfg_addr:
                        rdnss_list.append(cfg_addr)
                        encoded_addr = quote(cfg_addr['address'], '')
                        attr = f'/openconfig-interfaces-ext:rdnss-addresses/rdnss-address={encoded_addr}'
                        requests.append(self.get_delete_rt_adv_attr_req(interface, is_vlan, attr))
                if rdnss_list:
                    ipv6_nbr_dict.update({'interface': interface, 'rdnss': rdnss_list})

            if ipv6_nbr_dict:
                ipv6_nbr_list.append(ipv6_nbr_dict)
        if ipv6_nbr_list:
            config_dict['intf_ipv6_neighbors'] = ipv6_nbr_list

        return config_dict, requests

    def remove_default_entries(self, data):
        if data.get('ipv4_arp_timeout') == 180:
            data.pop('ipv4_arp_timeout')
        if data.get('ipv6_nd_cache_expiry') == 180:
            data.pop('ipv6_nd_cache_expiry')
        if data.get('num_local_neigh') == 0:
            data.pop('num_local_neigh')
        if data.get('ipv4_drop_neighbor_aging_time') == 300:
            data.pop('ipv4_drop_neighbor_aging_time')
        if data.get('ipv6_drop_neighbor_aging_time') == 300:
            data.pop('ipv6_drop_neighbor_aging_time')

        intf_ipv6_neighbors = data.get('intf_ipv6_neighbors')
        if intf_ipv6_neighbors:
            pop_list = []
            for nbr in intf_ipv6_neighbors:
                dad = nbr.get('dad')

                if dad == 'disable':
                    nbr.pop('dad')
                if 'interface' in nbr and len(nbr) == 1 or nbr['interface'] == 'Management0':
                    idx = intf_ipv6_neighbors.index(nbr)
                    pop_list.insert(0, idx)
            for idx in pop_list:
                intf_ipv6_neighbors.pop(idx)
            if not intf_ipv6_neighbors:
                data.pop('intf_ipv6_neighbors')

    def sort_lists_in_config(self, config):
        if config:
            intf_ipv6_neighbors = config.get('intf_ipv6_neighbors')
            if intf_ipv6_neighbors:
                intf_ipv6_neighbors.sort(key=lambda x: x['interface'])
                for nbr in intf_ipv6_neighbors:
                    dnssl = nbr.get('dnssl')
                    neighbors = nbr.get('neighbors')
                    ra_prefixes = nbr.get('ra_prefixes')
                    rdnss = nbr.get('rdnss')

                    if dnssl:
                        dnssl.sort(key=lambda x: x['name'])
                    if neighbors:
                        neighbors.sort(key=lambda x: x['ip'])
                    if ra_prefixes:
                        ra_prefixes.sort(key=lambda x: x['prefix'])
                    if rdnss:
                        rdnss.sort(key=lambda x: x['address'])

    def post_process_generated_config(self, config):
        if config:
            intf_ipv6_neighbors = config.get('intf_ipv6_neighbors')
            if intf_ipv6_neighbors:
                for nbr in intf_ipv6_neighbors:
                    if 'dnssl' in nbr and not nbr['dnssl']:
                        nbr.pop('dnssl')
                    if 'neighbors' in nbr and not nbr['neighbors']:
                        nbr.pop('neighbors')
                    if 'ra_prefixes' in nbr and not nbr['ra_prefixes']:
                        nbr.pop('ra_prefixes')
                    if 'rdnss' in nbr and not nbr['rdnss']:
                        nbr.pop('rdnss')
