#
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_ptp_default_ds class
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
    get_diff,
    update_states,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.formatted_diff_utils import (
    get_new_config,
    get_formatted_config_diff
)
from ansible.module_utils.connection import ConnectionError


PATCH = 'patch'
DELETE = 'delete'


def __derive_ptp_default_ds_delete_op(key_set, command, exist_conf):
    new_conf = exist_conf

    if command.get('announce_receipt_timeout', None):
        new_conf.pop('announce_receipt_timeout', None)

    if command.get('clock_type', None):
        new_conf.pop('clock_type', None)

    if command.get('domain_number', None):
        new_conf.pop('domain_number', None)

    if command.get('domain_profile', None):
        new_conf.pop('domain_profile', None)

    if command.get('log_announce_interval', None):
        new_conf.pop('log_announce_interval', None)

    if command.get('log_min_delay_req_interval', None):
        new_conf.pop('log_min_delay_req_interval', None)

    if command.get('log_sync_interval', None):
        new_conf.pop('log_sync_interval', None)

    if command.get('network_transport', None):
        new_conf.pop('network_transport', None)

    if command.get('priority1', None):
        new_conf.pop('priority1', None)

    if command.get('priority2', None):
        new_conf.pop('priority2', None)

    if command.get('unicast_multicast', None):
        new_conf.pop('unicast_multicast', None)

    if command.get('source_interface', None):
        new_conf.pop('source_interface', None)

    if command.get('two_step_flag', None):
        new_conf.pop('two_step_flag', None)

    return True, new_conf


TEST_KEYS_generate_config = [
    {'config': {'__delete_op': __derive_ptp_default_ds_delete_op}},
]


