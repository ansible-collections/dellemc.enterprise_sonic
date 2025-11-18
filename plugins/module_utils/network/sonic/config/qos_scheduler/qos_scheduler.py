#
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_qos_scheduler class
It is in this file where the current configuration (as list)
is compared to the provided configuration (as list) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from copy import deepcopy
from ansible.module_utils.connection import ConnectionError
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    get_diff,
    remove_empties_from_list,
    update_states
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.formatted_diff_utils import (
    __DELETE_OP_DEFAULT,
    get_new_config,
    get_formatted_config_diff
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import Facts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)

delete_all = False
is_replaced = False
QOS_SCHEDULER_PATH = '/data/openconfig-qos:qos/scheduler-policies'
PATCH = 'patch'
DELETE = 'delete'
TEST_KEYS = [
    {'config': {'name': ''}},
    {'schedulers': {'sequence': ''}}
]


def __derive_qos_scheduler_delete_op(key_set, command, exist_conf):
    if delete_all or is_replaced:
        return True, []

    return __DELETE_OP_DEFAULT(key_set, command, exist_conf)


TEST_KEYS_generate_config = [
    {'config': {'name': '', '__delete_op': __derive_qos_scheduler_delete_op}},
    {'schedulers': {'sequence': ''}}
]


class Qos_scheduler(ConfigBase):
    """
    The sonic_qos_scheduler class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'qos_scheduler',
    ]

    def __init__(self, module):
        super(Qos_scheduler, self).__init__(module)

    def get_qos_scheduler_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A list
        :returns: The current configuration as a list
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        qos_scheduler_facts = facts['ansible_network_resources'].get('qos_scheduler')
        if not qos_scheduler_facts:
            return []
        return qos_scheduler_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        commands = []

        existing_qos_scheduler_facts = self.get_qos_scheduler_facts()
        commands, requests = self.set_config(existing_qos_scheduler_facts)
        if commands and requests:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True

        result['commands'] = commands
        result['before'] = existing_qos_scheduler_facts
        old_config = existing_qos_scheduler_facts

        if self._module.check_mode:
            new_config = get_new_config(commands, existing_qos_scheduler_facts, TEST_KEYS_generate_config)
            self.sort_lists_in_config(new_config)
            result['after(generated)'] = new_config
        else:
            new_config = self.get_qos_scheduler_facts()
            if result['changed']:
                result['after'] = new_config
        if self._module._diff:
            self.sort_lists_in_config(new_config)
            self.sort_lists_in_config(old_config)
            result['diff'] = get_formatted_config_diff(old_config, new_config, self._module._verbosity)

        return result

    def set_config(self, existing_qos_scheduler_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a list from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = remove_empties_from_list(self._module.params['config'])
        have = existing_qos_scheduler_facts
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
        commands, requests = [], []
        state = self._module.params['state']
        diff = get_diff(want, have, TEST_KEYS)

        if state == 'merged':
            commands, requests = self._state_merged(diff)
        elif state == 'replaced':
            commands, requests = self._state_replaced(want, have, diff)
        elif state == 'overridden':
            commands, requests = self._state_overridden(want, have, diff)
        elif state == 'deleted':
            commands, requests = self._state_deleted(want, have, diff)
        return commands, requests

    def _state_merged(self, diff):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = diff
        requests = self.get_modify_qos_scheduler_request(commands)

        if commands and requests:
            commands = update_states(commands, 'merged')
        else:
            commands = []

        return commands, requests

    def _state_replaced(self, want, have, diff):
        """ The command generator when state is replaced

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        self.get_error_msg(want, 'Replaced')
        global is_replaced
        is_replaced = False
        commands, mod_commands = [], []
        replaced_config, requests = self.get_replaced_config(want, have)

        if replaced_config:
            is_replaced = True
            commands.extend(update_states(replaced_config, 'deleted'))
            mod_commands = want
        else:
            mod_commands = diff

        if mod_commands:
            mod_request = self.get_modify_qos_scheduler_request(mod_commands)

            if mod_request:
                requests.append(mod_request)
                commands.extend(update_states(mod_commands, 'replaced'))

        return commands, requests

    def _state_overridden(self, want, have, diff):
        """ The command generator when state is overridden

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        global delete_all
        self.get_error_msg(want, 'Overridden')
        delete_all = False
        commands, requests = [], []
        mod_commands, mod_request = None, None
        new_have = deepcopy(have)
        self.filter_scheduler_policies(new_have)
        del_commands = get_diff(new_have, want, TEST_KEYS)

        if del_commands:
            delete_all = True
            del_requests = self.get_delete_qos_scheduler_requests(del_commands, delete_all)
            requests.extend(del_requests)
            commands.extend(update_states(new_have, 'deleted'))
            mod_commands = want
            mod_request = self.get_modify_qos_scheduler_request(mod_commands)
        elif diff:
            mod_commands = diff
            mod_request = self.get_modify_qos_scheduler_request(mod_commands)

        if mod_request:
            requests.append(mod_request)
            commands.extend(update_states(mod_commands, 'overridden'))

        return commands, requests

    def _state_deleted(self, want, have, diff):
        """ The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        global delete_all
        delete_all = False
        requests = []

        if not want:
            commands = deepcopy(have)
            delete_all = True
            self.filter_scheduler_policies(commands)
        else:
            commands = get_diff(want, diff, TEST_KEYS)

        if commands:
            requests = self.get_delete_qos_scheduler_requests(commands, delete_all)
            if requests:
                commands = update_states(commands, 'deleted')
        else:
            commands = []

        return commands, requests

    def get_modify_qos_scheduler_request(self, commands):
        """ Returns a patch request to modify the QoS scheduler configuration"""
        request = None

        if commands:
            policy_list = []
            for policy in commands:
                policy_dict = {}
                name = policy['name']
                schedulers = policy.get('schedulers')
                if schedulers:
                    scheduler_list = []
                    for scheduler in schedulers:
                        cfg_dict, trtc_cfg_dict, scheduler_dict = {}, {}, {}
                        sequence = scheduler.get('sequence')
                        scheduler_type = scheduler.get('scheduler_type')
                        weight = scheduler.get('weight')
                        meter_type = scheduler.get('meter_type')
                        cir = scheduler.get('cir')
                        pir = scheduler.get('pir')
                        cbs = scheduler.get('cbs')
                        pbs = scheduler.get('pbs')

                        if sequence is not None:
                            if not (0 <= sequence <= 47 or sequence == 255):
                                self._module.fail_json(msg='Sequence attribute out of range. Please specify a sequence value within range 0-47'
                                                       ' for a CPU queue or a value of 255 for a port queue.')
                            else:
                                cfg_dict['sequence'] = sequence
                        if scheduler_type:
                            cfg_dict['priority'] = scheduler_type.upper()
                        if weight:
                            cfg_dict['weight'] = weight
                        if meter_type:
                            cfg_dict['meter-type'] = meter_type.upper()
                        if cir is not None:
                            trtc_cfg_dict['cir'] = str(cir)
                        if pir is not None:
                            trtc_cfg_dict['pir'] = str(pir)
                        if cbs is not None:
                            trtc_cfg_dict['bc'] = cbs
                        if pbs is not None:
                            trtc_cfg_dict['be'] = pbs

                        if cfg_dict:
                            scheduler_dict['sequence'] = sequence
                            scheduler_dict['config'] = cfg_dict
                        if trtc_cfg_dict:
                            scheduler_dict['two-rate-three-color'] = {'config': trtc_cfg_dict}
                        if scheduler_dict:
                            scheduler_list.append(scheduler_dict)
                    if scheduler_list:
                        policy_dict['schedulers'] = {'scheduler': scheduler_list}
                policy_dict['name'] = name
                policy_dict['config'] = {'name': name}
                if policy_dict:
                    policy_list.append(policy_dict)
            if policy_list:
                payload = {'openconfig-qos:scheduler-policies': {'scheduler-policy': policy_list}}
                request = {'path': QOS_SCHEDULER_PATH, 'method': PATCH, 'data': payload}

        return request

    def get_delete_qos_scheduler_requests(self, commands, is_delete_all):
        """Returns a list of delete requests to delete the specified QoS scheduler configuration"""
        requests = []

        if is_delete_all:
            requests.append({'path': QOS_SCHEDULER_PATH, 'method': DELETE})
            return requests

        for policy in commands:
            name = policy.get('name')
            if len(policy) == 1:
                requests.append(self.get_delete_scheduler_request(name))
                continue

            schedulers = policy.get('schedulers')

            if schedulers:
                for scheduler in schedulers:
                    sequence = scheduler.get('sequence')
                    if len(scheduler) == 1:
                        requests.append(self.get_delete_scheduler_request(name, sequence))
                        continue

                    scheduler_type = scheduler.get('scheduler_type')
                    weight = scheduler.get('weight')
                    meter_type = scheduler.get('meter_type')
                    cir = scheduler.get('cir')
                    pir = scheduler.get('pir')
                    cbs = scheduler.get('cbs')
                    pbs = scheduler.get('pbs')

                    # Weight must be deleted before scheduler type
                    if weight:
                        requests.append(self.get_delete_scheduler_request(name, sequence, 'weight'))
                    if scheduler_type:
                        requests.append(self.get_delete_scheduler_request(name, sequence, 'priority'))
                    if meter_type:
                        requests.append(self.get_delete_scheduler_request(name, sequence, 'meter-type'))
                    if cir is not None:
                        requests.append(self.get_delete_scheduler_request(name, sequence, 'cir'))
                    if pir is not None:
                        requests.append(self.get_delete_scheduler_request(name, sequence, 'pir'))
                    if cbs is not None:
                        requests.append(self.get_delete_scheduler_request(name, sequence, 'bc'))
                    if pbs is not None:
                        requests.append(self.get_delete_scheduler_request(name, sequence, 'be'))

        return requests

    def get_replaced_config(self, want, have):
        """Returns the replaced QoS scheduler configuration and the corresponding delete requests"""
        config_list, requests = [], []

        self.sort_lists_in_config(want)
        self.sort_lists_in_config(have)

        if not want or not have:
            return config_list, requests

        cfg_policy_dict = {policy.get('name'): policy for policy in have}
        for policy in want:
            name = policy['name']
            cfg_policy = cfg_policy_dict.get(name)

            if not cfg_policy:
                continue
            if policy != cfg_policy:
                requests.append(self.get_delete_scheduler_request(name))
                config_list.append(cfg_policy)

        return config_list, requests

    @staticmethod
    def sort_lists_in_config(config):
        """Sorts the lists in the QoS scheduler configuration"""
        if config:
            config.sort(key=lambda x: x['name'])
            for policy in config:
                if 'schedulers' in policy and policy['schedulers']:
                    policy['schedulers'].sort(key=lambda x: x['sequence'])

    def filter_scheduler_policies(self, config):
        """Filter out reserved policy name from the QoS scheduler configuration"""
        if config:
            index = None
            for policy in config:
                name = policy.get('name')
                if name == 'copp-scheduler-policy':
                    index = config.index(policy)
                    break
            if index is not None:
                config.pop(index)
                config = remove_empties_from_list(config)

    def get_error_msg(self, want, state):
        """Return error message for replace or override on reserved policy name"""
        if want:
            for policy in want:
                name = policy.get('name')
                if name == 'copp-scheduler-policy':
                    self._module.fail_json(msg=state + ' not supported for copp-scheduler-policy. Use merged and/or deleted state(s).')

    @staticmethod
    def get_delete_scheduler_request(name, sequence=None, attr=None):
        """Returns a delete request to delete the specified QoS scheduler configuration"""
        url = f'{QOS_SCHEDULER_PATH}/scheduler-policy={name}'

        if sequence is not None:
            url += f'/schedulers/scheduler={sequence}'
        if attr:
            if attr in ('cir', 'pir', 'bc', 'be'):
                url += f'/two-rate-three-color/config/{attr}'
            else:
                url += f'/config/{attr}'

        request = {'path': url, 'method': DELETE}

        return request
