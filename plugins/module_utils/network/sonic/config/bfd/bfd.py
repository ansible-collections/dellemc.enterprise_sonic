#
# -*- coding: utf-8 -*-
# Copyright 2023 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_bfd class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    get_diff,
    get_replaced_config,
    send_requests,
    remove_empties,
    update_states
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import Facts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)

from copy import deepcopy


BFD_PATH = '/data/openconfig-bfd:bfd'
PATCH = 'patch'
DELETE = 'delete'
TEST_KEYS = [
    {'profiles': {'profile_name': ''}},
    {'single_hops': {'remote_address': '', 'vrf': '', 'interface': '', 'local_address': ''}},
    {'multi_hops': {'remote_address': '', 'vrf': '', 'local_address': ''}}
]


class Bfd(ConfigBase):
    """
    The sonic_bfd class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'bfd',
    ]

    def __init__(self, module):
        super(Bfd, self).__init__(module)

    def get_bfd_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        bfd_facts = facts['ansible_network_resources'].get('bfd')
        if not bfd_facts:
            return {}
        return bfd_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = []
        commands = []

        existing_bfd_facts = self.get_bfd_facts()
        commands, requests = self.set_config(existing_bfd_facts)
        if commands and len(requests) > 0:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        changed_bfd_facts = self.get_bfd_facts()

        result['before'] = existing_bfd_facts
        if result['changed']:
            result['after'] = changed_bfd_facts

        result['warnings'] = warnings
        return result

    def set_config(self, existing_bfd_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']
        have = existing_bfd_facts
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

        if state == 'overridden':
            commands, requests = self._state_overridden(want, have)
        elif state == 'deleted':
            commands, requests = self._state_deleted(want, have)
        elif state == 'merged':
            commands, requests = self._state_merged(diff)
        elif state == 'replaced':
            commands, requests = self._state_replaced(want, have, diff)
        return commands, requests

    def _state_replaced(self, want, have, diff):
        """ The command generator when state is replaced
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        replaced_config = get_replaced_config(want, have, TEST_KEYS)

        if replaced_config:
            self.sort_lists_in_config(replaced_config)
            self.sort_lists_in_config(have)
            is_delete_all = (replaced_config == have)
            requests = self.get_delete_bfd_requests(replaced_config, have, is_delete_all)
            send_requests(self._module, requests)

            commands = want
        else:
            commands = diff

        requests = []

        if commands:
            requests = self.get_modify_bfd_request(commands)

            if len(requests) > 0:
                commands = update_states(commands, "replaced")
            else:
                commands = []
        else:
            commands = []

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
        self.sort_lists_in_config(want)
        self.sort_lists_in_config(have)

        if have and have != want:
            is_delete_all = True
            requests = self.get_delete_bfd_requests(have, None, is_delete_all)
            send_requests(self._module, requests)
            have = []

        commands = []
        requests = []

        if not have and want:
            commands = want
            requests = self.get_modify_bfd_request(commands)

            if len(requests) > 0:
                commands = update_states(commands, "overridden")
            else:
                commands = []

        return commands, requests

    def _state_merged(self, diff):
        """ The command generator when state is merged
        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = diff
        requests = self.get_modify_bfd_request(commands)

        if commands and len(requests) > 0:
            commands = update_states(commands, "merged")
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
        is_delete_all = False
        want = remove_empties(want)
        if not want:
            commands = deepcopy(have)
            is_delete_all = True
        else:
            commands = deepcopy(want)

        self.remove_default_entries(commands)
        requests = self.get_delete_bfd_requests(commands, have, is_delete_all)

        if commands and len(requests) > 0:
            commands = update_states(commands, "deleted")
        else:
            commands = []
        return commands, requests

    def get_modify_bfd_request(self, commands):
        request = None

        profiles = commands.get('profiles', None)
        single_hops = commands.get('single_hops', None)
        multi_hops = commands.get('multi_hops', None)
        bfd_dict = {}
        bfd_profile_dict = {}
        bfd_shop_dict = {}
        bfd_mhop_dict = {}

        if profiles:
            profile_list = []
            for profile in profiles:
                profile_dict = {}
                config_dict = {}
                profile_name = profile.get('profile_name', None)
                enabled = profile.get('enabled', None)
                transmit_interval = profile.get('transmit_interval', None)
                receive_interval = profile.get('receive_interval', None)
                detect_multiplier = profile.get('detect_multiplier', None)
                passive_mode = profile.get('passive_mode', None)
                min_ttl = profile.get('min_ttl', None)
                echo_interval = profile.get('echo_interval', None)
                echo_mode = profile.get('echo_mode', None)

                if profile_name:
                    profile_dict['profile-name'] = profile_name
                    config_dict['profile-name'] = profile_name
                if enabled is not None:
                    config_dict['enabled'] = enabled
                if transmit_interval:
                    config_dict['desired-minimum-tx-interval'] = transmit_interval
                if receive_interval:
                    config_dict['required-minimum-receive'] = receive_interval
                if detect_multiplier:
                    config_dict['detection-multiplier'] = detect_multiplier
                if passive_mode is not None:
                    config_dict['passive-mode'] = passive_mode
                if min_ttl:
                    config_dict['minimum-ttl'] = min_ttl
                if echo_interval:
                    config_dict['desired-minimum-echo-receive'] = echo_interval
                if echo_mode is not None:
                    config_dict['echo-active'] = echo_mode
                if config_dict:
                    profile_dict['config'] = config_dict
                    profile_list.append(profile_dict)
            if profile_list:
                bfd_profile_dict['profile'] = profile_list

        if single_hops:
            single_hop_list = []
            for hop in single_hops:
                hop_dict = {}
                config_dict = {}
                remote_address = hop.get('remote_address', None)
                vrf = hop.get('vrf', None)
                interface = hop.get('interface', None)
                local_address = hop.get('local_address', None)
                enabled = hop.get('enabled', None)
                transmit_interval = hop.get('transmit_interval', None)
                receive_interval = hop.get('receive_interval', None)
                detect_multiplier = hop.get('detect_multiplier', None)
                passive_mode = hop.get('passive_mode', None)
                echo_interval = hop.get('echo_interval', None)
                echo_mode = hop.get('echo_mode', None)
                profile_name = hop.get('profile_name', None)

                if remote_address:
                    hop_dict['remote-address'] = remote_address
                    config_dict['remote-address'] = remote_address
                if vrf:
                    hop_dict['vrf'] = vrf
                    config_dict['vrf'] = vrf
                if interface:
                    hop_dict['interface'] = interface
                    config_dict['interface'] = interface
                if local_address:
                    hop_dict['local-address'] = local_address
                    config_dict['local-address'] = local_address
                if enabled is not None:
                    config_dict['enabled'] = enabled
                if transmit_interval:
                    config_dict['desired-minimum-tx-interval'] = transmit_interval
                if receive_interval:
                    config_dict['required-minimum-receive'] = receive_interval
                if detect_multiplier:
                    config_dict['detection-multiplier'] = detect_multiplier
                if passive_mode is not None:
                    config_dict['passive-mode'] = passive_mode
                if echo_interval:
                    config_dict['desired-minimum-echo-receive'] = echo_interval
                if echo_mode is not None:
                    config_dict['echo-active'] = echo_mode
                if profile_name:
                    config_dict['profile-name'] = profile_name
                if config_dict:
                    hop_dict['config'] = config_dict
                    single_hop_list.append(hop_dict)
            if single_hop_list:
                bfd_shop_dict['single-hop'] = single_hop_list

        if multi_hops:
            multi_hop_list = []
            for hop in multi_hops:
                hop_dict = {}
                config_dict = {}
                remote_address = hop.get('remote_address', None)
                vrf = hop.get('vrf', None)
                local_address = hop.get('local_address', None)
                enabled = hop.get('enabled', None)
                transmit_interval = hop.get('transmit_interval', None)
                receive_interval = hop.get('receive_interval', None)
                detect_multiplier = hop.get('detect_multiplier', None)
                passive_mode = hop.get('passive_mode', None)
                min_ttl = hop.get('min_ttl', None)
                profile_name = hop.get('profile_name', None)

                if remote_address:
                    hop_dict['remote-address'] = remote_address
                    config_dict['remote-address'] = remote_address
                if vrf:
                    hop_dict['vrf'] = vrf
                    config_dict['vrf'] = vrf
                if local_address:
                    hop_dict['local-address'] = local_address
                    config_dict['local-address'] = local_address
                if enabled is not None:
                    config_dict['enabled'] = enabled
                if transmit_interval:
                    config_dict['desired-minimum-tx-interval'] = transmit_interval
                if receive_interval:
                    config_dict['required-minimum-receive'] = receive_interval
                if detect_multiplier:
                    config_dict['detection-multiplier'] = detect_multiplier
                if passive_mode is not None:
                    config_dict['passive-mode'] = passive_mode
                if min_ttl:
                    config_dict['minimum-ttl'] = min_ttl
                if profile_name:
                    config_dict['profile-name'] = profile_name
                if config_dict:
                    config_dict['interface'] = 'null'
                    hop_dict['interface'] = 'null'
                    hop_dict['config'] = config_dict
                    multi_hop_list.append(hop_dict)
            if multi_hop_list:
                bfd_mhop_dict['multi-hop'] = multi_hop_list

        if bfd_profile_dict:
            bfd_dict['openconfig-bfd-ext:bfd-profile'] = bfd_profile_dict
        if bfd_shop_dict:
            bfd_dict['openconfig-bfd-ext:bfd-shop-sessions'] = bfd_shop_dict
        if bfd_mhop_dict:
            bfd_dict['openconfig-bfd-ext:bfd-mhop-sessions'] = bfd_mhop_dict
        if bfd_dict:
            payload = {'openconfig-bfd:bfd': bfd_dict}
            request = {'path': BFD_PATH, 'method': PATCH, 'data': payload}

        return request

    def get_delete_bfd_requests(self, commands, have, is_delete_all):
        requests = []

        if not commands:
            return requests

        if is_delete_all:
            requests.extend(self.get_delete_all_bfd_cfg_requests(commands))
        else:
            requests.extend(self.get_delete_bfd_profile_requests(commands, have))
            requests.extend(self.get_delete_bfd_shop_requests(commands, have))
            requests.extend(self.get_delete_bfd_mhop_requests(commands, have))

        return requests

    def get_delete_bfd_profile_requests(self, commands, have):
        requests = []

        profiles = commands.get('profiles', None)
        if profiles:
            for profile in profiles:
                profile_name = profile.get('profile_name', None)
                enabled = profile.get('enabled', None)
                transmit_interval = profile.get('transmit_interval', None)
                receive_interval = profile.get('receive_interval', None)
                detect_multiplier = profile.get('detect_multiplier', None)
                passive_mode = profile.get('passive_mode', None)
                min_ttl = profile.get('min_ttl', None)
                echo_interval = profile.get('echo_interval', None)
                echo_mode = profile.get('echo_mode', None)

                cfg_profiles = have.get('profiles', None)
                if cfg_profiles:
                    for cfg_profile in cfg_profiles:
                        cfg_profile_name = cfg_profile.get('profile_name', None)
                        cfg_enabled = cfg_profile.get('enabled', None)
                        cfg_transmit_interval = cfg_profile.get('transmit_interval', None)
                        cfg_receive_interval = cfg_profile.get('receive_interval', None)
                        cfg_detect_multiplier = cfg_profile.get('detect_multiplier', None)
                        cfg_passive_mode = cfg_profile.get('passive_mode', None)
                        cfg_min_ttl = cfg_profile.get('min_ttl', None)
                        cfg_echo_interval = cfg_profile.get('echo_interval', None)
                        cfg_echo_mode = cfg_profile.get('echo_mode', None)

                        if profile_name == cfg_profile_name:
                            if enabled is not None and enabled == cfg_enabled:
                                requests.append(self.get_delete_profile_attr_request(profile_name, 'enabled'))
                            if transmit_interval and transmit_interval == cfg_transmit_interval:
                                requests.append(self.get_delete_profile_attr_request(profile_name, 'desired-minimum-tx-interval'))
                            if receive_interval and receive_interval == cfg_receive_interval:
                                requests.append(self.get_delete_profile_attr_request(profile_name, 'required-minimum-receive'))
                            if detect_multiplier and detect_multiplier == cfg_detect_multiplier:
                                requests.append(self.get_delete_profile_attr_request(profile_name, 'detection-multiplier'))
                            if passive_mode is not None and passive_mode == cfg_passive_mode:
                                requests.append(self.get_delete_profile_attr_request(profile_name, 'passive-mode'))
                            if min_ttl and min_ttl == cfg_min_ttl:
                                requests.append(self.get_delete_profile_attr_request(profile_name, 'minimum-ttl'))
                            if echo_interval and echo_interval == cfg_echo_interval:
                                requests.append(self.get_delete_profile_attr_request(profile_name, 'desired-minimum-echo-receive'))
                            if echo_mode is not None and echo_mode == cfg_echo_mode:
                                requests.append(self.get_delete_profile_attr_request(profile_name, 'echo-active'))
                            if (enabled is None and not transmit_interval and not receive_interval and not detect_multiplier and passive_mode is None
                                    and not min_ttl and not echo_interval and echo_mode is None):
                                requests.append(self.get_delete_profile_request(profile_name))

        return requests

    def get_delete_bfd_shop_requests(self, commands, have):
        requests = []

        single_hops = commands.get('single_hops', None)
        if single_hops:
            for hop in single_hops:
                remote_address = hop.get('remote_address', None)
                vrf = hop.get('vrf', None)
                interface = hop.get('interface', None)
                local_address = hop.get('local_address', None)
                enabled = hop.get('enabled', None)
                transmit_interval = hop.get('transmit_interval', None)
                receive_interval = hop.get('receive_interval', None)
                detect_multiplier = hop.get('detect_multiplier', None)
                passive_mode = hop.get('passive_mode', None)
                echo_interval = hop.get('echo_interval', None)
                echo_mode = hop.get('echo_mode', None)
                profile_name = hop.get('profile_name', None)

                cfg_single_hops = have.get('single_hops', None)
                if cfg_single_hops:
                    for cfg_hop in cfg_single_hops:
                        cfg_remote_address = cfg_hop.get('remote_address', None)
                        cfg_vrf = cfg_hop.get('vrf', None)
                        cfg_interface = cfg_hop.get('interface', None)
                        cfg_local_address = cfg_hop.get('local_address', None)
                        cfg_enabled = cfg_hop.get('enabled', None)
                        cfg_transmit_interval = cfg_hop.get('transmit_interval', None)
                        cfg_receive_interval = cfg_hop.get('receive_interval', None)
                        cfg_detect_multiplier = cfg_hop.get('detect_multiplier', None)
                        cfg_passive_mode = cfg_hop.get('passive_mode', None)
                        cfg_echo_interval = cfg_hop.get('echo_interval', None)
                        cfg_echo_mode = cfg_hop.get('echo_mode', None)
                        cfg_profile_name = cfg_hop.get('profile_name', None)

                        if remote_address == cfg_remote_address and vrf == cfg_vrf and interface == cfg_interface and local_address == cfg_local_address:
                            if enabled is not None and enabled == cfg_enabled:
                                requests.append(self.get_delete_shop_attr_request(remote_address, interface, vrf, local_address, 'enabled'))
                            if transmit_interval and transmit_interval == cfg_transmit_interval:
                                requests.append(self.get_delete_shop_attr_request(remote_address, interface, vrf, local_address,
                                                                                  'desired-minimum-tx-interval'))
                            if receive_interval and receive_interval == cfg_receive_interval:
                                requests.append(self.get_delete_shop_attr_request(remote_address, interface, vrf, local_address, 'required-minimum-receive'))
                            if detect_multiplier and detect_multiplier == cfg_detect_multiplier:
                                requests.append(self.get_delete_shop_attr_request(remote_address, interface, vrf, local_address, 'detection-multiplier'))
                            if passive_mode is not None and passive_mode == cfg_passive_mode:
                                requests.append(self.get_delete_shop_attr_request(remote_address, interface, vrf, local_address, 'passive-mode'))
                            if echo_interval and echo_interval == cfg_echo_interval:
                                requests.append(self.get_delete_shop_attr_request(remote_address, interface, vrf, local_address,
                                                                                  'desired-minimum-echo-receive'))
                            if echo_mode is not None and echo_mode == cfg_echo_mode:
                                requests.append(self.get_delete_shop_attr_request(remote_address, interface, vrf, local_address, 'echo-active'))
                            if profile_name and profile_name == cfg_profile_name:
                                requests.append(self.get_delete_shop_attr_request(remote_address, interface, vrf, local_address, 'profile-name'))
                            if (enabled is None and not transmit_interval and not receive_interval and not detect_multiplier and passive_mode is None
                                    and not echo_interval and echo_mode is None and not profile_name):
                                requests.append(self.get_delete_shop_request(remote_address, interface, vrf, local_address))

        return requests

    def get_delete_bfd_mhop_requests(self, commands, have):
        requests = []

        multi_hops = commands.get('multi_hops', None)
        if multi_hops:
            for hop in multi_hops:
                remote_address = hop.get('remote_address', None)
                vrf = hop.get('vrf', None)
                local_address = hop.get('local_address', None)
                enabled = hop.get('enabled', None)
                transmit_interval = hop.get('transmit_interval', None)
                receive_interval = hop.get('receive_interval', None)
                detect_multiplier = hop.get('detect_multiplier', None)
                passive_mode = hop.get('passive_mode', None)
                min_ttl = hop.get('min_ttl', None)
                profile_name = hop.get('profile_name', None)

                cfg_multi_hops = have.get('multi_hops', None)
                if cfg_multi_hops:
                    for cfg_hop in cfg_multi_hops:
                        cfg_remote_address = cfg_hop.get('remote_address', None)
                        cfg_vrf = cfg_hop.get('vrf', None)
                        cfg_local_address = cfg_hop.get('local_address', None)
                        cfg_enabled = cfg_hop.get('enabled', None)
                        cfg_transmit_interval = cfg_hop.get('transmit_interval', None)
                        cfg_receive_interval = cfg_hop.get('receive_interval', None)
                        cfg_detect_multiplier = cfg_hop.get('detect_multiplier', None)
                        cfg_passive_mode = cfg_hop.get('passive_mode', None)
                        cfg_min_ttl = cfg_hop.get('min_ttl', None)
                        cfg_profile_name = cfg_hop.get('profile_name', None)

                        if remote_address == cfg_remote_address and vrf == cfg_vrf and local_address == cfg_local_address:
                            if enabled is not None and enabled == cfg_enabled:
                                requests.append(self.get_delete_mhop_attr_request(remote_address, vrf, local_address, 'enabled'))
                            if transmit_interval and transmit_interval == cfg_transmit_interval:
                                requests.append(self.get_delete_mhop_attr_request(remote_address, vrf, local_address, 'desired-minimum-tx-interval'))
                            if receive_interval and receive_interval == cfg_receive_interval:
                                requests.append(self.get_delete_mhop_attr_request(remote_address, vrf, local_address, 'required-minimum-receive'))
                            if detect_multiplier and detect_multiplier == cfg_detect_multiplier:
                                requests.append(self.get_delete_mhop_attr_request(remote_address, vrf, local_address, 'detection-multiplier'))
                            if passive_mode is not None and passive_mode == cfg_passive_mode:
                                requests.append(self.get_delete_mhop_attr_request(remote_address, vrf, local_address, 'passive-mode'))
                            if min_ttl and min_ttl == cfg_min_ttl:
                                requests.append(self.get_delete_mhop_attr_request(remote_address, vrf, local_address, 'minimum-ttl'))
                            if profile_name and profile_name == cfg_profile_name:
                                requests.append(self.get_delete_mhop_attr_request(remote_address, vrf, local_address, 'profile-name'))
                            if (enabled is None and not transmit_interval and not receive_interval and not detect_multiplier and passive_mode is None
                                    and not min_ttl and not profile_name):
                                requests.append(self.get_delete_mhop_request(remote_address, vrf, local_address))

        return requests

    def get_delete_all_bfd_cfg_requests(self, commands):
        requests = []
        profiles = commands.get('profiles', None)
        single_hops = commands.get('single_hops', None)
        multi_hops = commands.get('multi_hops', None)

        if profiles:
            url = '%s/openconfig-bfd-ext:bfd-profile/profile' % (BFD_PATH)
            requests.append({'path': url, 'method': DELETE})
        if single_hops:
            url = '%s/openconfig-bfd-ext:bfd-shop-sessions/single-hop' % (BFD_PATH)
            requests.append({'path': url, 'method': DELETE})
        if multi_hops:
            url = '%s/openconfig-bfd-ext:bfd-mhop-sessions/multi-hop' % (BFD_PATH)
            requests.append({'path': url, 'method': DELETE})

        return requests

    def get_delete_profile_request(self, profile_name):
        url = '%s/openconfig-bfd-ext:bfd-profile/profile=%s' % (BFD_PATH, profile_name)
        request = {'path': url, 'method': DELETE}

        return request

    def get_delete_profile_attr_request(self, profile_name, attr):
        url = '%s/openconfig-bfd-ext:bfd-profile/profile=%s/config/%s' % (BFD_PATH, profile_name, attr)
        request = {'path': url, 'method': DELETE}

        return request

    def get_delete_shop_request(self, remote_address, interface, vrf, local_address):
        url = '%s/openconfig-bfd-ext:bfd-shop-sessions/single-hop=%s,%s,%s,%s' % (BFD_PATH, remote_address, interface, vrf, local_address)
        request = {'path': url, 'method': DELETE}

        return request

    def get_delete_shop_attr_request(self, remote_address, interface, vrf, local_address, attr):
        url = '%s/openconfig-bfd-ext:bfd-shop-sessions/single-hop=%s,%s,%s,%s/config/%s' % (BFD_PATH, remote_address, interface, vrf, local_address, attr)
        request = {'path': url, 'method': DELETE}

        return request

    def get_delete_mhop_request(self, remote_address, vrf, local_address):
        url = '%s/openconfig-bfd-ext:bfd-mhop-sessions/multi-hop=%s,null,%s,%s' % (BFD_PATH, remote_address, vrf, local_address)
        request = {'path': url, 'method': DELETE}

        return request

    def get_delete_mhop_attr_request(self, remote_address, vrf, local_address, attr):
        url = '%s/openconfig-bfd-ext:bfd-mhop-sessions/multi-hop=%s,null,%s,%s/config/%s' % (BFD_PATH, remote_address, vrf, local_address, attr)
        request = {'path': url, 'method': DELETE}

        return request

    def get_profile_name(self, profile_name):
        return profile_name.get('profile_name')

    def sort_lists_in_config(self, config):
        if 'profiles' in config and config['profiles'] is not None:
            config['profiles'].sort(key=self.get_profile_name)
        if 'single_hops' in config and config['single_hops'] is not None:
            config['single_hops'].sort(key=lambda x: (x['remote_address'], x['interface'], x['vrf'], x['local_address']))
        if 'multi_hops' in config and config['multi_hops'] is not None:
            config['multi_hops'].sort(key=lambda x: (x['remote_address'], x['vrf'], x['local_address']))

    def remove_default_entries(self, data):

        profiles = data.get('profiles', None)
        single_hops = data.get('single_hops', None)
        multi_hops = data.get('multi_hops', None)

        if profiles:
            for profile in profiles:
                enabled = profile.get('enabled', None)
                transmit_interval = profile.get('transmit_interval', None)
                receive_interval = profile.get('receive_interval', None)
                detect_multiplier = profile.get('detect_multiplier', None)
                passive_mode = profile.get('passive_mode', None)
                min_ttl = profile.get('min_ttl', None)
                echo_interval = profile.get('echo_interval', None)
                echo_mode = profile.get('echo_mode', None)

                if enabled:
                    profile.pop('enabled')
                if transmit_interval == 300:
                    profile.pop('transmit_interval')
                if receive_interval == 300:
                    profile.pop('receive_interval')
                if detect_multiplier == 3:
                    profile.pop('detect_multiplier')
                if passive_mode is False:
                    profile.pop('passive_mode')
                if min_ttl == 254:
                    profile.pop('min_ttl')
                if echo_interval == 300:
                    profile.pop('echo_interval')
                if echo_mode is False:
                    profile.pop('echo_mode')

        if single_hops:
            for hop in single_hops:
                enabled = hop.get('enabled', None)
                transmit_interval = hop.get('transmit_interval', None)
                receive_interval = hop.get('receive_interval', None)
                detect_multiplier = hop.get('detect_multiplier', None)
                passive_mode = hop.get('passive_mode', None)
                echo_interval = hop.get('echo_interval', None)
                echo_mode = hop.get('echo_mode', None)

                if enabled:
                    hop.pop('enabled')
                if transmit_interval == 300:
                    hop.pop('transmit_interval')
                if receive_interval == 300:
                    hop.pop('receive_interval')
                if detect_multiplier == 3:
                    hop.pop('detect_multiplier')
                if passive_mode is False:
                    hop.pop('passive_mode')
                if echo_interval == 300:
                    hop.pop('echo_interval')
                if echo_mode is False:
                    hop.pop('echo_mode')

        if multi_hops:
            for hop in multi_hops:
                enabled = hop.get('enabled', None)
                transmit_interval = hop.get('transmit_interval', None)
                receive_interval = hop.get('receive_interval', None)
                detect_multiplier = hop.get('detect_multiplier', None)
                passive_mode = hop.get('passive_mode', None)
                min_ttl = hop.get('min_ttl', None)

                if enabled:
                    hop.pop('enabled')
                if transmit_interval == 300:
                    hop.pop('transmit_interval')
                if receive_interval == 300:
                    hop.pop('receive_interval')
                if detect_multiplier == 3:
                    hop.pop('detect_multiplier')
                if passive_mode is False:
                    hop.pop('passive_mode')
                if min_ttl == 254:
                    hop.pop('min_ttl')
