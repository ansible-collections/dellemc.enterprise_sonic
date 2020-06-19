#
# -*- coding: utf-8 -*-
# © Copyright 2020 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_vrf_interfaces class
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
from ansible_collections.dellemc.sonic.plugins.module_utils.network.sonic.facts.facts import Facts
from ansible_collections.dellemc.sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible_collections.dellemc.sonic.plugins.module_utils.network.sonic.utils.utils import (
    get_diff,
    update_states,
    get_normalize_interface_name
)
try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote

PATCH = 'patch'
DELETE = 'DELETE'


class Vrf_interfaces(ConfigBase):
    """
    The sonic_vrf_interfaces class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'vrf_interfaces',
    ]

    delete_all_flag = False

    def __init__(self, module):
        super(Vrf_interfaces, self).__init__(module)

    def get_vrf_interfaces_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        vrf_interfaces_facts = facts['ansible_network_resources'].get('vrf_interfaces')
        if not vrf_interfaces_facts:
            return []
        return vrf_interfaces_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = list()
        commands = list()

        existing_vrf_interfaces_facts = self.get_vrf_interfaces_facts()
        commands, requests = self.set_config(existing_vrf_interfaces_facts)
        if commands and len(requests) > 0:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        changed_vrf_interfaces_facts = self.get_vrf_interfaces_facts()

        result['before'] = existing_vrf_interfaces_facts
        if result['changed']:
            result['after'] = changed_vrf_interfaces_facts

        result['warnings'] = warnings
        return result

    def set_config(self, existing_vrf_interfaces_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']
        have = existing_vrf_interfaces_facts

        self.normalize_interface_name_members(want)
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
        diff = get_diff(want, have, ['name'])

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

        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :param interface_type: interface type
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        requests = []

        commands_del = []
        diff_del = get_diff(have, want, ["name"])
        if diff_del:
            for cmd in diff_del:
                if any([want_cfg for want_cfg in want if want_cfg["name"] == cmd["name"]]):
                    commands_del.append(cmd)

        requests_del = []
        if commands_del:
            requests_del = self.get_delete_vrf_interface_requests(commands_del, have, want)

        if requests_del:
            requests.extend(requests_del)
            commands_del = update_states(commands_del, "deleted")
            commands.extend(commands_del)

        requests_rep = []
        commands_rep = diff
        if commands_rep:
            requests_rep = self.get_create_requests(commands_rep, have)

        if requests_rep:
            requests.extend(requests_rep)
            commands_rep = update_states(commands_rep, "replaced")
            commands.extend(commands_rep)

        return commands, requests

    def _state_overridden(self, want, have, diff):
        """ The command generator when state is overridden

        :param want: the desired configuration as a dictionary
        :param obj_in_have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        requests = []

        commands_del = get_diff(have, want, ["name"])

        requests_del = []
        if commands_del:
            requests_del = self.get_delete_vrf_interface_requests(commands_del, have, want)

        if requests_del:
            requests.extend(requests_del)
            commands_del = update_states(commands_del, "deleted")
            commands.extend(commands_del)

        commands_over = diff
        requests_over = []
        if commands_over:
            requests_over = self.get_create_requests(commands_over, have)

        if requests_over:
            requests.extend(requests_over)
            commands_over = update_states(commands_over, "overridden")
            commands.extend(commands_over)

        return commands, requests

    def _state_merged(self, want, have, diff):
        """ The command generator when state is merged

        :param want: the additive configuration as a dictionary
        :param obj_in_have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = diff
        requests = []
        if commands:
            requests = self.get_create_requests(commands, have)

        if requests:
            commands = update_states(commands, "merged")
        else:
            commands = []

        return commands, requests

    def _state_deleted(self, want, have, diff):
        """ The command generator when state is deleted

        :param want: the objects from which the configuration should be removed
        :param obj_in_have: the current configuration as a dictionary
        :param interface_type: interface type
        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        # if want is none, then delete all the vlans
        if not want:
            commands = have
            self.delete_all_flag = True
        else:
            commands = want
            self.delete_all_flag = False

        requests = []
        if commands:
            requests = self.get_delete_vrf_interface_requests(commands, have, want)

        if requests:
            commands = update_states(commands, "deleted")
        else:
            commands = []

        return commands, requests

    def get_delete_vrf_interface_requests(self, configs, have, want):
        requests = []
        if not configs:
            return requests

        # Create URL and payload
        method = DELETE
        for conf in configs:
            name = conf['name']
            del_members = conf.get("members")
            matched = next((have_cfg for have_cfg in have if have_cfg['name'] == name), None)
            if not matched:
                continue

            is_delete_vrf = False
            if want:
                is_delete_vrf = not any([want_cfg for want_cfg in want if want_cfg['name'] == name])
            # if members are not mentioned delet the vrf name
            if is_delete_vrf or (self._module.params['state'] == 'deleted' and self.delete_all_flag) or del_members is None:
                url = 'data/openconfig-network-instance:network-instances/network-instance={0}'.format(name)
                request = {"path": url, "method": method}
                requests.append(request)
            else:
                matched_members = matched.get('members', [])

                if matched_members:
                    common_members = [mem for mem in del_members if mem in matched_members]
                    for del_mem in common_members:
                        url = 'data/openconfig-network-instance:network-instances/network-instance={0}/interfaces/interface={1}'.format(name, del_mem)
                        request = {"path": url, "method": method}
                        requests.append(request)

        return requests

    def get_create_requests(self, configs, have):
        requests = []
        if not configs:
            return requests

        requests_vrf = self.get_create_vrf_requests(configs, have)
        if requests_vrf:
            requests.extend(requests_vrf)

        requests_vrf_intf = self.get_create_vrf_interface_requests(configs, have)
        if requests_vrf_intf:
            requests.extend(requests_vrf_intf)

        return requests

    def get_create_vrf_requests(self, configs, have):
        requests = []
        if not configs:
            return requests

        # Create URL and payload
        method = PATCH
        for conf in configs:
            name = conf["name"]
            matched = next((have_cfg for have_cfg in have if have_cfg['name'] == name), None)
            if not matched:
                url = 'data/openconfig-network-instance:network-instances/network-instance={0}'.format(name)
                payload = self.build_create_vrf_payload(conf)
                request = {"path": url, "method": method, "data": payload}
                requests.append(request)

        return requests

    def get_create_vrf_interface_requests(self, configs, have):
        requests = []
        if not configs:
            return requests

        # Create URL and payload
        method = PATCH
        for conf in configs:
            url = 'data/openconfig-network-instance:network-instances/network-instance={0}/interfaces/interface'.format(conf["name"])
            payload = self.build_create_vrf_interface_payload(conf)
            if payload:
                request = {"path": url, "method": method, "data": payload}
                requests.append(request)

        return requests

    def build_create_vrf_payload(self, conf):
        name = conf['name']

        netw_inst = dict({'name': name})
        netw_inst['config'] = dict({'name': name})

        netw_inst_arr = [netw_inst]

        return dict({'openconfig-network-instance:network-instance': netw_inst_arr})

    def build_create_vrf_interface_payload(self, conf):
        members = conf.get("members")
        network_inst_payload = dict()
        if members:
            network_inst_payload.update({"openconfig-network-instance:interface": []})
            for member in members:
                member_config_payload = dict({"id": member})
                member_payload = dict({"id": member, "config": member_config_payload})
                network_inst_payload["openconfig-network-instance:interface"].append(member_payload)

        return network_inst_payload

    def normalize_interface_name_members(self, configs):
        if not configs:
            return

        for conf in configs:
            members = conf.get('members', [])
            if members:
                norm_members = []
                for mem in members:
                    norm_mem = get_normalize_interface_name(mem)
                    norm_members.append(norm_mem)
                conf['members'] = norm_members
