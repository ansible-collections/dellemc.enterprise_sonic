#
# -*- coding: utf-8 -*-
# Copyright 2024 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_mirroring class
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
    remove_empties,
)
from ansible.module_utils.connection import ConnectionError
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import Facts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    update_states,
    get_diff,
    get_replaced_config,
    get_normalize_interface_name
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.formatted_diff_utils import (
    __DELETE_CONFIG_IF_NO_SUBCONFIG,
    get_new_config,
    get_formatted_config_diff
)

PATCH = 'patch'
DELETE = 'delete'
URL = 'data/sonic-mirror-session:sonic-mirror-session/MIRROR_SESSION/MIRROR_SESSION_LIST'
TEST_KEYS = [
    {'span': {'name': ''}},
    {'erspan': {'name': ''}},
]


def __preprocess_mirroring_config_for_merge_op(key_set, command, have):
    hv = remove_empties(have)
    cmd = remove_empties(command)
    if not hv or not cmd:
        return False, hv

    h_span = hv.get('span', [])
    h_erspan = hv.get('erspan', [])

    c_span = cmd.get('span', [])
    c_erspan = cmd.get('erspan', [])

    for ms in c_span:
        name = ms['name']
        for h_ms in h_erspan[:]:
            if name == h_ms['name']:
                h_erspan.remove(h_ms)
                break

    for ms in c_erspan:
        name = ms['name']
        for h_ms in h_span[:]:
            if name == h_ms['name']:
                h_span.remove(h_ms)
                break

    new_have = remove_empties(hv)
    return False, new_have


delete_all = False
TEST_KEYS_generate_config = [
    {'config': {'__merge_op': __preprocess_mirroring_config_for_merge_op}},
    {'span': {'name': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}},
    {'erspan': {'name': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}},
]


