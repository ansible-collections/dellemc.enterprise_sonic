#
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_system class
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
    remove_empties,
    to_list,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import Facts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    update_states,
    get_diff,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.formatted_diff_utils import (
    get_new_config,
    get_formatted_config_diff
)

PATCH = 'patch'
DELETE = 'delete'


def __derive_system_config_delete_op(key_set, command, exist_conf):
    new_conf = exist_conf

    if 'hostname' in command:
        new_conf['hostname'] = 'sonic'
    if 'interface_naming' in command:
        new_conf['interface_naming'] = 'native'
    if 'anycast_address' in command and 'anycast_address' in new_conf:
        if 'ipv4' in command['anycast_address']:
            new_conf['anycast_address']['ipv4'] = True
        if 'ipv6' in command['anycast_address']:
            new_conf['anycast_address']['ipv6'] = True
        if 'mac_address' in command['anycast_address']:
            new_conf['anycast_address']['mac_address'] = None
    if 'auto_breakout' in command:
        new_conf['auto_breakout'] = 'DISABLE'
    if 'load_share_hash_algo' in command:
        new_conf['load_share_hash_algo'] = None
    if 'audit_rules' in command:
        new_conf['audit_rules'] = 'NONE'

    return True, new_conf


TEST_KEYS_formatted_diff = [
    {'config': {'__delete_op': __derive_system_config_delete_op}},
]


