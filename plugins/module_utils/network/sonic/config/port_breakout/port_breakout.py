#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_port_breakout class
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
from ansible.module_utils.connection import ConnectionError
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import Facts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    update_states,
    get_diff,
    get_speed_from_breakout_mode,
    get_breakout_mode,
)

PATCH = 'patch'
DELETE = 'delete'
POST = 'post'


class Port_breakout(ConfigBase):
    """
    The sonic_port_breakout class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'port_breakout',
    ]

    def __init__(self, module):
        super(Port_breakout, self).__init__(module)

    def get_port_breakout_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        port_breakout_facts = facts['ansible_network_resources'].get('port_breakout')
        if not port_breakout_facts:
            return []
        return port_breakout_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = list()
        existing_port_breakout_facts = self.get_port_breakout_facts()
        commands, requests = self.set_config(existing_port_breakout_facts)
        if commands and len(requests) > 0:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        changed_port_breakout_facts = self.get_port_breakout_facts()

        result['before'] = existing_port_breakout_facts
        if result['changed']:
            result['after'] = changed_port_breakout_facts

        result['warnings'] = warnings
        return result

    def set_config(self, existing_port_breakout_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']
        have = existing_port_breakout_facts
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
        if not want:
            want = []

        have_new = self.get_all_breakout_mode(have)
        diff = get_diff(want, have_new)

        if state == 'overridden':
            commands, requests = self._state_overridden(want, have, diff)
        elif state == 'deleted':
            commands, requests = self._state_deleted(want, have, diff)
        elif state == 'merged':
            commands, requests = self._state_merged(want, have, diff)
        elif state == 'replaced':
            commands, requests = self._state_replaced(want, have, diff)
        return commands, requests

    def _state_merged(self, want, have, diff):
        """ The command generator when state is merged

        :param want: the additive configuration as a dictionary
        :param obj_in_have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = diff
        requests = self.get_modify_port_breakout_requests(commands, have)
        if commands and len(requests) > 0:
            commands = update_states(commands, "merged")
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
        # if want is none, then delete all the port_breakouti except admin
        if not want:
            commands = have
        else:
            commands = want

        requests = self.get_delete_port_breakout_requests(commands, have)

        if commands and len(requests) > 0:
            commands = update_states(commands, "deleted")
        else:
            commands = []

        return commands, requests

    def get_port_breakout_payload(self, name, mode, match):
        payload = {}
        speed = get_speed_from_breakout_mode(mode)
        if speed:
            num_channels = int(mode[0])
            mode_cfg = {'config': {'num-channels': num_channels, 'channel-speed': speed}}
            port_cfg = {'openconfig-platform-port:breakout-mode': mode_cfg}
            compo_cfg = {'name': name, 'port': port_cfg}
            payload = {'openconfig-platform:components': {'component': [compo_cfg]}}
        return payload

    def get_delete_single_port_breakout(self, name, match):
        del_req = None
        if match:
            del_url = 'data/openconfig-platform:components/component=%s/port/openconfig-platform-port:breakout-mode/config' % (name.replace('/', '%2f'))
            del_req = {'path': del_url, 'method': DELETE}
        return del_req

    def get_modify_port_breakout_request(self, conf, match):
        request = None
        name = conf.get('name', None)
        mode = conf.get('mode', None)
        url = 'data/openconfig-platform:components'
        payload = self.get_port_breakout_payload(name, mode, match)
        request = {'path': url, 'method': PATCH, 'data': payload}
        return request

    def get_modify_port_breakout_requests(self, commands, have):
        requests = []
        if not commands:
            return requests

        for conf in commands:
            match = next((cfg for cfg in have if cfg['name'] == conf['name']), None)
            req = self.get_modify_port_breakout_request(conf, match)
            if req:
                requests.append(req)
        return requests

    def get_default_port_breakout_modes(self):
        def_port_breakout_modes = []
        request = [{"path": "operations/sonic-port-breakout:breakout_capabilities", "method": POST}]
        try:
            response = edit_config(self._module, to_request(self._module, request))
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)

        raw_port_breakout_list = []
        if "sonic-port-breakout:output" in response[0][1]:
            raw_port_breakout_list = response[0][1].get("sonic-port-breakout:output", {}).get('caps', [])

        for port_breakout in raw_port_breakout_list:
            name = port_breakout.get('port', None)
            mode = port_breakout.get('defmode', None)
            if name and mode:
                if '[' in mode:
                    mode = mode[:mode.index('[')]
                def_port_breakout_modes.append({'name': name, 'mode': mode})
        return def_port_breakout_modes

    def get_delete_port_breakout_requests(self, commands, have):
        requests = []
        if not commands:
            return requests

        have_new = self.get_all_breakout_mode(have)
        for conf in commands:
            name = conf['name']
            match = next((cfg for cfg in have_new if cfg['name'] == name), None)
            req = self.get_delete_single_port_breakout(name, match)
            if req:
                requests.append(req)
        return requests

    def get_all_breakout_mode(self, have):
        new_have = []
        for cfg in have:
            name = cfg['name']
            mode = get_breakout_mode(self._module, name)
            if mode:
                new_have.append({'name': name, 'mode': mode})
        return new_have
