#
# -*- coding: utf-8 -*-
# Copyright 2024 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_ospfv2 class
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
    remove_empties_from_list
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.formatted_diff_utils import (
    get_new_config,
    get_formatted_config_diff,
    __DELETE_CONFIG
)
from ansible.module_utils.connection import ConnectionError

PATCH = 'patch'
DELETE = 'delete'
direction = "IMPORT"
network_instance_path = '/data/openconfig-network-instance:network-instances/network-instance'
protocol_ospf_path = 'protocols/protocol=OSPF,ospfv2/ospfv2'


TEST_KEYS = [
    {'config': {'vrf_name': ''}},
    {'helper': {'neighbor_id': ''}},
    {'passive_interfaces': {'addresses': {'address': ''}, 'interface': ''}},
    {'non_passive_interfaces': {'addresses': {'address': ''}, 'interface': ''}},
    {'redistribute': {'protocol': ''}}
]

TEST_KEYS_overridden_diff = [
    {'config': {'vrf_name': '', '__delete_op': __DELETE_CONFIG}},
    {'helper': {'neighbor_id': '', '__delete_op': __DELETE_CONFIG}},
    {'passive_interfaces': {'addresses': {'address': ''}, 'interface': '', '__delete_op': __DELETE_CONFIG}},
    {'non_passive_interfaces': {'addresses': {'address': ''}, 'interface': '', '__delete_op': __DELETE_CONFIG}},
    {'redistribute': {'protocol': '', '__delete_op': __DELETE_CONFIG}}
]

TEST_KEYS_diff = [
    {'config': {'vrf_name': ''}},
    {'helper': {'neighbor_id': ''}},
    {'passive_interfaces': {'addresses': {'address': ''}, 'interface': ''}},
    {'non_passive_interfaces': {'addresses': {'address': ''}, 'interface': ''}},
    {'redistribute': {'protocol': ''}}
]

default_entries = [
    [
        {'name': 'max_metric'},
        {'name': 'external_lsa_all', 'default': 16777215}
    ],
    [
        {'name': 'max_metric'},
        {'name': 'external_lsa_connected', 'default': 16777215}
    ],
    [
        {'name': 'max_metric'},
        {'name': 'router_lsa_all', 'default': 16777215}
    ],
    [
        {'name': 'max_metric'},
        {'name': 'router_lsa_stub', 'default': 16777215}
    ]
]

protocol_map = {
    "bgp": "BGP",
    "kernel": "KERNEL",
    "connected": "DIRECTLY_CONNECTED",
    "static": "STATIC",
    "table": "DEFAULT_ROUTE"
}

redistribute_delete_path = "/global/openconfig-ospfv2-ext:route-distribution-policies/distribute-list={},{}"

