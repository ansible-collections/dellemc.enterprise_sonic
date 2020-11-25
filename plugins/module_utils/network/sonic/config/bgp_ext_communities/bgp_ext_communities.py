#
# -*- coding: utf-8 -*-
# Copyright 2020 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_bgp_ext_communities class
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
    dict_to_set,
    update_states,
    get_diff,
    remove_empties_from_list
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import to_request
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
import urllib.parse
import json
from ansible.module_utils._text import to_native
import traceback
try:
    import jinja2
    HAS_LIB = True
except Exception as e:
    HAS_LIB = False
    ERR_MSG = to_native(e)
    LIB_IMP_ERR = traceback.format_exc()


class Bgp_ext_communities(ConfigBase):
    """
    The sonic_bgp_ext_communities class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'bgp_ext_communities',
    ]

    def __init__(self, module):
        super(Bgp_ext_communities, self).__init__(module)

    def get_bgp_ext_communities_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        bgp_ext_communities_facts = facts['ansible_network_resources'].get('bgp_ext_communities')
        if not bgp_ext_communities_facts:
            return []
        return bgp_ext_communities_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = list()
        commands = list()

        existing_bgp_ext_communities_facts = self.get_bgp_ext_communities_facts()
        commands, requests = self.set_config(existing_bgp_ext_communities_facts)
        if commands and len(requests) > 0:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        changed_bgp_ext_communities_facts = self.get_bgp_ext_communities_facts()

        result['before'] = existing_bgp_ext_communities_facts
        if result['changed']:
            result['after'] = changed_bgp_ext_communities_facts

        result['warnings'] = warnings
        return result

    def set_config(self, existing_bgp_ext_communities_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']
        have = existing_bgp_ext_communities_facts
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
        # with open('/root/ansible_log.log', 'a+') as fp:
        #     fp.write('extcomm: want: ' + str(want) + '\n')
        #     fp.write('extcomm: have: ' + str(have) + '\n')
        #     fp.write('extcomm: diff: ' + str(diff) + '\n')
        if state == 'overridden':
            commands, requests = self._state_overridden(want, have, diff)
        elif state == 'deleted':
            commands, requests = self._state_deleted(want, have, diff)
        elif state == 'merged':
            commands, requests = self._state_merged(want, have, diff)
        elif state == 'replaced':
            commands, requests = self._state_replaced(want, have, diff)
        return commands, requests

    @staticmethod
    def _state_replaced(**kwargs):
        """ The command generator when state is replaced

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        return commands

    @staticmethod
    def _state_overridden(**kwargs):
        """ The command generator when state is overridden

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        return commands

    def _state_merged(self, want, have, diff):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = diff
        requests = self.get_modify_bgp_ext_community_requests(commands, have)
        if commands and len(requests) > 0:
            commands = update_states(commands, "merged")
        else:
            commands = []

        return commands, requests

    def _state_deleted(self, want, have, diff):
        """ The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        is_delete_all = False
        # if want is none, then delete ALL
        if not want:
            commands = have
            is_delete_all = True
        else:
            commands = want

        requests = self.get_delete_bgp_ext_communities(commands, have, is_delete_all)

        if commands and len(requests) > 0:
            commands = update_states(commands, "deleted")
        else:
            commands = []

        return commands, requests

    def get_delete_single_bgp_ext_community_member_requests(self, name, type, members):
        requests = []
        for member in members:
            url = "data/openconfig-routing-policy:routing-policy/defined-sets/openconfig-bgp-policy:"
            url = url + "bgp-defined-sets/ext-community-sets/ext-community-set={name}/config/{members_param}"
            method = "DELETE"
            members_params = {'ext-community-member': member}
            members_str = urllib.parse.urlencode(members_params)
            request = {"path": url.format(name=name, members_param=members_str), "method": method}
            requests.append(request)
        return requests

    def get_delete_all_members_bgp_ext_community_requests(self, name):
        url = "data/openconfig-routing-policy:routing-policy/defined-sets/openconfig-bgp-policy:"
        url = url + "bgp-defined-sets/ext-community-sets/ext-community-set={}/config/ext-community-member"
        method = "DELETE"
        request = {"path": url.format(name), "method": method}
        return request

    def get_delete_single_bgp_ext_community_requests(self, name):
        url = "data/openconfig-routing-policy:routing-policy/defined-sets/openconfig-bgp-policy:bgp-defined-sets/ext-community-sets/ext-community-set={}"
        method = "DELETE"
        request = {"path": url.format(name), "method": method}
        return request

    def get_delete_all_bgp_ext_communities(self, commands):
        url = "data/openconfig-routing-policy:routing-policy/defined-sets/openconfig-bgp-policy:bgp-defined-sets/ext-community-sets"
        method = "DELETE"
        requests = []
        if commands:
            request = {"path": url, "method": method}
            requests.append(request)
        return requests

    def get_delete_bgp_ext_communities(self, commands, have, is_delete_all):
        requests = []
        if is_delete_all:
            requests = self.get_delete_all_bgp_ext_communities(commands)
        else:
            for cmd in commands:
                name = cmd['name']
                type = cmd['type']
                members = cmd['members']
                if members:
                    if members['regex'] or members['route_origin'] or members['route_target']:
                        diff_members = []
                        for item in have:
                            if item['name'] == name and item['members']:
                                if members['regex']:
                                    for member_want in members['regex']:
                                        if str(member_want) in item['members']['regex']:
                                            diff_members.append('REGEX:' + str(member_want))
                                if members['route_origin']:
                                    for member_want in members['route_origin']:
                                        if str(member_want) in item['members']['route_origin']:
                                            diff_members.append("route-origin:" + str(member_want))
                                if members['route_target']:
                                    for member_want in members['route_target']:
                                        if str(member_want) in item['members']['route_target']:
                                            diff_members.append("route-target:" + str(member_want))
                        if diff_members:
                            requests.extend(self.get_delete_single_bgp_ext_community_member_requests(name, type, diff_members))
                    else:
                        for item in have:
                            if item['name'] == name:
                                if item['members']:
                                    requests.append(self.get_delete_all_members_bgp_ext_community_requests(name))
                else:
                    for item in have:
                        if item['name'] == name:
                            requests.append(self.get_delete_single_bgp_ext_community_requests(name))

        # with open('/root/ansible_log.log', 'a+') as fp:
        #     fp.write('bgp_commmunities: delete requests' + str(requests) + '\n')
        return requests

    def get_new_add_request(self, conf):
        url = "data/openconfig-routing-policy:routing-policy/defined-sets/openconfig-bgp-policy:bgp-defined-sets/ext-community-sets"
        method = "PATCH"
        if 'members' in conf and conf['members'] is None:
            return
        if 'match' not in conf:
            conf['match'] = "ANY"
        else:
            conf['match'] = conf['match'].upper()
        # with open('/root/ansible_log.log', 'a+') as fp:
        #     fp.write('CONF  bgp_ext_communities: conf' + str(conf) + '\n')
        input_data = {'name': conf['name'], 'match': conf['match']}

        input_data['members_list'] = list()
        if 'route_target' in conf['members'] and conf['members']['route_target']:
            for i in conf['members']['route_target']:
                input_data['members_list'].append("route-target:" + i)
        if 'route_origin' in conf['members'] and conf['members']['route_origin']:
            for i in conf['members']['route_origin']:
                input_data['members_list'].append("route-origin:" + i)
        if 'regex' in conf['members'] and conf['members']['regex']:
            for i in conf['members']['regex']:
                input_data['members_list'].append("REGEX:" + i)
        if conf['type'] == 'expanded':
            input_data['regex'] = "REGEX:"
        else:
            input_data['regex'] = ""
        if conf['permit']:
            input_data['permit'] = "PERMIT"
        else:
            input_data['permit'] = "DENY"
        payload_template = """
                            {
                                "openconfig-bgp-policy:ext-community-sets": {
                                    "ext-community-set": [
                                        {
                                            "ext-community-set-name": "{{name}}",
                                            "config": {
                                                "ext-community-set-name": "{{name}}",
                                                "ext-community-member": [
                                                    {% for member in members_list %}"{{member}}"{%- if not loop.last -%},{% endif %}{%endfor%}
                                                ],
                                                "openconfig-bgp-policy-ext:action": "{{permit}}",
                                                "match-set-options": "{{match}}"
                                            }
                                        }
                                    ]
                                }
                            }"""
        env = jinja2.Environment(autoescape=False, extensions=['jinja2.ext.autoescape'])
        t = env.from_string(payload_template)
        intended_payload = t.render(input_data)
        ret_payload = json.loads(intended_payload)
        request = {"path": url, "method": method, "data": ret_payload}
        # with open('/root/ansible_log.log', 'a+') as fp:
        #     fp.write('bgp_extcommunities: request' + str(request) + '\n')
        return request

    def get_modify_bgp_ext_community_requests(self, commands, have):
        requests = []
        if not commands:
            return requests

        for conf in commands:
            for item in have:
                if item['name'] == conf['name']:
                    if 'type' not in conf:
                        conf['type'] = item['type']
                    if 'permit' not in conf:
                        conf['permit'] = item['permit']
                    if 'match' not in conf:
                        conf['match'] = item['match']
                    if 'members' not in conf:
                        conf['members'] = item['members']
            new_req = self.get_new_add_request(conf)
            if new_req:
                requests.append(new_req)
        return requests
