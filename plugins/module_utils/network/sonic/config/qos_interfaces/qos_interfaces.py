#
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_qos_interfaces class
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
    __DELETE_LEAFS_OR_CONFIG_IF_NO_NON_KEY_LEAF,
    get_new_config,
    get_formatted_config_diff
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import Facts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)

QOS_INTF_PATH = '/data/openconfig-qos:qos/interfaces'
QOS_QUEUE_PATH = '/data/openconfig-qos:qos/queues'
PATCH = 'patch'
DELETE = 'delete'
ANS_MAP_TO_OC_MAP = {
    'dscp_fwd_group': 'dscp-to-forwarding-group',
    'dot1p_fwd_group': 'dot1p-to-forwarding-group',
    'fwd_group_dscp': 'forwarding-group-to-dscp',
    'fwd_group_dot1p': 'forwarding-group-to-dot1p',
    'fwd_group_queue': 'forwarding-group-to-queue',
    'fwd_group_pg': 'forwarding-group-to-priority-group',
    'pfc_priority_queue': 'pfc-priority-to-queue',
    'pfc_priority_pg': 'pfc-priority-to-priority-group'
}

TEST_KEYS = [
    {'config': {'name': ''}},
    {'queues': {'id': ''}},
    {'priorities': {'dot1p': ''}}
]


def __derive_pfc_delete_op(key_set, command, exist_conf):
    """Returns new PFC configuration for delete operation"""
    new_conf = exist_conf
    asymmetric = command.get('asymmetric')
    priorities = command.get('priorities')
    watchdog_action = command.get('watchdog_action')
    watchdog_detect_time = command.get('watchdog_detect_time')
    watchdog_restore_time = command.get('watchdog_restore_time')

    if asymmetric:
        new_conf['asymmetric'] = False
    if watchdog_action != 'drop':
        new_conf['watchdog_action'] = 'drop'
    if watchdog_detect_time:
        new_conf.pop('watchdog_detect_time')
    if watchdog_restore_time:
        new_conf.pop('watchdog_restore_time')
    if priorities:
        new_priority_dict = {priority.get('dot1p'): priority for priority in new_conf['priorities']}
        for priority in priorities:
            dot1p = priority.get('dot1p')
            enable = priority.get('enable')
            new_priority = new_priority_dict.get(dot1p)

            if not new_priority:
                continue

            if enable:
                new_priority['enable'] = False

    return True, new_conf


TEST_KEYS_generate_config = [
    {'config': {'name': '', '__delete_op': __DELETE_LEAFS_OR_CONFIG_IF_NO_NON_KEY_LEAF}},
    {'queues': {'id': ''}},
    {'pfc': {'__delete_op': __derive_pfc_delete_op}}
]


