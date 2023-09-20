#
# -*- coding: utf-8 -*-
# Copyright 2023 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_dhcp_snooping class
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
    remove_empties
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import Facts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    get_diff,
    update_states
)

TEST_KEYS = [
    {"config": {'afis': {'afi': ''}}}
]

IPV4 = 'ipv4'
IPV6 = 'ipv6'

DELETE = 'delete'
PATCH = 'patch'


class Dhcp_snooping(ConfigBase):
    """
    The sonic_dhcp_snooping class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'dhcp_snooping',
    ]

    dhcp_snooping_uri = 'data/openconfig-dhcp-snooping:dhcp-snooping'
    config_uri = dhcp_snooping_uri + '/config'
    enable_uri = config_uri + '/dhcpv{v}-admin-enable'
    verify_mac_uri = config_uri + '/dhcpv{v}-verify-mac-address'
    binding_uri = dhcp_snooping_uri + '-static-binding/entry'
    trusted_uri = 'data/openconfig-interfaces:interfaces/interface={name}/dhcpv{v}-snooping-trust/config/dhcpv{v}-snooping-trust'
    vlans_uri = 'data/sonic-vlan:sonic-vlan/VLAN/VLAN_LIST={vlan_name}/dhcpv{v}_snooping_enable'

    def __init__(self, module):
        super(Dhcp_snooping, self).__init__(module)

    def get_dhcp_snooping_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset,
                                                         self.gather_network_resources)
        dhcp_snooping_facts = facts['ansible_network_resources'].get('dhcp_snooping')
        if not dhcp_snooping_facts:
            return []
        return dhcp_snooping_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = list()

        existing_dhcp_snooping_facts = self.get_dhcp_snooping_facts()
        commands, requests = self.set_config(existing_dhcp_snooping_facts)
        if commands:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands

        changed_dhcp_snooping_facts = self.get_dhcp_snooping_facts()

        result['before'] = existing_dhcp_snooping_facts
        if result['changed']:
            result['after'] = changed_dhcp_snooping_facts

        result['warnings'] = warnings
        return result

    def set_config(self, existing_dhcp_snooping_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']
        have = existing_dhcp_snooping_facts
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

        afis = {}
        want = remove_empties(want)

        if want.get('afis') is not None:
            for want_afi in want.get('afis'):
                if want_afi.get('afi') == IPV4:
                    afis['want_ipv4'] = want_afi
                elif want_afi.get('afi') == IPV6:
                    afis['want_ipv6'] = want_afi

        if have.get('afis') is not None:
            for have_afi in have.get('afis'):
                if have_afi.get('afi') == IPV4:
                    afis['have_ipv4'] = have_afi
                elif have_afi.get('afi') == IPV6:
                    afis['have_ipv6'] = have_afi

        state = self._module.params['state']
        if state == 'merged':
            commands, requests = self._state_merged(want, have)
        elif state == 'deleted':
            commands, requests = self._state_deleted(want, have, afis)
        elif state == 'replaced':
            commands, requests = self._state_replaced(want, have, afis)
        elif state == 'overridden':
            commands, requests = self._state_overridden(want, have, afis)

        return commands, requests

    def _state_merged(self, want, have):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        diff = get_diff(want, have)
        commands = diff
        requests = self.get_modify_requests(commands)
        if commands and len(requests) > 0:
            commands = update_states(commands, "merged")
        else:
            commands = []

        return commands, requests

    def _state_deleted(self, want, have, afis):
        """ The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        requests = []

        if not have or have == {} or have.get('afis') is None:
            commands = []
        elif not want or want == {} or want.get('afis') is None:
            commands = have
            requests = self.get_delete_all_requests(afis)
        else:
            commands = want
            requests = self.get_delete_specific_requests(afis)

        if commands and len(requests) > 0:
            commands = update_states(commands, "deleted")
        else:
            commands = []

        return commands, requests

    def _state_overridden(self, want, have, afis):
        """ The command generator when state is overridden

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        requests = []
        if not want:
            return commands, requests

        # Determine if there is any configuration specified in the playbook
        # that is not contained in the current configuration.
        diff_requested = get_diff(want, have, TEST_KEYS)

        # Determine if there is anything already configured that is not
        # specified in the playbook.
        diff_unwanted = get_diff(have, want, TEST_KEYS)

        # Idempotency check: If the configuration already matches the
        # requested configuration with no extra attributes, no
        # commands should be executed on the device.
        if not diff_requested and not diff_unwanted:
            return commands, requests

        # Delete all current DHCP snooping configuration
        commands = [have]
        requests = self.get_delete_all_requests(afis)
        if commands and len(requests) > 0:
            commands = update_states(commands, "deleted")

        # Apply the commands from the playbook
        merged_commands = want
        overridden_requests = self.get_modify_requests(merged_commands)
        requests.extend(overridden_requests)
        if merged_commands and len(overridden_requests) > 0:
            merged_commands = update_states(merged_commands, "overridden")
            commands.extend(merged_commands)
        return commands, requests

    def _state_replaced(self, want, have, afis):
        """ The command generator when state is replaced

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        requests = []

        # Delete replaced groupings
        commands = deepcopy(want)
        requests = self.get_delete_replaced_groupings(afis)
        if not requests:
            commands = []
        if commands and len(requests) > 0:
            commands = update_states(commands, "deleted")

        if requests:
            modify_have = []
        else:
            modify_have = have

        # Apply the commands from the playbook
        diff = get_diff(want, modify_have, TEST_KEYS)
        merged_commands = diff

        replaced_requests = self.get_modify_requests(merged_commands)
        requests.extend(replaced_requests)
        if merged_commands and len(replaced_requests) > 0:
            merged_commands = update_states(merged_commands, "replaced")
            commands.extend(merged_commands)

        return commands, requests

    def get_modify_requests(self, command):
        requests = []

        if command.get('afis') is not None:
            for afi in command.get('afis'):
                if afi.get('afi') == IPV4:
                    requests.extend(self.get_specific_modify_requests(afi, 4))
                if afi.get('afi') == IPV6:
                    requests.extend(self.get_specific_modify_requests(afi, 6))

        return requests

    def get_specific_modify_requests(self, afi, v):
        """Get requests to modify specific DHCP snooping configurations
        based on the command specified for the interface
        """
        requests = []

        if afi.get('enabled') is not None:
            payload = {'openconfig-dhcp-snooping:dhcpv{v}-admin-enable'.format(v=v): afi['enabled']}
            uri = self.enable_uri.format(v=v)
            requests.append({'path': uri, 'method': PATCH, 'data': payload})

        if afi.get('verify_mac') is not None:
            payload = {'openconfig-dhcp-snooping:dhcpv{v}-verify-mac-address'.format(v=v): afi['verify_mac']}
            uri = self.verify_mac_uri.format(v=v)
            requests.append({'path': uri, 'method': PATCH, 'data': payload})

        if afi.get('trusted'):
            for intf in afi.get('trusted'):
                intf_type = intf.get('intf_type')
                intf_number = intf.get('intf_number')
                if intf_type and intf_number:
                    payload = {'openconfig-interfaces:dhcpv{v}-snooping-trust'.format(v=v): 'ENABLE'}
                    uri = self.trusted_uri.format(name=intf_type + intf_number, v=v)
                    requests.append({'path': uri, 'method': PATCH, 'data': payload})

        if afi.get('vlans'):
            for vlan_id in afi.get('vlans'):
                payload = {'sonic-vlan:dhcpv{v}_snooping_enable'.format(v=v): 'enable'}
                uri = self.vlans_uri.format(vlan_name='Vlan' + vlan_id, v=v)
                requests.append({'path': uri, 'method': PATCH, 'data': payload})

        if afi.get('source_bindings'):
            entries = []
            for entry in afi.get('source_bindings'):
                if entry.get('mac_addr'):
                    entries.append({
                        'mac': entry.get('mac_addr'),
                        'iptype': 'ipv' + str(v),
                        'config': {
                            'mac': entry.get('mac_addr'),
                            'iptype': 'ipv' + str(v),
                            'vlan': str(entry.get('vlan_id')),
                            'interface': entry.get('intf_name'),
                            'ip': entry.get('ip_addr'),
                        }
                    })
            payload = {'openconfig-dhcp-snooping:entry': entries}
            uri = self.binding_uri
            requests.append({'path': uri, 'method': PATCH, 'data': payload})

        return requests

    def get_delete_all_requests(self, afis):
        requests = []

        requests.extend(self.get_delete_all_afi_requests(afis.get('have_ipv4')))
        requests.extend(self.get_delete_all_afi_requests(afis.get('have_ipv6')))

        return requests

    def get_delete_specific_requests(self, afis):
        requests = []

        want_ipv4 = afis.get('want_ipv4')
        want_ipv6 = afis.get('want_ipv6')
        have_ipv4 = afis.get('have_ipv4')
        have_ipv6 = afis.get('have_ipv6')

        if want_ipv4:
            if len(want_ipv4) == 3 and self.defaults_unchanged(want_ipv4):
                # AFI dict has only the afi key, meaning the whole AFI is targeted.
                requests.extend(self.get_delete_all_afi_requests(have_ipv4))
            else:
                requests.extend(self.get_delete_specific_afi_requests(want_ipv4, have_ipv4))
        if want_ipv6:
            if len(want_ipv6) == 3 and self.defaults_unchanged(want_ipv6):
                requests.extend(self.get_delete_all_afi_requests(have_ipv6))
            else:
                requests.extend(self.get_delete_specific_afi_requests(want_ipv6, have_ipv6))

        return requests

    def get_delete_all_afi_requests(self, have_afi):
        requests = []
        if have_afi:
            if have_afi.get('enabled') is True:
                requests.extend(self.get_delete_enabled_request(have_afi))
            if have_afi.get('verify_mac') is False:
                requests.extend(self.get_delete_verify_mac_request(have_afi))
            if have_afi.get('vlans') is not None and have_afi.get('vlans') != []:
                requests.extend(self.get_delete_vlans_requests(have_afi))
            if have_afi.get('trusted') is not None and have_afi.get('trusted') != []:
                requests.extend(self.get_delete_trusted_requests(have_afi))
            if have_afi.get('source_bindings') is not None and have_afi.get('source_bindings') != []:
                requests.extend(self.get_delete_all_source_bindings_request())
        return requests

    def get_delete_specific_afi_requests(self, want_afi, have_afi):
        requests = []

        if want_afi.get('enabled') is False and have_afi.get('enabled') is True:
            requests.extend(self.get_delete_enabled_request(want_afi))
        if want_afi.get('verify_mac') is True and have_afi.get('enabled') is False:
            requests.extend(self.get_delete_verify_mac_request(want_afi))
        if want_afi.get('vlans') and have_afi.get('vlans') is not None and have_afi.get('vlans') != []:
            if want_afi.get('vlans') == ['all']:
                requests.extend(self.get_delete_vlans_requests(have_afi))
            else:
                # Check to make sure that the vlans wanting to be deleted currently exist on the device.
                want_set = set()
                have_set = set()
                for vlan in want_afi.get('vlans'):
                    want_set.add(vlan)
                for vlan in have_afi.get('vlans'):
                    have_set.add(vlan)
                if len(have_set.intersection(want_set)):
                    requests.extend(self.get_delete_vlans_requests(want_afi))
        if want_afi.get('trusted') and have_afi.get('trusted') is not None and have_afi.get('trusted') != []:
            if want_afi.get('trusted') == [{'intf_type': 'Ethernet', 'intf_number': 'all'}]:
                requests.extend(self.get_delete_trusted_requests(have_afi))
            else:
                # Check to make sure that the interfaces wanting to be deleted currently exist on the device.
                want_set = set()
                have_set = set()
                for intf in want_afi.get('trusted'):
                    intfName = intf['intf_type'] + intf['intf_number']
                    want_set.add(intfName)
                for intf in have_afi.get('trusted'):
                    intfName = intf['intf_type'] + intf['intf_number']
                    have_set.add(intfName)
                if len(have_set.intersection(want_set)):
                    requests.extend(self.get_delete_trusted_requests(want_afi))
        if want_afi.get('source_bindings') and have_afi.get('source_bindings') is not None and have_afi.get('source_bindings') != []:
            if want_afi.get('source_bindings') == [{'mac_addr': 'all'}]:
                requests.extend(self.get_delete_all_source_bindings_request())
            else:
                # Check to make sure that the bindings wanting to be deleted currently exist on the device.
                want_set = set()
                have_set = set()
                for entry in want_afi.get('source_bindings'):
                    want_set.add(entry['mac_addr'])
                for entry in have_afi.get('source_bindings'):
                    have_set.add(entry['mac_addr'])
                if len(have_set.intersection(want_set)):
                    requests.extend(self.get_delete_specific_source_bindings_requests(want_afi))

        return requests

    def get_delete_enabled_request(self, afi):
        payload = {'openconfig-dhcp-snooping:dhcpv{v}-admin-enable'.format(v=self.afi_to_vnum(afi)): False}
        return [{'path': self.enable_uri.format(v=self.afi_to_vnum(afi)), 'method': PATCH, 'data': payload}]

    def get_delete_verify_mac_request(self, afi):
        payload = {'openconfig-dhcp-snooping:dhcpv{v}-verify-mac-address'.format(v=self.afi_to_vnum(afi)): True}
        return [{'path': self.verify_mac_uri.format(v=self.afi_to_vnum(afi)), 'method': PATCH, 'data': payload}]

    def get_delete_vlans_requests(self, afi):
        requests = []
        if afi.get('vlans'):
            for vlan_id in afi.get('vlans'):
                requests.append({
                    'path': self.vlans_uri.format(vlan_name='Vlan' + vlan_id, v=self.afi_to_vnum(afi)),
                    'method': DELETE
                })
        return requests

    def get_delete_trusted_requests(self, afi):
        requests = []
        if afi.get('trusted'):
            for intf in afi.get('trusted'):
                intf_type = intf.get('intf_type')
                intf_number = intf.get('intf_number')
                if intf_type and intf_number:
                    requests.append({
                        'path': self.trusted_uri.format(name=intf_type + intf_number, v=self.afi_to_vnum(afi)),
                        'method': DELETE
                    })
        return requests

    def get_delete_all_source_bindings_request(self):
        return [{'path': self.binding_uri, 'method': DELETE}]

    def get_delete_specific_source_bindings_requests(self, afi):
        requests = []
        for entry in afi.get('source_bindings'):
            if entry.get('mac_addr'):
                requests.append({
                    'path': self.binding_uri + '={mac},{ipv}'.format(mac=entry.get('mac_addr'), ipv=afi.get('afi'))
                })
        return requests

    def get_delete_individual_source_bindings_requests(self, afi, entry):
        return {'path': self.binding_uri + '={mac},{ipv}'.format(mac=entry.get('mac_addr'), ipv=afi.get('afi'))}

    def get_delete_replaced_groupings(self, afis):
        requests = []

        want_ipv4 = afis.get('want_ipv4')
        have_ipv4 = afis.get('have_ipv4')
        want_ipv6 = afis.get('want_ipv6')
        have_ipv6 = afis.get('have_ipv6')

        if want_ipv4 and have_ipv4:
            requests.extend(self.get_delete_replaced_groupings_afi(want_ipv4, have_ipv4))
        if want_ipv6 and have_ipv6:
            requests.extend(self.get_delete_replaced_groupings_afi(want_ipv6, have_ipv6))

        return requests

    def get_delete_replaced_groupings_afi(self, want_afi, have_afi):
        requests = []

        if (want_afi.get('enabled') != have_afi.get('enabled')
                or want_afi.get('verify_mac') != have_afi.get('verify_mac')):
            # If top level leafs have been changed, delete all attributes in afi.
            requests.extend(self.get_delete_all_afi_requests(have_afi))
        else:
            if want_afi.get('vlans') and have_afi.get('vlans'):
                # If the vlan list has been altered, delete all vlans.,
                if set(want_afi.get('vlans')) != set(have_afi.get('vlans')):
                    requests.extend(self.get_delete_vlans_requests(have_afi.get('vlans')))
            if want_afi.get('trusted') and have_afi.get('trusted'):
                # If the trusted interface list has been altered, delete all trusted interfaces.
                want_set = set()
                have_set = set()
                for intf in want_afi.get('trusted'):
                    want_set.add(intf.get('intf_type') + intf.get('intf_number'))
                for intf in have_afi.get('trusted'):
                    have_set.add(intf.get('intf_type') + intf.get('intf_number'))
                if want_set != have_set:
                    requests.extend(self.get_delete_trusted_requests(have_afi))
            if want_afi.get('source_bindings'):
                # Bindings are a dict keyed by the MAC address. If anything else changed, delete the entry.
                for want_entry in want_afi.get('source_bindings'):
                    for have_entry in have_afi.get('source_bindings'):
                        if want_entry.get('mac_addr') == have_entry.get('mac_addr') and want_entry != have_entry:
                            requests.extend(self.get_delete_individual_source_bindings_requests(have_afi, have_entry))

        return requests

    @staticmethod
    def defaults_unchanged(afi):
        if afi.get('enabled') is False and afi.get('verify_mac') is True:
            return True
        else:
            return False

    @staticmethod
    def afi_to_vnum(afi):
        if afi.get('afi') == 'ipv6':
            return '6'
        else:
            return '4'
