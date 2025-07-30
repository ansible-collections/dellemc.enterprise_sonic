#
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_vlans class
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
    search_obj_in_list,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import Facts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    get_diff,
    get_replaced_config,
    update_states,
    remove_empties_from_list,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.interfaces_util import (
    build_interfaces_create_request,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.formatted_diff_utils import (
    __DELETE_CONFIG_IF_NO_SUBCONFIG,
    get_new_config,
    get_formatted_config_diff
)
from ansible.module_utils.connection import ConnectionError


TEST_KEYS = [
    {'config': {'vlan_id': ''}},
]
TEST_KEYS_formatted_diff = [
    {'config': {'vlan_id': '', '__delete_op': __DELETE_CONFIG_IF_NO_SUBCONFIG}},
]


class Vlans(ConfigBase):
    """
    The sonic_vlans class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'vlans',
    ]

    def __init__(self, module):
        super(Vlans, self).__init__(module)

    def get_vlans_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        vlans_facts = facts['ansible_network_resources'].get('vlans', None)
        if not vlans_facts:
            return []
        return vlans_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = list()

        existing_vlans_facts = self.get_vlans_facts()
        commands, requests = self.set_config(existing_vlans_facts)
        if commands:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        changed_vlans_facts = self.get_vlans_facts()

        result['before'] = existing_vlans_facts
        if result['changed']:
            result['after'] = changed_vlans_facts

        new_config = changed_vlans_facts
        if self._module.check_mode:
            result.pop('after', None)
            new_config = get_new_config(commands, existing_vlans_facts,
                                        TEST_KEYS_formatted_diff)
            new_config = self.deal_with_default_entries(new_config, method="add")
            new_config.sort(key=lambda x: x['vlan_id'])
            result['after(generated)'] = new_config

        if self._module._diff:
            result['diff'] = get_formatted_config_diff(existing_vlans_facts,
                                                       new_config,
                                                       self._module._verbosity)
        result['warnings'] = warnings
        return result

    def set_config(self, existing_vlans_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = remove_empties_from_list(self._module.params['config'])
        have = existing_vlans_facts
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

        ret_commands = remove_empties_from_list(commands)
        return ret_commands, requests

    def _state_replaced(self, want, have, diff):
        """ The command generator when state is replaced

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        requests = []
        replaced_config = get_replaced_config(self.deal_with_default_entries(want, method="add"), have, TEST_KEYS)
        replaced_config = get_replaced_config(want, have, TEST_KEYS)
        replaced_vlans = []
            for config in replaced_config:
                vlan_obj = search_obj_in_list(config['vlan_id'], want, 'vlan_id')
                if vlan_obj:
                    replaced_vlans.append(vlan_obj)

            del_requests = self.get_delete_vlans_requests(replaced_vlans, delete_vlan=True)
            requests.extend(del_requests)
            commands.extend(update_states(replaced_config, "deleted"))

        diff = get_diff(want, have, TEST_KEYS)
        diff = self.deal_with_default_entries(diff, method="remove")
        if diff:
            rep_requests = self.get_create_vlans_requests(diff)
            if len(rep_requests) > 0:
                requests.extend(rep_requests)
                commands.extend(update_states(diff, "replaced"))

        return commands, requests

    def _state_overridden(self, want, have, diff):
        """ The command generator when state is overridden

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        requests = []

        reverse_diff = get_diff(have, want, TEST_KEYS)
        reverse_diff = self.deal_with_default_entries(reverse_diff, method="remove")

        if not diff and not reverse_diff:
            return commands, requests

        del_vlans = []
        del_vlans_attributes = []

        for config in reverse_diff:
            vlan_obj = search_obj_in_list(config['vlan_id'], want, 'vlan_id')
            have_vlan_obj = search_obj_in_list(config['vlan_id'], have, 'vlan_id')
            if vlan_obj:
                if vlan_obj.get('description', None) is None and have_vlan_obj.get("description") is not None:
                    del_vlans_attributes.append({"vlan_id": config.get("vlan_id"), "description": have_vlan_obj.get("description")})
                if vlan_obj.get('autostate', None) is False:
                    del_vlans_attributes.append({"vlan_id": config.get("vlan_id"), "autostate": False})
            else:
                del_vlans.append(config)

        if del_vlans:
            del_requests = self.get_delete_vlans_requests(del_vlans, delete_vlan=True)
            requests.extend(del_requests)
            commands.extend(update_states(del_vlans, "deleted"))

        if del_vlans_attributes:
            del_requests = self.get_delete_vlans_requests(del_vlans_attributes, delete_vlan=False)
            requests.extend(del_requests)
            commands.extend(update_states(del_vlans_attributes, "deleted"))

        if diff:
            ovr_commands = diff
            ovr_requests = self.get_create_vlans_requests(ovr_commands)
            if len(ovr_requests) > 0:
                requests.extend(ovr_requests)
                commands.extend(update_states(ovr_commands, "overridden"))

        return commands, requests

    def _state_merged(self, want, have, diff):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration at position-0
                  Requests necessary to merge to the current configuration
                  at position-1
        """
        commands = update_states(diff, "merged")
        requests = self.get_create_vlans_requests(commands)

        return commands, requests

    def _state_deleted(self, want, have, diff):
        """ The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        commands = list()
        # if want is none, then delete all the vlans
        delete_vlan = False
        if not want:
            commands = have
            delete_vlan = True
        else:  # delete specific vlans
            commands = get_diff(want, diff, TEST_KEYS)

        requests = self.get_delete_vlans_requests(commands, delete_vlan=delete_vlan)
        commands = update_states(commands, "deleted")
        return commands, requests

    def get_delete_vlans_requests(self, configs, delete_vlan=False):
        requests = []
        if not configs:
            return requests
        # Create URL and payload
        url = "data/openconfig-interfaces:interfaces/interface=Vlan{}"
        method = "DELETE"
        for vlan in configs:
            vlan_id = vlan.get("vlan_id", None)
            if delete_vlan or (vlan_id and not (vlan.get("description", None) or vlan.get("autostate", None))):
                path = url.format(vlan_id)
                request = {"path": path,
                           "method": method,
                           }
                requests.append(request)

            else:
                if vlan.get("description", None) is not None:
                    path = self.get_delete_vlan_config_attr(vlan_id, "description")
                    request = {"path": path,
                               "method": method,
                               }
                    requests.append(request)

                if vlan.get("autostate", None) is not None:
                    path = self.get_delete_vlan_config_attr(vlan_id, "autostate")
                    payload = {"sonic-vlan:autostate": "disable"}
                    request = {"path": path, "method": "PATCH", "data": payload}
                    requests.append(request)

        return requests

    def get_delete_vlan_config_attr(self, vlan_id, attr_name):
        if attr_name == "description":
            url = "data/openconfig-interfaces:interfaces/interface=Vlan{}/config/{}"
        elif attr_name == "autostate":
            url = "data/sonic-vlan:sonic-vlan/VLAN/VLAN_LIST=Vlan{}/{}"
        path = url.format(vlan_id, attr_name)

        return path

    def get_create_vlans_requests(self, configs):
        requests = []
        if not configs:
            return requests
        for vlan in configs:
            vlan_id = vlan.get("vlan_id", None)
            interface_name = "Vlan" + str(vlan_id)
            description = vlan.get("description", None)
            autostate = vlan.get("autostate", None)
            request = build_interfaces_create_request(interface_name=interface_name)
            requests.append(request)
            if description is not None:
                requests.append(self.get_modify_vlan_config_attr(interface_name, 'description', description))
            if autostate is not None:
                requests.append(self.get_modify_vlan_config_attr(interface_name, 'autostate', autostate))

        return requests

    def get_modify_vlan_config_attr(self, intf_name, attr_name, attr_value):
        if attr_name == "description":
            url = "data/openconfig-interfaces:interfaces/interface={}/config".format(intf_name)
            payload = {"openconfig-interfaces:config": {"name": intf_name, attr_name: attr_value}}
            method = "PATCH"
        elif attr_name == "autostate":
            url = "data/sonic-vlan:sonic-vlan/VLAN/VLAN_LIST={}/autostate".format(intf_name)
            if attr_value is True:
                attr_value = "enable"
            elif attr_value is False:
                attr_value = "disable"
            payload = {"sonic-vlan:{}".format(attr_name): attr_value}
            method = "PATCH"
        request = {"path": url, "method": method, "data": payload}
        return request

    def deal_with_default_entries(self, configs, method="add"):
        """
        Remove default entries for the data value in overridden state
        Autostate is defaulted to True and can never be truly deleted so it is a no-op
        Optional parameter: method [add|remove] to determine whether to fill in the missing default value or to remove the fields that are auto-populated
        """
        if configs:
            pop_list = []
            for index, vlan in enumerate(configs):
                if 'autostate' not in vlan:
                    pop_list.append(index)
            for index in pop_list:
                if method == "add":
                    configs[index]["autostate"] = True
                elif method == "remove":
                    if configs[index].get("autostate") is not None:
                        del configs[index]["autostate"]
        return configs
