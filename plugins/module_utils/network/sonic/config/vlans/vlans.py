#
# -*- coding: utf-8 -*-
# Copyright 2020 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_vlans class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import json

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import Facts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    get_diff,
    update_states,
    remove_empties_from_list,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.interfaces_util import (
    build_interfaces_create_request,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
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

TEST_KEYS = [
    {'config': {'vlan_id': ''}},
]


class Vlans(ConfigBase):
    """
    The sonic_vlans class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'vlans',
    ]

    def __init__(self, module):
        super(Vlans, self).__init__(module)

    def get_vlans_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        vlans_facts = facts['ansible_network_resources'].get('vlans')
        if not vlans_facts:
            return []
        return vlans_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = list()

        existing_vlans_facts = self.get_vlans_facts()
        commands, requests = self.set_config(existing_vlans_facts)
        if commands:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        changed_vlans_facts = self.get_vlans_facts()

        result['before'] = existing_vlans_facts
        if result['changed']:
            result['after'] = changed_vlans_facts

        result['warnings'] = warnings
        return result

    def set_config(self, existing_vlans_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = remove_empties_from_list(self._module.params['config'])
        have = existing_vlans_facts
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
        # diff method works on dict, so creating temp dict
        diff = get_diff(want, have, TEST_KEYS)

        if state == 'overridden':
            commands, requests = self._state_overridden(want, have, diff)
        elif state == 'deleted':
            commands, requests = self._state_deleted(want, have, diff)
        elif state == 'merged':
            commands, requests = self._state_merged(want, have, diff)
        elif state == 'replaced':
            commands, requests = self._state_replaced(want, have, diff)

        ret_commands = remove_empties_from_list(commands)
        return ret_commands, requests

    def _state_replaced(self, want, have, diff):
        """ The command generator when state is replaced

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        return self._state_merged(want, have, diff)

    def _state_overridden(self, want, have, diff):
        """ The command generator when state is overridden

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        ret_requests = list()
        commands = list()
        vlans_to_delete = get_diff(have, want, TEST_KEYS)
        if vlans_to_delete:
            delete_vlans_requests = self.get_delete_vlans_requests(vlans_to_delete)
            ret_requests.extend(delete_vlans_requests)
            commands.extend(update_states(vlans_to_delete, "deleted"))

        if diff:
            vlans_to_create_requests = self.get_create_vlans_requests(diff)
            ret_requests.extend(vlans_to_create_requests)
            commands.extend(update_states(diff, "merged"))

        return commands, ret_requests

    def _state_merged(self, want, have, diff):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration at position-0
                  Requests necessary to merge to the current configuration
                  at position-1
        """
        commands = update_states(diff, "merged")
        requests = self.get_create_vlans_requests(commands)

        return commands, requests

    def _state_deleted(self, want, have, diff):
        """ The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        commands = list()
        # if want is none, then delete all the vlans
        if not want:
            commands = have
        else:  # delete specific vlans
            commands = get_diff(want, diff, TEST_KEYS)

        requests = self.get_delete_vlans_requests(commands)
        commands = update_states(commands, "deleted")
        return commands, requests

    def get_delete_vlans_requests(self, configs):
        requests = []
        if not configs:
            return requests
        # Create URL and payload
        url = "data/openconfig-interfaces:interfaces/interface=Vlan{}"
        method = "DELETE"
        for vlan in configs:
            vlan_id = vlan.get("vlan_id")
            request = {"path": url.format(vlan_id),
                       "method": method,
                       }
            requests.append(request)

        return requests

    def get_create_vlans_requests(self, configs):
        requests = []
        if not configs:
            return requests
        for vlan in configs:
            vlan_id = vlan.get("vlan_id")
            interface_name = "Vlan" + str(vlan_id)
            request = build_interfaces_create_request(interface_name=interface_name)
            requests.append(request)

        return requests
