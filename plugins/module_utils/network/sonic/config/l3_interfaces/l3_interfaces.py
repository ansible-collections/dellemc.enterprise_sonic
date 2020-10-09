#
# -*- coding: utf-8 -*-
# Copyright 2020 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_l3_interfaces class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import json
import ipaddress

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)
from ansible_collections.dellemc.sonic.plugins.module_utils.network.sonic.facts.facts import Facts
from ansible_collections.dellemc.sonic.plugins.module_utils.network.sonic.utils.utils import (
    get_diff,
    update_states,
    normalize_interface_name,
)
from ansible_collections.dellemc.sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible.module_utils._text import to_native
import traceback

LIB_IMP_ERR = None
ERR_MSG = None
try:
    import jinja2
    HAS_LIB = True
except Exception as e:
    HAS_LIB = False
    ERR_MSG = to_native(e)
    LIB_IMP_ERR = traceback.format_exc()

TEST_KEYS = [
    {"ipv4": {"address"}},
    {"ipv6": {"address"}},
]

DELETE = "DELETE"
PATCH = "PATCH"


def get_sub_interface_name(name):
    if name.startswith("Vlan"):
        return "openconfig-vlan:routed-vlan"
    else:
        return "subinterfaces/subinterface=0"


class L3_interfaces(ConfigBase):
    """
    The sonic_l3_interfaces class
    """

    gather_subset = [
        '!all',
        '!min'
    ]

    gather_network_resources = [
        'l3_interfaces',
    ]

    def __init__(self, module):
        super(L3_interfaces, self).__init__(module)

    def get_l3_interfaces_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        l3_interfaces_facts = facts['ansible_network_resources'].get('l3_interfaces')
        if not l3_interfaces_facts:
            return []
        return l3_interfaces_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = list()

        existing_l3_interfaces_facts = self.get_l3_interfaces_facts()
        commands, requests = self.set_config(existing_l3_interfaces_facts)
        if commands:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        changed_l3_interfaces_facts = self.get_l3_interfaces_facts()

        result['before'] = existing_l3_interfaces_facts
        if result['changed']:
            result['after'] = changed_l3_interfaces_facts

        result['warnings'] = warnings
        return result

    def set_config(self, existing_l3_interfaces_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']
        normalize_interface_name(want)
        have = existing_l3_interfaces_facts
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
        # with open('/root/ansible_log.log', 'a+') as fp:
        #     fp.write('set_state want : ' + str(want) + '\n')
        #     fp.write('set_state diff : ' + str(diff) + '\n')
        #     fp.write('set_state have : ' + str(have) + '\n')
        if state == 'overridden':
            commands, requests = self._state_overridden(want, have, diff)
        elif state == 'deleted':
            commands, requests = self._state_deleted(want, have, diff)
        elif state == 'merged':
            commands, requests = self._state_merged(want, have, diff)
        elif state == 'replaced':
            commands, requests = self._state_replaced(want, have, diff)
        ret_commands = commands
        return ret_commands, requests

    def _state_replaced(self, want, have, diff):
        """ The command generator when state is replaced

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        ret_requests = list()
        commands = list()
        l3_interfaces_to_delete = get_diff(have, want, TEST_KEYS)
        obj = self.get_object(l3_interfaces_to_delete, want)
        diff = get_diff(obj, want, TEST_KEYS)
        if diff:
            delete_l3_interfaces_requests = self.get_delete_all_requests(want)
            ret_requests.extend(delete_l3_interfaces_requests)
            commands.extend(update_states(want, "deleted"))
            l3_interfaces_to_create_requests = self.get_create_l3_interfaces_requests(want, have, want)
            ret_requests.extend(l3_interfaces_to_create_requests)
            commands.extend(update_states(want, "merged"))
        return commands, ret_requests

    def _state_overridden(self, want, have, diff):
        """ The command generator when state is overridden

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        ret_requests = list()
        commands = list()
        interfaces_to_delete = get_diff(have, want, TEST_KEYS)
        if interfaces_to_delete:
            delete_interfaces_requests = self.get_delete_l3_interfaces_requests(want, have)
            ret_requests.extend(delete_interfaces_requests)
            commands.extend(update_states(interfaces_to_delete, "deleted"))

        if diff:
            interfaces_to_create_requests = self.get_create_l3_interfaces_requests(diff, have, want)
            ret_requests.extend(interfaces_to_create_requests)
            commands.extend(update_states(diff, "merged"))

        return commands, ret_requests

    def _state_merged(self, want, have, diff):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = diff
        requests = self.get_create_l3_interfaces_requests(commands, have, want)
        if commands and len(requests) > 0:
            commands = update_states(commands, "merged")
        else:
            commands = []

        return commands, requests

    def _state_deleted(self, want, have, diff):
        """ The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        commands = list()
        if not want:
            commands = have
            requests = self.get_delete_all_completely_requests(commands)
        else:
            commands = want
            requests = self.get_delete_l3_interfaces_requests(commands, have)
        if len(requests) == 0:
            commands = []
        if commands:
            commands = update_states(commands, "deleted")
        return commands, requests

    def get_object(self, have, want):
        objects = list()
        names = [i.get('name', None) for i in want]
        for obj in have:
            if 'name' in obj and obj['name'] in names:
                objects.append(obj.copy())
        return objects

    def get_address(self, ip_str, have_obj):
        to_return = list()
        for i in have_obj:
            if ip_str in i and i[ip_str] is not None:
                for ip in i[ip_str]:
                    to_return.append(ip['address'])
        return to_return

    def get_delete_l3_interfaces_requests(self, want, have):
        requests = []
        ipv4_url_all = 'data/openconfig-interfaces:interfaces/interface={intf_name}/{sub_intf_name}/openconfig-if-ip:ipv4/addresses'
        ipv6_url_all = 'data/openconfig-interfaces:interfaces/interface={intf_name}/{sub_intf_name}/openconfig-if-ip:ipv6/addresses'
        ipv4_url = 'data/openconfig-interfaces:interfaces/interface={intf_name}/{sub_intf_name}/openconfig-if-ip:ipv4/addresses/address={address}'
        ipv6_url = 'data/openconfig-interfaces:interfaces/interface={intf_name}/{sub_intf_name}/openconfig-if-ip:ipv6/addresses/address={address}'

        for each_l3 in want:
            l3 = each_l3.copy()
            name = l3.get('name')
            name = l3.pop('name')
            sub_intf = get_sub_interface_name(name)
            have_obj = next((e_cfg for e_cfg in have if e_cfg['name'] == name), None)
            have_ipv4 = list()
            have_ipv6 = list()
            if not have_obj:
                continue

            have_ipv4 = self.get_address('ipv4', [have_obj])
            have_ipv6 = self.get_address('ipv6', [have_obj])

            if 'ipv4' in l3 and l3['ipv4'] is None:
                l3.pop('ipv4')
            if 'ipv6' in l3 and l3['ipv6'] is None:
                l3.pop('ipv6')

            if not l3 or len(l3) == 0:
                if have_ipv4 and len(have_ipv4) != 0:
                    ipv4_delete_request = {"path": ipv4_url_all.format(intf_name=name, sub_intf_name=sub_intf), "method": DELETE}
                    requests.append(ipv4_delete_request)

                if have_ipv6 and len(have_ipv6) != 0:
                    ipv6_delete_request = {"path": ipv6_url_all.format(intf_name=name, sub_intf_name=sub_intf), "method": DELETE}
                    requests.append(ipv6_delete_request)
            else:
                ipv4 = l3.get('ipv4', [])
                ipv6 = l3.get('ipv6', [])
                for ip in ipv4:
                    if have_ipv4 and ip['address'] in have_ipv4:
                        addr = ip['address'].split('/')[0]
                        request = {"path": ipv4_url.format(intf_name=name, sub_intf_name=sub_intf, address=addr), "method": DELETE}
                        requests.append(request)
                for ip in ipv6:
                    if have_ipv6 and ip['address'] in have_ipv6:
                        addr = ip['address'].split('/')[0]
                        request = {"path": ipv6_url.format(intf_name=name, sub_intf_name=sub_intf, address=addr), "method": DELETE}
                        requests.append(request)
        # with open('/root/ansible_log.log', 'a+') as fp:
        #     fp.write('get_delete_l3_interfaces_requests requests : ' + str(requests) + '\n')
        return requests

    def get_delete_all_completely_requests(self, configs):
        # with open('/root/ansible_log.log', 'a+') as fp:
        #     fp.write('get_delete_all_completely_requests config : ' + str(configs) + '\n')
        delete_requests = list()
        for l3 in configs:
            if l3['ipv4'] or l3['ipv6']:
                delete_requests.append(l3)
        return self.get_delete_all_requests(delete_requests)

    def get_delete_all_requests(self, configs):
        requests = []
        ipv4_url_all = 'data/openconfig-interfaces:interfaces/interface={intf_name}/{sub_intf_name}/openconfig-if-ip:ipv4/addresses'
        ipv6_url_all = 'data/openconfig-interfaces:interfaces/interface={intf_name}/{sub_intf_name}/openconfig-if-ip:ipv6/addresses'
        for l3 in configs:
            name = l3.get('name')
            ipv4 = l3.get('ipv4', [])
            ipv6 = l3.get('ipv6', [])
            sub_intf = get_sub_interface_name(name)

            if ipv4:
                ipv4_delete_request = {"path": ipv4_url_all.format(intf_name=name, sub_intf_name=sub_intf), "method": DELETE}
                requests.append(ipv4_delete_request)
            if ipv6:
                ipv6_delete_request = {"path": ipv6_url_all.format(intf_name=name, sub_intf_name=sub_intf), "method": DELETE}
                requests.append(ipv6_delete_request)
        return requests

    def get_create_l3_interfaces_requests(self, configs, have, want):
        requests = []
        if not configs:
            return requests
        ipv4_url = 'data/openconfig-interfaces:interfaces/interface={intf_name}/{sub_intf_name}/openconfig-if-ip:ipv4/addresses'
        ipv6_url = 'data/openconfig-interfaces:interfaces/interface={intf_name}/{sub_intf_name}/openconfig-if-ip:ipv6/addresses'
        for l3 in configs:
            l3_interface_name = l3.get('name')
            if l3_interface_name == "eth0":
                continue

            sub_intf = get_sub_interface_name(l3_interface_name)

            have_obj = next((e_cfg for e_cfg in have if e_cfg['name'] == l3_interface_name), None)
            l3_interface_ipv4 = l3.get('ipv4')
            l3_interface_ipv6 = l3.get('ipv6')

            have_ipv4 = list()
            have_ipv6 = list()

            if have_obj:
                have_ipv4 = self.get_address('ipv4', [have_obj])
                have_ipv6 = self.get_address('ipv6', [have_obj])

            if l3_interface_ipv4:
                for item in l3_interface_ipv4:
                    ipv4 = item['address'].split('/')[0]
                    ipv4_mask = item['address'].split('/')[1]
                    if item['address'] not in have_ipv4:
                        payload = self.build_create_payload(ipv4, ipv4_mask)
                        request_ipv4 = {"path": ipv4_url.format(intf_name=l3_interface_name, sub_intf_name=sub_intf), "method": PATCH, "data": payload}
                        requests.append(request_ipv4)

            if l3_interface_ipv6:
                for item in l3_interface_ipv6:
                    ipv6 = item['address'].split('/')[0]
                    ipv6_mask = item['address'].split('/')[1]
                    if item['address'] not in have_ipv6:
                        payload = self.build_create_payload(ipv6, ipv6_mask)
                        request_ipv6 = {"path": ipv6_url.format(intf_name=l3_interface_name, sub_intf_name=sub_intf), "method": PATCH, "data": payload}
                        requests.append(request_ipv6)
        return requests

    def build_create_payload(self, ip, mask):
        payload_template = """{
                                  "openconfig-if-ip:addresses": {
                                      "address": [{
                                          "ip": "{{ip}}",
                                          "openconfig-if-ip:config": {
                                              "ip": "{{ip}}",
                                              "prefix-length": {{mask}}
                                          }
                                      }]
                                  }
                              }"""

        input_data = {'ip': ip, 'mask': mask}
        env = jinja2.Environment(autoescape=False, extensions=['jinja2.ext.autoescape'])
        t = env.from_string(payload_template)
        intended_payload = t.render(input_data)
        ret_payload = json.loads(intended_payload)
        return ret_payload