class Qos_interfaces(ConfigBase):
    """
    The sonic_qos_interfaces class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'qos_interfaces',
    ]

    def __init__(self, module):
        super(Qos_interfaces, self).__init__(module)

    def get_qos_interfaces_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A list
        :returns: The current configuration as a list
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        qos_interfaces_facts = facts['ansible_network_resources'].get('qos_interfaces')
        if not qos_interfaces_facts:
            return []
        return qos_interfaces_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        commands = []

        existing_qos_interfaces_facts = self.get_qos_interfaces_facts()
        commands, requests = self.set_config(existing_qos_interfaces_facts)
        if commands and requests:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True

        result['commands'] = commands
        result['before'] = existing_qos_interfaces_facts
        old_config = existing_qos_interfaces_facts

        if self._module.check_mode:
            new_config = get_new_config(commands, existing_qos_interfaces_facts, TEST_KEYS_generate_config)
            self.post_process_generated_config(new_config)
            self.sort_lists_in_config(new_config)
            result['after_generated'] = new_config
        else:
            new_config = self.get_qos_interfaces_facts()
            if result['changed']:
                result['after'] = new_config
        if self._module._diff:
            self.sort_lists_in_config(new_config)
            self.sort_lists_in_config(old_config)
            result['diff'] = get_formatted_config_diff(old_config, new_config, self._module._verbosity)

        return result

    def set_config(self, existing_qos_interfaces_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a list from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = remove_empties_from_list(self._module.params['config'])
        have = existing_qos_interfaces_facts
        self.sort_lists_in_config(want)
        self.sort_lists_in_config(have)
        resp = self.set_state(want, have)
        return to_list(resp)

    def set_state(self, want, have):
        """ Select the appropriate function based on the state provided

        :param want: the desired configuration as a list
        :param have: the current configuration as a list
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands, requests = [], []
        state = self._module.params['state']
        diff = get_diff(want, have, TEST_KEYS)

        if state == 'deleted':
            commands, requests = self._state_deleted(want, have, diff)
        elif state == 'merged':
            commands, requests = self._state_merged(diff)
        return commands, requests

    def _state_merged(self, diff):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = diff
        requests = self.get_modify_qos_interfaces_requests(commands)

        if commands and requests:
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
        delete_all = False
        commands, requests = [], []

        if not want:
            commands = deepcopy(have)
            delete_all = True
        else:
            commands = get_diff(want, diff, TEST_KEYS)

        self.remove_default_entries(commands)

        if commands:
            requests = self.get_delete_qos_interfaces_requests(commands, delete_all)
            if requests:
                commands = update_states(commands, 'deleted')
        else:
            commands = []

        return commands, requests

    def get_modify_qos_interfaces_requests(self, commands):
        """ Returns two patch requests to modify QoS interfaces and queues configuration"""
        requests = []

        if commands:
            intf_list, queue_list = [], []
            for intf in commands:
                intf_dict = {}
                name = intf.get('name')
                scheduler_policy = intf.get('scheduler_policy')
                cable_length = intf.get('cable_length')
                qos_maps = intf.get('qos_maps')
                pfc = intf.get('pfc')
                queues = intf.get('queues')

                if name:
                    intf_dict.update({'interface-id': name, 'config': {'interface-id': name}})
                if scheduler_policy:
                    intf_dict['output'] = {'scheduler-policy': {'config': {'name': scheduler_policy}}}
                if cable_length:
                    intf_dict['openconfig-qos-buffer:cable-length'] = {'config': {'length': cable_length}}
                if qos_maps:
                    map_dict = {}
                    for ans_map in ANS_MAP_TO_OC_MAP:
                        if qos_maps.get(ans_map):
                            map_dict[ANS_MAP_TO_OC_MAP[ans_map]] = qos_maps[ans_map]
                    if map_dict:
                        intf_dict['openconfig-qos-maps-ext:interface-maps'] = {'config': map_dict}
                if pfc:
                    pfc_dict, watchdog_dict = {}, {}
                    asymmetric = pfc.get('asymmetric')
                    watchdog_action = pfc.get('watchdog_action')
                    watchdog_detect_time = pfc.get('watchdog_detect_time')
                    watchdog_restore_time = pfc.get('watchdog_restore_time')
                    priorities = pfc.get('priorities')

                    if asymmetric is not None:
                        pfc_dict['config'] = {'asymmetric': asymmetric}
                    if watchdog_action:
                        watchdog_dict['action'] = watchdog_action.upper()
                    if watchdog_detect_time:
                        watchdog_dict['detection-time'] = watchdog_detect_time
                    if watchdog_restore_time:
                        watchdog_dict['restoration-time'] = watchdog_restore_time
                    if watchdog_dict:
                        pfc_dict['watchdog'] = {'config': watchdog_dict}
                    if priorities:
                        priority_list = []
                        for priority in priorities:
                            priority_dict = {}
                            dot1p = priority.get('dot1p')
                            enable = priority.get('enable')

                            if dot1p is not None:
                                priority_dict['dot1p'] = dot1p
                                priority_dict['config'] = {'dot1p': dot1p}
                            if enable is not None:
                                priority_dict['config']['enable'] = enable
                            if priority_dict:
                                priority_list.append(priority_dict)
                        if priority_list:
                            pfc_dict['pfc-priorities'] = {'pfc-priority': priority_list}
                    if pfc_dict:
                        intf_dict['pfc'] = pfc_dict
                if intf_dict:
                    intf_list.append(intf_dict)
                if queues:
                    queue_list = []
                    for queue in queues:
                        queue_dict = {}
                        queue_id = queue.get('id')
                        wred_profile = queue.get('wred_profile')

                        if queue_id is not None:
                            queue_name = name + ':' + str(queue_id)
                            queue_dict.update({'name': queue_name, 'config': {'name': queue_name}})
                        if wred_profile:
                            queue_dict['wred'] = {'config': {'wred-profile': wred_profile}}
                        if queue_dict:
                            queue_list.append(queue_dict)
                    if queue_list:
                        payload = {'openconfig-qos:queues': {'queue': queue_list}}
                        requests.append({'path': QOS_QUEUE_PATH, 'method': PATCH, 'data': payload})
            if intf_list:
                payload = {'openconfig-qos:interfaces': {'interface': intf_list}}
                requests.append({'path': QOS_INTF_PATH, 'method': PATCH, 'data': payload})

        return requests

    def get_delete_qos_interfaces_requests(self, commands, is_delete_all):
        """Returns a list of delete requests to delete the specified QoS interfaces configuration"""
        requests = []

        if not commands:
            return requests

        if is_delete_all:
            requests.append({'path': QOS_INTF_PATH, 'method': DELETE})
            requests.append({'path': QOS_QUEUE_PATH, 'method': DELETE})
            return requests

        for intf in commands:
            if len(intf) == 1:
                self._module.fail_json(msg='Deletion of a QoS interface not supported')
            name = intf.get('name')
            scheduler_policy = intf.get('scheduler_policy')
            cable_length = intf.get('cable_length')
            qos_maps = intf.get('qos_maps')
            pfc = intf.get('pfc')
            queues = intf.get('queues')

            if scheduler_policy:
                url = f'{QOS_INTF_PATH}/interface={name}/output/scheduler-policy'
                requests.append({'path': url, 'method': DELETE})

            if cable_length:
                url = f'{QOS_INTF_PATH}/interface={name}/openconfig-qos-buffer:cable-length'
                requests.append({'path': url, 'method': DELETE})

            if qos_maps:
                for ans_map in ANS_MAP_TO_OC_MAP:
                    if qos_maps.get(ans_map):
                        requests.append(self.get_delete_map_request(name, ANS_MAP_TO_OC_MAP[ans_map]))

            if pfc:
                asymmetric = pfc.get('asymmetric')
                watchdog_action = pfc.get('watchdog_action')
                watchdog_detect_time = pfc.get('watchdog_detect_time')
                watchdog_restore_time = pfc.get('watchdog_restore_time')
                priorities = pfc.get('priorities')

                # default false
                if asymmetric:
                    url = f'{QOS_INTF_PATH}/interface={name}/pfc/config/asymmetric'
                    requests.append({'path': url, 'method': DELETE})
                if watchdog_action:
                    requests.append(self.get_delete_watchdog_request(name, 'action'))
                if watchdog_detect_time:
                    requests.append(self.get_delete_watchdog_request(name, 'detection-time'))
                if watchdog_restore_time:
                    requests.append(self.get_delete_watchdog_request(name, 'restoration-time'))
                if priorities:
                    for priority in priorities:
                        if len(priority) == 1:
                            self._module.fail_json(msg='Deletion of PFC priority not supported')
                        dot1p = priority.get('dot1p')
                        enable = priority.get('enable')

                        # default false
                        if enable:
                            url = f'{QOS_INTF_PATH}/interface={name}/pfc/pfc-priorities/pfc-priority={dot1p}/config/enable'
                            requests.append({'path': url, 'method': DELETE})

            if queues:
                for queue in queues:
                    queue_id = queue.get('id')
                    queue_name = name + ':' + str(queue_id)

                    if len(queue) == 1:
                        url = f'{QOS_QUEUE_PATH}/queue={queue_name}'
                        requests.append({'path': url, 'method': DELETE})
                        continue

                    wred_profile = queue.get('wred_profile')

                    if wred_profile:
                        url = f'{QOS_QUEUE_PATH}/queue={queue_name}/wred/config/wred-profile'
                        requests.append({'path': url, 'method': DELETE})

        return requests

    @staticmethod
    def get_delete_map_request(name, map_name):
        """Returns a delete request to delete the specified QoS maps configuration"""
        url = f'{QOS_INTF_PATH}/interface={name}/openconfig-qos-maps-ext:interface-maps/config/{map_name}'
        request = {'path': url, 'method': DELETE}

        return request

    @staticmethod
    def get_delete_watchdog_request(name, attr):
        """Returns a delete request to delete the specified watchdog configuration"""
        url = f'{QOS_INTF_PATH}/interface={name}/pfc/watchdog/config/{attr}'
        request = {'path': url, 'method': DELETE}

        return request

    def remove_default_entries(self, data):
        """Removes default entries from the QoS interfaces data"""
        if data:
            intf_pop_list = []
            for idx, intf in enumerate(data):
                pfc = intf.get('pfc')
                if pfc:
                    asymmetric = pfc.get('asymmetric')
                    watchdog_action = pfc.get('watchdog_action')
                    priorities = pfc.get('priorities')

                    if asymmetric is False:
                        pfc.pop('asymmetric')
                    if watchdog_action == 'drop':
                        pfc.pop('watchdog_action')
                    if priorities:
                        priority_pop_list = []
                        for priority_idx, priority in enumerate(priorities):
                            enable = priority.get('enable')

                            if enable is False:
                                priority_pop_list.insert(0, priority_idx)

                        for priority_idx in priority_pop_list:
                            priorities.pop(priority_idx)

                        if not priorities:
                            pfc.pop('priorities')
                    if not pfc:
                        intf.pop('pfc')

                cable_length = intf.get('cable_length')
                if cable_length == '40m':
                    intf.pop('cable_length')

                if 'name' in intf and (len(intf) == 1 or intf['name'] == 'CPU'):
                    intf_pop_list.insert(0, idx)

            for idx in intf_pop_list:
                data.pop(idx)

    @staticmethod
    def sort_lists_in_config(config):
        """Sorts the lists in QoS interfaces configuration"""
        if config:
            config.sort(key=lambda x: x['name'])
            for intf in config:
                if 'queues' in intf and intf['queues']:
                    intf['queues'].sort(key=lambda x: x['id'])
                if 'pfc' in intf and intf['pfc'] and 'priorities' in intf['pfc'] and intf['pfc']['priorities']:
                    intf['pfc']['priorities'].sort(key=lambda x: x['dot1p'])

    def post_process_generated_config(self, configs):
        """Handle post processing for generated configuration"""
        for conf in configs:
            if conf.get('cable_length') is None:
                conf['cable_length'] = '40m'
            if 'queues' in conf and not conf['queues']:
                conf.pop('queues')
