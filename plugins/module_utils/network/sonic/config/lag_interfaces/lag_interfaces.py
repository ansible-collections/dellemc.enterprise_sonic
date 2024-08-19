#
# -*- coding: utf-8 -*-
# Copyright 2020 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_lag_interfaces class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote

import json

from copy import (
    deepcopy
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
    search_obj_in_list
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    update_states,
    get_diff,
    normalize_interface_name,
    remove_empties_from_list,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import Facts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.formatted_diff_utils import (
    __DELETE_CONFIG_IF_NO_SUBCONFIG,
    get_new_config,
    get_formatted_config_diff
)
from ansible.module_utils._text import to_native
from ansible.module_utils.connection import ConnectionError
import traceback

LIB_IMP_ERR = None
ERR_MSG = None
try:
    import jinja2
    HAS_LIB = True
except Exception as e:
    HAS_LIB = False
    ERR_MSG = to_native(e)
    LIB_IMP_ERR = traceback.format_exc()

PUT = 'put'
PATCH = 'patch'
DELETE = 'delete'
TEST_KEYS = [
    {'interfaces': {'member': ''}},
]
TEST_KEYS_formatted_diff = [
    {'config': {'name': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}},
    {'interfaces': {'member': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}},
]


class Lag_interfaces(ConfigBase):
    """
    The sonic_lag_interfaces class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'lag_interfaces',
    ]

    params = ('name', 'members')

    def __init__(self, module):
        super(Lag_interfaces, self).__init__(module)

    def get_lag_interfaces_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        lag_interfaces_facts = facts['ansible_network_resources'].get('lag_interfaces')
        if not lag_interfaces_facts:
            return []
        return lag_interfaces_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = list()
        commands = list()
        existing_lag_interfaces_facts = self.get_lag_interfaces_facts()
        commands, requests = self.set_config(existing_lag_interfaces_facts)
        if commands:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        changed_lag_interfaces_facts = self.get_lag_interfaces_facts()

        result['before'] = existing_lag_interfaces_facts
        if result['changed']:
            result['after'] = changed_lag_interfaces_facts

        new_config = changed_lag_interfaces_facts
        old_config = existing_lag_interfaces_facts
        if self._module.check_mode:
            result.pop('after', None)
            new_config = get_new_config(commands, existing_lag_interfaces_facts,
                                        TEST_KEYS_formatted_diff)
            result['after(generated)'] = new_config
        if self._module._diff:
            self.sort_config(new_config)
            self.sort_config(old_config)
            result['diff'] = get_formatted_config_diff(old_config,
                                                       new_config,
                                                       self._module._verbosity)
        result['warnings'] = warnings
        return result

    def set_config(self, existing_lag_interfaces_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']
        normalize_interface_name(want, self._module)
        have = existing_lag_interfaces_facts
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

        self.validate_want(want, state)
        self.preprocess_want(want, state)

        commands = []
        diff = get_diff(want, have, TEST_KEYS)
        if diff:
            diff_members, diff_portchannels = self.diff_list_for_member_creation(diff)
        else:
            diff_members = []
            diff_portchannels = []

        if state == 'overridden':
            commands, requests = self._state_overridden(want, have, diff_members, diff_portchannels)
        elif state == 'deleted':
            commands, requests = self._state_deleted(want, have, diff)
        elif state == 'merged':
            commands, requests = self._state_merged(want, have, diff_members, diff_portchannels)
        elif state == 'replaced':
            commands, requests = self._state_replaced(want, have, diff_members, diff_portchannels)

        return commands, requests

    def _state_replaced(self, want, have, diff_members, diff_portchannels):
        """ The command generator when state is replaced

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        requests = list()
        commands = list()
        delete_list = list()
        delete_list = get_diff(have, want, TEST_KEYS)
        delete_members, delete_portchannels = self.diff_list_for_member_creation(delete_list)
        replaced_list = list()

        for i in want:
            list_obj = search_obj_in_list(i['name'], delete_members, "name")
            if list_obj:
                replaced_list.append(list_obj)
        requests = self.get_delete_lag_interfaces_requests(replaced_list)
        if requests:
            commands.extend(update_states(replaced_list, "deleted"))

        es_commands, es_requests = self.get_delete_ethernet_segment_requests(replaced_list,
                                                                             want, have, True)
        if es_requests:
            es_cmds = list()
            for cmd in es_commands:
                po_name = cmd['name']
                cmd_in_cmds = next((po for po in commands if po['name'] == po_name), {})
                if not cmd_in_cmds:
                    es_cmds.append(cmd)
            if es_cmds:
                commands.extend(update_states(es_cmds, "deleted"))

            requests.extend(es_requests)

        replaced_commands, replaced_requests = self.template_for_lag_creation(have, diff_members, diff_portchannels, "replaced")
        if replaced_requests:
            commands.extend(replaced_commands)
            requests.extend(replaced_requests)

        return commands, requests

    def _state_overridden(self, want, have, diff_members, diff_portchannels):
        """ The command generator when state is overridden

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        requests = list()
        commands = list()
        delete_list = list()
        delete_list = get_diff(have, want, TEST_KEYS)
        delete_members, delete_portchannels = self.diff_list_for_member_creation(delete_list)

        replaced_list = list()
        for i in want:
            list_obj = search_obj_in_list(i['name'], delete_members, "name")
            if list_obj:
                replaced_list.append(list_obj)

        requests = self.get_delete_lag_interfaces_requests(replaced_list)

        nu, es_requests = self.get_delete_ethernet_segment_requests(replaced_list,
                                                                    want, have, True)
        requests.extend(es_requests)
        commands.extend(update_states(replaced_list, "deleted"))

        deleted_po_list = list()
        for i in delete_list:
            list_obj = search_obj_in_list(i['name'], want, "name")
            if not list_obj:
                deleted_po_list.append(i)

        nu, es_requests = self.get_delete_po_ethernet_segment_requests(deleted_po_list,
                                                                       have)
        requests.extend(es_requests)
        requests_deleted_po = self.get_delete_portchannel_requests(deleted_po_list)
        requests.extend(requests_deleted_po)
        commands_del = self.prune_commands(deleted_po_list)
        commands.extend(update_states(commands_del, "deleted"))

        override_commands, override_requests = self.template_for_lag_creation(have, diff_members, diff_portchannels, "overridden")
        commands.extend(override_commands)
        requests.extend(override_requests)

        return commands, requests

    def _state_merged(self, want, have, diff_members, diff_portchannels):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands, requests = self.template_for_lag_creation(have, diff_members,
                                                            diff_portchannels, "merged")
        return commands, requests

    def _state_deleted(self, want, have, diff):
        """ The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        commands = list()
        requests = list()
        portchannel_requests = list()
        # if want is none, then delete all the lag interfaces and all portchannels
        if not want:
            requests = self.get_delete_all_lag_interfaces_requests()
            portchannel_requests = self.get_delete_all_portchannel_requests()
            requests.extend(portchannel_requests)
            commands_del = self.prune_commands(have)
            commands.extend(update_states(commands_del, "deleted"))
        else:  # delete specific lag interfaces and specific portchannels
            po_commands = get_diff(want, diff, TEST_KEYS)
            po_commands = remove_empties_from_list(po_commands)
            want_members, want_portchannels = self.diff_list_for_member_creation(po_commands)

            del_commands, del_requests = self.template_for_lag_deletion(want, have, want_members,
                                                                        want_portchannels, "deleted")
            if del_commands:
                commands.extend(del_commands)
            if del_requests:
                requests.extend(del_requests)
        return commands, requests

    def diff_list_for_member_creation(self, diff):
        diff_members = list()
        diff_portchannels = list()
        for x in diff:
            if "members" in x.keys() or "ethernet_segment" in x.keys():
                diff_members.append(x)
            else:
                diff_portchannels.append(x)
        return diff_members, diff_portchannels

    def template_for_lag_creation(self, have, diff_members, diff_portchannels, state_name):
        commands = list()
        requests = list()
        if diff_members:
            commands_portchannels, requests = self.call_create_port_channel(diff_members, have)
            if commands_portchannels:
                po_list = [{'name': x['name']} for x in commands_portchannels if x['name']]
            else:
                po_list = []
            if po_list:
                commands.extend(update_states(po_list, state_name))
            diff_members_remove_none = [x for x in diff_members if x.get("members")]
            if diff_members_remove_none:
                request = self.create_lag_interfaces_requests(diff_members_remove_none)
                if request:
                    requests.extend(request)
                else:
                    requests = request

            es_commands, es_request = self.create_ethernet_segment_requests(diff_members, have)
            if es_request:
                requests.append(es_request)

            commands.extend(update_states(diff_members, state_name))
        if diff_portchannels:
            portchannels, po_requests = self.call_create_port_channel(diff_portchannels, have)
            requests.extend(po_requests)

            commands.extend(update_states(portchannels, state_name))
        return commands, requests

    def template_for_lag_deletion(self, want, have, delete_members, delete_portchannels, state_name):
        commands = list()
        requests = list()
        portchannel_requests = list()
        if delete_members:
            delete_members_remove_none = [x for x in delete_members if "members" in x.keys() and x["members"]]
            requests = self.get_delete_lag_interfaces_requests(delete_members_remove_none)
            delete_all_members = [x for x in delete_members if "members" in x.keys() and not x["members"]]
            delete_all_list = list()
            if delete_all_members:
                for i in delete_all_members:
                    list_obj = search_obj_in_list(i['name'], have, "name")
                    if list_obj['members']:
                        delete_all_list.append(list_obj)
            if delete_all_list:
                deleteall_requests = self.get_delete_lag_interfaces_requests(delete_all_list)
            else:
                deleteall_requests = []
            if requests and deleteall_requests:
                requests.extend(deleteall_requests)
            elif deleteall_requests:
                requests = deleteall_requests
            if requests:
                commands.extend(update_states(delete_members, state_name))

            es_commands, es_requests = self.get_delete_ethernet_segment_requests(delete_members,
                                                                                 want, have, False)
            if es_requests:
                es_cmds = list()
                for cmd in es_commands:
                    po_name = cmd['name']
                    cmd_in_cmds = next((po for po in commands if po['name'] == po_name), {})
                    if not cmd_in_cmds:
                        es_cmds.append(cmd)
                if es_cmds:
                    commands.extend(update_states(es_cmds, state_name))
                requests.extend(es_requests)

        if delete_portchannels:
            nu, es_requests = self.get_delete_po_ethernet_segment_requests(delete_portchannels,
                                                                           have)
            if es_requests:
                requests.extend(es_requests)

            portchannel_requests = self.get_delete_portchannel_requests(delete_portchannels)
            commands_del = self.prune_commands(delete_portchannels)
            commands.extend(update_states(commands_del, state_name))
        if requests:
            requests.extend(portchannel_requests)
        else:
            requests = portchannel_requests
        return commands, requests

    def create_lag_interfaces_requests(self, commands):
        requests = []
        for i in commands:
            if i.get('members') and i['members'].get('interfaces'):
                interfaces = i['members']['interfaces']
            else:
                continue
            for each in interfaces:
                edit_payload = self.build_create_payload_member(i['name'])
                template = 'data/openconfig-interfaces:interfaces/interface=%s/openconfig-if-ethernet:ethernet/config/openconfig-if-aggregate:aggregate-id'
                edit_path = template % quote(each['member'], safe='')
                request = {'path': edit_path, 'method': PATCH, 'data': edit_payload}
                requests.append(request)
        return requests

    def create_ethernet_segment_requests(self, diff_members, have):
        es_commands = []
        es_path = 'data/openconfig-network-instance:network-instances/network-instance=default/evpn/ethernet-segments'
        es_payload_list = list()

        for cmd in diff_members:
            po_name = cmd['name']
            cmd_es = cmd.get('ethernet_segment', None)
            if cmd_es:
                es = dict()
                have_po = next((po for po in have if po['name'] == po_name), {})
                have_es = have_po.get('ethernet_segment', {})

                if cmd_es.get('esi_type'):
                    esi_type = cmd_es['esi_type']
                else:
                    esi_type = have_es['esi_type']

                esi = cmd_es.get('esi')
                if esi_type == 'auto_lacp':
                    esi_t = 'TYPE_1_LACP_BASED'
                    esi = 'AUTO'
                elif esi_type == 'auto_system_mac':
                    esi_t = 'TYPE_3_MAC_BASED'
                    esi = 'AUTO'
                elif esi_type == 'ethernet_segment_id':
                    esi_t = 'TYPE_0_OPERATOR_CONFIGURED'
                    if not esi:
                        esi = have_es['esi']
                    esi = ''.join(esi.split(':'))

                if cmd_es.get('df_preference'):
                    df_pref = cmd_es['df_preference']
                else:
                    df_pref = None

                es_payload_item = {
                    'name': po_name,
                    'config': {
                        'name': po_name,
                        'esi-type' : esi_t,
                        'esi' : esi,
                        'interface': po_name
                    }
                }

                if df_pref:
                    df_election = {'config': {'preference': df_pref}}
                    es_payload_item['df-election'] = df_election

                es_payload_list.append(es_payload_item)
                es_commands.append(cmd)

        es_request = {}
        if es_payload_list:
            es_payload = {
                'openconfig-network-instance:ethernet-segments': {
                    'ethernet-segment': es_payload_list
                }
            }

            es_request = {'path': es_path, 'method': PATCH, 'data': es_payload}

        return es_commands, es_request

    def build_create_payload_member(self, name):
        payload_template = """{\n"openconfig-if-aggregate:aggregate-id": "{{name}}"\n}"""
        input_data = {"name": name}
        env = jinja2.Environment(autoescape=False)
        t = env.from_string(payload_template)
        intended_payload = t.render(input_data)
        ret_payload = json.loads(intended_payload)
        return ret_payload

    def build_create_payload_portchannel(self, name, mode):
        payload_template = """{\n"openconfig-interfaces:interfaces": {"interface": [{\n"name": "{{name}}",\n"config": {\n"name": "{{name}}"\n}"""
        input_data = {"name": name}
        if mode == "static":
            payload_template += """,\n "openconfig-if-aggregation:aggregation": {\n"config": {\n"lag-type": "{{mode}}"\n}\n}\n"""
            input_data["mode"] = mode.upper()
        payload_template += """}\n]\n}\n}"""
        env = jinja2.Environment(autoescape=False)
        t = env.from_string(payload_template)
        intended_payload = t.render(input_data)
        ret_payload = json.loads(intended_payload)
        return ret_payload

    def create_port_channel(self, cmd):
        requests = []
        path = 'data/openconfig-interfaces:interfaces'
        for i in cmd:
            payload = self.build_create_payload_portchannel(i['name'], i.get('mode', None))
            request = {'path': path, 'method': PATCH, 'data': payload}
            requests.append(request)
        return requests

    def call_create_port_channel(self, commands, have):
        commands_list = list()
        for c in commands:
            if not any(d['name'] == c['name'] for d in have):
                commands_list.append(c)
        requests = self.create_port_channel(commands_list)

        return commands_list, requests

    def get_delete_all_lag_interfaces_requests(self):
        requests = []
        delete_all_lag_url = 'data/sonic-portchannel:sonic-portchannel/PORTCHANNEL_MEMBER/PORTCHANNEL_MEMBER_LIST'
        method = DELETE
        delete_all_lag_request = {"path": delete_all_lag_url, "method": method}
        requests.append(delete_all_lag_request)
        return requests

    def get_delete_all_portchannel_requests(self):
        requests = []
        delete_all_lag_url = 'data/sonic-portchannel:sonic-portchannel/PORTCHANNEL/PORTCHANNEL_LIST'
        method = DELETE
        delete_all_lag_request = {"path": delete_all_lag_url, "method": method}
        requests.append(delete_all_lag_request)
        return requests

    def get_delete_lag_interfaces_requests(self, commands):
        requests = []
        # Create URL and payload
        url = 'data/openconfig-interfaces:interfaces/interface={}/openconfig-if-ethernet:ethernet/config/openconfig-if-aggregate:aggregate-id'
        method = DELETE
        for c in commands:
            if c.get('members') and c['members'].get('interfaces'):
                interfaces = c['members']['interfaces']
            else:
                continue

            for each in interfaces:
                ifname = each["member"]
                request = {"path": url.format(ifname), "method": method}
                requests.append(request)

        return requests

    def get_delete_po_ethernet_segment_requests(self, delete_portchannels, have):
        es_commands = []
        es_requests = []
        es_path = 'data/openconfig-network-instance:network-instances/network-instance=default/evpn/ethernet-segments'
        ess_path = es_path + '/ethernet-segment=%s'

        for cmd in delete_portchannels:
            po_name = cmd['name']
            have_po = next((po for po in have if po['name'] == po_name), {})
            have_es = have_po.get('ethernet_segment', {})
            if have_es:
                ed_ess_path = ess_path % quote(po_name, safe='')
                es_request = {'path': ed_ess_path, 'method': DELETE}
                es_requests.append(es_request)

                es_commands.append(cmd)

        return es_commands, es_requests

    def get_delete_ethernet_segment_requests(self, delete_members, want, have, delete_es=False):
        es_commands = []
        es_requests = []
        es_path = 'data/openconfig-network-instance:network-instances/network-instance=default/evpn/ethernet-segments'
        ess_path = es_path + '/ethernet-segment=%s'
        df_pref_path = es_path + '/ethernet-segment=%s/df-election/config/preference'

        for cmd in delete_members:
            po_name = cmd['name']
            cmd_es = cmd.get('ethernet_segment', None)
            if cmd_es:
                have_po = next((po for po in have if po['name'] == po_name), {})
                have_es = have_po.get('ethernet_segment', {})
                if not have_es:
                    continue

                want_po = next((po for po in want if po['name'] == po_name), {})
                want_es = want_po.get('ethernet_segment', {})

                del_es = False
                del_df_pref = False
                if delete_es:
                    del_es = True
                else:
                    if cmd_es.get('esi_type'):
                        if cmd_es.get('esi'):
                            if cmd_es.get('df_preference') or not want_es.get('df_preference'):
                                del_es = True
                        elif not want_es.get('esi'):
                            if cmd_es.get('df_preference'):
                                if have_es.get('df_preference'):
                                    del_df_pref = True
                            elif not want_es.get('df_preference'):
                                del_es = True

                if del_es:
                    ed_ess_path = ess_path % quote(po_name, safe='')
                    es_request = {'path': ed_ess_path, 'method': DELETE}
                    es_requests.append(es_request)
                elif del_df_pref:
                    ed_df_pref_path = df_pref_path % quote(po_name, safe='')
                    df_pref_request = {'path': ed_df_pref_path, 'method': DELETE}
                    es_requests.append(df_pref_request)

                es_commands.append(cmd)

        return es_commands, es_requests

    def get_delete_portchannel_requests(self, commands):
        requests = []
        # Create URL and payload
        url = 'data/openconfig-interfaces:interfaces/interface={}'
        method = DELETE
        for c in commands:
            name = c["name"]
            request = {"path": url.format(name), "method": method}
            requests.append(request)

        return requests

    def sort_config(self, configs):
        # natsort provides better result.
        # The use of natsort causes sanity error due to it is not available in
        # python version currently used.
        # new_config = natsorted(new_config, key=lambda x: x['name'])
        # For time-being, use simple "sort"
        configs.sort(key=lambda x: x['name'])

        for conf in configs:
            if conf.get('members', {}) and conf['members'].get('interfaces', []):
                conf['members']['interfaces'].sort(key=lambda x: x['member'])

    def prune_commands(self, commands):
        cmds = deepcopy(commands)
        for cmd in cmds:
            cmd.pop('members', None)
            cmd.pop('ethernet_segment', None)
        return cmds

    def validate_want(self, want, state):
        if not want:
            if state in ('overridden', 'merged', 'replaced'):
                self._module.fail_json(msg='value of config parameter must not be empty for state {0}'.format(state))

            return
        for conf in want:
            es = conf.get('ethernet_segment', None)
            if es:
                esi = es.get('esi', None)
                if es['esi_type'] in ['auto_lacp', 'auto_system_mac']:
                    if esi and esi != 'AUTO':
                        self._module.fail_json(msg='value of esi must be "AUTO" for esi_type {0}'.format(es['esi_type']))
                else:
                    if not esi and state != 'deleted':
                        self._module.fail_json(msg='value of esi must be provided for esi_type {0}'.format(es['esi_type']))

                df_pref = es.get('df_preference')
                if df_pref and (df_pref < 1 or df_pref > 65535):
                    self._module.fail_json(msg='value of df_preference must be in range 1..65535')

    def preprocess_want(self, want, state):
        if not want:
            return
        for conf in want:
            es = conf.get('ethernet_segment', None)
            if es:
                if es['esi_type'] in ['auto_lacp', 'auto_system_mac']:
                    if state != 'deleted':
                        es['esi'] = 'AUTO'