class Mirroring(ConfigBase):
    """
    The sonic_mirroring class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'mirroring',
    ]

    def __init__(self, module):
        super(Mirroring, self).__init__(module)

    def get_mirroring_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset,
                                                         self.gather_network_resources)
        mirroring_facts = facts['ansible_network_resources'].get('mirroring')
        if not mirroring_facts:
            return {}
        return mirroring_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = list()
        existing_mirroring_facts = self.get_mirroring_facts()
        commands, requests = self.set_config(existing_mirroring_facts)
        if commands and len(requests) > 0:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        changed_mirroring_facts = self.get_mirroring_facts()

        result['before'] = existing_mirroring_facts
        if result['changed']:
            result['after'] = changed_mirroring_facts

        new_config = changed_mirroring_facts
        old_config = existing_mirroring_facts
        if self._module.check_mode:
            result.pop('after', None)
            new_config = get_new_config(commands, old_config,
                                        TEST_KEYS_generate_config)
            new_config = remove_empties(new_config)
            result['after(generated)'] = new_config

        if self._module._diff:
            self.sort_mirrors(old_config)
            self.sort_mirrors(new_config)
            result['diff'] = get_formatted_config_diff(old_config,
                                                       new_config,
                                                       self._module._verbosity)
        result['warnings'] = warnings
        return result

    def set_config(self, existing_mirroring_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']

        have = existing_mirroring_facts
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
        new_want = self.preprocess_want(want)
        self.validate_want(new_want, state)

        commands = []
        requests = []
        if not new_want:
            new_want = {}

        diff = get_diff(new_want, have, TEST_KEYS)

        if state == 'overridden':
            commands, requests = self._state_overridden(new_want, have, diff)
        elif state == 'replaced':
            commands, requests = self._state_replaced(new_want, have, diff)
        elif state == 'deleted':
            commands, requests = self._state_deleted(new_want, have, diff)
        elif state == 'merged':
            commands, requests = self._state_merged(new_want, have, diff)
        return commands, requests

    def _state_merged(self, want, have, diff):
        """ The command generator when state is merged

        :param want: the additive configuration as a dictionary
        :param obj_in_have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = []
        command = diff
        requests = self.get_modify_mirroring_requests(command, have)
        if command and len(requests) > 0:
            commands = update_states([command], "merged")
        else:
            commands = []

        return commands, requests

    def _state_deleted(self, want, have, diff):
        """ The command generator when state is deleted

        :param want: the objects from which the configuration should be removed
        :param obj_in_have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        # if want is none, then delete all the mirroring except admin
        commands = []
        global delete_all
        delete_all = False
        if not want:
            command = have
            delete_all = True
        else:
            command = want

        requests = self.get_delete_mirroring_requests(command, have, delete_all)

        if command and len(requests) > 0:
            commands = update_states([command], "deleted")

        return commands, requests

    def _state_replaced(self, want, have, diff):
        """ The command generator when state is replaced

        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :param diff: the difference between want and have
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        requests = []
        replaced_config = get_replaced_config(want, have, TEST_KEYS)

        add_commands = []
        if replaced_config:
            del_requests = self.get_delete_mirroring_requests(replaced_config, have)
            requests.extend(del_requests)
            commands.extend(update_states(replaced_config, "deleted"))
            add_commands = want
        else:
            add_commands = diff

        if add_commands:
            add_requests = self.get_modify_mirroring_requests(add_commands, have)
            if len(add_requests) > 0:
                requests.extend(add_requests)
                commands.extend(update_states(add_commands, "replaced"))

        return commands, requests

    def _state_overridden(self, want, have, diff):
        """ The command generator when state is overridden

        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :param diff: the difference between want and have
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        requests = []

        r_diff = get_diff(have, want, TEST_KEYS)
        if have and (diff or r_diff):
            del_requests = self.get_delete_mirroring_requests(have, have, True)
            requests.extend(del_requests)
            commands.extend(update_states(have, "deleted"))
            have = []

        if not have and want:
            want_commands = want
            want_requests = self.get_modify_mirroring_requests(want_commands, have)

            if len(want_requests) > 0:
                requests.extend(want_requests)
                commands.extend(update_states(want_commands, "overridden"))

        return commands, requests

    def get_modify_span_requests(self, command):
        requests = []

        config = []
        span = command.get('span', [])
        if span:
            for ms in span:
                name = ms.get('name')
                dst_port = ms.get('dst_port')
                source = ms.get('source')
                direction = ms.get('direction')

                conf = {'name': name}
                if dst_port:
                    conf['dst_port'] = dst_port
                if source:
                    conf['src_port'] = source
                if direction:
                    conf['direction'] = direction.upper()

                conf['type'] = 'span'
                config.append(conf)

            path = URL
            payload = {'MIRROR_SESSION_LIST': config}
            request = {'path': path, 'method': PATCH, 'data': payload}
            requests.append(request)

        return requests

    def get_modify_erspan_requests(self, command):
        requests = []

        config = []
        erspan = command.get('erspan', [])
        if erspan:
            for ms in erspan:
                name = ms.get('name')
                dst_ip = ms.get('dst_ip')
                src_ip = ms.get('src_ip')
                source = ms.get('source')
                direction = ms.get('direction')
                dscp = ms.get('dscp')
                gre = ms.get('gre')
                ttl = ms.get('ttl')
                queue = ms.get('queue')

                conf = {'name': name}
                if dst_ip:
                    conf['dst_ip'] = dst_ip
                if src_ip:
                    conf['src_ip'] = src_ip
                if source:
                    conf['src_port'] = source
                if direction:
                    conf['direction'] = direction.upper()
                if dscp is not None:
                    conf['dscp'] = dscp
                if gre:
                    conf['gre_type'] = gre
                if ttl is not None:
                    conf['ttl'] = ttl
                if queue is not None:
                    conf['queue'] = queue

                conf['type'] = 'erspan'
                config.append(conf)

            path = URL
            payload = {'MIRROR_SESSION_LIST': config}
            request = {'path': path, 'method': PATCH, 'data': payload}
            requests.append(request)

        return requests

    def get_modify_mirroring_requests(self, command, have):
        requests = []
        if not command:
            return requests

        span_requests = self.get_modify_span_requests(command)
        if span_requests:
            requests.extend(span_requests)

        erspan_requests = self.get_modify_erspan_requests(command)
        if erspan_requests:
            requests.extend(erspan_requests)

        return requests

    def get_delete_mirroring_requests(self, command, have, is_delete_all=False):
        requests = []
        if not command or not have:
            return requests

        if is_delete_all:
            path = URL
            request = {'path': path, 'method': DELETE}
            requests.append(request)
            return requests

        c_span = command.get('span', [])
        c_erspan = command.get('erspan', [])
        h_span = have.get('span', [])
        h_erspan = have.get('erspan', [])

        for ms in c_span:
            ms_name = ms.get('name')
            if next((h_ms for h_ms in h_span if h_ms['name'] == ms_name), None):
                path = (URL + '={name}').format(name=ms_name)
                request = {'path': path, 'method': DELETE}
                requests.append(request)
        for ms in c_erspan:
            ms_name = ms.get('name')
            if next((h_ms for h_ms in h_erspan if h_ms['name'] == ms_name), None):
                path = (URL + '={name}').format(name=ms_name)
                request = {'path': path, 'method': DELETE}
                requests.append(request)
        return requests

    def validate_want(self, want, state):
        if not want:
            return

        span = want.get('span', [])
        erspan = want.get('erspan', [])

        if span and erspan:
            for ms in span:
                name = ms['name']
                in_erspan = next((ems for ems in erspan if name == ems['name']), None)
                if in_erspan:
                    err_msg = "Names of SPAN and ERSPAN mirror sessions should not be duplicated."
                    self._module.fail_json(msg=err_msg, code=400)

        if state == 'deleted':
            for ms in span:
                if len(ms.keys()) > 1:
                    err_msg = "Attribute deletion of SPAN mirror session is not supported."
                    self._module.fail_json(msg=err_msg, code=400)
            for ms in erspan:
                if len(ms.keys()) > 1:
                    err_msg = "Attribute deletion of ERSPAN mirror session is not supported."
                    self._module.fail_json(msg=err_msg, code=400)

    def preprocess_want(self, want):
        new_want = remove_empties(want)
        if not new_want:
            return new_want

        span = new_want.get('span', [])
        erspan = new_want.get('erspan', [])
        for ms in span:
            dst_port = ms.get('dst_port')
            if dst_port and dst_port != 'CPU':
                ms['dst_port'] = get_normalize_interface_name(dst_port, self._module)
            source = ms.get('source')
            if source:
                ms['source'] = get_normalize_interface_name(source, self._module)

        for ms in erspan:
            source = ms.get('source')
            if source:
                ms['source'] = get_normalize_interface_name(source, self._module)

        return new_want

    def sort_mirrors(self, mirror_sessions):
        if not mirror_sessions:
            return

        span = mirror_sessions.get('span', [])
        if span:
            span.sort(key=lambda x: x['name'])

        erspan = mirror_sessions.get('erspan', [])
        if erspan:
            erspan.sort(key=lambda x: x['name'])