class Ptp_default_ds(ConfigBase):
    """
    The sonic_ptp_default_ds class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'ptp_default_ds',
    ]

    ptp_default_ds_path = 'data/ietf-ptp:ptp/instance-list=0/default-ds'
    ptp_default_ds_config_path = {
        'priority1': ptp_default_ds_path + '/priority1',
        'priority2': ptp_default_ds_path + '/priority2',
        'domain_number': ptp_default_ds_path + '/domain-number',
        'log_announce_interval': ptp_default_ds_path + '/ietf-ptp-ext:log-announce-interval',
        'announce_receipt_timeout': ptp_default_ds_path + '/ietf-ptp-ext:announce-receipt-timeout',
        'log_sync_interval': ptp_default_ds_path + '/ietf-ptp-ext:log-sync-interval',
        'log_min_delay_req_interval': ptp_default_ds_path + '/ietf-ptp-ext:log-min-delay-req-interval',
        'two_step_flag': ptp_default_ds_path + '/two-step-flag',
        'clock_type': ptp_default_ds_path + '/ietf-ptp-ext:clock-type',
        'network_transport': ptp_default_ds_path + '/ietf-ptp-ext:network-transport',
        'unicast_multicast': ptp_default_ds_path + '/ietf-ptp-ext:unicast-multicast',
        'domain_profile': ptp_default_ds_path + '/ietf-ptp-ext:domain-profile',
        'source_interface': ptp_default_ds_path + '/ietf-ptp-ext:source-interface',
    }

    def __init__(self, module):
        super(Ptp_default_ds, self).__init__(module)

    def get_ptp_default_ds_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        ptp_default_ds_facts = facts['ansible_network_resources'].get('ptp_default_ds')
        if not ptp_default_ds_facts:
            return []
        return ptp_default_ds_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = []

        existing_ptp_default_ds_facts = self.get_ptp_default_ds_facts()
        commands, requests = self.set_config(existing_ptp_default_ds_facts)
        if commands:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True

        changed_ptp_default_ds_facts = self.get_ptp_default_ds_facts()

        result['before'] = existing_ptp_default_ds_facts
        if result['changed']:
            result['after'] = changed_ptp_default_ds_facts

        result['commands'] = commands

        new_config = changed_ptp_default_ds_facts
        old_config = existing_ptp_default_ds_facts
        if self._module.check_mode:
            result.pop('after', None)
            new_config = get_new_config(commands, existing_ptp_default_ds_facts,
                                        TEST_KEYS_generate_config)
            result['after(generated)'] = new_config

        if self._module._diff:
            result['diff'] = get_formatted_config_diff(old_config,
                                                       new_config,
                                                       self._module._verbosity)
        result['warnings'] = warnings
        return result

    def set_config(self, existing_ptp_default_ds_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']
        have = existing_ptp_default_ds_facts
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
        if state == 'deleted':
            commands, requests = self._state_deleted(want, have, diff)
        elif state == 'merged':
            commands, requests = self._state_merged(diff)
        elif state == 'overridden' or state == 'replaced':
            commands, requests = self._state_replaced_or_overridden(want, have, state)

        return commands, requests

    def _state_replaced_or_overridden(self, want, have, state):
        """ The command generator when state is replaced or overridden

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        requests = []

        if len(have) == 1 and have.get("domain_number") is not None :
            if len(want) == 1 and want.get("domain_number") is not None and want == have:
                return commands, requests
            if have["domain_number"] == 0:
                have.pop("domain_number")

        if want and have and not get_diff(want, have) and not get_diff(have, want):
            return commands, requests

        del_requests = self.get_delete_ptp_default_ds_completely_requests(have)
        requests.extend(del_requests)
        commands.extend(update_states(have, "deleted"))
        have = {}

        if not have and want:
            mod_requests = self.get_modify_specific_ptp_default_ds_param_requests(want)
            mod_commands = want
            if len(mod_requests) > 0:
                requests.extend(mod_requests)
                commands.extend(update_states(mod_commands, state))

        return commands, requests

    def _state_merged(self, diff):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = diff
        requests = []
        requests.extend(self.get_modify_specific_ptp_default_ds_param_requests(commands))
        if commands and len(requests) > 0:
            commands = update_states(commands, 'merged')
        else:
            commands = []

        return commands, requests

    def _state_deleted(self, want, have, diff):
        """ The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        commands = []
        requests = []

        if len(have) == 1 and have.get("domain_number") is not None:
            have.pop("domain_number")

        if not want or len(want) == 0:
            commands = have
            requests.extend(self.get_delete_ptp_default_ds_completely_requests(commands))
        else:
            commands = get_diff(want, diff)
            requests.extend(self.get_delete_specific_ptp_default_ds_param_requests(commands, have))
        if len(requests) == 0:
            commands = []

        if commands:
            commands = update_states(commands, "deleted")

        return commands, requests

    def get_modify_specific_ptp_default_ds_param_requests(self, command):
        """Get requests to modify specific PTP default ds configurations
        based on the command specified for the interface
        """
        requests = []

        if not command:
            return requests
        if 'priority1' in command and command['priority1'] is not None:
            payload = {'ietf-ptp:priority1': command['priority1']}
            url = self.ptp_default_ds_config_path['priority1']
            requests.append({'path': url, 'method': PATCH, 'data': payload})

        if 'priority2' in command and command['priority2'] is not None:
            payload = {'ietf-ptp:priority2': command['priority2']}
            url = self.ptp_default_ds_config_path['priority2']
            requests.append({'path': url, 'method': PATCH, 'data': payload})

        if 'clock_type' in command and command['clock_type'] is not None:
            payload = {'ietf-ptp-ext:clock-type': command['clock_type']}
            url = self.ptp_default_ds_config_path['clock_type']
            requests.append({'path': url, 'method': PATCH, 'data': payload})

        if 'network_transport' in command and command['network_transport'] is not None:
            payload = {'ietf-ptp-ext:network-transport': command['network_transport']}
            url = self.ptp_default_ds_config_path['network_transport']
            requests.append({'path': url, 'method': PATCH, 'data': payload})

        if 'unicast_multicast' in command and command['unicast_multicast'] is not None:
            payload = {'ietf-ptp-ext:unicast-multicast': command['unicast_multicast']}
            url = self.ptp_default_ds_config_path['unicast_multicast']
            requests.append({'path': url, 'method': PATCH, 'data': payload})

        if 'domain_number' in command and command['domain_number'] is not None:
            payload = {'ietf-ptp:domain-number': command['domain_number']}
            url = self.ptp_default_ds_config_path['domain_number']
            requests.append({'path': url, 'method': PATCH, 'data': payload})

        if 'domain_profile' in command and command['domain_profile'] is not None:
            payload = {'ietf-ptp-ext:domain-profile': command['domain_profile']}
            url = self.ptp_default_ds_config_path['domain_profile']
            requests.append({'path': url, 'method': PATCH, 'data': payload})

        if 'two_step_flag' in command and command['two_step_flag'] is not None:
            payload = {'ietf-ptp:two-step-flag': command['two_step_flag']}
            url = self.ptp_default_ds_config_path['two_step_flag']
            requests.append({'path': url, 'method': PATCH, 'data': payload})

        if 'source_interface' in command and command['source_interface'] is not None:
            payload = {'ietf-ptp-ext:source-interface': command['source_interface']}
            url = self.ptp_default_ds_config_path['source_interface']
            requests.append({'path': url, 'method': PATCH, 'data': payload})

        if 'log_announce_interval' in command and command['log_announce_interval'] is not None:
            payload = {'ietf-ptp-ext:log-announce-interval': command['log_announce_interval']}
            url = self.ptp_default_ds_config_path['log_announce_interval']
            requests.append({'path': url, 'method': PATCH, 'data': payload})

        if 'announce_receipt_timeout' in command and command['announce_receipt_timeout'] is not None:
            payload = {'ietf-ptp-ext:announce-receipt-timeout': command['announce_receipt_timeout']}
            url = self.ptp_default_ds_config_path['announce_receipt_timeout']
            requests.append({'path': url, 'method': PATCH, 'data': payload})

        if 'log_sync_interval' in command and command['log_sync_interval'] is not None:
            payload = {'ietf-ptp-ext:log-sync-interval': command['log_sync_interval']}
            url = self.ptp_default_ds_config_path['log_sync_interval']
            requests.append({'path': url, 'method': PATCH, 'data': payload})

        if 'log_min_delay_req_interval' in command and command['log_min_delay_req_interval'] is not None:
            payload = {'ietf-ptp-ext:log-min-delay-req-interval': command['log_min_delay_req_interval']}
            url = self.ptp_default_ds_config_path['log_min_delay_req_interval']
            requests.append({'path': url, 'method': PATCH, 'data': payload})

        return requests

    def get_delete_ptp_default_ds_completely_requests(self, have):
        """Get requests to delete all existing PTP default ds
        configurations in the chassis
        """
        requests = []
        if have:
            url = 'data/ietf-ptp:ptp/instance-list=0/default-ds'
            requests.append({'path': url, 'method': DELETE})

        return requests

    def get_delete_specific_ptp_default_ds_param_requests(self, command, config):
        """Get requests to delete specific PTP default ds configurations
        based on the command specified for the interface
        """
        requests = []

        if not command:
            return requests

        if 'priority1' in command:
            url = self.ptp_default_ds_config_path['priority1']
            requests.append({'path': url, 'method': DELETE})

        if 'priority2' in command:
            url = self.ptp_default_ds_config_path['priority2']
            requests.append({'path': url, 'method': DELETE})

        if 'source_interface' in command:
            url = self.ptp_default_ds_config_path['source_interface']
            requests.append({'path': url, 'method': DELETE})

        if 'log_announce_interval' in command:
            url = self.ptp_default_ds_config_path['log_announce_interval']
            requests.append({'path': url, 'method': DELETE})

        if 'announce_receipt_timeout' in command:
            url = self.ptp_default_ds_config_path['announce_receipt_timeout']
            requests.append({'path': url, 'method': DELETE})

        if 'log_sync_interval' in command:
            url = self.ptp_default_ds_config_path['log_sync_interval']
            requests.append({'path': url, 'method': DELETE})

        if 'log_min_delay_req_interval' in command:
            url = self.ptp_default_ds_config_path['log_min_delay_req_interval']
            requests.append({'path': url, 'method': DELETE})

        if 'two-step-flag' in command:
            url = self.ptp_default_ds_config_path['two_step_flag']
            requests.append({'path': url, 'method': DELETE})

        if 'domain_profile' in command:
            url = self.ptp_default_ds_config_path['domain_profile']
            requests.append({'path': url, 'method': DELETE})

        if 'domain_number' in command:
            url = self.ptp_default_ds_config_path['domain_number']
            requests.append({'path': url, 'method': DELETE})

        if 'network_transport' in command:
            url = self.ptp_default_ds_config_path['network_transport']
            requests.append({'path': url, 'method': DELETE})

        if 'unicast_multicast' in command:
            url = self.ptp_default_ds_config_path['unicast_multicast']
            requests.append({'path': url, 'method': DELETE})

        if 'clock_type' in command:
            url = self.ptp_default_ds_config_path['clock_type']
            requests.append({'path': url, 'method': DELETE})

        return requests
