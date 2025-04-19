#
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_ars class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from __future__ import absolute_import, division, print_function
__metaclass__ = type

from copy import deepcopy
from ansible.module_utils.connection import ConnectionError
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import Facts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    get_diff,
    remove_empties,
    update_states
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    edit_config,
    to_request
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.formatted_diff_utils import (
    get_new_config,
    get_formatted_config_diff
)

ARS_PATH = 'data/openconfig-system:system/openconfig-system-ext:adaptive-routing-switching'
PATCH = 'patch'
DELETE = 'delete'
is_delete_all = False
is_replaced = False
TEST_KEYS = [
    {'ars_objects': {'name': ''}},
    {'port_bindings': {'name': ''}},
    {'port_profiles': {'name': ''}},
    {'profiles': {'name': ''}},
    {'switch_bindings': {'name': ''}}
]
enum_dict = {
    0.0: '0',
    1.0: '1',
    2.5: '2.5',
    4.0: '4',
    5.0: '5',
    10.0: '10',
    20.0: '20',
    40.0: '40',
    80.0: '80',
    'fixed': 'ARS_MODE_FIXED',
    'flowlet_quality': 'ARS_MODE_FLOWLET_QUALITY',
    'flowlet_random': 'ARS_MODE_FLOWLET_RANDOM',
    'packet_quality': 'ARS_MODE_PER_PACKET_QUALITY',
    'packet_random': 'ARS_MODE_PER_PACKET_RANDOM'
}
default_entries = {
    'algo': 'EWMA',
    'enable': False,
    'idle_time': 80,
    'load_current_max_val': 6291456,
    'load_current_min_val': 1048576,
    'load_future_max_val': 12582912,
    'load_future_min_val': 2097152,
    'load_future_weight': 10,
    'load_past_max_val': 6000,
    'load_past_min_val': 3000,
    'load_past_weight': 80,
    'load_scaling_factor': 0.0,
    'max_flows': 256,
    'mode': 'flowlet_quality',
    'port_load_current': False,
    'port_load_exponent': 2,
    'port_load_future': True,
    'port_load_future_weight': 2,
    'port_load_past': True,
    'port_load_past_weight': 2,
    'random_seed': 10,
    'sampling_interval': 16,

}


