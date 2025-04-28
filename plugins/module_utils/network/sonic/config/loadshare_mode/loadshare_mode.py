#
# -*- coding: utf-8 -*-
# Copyright 2024 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_loadshare_mode
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
    get_replaced_config
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.formatted_diff_utils import (
    __DELETE_LEAFS_THEN_CONFIG_IF_NO_NON_KEY_LEAF,
    get_new_config,
    get_formatted_config_diff
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.loadshare_mode.loadshare_mode import (
    LOADSHARE_MODE_ATTR_MAP,
    LOADSHARE_MODE_DICT_MAP
)

PATCH = 'patch'
DELETE = 'delete'
URL = 'data/openconfig-loadshare-mode-ext:loadshare'


delete_all = False
TEST_KEYS_generate_config = [
    {'config': {'__delete_op': __DELETE_LEAFS_THEN_CONFIG_IF_NO_NON_KEY_LEAF}},
    {'ipv4': {'__delete_op': __DELETE_LEAFS_THEN_CONFIG_IF_NO_NON_KEY_LEAF}},
    {'ipv6': {'__delete_op': __DELETE_LEAFS_THEN_CONFIG_IF_NO_NON_KEY_LEAF}},
    {'hash_offset': {'__delete_op': __DELETE_LEAFS_THEN_CONFIG_IF_NO_NON_KEY_LEAF}}
]


class Loadshare_mode(ConfigBase):
    """
    The sonic_loadshare_mode class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'loadshare_mode',
    ]

    def __init__(self, module):
        super(Loadshare_mode, self).__init__(module)

    def get_loadshare_mode_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset,
                                                         self.gather_network_resources)
        loadshare_mode_facts = facts['ansible_network_resources'].get('loadshare_mode')
        if not loadshare_mode_facts:
            return {}
        return loadshare_mode_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = list()
        existing_loadshare_mode_facts = self.get_loadshare_mode_facts()
        commands, requests = self.set_config(existing_loadshare_mode_facts)
        if commands and len(requests) > 0:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        changed_loadshare_mode_facts = self.get_loadshare_mode_facts()

        result['before'] = existing_loadshare_mode_facts
        if result['changed']:
            result['after'] = changed_loadshare_mode_facts

        new_config = changed_loadshare_mode_facts
        old_config = existing_loadshare_mode_facts
        if self._module.check_mode:
            result.pop('after', None)
            new_config = get_new_config(commands, old_config,
                                        TEST_KEYS_generate_config)
            new_config = remove_empties(new_config)
            result['after(generated)'] = new_config

        if self._module._diff:
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

        commands = []
        requests = []

        want = remove_empties(want)
        if state == 'overridden':
            commands, requests = self._state_overridden(want, have)
        elif state == 'replaced':
            commands, requests = self._state_replaced(want, have)
        elif state == 'deleted':
            commands, requests = self._state_deleted(want, have)
        elif state == 'merged':
            commands, requests = self._state_merged(want, have)
        return commands, requests

    def _state_merged(self, want, have):
        """ The command generator when state is merged

        :param want: the additive configuration as a dictionary
        :param obj_in_have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = []
        diff = get_diff(want, have)
        command = diff
        requests = self.get_modify_loadshare_mode_requests(command, have)
        if command and len(requests) > 0:
            commands = update_states([command], "merged")
        else:
            commands = []

        return commands, requests

    def _state_deleted(self, want, have):
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

        requests = self.get_delete_loadshare_mode_requests(command, have, True, delete_all)

        if command and len(requests) > 0:
            commands = update_states([command], "deleted")

        return commands, requests

    def _state_replaced(self, want, have):
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
        self.preprocess_want(want, have)
        diff = get_diff(want, have)
        replaced_config = get_replaced_config(want, have)

        add_commands = []
        if replaced_config:
            del_requests = self.get_delete_loadshare_mode_requests(replaced_config, have)
            requests.extend(del_requests)
            commands.extend(update_states(replaced_config, "deleted"))
            add_commands = want
        else:
            add_commands = diff

        if add_commands:
            add_requests = self.get_modify_loadshare_mode_requests(add_commands, have)
            if len(add_requests) > 0:
                requests.extend(add_requests)
                commands.extend(update_states(add_commands, "replaced"))

        return commands, requests

    def _state_overridden(self, want, have):
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

        self.preprocess_want(want, have)
        diff = get_diff(want, have)
        r_diff = get_diff(have, want)
        if have and (diff or r_diff):
            del_requests = self.get_delete_loadshare_mode_requests(have, have, False, True)
            requests.extend(del_requests)
            commands.extend(update_states(have, "deleted"))
            have = []

        if not have and want:
            want_commands = want
            want_requests = self.get_modify_loadshare_mode_requests(want_commands, have)

            if len(want_requests) > 0:
                requests.extend(want_requests)
                commands.extend(update_states(want_commands, "overridden"))

        return commands, requests

    def get_modify_loadshare_mode_requests(self, command, have):
        requests = []
        if not command:
            return requests

        lsm_payload = dict()

        for amap in LOADSHARE_MODE_ATTR_MAP:
            ans_attr = amap['ans_attr']
            cfg_attr = amap['cfg_attr']
            cfg_subattr = amap['cfg_subattr']
            cfg_hash = amap.get('hash')

            cmd_attr = command.get(ans_attr, None)
            if cmd_attr is not None:
                lsm_payload[cfg_attr] = {'config': {cfg_subattr: cmd_attr}}
                if cfg_hash:
                    lsm_payload[cfg_attr]['config'].update(cfg_hash)

        for amap in LOADSHARE_MODE_DICT_MAP:
            ans_attr = amap['ans_attr']
            cfg_attr = amap['cfg_attr']
            cfg_hash = amap.get('hash')

            cmd_attrs = command.get(ans_attr, None)
            if cmd_attrs is not None:
                amap_subattrs = amap['map_subattrs']
                config = {}
                for amap_subattr in amap_subattrs:
                    ans_subattr = amap_subattr['ans_attr']
                    cfg_subattr = amap_subattr['cfg_attr']
                    cmd_subattr = cmd_attrs.get(ans_subattr, None)
                    if cmd_subattr is not None:
                        config.update({cfg_subattr: cmd_subattr})

                if config:
                    lsm_payload[cfg_attr] = {'config': config}
                    if cfg_hash:
                        lsm_payload[cfg_attr]['config'].update(cfg_hash)

        if lsm_payload:
            path = URL
            payload = {"openconfig-loadshare-mode-ext:loadshare": lsm_payload}
            request = {'path': path, 'method': PATCH, 'data': payload}
            requests.append(request)

        return requests

    def check_delete(self, cmd_attr, have_attr, ans_delete):
        # cmd_attr must not be None.
        del_attr = False
        if ans_delete:
            if isinstance(cmd_attr, bool):
                del_attr = cmd_attr and have_attr
            elif isinstance(cmd_attr, int) or isinstance(cmd_attr, str):
                del_attr = cmd_attr == have_attr
        else:
            if have_attr is not None:
                del_attr = True
        return del_attr

    def get_delete_loadshare_mode_requests(self, command, have, ans_delete=False, is_delete_all=False):
        requests = []
        if not command or not have:
            return requests

        if is_delete_all:
            path = URL
            request = {'path': path, 'method': DELETE}
            requests.append(request)

            if not ans_delete:
                request = self.get_patch_config_with_defaults_request(have)
                if request:
                    requests.append(request)

            return requests

        for amap in LOADSHARE_MODE_ATTR_MAP:
            ans_attr = amap['ans_attr']
            cfg_attr = amap['cfg_attr']

            cmd_attr = command.get(ans_attr, None)
            have_attr = have.get(ans_attr, None)

            if cmd_attr is not None:
                del_attr = self.check_delete(cmd_attr, have_attr, ans_delete)
                if del_attr:
                    path = URL + '/' + cfg_attr
                    request = {'path': path, 'method': DELETE}
                    requests.append(request)

        lsm_payload = dict()
        for amap in LOADSHARE_MODE_DICT_MAP:
            ans_attr = amap['ans_attr']
            cfg_attr = amap['cfg_attr']
            cfg_hash = amap.get('hash')
            del_op = amap['delete_op']

            cmd_attrs = command.get(ans_attr, {})
            have_attrs = have.get(ans_attr, {})
            if cmd_attrs:
                amap_subattrs = amap['map_subattrs']
                config = {}
                for amap_subattr in amap_subattrs:
                    ans_subattr = amap_subattr['ans_attr']
                    cfg_subattr = amap_subattr['cfg_attr']
                    cmd_subattr = cmd_attrs.get(ans_subattr, None)
                    have_subattr = have_attrs.get(ans_subattr, None)
                    if cmd_subattr is not None:
                        del_attr = self.check_delete(cmd_subattr, have_subattr, ans_delete)
                        if del_attr:
                            if del_op == 'DELETE':
                                path = URL + '/' + cfg_attr + '/config/' + cfg_subattr
                                request = {'path': path, 'method': DELETE}
                                requests.append(request)
                            else:
                                config.update({cfg_subattr: False})

                if config:
                    lsm_payload[cfg_attr] = {'config': config}
                    if cfg_hash:
                        lsm_payload[cfg_attr]['config'].update(cfg_hash)

        if lsm_payload:
            path = URL
            payload = {"openconfig-loadshare-mode-ext:loadshare": lsm_payload}
            request = {'path': path, 'method': PATCH, 'data': payload}
            requests.append(request)

        return requests

    def get_patch_config_with_defaults_request(self, have):

        request = dict()
        lsm_payload = dict()

        for attr in ['ipv4', 'ipv6']:
            have_attr = have.get(attr)
            if have_attr:
                config = {}
                attr_map = next((amap for amap in LOADSHARE_MODE_DICT_MAP if amap['ans_attr'] == attr), None)
                cfg_attr = attr_map['cfg_attr']
                cfg_hash = attr_map.get('hash')
                for amap_subattr in attr_map['map_subattrs']:
                    cfg_subattr = amap_subattr['cfg_attr']
                    attr_dft_value = amap_subattr['dft_value']
                    config.update({cfg_subattr: attr_dft_value})

                config.update(cfg_hash)
                lsm_payload[cfg_attr] = {'config': config}

        if lsm_payload:
            path = URL
            payload = {"openconfig-loadshare-mode-ext:loadshare": lsm_payload}
            request = {'path': path, 'method': PATCH, 'data': payload}

        return request

    def preprocess_want(self, want, have):

        for attr in ['ipv4', 'ipv6']:
            cmd_attr = want.get(attr)
            have_attr = have.get(attr)
            if cmd_attr and have_attr:
                attr_map = next((amap for amap in LOADSHARE_MODE_DICT_MAP if amap['ans_attr'] == attr), None)
                for amap_subattr in attr_map['map_subattrs']:
                    ans_subattr = amap_subattr['ans_attr']
                    attr_dft_value = amap_subattr['dft_value']
                    if not cmd_attr.get(ans_subattr) and have_attr.get(ans_subattr) == attr_dft_value:
                        cmd_attr[ans_subattr] = attr_dft_value
