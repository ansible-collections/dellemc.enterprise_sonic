#
# -*- coding: utf-8 -*-
# Copyright 2022 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_vrrp class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import Facts

from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils \
    import (
        get_diff,
        update_states,
    )

from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)

PATCH = 'patch'
DELETE = 'delete'

ipv4_path = '/openconfig-if-ip:ipv4/addresses/address=1.1.1.1/'
ipv6_path = '/openconfig-if-ip:ipv6/addresses/address=1::1/'

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
        commands = list()

        existing_vrrp_facts = self.get_vrrp_facts()
        commands, requests = self.set_config(existing_vrrp_facts)
        if commands and len(requests) > 0:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module,
                        requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        changed_vrrp_facts = self.get_vrrp_facts()

        result['before'] = existing_vrrp_facts
        if result['changed']:
            result['after'] = changed_vrrp_facts

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
        diff = get_diff(want, have)

        if state == 'overridden':
            commands, requests = self._state_overridden(want, have, diff)
        elif state == 'deleted':
            commands, requests = self._state_deleted(want, have)
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
        commands = []
        requests = []

        commands_del = []
        requests_del = []

        if diff:
            commands_del = self.get_replaced_vrrp_group_list(want, have)

        if commands_del:
            is_delete_all = False
            requests_del = self.get_delete_vrrp_requests(commands_del, have, is_delete_all)
        if requests_del:
            requests.extend(requests_del)
            commands_del = update_states(commands_del, "deleted")
            commands.extend(commands_del)

        commands_replace = diff
        requests_replace = []
        if commands_replace:
            requests_replace = self.get_create_vrrp_requests(commands_replace, have)
        if requests_replace:
            requests.extend(requests_replace)
            commands_over = update_states(commands_replace, "replaced")
            commands.extend(commands_replace)

        return commands, requests

    def _state_overridden(self, want, have, diff):
        """ The command generator when state is overridden

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        requests = []
        commands = []

        commands_del = []
        requests_del = []

        if diff:
            commands_del = self.get_overridden_vrrp_group_list(diff, have)

        if commands_del:
            is_delete_all = True
            requests_del = self.get_delete_vrrp_requests(commands_del, have, is_delete_all)
        if requests_del:
            commands_del = want
            requests.extend(requests_del)
            commands_del = update_states(commands_del, "deleted")
            commands.extend(commands_del)

        commands_over = diff
        requests_over = []
        if commands_over:
            requests_over = self.get_create_vrrp_requests(commands_over, have)
        if requests_over:
            requests.extend(requests_over)
            commands_over = update_states(commands_over, "overridden")
            commands.extend(commands_over)

        return commands, requests

    def _state_merged(self, want, have, diff):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = diff
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
            commands = want

        requests.extend(self.get_delete_vrrp_requests(commands, have, is_delete_all))

        if len(requests) == 0:
            commands = []

        if commands:
            commands = update_states(commands, 'deleted')

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
            intf_name = name.replace('/', '%2F')
            group_list = cmd.get('group', [])
            if group_list:
                for group in group_list:
                    virtual_router_id = group.get('virtual_router_id', None)
                    if "Vlan" in intf_name:
                        keypath = self.vrrp_vlan_path.format(intf_name=intf_name)
                        requests.extend(self.get_create_specific_vrrp_param_requests(virtual_router_id, group, keypath))
                    else:
                        parent_intf = intf_name
                        sub_intf = 0
                        if "." in parent_intf:
                            parent_intf = intf_name.split(".")[0]
                            sub_intf = intf_name.split(".")[1]
                        keypath = self.vrrp_intf_path.format(intf_name=parent_intf, intf_index=sub_intf)
                        requests.extend(self.get_create_specific_vrrp_param_requests(virtual_router_id, group, keypath))

        return requests

    def get_create_specific_vrrp_param_requests(self, virtual_router_id, group, keypath):
        """ Get list of requests to create/modify VRRP and VRRP6 configurations
        based on the command specified for the interface
        """
        requests = []

        afi = group.get('afi', None)
        vip_addresses = self.get_vip_addresses(group.get('virtual_address'))
        preempt = group.get('preempt', None)
        advertisement_interval = group.get('advertisement_interval', None)
        priority = group.get('priority', None)
        version = group.get('version', None)
        use_v2_checksum = group.get('use_v2_checksum', None)
        track_interfaces = self.get_track_interfaces(group.get('track_interface'))
        if virtual_router_id is None:
            return requests

        if afi is None:
            return requests

        if afi:
            payload = {
                    'openconfig-if-ip:vrrp': {
                        'vrrp-group':[{
                                'virtual-router-id': virtual_router_id,
                                'config': {'virtual-router-id': virtual_router_id}}]
                        }
                    }

            if afi == "ipv4":
                url = keypath + ipv4_path + self.vrrp_config_path['virtual_router_id']
            if afi == "ipv6":
                url = keypath + ipv6_path + self.vrrp_config_path['virtual_router_id']

            requests.append({'path': url, 'method': PATCH, 'data': payload})

        if vip_addresses:
            for addr in vip_addresses:
                payload = {"openconfig-if-ip:virtual-address": [addr]}
                if afi == "ipv4":
                    url = keypath + ipv4_path + self.vrrp_config_path['virtual_address'].format(vrid=virtual_router_id)
                if afi == "ipv6":
                    url = keypath + ipv6_path + self.vrrp_config_path['virtual_address'].format(vrid=virtual_router_id)

                requests.append({'path': url, 'method': PATCH, 'data': payload})

        if preempt is not None:
            payload = {"openconfig-if-ip:preempt": preempt}
            if afi == "ipv4":
                url = keypath + ipv4_path + self.vrrp_config_path['preempt'].format(vrid=virtual_router_id)
            if afi == "ipv6":
                url = keypath + ipv6_path + self.vrrp_config_path['preempt'].format(vrid=virtual_router_id)

            requests.append({'path': url, 'method': PATCH, 'data': payload})

        if advertisement_interval:
            payload = {"openconfig-if-ip:advertisement-interval": advertisement_interval }
            if afi == "ipv4":
                url = keypath + ipv4_path + self.vrrp_config_path['advertisement_interval'].format(vrid=virtual_router_id)
            if afi == "ipv6":
                url = keypath + ipv6_path + self.vrrp_config_path['advertisement_interval'].format(vrid=virtual_router_id)

            requests.append({'path': url, 'method': PATCH, 'data': payload})

        if priority:
            payload = {"openconfig-if-ip:priority": priority }
            if afi == "ipv4":
                url = keypath + ipv4_path + self.vrrp_config_path['priority'].format(vrid=virtual_router_id)
            if afi == "ipv6":
                url = keypath + ipv6_path + self.vrrp_config_path['priority'].format(vrid=virtual_router_id)

            requests.append({'path': url, 'method': PATCH, 'data': payload})

        if version:
            payload = {"openconfig-interfaces-ext:version": version }
            if afi == "ipv4":
                url = keypath + ipv4_path + self.vrrp_config_path['version'].format(vrid=virtual_router_id)
            if afi == "ipv6":
                url = keypath + ipv6_path + self.vrrp_config_path['version'].format(vrid=virtual_router_id)

            requests.append({'path': url, 'method': PATCH, 'data': payload})

        if use_v2_checksum is not None:
            payload = {"openconfig-if-ip:use-v2-checksum": use_v2_checksum }
            if afi == "ipv4":
                url = keypath + ipv4_path + self.vrrp_config_path['use_v2_checksum'].format(vrid=virtual_router_id)
            if afi == "ipv6":
                url = keypath + ipv6_path + self.vrrp_config_path['use_v2_checksum'].format(vrid=virtual_router_id)

            requests.append({'path': url, 'method': PATCH, 'data': payload})

        if track_interfaces:
            for track in track_interfaces:
                interface = track['interface']
                priority_increment = track['priority_increment']

                payload = {
                        "openconfig-interfaces-ext:vrrp-track": {
                            "vrrp-track-interface": [{
                                "track-intf": interface,
                                "config": {
                                    "track-intf": interface,
                                    "priority-increment": int(priority_increment),
                                    },
                                }]
                            }
                        }

                if afi == "ipv4":
                    url = keypath + ipv4_path + self.vrrp_config_path['track_interface'].format(vrid=virtual_router_id)
                if afi == "ipv6":
                    url = keypath + ipv6_path + self.vrrp_config_path['track_interface'].format(vrid=virtual_router_id)

                requests.append({'path': url, 'method': PATCH, 'data': payload})
        return requests

    def get_delete_vrrp_requests(self, commands, have, is_delete_all):
        """ Get list of requests to delete VRRP and VRRP6 configurations
        for all interfaces specified by the commands
        """
        requests = []

        if is_delete_all:
            for cmd in commands:
                name = cmd.get('name', None)
                intf_name = name.replace('/', '%2F')
                group_list = cmd.get('group', [])

                if group_list:
                    last_vrrp = []
                    for group in group_list:
                        virtual_router_id = group.get('virtual_router_id', None)
                        afi = group.get('afi', None)
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
            for cmd in commands:
                name = cmd.get('name', None)
                intf_name = name.replace('/', '%2F')
                group_list = cmd.get('group', [])

                if group_list:
                    for group in group_list:
                        virtual_router_id = group.get('virtual_router_id', None)
                        afi = group.get('afi', None)
                        for cfg in have:
                            cfg_name = cfg.get('name', None)
                            cfg_intf_name = cfg_name.replace('/', '%2F')
                            if cfg_intf_name == intf_name:
                                cfg_group_list = cfg.get('group', None)
                                if cfg_group_list:
                                    for cfg_group in cfg_group_list:
                                        cfg_virtual_router_id = cfg_group.get('virtual_router_id', None)
                                        cfg_afi = cfg_group.get('afi', None)

                                        if cfg_virtual_router_id == virtual_router_id:
                                            if cfg_afi == afi:
                                                if "Vlan" in intf_name:
                                                    keypath =self.vrrp_vlan_path.format(intf_name=intf_name)
                                                    requests.extend(self.get_delete_specific_vrrp_param_requests(cfg_group, virtual_router_id, group, keypath))
                                                else:
                                                    parent_intf = intf_name
                                                    sub_intf = 0
                                                    if "." in parent_intf:
                                                        parent_intf = intf_name.split(".")[0]
                                                        sub_intf = intf_name.split(".")[1]
                                                    keypath = self.vrrp_intf_path.format(intf_name=parent_intf, intf_index=sub_intf)
                                                    requests.extend(self.get_delete_specific_vrrp_param_requests(cfg_group, virtual_router_id, group, keypath))
                else:
                    for cfg in have:
                        cfg_name = cfg.get('name', None)
                        cfg_intf_name = cfg_name.replace('/', '%2F')

                        if cfg_intf_name == intf_name:
                            cfg_group_list = cfg.get('group', None)
                            if cfg_group_list:
                                last_vrrp = []
                                for cfg_group in cfg_group_list:
                                    cfg_virtual_router_id = cfg_group.get('virtual_router_id', None)
                                    cfg_afi = cfg_group.get('afi', None)
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
        if virtual_router_id is None:
            return requests

        if afi is None:
            return requests

        if afi:
            if "Vlan" in intf_name:
                keypath = self.vrrp_vlan_path.format(intf_name=intf_name)
            else:
                parent_intf = intf_name
                sub_intf = 0
                if "." in parent_intf:
                    parent_intf = intf_name.split(".")[0]
                    sub_intf = intf_name.split(".")[1]
                keypath = self.vrrp_intf_path.format(intf_name=parent_intf, intf_index=sub_intf)
            if afi == "ipv4":
                url = keypath + ipv4_path + "vrrp/vrrp-group={vrid}".format(vrid=virtual_router_id)
            if afi == "ipv6":
                url = keypath + ipv6_path + "vrrp/vrrp-group={vrid}".format(vrid=virtual_router_id)
            requests.append({'path': url, 'method': DELETE})

        return requests

    def get_delete_specific_vrrp_param_requests(self, cfg_group, virtual_router_id, group, keypath):
        """ Get list of requests to delete VRRP and VRRP6 configurations
        based on the command specified for the interface
        """
        requests = []

        afi = group.get('afi', None)
        vip_addresses = self.get_vip_addresses(group.get('virtual_address'))
        preempt = group.get('preempt', None)
        advertisement_interval = group.get('advertisement_interval', None)
        priority = group.get('priority', None)
        version = group.get('version', None)
        use_v2_checksum = group.get('use_v2_checksum', None)
        track_interfaces = self.get_track_interfaces(group.get('track_interface'))

        if virtual_router_id is None:
            return requests

        if afi is None:
            return requests

        cfg_vip_addresses = self.get_vip_addresses(cfg_group.get('virtual_address'))
        cfg_preempt = cfg_group.get('preempt', None)
        cfg_advertisement_interval = cfg_group.get('advertisement_interval', None)
        cfg_priority = cfg_group.get('priority', None)
        cfg_version = cfg_group.get('version', None)
        cfg_use_v2_checksum = cfg_group.get('use_v2_checksum', None)
        cfg_track_interfaces = self.get_track_interfaces(cfg_group.get('track_interface'))

        if not (vip_addresses or preempt or advertisement_interval or priority or version or use_v2_checksum or track_interfaces):
            if afi == "ipv4":
                url = keypath + ipv4_path + "vrrp/vrrp-group={vrid}".format(vrid=virtual_router_id)
            if afi == "ipv6":
                url = keypath + ipv6_path + "vrrp/vrrp-group={vrid}".format(vrid=virtual_router_id)
            requests.append({'path': url, 'method': DELETE})
            return requests

        if vip_addresses and cfg_vip_addresses:
            for addr in vip_addresses:
                for cfg_addr in cfg_vip_addresses:
                    if addr == cfg_addr:
                        if afi == "ipv4":
                            url = keypath + ipv4_path + self.vrrp_config_path['virtual_address'].format(vrid=virtual_router_id) + "=" + addr
                        if afi == "ipv6":
                            url = keypath + ipv6_path + self.vrrp_config_path['virtual_address'].format(vrid=virtual_router_id) + "=" + addr

                        requests.append({'path': url, 'method': DELETE})

        if preempt is not None and cfg_preempt is not None:
            if preempt == cfg_preempt:
                if afi == "ipv4":
                    url = keypath + ipv4_path + self.vrrp_config_path['preempt'].format(vrid=virtual_router_id)
                if afi == "ipv6":
                    url = keypath + ipv6_path + self.vrrp_config_path['preempt'].format(vrid=virtual_router_id)

                requests.append({'path': url, 'method': DELETE})

        if advertisement_interval and cfg_advertisement_interval:
            if advertisement_interval == cfg_advertisement_interval:
                if afi == "ipv4":
                    url = keypath + ipv4_path + self.vrrp_config_path['advertisement_interval'].format(vrid=virtual_router_id)
                if afi == "ipv6":
                    url = keypath + ipv6_path + self.vrrp_config_path['advertisement_interval'].format(vrid=virtual_router_id)

                requests.append({'path': url, 'method': DELETE})

        if priority and cfg_priority:
            if priority == cfg_priority:
                if afi == "ipv4":
                    url = keypath + ipv4_path + self.vrrp_config_path['priority'].format(vrid=virtual_router_id)
                if afi == "ipv6":
                    url = keypath + ipv6_path + self.vrrp_config_path['priority'].format(vrid=virtual_router_id)

                requests.append({'path': url, 'method': DELETE})

        if version and cfg_version:
            if version == cfg_version:
                if afi == "ipv4":
                    url = keypath + ipv4_path + self.vrrp_config_path['version'].format(vrid=virtual_router_id)
                if afi == "ipv6":
                    url = keypath + ipv6_path + self.vrrp_config_path['version'].format(vrid=virtual_router_id)

                requests.append({'path': url, 'method': DELETE})

        if use_v2_checksum is not None and cfg_use_v2_checksum is not None:
            if use_v2_checksum == cfg_use_v2_checksum:
                if afi == "ipv4":
                    url = keypath + ipv4_path + self.vrrp_config_path['use_v2_checksum'].format(vrid=virtual_router_id)
                if afi == "ipv6":
                    url = keypath + ipv6_path + self.vrrp_config_path['use_v2_checksum'].format(vrid=virtual_router_id)

                requests.append({'path': url, 'method': DELETE})

        if track_interfaces and cfg_track_interfaces:
            for track in track_interfaces:
                interface = track['interface']
                interface = interface.replace('/', '%2F')
                for cfg_track in cfg_track_interfaces:
                    cfg_interface = cfg_track['interface']
                    cfg_interface = cfg_interface.replace('/', '%2F')
                    if interface == cfg_interface:
                        if afi == "ipv4":
                            url = keypath + ipv4_path + self.vrrp_config_path['track_interface'].format(vrid=virtual_router_id) + "/vrrp-track-interface={trackif}".format(trackif=interface)
                        if afi == "ipv6":
                            url = keypath + ipv6_path + self.vrrp_config_path['track_interface'].format(vrid=virtual_router_id) + "/vrrp-track-interface={trackif}".format(trackif=interface)

                        requests.append({'path': url, 'method': DELETE})
        return requests

    def get_overridden_vrrp_group_list(self, want, have):
        """ Get all the commands to override VRRP and VRRP6 configurations
        based on the specified interface
        """
        commands = []

        for cmd in want:
            intf_name = cmd.get('name', None)
            if intf_name:
                for cfg in have:
                    cfg_intf_name = cfg.get('name', None)
                    if cfg_intf_name and intf_name == cfg_intf_name:
                        cfg_group = cfg.get('group', [])
                        commands.append({'name': intf_name, 'group': cfg_group})
                        break
        return commands

    def get_replaced_vrrp_group_list(self, want, have):
        """ Get all the commands to replace VRRP and VRRP6 configurations
        based on the specified interface
        """
        commands = []
        for cmd in want:
            intf_name = cmd.get('name', None)
            group_list = cmd.get('group', [])
            if intf_name and group_list:
                for cfg in have:
                    cfg_intf_name = cfg.get('name', None)
                    if cfg_intf_name and intf_name == cfg_intf_name:
                        cfg_group_list = cfg.get('group', [])
                        if cfg_group_list:
                            delete_group_list = []
                            for group in group_list:
                                virtual_router_id = group.get('virtual_router_id', None)
                                afi = group.get('afi', None)
                                if virtual_router_id and afi:
                                    for cfg_group in cfg_group_list:
                                        cfg_virtual_router_id = cfg_group.get('virtual_router_id', None)
                                        cfg_afi = cfg_group.get('afi', None)
                                        if cfg_virtual_router_id and cfg_afi:
                                            if cfg_virtual_router_id == virtual_router_id and cfg_afi == afi:
                                                delete_group_list.append(cfg_group)
                                                break
                            commands.append({'name': intf_name, 'group': delete_group_list})
                            break

        return commands

    @staticmethod
    def get_vip_addresses(vip_addresses_list):
        """ Get a set of virtual IP/IPv6 addresses available in the given
        vip_addresses list
        """
        vip_addresses = set()
        if not vip_addresses_list:
            return vip_addresses

        for addr in vip_addresses_list:
            if addr.get('address'):
                vip_addresses.add(addr['address'])

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
