#
# -*- coding: utf-8 -*-
# © Copyright 2020 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_l2_interfaces class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from __future__ import absolute_import, division, print_function
__metaclass__ = type

import json
from urllib.parse import quote

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    get_diff,
    update_states,
    normalize_interface_name
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import (
    Facts
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible.module_utils._text import to_native
from ansible.module_utils.connection import ConnectionError
import copy
import traceback

LIB_IMP_ERR = None
ERR_MSG = None
try:
    import requests
    HAS_LIB = True
except Exception as e:
    HAS_LIB = False
    ERR_MSG = to_native(e)
    LIB_IMP_ERR = traceback.format_exc()

PATCH = 'patch'
intf_key = 'openconfig-if-ethernet:ethernet'
port_chnl_key = 'openconfig-if-aggregate:aggregation'

TEST_KEYS = [
    {'allowed_vlans': {'vlan': ''}},
]


class L2_interfaces(ConfigBase):
    """
    The sonic_l2_interfaces class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'l2_interfaces',
    ]

    def __init__(self, module):
        super(L2_interfaces, self).__init__(module)

    def get_l2_interfaces_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        l2_interfaces_facts = facts['ansible_network_resources'].get('l2_interfaces')
        if not l2_interfaces_facts:
            return []
        return l2_interfaces_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = list()

        existing_l2_interfaces_facts = self.get_l2_interfaces_facts()
        commands, requests = self.set_config(existing_l2_interfaces_facts)

        if commands:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        changed_l2_interfaces_facts = self.get_l2_interfaces_facts()

        result['before'] = existing_l2_interfaces_facts
        if result['changed']:
            result['after'] = changed_l2_interfaces_facts

        result['warnings'] = warnings
        return result

    def set_config(self, existing_l2_interfaces_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = copy.deepcopy(self._module.params['config'])
        normalize_interface_name(want, self._module)
        have = existing_l2_interfaces_facts

        for intf in have:
            if not intf.get('access'):
                intf.update({'access': None})
            if not intf.get('trunk'):
                intf.update({'trunk': None})

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

        diff = get_diff(want, have, TEST_KEYS)

        if state == 'overridden':
            commands, requests = self._state_overridden(want, have, diff)
        elif state == 'deleted':
            commands, requests = self._state_deleted(want, have, diff)
        elif state == 'merged':
            commands, requests = self._state_merged(want, have, diff)
        elif state == 'replaced':
            commands, requests = self._state_replaced(want, have, diff)

        return commands, requests

    def _state_replaced(self, want, have, diff):
        """ The command generator when state is replaced

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """

        requests = []
        commands = diff

        if commands:
            requests_del = self.get_delete_all_switchport_requests(commands)
            if requests_del:
                requests.extend(requests_del)

            requests_rep = self.get_create_l2_interface_request(commands, have)
            if len(requests_del) or len(requests_rep):
                requests.extend(requests_rep)
                commands = update_states(commands, "replaced")
            else:
                commands = []

        return commands, requests

    def _state_overridden(self, want, have, diff):
        """ The command generator when state is overridden

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        requests = []

        commands_del = get_diff(have, want, TEST_KEYS)
        requests_del = self.get_delete_all_switchport_requests(commands_del)
        if len(requests_del):
            requests.extend(requests_del)
            commands_del = update_states(commands_del, "deleted")
            commands.extend(commands_del)

        commands_over = diff
        requests_over = self.get_create_l2_interface_request(commands_over, have)
        if requests_over:
            requests.extend(requests_over)
            commands_over = update_states(commands_over, "overridden")
            commands.extend(commands_over)

        return commands, requests

    def _state_merged(self, want, have, diff):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration at position-0
                  Requests necessary to merge to the current configuration
                  at position-1
        """
        commands = diff
        requests = self.get_create_l2_interface_request(commands, have)
        if commands and len(requests):
            commands = update_states(commands, "merged")
        return commands, requests

    def _state_deleted(self, want, have, diff):
        """ The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """

        # if want is none, then delete all the vlan links
        if not want or len(have) == 0:
            commands = have
            requests = self.get_delete_all_switchport_requests(commands)
        else:
            requests = self.get_delete_specific_switchport_requests(want, have)
            # If "want" has been modified during execution of
            # get_delete_specific_switchport_requests due to absence of some
            # of the specified commands from the current device configuration,
            # the returned value for "commands" needs to reflect the revised
            # set of commands so that the playbook output can correctly display
            # the commands actually sent to the device.
            commands = want
            if len(requests) == 0:
                commands = []

        if commands:
            commands = update_states(commands, "deleted")

        return commands, requests

    def get_trunk_delete_switchport_request(self, config, match_config):
        method = "DELETE"
        name = config['name']
        requests = []
        conf_allowed_vlans = config['trunk'].get('allowed_vlans', [])
        match_trunk = match_config.get('trunk')
        if match_trunk:
            match_trunk_vlans = match_trunk.get('allowed_vlans', [])
            if conf_allowed_vlans and match_trunk_vlans:
                vlan_id_list = ""
                conf_vlan_index = 0
                pop_list = []
                for each_allowed_vlan in conf_allowed_vlans:
                    vlan_id = each_allowed_vlan.get('vlan')
                    if not vlan_id:
                        pop_list.insert(0, conf_vlan_index)
                        conf_vlan_index += 1
                        continue
                    if self.input_vlan_id_in_device_config(vlan_id, match_trunk_vlans):
                        if '-' in vlan_id:
                            vlan_id_fmt = vlan_id.replace('-', '..')
                        else:
                            vlan_id_fmt = vlan_id

                        if vlan_id_list:
                            vlan_id_list += ",{}".format(vlan_id_fmt)
                        else:
                            vlan_id_list = vlan_id_fmt
                    else:
                        # defer popping of unconfigured vlans until completion of the outer loop.
                        pop_list.insert(0, conf_vlan_index)


                    conf_vlan_index += 1

                if vlan_id_list:
                    key = intf_key
                    if name.startswith('PortChannel'):
                        key = port_chnl_key

                    url = "data/openconfig-interfaces:interfaces/interface={0}/{1}/".format(name, key)
                    url += "openconfig-vlan:switched-vlan/config/"
                    url +=  "trunk-vlans=" + quote(vlan_id_list)

                    request = {"path": url, "method": method}
                    requests.append(request)

                    for pop_list_index in pop_list:
                        config['trunk']['allowed_vlans'].pop(pop_list_index)

        if conf_allowed_vlans and not requests:
            config['trunk'].pop('allowed_vlans')

        return requests

    def get_access_delete_switchport_request(self, config, match_config):
        method = "DELETE"
        request = None
        name = config['name']
        match_access = match_config.get('access')
        if match_access and match_access.get('vlan') == config['access'].get('vlan'):
            key = intf_key
            if name.startswith('PortChannel'):
                key = port_chnl_key
            url = "data/openconfig-interfaces:interfaces/interface={}/{}/openconfig-vlan:switched-vlan/config/access-vlan"
            request = {"path": url.format(name, key), "method": method}
        elif config['access'].get('vlan'):
            config['access'].pop('vlan')

        return request

    def get_delete_all_switchport_requests(self, configs):
        requests = []
        if not configs:
            return requests
        # Create URL and payload
        url = "data/openconfig-interfaces:interfaces/interface={}/{}/openconfig-vlan:switched-vlan/config"
        method = "DELETE"
        for intf in configs:
            name = intf.get("name")
            key = intf_key
            if name.startswith('PortChannel'):
                key = port_chnl_key
            request = {"path": url.format(name, key),
                       "method": method,
                       }
            requests.append(request)

        return requests

    def get_delete_specific_switchport_requests(self, configs, have):
        requests = []
        if not configs:
            return requests

        for conf in configs:
            name = conf['name']

            matched = next((cnf for cnf in have if cnf['name'] == name), None)
            if matched:
                keys = conf.keys()

                # if both access and trunk not mention in delete
                if not ('access' in keys) and not ('trunk' in keys):
                    requests.extend(self.get_delete_all_switchport_requests([conf]))
                else:
                    # if access or trunk is mentioned with value
                    if conf.get('access') or conf.get('trunk'):
                        # if access is mentioned with value
                        if conf.get('access'):
                            vlan = conf.get('access').get('vlan')
                            if vlan:
                                request = self.get_access_delete_switchport_request(conf, matched)
                                if request:
                                    requests.append(request)
                            else:
                                if matched.get('access') and matched.get('access').get('vlan'):
                                    conf['access']['vlan'] = matched.get('access').get('vlan')
                                    request = self.get_access_delete_switchport_request(conf, matched)
                                    if request:
                                        requests.append(request)

                        # if trunk is mentioned with value
                        if conf.get('trunk'):
                            allowed_vlans = conf['trunk'].get('allowed_vlans')
                            if allowed_vlans:
                                requests.extend(self.get_trunk_delete_switchport_request(conf, matched))
                            # allowed vlans mentioned without value
                            else:
                                trunk_match = matched.get('trunk')
                                if trunk_match and trunk_match.get('allowed_vlans'):
                                    conf['trunk']['allowed_vlans'] = trunk_match.get('allowed_vlans').copy()
                                    requests.extend(
                                           self.get_trunk_delete_switchport_request(conf, matched))

                    # check for access or trunk is mentioned without value
                    else:
                        # access mentioned without value
                        if ('access' in keys) and conf.get('access', None) is None:
                            # get the existing values and delete it
                            if matched.get('access'):
                                conf['access'] = matched.get('access').copy()
                                request = self.get_access_delete_switchport_request(conf, matched)
                                if request:
                                    requests.append(request)
                        # trunk mentioned without value
                        if ('trunk' in keys) and conf.get('trunk', None) is None:
                            # get the existing values and delete it
                            if matched.get('trunk'):
                                conf['trunk'] = matched.get('trunk').copy()
                                requests.extend(self.get_trunk_delete_switchport_request(conf, matched))

        return requests

    def get_create_l2_interface_request(self, configs, have):
        requests = []
        if not configs:
            return requests
        # Create URL and payload
        url = "data/openconfig-interfaces:interfaces/interface={}/{}/openconfig-vlan:switched-vlan/config"
        method = "PATCH"
        pop_list = []
        conf_index = 0
        for conf in configs:
            name = conf.get('name')
            if name == "eth0":
                pop_list.insert(0, conf_index)
                conf_index += 1
                continue
            key = intf_key
            if name.startswith('PortChannel'):
                key = port_chnl_key
            matched = next((cnf for cnf in have if cnf['name'] == name), None)
            payload = self.build_create_payload(conf, matched)
            if payload:
                request = {"path": url.format(name, key),
                           "method": method,
                           "data": payload
                           }
                requests.append(request)
            else:
                pop_list.insert(0, conf_index)
            conf_index += 1

        for index in pop_list:
            configs.pop(index)
        return requests

    def build_create_payload(self, conf, matched):
        payload_url = '{"openconfig-vlan:config":{ '
        access_payload = ''
        trunk_payload = ''
        if conf.get('access'):
            access_vlan_id = conf['access']['vlan']
            access_payload = '"access-vlan": {0}'.format(access_vlan_id)
        if conf.get('trunk') and conf['trunk'].get('allowed_vlans'):
            trunk_payload = '"trunk-vlans": ['
            cnt = 0
            pop_list = []
            conf_vlan_index = 0
            match_trunk_vlans = []
            match_trunk = {}
            if matched:
                match_trunk = matched.get('trunk')
            if match_trunk:
                match_trunk_vlans = match_trunk.get('allowed_vlans', [])

            for each_allowed_vlan in conf['trunk']['allowed_vlans']:
                vlan_val = each_allowed_vlan['vlan']
                # The following idempotency handling is required because of
                # vlan trunk ranges. A configured range can contain a vlan or
                # range that has been requested for configuration in the
                # executing playbook. In this case, the requested vlan or range will
                # not be removed during "get_diff" processing because the subset
                # vlan or range value will not match the value of a larger
                # configured range in which it is contained.
                #
                # Don't request configuration of any vlans or ranges that are already
                # configured on the target device.
                if match_trunk_vlans:
                    if self.vlan_or_range_is_already_configured(vlan_val, match_trunk_vlans):
                        # Defer popping of already configured vlan values until
                        # completion of the loop.
                        pop_list.insert(0, conf_vlan_index)
                        conf_vlan_index += 1
                        continue

                if '-' in vlan_val:
                    request_vlan_val = '"{}"'.format(vlan_val.replace("-", ".."))
                else:
                    request_vlan_val = vlan_val
                conf_vlan_index += 1

                # The specified vlan or range is not already fully configured
                # on the target device, so include it in the request.
                if cnt > 0:
                    trunk_payload += ','
                trunk_payload += request_vlan_val
                cnt = cnt + 1

            if cnt:
                # Remove from the list of "invocation" configured vlans any
                # vlans or ranges that are already configured on the target
                # device. This enables correct reporting of the vlans that
                # are actually being configured on the device.
                for pop_list_index in pop_list:
                    conf['trunk']['allowed_vlans'].pop(pop_list_index)
                trunk_payload += ']'
            else:
                trunk_payload = ''

        if access_payload == '' and trunk_payload == '':
            return ''

        if access_payload != '':
            payload_url += access_payload
        if trunk_payload != '':
            if access_payload != '':
                payload_url += ','
            payload_url += trunk_payload

        payload_url += '}}'

        ret_payload = json.loads(payload_url)
        return ret_payload

    def get_range_bounds(self, range_val):
        """Assume an input range value that is a string containing either
        a single integer value or a range string with bounds separated by
        a "-' character or "..".
        Return integer values for the lower and upper bounds of the
        input range string.
        """

        range_bounds = []
        if '-' in range_val:
            range_bounds = range_val.split("-")
        elif '..' in range_val:
            range_bounds = range_val.split("..")
        if range_bounds:
            range_lower = int(range_bounds[0])
            range_upper = int(range_bounds[1])
        else:
            range_lower = range_upper = int(range_val)

        return range_lower, range_upper

    def vlan_range_subset(self, subset, superset):
        """Vlan range string subset check:

        Determine what portion of the range or vlan specified by the input
        "subset" string is a subset of the range specified by the input
        "superset" string. If any portion of the input subset is contained
        in the input superset, return a string specifying the contained
        portion as either a single vlan or a range string in the form
        "<lower bound>..<upper bound>". If no portion of the input subset
        string is contained in the input superset string, return an empty
        string.
        """

        subset_lower, subset_upper = self.get_range_bounds(subset)
        superset_lower, superset_upper = self.get_range_bounds(superset)

        # Check for a subset fully contained in the superset.
        if (subset_lower >= superset_lower and
                subset_upper <= superset_upper):
            return subset

        # Check for a subset lower bound contained in the superset.
        if (subset_lower >= superset_lower and
                subset_lower <= superset_upper):
            if subset_lower == superset_upper:
                # The subset portion is a single vlan.
                return str(subset_lower)
            return "{}..{}".format(str(subset_lower), str(superset_upper))

        # Check for a subset upper bound contained in the superset.
        if (subset_upper <= superset_upper and
                subset_upper >= superset_lower):
            if superset_lower == subset_upper:
                return str(subset_upper)
            return "{}..{}".format(str(superset_lower), str(subset_upper))

        # None of the subset is contained in the superset.
        return ""

    def vlan_or_range_is_already_configured(self, input_vlan_val, match_trunk_vlans):
        """ Determine if the trunk vlan or range specified by input_vlan_val
            is already fully configured on the target device.

        :param input_val: a string containing either a single vlan (integer)
                          value or a range in the form "x-y" or "x..y".
        :param match_trunk_vlans: the current trunk vlan configuration for the interface on
                        which adding of the input_vlan_val trunk vlan(s) has been requested:
                        specified as a list of individual vlan dictionaries.
        :rtype: bool
        :returns: True if the vlan or range is aleady configured on the device; False if
                  the vlan or range is not already configured.
        """
        if not input_vlan_val or not match_trunk_vlans:
            return False
        input_range_lower, input_range_upper = self.get_range_bounds(input_vlan_val)

        for match_trunk_vlan in match_trunk_vlans:
            cfg_trunk_vlan_val = match_trunk_vlan.get('vlan')
            if not cfg_trunk_vlan_val:
                continue
            overlap_vlans = self.vlan_range_subset(input_vlan_val, cfg_trunk_vlan_val)
            if overlap_vlans:
                overlap_range_lower, overlap_range_upper = self.get_range_bounds(overlap_vlans)
                if (overlap_range_lower == input_range_lower and
                    overlap_range_upper == input_range_upper):
                    return True
        return False

    def input_vlan_id_in_device_config(self, input_vlan_id, match_trunk_vlans):
        """ Determine if any portion of the trunk vlan or range specified by input_vlan_id
            is configured on the target device.

        :param input_vlan_id: a string containing either a single vlan (integer)
                              value or a range in the form "x-y" or "x..y".
        :param match_trunk_vlans: the current trunk vlan configuration for the interface on
                        which adding of the input_vlan_val trunk vlan(s) has been requested:
                        specified as a list of individual vlan dictionaries.
        :rtype: bool
        :returns: True if any portion of the vlan or range is aleady configured on the
                  device; False if the vlan or range is not already configured.
        """
        for match_trunk_vlan in match_trunk_vlans:
            cfg_vlan_id = match_trunk_vlan.get('vlan')
            if not cfg_vlan_id:
                continue
            vlan_id = self.vlan_range_subset(input_vlan_id,
                                             cfg_vlan_id)
            if vlan_id:
                return True
        return False
