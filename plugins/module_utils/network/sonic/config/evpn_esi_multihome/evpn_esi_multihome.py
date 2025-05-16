#
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_evpn_esi_multihome class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from __future__ import absolute_import, division, print_function
__metaclass__ = type
from copy import deepcopy
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    update_states,
    get_diff,
    remove_none
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.formatted_diff_utils import (
    get_new_config,
    get_formatted_config_diff
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import Facts

PATCH = "patch"
DELETE = "delete"
EVPN_MH_PATH = 'data/openconfig-network-instance:network-instances/network-instance=default/evpn/evpn-mh/config'


class Evpn_esi_multihome(ConfigBase):
    """
    The sonic_evpn_esi_multihome class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'evpn_esi_multihome',
    ]

    def __init__(self, module):
        super(Evpn_esi_multihome, self).__init__(module)

    def get_evpn_esi_multihome_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        evpn_esi_multihome_facts = dict()
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        evpn_esi_multihome_facts = facts['ansible_network_resources'].get('evpn_esi_multihome')
        if evpn_esi_multihome_facts is None:
            return {}
        return evpn_esi_multihome_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        commands = list()

        existing_evpn_esi_multihome_facts = self.get_evpn_esi_multihome_facts()
        commands, requests = self.set_config(existing_evpn_esi_multihome_facts)
        if commands and requests:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.errno)
            result['changed'] = True
        result['commands'] = commands

        changed_evpn_esi_mh_facts = self.get_evpn_esi_multihome_facts()

        result['before'] = existing_evpn_esi_multihome_facts
        if result['changed']:
            result['after'] = changed_evpn_esi_mh_facts

        new_config = changed_evpn_esi_mh_facts
        old_config = existing_evpn_esi_multihome_facts
        if self._module.check_mode:
            result.pop('after', None)
            new_config = get_new_config(commands, existing_evpn_esi_multihome_facts)
        if self._module._diff:
            result['diff'] = get_formatted_config_diff(old_config, new_config, self._module._verbosity)

        return result

    def set_config(self, existing_evpn_esi_multihome_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: Two lists
        :returns: the commands and requests necessary to migrate the current configuration
                  to the desired configuration
        """
        want = remove_none(self._module.params['config'])
        have = existing_evpn_esi_multihome_facts
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
            commands, requests = self._state_overridden(want, have)
        elif state == 'deleted':
            commands, requests = self._state_deleted(want, have)
        elif state == 'merged':
            commands, requests = self._state_merged(want, have)
        elif state == 'replaced':
            commands, requests = self._state_replaced(want, have)
        return commands, requests

    def _state_replaced(self, want, have):
        """ The command generator when state is replaced

        :rtype: Two list
        :returns: the commands and requests necessary to migrate the current configuration
                  to the desired configuration
        """
        requests = []
        commands = []
        delete_all = False

        if want is None or have is None:
            return commands, requests
        if not want:
            return commands, requests

        diff_want = get_diff(want, have)
        if not diff_want:
            return commands, requests

        commands = deepcopy(want)
        diff = get_diff(have, want)
        if diff is None:
            delete_all = True
            commands = have
        else:
            commands = get_diff(want, diff)

        requests = self.get_delete_evpn_esi_mh_request(commands, have, delete_all)

        if len(commands) > 0 and len(requests) > 0:
            commands = update_states(commands, 'deleted')
        else:
            commands = []

        if len(requests) > 0:
            new_have = {}
        else:
            new_have = have

        diff = get_diff(want, new_have)
        merged_commands = diff

        replaced_snmp = self.get_create_evpn_esi_mh_request(merged_commands, have)
        requests.extend(replaced_snmp)
        if merged_commands and len(replaced_snmp) > 0:
            merged_commands = update_states(merged_commands, 'replaced')
            new_commands = list()
            for command in merged_commands:
                new_commands.append(remove_none(command))
            commands = new_commands
        else:
            commands = []

        return commands, requests

    def _state_overridden(self, want, have):
        """ The command generator when state is overridden

        :rtype: Two lists
        :returns: the commands and requests necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        requests = []
        if want is None or have is None:
            return commands, requests

        if not want:
            return commands, requests

        diff_want = get_diff(want, have)
        diff_dont_want = get_diff(have, want)

        if diff_want is None and diff_dont_want is None:
            return commands, requests
        if not diff_want:
            return commands, requests

        commands = have
        requests = list(self.get_delete_evpn_esi_mh_request(commands, have, True))

        if commands and len(requests) > 0:
            commands = update_states(commands, "deleted")

        merged_commands = want
        overridden_requests = self.get_create_evpn_esi_mh_request(merged_commands, want)

        requests.extend(overridden_requests)

        if want and len(overridden_requests) > 0:
            merged_commands = update_states(want, "overridden")
            commands = merged_commands
        else:
            commands = []

        return commands, requests

    def _state_merged(self, want, have):
        """ The command generator when state is merged

        :rtype: Two lists
        :returns: the commands and requests necessary to merge the provided into
                  the current configuration
        """
        commands = get_diff(want, have)
        requests = self.get_create_evpn_esi_mh_request(commands, have)

        if commands and len(requests) > 0:
            commands = update_states(commands, "merged")
        else:
            commands = []

        return commands, requests

    def _state_deleted(self, want, have):
        """ The command generator when state is deleted

        :rtype: Two lists
        :returns: the commands and requests necessary to remove the current configuration
                  of the provided objects
        """
        requests = []
        commands = []

        if not have or have is None or have is {}:
            return commands, requests

        delete_all = False
        have = remove_none(have)

        if have is None:
            return commands, requests
        if not want or want is None:
            commands = deepcopy(have)
            delete_all = True
        else:
            commands = want

        requests = list(self.get_delete_evpn_esi_mh_request(commands, have, delete_all))

        if commands and len(requests) > 0:
            commands = update_states(commands, "deleted")
        else:
            commands = []

        return commands, requests

    def get_create_evpn_esi_mh_request(self, config, have=None):
        """ Creates the request for creating the evpn_esi_mh object

        :rtype: A list
        :returns: the request for creating the evpn_esi_mh object
        """
        request_info = dict()
        method = PATCH
        path = EVPN_MH_PATH
        requests = list()

        request_info['openconfig-network-instance:config'] = {'df-election-time': config.get('df_election_time', None),
                                                              'es-activation-delay': config.get('es_activation_delay', None),
                                                              'mac-holdtime': config.get('mac_holdtime', None),
                                                              'neigh-holdtime': config.get('neigh_holdtime', None),
                                                              'startup-delay': config.get('startup_delay', None)
                                                             }

        request = dict()
        request = {'path': path, 'method': method, 'data': request_info}
        requests.append(request)

        return requests

    def get_delete_evpn_esi_mh_request(self, configs, have, delete_all):
        """ Creates the request for deleting the evpn_esi_mh object

        :rtype: A list
        :returns: the requests for deleting the evpn_esi_mh object
        """
        requests = []
        path = EVPN_MH_PATH
        if not configs:
            return requests

        have_df_election_time = have.get('df_election_time', None)
        have_es_activation_delay = have.get('es_activation_delay', None)
        have_mac_holdtime = have.get('mac_holdtime', None)
        have_neigh_holdtime = have.get('neigh_holdtime', None)
        have_startup_delay = have.get('startup_delay', None)

        df_election_time = 'df_election_time' in configs
        es_activation_delay = 'es_activation_delay' in configs
        mac_holdtime = 'mac_holdtime' in configs
        neigh_holdtime = 'neigh_holdtime' in configs
        startup_delay = 'startup_delay' in configs

        if delete_all:
            delete_all_request = {'path': path, 'method': DELETE}
            requests.append(delete_all_request)
            return requests

        if df_election_time and have_df_election_time:
            df_election_time_url = '{0}/{1}'.format(path, 'df-election-time')
            df_election_time_request = {'path': df_election_time_url, 'method': DELETE}
            requests.append(df_election_time_request)

        if es_activation_delay and have_es_activation_delay:
            es_activation_delay_url = '{0}/{1}'.format(path, 'es-activation-delay')
            es_activation_delay_request = {'path': es_activation_delay_url, 'method': DELETE}
            requests.append(es_activation_delay_request)

        if mac_holdtime and have_mac_holdtime:
            mac_holdtime_url = '{0}/{1}'.format(path, 'mac-holdtime')
            mac_holdtime_delay_request = {'path': mac_holdtime_url, 'method': DELETE}
            requests.append(mac_holdtime_delay_request)

        if neigh_holdtime and have_neigh_holdtime:
            neigh_holdtime_url = '{0}/{1}'.format(path, 'neigh-holdtime')
            neigh_holdtime_request = {'path': neigh_holdtime_url, 'method': DELETE}
            requests.append(neigh_holdtime_request)

        if startup_delay and have_startup_delay:
            startup_delay_url = '{0}/{1}'.format(path, 'startup-delay')
            startup_delay_request = {'path': startup_delay_url, 'method': DELETE}
            requests.append(startup_delay_request)

        return requests
