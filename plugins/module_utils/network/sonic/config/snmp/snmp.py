#
# -*- coding: utf-8 -*-
# Copyright 2020 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_snmp class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import jinja2
import json
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)
from ansible_collections.dellemc.sonic.plugins.module_utils.network.sonic.facts.facts import Facts
from ansible_collections.dellemc.sonic.plugins.module_utils.network.sonic.utils.utils import (
    get_diff,
    update_states,
)
from ansible_collections.dellemc.sonic.plugins.module_utils.network.sonic.sonic import send_requests


class Snmp(ConfigBase):
    """
    The sonic_snmp class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'snmp',
    ]

    def __init__(self, module):
        super(Snmp, self).__init__(module)

    def get_snmp_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        snmp_facts = facts['ansible_network_resources'].get('snmp')
        if not snmp_facts:
            return []
        return snmp_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = list()
        existing_snmp_facts = self.get_snmp_facts()
        commands, requests = self.set_config(existing_snmp_facts)
        if commands:
            if not self._module.check_mode:
                self.edit_config(requests)
            result['changed'] = True
        result['commands'] = commands

        changed_snmp_facts = self.get_snmp_facts()
        result['before'] = existing_snmp_facts
        if result['changed']:
            result['after'] = changed_snmp_facts
        result['warnings'] = warnings
        return result

    def edit_config(self, requests):
        try:
            response = send_requests(self._module, requests=requests)
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)

    def set_config(self, existing_snmp_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']
        state = self._module.params['state']
        have = existing_snmp_facts
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
        diff = get_diff(want, have)
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
        commands = update_states(diff, "merged")
        requests = self.get_edit_snmp_requests(commands)
        return commands, requests

    def _state_overridden(self, want, have, diff):
        """ The command generator when state is overridden

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        ret_requests = list()
        commands = list()
        snmps_to_delete = get_diff(have, want)
        if snmps_to_delete:
            delete_snmp_requests = self.get_delete_snmp_requests(snmps_to_delete)
            ret_requests.extend(delete_snmp_requests)
            commands.extend(update_states(snmps_to_delete, "deleted"))

        if diff:
            snmp_to_create_requests = self.get_create_snmp_requests(diff)
            ret_requests.extend(snmp_to_create_requests)
            commands.extend(update_states(diff, "merged"))

        return commands, ret_requests

    def _state_merged(self, want, have, diff):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = update_states(diff, "merged")
        requests = self.get_create_snmp_requests(commands)
        return commands, requests

    def _state_deleted(self, want, have, diff):
        """ The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        commands = list()
        if not want:
            commands = have
            requests = self.get_delete_all_requests(commands)
        else:
            commands = get_diff(want, diff)
            requests = self.get_delete_snmp_requests(commands)
        commands = update_states(commands, "deleted")
        return commands, requests

    def get_delete_snmp_requests(self, configs):
        requests = []
        if not configs:
            return requests
        url = "data/sonic-snmp:sonic-snmp/SNMP_SERVER_COMMUNITY/SNMP_SERVER_COMMUNITY_LIST={}"
        method = "DELETE"
        for snmp in configs:
            snmp_index = snmp.get("community")
            request = {"path": url.format(snmp_index),
                       "method": method,
                       }
            requests.append(request)
        return requests

    def get_delete_all_requests(self, configs):
        requests = []
        delete_all_snmp_url = "data/sonic-snmp:sonic-snmp/SNMP_SERVER_COMMUNITY/SNMP_SERVER_COMMUNITY_LIST"
        method = "DELETE"
        delete_all_snmp_request = {"path": delete_all_snmp_url, "method": method}
        requests.append(delete_all_snmp_request)
        return requests

    def get_edit_snmp_requests(self, configs):
        requests = []
        if not configs:
            return requests
        url = "data/sonic-snmp:sonic-snmp/SNMP_SERVER_COMMUNITY"
        method = "PATCH"
        for snmp in configs:
            community_str = snmp.get("community")
            securityName = snmp.get("access")
            payload_content = self.build_create_payload(community_str, securityName)
            payload = dict()
            payload["sonic-snmp:SNMP_SERVER_COMMUNITY"] = payload_content
            request = {"path": url, "method": method, "data": payload}
            requests.append(request)
        return requests

    def get_create_snmp_requests(self, configs):
        requests = []
        if not configs:
            return requests
        url = "data/sonic-snmp:sonic-snmp/SNMP_SERVER_COMMUNITY"
        method = "POST"
        for snmp in configs:
            community_str = snmp.get("community")
            securityName = snmp.get("access")
            payload = self.build_create_payload(community_str, securityName)
            request = {"path": url, "method": method, "data": payload}
            requests.append(request)
        return requests

    def build_create_payload(self, community_str, securityName):
        payload_template = """{\n"sonic-snmp:SNMP_SERVER_COMMUNITY_LIST": [\n{\n"index": "{{index}}",\n"securityName": "{{securityName}}"\n}\n]\n}"""
        input_data = {"index": community_str, "securityName": securityName}
        env = jinja2.Environment(autoescape=False, extensions=['jinja2.ext.autoescape'])
        t = env.from_string(payload_template)
        intended_payload = t.render(input_data)
        ret_payload = json.loads(intended_payload)
        return ret_payload
