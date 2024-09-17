#
# -*- coding: utf-8 -*-
# Copyright 2024 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_qos_buffer class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.connection import ConnectionError
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    get_diff,
    remove_empties,
    update_states
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.formatted_diff_utils import (
    __DELETE_CONFIG_IF_NO_SUBCONFIG,
    get_new_config,
    get_formatted_config_diff
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import Facts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)

from copy import deepcopy


QOS_BUFFER_PATH = '/data/openconfig-qos:qos/openconfig-qos-buffer:buffer'
PATCH = 'patch'
DELETE = 'delete'
TEST_KEYS = [
    {'buffer_pools': {'name': ''}},
    {'buffer_profiles': {'name': ''}}
]
TEST_KEYS_formatted_diff = [
    {'buffer_pools': {'name': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}},
    {'buffer_profiles': {'name': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}}
]


class Qos_buffer(ConfigBase):
    """
    The sonic_qos_buffer class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'qos_buffer',
    ]

    def __init__(self, module):
        super(Qos_buffer, self).__init__(module)

    def get_qos_buffer_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        qos_buffer_facts = facts['ansible_network_resources'].get('qos_buffer')
        if not qos_buffer_facts:
            return []
        return qos_buffer_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = []
        commands = []

        existing_qos_buffer_facts = self.get_qos_buffer_facts()
        commands, requests = self.set_config(existing_qos_buffer_facts)
        if commands and len(requests) > 0:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        changed_qos_buffer_facts = self.get_qos_buffer_facts()

        result['before'] = existing_qos_buffer_facts
        if result['changed']:
            result['after'] = changed_qos_buffer_facts

        new_config = changed_qos_buffer_facts
        old_config = existing_qos_buffer_facts
        if self._module.check_mode:
            result.pop('after', None)
            new_config = get_new_config(commands, existing_qos_buffer_facts,
                                        TEST_KEYS_formatted_diff)
            result['after(generated)'] = new_config
        if self._module._diff:
            self.sort_lists_in_config(new_config)
            self.sort_lists_in_config(old_config)
            result['diff'] = get_formatted_config_diff(old_config,
                                                       new_config,
                                                       self._module._verbosity)

        result['warnings'] = warnings
        return result

    def set_config(self, existing_qos_buffer_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']
        have = existing_qos_buffer_facts
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
        diff = get_diff(want, have, TEST_KEYS)

        if state == 'deleted':
            commands, requests = self._state_deleted(want, have)
        elif state == 'merged':
            commands, requests = self._state_merged(diff)
        elif state == 'overridden':
            self._module.fail_json(msg='Overridden state not supported for this module')
        elif state == 'replaced':
            self._module.fail_json(msg='Replaced state not supported for this module')

        return commands, requests

    def _state_merged(self, diff):
        """ The command generator when state is merged
        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = diff
        requests = self.get_modify_qos_buffer_request(commands)

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
        want = remove_empties(want)

        if not want:
            commands = deepcopy(have)
            is_delete_all = True
        else:
            commands = deepcopy(want)

        requests = self.get_delete_qos_buffer_requests(commands, have, is_delete_all)

        if commands and len(requests) > 0:
            commands = update_states(commands, "deleted")
        else:
            commands = []
        return commands, requests

    def get_modify_qos_buffer_request(self, commands):
        request = None
        buffer_dict = {}
        buffer_pools = commands.get('buffer_pools')
        buffer_profiles = commands.get('buffer_profiles')

        if buffer_pools:
            buffer_pool_list = []
            for pool in buffer_pools:
                config_dict = {}
                name = pool.get('name')
                xoff = pool.get('xoff')

                if name:
                    config_dict['name'] = name
                if xoff:
                    config_dict['xoff'] = str(xoff)
                if config_dict:
                    buffer_pool_list.append({'name': name, 'config': config_dict})

            if buffer_pool_list:
                buffer_dict['buffer-pools'] = {'buffer-pool': buffer_pool_list}

        if buffer_profiles:
            buffer_profile_list = []
            for profile in buffer_profiles:
                config_dict = {}
                name = profile.get('name')
                pool = profile.get('pool')
                size = profile.get('size')
                static_threshold = profile.get('static_threshold')
                dynamic_threshold = profile.get('dynamic_threshold')
                pause_threshold = profile.get('pause_threshold')

                if name:
                    config_dict['name'] = name
                if pool:
                    config_dict['pool'] = pool
                if size:
                    config_dict['size'] = str(size)
                if static_threshold:
                    config_dict['static-threshold'] = str(static_threshold)
                if dynamic_threshold:
                    config_dict['dynamic-threshold'] = dynamic_threshold
                if pause_threshold:
                    config_dict['pause-threshold'] = str(pause_threshold)
                if config_dict:
                    buffer_profile_list.append({'name': name, 'config': config_dict})

            if buffer_profile_list:
                buffer_dict['buffer-profiles'] = {'buffer-profile': buffer_profile_list}

        if buffer_dict:
            payload = {'openconfig-qos-buffer:buffer': buffer_dict}
            request = {'path': QOS_BUFFER_PATH, 'method': PATCH, 'data': payload}

        return request

    def get_delete_qos_buffer_requests(self, commands, have, is_delete_all):
        requests = []

        if not commands:
            return requests

        if is_delete_all:
            self._module.fail_json(msg='Deletion of all QoS buffer configuration not supported')

        buffer_pools = commands.get('buffer_pools')
        if buffer_pools:
            self._module.fail_json(msg='Deletion of QoS buffer pool configuration not supported')

        buffer_profiles = commands.get('buffer_profiles')
        if buffer_profiles:
            profile_list = []
            for profile in buffer_profiles:
                name = profile.get('name')
                pool = profile.get('pool')
                size = profile.get('size')
                static_threshold = profile.get('static_threshold')
                dynamic_threshold = profile.get('dynamic_threshold')
                pause_threshold = profile.get('pause_threshold')

                cfg_buffer_profiles = have.get('buffer_profiles')
                if cfg_buffer_profiles:
                    for cfg_profile in cfg_buffer_profiles:
                        profile_dict = {}
                        cfg_name = cfg_profile.get('name')
                        if name != cfg_name:
                            continue
                        cfg_pool = cfg_profile.get('pool')
                        cfg_size = cfg_profile.get('size')
                        cfg_static_threshold = cfg_profile.get('static_threshold')
                        cfg_dynamic_threshold = cfg_profile.get('dynamic_threshold')
                        cfg_pause_threshold = cfg_profile.get('pause_threshold')

                        if pool:
                            self._module.fail_json(msg='Mandatory attribute pool cannot be deleted')
                        if size:
                            self._module.fail_json(msg='Mandatory attribute size cannot be deleted')
                        if static_threshold and static_threshold == cfg_static_threshold:
                            requests.append(self.get_delete_buffer_profile_attr(name, 'static-threshold'))
                            profile_dict.update({'name': name, 'static_threshold': static_threshold})
                        if dynamic_threshold and dynamic_threshold == cfg_dynamic_threshold:
                            requests.append(self.get_delete_buffer_profile_attr(name, 'dynamic-threshold'))
                            profile_dict.update({'name': name, 'dynamic_threshold': dynamic_threshold})
                        if pause_threshold and pause_threshold == cfg_pause_threshold:
                            requests.append(self.get_delete_buffer_profile_attr(name, 'pause-threshold'))
                            profile_dict.update({'name': name, 'pause_threshold': pause_threshold})
                        if not pool and not size and not static_threshold and not dynamic_threshold and not pause_threshold:
                            requests.append(self.get_delete_buffer_profile(name))
                            profile_dict.update({'name': name})
                        if profile_dict:
                            profile_list.append(profile_dict)
            if profile_list:
                commands['buffer_profiles'] = profile_list
            else:
                commands.pop('buffer_profiles')

        return requests

    def sort_lists_in_config(self, config):
        if config:
            if 'buffer_pools' in config and config['buffer_pools']:
                config['buffer_pools'].sort(key=lambda x: x['name'])
            if 'buffer_profiles' in config and config['buffer_profiles']:
                config['buffer_profiles'].sort(key=lambda x: x['name'])

    def get_delete_buffer_profile(self, name):
        url = '%s/buffer-profiles/buffer-profile=%s' % (QOS_BUFFER_PATH, name)
        request = {'path': url, 'method': DELETE}

        return request

    def get_delete_buffer_profile_attr(self, name, attr):
        url = '%s/buffer-profiles/buffer-profile=%s/config/%s' % (QOS_BUFFER_PATH, name, attr)
        request = {'path': url, 'method': DELETE}

        return request
