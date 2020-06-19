#
# -*- coding: utf-8 -*-
# Copyright 2020 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_mclag class
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
    to_list, remove_empties
)
from ansible_collections.dellemc.sonic.plugins.module_utils.network.sonic.facts.facts import Facts
from ansible_collections.dellemc.sonic.plugins.module_utils.network.sonic.utils.utils import (
    update_states, get_diff
)
from ansible_collections.dellemc.sonic.plugins.module_utils.network.sonic.sonic import send_requests

PATCH = 'patch'
DELETE = 'delete'


class Mclag(ConfigBase):
    """
    The sonic_mclag class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'mclag',
    ]

    def __init__(self, module):
        super(Mclag, self).__init__(module)

    def get_mclag_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        mclag_facts = facts['ansible_network_resources'].get('mclag')
        if not mclag_facts:
            return []
        return mclag_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = list()
        commands = list()

        existing_mclag_facts = self.get_mclag_facts()
        commands, requests = self.set_config(existing_mclag_facts)
        if commands:
            if not self._module.check_mode:
                self.edit_config(requests)
            result['changed'] = True
        result['commands'] = commands

        changed_mclag_facts = self.get_mclag_facts()

        result['before'] = existing_mclag_facts
        if result['changed']:
            result['after'] = changed_mclag_facts

        result['warnings'] = warnings
        return result

    def edit_config(self, requests):
        try:
            response = send_requests(self._module, requests=requests)
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)

    def set_config(self, existing_mclag_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']
        want = remove_empties(want)
        have = existing_mclag_facts
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
        if not have:
            diff = want
        else:
            diff = get_diff(want, have)

        if state == 'deleted':
            commands = self._state_deleted(want, have, diff)
        elif state == 'merged':
            commands = self._state_merged(want, have, diff)
        return commands

    def _state_merged(self, want, have, diff):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        requests = {}
        commands = {}
        if diff:
            requests = self.get_create_mclag_request(want, diff)
            commands = update_states(diff, "merged")
        return commands, requests

    def _state_deleted(self, want, have, diff):
        """ The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        commands = []
        requests = []
        if not want:
            if have:
                requests = self.get_delete_all_mclag_domain_request()
                commands = update_states(have, "delete_all")
        else:
            diff_want = get_diff(want, diff)
            if 'domain_id' in diff_want:
                del diff_want['domain_id']
            if diff_want:
                for each in diff_want:
                    requests.extend(self.get_delete_mclag_attribute_request(want, each))
                commands = update_states(diff_want, "deleted")
        return commands, requests

    def get_delete_mclag_attribute_request(self, want, command):
        requests = []
        url = 'data/openconfig-mclag:mclag/mclag-domains/mclag-domain=%s/config' % (want["domain_id"])
        method = DELETE
        if 'source_address' in command and want["source_address"]:
            url = url + '/source-address'
            request = {'path': url, 'method': method}
            requests.append(request)
        if 'peer_address' in command and want["peer_address"]:
            url = url + '/peer-address'
            request = {'path': url, 'method': method}
            requests.append(request)
        if 'peer_link' in command and want["peer_link"]:
            url = url + '/peer-link'
            request = {'path': url, 'method': method}
            requests.append(request)
        if 'keepalive' in command and want["keepalive"]:
            url = url + '/keepalive-interval'
            request = {'path': url, 'method': method}
            requests.append(request)
        if 'unique_ip' in command and want['unique_ip']:
            for each in want['unique_ip']:
                unique_ip_url = 'data/openconfig-mclag:mclag/vlan-interfaces/vlan-interface=%s' % (each)
                request = {'path': unique_ip_url, 'method': method}
                requests.append(request)
        if 'portchannel_members' in command and want['portchannel_members']:
            for each in want['portchannel_members']:
                portchannel_url = 'data/openconfig-mclag:mclag/interfaces/interface=%s' % (each)
                request = {'path': portchannel_url, 'method': method}
                requests.append(request)
        return requests

    def get_delete_all_mclag_domain_request(self):
        requests = []
        path = 'data/openconfig-mclag:mclag/mclag-domains'
        method = DELETE
        request = {'path': path, 'method': method}
        requests.append(request)
        return requests

    def get_create_mclag_request(self, want, commands):
        requests = []
        path = 'data/openconfig-mclag:mclag/mclag-domains/mclag-domain'
        method = PATCH
        payload = self.build_create_payload(want, commands)
        request = {'path': path, 'method': method, 'data': payload}
        requests.append(request)
        if ('unique_ip' in commands) and (commands['unique_ip']):
            unique_ip_path = 'data/openconfig-mclag:mclag/vlan-interfaces/vlan-interface'
            unique_ip_method = PATCH
            unique_ip_payload = self.build_create_unique_ip_payload(commands['unique_ip'])
            request = {'path': unique_ip_path, 'method': unique_ip_method, 'data': unique_ip_payload}
            requests.append(request)
        if ('portchannel_members' in commands) and (commands['portchannel_members']):
            portchannel_path = 'data/openconfig-mclag:mclag/interfaces/interface'
            portchannel_method = PATCH
            portchannel_payload = self.build_create_portchannel_payload(want, commands['portchannel_members'])
            request = {'path': portchannel_path, 'method': portchannel_method, 'data': portchannel_payload}
            requests.append(request)
        return requests

    def build_create_payload(self, want, commands):
        temp = {}
        if ('session_timeout' in commands) and (commands['session_timeout']):
            temp['session-timeout'] = commands['session_timeout']
        if ('keepalive' in commands) and (commands['keepalive']):
            temp['keepalive-interval'] = commands['keepalive']
        if ('source_address' in commands) and (commands['source_address']):
            temp['source-address'] = commands['source_address']
        if ('peer_address' in commands) and (commands['peer_address']):
            temp['peer-address'] = commands['peer_address']
        if ('peer_link' in commands) and (commands['peer_link']):
            temp['peer-link'] = commands['peer_link']
        mclag_dict = {}
        domain_id = {"domain-id": want["domain_id"]}
        mclag_dict.update(domain_id)
        config = {"config": temp}
        mclag_dict.update(config)
        payload = {"openconfig-mclag:mclag-domain": [mclag_dict]}
        return payload

    def build_create_unique_ip_payload(self, commands):
        payload = {"openconfig-mclag:vlan-interface": []}
        for each in commands:
            payload['openconfig-mclag:vlan-interface'].append({"name": each, "config": {"name": each, "unique-ip-enable": "enable"}})
        return payload

    def build_create_portchannel_payload(self, want, commands):
        payload = {"openconfig-mclag:interface": []}
        for each in commands:
            payload['openconfig-mclag:interface'].append({"name": each, "config": {"name": each, "mclag-domain-id": want['domain_id']}})
        return payload
