#
# -*- coding: utf-8 -*-
# Copyright 2023 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_stp class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import re
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
    get_ranges_in_list,
    get_diff,
    remove_empties,
)
from ansible.module_utils.connection import ConnectionError


PATCH = 'patch'
DELETE = 'delete'
TEST_KEYS = [
    {'interfaces': {'intf_name': ''}},
    {'mst_instances': {'mst_id': ''}},
    {'pvst': {'vlan_id': ''}},
    {'rapid_pvst': {'vlan_id': ''}},
]
STP_PATH = 'data/openconfig-spanning-tree:stp'
stp_map = {
    True: 'EDGE_ENABLE',
    False: 'EDGE_DISABLE',
    'mst': 'MSTP',
    'pvst': 'PVST',
    'rapid_pvst': 'RAPID_PVST',
    'point-to-point': 'P2P',
    'shared': 'SHARED',
    'loop': 'LOOP',
    'root': 'ROOT',
    'none': 'NONE'
}


class Stp(ConfigBase):
    """
    The sonic_stp class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'stp',
    ]

    def __init__(self, module):
        super(Stp, self).__init__(module)

    def get_stp_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        stp_facts = facts['ansible_network_resources'].get('stp')
        if not stp_facts:
            return []
        return stp_facts

    def execute_module(self):
        """ Execute the module
        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = []
        commands = []

        existing_stp_facts = self.get_stp_facts()
        commands, requests = self.set_config(existing_stp_facts)
        if commands and len(requests) > 0:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        changed_stp_facts = self.get_stp_facts()

        result['before'] = existing_stp_facts
        if result['changed']:
            result['after'] = changed_stp_facts

        result['warnings'] = warnings
        return result

    def set_config(self, existing_stp_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']
        have = existing_stp_facts
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
            commands, requests = self._state_overridden(want, have)
        elif state == 'deleted':
            commands, requests = self._state_deleted(want, have)
        elif state == 'merged':
            commands, requests = self._state_merged(diff, have)
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
        mod_commands = []
        replaced_config, requests = self.get_replaced_config(want, have)

        if replaced_config:
            commands.extend(update_states(replaced_config, "deleted"))
            mod_commands = want
        else:
            mod_commands = diff

        if mod_commands:
            mod_requests = self.get_modify_stp_requests(mod_commands, have)
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
        commands = []
        requests = []
        del_commands = get_diff(have, want, TEST_KEYS)
        self.remove_default_entries(del_commands)
        del_commands = remove_empties(del_commands)

        if del_commands:
            is_delete_all = True
            del_requests = self.get_delete_stp_requests(del_commands, have, is_delete_all)
            requests.extend(del_requests)
            commands.extend(update_states(have, "deleted"))
            have = {}

        if not have and want:
            mod_commands = want
            mod_requests = self.get_modify_stp_requests(mod_commands, have)

            if len(mod_requests) > 0:
                requests.extend(mod_requests)
                commands.extend(update_states(mod_commands, "overridden"))
        return commands, requests

    def _state_merged(self, diff, have):
        """ The command generator when state is merged
        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = diff
        requests = self.get_modify_stp_requests(commands, have)
        commands = remove_empties(commands)

        if commands and len(requests) > 0:
            commands = update_states(commands, "merged")
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
        want = remove_empties(want)

        if not want:
            commands = deepcopy(have)
            is_delete_all = True
        else:
            commands = deepcopy(want)

        self.remove_default_entries(commands)
        commands = remove_empties(commands)
        requests = self.get_delete_stp_requests(commands, have, is_delete_all)

        if commands and len(requests) > 0:
            commands = update_states(commands, "deleted")
        else:
            commands = []
        return commands, requests

    def get_modify_stp_requests(self, commands, have):
        requests = []

        if not commands:
            return requests

        global_request = self.get_modify_stp_global_request(commands, have)
        interfaces_request = self.get_modify_stp_interfaces_request(commands)
        mstp_requests = self.get_modify_stp_mstp_request(commands, have)
        pvst_request = self.get_modify_stp_pvst_request(commands)
        rapid_pvst_request = self.get_modify_stp_rapid_pvst_request(commands)

        if global_request:
            requests.append(global_request)
        if interfaces_request:
            requests.append(interfaces_request)
        if mstp_requests:
            requests.append(mstp_requests)
        if pvst_request:
            requests.append(pvst_request)
        if rapid_pvst_request:
            requests.append(rapid_pvst_request)

        return requests

    def get_modify_stp_global_request(self, commands, have):
        request = None

        if not commands:
            return request

        stp_global = commands.get('global', None)
        if stp_global:
            global_dict = {}
            config_dict = {}
            enabled_protocol = stp_global.get('enabled_protocol', None)
            loop_guard = stp_global.get('loop_guard', None)
            bpdu_filter = stp_global.get('bpdu_filter', None)
            disabled_vlans = stp_global.get('disabled_vlans', None)
            root_guard_timeout = stp_global.get('root_guard_timeout', None)
            portfast = stp_global.get('portfast', None)
            hello_time = stp_global.get('hello_time', None)
            max_age = stp_global.get('max_age', None)
            fwd_delay = stp_global.get('fwd_delay', None)
            bridge_priority = stp_global.get('bridge_priority', None)

            if enabled_protocol:
                config_dict['enabled-protocol'] = [stp_map[enabled_protocol]]
            if loop_guard is not None:
                config_dict['loop-guard'] = loop_guard
            if bpdu_filter is not None:
                config_dict['bpdu-filter'] = bpdu_filter
            if disabled_vlans:
                if have:
                    cfg_stp_global = have.get('global', None)
                    if cfg_stp_global:
                        cfg_disabled_vlans = cfg_stp_global.get('disabled_vlans', None)
                        if cfg_disabled_vlans:
                            disabled_vlans = self.get_vlans_diff(disabled_vlans, cfg_disabled_vlans)
                            if not disabled_vlans:
                                commands['global'].pop('disabled_vlans')
                if disabled_vlans:
                    config_dict['openconfig-spanning-tree-ext:disabled-vlans'] = self.convert_vlans_list(disabled_vlans)
            if root_guard_timeout:
                config_dict['openconfig-spanning-tree-ext:rootguard-timeout'] = root_guard_timeout
            if portfast is not None and enabled_protocol == 'pvst':
                config_dict['openconfig-spanning-tree-ext:portfast'] = portfast
            elif portfast:
                self._module.fail_json(msg='Portfast only configurable for pvst protocol.')
            if hello_time:
                config_dict['openconfig-spanning-tree-ext:hello-time'] = hello_time
            if max_age:
                config_dict['openconfig-spanning-tree-ext:max-age'] = max_age
            if fwd_delay:
                config_dict['openconfig-spanning-tree-ext:forwarding-delay'] = fwd_delay
            if bridge_priority:
                config_dict['openconfig-spanning-tree-ext:bridge-priority'] = bridge_priority
            if config_dict:
                global_dict['config'] = config_dict
                url = '%s/global' % (STP_PATH)
                payload = {'openconfig-spanning-tree:global': global_dict}
                request = {'path': url, 'method': PATCH, 'data': payload}

        return request

    def get_modify_stp_interfaces_request(self, commands):
        request = None
        interfaces = commands.get('interfaces', None)

        if interfaces:
            intf_list = []
            for intf in interfaces:
                intf_dict = {}
                config_dict = {}
                intf_name = intf.get('intf_name', None)
                edge_port = intf.get('edge_port', None)
                link_type = intf.get('link_type', None)
                guard = intf.get('guard', None)
                bpdu_guard = intf.get('bpdu_guard', None)
                bpdu_filter = intf.get('bpdu_filter', None)
                portfast = intf.get('portfast', None)
                uplink_fast = intf.get('uplink_fast', None)
                shutdown = intf.get('shutdown', None)
                cost = intf.get('cost', None)
                port_priority = intf.get('port_priority', None)
                stp_enable = intf.get('stp_enable', None)

                if intf_name:
                    config_dict['name'] = intf_name
                if edge_port is not None:
                    config_dict['edge-port'] = stp_map[edge_port]
                if link_type:
                    config_dict['link-type'] = stp_map[link_type]
                if guard:
                    config_dict['guard'] = stp_map[guard]
                if bpdu_guard is not None:
                    config_dict['bpdu-guard'] = bpdu_guard
                if bpdu_filter is not None:
                    config_dict['bpdu-filter'] = bpdu_filter
                if portfast is not None:
                    config_dict['openconfig-spanning-tree-ext:portfast'] = portfast
                if uplink_fast is not None:
                    config_dict['openconfig-spanning-tree-ext:uplink-fast'] = uplink_fast
                if shutdown is not None:
                    config_dict['openconfig-spanning-tree-ext:bpdu-guard-port-shutdown'] = shutdown
                if cost:
                    config_dict['openconfig-spanning-tree-ext:cost'] = cost
                if port_priority:
                    config_dict['openconfig-spanning-tree-ext:port-priority'] = port_priority
                if stp_enable is not None:
                    config_dict['openconfig-spanning-tree-ext:spanning-tree-enable'] = stp_enable
                if config_dict:
                    intf_dict['name'] = intf_name
                    intf_dict['config'] = config_dict
                    intf_list.append(intf_dict)
            if intf_list:
                url = '%s/interfaces' % (STP_PATH)
                payload = {'openconfig-spanning-tree:interfaces': {'interface': intf_list}}
                request = {'path': url, 'method': PATCH, 'data': payload}

        return request

    def get_modify_stp_mstp_request(self, commands, have):
        request = None

        if not commands:
            return request

        mstp = commands.get('mstp', None)

        if mstp:
            mstp_dict = {}
            config_dict = {}
            mst_name = mstp.get('mst_name', None)
            revision = mstp.get('revision', None)
            max_hop = mstp.get('max_hop', None)
            hello_time = mstp.get('hello_time', None)
            max_age = mstp.get('max_age', None)
            fwd_delay = mstp.get('fwd_delay', None)
            mst_instances = mstp.get('mst_instances', None)

            if mst_name:
                config_dict['name'] = mst_name
            if revision:
                config_dict['revision'] = revision
            if max_hop:
                config_dict['max-hop'] = max_hop
            if hello_time:
                config_dict['hello-time'] = hello_time
            if max_age:
                config_dict['max-age'] = max_age
            if fwd_delay:
                config_dict['forwarding-delay'] = fwd_delay
            if mst_instances:
                mst_inst_list = []
                pop_list = []
                for mst in mst_instances:
                    mst_inst_dict = {}
                    mst_cfg_dict = {}
                    mst_index = mst_instances.index(mst)
                    mst_id = mst.get('mst_id', None)
                    bridge_priority = mst.get('bridge_priority', None)
                    interfaces = mst.get('interfaces', None)
                    vlans = mst.get('vlans', None)

                    if mst_id:
                        mst_cfg_dict['mst-id'] = mst_id
                    if bridge_priority:
                        mst_cfg_dict['bridge-priority'] = bridge_priority
                    if interfaces:
                        intf_list = self.get_interfaces_list(interfaces)
                        if intf_list:
                            mst_inst_dict['interfaces'] = {'interface': intf_list}
                    if vlans:
                        if have:
                            cfg_mstp = have.get('mstp', None)
                            if cfg_mstp:
                                cfg_mst_instances = cfg_mstp.get('mst_instances', None)
                                if cfg_mst_instances:
                                    for cfg_mst in cfg_mst_instances:
                                        cfg_mst_id = cfg_mst.get('mst_id', None)
                                        cfg_vlans = cfg_mst.get('vlans', None)

                                        if mst_id == cfg_mst_id and cfg_vlans:
                                            vlans = self.get_vlans_diff(vlans, cfg_vlans)
                                            if not vlans:
                                                pop_list.insert(0, mst_index)
                        if vlans:
                            mst_cfg_dict['vlan'] = self.convert_vlans_list(vlans)
                    if mst_cfg_dict:
                        mst_inst_dict['mst-id'] = mst_id
                        mst_inst_dict['config'] = mst_cfg_dict
                    if mst_inst_dict:
                        mst_inst_list.append(mst_inst_dict)
                if pop_list:
                    for i in pop_list:
                        commands['mstp']['mst_instances'][i].pop('vlans')
                if mst_inst_list:
                    mstp_dict['mst-instances'] = {'mst-instance': mst_inst_list}

            if config_dict:
                mstp_dict['config'] = config_dict

            if mstp_dict:
                url = '%s/mstp' % (STP_PATH)
                payload = {'openconfig-spanning-tree:mstp': mstp_dict}
                request = {'path': url, 'method': PATCH, 'data': payload}

        return request

    def get_modify_stp_pvst_request(self, commands):
        request = None
        pvst = commands.get('pvst', None)

        if pvst:
            vlans_list = self.get_vlans_list(pvst)
            if vlans_list:
                url = '%s/openconfig-spanning-tree-ext:pvst' % (STP_PATH)
                payload = {'openconfig-spanning-tree-ext:pvst': {'vlans': vlans_list}}
                request = {'path': url, 'method': PATCH, 'data': payload}

        return request

    def get_modify_stp_rapid_pvst_request(self, commands):
        request = None
        rapid_pvst = commands.get('rapid_pvst', None)

        if rapid_pvst:
            vlans_list = self.get_vlans_list(rapid_pvst)
            if vlans_list:
                url = '%s/rapid-pvst' % (STP_PATH)
                payload = {'openconfig-spanning-tree:rapid-pvst': {'vlan': vlans_list}}
                request = {'path': url, 'method': PATCH, 'data': payload}

        return request

    def get_vlans_list(self, data):
        vlans_list = []

        for vlan in data:
            vlans_dict = {}
            config_dict = {}
            vlan_id = vlan.get('vlan_id', None)
            hello_time = vlan.get('hello_time', None)
            max_age = vlan.get('max_age', None)
            fwd_delay = vlan.get('fwd_delay', None)
            bridge_priority = vlan.get('bridge_priority', None)
            interfaces = vlan.get('interfaces', None)

            if vlan_id:
                config_dict['vlan-id'] = vlan_id
            if hello_time:
                config_dict['hello-time'] = hello_time
            if max_age:
                config_dict['max-age'] = max_age
            if fwd_delay:
                config_dict['forwarding-delay'] = fwd_delay
            if bridge_priority:
                config_dict['bridge-priority'] = bridge_priority
            if interfaces:
                intf_list = self.get_interfaces_list(interfaces)
                if intf_list:
                    vlans_dict['interfaces'] = {'interface': intf_list}
            if config_dict:
                vlans_dict['vlan-id'] = vlan_id
                vlans_dict['config'] = config_dict
            if vlans_dict:
                vlans_list.append(vlans_dict)

        return vlans_list

    def get_interfaces_list(self, interfaces):
        intf_list = []
        for intf in interfaces:
            intf_dict = {}
            intf_cfg_dict = {}
            intf_name = intf.get('intf_name', None)
            cost = intf.get('cost', None)
            port_priority = intf.get('port_priority', None)

            if intf_name:
                intf_cfg_dict['name'] = intf_name
            if cost:
                intf_cfg_dict['cost'] = cost
            if port_priority:
                intf_cfg_dict['port-priority'] = port_priority
            if intf_cfg_dict:
                intf_dict['name'] = intf_name
                intf_dict['config'] = intf_cfg_dict
                intf_list.append(intf_dict)

        return intf_list

    def get_vlans_common(self, vlans, cfg_vlans):
        """Returns the vlan ranges that are common in the want and have
        vlans lists
        """
        vlans = self.get_vlan_id_list(vlans)
        cfg_vlans = self.get_vlan_id_list(cfg_vlans)
        return self.get_vlan_range_list(list(set(vlans).intersection(set(cfg_vlans))))

    def get_vlans_diff(self, vlans, cfg_vlans):
        """Returns the vlan ranges present only in the want vlans list
        and not in the have vlans list
        """
        vlans = self.get_vlan_id_list(vlans)
        cfg_vlans = self.get_vlan_id_list(cfg_vlans)
        return self.get_vlan_range_list(list(set(vlans) - set(cfg_vlans)))

    @staticmethod
    def get_vlan_id_list(vlans):
        """Returns a list of all VLAN IDs specified in a vlans list"""
        vlan_id_list = []

        if vlans:
            for vlan_val in vlans:
                if '-' in vlan_val or '..' in vlan_val:
                    start, end = re.split(r'-|\.\.', vlan_val)
                    vlan_id_list.extend(range(int(start), int(end) + 1))
                else:
                    # Single VLAN ID
                    vlan_id_list.append(int(vlan_val))

        return vlan_id_list

    @staticmethod
    def get_vlan_range_list(vlan_id_list):
        """Returns the vlans list for a given list of VLAN IDs"""
        vlan_range_list = []

        if vlan_id_list:
            vlan_id_list.sort()
            for vlan_range in get_ranges_in_list(vlan_id_list):
                vlan_range_list.append('-'.join(map(str, (vlan_range[0], vlan_range[-1])[:len(vlan_range)])))

        return vlan_range_list

    def convert_vlans_list(self, vlans):
        converted_vlans = []

        for vlan in vlans:
            if len(vlan) == 1:
                converted_vlans.append(int(vlan))
            else:
                converted_vlans.append(vlan.replace('-', '..'))

        return converted_vlans

    def get_delete_stp_requests(self, commands, have, is_delete_all):
        requests = []

        if not commands:
            return requests

        if is_delete_all:
            requests.append(self.get_delete_all_stp_request())
        else:
            requests.extend(self.get_delete_stp_mstp_requests(commands, have))
            requests.extend(self.get_delete_stp_pvst_requests(commands, have))
            requests.extend(self.get_delete_stp_rapid_pvst_requests(commands, have))
            requests.extend(self.get_delete_stp_interfaces_requests(commands, have))
            requests.extend(self.get_delete_stp_global_requests(commands, have))

        return requests

    def get_delete_stp_global_requests(self, commands, have):
        requests = []

        stp_global = commands.get('global', None)
        if stp_global:
            enabled_protocol = stp_global.get('enabled_protocol', None)
            loop_guard = stp_global.get('loop_guard', None)
            bpdu_filter = stp_global.get('bpdu_filter', None)
            disabled_vlans = stp_global.get('disabled_vlans', None)
            root_guard_timeout = stp_global.get('root_guard_timeout', None)
            portfast = stp_global.get('portfast', None)
            hello_time = stp_global.get('hello_time', None)
            max_age = stp_global.get('max_age', None)
            fwd_delay = stp_global.get('fwd_delay', None)
            bridge_priority = stp_global.get('bridge_priority', None)

            cfg_stp_global = have.get('global', None)
            if cfg_stp_global:
                cfg_enabled_protocol = cfg_stp_global.get('enabled_protocol', None)
                cfg_loop_guard = cfg_stp_global.get('loop_guard', None)
                cfg_bpdu_filter = cfg_stp_global.get('bpdu_filter', None)
                cfg_disabled_vlans = cfg_stp_global.get('disabled_vlans', None)
                cfg_root_guard_timeout = cfg_stp_global.get('root_guard_timeout', None)
                cfg_portfast = cfg_stp_global.get('portfast', None)
                cfg_hello_time = cfg_stp_global.get('hello_time', None)
                cfg_max_age = cfg_stp_global.get('max_age', None)
                cfg_fwd_delay = cfg_stp_global.get('fwd_delay', None)
                cfg_bridge_priority = cfg_stp_global.get('bridge_priority', None)

                # Default loop_guard is false, don't delete if false
                if loop_guard and loop_guard == cfg_loop_guard:
                    requests.append(self.get_delete_stp_global_attr('loop-guard'))
                # Default bpdu_filter is false, don't delete if false
                if bpdu_filter and bpdu_filter == cfg_bpdu_filter:
                    requests.append(self.get_delete_stp_global_attr('bpdu-filter'))
                if disabled_vlans and cfg_disabled_vlans:
                    disabled_vlans_to_delete = self.get_vlans_common(disabled_vlans, cfg_disabled_vlans)
                    for i, vlan in enumerate(disabled_vlans_to_delete):
                        if '-' in vlan:
                            disabled_vlans_to_delete[i] = vlan.replace('-', '..')
                    if disabled_vlans_to_delete:
                        encoded_vlans = '%2C'.join(disabled_vlans_to_delete)
                        attr = 'openconfig-spanning-tree-ext:disabled-vlans=%s' % (encoded_vlans)
                        requests.append(self.get_delete_stp_global_attr(attr))
                    else:
                        commands['global'].pop('disabled_vlans')
                if root_guard_timeout:
                    if root_guard_timeout == cfg_root_guard_timeout:
                        requests.append(self.get_delete_stp_global_attr('openconfig-spanning-tree-ext:rootguard-timeout'))
                    else:
                        commands['global'].pop('root_guard_timeout')
                # Default portfast is false, don't delete if false
                if portfast and portfast == cfg_portfast:
                    requests.append(self.get_delete_stp_global_attr('openconfig-spanning-tree-ext:portfast'))
                if hello_time and hello_time == cfg_hello_time:
                    requests.append(self.get_delete_stp_global_attr('openconfig-spanning-tree-ext:hello-time'))
                if max_age and max_age == cfg_max_age:
                    requests.append(self.get_delete_stp_global_attr('openconfig-spanning-tree-ext:max-age'))
                if fwd_delay and fwd_delay == cfg_fwd_delay:
                    requests.append(self.get_delete_stp_global_attr('openconfig-spanning-tree-ext:forwarding-delay'))
                if bridge_priority and bridge_priority == cfg_bridge_priority:
                    requests.append(self.get_delete_stp_global_attr('openconfig-spanning-tree-ext:bridge-priority'))
                if enabled_protocol:
                    if enabled_protocol == cfg_enabled_protocol:
                        requests.append(self.get_delete_stp_global_attr('enabled-protocol'))
                    else:
                        commands['global'].pop('enabled_protocol')

        return requests

    def get_delete_stp_interfaces_requests(self, commands, have):
        requests = []

        interfaces = commands.get('interfaces', None)
        if interfaces:
            intf_list = []
            for intf in interfaces:
                intf_dict = {}
                intf_name = intf.get('intf_name', None)
                edge_port = intf.get('edge_port', None)
                link_type = intf.get('link_type', None)
                guard = intf.get('guard', None)
                bpdu_guard = intf.get('bpdu_guard', None)
                bpdu_filter = intf.get('bpdu_filter', None)
                portfast = intf.get('portfast', None)
                uplink_fast = intf.get('uplink_fast', None)
                shutdown = intf.get('shutdown', None)
                cost = intf.get('cost', None)
                port_priority = intf.get('port_priority', None)
                stp_enable = intf.get('stp_enable', None)

                cfg_interfaces = have.get('interfaces', None)
                if cfg_interfaces:
                    for cfg_intf in cfg_interfaces:
                        cfg_intf_name = cfg_intf.get('intf_name', None)
                        cfg_edge_port = cfg_intf.get('edge_port', None)
                        cfg_link_type = cfg_intf.get('link_type', None)
                        cfg_guard = cfg_intf.get('guard', None)
                        cfg_bpdu_guard = cfg_intf.get('bpdu_guard', None)
                        cfg_bpdu_filter = cfg_intf.get('bpdu_filter', None)
                        cfg_portfast = cfg_intf.get('portfast', None)
                        cfg_uplink_fast = cfg_intf.get('uplink_fast', None)
                        cfg_shutdown = cfg_intf.get('shutdown', None)
                        cfg_cost = cfg_intf.get('cost', None)
                        cfg_port_priority = cfg_intf.get('port_priority', None)
                        cfg_stp_enable = cfg_intf.get('stp_enable', None)

                        if intf_name and intf_name == cfg_intf_name:
                            # Default edge_port is false, don't delete if false
                            if edge_port and edge_port == cfg_edge_port:
                                requests.append(self.get_delete_stp_interface_attr(intf_name, 'edge-port'))
                                intf_dict.update({'intf_name': intf_name, 'edge_port': edge_port})
                            if link_type and link_type == cfg_link_type:
                                requests.append(self.get_delete_stp_interface_attr(intf_name, 'link-type'))
                                intf_dict.update({'intf_name': intf_name, 'link_type': link_type})
                            if guard and guard == cfg_guard:
                                requests.append(self.get_delete_stp_interface_attr(intf_name, 'guard'))
                                intf_dict.update({'intf_name': intf_name, 'guard': guard})
                            # Default bpdu_guard is false, don't delete if false
                            if bpdu_guard and bpdu_guard == cfg_bpdu_guard:
                                url = '%s/interfaces/interface=%s/config/bpdu-guard' % (STP_PATH, intf_name)
                                payload = {'openconfig-spanning-tree:bpdu-guard': False}
                                request = {'path': url, 'method': PATCH, 'data': payload}
                                requests.append(request)
                                intf_dict.update({'intf_name': intf_name, 'bpdu_guard': bpdu_guard})
                            # Default bpdu_filter is false, don't delete if false
                            if bpdu_filter and bpdu_filter == cfg_bpdu_filter:
                                requests.append(self.get_delete_stp_interface_attr(intf_name, 'bpdu-filter'))
                                intf_dict.update({'intf_name': intf_name, 'bpdu_filter': bpdu_filter})
                            # Default portfast is false, don't delete if false
                            if portfast and portfast == cfg_portfast:
                                requests.append(self.get_delete_stp_interface_attr(intf_name, 'openconfig-spanning-tree-ext:portfast'))
                                intf_dict.update({'intf_name': intf_name, 'portfast': portfast})
                            # Default uplink_fast is false, don't delete if false
                            if uplink_fast and uplink_fast == cfg_uplink_fast:
                                url = '%s/interfaces/interface=%s/config/openconfig-spanning-tree-ext:uplink-fast' % (STP_PATH, intf_name)
                                payload = {'openconfig-spanning-tree-ext:uplink-fast': False}
                                request = {'path': url, 'method': PATCH, 'data': payload}
                                requests.append(request)
                                intf_dict.update({'intf_name': intf_name, 'uplink_fast': uplink_fast})
                            # Default shutdown is false, don't delete if false
                            if shutdown and shutdown == cfg_shutdown:
                                url = '%s/interfaces/interface=%s/config/openconfig-spanning-tree-ext:bpdu-guard-port-shutdown' % (STP_PATH, intf_name)
                                payload = {'openconfig-spanning-tree-ext:bpdu-guard-port-shutdown': False}
                                request = {'path': url, 'method': PATCH, 'data': payload}
                                requests.append(request)
                                intf_dict.update({'intf_name': intf_name, 'shutdown': shutdown})
                            if cost and cost == cfg_cost:
                                requests.append(self.get_delete_stp_interface_attr(intf_name, 'openconfig-spanning-tree-ext:cost'))
                                intf_dict.update({'intf_name': intf_name, 'cost': cost})
                            if port_priority and port_priority == cfg_port_priority:
                                requests.append(self.get_delete_stp_interface_attr(intf_name, 'openconfig-spanning-tree-ext:port-priority'))
                                intf_dict.update({'intf_name': intf_name, 'port_priority': port_priority})
                            # Default stp_enable is true, don't delete if true
                            if stp_enable is False and stp_enable == cfg_stp_enable:
                                url = '%s/interfaces/interface=%s/config/openconfig-spanning-tree-ext:spanning-tree-enable' % (STP_PATH, intf_name)
                                payload = {'openconfig-spanning-tree-ext:spanning-tree-enable': True}
                                request = {'path': url, 'method': PATCH, 'data': payload}
                                requests.append(request)
                                intf_dict.update({'intf_name': intf_name, 'stp_enable': stp_enable})
                            if (edge_port is None and not link_type and not guard and bpdu_guard is None and bpdu_filter is None and portfast is None and
                                    uplink_fast is None and shutdown is None and not cost and not port_priority and stp_enable is None):
                                requests.append(self.get_delete_stp_interface(intf_name))
                                intf_dict.update({'intf_name': intf_name})
                            if intf_dict:
                                intf_list.append(intf_dict)
            if intf_list:
                commands['interfaces'] = intf_list
            else:
                commands.pop('interfaces')

        return requests

    def get_delete_stp_mstp_requests(self, commands, have):
        requests = []

        mstp = commands.get('mstp', None)
        if mstp:
            mst_name = mstp.get('mst_name', None)
            revision = mstp.get('revision', None)
            max_hop = mstp.get('max_hop', None)
            hello_time = mstp.get('hello_time', None)
            max_age = mstp.get('max_age', None)
            fwd_delay = mstp.get('fwd_delay', None)
            mst_instances = mstp.get('mst_instances', None)

            cfg_mstp = have.get('mstp', None)
            if cfg_mstp:
                cfg_mst_name = cfg_mstp.get('mst_name', None)
                cfg_revision = cfg_mstp.get('revision', None)
                cfg_max_hop = cfg_mstp.get('max_hop', None)
                cfg_hello_time = cfg_mstp.get('hello_time', None)
                cfg_max_age = cfg_mstp.get('max_age', None)
                cfg_fwd_delay = cfg_mstp.get('fwd_delay', None)
                cfg_mst_instances = cfg_mstp.get('mst_instances', None)

                if mst_name:
                    if mst_name == cfg_mst_name:
                        requests.append(self.get_delete_stp_mstp_cfg_attr('name'))
                    else:
                        commands['mstp'].pop('mst_name')
                if revision:
                    if revision == cfg_revision:
                        requests.append(self.get_delete_stp_mstp_cfg_attr('revision'))
                    else:
                        commands['mstp'].pop('revision')
                if max_hop:
                    if max_hop == cfg_max_hop:
                        requests.append(self.get_delete_stp_mstp_cfg_attr('max-hop'))
                    else:
                        commands['mstp'].pop('max_hop')
                if hello_time:
                    if hello_time == cfg_hello_time:
                        requests.append(self.get_delete_stp_mstp_cfg_attr('hello-time'))
                    else:
                        commands['mstp'].pop('hello_time')
                if max_age:
                    if max_age == cfg_max_age:
                        requests.append(self.get_delete_stp_mstp_cfg_attr('max-age'))
                    else:
                        commands['mstp'].pop('max_age')
                if fwd_delay:
                    if fwd_delay == cfg_fwd_delay:
                        requests.append(self.get_delete_stp_mstp_cfg_attr('forwarding-delay'))
                    else:
                        commands['mstp'].pop('fwd_delay')
                if mst_instances:
                    mst_inst_list = []
                    for mst in mst_instances:
                        mst_inst_dict = {}
                        mst_id = mst.get('mst_id', None)
                        bridge_priority = mst.get('bridge_priority', None)
                        interfaces = mst.get('interfaces', None)
                        vlans = mst.get('vlans', None)
                        if cfg_mst_instances:
                            for cfg_mst in cfg_mst_instances:
                                cfg_mst_id = cfg_mst.get('mst_id', None)
                                cfg_bridge_priority = cfg_mst.get('bridge_priority', None)
                                cfg_interfaces = cfg_mst.get('interfaces', None)
                                cfg_vlans = cfg_mst.get('vlans', None)

                                if mst_id == cfg_mst_id:
                                    if bridge_priority and bridge_priority == cfg_bridge_priority:
                                        requests.append(self.get_delete_mst_inst_cfg_attr(mst_id, 'bridge-priority'))
                                        mst_inst_dict.update({'mst_id': mst_id, 'bridge_priority': bridge_priority})
                                    if interfaces:
                                        intf_list = []
                                        for intf in interfaces:
                                            intf_dict = {}
                                            intf_name = intf.get('intf_name', None)
                                            cost = intf.get('cost', None)
                                            port_priority = intf.get('port_priority', None)

                                            if cfg_interfaces:
                                                for cfg_intf in cfg_interfaces:
                                                    cfg_intf_name = cfg_intf.get('intf_name', None)
                                                    cfg_cost = cfg_intf.get('cost', None)
                                                    cfg_port_priority = cfg_intf.get('port_priority', None)

                                                    if intf_name == cfg_intf_name:
                                                        if cost and cost == cfg_cost:
                                                            requests.append(self.get_delete_mst_intf_cfg_attr(mst_id, intf_name, 'cost'))
                                                            intf_dict.update({'intf_name': intf_name, 'cost': cost})
                                                        if port_priority and port_priority == cfg_port_priority:
                                                            requests.append(self.get_delete_mst_intf_cfg_attr(mst_id, intf_name, 'port-priority'))
                                                            intf_dict.update({'intf_name': intf_name, 'port_priority': port_priority})
                                                        if not cost and not port_priority:
                                                            requests.append(self.get_delete_mst_intf(mst_id, intf_name))
                                                            intf_dict.update({'intf_name': intf_name})
                                                        if intf_dict:
                                                            intf_list.append(intf_dict)
                                        if intf_list:
                                            mst_inst_dict.update({'mst_id': mst_id, 'interfaces': intf_list})

                                    if vlans and cfg_vlans:
                                        vlans_to_delete = self.get_vlans_common(vlans, cfg_vlans)
                                        cmd_vlans = deepcopy(vlans_to_delete)
                                        for i, vlan in enumerate(vlans_to_delete):
                                            if '-' in vlan:
                                                vlans_to_delete[i] = vlan.replace('-', '..')
                                        if vlans_to_delete:
                                            encoded_vlans = '%2C'.join(vlans_to_delete)
                                            attr = 'vlan=%s' % (encoded_vlans)
                                            requests.append(self.get_delete_mst_inst_cfg_attr(mst_id, attr))
                                            mst_inst_dict.update({'mst_id': mst_id, 'vlans': cmd_vlans})
                                    if not bridge_priority and not vlans and not interfaces:
                                        requests.append(self.get_delete_mst_inst(mst_id))
                                        mst_inst_dict.update({'mst_id': mst_id})
                                    if mst_inst_dict:
                                        mst_inst_list.append(mst_inst_dict)
                    if mst_inst_list:
                        commands['mstp']['mst_instances'] = mst_inst_list
                    else:
                        commands['mstp'].pop('mst_instances')
            if not commands['mstp']:
                commands.pop('mstp')

        return requests

    def get_delete_stp_pvst_requests(self, commands, have):
        requests = []

        pvst = commands.get('pvst', None)
        if pvst:
            vlans_list = []
            for vlan in pvst:
                vlans_dict = {}
                vlan_id = vlan.get('vlan_id', None)
                hello_time = vlan.get('hello_time', None)
                max_age = vlan.get('max_age', None)
                fwd_delay = vlan.get('fwd_delay', None)
                bridge_priority = vlan.get('bridge_priority', None)
                interfaces = vlan.get('interfaces', [])

                cfg_pvst = have.get('pvst', None)
                if cfg_pvst:
                    for cfg_vlan in cfg_pvst:
                        cfg_vlan_id = cfg_vlan.get('vlan_id', None)
                        cfg_hello_time = cfg_vlan.get('hello_time', None)
                        cfg_max_age = cfg_vlan.get('max_age', None)
                        cfg_fwd_delay = cfg_vlan.get('fwd_delay', None)
                        cfg_bridge_priority = cfg_vlan.get('bridge_priority', None)
                        cfg_interfaces = cfg_vlan.get('interfaces', [])

                        if vlan_id == cfg_vlan_id:
                            if hello_time and hello_time == cfg_hello_time:
                                requests.append(self.get_delete_pvst_vlan_cfg_attr(vlan_id, 'hello-time'))
                                vlans_dict.update({'vlan_id': vlan_id, 'hello_time': hello_time})
                            if max_age and max_age == cfg_max_age:
                                requests.append(self.get_delete_pvst_vlan_cfg_attr(vlan_id, 'max-age'))
                                vlans_dict.update({'vlan_id': vlan_id, 'max_age': max_age})
                            if fwd_delay and fwd_delay == cfg_fwd_delay:
                                requests.append(self.get_delete_pvst_vlan_cfg_attr(vlan_id, 'forwarding-delay'))
                                vlans_dict.update({'vlan_id': vlan_id, 'fwd_delay': fwd_delay})
                            if bridge_priority and bridge_priority == cfg_bridge_priority:
                                requests.append(self.get_delete_pvst_vlan_cfg_attr(vlan_id, 'bridge-priority'))
                                vlans_dict.update({'vlan_id': vlan_id, 'bridge_priority': bridge_priority})

                            if interfaces:
                                intf_list = []
                                for intf in interfaces:
                                    intf_dict = {}
                                    intf_name = intf.get('intf_name', None)
                                    cost = intf.get('cost', None)
                                    port_priority = intf.get('port_priority', None)

                                    if cfg_interfaces:
                                        for cfg_intf in cfg_interfaces:
                                            cfg_intf_name = cfg_intf.get('intf_name', None)
                                            cfg_cost = cfg_intf.get('cost', None)
                                            cfg_port_priority = cfg_intf.get('port_priority', None)

                                            if intf_name == cfg_intf_name:
                                                if cost and cost == cfg_cost:
                                                    requests.append(self.get_delete_pvst_intf_cfg_attr(vlan_id, intf_name, 'cost'))
                                                    intf_dict.update({'intf_name': intf_name, 'cost': cost})
                                                if port_priority and port_priority == cfg_port_priority:
                                                    requests.append(self.get_delete_pvst_intf_cfg_attr(vlan_id, intf_name, 'port-priority'))
                                                    intf_dict.update({'intf_name': intf_name, 'port_priority': port_priority})
                                                if not cost and not port_priority:
                                                    requests.append(self.get_delete_pvst_intf(vlan_id, intf_name))
                                                    intf_dict.update({'intf_name': intf_name})
                                                if intf_dict:
                                                    intf_list.append(intf_dict)
                                if intf_list:
                                    vlans_dict.update({'vlan_id': vlan_id, 'interfaces': intf_list})
                            if vlans_dict:
                                vlans_list.append(vlans_dict)
            if vlans_list:
                commands['pvst'] = vlans_list
            else:
                commands.pop('pvst')

        return requests

    def get_delete_stp_rapid_pvst_requests(self, commands, have):
        requests = []

        rapid_pvst = commands.get('rapid_pvst', None)
        if rapid_pvst:
            vlans_list = []
            for vlan in rapid_pvst:
                vlans_dict = {}
                vlan_id = vlan.get('vlan_id', None)
                hello_time = vlan.get('hello_time', None)
                max_age = vlan.get('max_age', None)
                fwd_delay = vlan.get('fwd_delay', None)
                bridge_priority = vlan.get('bridge_priority', None)
                interfaces = vlan.get('interfaces', [])

                cfg_rapid_pvst = have.get('rapid_pvst', None)
                if cfg_rapid_pvst:
                    for cfg_vlan in cfg_rapid_pvst:
                        cfg_vlan_id = cfg_vlan.get('vlan_id', None)
                        cfg_hello_time = cfg_vlan.get('hello_time', None)
                        cfg_max_age = cfg_vlan.get('max_age', None)
                        cfg_fwd_delay = cfg_vlan.get('fwd_delay', None)
                        cfg_bridge_priority = cfg_vlan.get('bridge_priority', None)
                        cfg_interfaces = cfg_vlan.get('interfaces', [])

                        if vlan_id == cfg_vlan_id:
                            if hello_time and hello_time == cfg_hello_time:
                                requests.append(self.get_delete_rapid_pvst_vlan_cfg_attr(vlan_id, 'hello-time'))
                                vlans_dict.update({'vlan_id': vlan_id, 'hello_time': hello_time})
                            if max_age and max_age == cfg_max_age:
                                requests.append(self.get_delete_rapid_pvst_vlan_cfg_attr(vlan_id, 'max-age'))
                                vlans_dict.update({'vlan_id': vlan_id, 'max_age': max_age})
                            if fwd_delay and fwd_delay == cfg_fwd_delay:
                                requests.append(self.get_delete_rapid_pvst_vlan_cfg_attr(vlan_id, 'forwarding-delay'))
                                vlans_dict.update({'vlan_id': vlan_id, 'fwd_delay': fwd_delay})
                            if bridge_priority and bridge_priority == cfg_bridge_priority:
                                requests.append(self.get_delete_rapid_pvst_vlan_cfg_attr(vlan_id, 'bridge-priority'))
                                vlans_dict.update({'vlan_id': vlan_id, 'bridge_priority': bridge_priority})

                            if interfaces:
                                intf_list = []
                                for intf in interfaces:
                                    intf_dict = {}
                                    intf_name = intf.get('intf_name', None)
                                    cost = intf.get('cost', None)
                                    port_priority = intf.get('port_priority', None)

                                    if cfg_interfaces:
                                        for cfg_intf in cfg_interfaces:
                                            cfg_intf_name = cfg_intf.get('intf_name', None)
                                            cfg_cost = cfg_intf.get('cost', None)
                                            cfg_port_priority = cfg_intf.get('port_priority', None)

                                            if intf_name == cfg_intf_name:
                                                if cost and cost == cfg_cost:
                                                    requests.append(self.get_delete_rapid_pvst_intf_cfg_attr(vlan_id, intf_name, 'cost'))
                                                    intf_dict.update({'intf_name': intf_name, 'cost': cost})
                                                if port_priority and port_priority == cfg_port_priority:
                                                    requests.append(self.get_delete_rapid_pvst_intf_cfg_attr(vlan_id, intf_name, 'port-priority'))
                                                    intf_dict.update({'intf_name': intf_name, 'port_priority': port_priority})
                                                if not cost and not port_priority:
                                                    requests.append(self.get_delete_rapid_pvst_intf(vlan_id, intf_name))
                                                    intf_dict.update({'intf_name': intf_name})
                                                if intf_dict:
                                                    intf_list.append(intf_dict)
                                if intf_list:
                                    vlans_dict.update({'vlan_id': vlan_id, 'interfaces': intf_list})
                            if vlans_dict:
                                vlans_list.append(vlans_dict)
            if vlans_list:
                commands['rapid_pvst'] = vlans_list
            else:
                commands.pop('rapid_pvst')

        return requests

    def get_delete_all_stp_request(self):
        request = {'path': STP_PATH, 'method': DELETE}

        return request

    def get_delete_stp_global_attr(self, attr):
        url = '%s/global/config/%s' % (STP_PATH, attr)
        request = {'path': url, 'method': DELETE}

        return request

    def get_delete_stp_interface(self, intf_name):
        url = '%s/interfaces/interface=%s' % (STP_PATH, intf_name)
        request = {'path': url, 'method': DELETE}

        return request

    def get_delete_stp_interface_attr(self, intf_name, attr):
        url = '%s/interfaces/interface=%s/config/%s' % (STP_PATH, intf_name, attr)
        request = {'path': url, 'method': DELETE}

        return request

    def get_delete_stp_mstp_cfg_attr(self, attr):
        url = '%s/mstp/config/%s' % (STP_PATH, attr)
        request = {'path': url, 'method': DELETE}

        return request

    def get_delete_mst_inst(self, mst_id):
        url = '%s/mstp/mst-instances/mst-instance=%s' % (STP_PATH, mst_id)
        request = {'path': url, 'method': DELETE}

        return request

    def get_delete_mst_inst_cfg_attr(self, mst_id, attr):
        url = '%s/mstp/mst-instances/mst-instance=%s/config/%s' % (STP_PATH, mst_id, attr)
        request = {'path': url, 'method': DELETE}

        return request

    def get_delete_mst_intf(self, mst_id, intf_name):
        url = '%s/mstp/mst-instances/mst-instance=%s/interfaces/interface=%s' % (STP_PATH, mst_id, intf_name)
        request = {'path': url, 'method': DELETE}

        return request

    def get_delete_mst_intf_cfg_attr(self, mst_id, intf_name, attr):
        url = '%s/mstp/mst-instances/mst-instance=%s/interfaces/interface=%s/config/%s' % (STP_PATH, mst_id, intf_name, attr)
        request = {'path': url, 'method': DELETE}

        return request

    def get_delete_pvst_vlan_cfg_attr(self, vlan_id, attr):
        url = '%s/openconfig-spanning-tree-ext:pvst/vlans=%s/config/%s' % (STP_PATH, vlan_id, attr)
        request = {'path': url, 'method': DELETE}

        return request

    def get_delete_pvst_intf(self, vlan_id, intf_name):
        url = '%s/openconfig-spanning-tree-ext:pvst/vlans=%s/interfaces/interface=%s' % (STP_PATH, vlan_id, intf_name)
        request = {'path': url, 'method': DELETE}

        return request

    def get_delete_pvst_intf_cfg_attr(self, vlan_id, intf_name, attr):
        url = '%s/openconfig-spanning-tree-ext:pvst/vlans=%s/interfaces/interface=%s/config/%s' % (STP_PATH, vlan_id, intf_name, attr)
        request = {'path': url, 'method': DELETE}

        return request

    def get_delete_rapid_pvst_vlan_cfg_attr(self, vlan_id, attr):
        url = '%s/rapid-pvst/vlan=%s/config/%s' % (STP_PATH, vlan_id, attr)
        request = {'path': url, 'method': DELETE}

        return request

    def get_delete_rapid_pvst_intf(self, vlan_id, intf_name):
        url = '%s/rapid-pvst/vlan=%s/interfaces/interface=%s' % (STP_PATH, vlan_id, intf_name)
        request = {'path': url, 'method': DELETE}

        return request

    def get_delete_rapid_pvst_intf_cfg_attr(self, vlan_id, intf_name, attr):
        url = '%s/rapid-pvst/vlan=%s/interfaces/interface=%s/config/%s' % (STP_PATH, vlan_id, intf_name, attr)
        request = {'path': url, 'method': DELETE}

        return request

    def remove_default_entries(self, data):
        stp_global = data.get('global', None)
        interfaces = data.get('interfaces', None)

        if stp_global:
            loop_guard = stp_global.get('loop_guard', None)
            bpdu_filter = stp_global.get('bpdu_filter', None)
            portfast = stp_global.get('portfast', None)
            hello_time = stp_global.get('hello_time', None)
            max_age = stp_global.get('max_age', None)
            fwd_delay = stp_global.get('fwd_delay', None)
            bridge_priority = stp_global.get('bridge_priority', None)

            if loop_guard is False:
                stp_global.pop('loop_guard')
            if bpdu_filter is False:
                stp_global.pop('bpdu_filter')
            if portfast is False:
                stp_global.pop('portfast')
            if hello_time == 2:
                stp_global.pop('hello_time')
            if max_age == 20:
                stp_global.pop('max_age')
            if fwd_delay == 15:
                stp_global.pop('fwd_delay')
            if bridge_priority == 32768:
                stp_global.pop('bridge_priority')
            if not stp_global:
                data.pop('global')

        if interfaces:
            for intf in interfaces:
                edge_port = intf.get('edge_port', None)
                bpdu_guard = intf.get('bpdu_guard', None)
                bpdu_filter = intf.get('bpdu_filter', None)
                portfast = intf.get('portfast', None)
                uplink_fast = intf.get('uplink_fast', None)
                shutdown = intf.get('shutdown', None)
                stp_enable = intf.get('stp_enable', None)

                if edge_port is False:
                    intf.pop('edge_port')
                if bpdu_guard is False:
                    intf.pop('bpdu_guard')
                if bpdu_filter is False:
                    intf.pop('bpdu_filter')
                if portfast is False:
                    intf.pop('portfast')
                if uplink_fast is False:
                    intf.pop('uplink_fast')
                if shutdown is False:
                    intf.pop('shutdown')
                if stp_enable:
                    intf.pop('stp_enable')

    def get_replaced_config(self, want, have):
        config_dict = {}
        requests = []
        stp_global = want.get('global', None)
        new_have = self.remove_default_entries(deepcopy(have))
        new_have = remove_empties(new_have)
        cfg_stp_global = new_have.get('global', None)

        if stp_global and cfg_stp_global and stp_global != cfg_stp_global:
            requests.append(self.get_delete_all_stp_request())
            return have, requests

        interfaces = want.get('interfaces', None)
        cfg_interfaces = have.get('interfaces', None)
        if interfaces and cfg_interfaces:
            intf_list = []
            for intf in interfaces:
                intf_name = intf.get('intf_name', None)
                for cfg_intf in cfg_interfaces:
                    cfg_intf_name = cfg_intf.get('intf_name', None)
                    if intf_name == cfg_intf_name:
                        if intf != cfg_intf:
                            intf_list.append(cfg_intf)
                            requests.append(self.get_delete_stp_interface(cfg_intf_name))
            if intf_list:
                config_dict['interfaces'] = intf_list

        mstp = want.get('mstp', None)
        cfg_mstp = have.get('mstp', None)
        if mstp and cfg_mstp:
            mst_name = mstp.get('mst_name', None)
            revision = mstp.get('revision', None)
            max_hop = mstp.get('max_hop', None)
            hello_time = mstp.get('hello_time', None)
            max_age = mstp.get('max_age', None)
            fwd_delay = mstp.get('fwd_delay', None)
            mst_instances = mstp.get('mst_instances', None)

            cfg_mst_name = cfg_mstp.get('mst_name', None)
            cfg_revision = cfg_mstp.get('revision', None)
            cfg_max_hop = cfg_mstp.get('max_hop', None)
            cfg_hello_time = cfg_mstp.get('hello_time', None)
            cfg_max_age = cfg_mstp.get('max_age', None)
            cfg_fwd_delay = cfg_mstp.get('fwd_delay', None)
            cfg_mst_instances = cfg_mstp.get('mst_instances', None)

            if ((mst_name and mst_name != cfg_mst_name) or (revision and revision != cfg_revision) or (max_hop and max_hop != cfg_max_hop) or
                    (hello_time and hello_time != cfg_hello_time) or (max_age and max_age != cfg_max_age) or
                    (fwd_delay and fwd_delay != cfg_fwd_delay)):
                config_dict['mstp'] = cfg_mstp
                requests.append({'path': '%s/mstp/config' % STP_PATH, 'method': DELETE})
                requests.append({'path': '%s/mstp/mst-instances' % STP_PATH, 'method': DELETE})
            else:
                if mst_instances and cfg_mst_instances:
                    mst_inst_list = []
                    for mst in mst_instances:
                        mst_id = mst.get('mst_id', None)
                        bridge_priority = mst.get('bridge_priority', None)
                        vlans = mst.get('vlans', None)
                        if vlans:
                            vlans.sort()
                        interfaces = mst.get('interfaces', None)
                        for cfg_mst in cfg_mst_instances:
                            cfg_mst_id = cfg_mst.get('mst_id', None)
                            cfg_bridge_priority = cfg_mst.get('bridge_priority', None)
                            cfg_vlans = cfg_mst.get('vlans', None)
                            if cfg_vlans:
                                cfg_vlans.sort()
                            cfg_interfaces = cfg_mst.get('interfaces', None)

                            if mst_id == cfg_mst_id:
                                if ((bridge_priority and bridge_priority != cfg_bridge_priority) or (vlans and vlans != cfg_vlans)):
                                    mst_inst_list.append(cfg_mst)
                                    requests.append(self.get_delete_mst_inst(cfg_mst_id))
                                else:
                                    if interfaces and cfg_interfaces:
                                        intf_list = []
                                        for intf in interfaces:
                                            intf_name = intf.get('intf_name', None)
                                            for cfg_intf in cfg_interfaces:
                                                cfg_intf_name = cfg_intf.get('intf_name', None)
                                                if intf_name == cfg_intf_name:
                                                    if intf != cfg_intf:
                                                        intf_list.append(cfg_intf)
                                                        mst_inst_list.append({'mst_id': cfg_mst_id, 'interfaces': intf_list})
                                                        requests.append(self.get_delete_mst_intf(cfg_mst_id, cfg_intf_name))
                    if mst_inst_list:
                        config_dict['mstp'] = {'mst_instances': mst_inst_list}

        pvst = want.get('pvst', None)
        cfg_pvst = have.get('pvst', None)
        if pvst and cfg_pvst:
            vlans_list, vlans_requests = self.get_replaced_vlans_list(pvst, cfg_pvst, 'pvst')
            if vlans_list:
                config_dict['pvst'] = vlans_list
                requests.extend(vlans_requests)

        rapid_pvst = want.get('rapid_pvst', None)
        cfg_rapid_pvst = have.get('rapid_pvst', None)
        if rapid_pvst and cfg_rapid_pvst:
            vlans_list, vlans_requests = self.get_replaced_vlans_list(rapid_pvst, cfg_rapid_pvst, 'rapid_pvst')
            if vlans_list:
                config_dict['rapid_pvst'] = vlans_list
                requests.extend(vlans_requests)

        return config_dict, requests

    def get_replaced_vlans_list(self, want_data, have_data, protocol):
        vlans_list = []
        requests = []
        for vlan in want_data:
            vlan_id = vlan.get('vlan_id', None)
            hello_time = vlan.get('hello_time', None)
            max_age = vlan.get('max_age', None)
            fwd_delay = vlan.get('fwd_delay', None)
            bridge_priority = vlan.get('bridge_priority', None)
            interfaces = vlan.get('interfaces', None)

            for cfg_vlan in have_data:
                cfg_vlan_id = cfg_vlan.get('vlan_id', None)
                cfg_hello_time = cfg_vlan.get('hello_time', None)
                cfg_max_age = cfg_vlan.get('max_age', None)
                cfg_fwd_delay = cfg_vlan.get('fwd_delay', None)
                cfg_bridge_priority = cfg_vlan.get('bridge_priority', None)
                cfg_interfaces = cfg_vlan.get('interfaces', None)

                if vlan_id == cfg_vlan_id:
                    if ((hello_time and hello_time != cfg_hello_time) or (max_age and max_age != cfg_max_age) or
                            (fwd_delay and fwd_delay != cfg_fwd_delay) or (bridge_priority and bridge_priority != cfg_bridge_priority)):
                        vlans_list.append(cfg_vlan)

                        if cfg_hello_time:
                            if protocol == 'pvst':
                                requests.append(self.get_delete_pvst_vlan_cfg_attr(cfg_vlan_id, 'hello-time'))
                            elif protocol == 'rapid_pvst':
                                requests.append(self.get_delete_rapid_pvst_vlan_cfg_attr(cfg_vlan_id, 'hello-time'))
                        if cfg_max_age:
                            if protocol == 'pvst':
                                requests.append(self.get_delete_pvst_vlan_cfg_attr(cfg_vlan_id, 'max-age'))
                            elif protocol == 'rapid_pvst':
                                requests.append(self.get_delete_rapid_pvst_vlan_cfg_attr(cfg_vlan_id, 'max-age'))
                        if cfg_fwd_delay:
                            if protocol == 'pvst':
                                requests.append(self.get_delete_pvst_vlan_cfg_attr(cfg_vlan_id, 'forwarding-delay'))
                            elif protocol == 'rapid_pvst':
                                requests.append(self.get_delete_rapid_pvst_vlan_cfg_attr(cfg_vlan_id, 'forwarding-delay'))
                        if cfg_bridge_priority:
                            if protocol == 'pvst':
                                requests.append(self.get_delete_pvst_vlan_cfg_attr(cfg_vlan_id, 'bridge-priority'))
                            elif protocol == 'rapid_pvst':
                                requests.append(self.get_delete_rapid_pvst_vlan_cfg_attr(cfg_vlan_id, 'bridge-priority'))
                        if cfg_interfaces:
                            for cfg_intf in cfg_interfaces:
                                cfg_intf_name = cfg_intf.get('intf_name', None)
                                if protocol == 'pvst':
                                    requests.append(self.get_delete_pvst_intf(cfg_vlan_id, cfg_intf_name))
                                elif protocol == 'rapid_pvst':
                                    requests.append(self.get_delete_rapid_pvst_intf(cfg_vlan_id, cfg_intf_name))

                    else:
                        if interfaces and cfg_interfaces:
                            intf_list = []
                            for intf in interfaces:
                                intf_name = intf.get('intf_name', None)
                                for cfg_intf in cfg_interfaces:
                                    cfg_intf_name = cfg_intf.get('intf_name', None)
                                    if intf_name == cfg_intf_name:
                                        if intf != cfg_intf:
                                            intf_list.append(cfg_intf)
                                            vlans_list.append({'vlan_id': cfg_vlan_id, 'interfaces': intf_list})
                                            if protocol == 'pvst':
                                                requests.append(self.get_delete_pvst_intf(cfg_vlan_id, cfg_intf_name))
                                            elif protocol == 'rapid_pvst':
                                                requests.append(self.get_delete_rapid_pvst_intf(cfg_vlan_id, cfg_intf_name))

        return vlans_list, requests
