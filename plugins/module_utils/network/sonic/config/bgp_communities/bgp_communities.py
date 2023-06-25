#
# -*- coding: utf-8 -*-
# Copyright 2023 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_bgp_communities class
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
from ansible.module_utils.connection import ConnectionError
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

try:
    from urllib.parse import urlencode
except Exception:
    from urllib import urlencode


class Bgp_communities(ConfigBase):
    """
    The sonic_bgp_communities class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'bgp_communities',
    ]

    def __init__(self, module):
        super(Bgp_communities, self).__init__(module)

    def get_bgp_communities_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        bgp_communities_facts = facts['ansible_network_resources'].get('bgp_communities')
        if not bgp_communities_facts:
            return []
        return bgp_communities_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = list()
        commands = list()

        existing_bgp_communities_facts = self.get_bgp_communities_facts()
        commands, requests = self.set_config(existing_bgp_communities_facts)

        if commands and len(requests) > 0:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        changed_bgp_communities_facts = self.get_bgp_communities_facts()

        result['before'] = existing_bgp_communities_facts
        if result['changed']:
            result['after'] = changed_bgp_communities_facts

        result['warnings'] = warnings
        return result

    def set_config(self, existing_bgp_communities_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']
        have = existing_bgp_communities_facts
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
        #     fp.write('comm: want: ' + str(want) + '\n')
        #     fp.write('comm: have: ' + str(have) + '\n')
        #     fp.write('comm: diff: ' + str(diff) + '\n')
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
            requests_del = self.get_delete_bgp_communities(commands_del, have, False)

            if len(requests_del) > 0:
                commands = update_states(commands_del, "deleted")
                requests = requests_del

        if commands_replace and get_diff(commands_replace, have):
            requests_replace = self.get_modify_bgp_community_requests(commands_replace, have)
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
            requests_del = self.get_delete_all_bgp_communities(commands_del)

            if len(requests_del) > 0:
                commands = update_states(have, "deleted")
                requests = requests_del

        if commands_over and get_diff(commands_over, have):
            requests_over = self.get_modify_bgp_community_requests(commands_over, have)

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
        requests = self.get_modify_bgp_community_requests(commands, have)
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
        # Delete a community
        # https://100.94.81.19/restconf/data/openconfig-routing-policy:routing-policy/defined-sets/openconfig-bgp-policy:bgp-defined-sets/community-sets/community-set=extest
        # Delete all members but not community
        # https://100.94.81.19/restconf/data/openconfig-routing-policy:routing-policy/defined-sets/openconfig-bgp-policy:bgp-defined-sets/community-sets/community-set=extest/config/community-member
        # Dete a memeber from the expanded community
        # https://100.94.81.19/restconf/data/openconfig-routing-policy:routing-policy/defined-sets/openconfig-bgp-policy:bgp-defined-sets/community-sets/community-set=extest/config/community-member=REGEX%3A100.100
        # Delete ALL Bgp_communities and its members
        # https://100.94.81.19/restconf/data/openconfig-routing-policy:routing-policy/defined-sets/openconfig-bgp-policy:bgp-defined-sets/community-sets
        is_delete_all = False
        # if want is none, then delete ALL
        if not want:
            commands = have
            is_delete_all = True
        else:
            commands = want

        requests = self.get_delete_bgp_communities(commands, have, is_delete_all)

        if commands and len(requests) > 0:
            commands = update_states(commands, "deleted")
        else:
            commands = []

        return commands, requests

    def get_delete_single_bgp_community_member_requests(self, name, members):
        requests = []
        for member in members:
            url = "data/openconfig-routing-policy:routing-policy/defined-sets/openconfig-bgp-policy:"
            url = url + "bgp-defined-sets/community-sets/community-set={name}/config/{members_param}"
            method = "DELETE"
            members_params = {'community-member': member}
            members_str = urlencode(members_params)
            request = {"path": url.format(name=name, members_param=members_str), "method": method}
            requests.append(request)
        return requests

    def get_delete_all_members_bgp_community_requests(self, name):
        url = "data/openconfig-routing-policy:routing-policy/defined-sets/openconfig-bgp-policy:"
        url = url + "bgp-defined-sets/community-sets/community-set={}/config/community-member"
        method = "DELETE"
        request = {"path": url.format(name), "method": method}
        return request

    def get_delete_single_bgp_community_requests(self, name):
        url = "data/openconfig-routing-policy:routing-policy/defined-sets/openconfig-bgp-policy:bgp-defined-sets/community-sets/community-set={}"
        method = "DELETE"
        request = {"path": url.format(name), "method": method}
        return request

    def get_delete_all_bgp_communities(self, commands):
        url = "data/openconfig-routing-policy:routing-policy/defined-sets/openconfig-bgp-policy:bgp-defined-sets/community-sets"
        method = "DELETE"
        requests = []
        if commands:
            request = {"path": url, "method": method}
            requests.append(request)
        return requests

    def get_delete_bgp_communities(self, commands, have, is_delete_all):
        requests = []
        if is_delete_all:
            requests = self.get_delete_all_bgp_communities(commands)
        else:
            for cmd in commands:
                name = cmd['name']
                members = cmd['members']
                aann_list = cmd['aann']
                local_as = cmd['local_as']
                no_advertise = cmd['no_advertise']
                no_export = cmd['no_export']
                no_peer = cmd['no_peer']

                diff_members = []

                for item in have:
                    if item['name'] == name:
                        if local_as and local_as == item['local_as']:
                            diff_members.append("NO_EXPORT_SUBCONFED")
                        if no_advertise and no_advertise == item['no_advertise']:
                            diff_members.append("NO_ADVERTISE")
                        if no_export and no_export == item['no_export']:
                            diff_members.append("NO_EXPORT")
                        if no_peer and no_peer == item['no_peer']:
                            diff_members.append("NOPEER")

                        if members:
                            if members['regex']:
                                for member_want in members['regex']:
                                    if str(member_want) in item['members']['regex']:
                                        diff_members.append("REGEX:" + str(member_want))
                            else:
                                if item['members']:
                                    requests.append(self.get_delete_all_members_bgp_community_requests(name))

                        if aann_list is not None:
                            if len(aann_list) > 0:
                                for aann in aann_list:
                                    if str(aann) in item['aann']:
                                        diff_members.append(str(aann))
                            else:
                                diff_members.extend(item['aann'])

                        if local_as is None and no_advertise is None and no_export is None:
                            if no_peer is None and members is None and aann_list is None:
                                requests.append(self.get_delete_single_bgp_community_requests(name))

                if diff_members:
                    requests.extend(self.get_delete_single_bgp_community_member_requests(name, diff_members))

        return requests

    def get_new_add_request(self, conf):
        url = "data/openconfig-routing-policy:routing-policy/defined-sets/openconfig-bgp-policy:bgp-defined-sets/community-sets"
        method = "PATCH"
        community_members = []
        community_action = ""

        if 'match' not in conf:
            conf['match'] = "ANY"

        if conf['type'] == 'standard':
            if 'local_as' in conf and conf['local_as']:
                community_members.append("NO_EXPORT_SUBCONFED")
            if 'no_peer' in conf and conf['no_peer']:
                community_members.append("NOPEER")
            if 'no_export' in conf and conf['no_export']:
                community_members.append("NO_EXPORT")
            if 'no_advertise' in conf and conf['no_advertise']:
                community_members.append("NO_ADVERTISE")
            if 'aann' in conf and conf['aann']:
                community_members.extend(conf['aann'])
        elif conf['type'] == 'expanded':
            if 'members' in conf and conf['members']:
                for i in conf['members']['regex']:
                    community_members.extend(["REGEX:" + str(i)])

        if conf['permit']:
            community_action = "PERMIT"
        else:
            community_action = "DENY"

        input_data = {'name': conf['name'], 'members_list': community_members, 'match': conf['match'], 'permit': community_action}

        payload_template = """
                            {
                                "openconfig-bgp-policy:community-sets": {
                                    "community-set": [
                                        {
                                            "community-set-name": "{{name}}",
                                            "config": {
                                                "community-set-name": "{{name}}",
                                                "community-member": [
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

    def get_modify_bgp_community_requests(self, commands, have):
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
                        if item['members'] and item['members']['regex']:
                            members = list(map(str, item['members']['regex']))
                            members.sort()
                            conf['members'] = {'regex': members}
                        else:
                            conf['members'] = item['members']
                    if 'aann' not in conf:
                        if item['aann']:
                            aann = list(map(str, item['aann']))
                            aann.sort()
                            conf['aann'] = aann
                        else:
                            conf['aann'] = item['aann']
                    if 'local_as' not in conf:
                        conf['local_as'] = item['local_as']
                    if 'no_advertise' not in conf:
                        conf['no_advertise'] = item['no_advertise']
                    if 'no_export' not in conf:
                        conf['no_export'] = item['no_export']
                    if 'no_peer' not in conf:
                        conf['no_peer'] = item['no_peer']

            new_req = self.get_new_add_request(conf)
            if new_req:
                requests.append(new_req)
        return requests

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
                add_conf['local_as'] = False
                add_conf['no_advertise'] = False
                add_conf['no_export'] = False
                add_conf['no_peer'] = False
                add_conf['permit'] = False
                add_conf['match'] = "ANY"
                add_conf['aann'] = None
                add_conf['members'] = None

                if 'local_as' not in conf:
                    if have_conf['local_as']:
                        delete_conf['local_as'] = have_conf['local_as']
                elif conf['local_as']:
                    add_conf['local_as'] = True
                else:
                    if have_conf['local_as']:
                        delete_conf['local_as'] = True

                if 'no_advertise' not in conf:
                    if have_conf['no_advertise']:
                        delete_conf['no_advertise'] = have_conf['no_advertise']
                elif conf['no_advertise']:
                    add_conf['no_advertise'] = True
                else:
                    if have_conf['no_advertise']:
                        delete_conf['no_advertise'] = True

                if 'no_export' not in conf:
                    if have_conf['no_export']:
                        delete_conf['no_export'] = have_conf['no_export']
                elif conf['no_export']:
                    add_conf['no_export'] = True
                else:
                    if have_conf['no_export']:
                        delete_conf['no_export'] = True

                if 'no_peer' not in conf:
                    if have_conf['no_peer']:
                        delete_conf['no_peer'] = have_conf['no_peer']
                elif conf['no_peer']:
                    add_conf['no_peer'] = True
                else:
                    if have_conf['no_peer']:
                        delete_conf['no_peer'] = True

                if 'permit' not in conf:
                    if have_conf['permit']:
                        delete_conf['permit'] = have_conf['permit']
                elif conf['permit']:
                    add_conf['permit'] = True
                else:
                    if have_conf['permit']:
                        delete_conf['permit'] = True

                if 'match' not in conf:
                    if have_conf['match'] and have_conf['match'] == "ALL":
                        delete_conf['match'] = have_conf['match']
                else:
                    if have_conf['match'] != conf['match']:
                        delete_conf['match'] = have_conf['match']
                    add_conf['match'] = conf['match']

                if 'aann' not in conf:
                    if have_conf['aann']:
                        delete_conf['aann'] = have_conf['aann']
                else:
                    if conf['aann']:
                        aann = list(map(str, conf['aann']))
                        aann.sort()
                        if have_conf['aann']:
                            have_conf['aann'].sort()
                            if have_conf['aann'] != aann:
                                delete_conf['aann'] = have_conf['aann']
                        add_conf['aann'] = aann
                    else:
                        if have_conf['aann']:
                            delete_conf['aann'] = have_conf['aann']

                if have_conf['members'] and 'regex' in have_conf['members']:
                    if have_conf['members']['regex']:
                        have_conf['members']['regex'].sort()
                if 'members' not in conf:
                    if have_conf['members'] and 'regex' in have_conf['members']:
                        delete_conf['members'] = have_conf['members']
                else:
                    if conf['members']:
                        if 'regex' in conf['members']:
                            if conf['members']['regex']:
                                members = list(map(str, conf['members']['regex']))
                                members.sort()
                                if have_conf['members'] and 'regex' in have_conf['members']:
                                    if have_conf['members']['regex'] != members:
                                        delete_conf['members'] =  have_conf['members']
                                add_conf['members'] = {'regex': members}
                            else:
                                if have_conf['members'] and 'regex' in have_conf['members']:
                                    delete_conf['members'] =  have_conf['members']
                        else:
                            if have_conf['members'] and 'regex' in have_conf['members']:
                                delete_conf['members'] =  have_conf['members']
                    else:
                        if have_conf['members'] and 'regex' in have_conf['members']:
                            delete_conf['members'] =  have_conf['members']

                add_conf['name'] = name
                commands_add.append(add_conf)
                if delete_conf:
                    delete_conf['name'] = name
                    commands_del.append(delete_conf)
            else:
                commands_add.append(conf)

        return commands_del, commands_add