ospf_attributes = {
    "abr_type": "/global/config/openconfig-ospfv2-ext:abr-type",
    "auto_cost_reference_bandwidth": "/global/config/openconfig-ospfv2-ext:auto-cost-reference-bandwidth",
    "default_information": {
        "originate": "/global/openconfig-ospfv2-ext:route-distribution-policies/distribute-list={},{}",
        "always": "/global/openconfig-ospfv2-ext:route-distribution-policies/distribute-list={},{}/config/always",
        "metric": "/global/openconfig-ospfv2-ext:route-distribution-policies/distribute-list={},{}/config/metric",
        "metric_type": "/global/openconfig-ospfv2-ext:route-distribution-policies/distribute-list={},{}/config/metric-type",
        "route_map": "/global/openconfig-ospfv2-ext:route-distribution-policies/distribute-list={},{}/config/route-map"
    },
    "default_metric": "/global/config/openconfig-ospfv2-ext:default-metric",
    "default_passive": "/global/config/openconfig-ospfv2-ext:passive-interface-default",
    "distance": {
        "all": "/global/openconfig-ospfv2-ext:distance/config/all",
        "external": "/global/openconfig-ospfv2-ext:distance/config/external",
        "inter_area": "/global/openconfig-ospfv2-ext:distance/config/inter-area",
        "intra_area": "/global/openconfig-ospfv2-ext:distance/config/intra-area"
    },
    "graceful_restart": {
        "grace_period": "/global/graceful-restart/config/openconfig-ospfv2-ext:grace-period",
        "graceful_restart_enable": "/global/graceful-restart/config/enabled",
        "helper": {
            "enable": "/global/graceful-restart/config/helper-only",
            "planned_only": "/global/graceful-restart/config/openconfig-ospfv2-ext:planned-only",
            "strict_lsa_checking": "/global/graceful-restart/config/openconfig-ospfv2-ext:strict-lsa-checking",
            "supported_grace_time": "/global/graceful-restart/config/openconfig-ospfv2-ext:supported-grace-time",
            "neighbor_id": "/global/graceful-restart/openconfig-ospfv2-ext:helpers/neighbour-id"
        }
    },
    "log_adjacency_changes": "/global/config/openconfig-ospfv2-ext:log-adjacency-state-changes",
    "max_metric": {
        "administrative": "/global/timers/max-metric/config/openconfig-ospfv2-ext:administrative",
        "external_lsa_all": "/global/timers/max-metric/config/openconfig-ospfv2-ext:external-lsa-all",
        "external_lsa_connected": "/global/timers/max-metric/config/openconfig-ospfv2-ext:external-lsa-connected",
        "router_lsa_all": "/global/timers/max-metric/config/openconfig-ospfv2-ext:router-lsa-all",
        "router_lsa_stub": "/global/timers/max-metric/config/openconfig-ospfv2-ext:router-lsa-stub",
        "on_startup": "/global/timers/max-metric/config/openconfig-ospfv2-ext:on-startup"
    },
    "maximum_paths": "/global/config/openconfig-ospfv2-ext:maximum-paths",
    "non_passive_interfaces": {
        "interface": "/global/openconfig-ospfv2-ext:passive-interfaces/passive-interface={},{},{}",
        "addresses": {
            "address": "/global/openconfig-ospfv2-ext:passive-interfaces/passive-interface={},{},{}"
        }
    },
    "opaque_lsa_capability": "/global/config/openconfig-ospfv2-ext:opaque-lsa-capability",
    "passive_interfaces": {
        "interface": "/global/openconfig-ospfv2-ext:passive-interfaces/passive-interface={},{},{}",
        "addresses": {
            "address": "/global/openconfig-ospfv2-ext:passive-interfaces/passive-interface={},{},{}"
        }
    },
    "redistribute": {
        "protocol": "/global/openconfig-ospfv2-ext:route-distribution-policies/distribute-list={},{}",
        "metric": "/global/openconfig-ospfv2-ext:route-distribution-policies/distribute-list={},{}/config/metric",
        "metric_type": "/global/openconfig-ospfv2-ext:route-distribution-policies/distribute-list={},{}/config/metric-type",
        "route_map": "/global/openconfig-ospfv2-ext:route-distribution-policies/distribute-list={},{}/config/route-map"
    },
    "refresh_timer": "/global/timers/lsa-generation/config/openconfig-ospfv2-ext:refresh-timer",
    "rfc1583_compatible": "/global/config/openconfig-ospfv2-ext:ospf-rfc1583-compatible",
    "router_id": "/global/config/router-id",
    "timers": {
        "lsa_min_arrival": "/global/timers/lsa-generation/config/openconfig-ospfv2-ext:minimum-arrival",
        "throttle_lsa_all": "/global/timers/lsa-generation/config/openconfig-ospfv2-ext:minimum-interval",
        "throttle_spf": {
            "initial_hold_time": "/global/timers/spf/config/initial-delay",
            "maximum_hold_time": "/global/timers/spf/config/maximum-delay",
            "delay_time": "/global/timers/spf/config/openconfig-ospfv2-ext:throttle-delay"
        }
    },
    "write_multiplier": "/global/config/openconfig-ospfv2-ext:write-multiplier",
}


