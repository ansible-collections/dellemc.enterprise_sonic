#
# -*- coding: utf-8 -*-
# Copyright 2022 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_dcbx_global class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
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
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible.module_utils.connection import ConnectionError

PATCH = "patch"
DELETE = "delete"
class Dcbx_global(ConfigBase):
    """
    The sonic_dcbx_global class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'dcbx_global',
    ]

    dcbx_config_path = 'data/openconfig-dcbx:dcbx/config'
    dcbx_mode_path = {
        'enable': dcbx_config_path + '/enabled'
    }

    def __init__(self, module):
        super(Dcbx_global, self).__init__(module)

    def get_dcbx_global_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        dcbx_global_facts = facts['ansible_network_resources'].get('dcbx_global')
        if not dcbx_global_facts:
            return []
        return dcbx_global_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = list()
        commands = list()

        existing_dcbx_global_facts = self.get_dcbx_global_facts()
        commands, requests = self.set_config(existing_dcbx_global_facts)
        if commands:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        changed_dcbx_global_facts = self.get_dcbx_global_facts()
        result['before'] = existing_dcbx_global_facts
        if result['changed']:
            result['after'] = changed_dcbx_global_facts

        result['warnings'] = warnings
        return result

    def set_config(self, existing_dcbx_global_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']
        have = existing_dcbx_global_facts
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
        if state == 'overridden':
            commands,requests = self._state_overridden(want, have)
        elif state == 'deleted':
            commands, requests = self._state_deleted(want, have)
        elif state == 'merged':
            commands, requests = self._state_merged(want, have)
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
        return commands, requests

    def _state_overridden(self, want, have):
        """ The command generator when state is overridden

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        requests = []
        return commands, requests

    def _state_merged(self, want, have):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        diff = get_diff(want, have)
        commands = diff
        requests = []
        requests.extend(self.modify_specific_dcbx_global_param_requests(commands))
        if commands and len(requests) > 0:
            commands = update_states(commands, 'merged')
        else:
            commands = []
        return commands, requests

    def _state_deleted(self, want, have):
        """ The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        if not want:
            commands = have
        else:
            diff = get_diff(want, have)
            commands = get_diff(want, diff)
        requests = []

        if commands and 'enabled' in commands and commands['enabled'] is True:
            requests.extend(self.delete_dcbx_global_param_requests())

        if len(requests) == 0:
            commands = []

        if commands and 'enabled' in commands and commands['enabled'] is False:
            return commands, requests

        if commands:
            commands = update_states(commands, "deleted")

        return commands, requests

    def delete_dcbx_global_param_requests(self):
        """Requests to delete global DCBx mode configurations in the chassis
        """
        requests = []
        requests.append({'path': self.dcbx_config_path, 'method': DELETE})

        return requests

    def modify_specific_dcbx_global_param_requests(self, command):
        """Requests to modify specific FIPS mode configurations
        """
        requests = []

        if not command:
            return requests

        if 'enabled' in command and command['enabled'] is not None:
            payload = {'openconfig-dcbx:enabled': command['enabled']}
            url = self.dcbx_mode_path['enable']
            requests.append({'path': url, 'method': PATCH, 'data': payload})

        return requests