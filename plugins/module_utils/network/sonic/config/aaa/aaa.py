#
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_aaa class
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
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import Facts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    update_states,
    get_diff,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)

PATCH = 'patch'
DELETE = 'delete'


class Aaa(ConfigBase):
    """
    The sonic_aaa class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'aaa',
    ]

    def __init__(self, module):
        super(Aaa, self).__init__(module)

    def get_aaa_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        aaa_facts = facts['ansible_network_resources'].get('aaa')
        if not aaa_facts:
            return []
        return aaa_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = list()
        commands = list()

        existing_aaa_facts = self.get_aaa_facts()
        commands, requests = self.set_config(existing_aaa_facts)
        if commands and len(requests) > 0:
            if not self._module.check_mode:
                self.edit_config(requests)
            result['changed'] = True
        result['commands'] = commands

        changed_aaa_facts = self.get_aaa_facts()

        result['before'] = existing_aaa_facts
        if result['changed']:
            result['after'] = changed_aaa_facts

        result['warnings'] = warnings
        return result

    def edit_config(self, requests):
        try:
            response = edit_config(self._module, to_request(self._module, requests))
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)

    def set_config(self, existing_aaa_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']
        have = existing_aaa_facts
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
        if not want:
            want = {}

        if state == 'deleted':
            commands = self._state_deleted(want, have)
        elif state == 'merged':
            diff = get_diff(want, have)
            commands = self._state_merged(want, have, diff)
        return commands

    def _state_merged(self, want, have, diff):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = []
        requests = []
        if diff:
            requests = self.get_create_aaa_request(diff)
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
        if not want:
            if have:
                requests = self.get_delete_all_aaa_request(have)
                if len(requests) > 0:
                    commands = update_states(have, "deleted")
        else:
            want = utils.remove_empties(want)
            new_have = self.remove_default_entries(have)
            d_diff = get_diff(want, new_have, is_skeleton=True)
            diff_want = get_diff(want, d_diff, is_skeleton=True)
            if diff_want:
                requests = self.get_delete_all_aaa_request(diff_want)
                if len(requests) > 0:
                    commands = update_states(diff_want, "deleted")
        return commands, requests

    def get_create_aaa_request(self, commands):
        requests = []
        aaa_path = 'data/openconfig-system:system/aaa'
        method = PATCH
        aaa_payload = self.build_create_aaa_payload(commands)
        if aaa_payload:
            request = {'path': aaa_path, 'method': method, 'data': aaa_payload}
            requests.append(request)
        return requests

    def build_create_aaa_payload(self, commands):
        payload = {}
        if "authentication" in commands and commands["authentication"]:
            payload = {"openconfig-system:aaa": {"authentication": {"config": {"authentication-method": []}}}}
            if "local" in commands["authentication"]["data"] and commands["authentication"]["data"]["local"]:
                payload['openconfig-system:aaa']['authentication']['config']['authentication-method'].append("local")
            if "group" in commands["authentication"]["data"] and commands["authentication"]["data"]["group"]:
                auth_method = commands["authentication"]["data"]["group"]
                payload['openconfig-system:aaa']['authentication']['config']['authentication-method'].append(auth_method)
            if "fail_through" in commands["authentication"]["data"]:
                cfg = {'openconfig-system-ext:failthrough': str(commands["authentication"]["data"]["fail_through"])}
                payload['openconfig-system:aaa']['authentication']['config'].update(cfg)
        return payload

    def remove_default_entries(self, data):
        new_data = {}
        if not data:
            return new_data
        else:
            new_data = {'authentication': {'data': {}}}
            local = data['authentication']['data'].get('local', None)
            if local is not None:
                new_data["authentication"]["data"]["local"] = local
            group = data['authentication']['data'].get('group', None)
            if group is not None:
                new_data["authentication"]["data"]["group"] = group
            fail_through = data['authentication']['data'].get('fail_through', None)
            if fail_through is not None:
                new_data["authentication"]["data"]["fail_through"] = fail_through
            return new_data

    def get_delete_all_aaa_request(self, have):
        requests = []
        if "authentication" in have and have["authentication"]:
            if "local" or "group" in have["authentication"]["data"]:
                request = self.get_authentication_method_delete_request()
                requests.append(request)
            if "fail_through" in have["authentication"]["data"]:
                request = self.get_failthrough_delete_request()
                requests.append(request)
        return requests

    def get_authentication_method_delete_request(self):
        path = 'data/openconfig-system:system/aaa/authentication/config/authentication-method'
        method = DELETE
        request = {'path': path, 'method': method}
        return request

    def get_failthrough_delete_request(self):
        path = 'data/openconfig-system:system/aaa/authentication/config/openconfig-system-ext:failthrough'
        method = DELETE
        request = {'path': path, 'method': method}
        return request
