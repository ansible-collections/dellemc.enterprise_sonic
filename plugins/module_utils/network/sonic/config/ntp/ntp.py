#
# -*- coding: utf-8 -*-
# Copyright 2022 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_ntp class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import re

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
    normalize_interface_name,
    normalize_interface_name_list
)
from ansible.module_utils.connection import ConnectionError

PATCH = 'PATCH'
DELETE = 'DELETE'

TEST_KEYS_ADD = [
    {"vrf": "", "source_interfaces": "", "servers": {"address": "", "maxpoll": "", "minpoll": ""}}
]

TEST_KEYS_DEL = [
    {"vrf": "", "source_interfaces": "", "servers": {"address": ""}}
]


class Ntp(ConfigBase):
    """
    The sonic_ntp class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'ntp',
    ]

    def __init__(self, module):
        super(Ntp, self).__init__(module)

    def get_ntp_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        ntp_facts = facts['ansible_network_resources'].get('ntp')
        if not ntp_facts:
            return []
        return ntp_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = list()
        commands = list()
        requests = list()

        existing_ntp_facts = self.get_ntp_facts()
        commands, requests = self.set_config(existing_ntp_facts)

        if commands and len(requests) > 0:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    if not re.search("code.*404", str(exc)):
                        # Not "Resource not found"
                        self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        changed_ntp_facts = self.get_ntp_facts()

        result['before'] = existing_ntp_facts
        if result['changed']:
            result['after'] = changed_ntp_facts

        result['warnings'] = warnings
        return result

    def set_config(self, existing_ntp_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']
        if want is None:
            want = []

        have = existing_ntp_facts

        self.preprocess_want(want)

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
            commands, requests = self._state_deleted(want, have)
        elif state == 'merged':
            commands, requests = self._state_merged(want, have)

        return commands, requests

    def _state_merged(self, want, have):
        """ The command generator when state is merged

        :param want: the additive configuration as a dictionary
        :param obj_in_have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        diff = get_diff(want, have, TEST_KEYS_ADD)

        commands = diff
        requests = []
        if commands:
            requests = self.get_create_requests(commands, have)

        if len(requests) > 0:
            commands = update_states(commands, "merged")
        else:
            commands = []
        return commands, requests

    def _state_deleted(self, want, have):
        """ The command generator when state is deleted

        :param want: the objects from which the configuration should be removed
        :param obj_in_have: the current configuration as a dictionary
        :param interface_type: interface type
        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        diff = get_diff(want, have, TEST_KEYS_DEL)

        want_none = {'servers': None, 'source_interfaces': [], 'vrf': None}
        want_any = get_diff(want, want_none, TEST_KEYS_DEL)
        # if want_any is none, then delete all NTP configurations

        if not want_any:
            commands = have
        else:
            if not diff:
                commands = want_any
            else:
                commands = get_diff(want_any, diff, TEST_KEYS_DEL)

        requests = []
        if commands:
            requests = self.get_delete_requests(commands, have)

        if len(requests) > 0:
            commands = update_states(commands, "deleted")
        else:
            commands = []

        return commands, requests

    def preprocess_want(self, want):

        if 'source_interfaces' in want:
            want['source_interfaces'] = normalize_interface_name_list(want['source_interfaces'], self._module)

        if 'servers' in want and want['servers'] is not None:
            for server in want['servers']:
                if not server['minpoll']:
                    server.pop('minpoll')
                if not server['maxpoll']:
                    server.pop('maxpoll')

    def get_create_requests(self, configs, have):

        requests = []

        src_intf_config = configs.get('source_interfaces', None)
        if src_intf_config:
            src_intf_request = self.get_create_source_interface_requests(src_intf_config, have)
            if src_intf_request:
                requests.extend(src_intf_request)

        servers_config = configs.get('servers', None)
        if servers_config:
            servers_request = self.get_create_servers_requests(servers_config, have)
            if servers_request:
                requests.extend(servers_request)

        vrf_config = configs.get('vrf', None)
        if vrf_config:
            vrf_request = self.get_create_vrf_requests(vrf_config, have)
            if vrf_request:
                requests.extend(vrf_request)

        return requests

    def get_delete_requests(self, configs, have):

        requests = []

        src_intf_config = configs.get('source_interfaces', None)
        if src_intf_config:
            src_intf_request = self.get_delete_source_interface_requests(src_intf_config, have)
            if src_intf_request:
                requests.extend(src_intf_request)

        servers_config = configs.get('servers', None)
        if servers_config:
            servers_request = self.get_delete_servers_requests(servers_config, have)
            if servers_request:
                requests.extend(servers_request)

        vrf_config = configs.get('vrf', None)
        if vrf_config:
            vrf_request = self.get_delete_vrf_requests(vrf_config, have)
            if vrf_request:
                requests.extend(vrf_request)

        return requests

    def get_create_source_interface_requests(self, configs, have):

        requests = []

        # Create URL and payload
        method = PATCH
        url = 'data/openconfig-system:system/ntp/config/source-interface'
        payload = {"openconfig-system:source-interface": configs}
        request = {"path": url, "method": method, "data": payload}
        requests.append(request)

        return requests

    def get_create_servers_requests(self, configs, have):

        requests = []

        # Create URL and payload
        method = PATCH
        url = 'data/openconfig-system:system/ntp/servers'
        server_configs = []
        for config in configs:
            server_addr = config['address']
            server_config = {"address": server_addr, "config": config}
            server_configs.append(server_config)

        payload = {"openconfig-system:servers": {"server": server_configs}}
        request = {"path": url, "method": method, "data": payload}
        requests.append(request)

        return requests

    def get_create_vrf_requests(self, configs, have):

        requests = []

        # Create URL and payload
        method = PATCH
        url = 'data/openconfig-system:system/ntp/config/network-instance'
        server_configs = []
        payload = {"openconfig-system:network-instance": configs}
        request = {"path": url, "method": method, "data": payload}
        requests.append(request)

        return requests

    def get_delete_source_interface_requests(self, configs, have):

        requests = []

        # Create URL and payload
        method = DELETE
        for config in configs:
            url = 'data/openconfig-system:system/ntp/config/source-interface={0}'.format(config)
            request = {"path": url, "method": method}
            requests.append(request)

        return requests

    def get_delete_servers_requests(self, configs, have):

        requests = []

        # Create URL and payload
        method = DELETE
        for config in configs:
            server_addr = config['address']
            url = 'data/openconfig-system:system/ntp/servers/server={0}'.format(server_addr)
            request = {"path": url, "method": method}
            requests.append(request)

        return requests

    def get_delete_vrf_requests(self, configs, have):

        requests = []

        # Create URL and payload
        method = DELETE
        url = 'data/openconfig-system:system/ntp/config/network-instance'
        request = {"path": url, "method": method}
        requests.append(request)

        return requests
