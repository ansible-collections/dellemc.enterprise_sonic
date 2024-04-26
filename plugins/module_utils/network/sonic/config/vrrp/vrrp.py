#
# -*- coding: utf-8 -*-
# Copyright 2024 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_vrrp class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
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
    update_states,
    get_diff,
    remove_matching_defaults,
    remove_empties_from_list,
    get_replaced_config
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.formatted_diff_utils import (
    get_new_config,
    get_formatted_config_diff,
    __DELETE_CONFIG
)
from ansible.module_utils.connection import ConnectionError

PATCH = 'patch'
DELETE = 'delete'

ipv4_path = '/openconfig-if-ip:ipv4/addresses/address=1.1.1.1/'
ipv6_path = '/openconfig-if-ip:ipv6/addresses/address=1::1/'

TEST_KEYS = [
    {'config': {'name': ''}},
    {'group': {'virtual_router_id': '', 'afi': ''}},
    {'virtual_address': {'address': ''}},
    {'track_interface': {'interface': '', 'priority_increment': ''}}
]

TEST_KEYS_for_replaced = [
    {'config': {'name': ''}},
    {'group': {'virtual_router_id': '', 'afi': ''}}
]

TEST_KEYS_diff = [
    {'config': {'name': ''}},
    {'group': {'virtual_router_id': '', 'afi': ''}},
    {'virtual_address': {'address': ''}},
    {'track_interface': {'interface': '', 'priority_increment': ''}}
]

TEST_KEYS_overridden_diff = [
    {'config': {'name': '', '__delete_op': __DELETE_CONFIG}},
    {'group': {'virtual_router_id': '', 'afi': '', '__delete_op': __DELETE_CONFIG}},
    {'virtual_address': {'address': '', '__delete_op': __DELETE_CONFIG}},
    {'track_interface': {'interface': '', 'priority_increment': '', '__delete_op': __DELETE_CONFIG}}
]

default_entries = [
    [
        {'name': 'group'},
        {'name': 'priority', 'default': 100}
    ],
    [
        {'name': 'group'},
        {'name': 'preempt', 'default': True}
    ],
    [
        {'name': 'group'},
        {'name': 'advertisement_interval', 'default': 1}
    ],
    [
        {'name': 'group'},
        {'name': 'version', 'default': 2}
    ],
    [
        {'name': 'group'},
        {'name': 'use_v2_checksum', 'default': False}
    ],
]