class Ars(ConfigBase):
    """
    The sonic_ars class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'ars',
    ]

    def __init__(self, module):
        super(Ars, self).__init__(module)

    def get_ars_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        ars_facts = facts['ansible_network_resources'].get('ars')
        if not ars_facts:
            return {}
        return ars_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        commands = []

        existing_ars_facts = self.get_ars_facts()
        commands, requests = self.set_config(existing_ars_facts)
        if commands and len(requests) > 0:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        result['before'] = existing_ars_facts
        old_config = existing_ars_facts
        if self._module.check_mode:
            new_config = self.get_new_config(commands, existing_ars_facts)
            self.sort_lists_dicts_in_config(new_config)
            result['after(generated)'] = new_config
        else:
            new_config = self.get_ars_facts()
            if result['changed']:
                result['after'] = new_config
        if self._module._diff:
            self.sort_lists_dicts_in_config(new_config)
            self.sort_lists_dicts_in_config(old_config)
            result['diff'] = get_formatted_config_diff(old_config, new_config, self._module._verbosity)

        return result

    def set_config(self, existing_ars_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = remove_empties(self._module.params['config'])
        have = existing_ars_facts
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

        if state == 'merged':
            commands, requests = self._state_merged(diff)
        elif state == 'replaced':
            commands, requests = self._state_replaced(want, have, diff)
        elif state == 'overridden':
            commands, requests = self._state_overridden(want, have, diff)
        elif state == 'deleted':
            commands, requests = self._state_deleted(want, have, diff)
        return commands, requests

    def _state_replaced(self, want, have, diff):
        """ The command generator when state is replaced

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        mod_commands = None
        replaced_config, requests = self.get_replaced_config(want, have)
        global is_replaced
        is_replaced = False

        if replaced_config:
            is_replaced = True
            commands.extend(update_states(replaced_config, 'deleted'))
            mod_commands = want
        else:
            mod_commands = diff

        if mod_commands:
            mod_request = self.get_modify_ars_request(mod_commands)

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
        commands = []
        requests = []
        mod_commands = None
        mod_request = None
        global is_delete_all
        is_delete_all = False
        self.add_default_entries(want)
        del_commands = get_diff(have, want, TEST_KEYS)

        if not del_commands and diff:
            mod_commands = diff
            mod_request = self.get_modify_ars_request(mod_commands)

        if del_commands:
            is_delete_all = True
            del_requests = self.get_delete_ars_requests(del_commands, is_delete_all)
            requests.extend(del_requests)
            commands.extend(update_states(have, 'deleted'))
            mod_commands = want
            mod_request = self.get_modify_ars_request(mod_commands)

        if mod_request:
            requests.append(mod_request)
            commands.extend(update_states(mod_commands, 'overridden'))

        return commands, requests

    def _state_merged(self, diff):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = diff
        requests = self.get_modify_ars_request(commands)

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
        global is_delete_all
        is_delete_all = False
        requests = []

        if not want:
            commands = deepcopy(have)
            is_delete_all = True
        else:
            commands = get_diff(want, diff, TEST_KEYS)
            self.remove_default_entries(commands)

        if commands:
            requests = self.get_delete_ars_requests(commands, is_delete_all)
            if len(requests) > 0:
                commands = update_states(commands, 'deleted')
        else:
            commands = []

        return commands, requests

    def get_modify_ars_request(self, commands):
        """This method returns a patch request generated from commands"""
        request = None

        if commands:
            ars_dict = {}
            if commands.get('profiles'):
                profile_list = []
                for profile in commands['profiles']:
                    profile_list.append({'name': profile['name'], 'config': self.get_renamed_dict(profile)})
                if profile_list:
                    ars_dict['ars-profile'] = {'profile': profile_list}

            if commands.get('switch_bindings'):
                switchbind_list = []
                for bind in commands['switch_bindings']:
                    switchbind_list.append({'name': bind['name'], 'config': bind})
                if switchbind_list:
                    ars_dict['ars-switch-bind'] = {'switchbind': switchbind_list}

            if commands.get('port_profiles'):
                portprofile_list = []
                for profile in commands['port_profiles']:
                    profile_dict = self.get_renamed_dict(profile)
                    if profile_dict.get('load-scaling-factor') is not None:
                        profile_dict['load-scaling-factor'] = enum_dict[profile_dict['load-scaling-factor']]
                    portprofile_list.append({'name': profile['name'], 'config': profile_dict})
                if portprofile_list:
                    ars_dict['ars-port-profile'] = {'portprofile': portprofile_list}

            if commands.get('port_bindings'):
                portbind_list = []
                for bind in commands['port_bindings']:
                    portbind_list.append({'name': bind['name'], 'config': bind})
                if portbind_list:
                    ars_dict['ars-port-bind'] = {'portbind': portbind_list}

            if commands.get('ars_objects'):
                arsobject_list = []
                for obj in commands['ars_objects']:
                    obj_dict = self.get_renamed_dict(obj)
                    if obj_dict.get('mode'):
                        obj_dict['mode'] = enum_dict[obj_dict['mode']]
                    arsobject_list.append({'name': obj_dict['name'], 'config': obj_dict})
                if arsobject_list:
                    ars_dict['ars-object'] = {'arsobject': arsobject_list}

            if ars_dict:
                payload = {'openconfig-system-ext:adaptive-routing-switching': ars_dict}
                request = {'path': ARS_PATH, 'method': PATCH, 'data': payload}

        return request

    def get_renamed_dict(self, cfg_dict):
        """This method renames the keys in a dictionary by replacing underscores with hyphens"""
        renamed_dict = {}
        for key in cfg_dict:
            new_key = key.replace('_', '-')
            renamed_dict[new_key] = cfg_dict[key]

        return renamed_dict

    def get_delete_ars_requests(self, commands, delete_all):
        """This method returns a list of delete requests generated from commands"""
        requests = []

        if not commands:
            return requests
        if delete_all:
            requests.append({'path': ARS_PATH, 'method': DELETE})
            return requests

        if commands.get('ars_objects'):
            for obj in commands['ars_objects']:
                name = obj['name']
                if len(obj) == 1:
                    requests.append(self.get_delete_ars_object(name))
                    continue
                if obj.get('idle_time'):
                    requests.append(self.get_delete_ars_object(name, 'idle-time'))
                if obj.get('max_flows'):
                    requests.append(self.get_delete_ars_object(name, 'max-flows'))
                if obj.get('mode'):
                    requests.append(self.get_delete_ars_object(name, 'mode'))

        if commands.get('port_bindings'):
            for bind in commands['port_bindings']:
                name = bind['name']
                if len(bind) == 1:
                    requests.append(self.get_delete_port_bind(name))
                    continue
                if bind.get('profile'):
                    requests.append(self.get_delete_port_bind(name, 'profile'))

        if commands.get('switch_bindings'):
            for bind in commands['switch_bindings']:
                name = bind['name']
                if len(bind) == 1:
                    requests.append(self.get_delete_switch_bind(name))
                    continue
                if bind.get('profile'):
                    requests.append(self.get_delete_switch_bind(name, 'profile'))

        if commands.get('port_profiles'):
            for profile in commands.get('port_profiles'):
                name = profile['name']
                if len(profile) == 1:
                    requests.append(self.get_delete_port_profile(name))
                    continue
                if profile.get('enable') is not None:
                    requests.append(self.get_delete_port_profile(name, 'enable'))
                if profile.get('load_future_weight'):
                    requests.append(self.get_delete_port_profile(name, 'load-future-weight'))
                if profile.get('load_past_weight') is not None:
                    requests.append(self.get_delete_port_profile(name, 'load-past-weight'))
                if profile.get('load_scaling_factor') is not None:
                    requests.append(self.get_delete_port_profile(name, 'load-scaling-factor'))

        if commands.get('profiles'):
            for profile in commands.get('profiles'):
                name = profile['name']
                if len(profile) == 1:
                    requests.append(self.get_delete_profile(name))
                    continue
                if profile.get('algo'):
                    requests.append(self.get_delete_profile(name, 'algo'))
                if profile.get('load_current_max_val') is not None:
                    requests.append(self.get_delete_profile(name, 'load-current-max-val'))
                if profile.get('load_current_min_val') is not None:
                    requests.append(self.get_delete_profile(name, 'load-current-min-val'))
                if profile.get('load_future_max_val') is not None:
                    requests.append(self.get_delete_profile(name, 'load-future-max-val'))
                if profile.get('load_future_min_val') is not None:
                    requests.append(self.get_delete_profile(name, 'load-future-min-val'))
                if profile.get('load_past_max_val') is not None:
                    requests.append(self.get_delete_profile(name, 'load-past-max-val'))
                if profile.get('load_past_min_val') is not None:
                    requests.append(self.get_delete_profile(name, 'load-past-min-val'))
                if profile.get('port_load_current') is not None:
                    requests.append(self.get_delete_profile(name, 'port-load-current'))
                if profile.get('port_load_exponent'):
                    requests.append(self.get_delete_profile(name, 'port-load-exponent'))
                if profile.get('port_load_future') is not None:
                    requests.append(self.get_delete_profile(name, 'port-load-future'))
                if profile.get('port_load_future_weight'):
                    requests.append(self.get_delete_profile(name, 'port-load-future-weight'))
                if profile.get('port_load_past') is not None:
                    requests.append(self.get_delete_profile(name, 'port-load-past'))
                if profile.get('port_load_past_weight'):
                    requests.append(self.get_delete_profile(name, 'port-load-past-weight'))
                if profile.get('random_seed') is not None:
                    requests.append(self.get_delete_profile(name, 'random-seed'))
                if profile.get('sampling_interval'):
                    requests.append(self.get_delete_profile(name, 'sampling-interval'))

        return requests

    def get_delete_ars_object(self, name=None, attr=None):
        url = '%s/ars-object' % (ARS_PATH)
        if name:
            url += '/arsobject=%s' % (name)
        if attr:
            url += '/config/%s' % (attr)
        request = {'path': url, 'method': DELETE}
        return request

    def get_delete_port_bind(self, name=None, attr=None):
        url = '%s/ars-port-bind' % (ARS_PATH)
        if name:
            url += '/portbind=%s' % (name)
        if attr:
            url += '/config/%s' % (attr)
        request = {'path': url, 'method': DELETE}
        return request

    def get_delete_port_profile(self, name=None, attr=None):
        url = '%s/ars-port-profile' % (ARS_PATH)
        if name:
            url += '/portprofile=%s' % (name)
        if attr:
            url += '/config/%s' % (attr)
        request = {'path': url, 'method': DELETE}
        return request

    def get_delete_profile(self, name=None, attr=None):
        url = '%s/ars-profile' % (ARS_PATH)
        if name:
            url += '/profile=%s' % (name)
        if attr:
            url += '/config/%s' % (attr)
        request = {'path': url, 'method': DELETE}
        return request

    def get_delete_switch_bind(self, name=None, attr=None):
        url = '%s/ars-switch-bind' % (ARS_PATH)
        if name:
            url += '/switchbind=%s' % (name)
        if attr:
            url += '/config/%s' % (attr)
        request = {'path': url, 'method': DELETE}
        return request

    def sort_lists_dicts_in_config(self, config):
        """This method sorts the lists and dicts in the ARS configuration"""
        if config:
            if config.get('ars_objects'):
                dict_list = []
                for obj in config['ars_objects']:
                    dict_list.append(dict(sorted(obj.items())))
                dict_list.sort(key=lambda x: x['name'])
                config['ars_objects'] = dict_list
            if config.get('port_bindings'):
                dict_list = []
                for bind in config['port_bindings']:
                    dict_list.append(dict(sorted(bind.items())))
                dict_list.sort(key=lambda x: x['name'])
                config['port_bindings'] = dict_list
            if config.get('port_profiles'):
                dict_list = []
                for profile in config['port_profiles']:
                    dict_list.append(dict(sorted(profile.items())))
                dict_list.sort(key=lambda x: x['name'])
                config['port_profiles'] = dict_list
            if config.get('profiles'):
                dict_list = []
                for profile in config['profiles']:
                    dict_list.append(dict(sorted(profile.items())))
                dict_list.sort(key=lambda x: x['name'])
                config['profiles'] = dict_list
            if config.get('switch_bindings'):
                dict_list = []
                for bind in config['switch_bindings']:
                    dict_list.append(dict(sorted(bind.items())))
                dict_list.sort(key=lambda x: x['name'])
                config['switch_bindings'] = dict_list

    def remove_default_entries(self, data):
        """This method removes the default entries from the ARS configuration"""

        if data:
            ars_lists = ['ars_objects', 'port_profiles', 'profiles']
            for ars_list in ars_lists:
                if data.get(ars_list):
                    pop_list = []
                    for ars_dict in data[ars_list]:
                        if len(ars_dict) == 1:
                            continue
                        key_pop_list = []
                        for key in ars_dict:
                            if key not in default_entries:
                                continue
                            if ars_dict[key] == default_entries[key]:
                                key_pop_list.append(key)
                        for key in key_pop_list:
                            ars_dict.pop(key)
                        if len(ars_dict) == 1:
                            idx = data[ars_list].index(ars_dict)
                            pop_list.insert(0, idx)
                    for idx in pop_list:
                        data[ars_list].pop(idx)
                    if not data[ars_list]:
                        data.pop(ars_list)

    def add_default_entries(self, data):
        """This method adds the default entries to the ARS configuration"""

        if data.get('ars_objects'):
            for obj in data['ars_objects']:
                if 'idle_time' not in obj:
                    obj['idle_time'] = 80
                if 'max_flows' not in obj:
                    obj['max_flows'] = 256
                if 'mode' not in obj:
                    obj['mode'] = 'flowlet_quality'
        if data.get('port_profiles'):
            for profile in data['port_profiles']:
                if 'enable' not in profile:
                    profile['enable'] = False
                if 'load_future_weight' not in profile:
                    profile['load_future_weight'] = 10
                if 'load_past_weight' not in profile:
                    profile['load_past_weight'] = 80
                if 'load_scaling_factor' not in profile:
                    profile['load_scaling_factor'] = 0.0
        if data.get('profiles'):
            for profile in data['profiles']:
                if 'algo' not in profile:
                    profile['algo'] = 'EWMA'
                if 'load_current_max_val' not in profile:
                    profile['load_current_max_val'] = 6291456
                if 'load_current_min_val' not in profile:
                    profile['load_current_min_val'] = 1048576
                if 'load_future_max_val' not in profile:
                    profile['load_future_max_val'] = 12582912
                if 'load_future_min_val' not in profile:
                    profile['load_future_min_val'] = 2097152
                if 'load_past_max_val' not in profile:
                    profile['load_past_max_val'] = 6000
                if 'load_past_min_val' not in profile:
                    profile['load_past_min_val'] = 3000
                if 'port_load_current' not in profile:
                    profile['port_load_current'] = False
                if 'port_load_exponent' not in profile:
                    profile['port_load_exponent'] = 2
                if 'port_load_future' not in profile:
                    profile['port_load_future'] = True
                if 'port_load_future_weight' not in profile:
                    profile['port_load_future_weight'] = 2
                if 'port_load_past' not in profile:
                    profile['port_load_past'] = True
                if 'port_load_past_weight' not in profile:
                    profile['port_load_past_weight'] = 2
                if 'random_seed' not in profile:
                    profile['random_seed'] = 10
                if 'sampling_interval' not in profile:
                    profile['sampling_interval'] = 16

    def get_replaced_config(self, want, have):
        """This method returns the ARS configuration to be deleted and the respective delete requests"""

        config_dict = {}
        requests = []
        new_want = deepcopy(want)
        self.add_default_entries(new_want)
        diff = get_diff(have, new_want, TEST_KEYS)

        if diff.get('ars_objects'):
            requests.append(self.get_delete_ars_object())
            config_dict['ars_objects'] = have['ars_objects']
        if diff.get('port_bindings'):
            requests.append(self.get_delete_port_bind())
            config_dict['port_bindings'] = have['port_bindings']
        if diff.get('switch_bindings'):
            requests.append(self.get_delete_switch_bind())
            config_dict['switch_bindings'] = have['switch_bindings']
        if diff.get('port_profiles'):
            requests.append(self.get_delete_port_profile())
            config_dict['port_profiles'] = have['port_profiles']
        if diff.get('profiles'):
            requests.append(self.get_delete_profile())
            config_dict['profiles'] = have['profiles']

        return config_dict, requests

    def __derive_ars_delete_op(self, key_set, command, exist_conf):
        """Returns new ARS configuration on delete operation"""
        if is_delete_all:
            return True, {}

        new_conf = exist_conf

        for ars_list in command:
            if is_replaced:
                new_conf.pop(ars_list)
                continue
            pop_list = []
            for ars_dict in command[ars_list]:
                idx = command[ars_list].index(ars_dict)
                if len(ars_dict) == 1:
                    pop_list.insert(0, idx)
                    continue
                for key in ars_dict:
                    if key == 'name':
                        continue
                    if key in default_entries:
                        new_conf[ars_list][idx][key] = default_entries[key]
                    else:
                        new_conf[ars_list][idx].pop(key)
            for idx in pop_list:
                new_conf[ars_list].pop(idx)
            if not new_conf[ars_list]:
                new_conf.pop(ars_list)

        return True, new_conf

    def get_new_config(self, commands, have):
        """Returns generated configuration based on commands and
            existing configuration"""
        key_set = [
            {'config': {'__delete_op': self.__derive_ars_delete_op}},
            {'ars_objects': {'name': ''}},
            {'port_bindings': {'name': ''}},
            {'port_profiles': {'name': ''}},
            {'profiles': {'name': ''}},
            {'switch_bindings': {'name': ''}},
        ]
        new_config = get_new_config(commands, have, key_set)
        self.add_default_entries(new_config)

        return new_config