class Ospfv2(ConfigBase):
    """
    The sonic_ospfv2 class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'ospfv2',
    ]

    def __init__(self, module):
        super(Ospfv2, self).__init__(module)

    def get_ospfv2_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        ospfv2_facts = facts['ansible_network_resources'].get('ospfv2')
        if not ospfv2_facts:
            return []
        return ospfv2_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = list()
        existing_ospfv2_facts = self.get_ospfv2_facts()
        commands, requests = self.set_config(existing_ospfv2_facts, warnings)
        if commands and len(requests) > 0:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        changed_ospfv2_facts = self.get_ospfv2_facts()

        result['before'] = existing_ospfv2_facts
        if result['changed']:
            result['after'] = changed_ospfv2_facts

        new_config = changed_ospfv2_facts
        old_config = existing_ospfv2_facts
        if self._module.check_mode:
            result.pop('after', None)
            existing_ospfv2_facts = remove_empties_from_list(existing_ospfv2_facts)
            is_overridden = False
            for cmd in commands:
                if cmd['state'] == 'overridden':
                    is_overridden = True
                    break
            if is_overridden:
                new_config = get_new_config(commands, existing_ospfv2_facts, TEST_KEYS_overridden_diff)
            else:
                new_config = get_new_config(commands, existing_ospfv2_facts, TEST_KEYS_diff)
            result['after(generated)'] = remove_empties_from_list(new_config)

        if self._module._diff:
            self.sort_lists_in_config(old_config)
            self.sort_lists_in_config(new_config)
            result['diff'] = get_formatted_config_diff(old_config, new_config, self._module._verbosity)

        result['warnings'] = warnings
        return result

    def set_config(self, existing_ospfv2_facts, warnings):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']
        have = existing_ospfv2_facts
        want = remove_empties_from_list(want)
        new_want, new_have = self.validate_and_normalize_config(want, have, warnings)
        self.sort_lists_in_config(new_want)
        self.sort_lists_in_config(new_have)
        resp = self.set_state(new_want, new_have)
        return to_list(resp)

    def validate_and_normalize_config(self, want, have, warnings):
        """ Validate the configuration
        """
        new_want = deepcopy(want)
        new_have = deepcopy(have)
        for cfg in new_have:
            self._normalize_passive_intf(cfg)
        if new_want:
            for cmd in new_want:
                have_cmd = next((cfg for cfg in new_have if cfg['vrf_name'] == cmd['vrf_name']), None)
                state = self._module.params['state']
                self._normalize_passive_intf(cmd)
                if state == 'merged':
                    if have_cmd:
                        want_default_passive = cmd.get('default_passive')
                        have_default_passive = have_cmd.get('default_passive')
                        want_non_passive = cmd.get('non_passive_interfaces', [])
                        want_passive = cmd.get('passive_interfaces', [])
                        have_passive = have_cmd.get('passive_interfaces', [])

                        if want_passive and ((want_default_passive is None and have_default_passive) or want_default_passive):
                            self._module.fail_json(msg="Passive-interface default is configured. All interfaces are passive by default")
                        if want_non_passive and ((want_default_passive is None and not have_default_passive) or want_default_passive is False):
                            self._module.fail_json(msg="Passive-interface default is not configured. All interfaces are non-passive by default")

                        if have_default_passive and want_passive:
                            warnings.append("Passive and non-passive interfaces cannot be configured together")
                            cmd.pop('passive_interfaces')
                        elif (want_non_passive or want_default_passive) and have_passive:
                            warnings.append("Passive and non-passive interfaces cannot be configured together")
                            cmd.pop('non_passive_interfaces')
                            if 'default_passive' in cmd:
                                cmd.pop('default_passive')
                elif state != "deleted":
                    want_default_passive = cmd.get('default_passive')
                    want_non_passive = cmd.get('non_passive_interfaces', [])
                    want_passive = cmd.get('passive_interfaces', [])
                    if want_default_passive and want_passive:
                        warnings.append("If Passive-interface default is configured then all interfaces are passive by default")
                        cmd.pop('passive_interfaces')
                    if want_default_passive is not None and not want_default_passive and want_non_passive:
                        warnings.append("If Passive-interface default is not configured then all interfaces are non-passive by default")
                        cmd.pop('non_passive_interfaces')
                    if want_default_passive is None:
                        if want_non_passive:
                            cmd['default_passive'] = True
                        elif want_passive:
                            cmd['default_passive'] = False
        return new_want, new_have

    def set_state(self, want, have):
        """ Select the appropriate function based on the state provided

        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands, requests = [], []
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
        self.sort_lists_in_config(want)
        self.sort_lists_in_config(have)
        add_config, del_config = self._get_replaced_config(want, have)
        if del_config:
            del_requests = self.get_delete_ospfv2_requests(del_config, have, True)
            if len(del_requests) > 0:
                requests.extend(del_requests)
                commands.extend(update_states(del_config, "deleted"))
        if add_config:
            mod_requests = self.get_create_ospfv2_requests(add_config)
            if len(mod_requests) > 0:
                requests.extend(mod_requests)
                commands.extend(update_states(add_config, "replaced"))
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
        diff = get_diff(want, have, TEST_KEYS)
        diff2 = get_diff(have, want, TEST_KEYS)
        for default_entry in default_entries:
            remove_matching_defaults(diff, default_entry)
            remove_matching_defaults(diff2, default_entry)
        if diff or diff2:
            del_requests = self.get_delete_ospfv2_requests(have, have, True)
            if len(del_requests) > 0:
                requests.extend(del_requests)
                commands.extend(update_states(have, "deleted"))
            mod_requests = self.get_create_ospfv2_requests(want)
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
        commands = get_diff(want, have, TEST_KEYS)
        requests = self.get_create_ospfv2_requests(commands)

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
        commands, requests = [], []
        is_delete_all = False

        if not want:
            commands = have
            is_delete_all = True
        else:
            self.sort_lists_in_config(want)
            self.sort_lists_in_config(have)
            new_want = deepcopy(want)
            new_have = deepcopy(have)
            for default_entry in default_entries:
                remove_matching_defaults(new_have, default_entry)

            new_have = remove_empties_from_list(new_have)
            commands = new_want
        requests = self.get_delete_ospfv2_requests(commands, have, is_delete_all)

        if commands and len(requests) > 0:
            commands = update_states(commands, "deleted")
        else:
            commands = []
        return commands, requests

    def _get_replaced_config(self, want, have):
        add_config, del_config = [], []
        for conf in want:
            is_change = False
            vrf_name = conf.get('vrf_name')
            have_conf = next((cfg for cfg in have if cfg['vrf_name'] == vrf_name), None)
            if not have_conf:
                add_config.append(conf)
            else:
                for attr in ospf_attributes:
                    if attr in have_conf:
                        if attr not in conf:
                            is_change = True
                            break
                        else:
                            if attr not in ["vrf_name", "redistribute", "passive_interfaces", "non_passive_interfaces"]:
                                if have_conf[attr] != conf[attr]:
                                    is_change = True
                                    break
                            elif attr == "redistribute":
                                for redis_list in conf.get(attr, []):
                                    protocol = redis_list.get('protocol')
                                    have_redis = next((redis for redis in have_conf.get(attr, []) if redis['protocol'] == protocol), None)
                                    if have_redis:
                                        if redis_list != have_redis:
                                            is_change = True
                                            break
                                    else:
                                        is_change = True
                                        break
                            elif attr == "passive_interfaces" or attr == "non_passive_interfaces":
                                for interface in conf.get(attr, []):
                                    interface_name = interface.get('interface')
                                    have_interface = next((intf for intf in have_conf.get(attr, []) if intf['interface'] == interface_name), None)
                                    if have_interface:
                                        if interface != have_interface:
                                            is_change = True
                                            break
                                    else:
                                        is_change = True
                                        break
                    elif attr in conf:
                        is_change = True
                        break
            if is_change:
                add_config.append(conf)
                del_config.append(have_conf)
        return add_config, del_config

    def get_create_ospfv2_requests(self, commands):
        requests = []

        for cmd in commands:
            vrf_name = cmd.get('vrf_name')
            sub_commands = deepcopy(cmd)
            sub_commands.pop('vrf_name')
            ospf_path = self.get_ospf_uri(vrf_name)
            payload = {}
            self._get_create_request_path_from_dict(sub_commands, ospf_attributes, payload)
            if payload:
                requests.append({'path': ospf_path, 'method': PATCH, 'data': {'openconfig-network-instance:ospfv2': payload}})
        return requests

    def _get_create_request_path_from_dict(self, command, ospf_dict, payload):
        for attr in ospf_dict:
            if attr in command and command[attr] is not None:
                if not isinstance(ospf_dict[attr], dict):
                    path = ospf_dict[attr]
                    request_body = path.split("/")
                    last_body = request_body[-1]
                    if "=" in last_body:
                        last_body = last_body.split("=")[0]
                    payload_iter = payload
                    for body in request_body[1:-1]:
                        payload_iter.setdefault(body, {})
                        payload_iter = payload_iter[body]
                    if attr == 'neighbor_id':
                        for ip in command['neighbor_id']:
                            payload_iter.setdefault('helper', [])
                            payload_iter['helper'].append({"neighbour-id": ip, "config": {"neighbour-id": ip}})
                    elif attr == 'abr_type':
                        payload_iter[last_body] = "openconfig-ospfv2-ext:" + command[attr].upper()
                    elif attr == "log_adjacency_changes":
                        payload_iter[last_body] = "openconfig-ospfv2-ext:" + command[attr].upper()
                    else:
                        payload_iter[last_body] = command[attr]
                elif attr == "default_information" or attr == "redistribute":
                    self._get_create_redistribute_request(command[attr], ospf_dict[attr], attr, payload)
                elif attr == "passive_interfaces" or attr == "non_passive_interfaces":
                    self._get_create_passive_interfaces_request(command[attr], attr, payload)
                else:
                    self._get_create_request_path_from_dict(command[attr], ospf_dict[attr], payload)

    def _get_create_redistribute_request(self, command, ospf_dict, attr, payload):
        protocol = "DEFAULT_ROUTE"
        path = ospf_attributes['default_information']['originate']
        request_body = path.split("/")
        payload_iter = payload
        for body in request_body[1:-1]:
            payload_iter.setdefault(body, {})
            payload_iter = payload_iter[body]
        payload_iter.setdefault('distribute-list', [])
        if attr == "default_information":
            if "originate" in command:
                if len(command) == 1:
                    payload_iter['distribute-list'].append({"protocol": protocol, "direction": direction})
                else:
                    distribute_payload = {"protocol": protocol, "direction": direction}
                    for item in command:
                        if item != "originate" and item != "metric_type":
                            config_type = ospf_dict[item].split("/")[-1]
                            distribute_payload.setdefault('config', {})
                            distribute_payload['config'][config_type] = command[item]
                        elif item == "metric_type":
                            distribute_payload.setdefault('config', {})
                            metric_type = "TYPE_1" if command[item] == 1 else "TYPE_2"
                            distribute_payload['config']['openconfig-ospfv2-ext:metric-type'] = metric_type
                    payload_iter['distribute-list'].append(distribute_payload)
        else:
            for redistribute_list in command:
                if "protocol" in redistribute_list:
                    protocol = protocol_map[redistribute_list['protocol']]
                    if len(redistribute_list) == 1:
                        payload_iter['distribute-list'].append({"protocol": protocol, "direction": direction})
                    else:
                        distribute_payload = {"protocol": protocol, "direction": direction}
                        for item in redistribute_list:
                            if item != "protocol" and item != "metric_type":
                                config_type = ospf_dict[item].split("/")[-1]
                                distribute_payload.setdefault('config', {})
                                distribute_payload['config'][config_type] = redistribute_list[item]
                            elif item == "metric_type":
                                distribute_payload.setdefault('config', {})
                                metric_type = "TYPE_1" if redistribute_list[item] == 1 else "TYPE_2"
                                distribute_payload['config']['openconfig-ospfv2-ext:metric-type'] = metric_type
                        payload_iter['distribute-list'].append(distribute_payload)

    def _get_create_passive_interfaces_request(self, command, attr, payload):
        non_passive = True if attr == "non_passive_interfaces" else False
        body = {"openconfig-ospfv2-ext:non-passive": non_passive}
        default_address = "0.0.0.0"
        for intf in command:
            if "interface" in intf:
                parent_intf, sub_intf = intf['interface'].split(".") if "." in intf['interface'] else (intf['interface'], 0)
                payload.setdefault("global", {})
                payload['global'].setdefault("openconfig-ospfv2-ext:passive-interfaces", {})
                payload['global']['openconfig-ospfv2-ext:passive-interfaces'].setdefault('passive-interface', [])
                for address in intf.get('addresses', []):
                    if address.get('address'):
                        request_body = {
                            'name': parent_intf,
                            'subinterface': sub_intf,
                            'address': address.get('address'),
                            'config': body
                        }
                        payload['global']['openconfig-ospfv2-ext:passive-interfaces']['passive-interface'].append(request_body)

                if not payload['global']['openconfig-ospfv2-ext:passive-interfaces']['passive-interface']:
                    intf['addresses'] = [default_address]
                    payload['global']['openconfig-ospfv2-ext:passive-interfaces']['passive-interface'].append(
                        {
                            'name': parent_intf,
                            'subinterface': sub_intf,
                            'address': default_address,
                            'config': body
                        }
                    )

    def get_delete_ospfv2_requests(self, commands, have, is_delete_all):
        requests = []
        for cmd in commands:
            vrf_name = cmd.get('vrf_name')
            sub_commands = deepcopy(cmd)
            sub_commands.pop('vrf_name')
            url = self.get_ospf_uri(vrf_name)
            if is_delete_all:
                requests.append({'path': url + "/global", 'method': DELETE})
            elif sub_commands == {}:
                have_cmd = next((cfg for cfg in have if cfg['vrf_name'] == vrf_name), None)
                if have_cmd:
                    requests.append({'path': url + "/global", 'method': DELETE})
            else:
                have_cmd = next((cfg for cfg in have if cfg['vrf_name'] == vrf_name), None)
                if have_cmd:
                    requests.extend(self._get_delete_request_path_from_dict(sub_commands, have_cmd, ospf_attributes, url))
        return requests

    def _get_delete_request_path_from_dict(self, command, have, ospf_dict, ospf_path):
        requests = []
        for attr in ospf_dict:
            if attr in command and attr in have:
                if not isinstance(ospf_dict[attr], dict):
                    if attr == "neighbor_id":
                        for ip in command['neighbor_id']:
                            if ip in have['neighbor_id']:
                                url = '%s%s=%s' % (ospf_path, ospf_dict['neighbor_id'], ip)
                                requests.append({'path': url, 'method': DELETE})
                    elif command.get(attr) == have.get(attr):
                        url = '%s%s' % (ospf_path, ospf_dict[attr])
                        requests.append({'path': url, 'method': DELETE})
                elif attr == "default_information" or attr == "redistribute":
                    requests.extend(self._get_delete_redistribute_request(command[attr], have[attr], ospf_dict[attr], attr, ospf_path))
                elif attr == "passive_interfaces" or attr == "non_passive_interfaces":
                    requests.extend(self._get_delete_passive_interfaces_request(command[attr], have[attr], ospf_dict[attr], attr, ospf_path))
                else:
                    requests.extend(self._get_delete_request_path_from_dict(command[attr], have[attr], ospf_dict[attr], ospf_path))
        return requests

    def _get_delete_redistribute_request(self, command, have, ospf_dict, attr, ospf_path):
        requests = []
        protocol = "DEFAULT_ROUTE"
        if attr == "default_information":
            if "originate" in command and "originate" in have:
                if len(command) == 1:
                    url = '%s%s' % (ospf_path, ospf_dict['originate'])
                    requests.append({'path': url.format(protocol, direction), 'method': DELETE})
                else:
                    for item in command:
                        if item != "originate" and (item in have and item in command):
                            url = '%s%s' % (ospf_path, ospf_dict[item])
                            requests.append({'path': url.format(protocol, direction), 'method': DELETE})
        else:
            for redistribute_list in command:
                if "protocol" in redistribute_list:
                    have_redistribute_list = next((cfg for cfg in have if cfg['protocol'] == redistribute_list['protocol']), None)
                    if have_redistribute_list:
                        protocol = protocol_map[redistribute_list['protocol']]
                        if len(redistribute_list) == 1:
                            url = '%s%s' % (ospf_path, ospf_dict['protocol'])
                            requests.append({'path': url.format(protocol, direction), 'method': DELETE})
                        else:
                            for item in redistribute_list:
                                if item != "protocol" and (item in have and have_redistribute_list in redistribute_list):
                                    url = '%s%s' % (ospf_path, ospf_dict[item])
                                    requests.append({'path': url.format(protocol, direction), 'method': DELETE})
        return requests

    def _get_delete_passive_interfaces_request(self, command, have, ospf_dict, attr, ospf_path):
        non_passive = True if attr == "non_passive_interfaces" else False
        body = {"openconfig-ospfv2-ext:non-passive": False}
        request_body = {
            "openconfig-network-instance:ospfv2": {
                "global": {
                    "openconfig-ospfv2-ext:passive-interfaces": {
                        "passive-interface": []
                    }
                }
            }
        }
        passive_intf = request_body['openconfig-network-instance:ospfv2']['global']['openconfig-ospfv2-ext:passive-interfaces']['passive-interface']
        requests = []
        for intf in command:
            if "interface" in intf:
                have_intf = next((cfg for cfg in have if cfg['interface'] == intf['interface']), None)
                if have_intf:
                    intf_name = intf['interface']
                    parent_intf, sub_intf = intf_name.split(".") if "." in intf_name else (intf_name, 0)
                    if len(intf) == 1:
                        for address in have_intf['addresses']:
                            if address.get('address'):
                                if non_passive:
                                    passive_intf.append({
                                        'name': parent_intf,
                                        'subinterface': sub_intf,
                                        'address': address['address'],
                                        'config': body
                                    })
                                else:
                                    url = '%s%s' % (ospf_path, ospf_dict['interface'])
                                    requests.append({'path': url.format(parent_intf.replace('/', '%2f'), sub_intf, address['address']), 'method': DELETE})
                    else:
                        for address in intf['addresses']:
                            if address.get('address'):
                                have_address = next((cfg for cfg in have_intf['addresses'] if cfg['address'] == address['address']), None)
                                if have_address:
                                    if non_passive:
                                        passive_intf.append({
                                            'name': parent_intf,
                                            'subinterface': sub_intf,
                                            'address': address['address'],
                                            'config': body
                                        })
                                    else:
                                        url = '%s%s' % (ospf_path, ospf_dict['interface'])
                                        url = url.format(parent_intf.replace('/', '%2f'), sub_intf, have_address['address'])
                                        requests.append({'path': url, 'method': DELETE})
        if passive_intf:
            requests.append({'path': ospf_path, 'method': PATCH, 'data': request_body})
        return requests

    def sort_lists_in_config(self, config):
        if config:
            config.sort(key=lambda x: x['vrf_name'])
            for cfg in config:
                if cfg.get('passive_interfaces', None):
                    cfg['passive_interfaces'].sort(key=lambda x: x['interface'])
                    for intf in cfg['passive_interfaces']:
                        intf_addresses = intf.get('addresses', [])
                        if intf_addresses:
                            intf_addresses.sort(key=lambda x: x['address'])
                if cfg.get('non_passive_interfaces', None):
                    cfg['non_passive_interfaces'].sort(key=lambda x: x['interface'])
                    for intf in cfg['non_passive_interfaces']:
                        intf_addresses = intf.get('addresses', [])
                        if intf_addresses:
                            intf_addresses.sort(key=lambda x: x['address'])
                if cfg.get('redistribute', None):
                    cfg['redistribute'].sort(key=lambda x: x['protocol'])
                if cfg.get('graceful_restart', None):
                    if cfg['graceful_restart'].get('helper', None):
                        if cfg['graceful_restart']['helper'].get('neighbor_id', []):
                            cfg['graceful_restart']['helper']['neighbor_id'].sort()

    def get_ospf_uri(self, vrf_name):
        return '%s=%s/%s' % (network_instance_path, vrf_name, protocol_ospf_path)

    def _normalize_passive_intf(self, cmd):
        if "non_passive_interfaces" in cmd:
            for intf in cmd['non_passive_interfaces']:
                intf['interface'] = intf['interface'].replace(" ", "")
                if not intf.get('addresses', []):
                    intf['addresses'] = [{"address": "0.0.0.0"}]

        elif "passive_interfaces" in cmd:
            for intf in cmd['passive_interfaces']:
                intf['interface'] = intf['interface'].replace(" ", "")
                if not intf.get('addresses', []):
                    intf['addresses'] = [{"address": "0.0.0.0"}]