class System(ConfigBase):
    """
    The sonic_system class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'system',
    ]

    def __init__(self, module):
        super(System, self).__init__(module)

    def get_system_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        system_facts = facts['ansible_network_resources'].get('system')
        if not system_facts:
            return []
        return system_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = list()
        commands = list()

        existing_system_facts = self.get_system_facts()
        commands, requests = self.set_config(existing_system_facts)
        if commands and len(requests) > 0:
            if not self._module.check_mode:
                self.edit_config(requests)
            result['changed'] = True
        result['commands'] = commands

        changed_system_facts = self.get_system_facts()

        result['before'] = existing_system_facts
        if result['changed']:
            result['after'] = changed_system_facts

        new_config = changed_system_facts
        if self._module.check_mode:
            result.pop('after', None)
            new_config = get_new_config(commands, existing_system_facts,
                                        TEST_KEYS_formatted_diff)
            result['after(generated)'] = new_config

        if self._module._diff:
            result['diff'] = get_formatted_config_diff(existing_system_facts,
                                                       new_config,
                                                       self._module._verbosity)
        result['warnings'] = warnings
        return result

    def edit_config(self, requests):
        try:
            response = edit_config(self._module, to_request(self._module, requests))
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)

    def set_config(self, existing_system_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']
        have = existing_system_facts
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
        if state == 'deleted':
            commands = self._state_deleted(want, have)
        elif state == 'merged':
            diff = get_diff(want, have)
            commands = self._state_merged(want, have, diff)
        elif state in ('overridden', 'replaced'):
            commands = self._state_replaced_overridden(want, have)

        return commands

    def _state_merged(self, want, have, diff):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        requests = []
        commands = []
        if diff:
            requests = self.get_create_system_request(want, diff)
            if len(requests) > 0:
                commands = update_states(diff, "merged")

        return commands, requests

    def _state_deleted(self, want, have):
        """ The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        commands = []
        requests = []
        new_have = self.remove_default_entries(have)
        if not want:
            if have:
                requests = self.get_delete_all_system_request(new_have)
                if len(requests) > 0:
                    commands = update_states(have, "deleted")
        else:
            want = utils.remove_empties(want)
            d_diff = get_diff(want, new_have, is_skeleton=True)
            diff_want = get_diff(want, d_diff, is_skeleton=True)
            if diff_want:
                requests = self.get_delete_all_system_request(diff_want)
                if len(requests) > 0:
                    commands = update_states(diff_want, "deleted")

        return commands, requests

    def _state_replaced_overridden(self, want, have):
        """ The command generator when state is replaced or overridden

        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :param diff: the difference between want and have
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        add_command = {}
        del_command = {}

        requests = []
        del_requests = []

        default_values = {
            'hostname': 'sonic',
            'interface_naming': 'native',
            'anycast_address': {
                'ipv4': True,
                'ipv6': True
            },
            'auto_breakout': 'DISABLE'
        }
        del_request_method = {
            'hostname': self.get_hostname_delete_request,
            'interface_naming': self.get_intfname_delete_request,
            'auto_breakout': self.get_auto_breakout_delete_request,
            'load_share_hash_algo': self.get_load_share_hash_algo_delete_request,
            'audit_rules': self.get_audit_rules_delete_request
        }

        new_have = remove_empties(have)
        new_want = remove_empties(want)

        for option in ('hostname', 'interface_naming', 'auto_breakout', 'load_share_hash_algo', 'audit_rules'):
            if option in new_want:
                if new_want[option] != new_have.get(option):
                    add_command[option] = new_want[option]
            else:
                if option in new_have and new_have[option] != default_values.get(option):
                    del_command[option] = new_have[option]
                    del_requests.append(del_request_method[option]())

        want_anycast = new_want.get('anycast_address', {})
        have_anycast = new_have.get('anycast_address', {})
        if want_anycast:
            for option in ('ipv4', 'ipv6', 'mac_address'):
                if option in want_anycast:
                    if want_anycast[option] != have_anycast.get(option):
                        add_command.setdefault('anycast_address', {})
                        add_command['anycast_address'][option] = want_anycast[option]
                else:
                    if option in have_anycast and have_anycast[option] != default_values['anycast_address'].get(option):
                        del_command.setdefault('anycast_address', {})
                        del_command['anycast_address'][option] = have_anycast[option]

            if del_command.get('anycast_address'):
                del_requests.extend(self.get_anycast_delete_request(del_command['anycast_address']))
        else:
            if have_anycast:
                del_command['anycast_address'] = have_anycast
                del_requests.extend(self.get_anycast_delete_request(del_command['anycast_address']))

        if del_command:
            commands = update_states(del_command, 'deleted')
            requests.extend(del_requests)

        if add_command:
            commands.extend(update_states(add_command, self._module.params['state']))
            requests.extend(self.get_create_system_request(new_want, add_command))

        return commands, requests

    def get_create_system_request(self, want, commands):
        requests = []
        host_path = 'data/openconfig-system:system/config'
        method = PATCH
        hostname_payload = self.build_create_hostname_payload(commands)
        if hostname_payload:
            request = {'path': host_path, 'method': method, 'data': hostname_payload}
            requests.append(request)
        name_path = 'data/sonic-device-metadata:sonic-device-metadata/DEVICE_METADATA/DEVICE_METADATA_LIST=localhost/intf_naming_mode'
        name_payload = self.build_create_name_payload(commands)
        if name_payload:
            request = {'path': name_path, 'method': method, 'data': name_payload}
            requests.append(request)
        anycast_path = 'data/sonic-sag:sonic-sag/SAG_GLOBAL/SAG_GLOBAL_LIST/'
        anycast_payload = self.build_create_anycast_payload(commands)
        if anycast_payload:
            request = {'path': anycast_path, 'method': method, 'data': anycast_payload}
            requests.append(request)
        auto_breakout_path = 'data/sonic-device-metadata:sonic-device-metadata/DEVICE_METADATA/DEVICE_METADATA_LIST=localhost/auto-breakout'
        auto_breakout_payload = self.build_create_auto_breakout_payload(commands)
        if auto_breakout_payload:
            request = {'path': auto_breakout_path, 'method': method, 'data': auto_breakout_payload}
            requests.append(request)
        load_share_hash_algo_path = "data/openconfig-loadshare-mode-ext:loadshare/hash-algorithm/config"
        load_share_hash_algo_payload = self.build_create_load_share_hash_algo_payload(commands)
        if load_share_hash_algo_payload:
            request = {'path': load_share_hash_algo_path, 'method': method, 'data': load_share_hash_algo_payload}
            requests.append(request)
        audit_rules_path = 'data/openconfig-system:system/openconfig-system-ext:auditd-system/config/audit-rules'
        audit_rules_payload = self.build_create_audit_rules_payload(commands)
        if audit_rules_payload:
            request = {'path': audit_rules_path, 'method': method, 'data': audit_rules_payload}
            requests.append(request)
        return requests

    def build_create_hostname_payload(self, commands):
        payload = {}
        if "hostname" in commands and commands["hostname"]:
            payload = {"openconfig-system:config": {}}
            payload['openconfig-system:config'].update({"hostname": commands["hostname"]})
        return payload

    def build_create_name_payload(self, commands):
        payload = {}
        if "interface_naming" in commands and commands["interface_naming"]:
            if commands["interface_naming"] == 'standard_extended':
                payload.update({'sonic-device-metadata:intf_naming_mode': "standard-ext"})
            else:
                payload.update({'sonic-device-metadata:intf_naming_mode': commands["interface_naming"]})
        return payload

    def build_create_anycast_payload(self, commands):
        payload = {}
        if "anycast_address" in commands and commands["anycast_address"]:
            payload = {"sonic-sag:SAG_GLOBAL_LIST": []}
            temp = {}
            if "ipv4" in commands["anycast_address"] and commands["anycast_address"]["ipv4"]:
                temp.update({'IPv4': "enable"})
            if "ipv4" in commands["anycast_address"] and not commands["anycast_address"]["ipv4"]:
                temp.update({'IPv4': "disable"})
            if "ipv6" in commands["anycast_address"] and commands["anycast_address"]["ipv6"]:
                temp.update({'IPv6': "enable"})
            if "ipv6" in commands["anycast_address"] and not commands["anycast_address"]["ipv6"]:
                temp.update({'IPv6': "disable"})
            if "mac_address" in commands["anycast_address"] and commands["anycast_address"]["mac_address"]:
                temp.update({'gwmac': commands["anycast_address"]["mac_address"]})
            if temp:
                temp.update({"table_distinguisher": "IP"})
                payload["sonic-sag:SAG_GLOBAL_LIST"].append(temp)
        return payload

    def build_create_auto_breakout_payload(self, commands):
        payload = {}
        if "auto_breakout" in commands and commands["auto_breakout"]:
            payload.update({'sonic-device-metadata:auto-breakout': commands["auto_breakout"]})
        return payload

    def build_create_load_share_hash_algo_payload(self, commands):
        payload = {}
        if "load_share_hash_algo" in commands and commands["load_share_hash_algo"]:
            payload = {"openconfig-loadshare-mode-ext:config": {}}
            payload['openconfig-loadshare-mode-ext:config'].update({"algorithm": commands["load_share_hash_algo"]})
        return payload

    def build_create_audit_rules_payload(self, commands):
        payload = {}
        if "audit_rules" in commands and commands["audit_rules"]:
            payload.update({'openconfig-system-ext:audit-rules': commands["audit_rules"]})
        return payload

    def remove_default_entries(self, data):
        new_data = {}
        if not data:
            return new_data
        else:
            hostname = data.get('hostname', None)
            if hostname != "sonic":
                new_data["hostname"] = hostname
            intf_name = data.get('interface_naming', None)
            if intf_name != "native":
                new_data["interface_naming"] = intf_name
            new_anycast = {}
            anycast = data.get('anycast_address', None)
            if anycast:
                ipv4 = anycast.get("ipv4", None)
                if ipv4 is not True:
                    new_anycast["ipv4"] = ipv4
                ipv6 = anycast.get("ipv6", None)
                if ipv6 is not True:
                    new_anycast["ipv6"] = ipv6
                mac = anycast.get("mac_address", None)
                if mac is not None:
                    new_anycast["mac_address"] = mac
            new_data["anycast_address"] = new_anycast
            auto_breakout_mode = data.get('auto_breakout', None)
            if auto_breakout_mode != "DISABLE":
                new_data["auto_breakout"] = auto_breakout_mode
            load_share_hash_algo = data.get('load_share_hash_algo', None)
            if load_share_hash_algo is not None:
                new_data["load_share_hash_algo"] = load_share_hash_algo
            audit_rules = data.get('audit_rules', None)
            if audit_rules is not None and audit_rules != "NONE":
                new_data["audit_rules"] = audit_rules
        return new_data

    def get_delete_all_system_request(self, have):
        requests = []
        if "hostname" in have:
            request = self.get_hostname_delete_request()
            requests.append(request)
        if "interface_naming" in have:
            request = self.get_intfname_delete_request()
            requests.append(request)
        if "anycast_address" in have:
            request = self.get_anycast_delete_request(have["anycast_address"])
            requests.extend(request)
        if "auto_breakout" in have:
            request = self.get_auto_breakout_delete_request()
            requests.append(request)
        if "load_share_hash_algo" in have:
            request = self.get_load_share_hash_algo_delete_request()
            requests.append(request)
        if "audit_rules" in have:
            request = self.get_audit_rules_delete_request()
            requests.append(request)

        return requests

    def get_hostname_delete_request(self):
        path = 'data/openconfig-system:system/config'
        method = PATCH
        payload = {"openconfig-system:config": {}}
        payload['openconfig-system:config'].update({"hostname": "sonic"})
        request = {'path': path, 'method': method, 'data': payload}
        return request

    def get_intfname_delete_request(self):
        path = 'data/sonic-device-metadata:sonic-device-metadata/DEVICE_METADATA/DEVICE_METADATA_LIST=localhost/intf_naming_mode'
        method = DELETE
        request = {'path': path, 'method': method}
        return request

    def get_anycast_delete_request(self, anycast):
        requests = []
        if "ipv4" in anycast:
            path = 'data/sonic-sag:sonic-sag/SAG_GLOBAL/SAG_GLOBAL_LIST=IP/IPv4'
            method = DELETE
            request = {'path': path, 'method': method}
            requests.append(request)
        if "ipv6" in anycast:
            path = 'data/sonic-sag:sonic-sag/SAG_GLOBAL/SAG_GLOBAL_LIST=IP/IPv6'
            method = DELETE
            request = {'path': path, 'method': method}
            requests.append(request)
        if "mac_address" in anycast:
            path = 'data/sonic-sag:sonic-sag/SAG_GLOBAL/SAG_GLOBAL_LIST=IP/gwmac'
            method = DELETE
            request = {'path': path, 'method': method}
            requests.append(request)
        return requests

    def get_auto_breakout_delete_request(self):
        path = 'data/sonic-device-metadata:sonic-device-metadata/DEVICE_METADATA/DEVICE_METADATA_LIST=localhost/auto-breakout'
        method = DELETE
        request = {'path': path, 'method': method}
        return request

    def get_load_share_hash_algo_delete_request(self):
        path = 'data/openconfig-loadshare-mode-ext:loadshare/hash-algorithm/config/algorithm'
        method = DELETE
        request = {'path': path, 'method': method}
        return request

    def get_audit_rules_delete_request(self):
        path = 'data/openconfig-system:system/openconfig-system-ext:auditd-system/config/audit-rules'
        method = DELETE
        request = {'path': path, 'method': method}
        return request
