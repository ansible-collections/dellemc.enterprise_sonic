#
# -*- coding: utf-8 -*-
# Copyright 2023 Dell Inc. or its subsidiaries. All Rights Reserved
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
    update_states,
    get_diff,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import to_request
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
import json
from ansible.module_utils._text import to_native
from ansible.module_utils.connection import ConnectionError
import traceback
try:
    import jinja2
    HAS_LIB = True
except Exception as e:
    HAS_LIB = False
    ERR_MSG = to_native(e)
    LIB_IMP_ERR = traceback.format_exc()

try:
    from urllib.parse import urlencode
except Exception:
    from urllib import urlencode


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
        new_want = self.validate_type(want)
        diff = get_diff(new_want, have)
        if state == 'overridden':
            commands, requests = self._state_overridden(want, have)
        elif state == 'deleted':
            commands, requests = self._state_deleted(want, have)
        elif state == 'merged':
            commands, requests = self._state_merged(want, have, diff)
        elif state == 'replaced':
            commands, requests = self._state_replaced(want, have)
        return commands, requests

    def _state_replaced(self, want, have):
        """ The command generator when state is replaced

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        requests = []
        commands_del = []
        commands_replace = []
        requests_del = []
        requests_replace = []

        commands_del, commands_replace = self.get_replaced_overridden_config(want, have)

        if commands_del:
            requests_del = self.get_delete_bgp_ext_communities(commands_del, have, False)

            if len(requests_del) > 0:
                commands = update_states(commands_del, "deleted")
                requests = requests_del

        if commands_replace and get_diff(commands_replace, have):
            requests_replace = self.get_modify_bgp_ext_community_requests(commands_replace, have)
            if len(requests_replace) > 0:
                commands.extend(update_states(commands_replace, "replaced"))
                requests.extend(requests_replace)

        return commands, requests

    def _state_overridden(self, want, have):
        """ The command generator when state is overridden

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        requests = []
        commands_del = []
        commands_over = []
        requests_del = []
        requests_over = []

        commands_del, commands_over = self.get_replaced_overridden_config(want, have)

        if commands_del:
            requests_del = self.get_delete_all_bgp_ext_communities(commands_del)

            if len(requests_del) > 0:
                commands = update_states(have, "deleted")
                requests = requests_del

        if commands_over and get_diff(commands_over, have):
            requests_over = self.get_modify_bgp_ext_community_requests(commands_over, have)

            if len(requests_over) > 0:
                commands.extend(update_states(commands_over, "overridden"))
                requests.extend(requests_over)

        return commands, requests

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

    def _state_deleted(self, want, have):
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
            members_str = urlencode(members_params)
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
                        delete_all_route_origin = False
                        delete_all_route_target = False
                        no_route_origin = False
                        no_route_target = False

                        for item in have:
                            if item['name'] == name and item['members']:
                                if members['regex']:
                                    members['regex'].sort()
                                    item['members']['regex'].sort()
                                    if members['regex'] == item['members']['regex']:
                                        requests.append(self.get_delete_single_bgp_ext_community_requests(name))
                                    else:
                                        for member_want in members['regex']:
                                            if str(member_want) in item['members']['regex']:
                                                diff_members.append('REGEX:' + str(member_want))
                                if members['route_origin']:
                                    if item['members']['route_origin']:
                                        members['route_origin'].sort()
                                        item['members']['route_origin'].sort()
                                        if members['route_origin'] == item['members']['route_origin']:
                                            delete_all_route_origin = True
                                        else:
                                            for member_want in members['route_origin']:
                                                if str(member_want) in item['members']['route_origin']:
                                                    diff_members.append("route-origin:" + str(member_want))
                                else:
                                    no_route_origin = True

                                if members['route_target']:
                                    if item['members']['route_target']:
                                        members['route_target'].sort()
                                        item['members']['route_target'].sort()
                                        if members['route_target'] == item['members']['route_target']:
                                            delete_all_route_target = True
                                        else:
                                            for member_want in members['route_target']:
                                                if str(member_want) in item['members']['route_target']:
                                                    diff_members.append("route-target:" + str(member_want))
                                else:
                                    no_route_target = True

                        if delete_all_route_target and delete_all_route_origin:
                            requests.append(self.get_delete_single_bgp_ext_community_requests(name))

                        if delete_all_route_target and no_route_origin:
                            requests.append(self.get_delete_single_bgp_ext_community_requests(name))

                        if delete_all_route_origin and no_route_target:
                            requests.append(self.get_delete_single_bgp_ext_community_requests(name))

                        if diff_members:
                            requests.extend(self.get_delete_single_bgp_ext_community_member_requests(name, type, diff_members))

                    else:
                        for item in have:
                            if item['name'] == name:
                                if item['members']:
                                    requests.append(self.get_delete_single_bgp_ext_community_requests(name))
                else:
                    for item in have:
                        if item['name'] == name:
                            requests.append(self.get_delete_single_bgp_ext_community_requests(name))
        return requests

    def get_new_add_request(self, conf):

        url = "data/openconfig-routing-policy:routing-policy/defined-sets/openconfig-bgp-policy:bgp-defined-sets/ext-community-sets"
        method = "PATCH"
        members = conf.get('members', None)
        if 'match' not in conf:
            conf['match'] = "ANY"
        else:
            conf['match'] = conf['match'].upper()
        input_data = {'name': conf['name'], 'match': conf['match']}

        input_data['members_list'] = list()
        if members:
            regex = members.get('regex', None)
            if regex:
                input_data['members_list'].extend(["REGEX:" + cfg for cfg in regex])
            else:
                route_target = members.get('route_target', None)
                if route_target:
                    input_data['members_list'].extend(["route-target:" + cfg for cfg in route_target])
                route_origin = members.get('route_origin', None)
                if route_origin:
                    input_data['members_list'].extend(["route-origin:" + cfg for cfg in route_origin])

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
        env = jinja2.Environment(autoescape=False)
        t = env.from_string(payload_template)
        intended_payload = t.render(input_data)
        ret_payload = json.loads(intended_payload)
        request = {"path": url, "method": method, "data": ret_payload}
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
                    break
            new_req = self.get_new_add_request(conf)
            if new_req:
                requests.append(new_req)
        return requests

    def validate_type(self, want):
        new_want = []
        if want:
            for conf in want:
                cfg = conf.copy()
                cfg['type'] = 'standard'
                members = conf.get('members', None)
                if members and members.get('regex', None):
                    cfg['type'] = 'expanded'

                new_want.append(cfg)
        return new_want

    def get_replaced_overridden_config(self, want, have):
        commands_del = []
        commands_add = []

        for conf in want:
            add_conf = {}
            delete_conf = {}
            name = conf['name']
            have_conf = None
            for h_conf in have:
                if h_conf['name'] == name:
                    have_conf = h_conf
                    break

            if have_conf:
                if have_conf['type'] and conf['type']:
                    if have_conf['type'] != conf['type']:
                        commands_del.append(have_conf)
                        commands_add.append(conf)
                        continue
                    else:
                        add_conf['type'] = conf['type']
                    add_conf['match'] = "ANY"
                    add_conf['permit'] = False
                    add_conf['members'] = {'regex': None, 'route_target': None, 'route_origin': None}

                    if 'match' not in conf:
                        if have_conf['match'] and have_conf['match'] == "ALL":
                            delete_conf['match'] = have_conf['match']
                    else:
                        if have_conf['match'] != conf['match']:
                            delete_conf['match'] = have_conf['match']
                        add_conf['match'] = conf['match']

                    if 'permit' not in conf:
                        if have_conf['permit']:
                            delete_conf['permit'] = have_conf['permit']
                    elif conf['permit']:
                        add_conf['permit'] = True
                    else:
                        if have_conf['permit']:
                            delete_conf['permit'] = True

                    if have_conf['members']:
                        if 'regex' in have_conf['members'] and have_conf['members']['regex']:
                            have_conf['members']['regex'].sort()
                        if 'route_target' in have_conf['members'] and have_conf['members']['route_target']:
                            have_conf['members']['route_target'].sort()
                        if 'route_origin' in have_conf['members'] and have_conf['members']['route_origin']:
                            have_conf['members']['route_origin'].sort()

                    if 'members' not in conf:
                        if have_conf['members']:
                            delete_conf['members'] = have_conf['members']
                    else:
                        if conf['members']:
                            if 'regex' in conf['members']:
                                if conf['members']['regex']:
                                    members = list(map(str, conf['members']['regex']))
                                    members.sort()
                                    if have_conf['members'] and 'regex' in have_conf['members']:
                                        if have_conf['members']['regex'] != members:
                                            delete_conf['members'] = have_conf['members']
                                    add_conf['members'] = {'regex': members}
                            else:
                                if 'route_target' in conf['members']:
                                    members = list(map(str, conf['members']['route_target']))
                                    members.sort()
                                    if have_conf['members'] and 'route_target' in have_conf['members']:
                                        if have_conf['members']['route_target'] != members:
                                            delete_conf['members'] = have_conf['members']
                                    add_conf['members'] = {'route_target': members}

                                if 'route_origin' in conf['members']:
                                    members = list(map(str, conf['members']['route_origin']))
                                    members.sort()
                                    if have_conf['members'] and 'route_origin' in have_conf['members']:
                                        if have_conf['members']['route_origin'] != members:
                                            delete_conf['members'] = have_conf['members']
                                    add_conf['members'] = {'route_origin': members}

                                if 'route_target' not in conf['members'] and 'route_origin' not in conf['members']:
                                    delete_conf['members'] = have_conf['members']

                        else:
                            if have_conf['members']:
                                delete_conf['members'] = have_conf['members']

                add_conf['name'] = name
                commands_add.append(add_conf)
                if delete_conf:
                    delete_conf['name'] = name
                    commands_del.append(delete_conf)

            else:
                commands_add.append(conf)

        return commands_del, commands_add