class Vrrp(ConfigBase):
    """
    The sonic_vrrp class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'vrrp',
    ]

    vrrp_path = 'data/openconfig-interfaces:interfaces/interface={intf_name}'
    vrrp_vlan_path = vrrp_path + '/openconfig-vlan:routed-vlan'
    vrrp_intf_path = vrrp_path + '/subinterfaces/subinterface={intf_index}'

    vrrp_config_path = {
        'virtual_router_id': 'vrrp',
        'preempt': 'vrrp/vrrp-group={vrid}/config/preempt',
        'use_v2_checksum': 'vrrp/vrrp-group={vrid}/config/openconfig-interfaces-ext:use-v2-checksum',
        'priority': 'vrrp/vrrp-group={vrid}/config/priority',
        'advertisement_interval': 'vrrp/vrrp-group={vrid}/config/advertisement-interval',
        'version': 'vrrp/vrrp-group={vrid}/config/openconfig-interfaces-ext:version',
        'virtual_address': 'vrrp/vrrp-group={vrid}/config/virtual-address',
        'track_interface': 'vrrp/vrrp-group={vrid}/openconfig-interfaces-ext:vrrp-track'
    }

    def __init__(self, module):
        super(Vrrp, self).__init__(module)

    def get_vrrp_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        vrrp_facts = facts['ansible_network_resources'].get('vrrp')
        if not vrrp_facts:
            return []
        return vrrp_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = list()
        existing_vrrp_facts = self.get_vrrp_facts()
        commands, requests = self.set_config(existing_vrrp_facts)
        if commands and len(requests) > 0:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        changed_vrrp_facts = self.get_vrrp_facts()

        result['before'] = existing_vrrp_facts
        if result['changed']:
            result['after'] = changed_vrrp_facts

        new_config = changed_vrrp_facts
        old_config = existing_vrrp_facts
        if self._module.check_mode:
            result.pop('after', None)
            existing_vrrp_facts = remove_empties_from_list(existing_vrrp_facts)
            is_overridden = False
            for cmd in commands:
                if cmd['state'] == "overridden":
                    is_overridden = True
                    break
            if is_overridden:
                new_config = get_new_config(commands, existing_vrrp_facts, TEST_KEYS_overridden_diff)
            else:
                new_config = get_new_config(commands, existing_vrrp_facts, TEST_KEYS_diff)
            result['after(generated)'] = remove_empties_from_list(new_config)

        if self._module._diff:
            self.sort_lists_in_config(old_config)
            self.sort_lists_in_config(new_config)
            result['diff'] = get_formatted_config_diff(old_config, new_config, self._module._verbosity)

        result['warnings'] = warnings
        return result

    def set_config(self, existing_vrrp_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']
        have = existing_vrrp_facts
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

        if state == 'overridden':
            commands, requests = self._state_overridden(want, have)
        elif state == 'deleted':
            commands, requests = self._state_deleted(want, have)
        elif state == 'merged':
            commands, requests = self._state_merged(want, have)
        elif state == 'replaced':
            commands, requests = self._state_replaced(want, have)
        return commands, requests

    def _state_replaced(self, want, have):
        """ The command generator when state is replaced

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands, requests = [], []
        mod_commands = []
        diff = get_diff(want, have, TEST_KEYS)
        self.sort_lists_in_config(want)
        self.sort_lists_in_config(have)
        new_have = deepcopy(have)
        new_want = deepcopy(want)
        for default_entry in default_entries:
            remove_matching_defaults(new_have, default_entry)
            remove_matching_defaults(new_want, default_entry)
        new_have = remove_empties_from_list(new_have)
        new_want = remove_empties_from_list(new_want)
        replaced_config = get_replaced_config(new_want, new_have, TEST_KEYS_for_replaced)
        if replaced_config:
            is_delete_all = (replaced_config == new_have)
            del_requests = self.get_delete_vrrp_requests(replaced_config, new_have, is_delete_all)
            if len(del_requests) > 0:
                requests.extend(del_requests)
                commands.extend(update_states(replaced_config, "deleted"))
            mod_commands = new_want
        else:
            mod_commands = diff
        if mod_commands:
            mod_requests = self.get_create_vrrp_requests(mod_commands, have)
            if len(mod_requests) > 0:
                requests.extend(mod_requests)
                commands.extend(update_states(mod_commands, "replaced"))
        return commands, requests

    def _state_overridden(self, want, have):
        """ The command generator when state is overridden

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands, requests = [], []
        self.sort_lists_in_config(want)
        self.sort_lists_in_config(have)
        new_have = deepcopy(have)
        new_want = deepcopy(want)
        for default_entry in default_entries:
            remove_matching_defaults(new_have, default_entry)
            remove_matching_defaults(new_want, default_entry)
        new_have = remove_empties_from_list(new_have)
        new_want = remove_empties_from_list(new_want)
        diff = get_diff(new_want, new_have, TEST_KEYS)
        diff2 = get_diff(new_have, new_want, TEST_KEYS)
        if diff or diff2:
            is_delete_all = True
            del_requests = self.get_delete_vrrp_requests(have, have, is_delete_all)
            if len(del_requests) > 0:
                requests.extend(del_requests)
                commands.extend(update_states(have, "deleted"))
            mod_requests = self.get_create_vrrp_requests(new_want, [])
            if len(mod_requests) > 0:
                requests.extend(mod_requests)
                commands.extend(update_states(want, "overridden"))
        return commands, requests

    def _state_merged(self, want, have):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = get_diff(want, have)
        requests = self.get_create_vrrp_requests(commands, have)

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
        commands = []
        requests = []
        is_delete_all = False

        if not want:
            commands = have
            is_delete_all = True
        else:
            self.sort_lists_in_config(want)
            self.sort_lists_in_config(have)
            new_want = deepcopy(want)
            for default_entry in default_entries:
                remove_matching_defaults(new_want, default_entry)
            new_want = remove_empties_from_list(new_want)
            commands = new_want

        requests = self.get_delete_vrrp_requests(commands, have, is_delete_all)

        if commands and len(requests) > 0:
            commands = update_states(commands, 'deleted')
        else:
            commands = []

        return commands, requests

    def get_create_vrrp_requests(self, commands, have):
        """ Get list of requests to create/modify VRRP and VRRP6 configurations
        for all interfaces specified by the commands
        """
        requests = []

        if not commands:
            return requests

        for cmd in commands:
            name = cmd.get('name', None)
            intf_name = name.replace('/', '%2f')
            group_list = cmd.get('group', [])
            if group_list:
                for group in group_list:
                    virtual_router_id = group.get('virtual_router_id', None)
                    if "Vlan" in intf_name:
                        keypath = self.vrrp_vlan_path.format(intf_name=intf_name)
                    else:
                        parent_intf, sub_intf = intf_name.split(".") if "." in intf_name else (intf_name, 0)
                        keypath = self.vrrp_intf_path.format(intf_name=parent_intf, intf_index=sub_intf)
                    requests.extend(self.get_create_specific_vrrp_param_requests(virtual_router_id, group, keypath))

        return requests

    def get_create_specific_vrrp_param_requests(self, virtual_router_id, group, keypath):
        """ Get list of requests to create/modify VRRP and VRRP6 configurations
        based on the command specified for the interface
        """
        requests = []

        afi = group.get('afi')
        ip_path = ipv4_path
        vip_addresses = self.get_vip_addresses(group.get('virtual_address'))
        preempt = group.get('preempt')
        advertisement_interval = group.get('advertisement_interval')
        priority = group.get('priority')
        version = group.get('version')
        use_v2_checksum = group.get('use_v2_checksum')
        track_interfaces = self.get_track_interfaces(group.get('track_interface'))
        if not virtual_router_id or not afi:
            return requests

        def update_requests(attr, payload):
            url = keypath + ip_path + self.vrrp_config_path[attr].format(vrid=virtual_router_id)
            return [{'path': url, 'method': PATCH, 'data': payload}]

        if afi:
            payload = {
                'openconfig-if-ip:vrrp': {
                    'vrrp-group':
                    [
                        {
                            'virtual-router-id': virtual_router_id,
                            'config': {'virtual-router-id': virtual_router_id}
                        }
                    ]
                }
            }

            if afi == "ipv6":
                ip_path = ipv6_path
            url = keypath + ip_path + self.vrrp_config_path['virtual_router_id']

            requests.append({'path': url, 'method': PATCH, 'data': payload})

        if vip_addresses:
            requests.extend(update_requests('virtual_address', {"openconfig-if-ip:virtual-address": vip_addresses}))

        if preempt is not None:
            requests.extend(update_requests('preempt', {"openconfig-if-ip:preempt": preempt}))

        if advertisement_interval:
            requests.extend(update_requests('advertisement_interval', {"openconfig-if-ip:advertisement-interval": advertisement_interval}))

        if priority:
            requests.extend(update_requests('priority', {"openconfig-if-ip:priority": priority}))

        if version:
            requests.extend(update_requests('version', {"openconfig-interfaces-ext:version": version}))

        if use_v2_checksum is not None:
            requests.extend(update_requests('use_v2_checksum', {"openconfig-if-ip:use-v2-checksum": use_v2_checksum}))

        if track_interfaces:
            for track in track_interfaces:
                interface = track['interface']
                priority_increment = track['priority_increment']

                payload = {
                    "openconfig-interfaces-ext:vrrp-track": {
                        "vrrp-track-interface": [
                            {
                                "track-intf": interface,
                                "config": {
                                    "track-intf": interface,
                                    "priority-increment": int(priority_increment),
                                },
                            }
                        ]
                    }
                }
                requests.extend(update_requests('track_interface', payload))
        return requests

    def get_delete_vrrp_requests(self, commands, have, is_delete_all):
        """ Get list of requests to delete VRRP and VRRP6 configurations
        for all interfaces specified by the commands
        """
        requests = []

        for cmd in commands:
            name = cmd.get('name', None)
            intf_name = name.replace('/', '%2f')
            group_list = [] if cmd.get('group', []) is None else cmd.get('group', [])

            if is_delete_all:
                last_vrrp = []
                for group in group_list:
                    virtual_router_id = group.get('virtual_router_id')
                    afi = group.get('afi')
                    # VRRP with VRRP ID 1 can be removed only if other VRRP
                    # groups are removed first
                    # Hence the check
                    if virtual_router_id == 1:
                        last_vrrp.extend(self.get_delete_vrrp_group(intf_name, virtual_router_id, afi))
                    else:
                        requests.extend(self.get_delete_vrrp_group(intf_name, virtual_router_id, afi))
                if last_vrrp:
                    requests.extend(last_vrrp)
            else:
                for group in group_list:
                    virtual_router_id = group.get('virtual_router_id')
                    afi = group.get('afi')
                    for cfg in have:
                        cfg_name = cfg.get('name')
                        cfg_intf_name = cfg_name.replace('/', '%2f')
                        if cfg_intf_name == intf_name:
                            cfg_group_list = [] if cfg.get('group', []) is None else cfg.get('group', [])
                            for cfg_group in cfg_group_list:
                                cfg_virtual_router_id = cfg_group.get('virtual_router_id')
                                cfg_afi = cfg_group.get('afi')
                                if cfg_virtual_router_id == virtual_router_id and cfg_afi == afi:
                                    if len(cfg_group.keys()) == 2:
                                        requests.extend(self.get_delete_vrrp_group(intf_name, virtual_router_id, afi))
                                        continue
                                    if "Vlan" in intf_name:
                                        keypath = self.vrrp_vlan_path.format(intf_name=intf_name)
                                        requests.extend(self.get_delete_specific_vrrp_param_requests(cfg_group, virtual_router_id, group, keypath))
                                    else:
                                        parent_intf = intf_name.split(".")[0] if "." in intf_name else intf_name
                                        sub_intf = intf_name.split(".")[1] if "." in intf_name else 0
                                        keypath = self.vrrp_intf_path.format(intf_name=parent_intf, intf_index=sub_intf)
                                        requests.extend(self.get_delete_specific_vrrp_param_requests(cfg_group, virtual_router_id, group, keypath))
                if not group_list:
                    for cfg in have:
                        cfg_name = cfg.get('name')
                        cfg_intf_name = cfg_name.replace('/', '%2f')

                        if cfg_intf_name == intf_name:
                            cfg_group_list = cfg.get('group', [])
                            last_vrrp = []
                            for cfg_group in cfg_group_list:
                                cfg_virtual_router_id = cfg_group.get('virtual_router_id')
                                cfg_afi = cfg_group.get('afi')
                                # VRRP with VRRP ID 1 can be removed only if other VRRP
                                # groups are removed first
                                # Hence the check
                                if cfg_virtual_router_id == 1:
                                    last_vrrp.extend(self.get_delete_vrrp_group(cfg_intf_name, cfg_virtual_router_id, cfg_afi))
                                else:
                                    requests.extend(self.get_delete_vrrp_group(cfg_intf_name, cfg_virtual_router_id, cfg_afi))
                            if last_vrrp:
                                requests.extend(last_vrrp)
        return requests

    def get_delete_vrrp_group(self, intf_name, virtual_router_id, afi):
        """ Get list of requests to delete the entire VRRP and VRRP6 group configurations
        based on the specified interface
        """
        requests = []
        if not virtual_router_id or not afi:
            return requests

        ip_path = ipv4_path if afi == "ipv4" else ipv6_path
        if "Vlan" in intf_name:
            keypath = self.vrrp_vlan_path.format(intf_name=intf_name)
        else:
            parent_intf, sub_intf = intf_name.split(".") if "." in intf_name else (intf_name, 0)
            keypath = self.vrrp_intf_path.format(intf_name=parent_intf, intf_index=sub_intf)
        url = f"{keypath}{ip_path}vrrp/vrrp-group={virtual_router_id}"
        requests.append({'path': url, 'method': DELETE})

        return requests

    def get_delete_specific_vrrp_param_requests(self, cfg_group, virtual_router_id, group, keypath):
        """ Get list of requests to delete VRRP and VRRP6 configurations
        based on the command specified for the interface
        """
        requests = []

        afi = group.get('afi')
        vip_addresses = self.get_vip_addresses(group.get('virtual_address'))
        preempt = group.get('preempt')
        ip_path = ipv4_path if afi == "ipv4" else ipv6_path
        adv_interval = group.get('advertisement_interval')
        priority = group.get('priority')
        version = group.get('version')
        use_v2_checksum = group.get('use_v2_checksum')
        track_interfaces = self.get_track_interfaces(group.get('track_interface'))

        if not virtual_router_id or not afi:
            return requests

        cfg_vip_addresses = self.get_vip_addresses(cfg_group.get('virtual_address'))
        cfg_preempt = cfg_group.get('preempt')
        cfg_adv_interval = cfg_group.get('advertisement_interval')
        cfg_priority = cfg_group.get('priority')
        cfg_version = cfg_group.get('version')
        cfg_use_v2_checksum = cfg_group.get('use_v2_checksum')
        cfg_track_interfaces = self.get_track_interfaces(cfg_group.get('track_interface'))

        if not (vip_addresses or preempt or adv_interval or priority or version or use_v2_checksum or track_interfaces):
            url = keypath + ip_path + "vrrp/vrrp-group={vrid}".format(vrid=virtual_router_id)
            requests.append({'path': url, 'method': DELETE})
            return requests

        def update_requests(group_attr, cfg_attr, attr_path):
            if group_attr == cfg_attr:
                url = keypath + ip_path + attr_path
                return [{'path': url, 'method': DELETE}]
            return []

        if vip_addresses and cfg_vip_addresses:
            for addr in vip_addresses:
                for cfg_addr in cfg_vip_addresses:
                    requests.extend(update_requests(addr, cfg_addr, self.vrrp_config_path['virtual_address'].format(vrid=virtual_router_id) + "=" + addr))

        if preempt is not None and cfg_preempt is not None:
            requests.extend(update_requests(preempt, cfg_preempt, self.vrrp_config_path['preempt'].format(vrid=virtual_router_id)))

        if adv_interval and cfg_adv_interval:
            requests.extend(update_requests(adv_interval, cfg_adv_interval, self.vrrp_config_path['advertisement_interval'].format(vrid=virtual_router_id)))

        if priority and cfg_priority:
            requests.extend(update_requests(priority, cfg_priority, self.vrrp_config_path['priority'].format(vrid=virtual_router_id)))

        if version and cfg_version:
            requests.extend(update_requests(version, cfg_version, self.vrrp_config_path['version'].format(vrid=virtual_router_id)))

        if use_v2_checksum is not None and cfg_use_v2_checksum is not None:
            requests.extend(update_requests(use_v2_checksum, cfg_use_v2_checksum, self.vrrp_config_path['use_v2_checksum'].format(vrid=virtual_router_id)))

        if track_interfaces and cfg_track_interfaces:
            for track in track_interfaces:
                interface = track['interface']
                interface = interface.replace('/', '%2f')
                for cfg_track in cfg_track_interfaces:
                    cfg_interface = cfg_track['interface']
                    cfg_interface = cfg_interface.replace('/', '%2f')
                    track_url = self.vrrp_config_path['track_interface'].format(vrid=virtual_router_id) + "/vrrp-track-interface=" + interface
                    requests.extend(update_requests(interface, cfg_interface, track_url))
        return requests

    def sort_lists_in_config(self, config):
        if config:
            config.sort(key=lambda x: x['name'])
            for cfg in config:
                if cfg.get('group'):
                    cfg['group'].sort(key=lambda x: x['virtual_router_id'])
                    for group in cfg['group']:
                        if group.get('virtual_address'):
                            group['virtual_address'].sort(key=lambda x: x['address'])
                        if group.get('track_interface'):
                            group['track_interface'].sort(key=lambda x: x['interface'])

    @staticmethod
    def get_vip_addresses(vip_addresses_list):
        """ Get a set of virtual IP/IPv6 addresses available in the given
        vip_addresses list
        """
        vip_addresses = []
        if not vip_addresses_list:
            return vip_addresses

        for addr in vip_addresses_list:
            if addr.get('address'):
                vip_addresses.append(addr['address'])

        return vip_addresses

    @staticmethod
    def get_track_interfaces(track_interfaces_list):
        """ Get a set of track interface groups available in the given
        track_interfaces list
        """
        track_interfaces = []
        if not track_interfaces_list:
            return track_interfaces

        for track_interface in track_interfaces_list:
            if track_interface['interface'] and track_interface['priority_increment']:
                track_interfaces.append(track_interface)

        return track_interfaces
