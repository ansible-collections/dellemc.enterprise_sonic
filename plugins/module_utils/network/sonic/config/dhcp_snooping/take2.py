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
    remove_empties,
    validate_config
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



class Dhcp_snooping(ConfigBase):
    """
    The sonic_dhcp_snooping class
    """
    test_keys = [
        {'afis': {'afi': ''}},
        {"source_bindings": {"mac_addr": ""}},
        {"trusted": {"intf_name": ""}}
    ]

    ipv4_key = 'ipv4'
    ipv6_key = 'ipv6'

    delete_method_value = 'delete'
    patch_method_value = 'patch'

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
        want = self.remove_none(want)

        # just in case weird arguments passed
        if want is None:
            want = {}
        if have is None:
            have = {}

        if want.get('afis') is not None:
            for want_afi in want.get('afis'):
                if want_afi.get('afi') == self.ipv4_key:
                    afis['want_ipv4'] = want_afi
                elif want_afi.get('afi') == self.ipv6_key:
                    afis['want_ipv6'] = want_afi

        if have.get('afis') is not None:
            for have_afi in have.get('afis'):
                if have_afi.get('afi') == self.ipv4_key:
                    afis['have_ipv4'] = have_afi
                elif have_afi.get('afi') == self.ipv6_key:
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
        if want is None:
            want = {}
        else:
            want = remove_empties(want)
            self.validate_config({"config": want})

        commands = get_diff(want, have, test_keys=self.test_keys)
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
        if not have or not have.get('afis'):
            # nothing that could be deleted
            return [], []
        elif not want or not want.get('afis'):
            # want is completly empty, meaning want to delete all config
            # afis parameter only stores the on device config at this point
            commands = have
            requests = self.get_delete_all_have_requests(afis)
        else:
            commands = {}
            used_commands_per_afi = []
            requests = []
            for afi in ["ipv4", "ipv6"]:
                want_afi = afis["want_" + afi]
                have_afi = afis["have_" + afi]
                self.clear_defaults(want_afi)
                if len(want_afi) == 1:
                    # means it looked like default or only specified afi, which interpreted as clear all settings for that afi
                    afi_commands, afi_requests = self.get_single_afi_delete_requests(have_afi, have_afi)
                else:
                    afi_commands, afi_requests = self.get_single_afi_delete_requests(want_afi, have_afi)
                
                if afi_commands:
                    afi_commands["afi"] = afi
                    used_commands_per_afi.append(afi_commands)
                requests.extend(afi_requests)
            
            if len(used_commands_per_afi):
                commands = {"afis": used_commands_per_afi}

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
        if not want or not want.get('afis'):
            # overridding with empty want, so clear everything
            commands = have
            requests = self.get_delete_all_have_requests(afis)

            if commands and len(requests) > 0:
                commands = update_states(commands, "deleted")
            return commands, requests
        
        for afi in want:
            self.clear_defaults(afi)
        for afi in have:
            self.clear_defaults(afi)
        # Get everything that is in playbook and either not in device or different form device
        diff_requested = get_diff(want, have, self.test_keys)

        # Get everything that is in device and either not in playbook or different form playbook
        diff_unwanted = get_diff(have, want, self.test_keys)

        # Idempotency check: If the configuration already matches the
        # requested configuration with no extra attributes, no
        # commands should be executed on the device.
        if not diff_requested and not diff_unwanted:
            return commands, requests
        used_commands_per_afi = []
        commands = {}

        for diff_unwanted_afi in diff_unwanted:
            afi_commands, afi_requests = self.get_single_afi_delete_requests(diff_unwanted_afi, have)
            if afi_commands:
                afi_commands["afi"] = diff_unwanted["afi"]
                used_commands_per_afi.append(afi_commands)
            requests.extend(afi_requests)
        if len(used_commands_per_afi):
            commands = {"afis": used_commands_per_afi}
        if commands and len(requests) > 0:
            commands = update_states(commands, "deleted")

        # Apply the commands from the playbook
        overridden_requests = self.get_modify_requests(diff_requested)
        requests.extend(overridden_requests)
        if merged_commands and len(overridden_requests) > 0:
            merged_commands = update_states(merged_commands, "overridden")
            commands.extend(diff_requested)
        return commands, requests

    def _state_replaced(self, want, have, afis):
        """ The command generator when state is replaced

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        requests = []
        if have.get('afis') and want.get("afis"):
            delete_commands = []
            merge_commands = []
            requests = []

            for afi in ["ipv4", "ipv6"]:
                want_afi = afis["want_" + afi]
                have_afi = afis["have_" + afi]
                self.clear_defaults(want_afi)
                afi_commands, afi_requests, afi_to_merge = self.get_single_afi_replace_requests(want_afi, have_afi)
                if afi_commands:
                    afi_commands["afi"] = afi
                    delete_commands.append(afi_commands)
                requests.extend(afi_requests)
                if afi_to_merge:
                    afi_to_merge["afi"] = afi
                    merge_commands.append(afi_to_merge)
                    merge_requests = self.get_single_afi_modify_requests(afi_to_merge)
                requests.extend(merge_requests)
                
            if delete_commands:
                delete_commands = {"afis": delete_commands}
                commands = update_states(delete_commands, "deleted")
            if merge_commands:
                merge_commands = {"afis": merge_commands}
                merge_commands = update_states(merge_commands, "replaced")
                commands.extend(merge_commands)

        return commands, requests

    def validate_config(self, config):
        '''validate passed in config is argspec compliant. Also does checks on values in ranges that ansible might not do'''
        validated_config = validate_config(self._module.argument_spec, config)
        return validated_config

    def remove_none(self, config):
        '''goes through nested dictionary items and removes any keys that have None as value.
        enables using empty list/dict to specify clear everything for that section and differentiate this
        'clear everything' case from when no value was given
        remove_empties in ansible utils will remove empty lists and dicts as well as None'''
        if type(config) is dict:
            for k, v in list(config.items()):
                if v is None:
                    del config[k]
                else:
                    self.remove_none(v)
        elif type(config) is list:
            for item in list(config):
                if item is None:
                    config.remove(item)
                self.remove_none(item)
        return config
    
    def clear_defaults(self, afi_config):
        '''if the fields with default values are set to default values in config, clear those fields out. This way it doesn't mess with comparisons elsewhere'''
        if "enabled" in afi_config and afi_config["enabled"] is False:
            del afi_config["enabled"]
        if "verify_mac" in afi_config and afi_config["verify_mac"] is False:
            del afi_config ["verify_mac"]

    def get_modify_requests(self, to_modify_config):
        '''builds and returns requests to add in given config 

        :param to_modify: dictionary specifying what to modify in argspec format. expected to be at root level of config'''
        requests = []

        if to_modify_config.get('afis') is not None:
            for afi_config in to_modify_config.get('afis'):
                requests.extend(self.get_single_afi_modify_requests(afi_config))

        return requests

    def get_single_afi_modify_requests(self, to_modify_afi):
        """build requests to modify a single afi family. Uses passed in config to find which family and what to change

        :param to_modify_afi: dictionary specifying the config to add/change in argspec format. expected to be for a single afi
        :param v: version number of afi to modify
        """
        requests = []
        v = self.afi_to_vnum(to_modify_afi)

        if to_modify_afi.get('enabled') is not None:
            payload = {'openconfig-dhcp-snooping:dhcpv{v}-admin-enable'.format(v=v): to_modify_afi['enabled']}
            uri = self.enable_uri.format(v=v)
            requests.append({'path': uri, 'method': self.patch_method_value, 'data': payload})

        if to_modify_afi.get('verify_mac') is not None:
            payload = {'openconfig-dhcp-snooping:dhcpv{v}-verify-mac-address'.format(v=v): to_modify_afi['verify_mac']}
            uri = self.verify_mac_uri.format(v=v)
            requests.append({'path': uri, 'method': self.patch_method_value, 'data': payload})

        if to_modify_afi.get('trusted'):
            for intf in to_modify_afi.get('trusted'):
                intf_name = intf.get("intf_name")
                if intf_name:
                    payload = {'openconfig-interfaces:dhcpv{v}-snooping-trust'.format(v=v): 'ENABLE'}
                    uri = self.trusted_uri.format(name=intf_name, v=v)
                    requests.append({'path': uri, 'method': self.patch_method_value, 'data': payload})

        if to_modify_afi.get('vlans'):
            for vlan_id in to_modify_afi.get('vlans'):
                payload = {'sonic-vlan:dhcpv{v}_snooping_enable'.format(v=v): 'enable'}
                uri = self.vlans_uri.format(vlan_name='Vlan' + vlan_id, v=v)
                requests.append({'path': uri, 'method': self.patch_method_value, 'data': payload})

        if to_modify_afi.get('source_bindings'):
            entries = []
            for entry in to_modify_afi.get('source_bindings'):
                if entry.get('mac_addr'):
                    entries.append({
                        'mac': entry.get('mac_addr'),
                        'iptype': 'ipv' + str(v),
                        'config': {
                            'mac': entry.get('mac_addr'),
                            'iptype': 'ipv' + str(v),
                            'vlan': "Vlan" + str(entry.get('vlan_id')),
                            'interface': entry.get('intf_name'),
                            'ip': entry.get('ip_addr'),
                        }
                    })
                
            payload = {'openconfig-dhcp-snooping:entry': entries}
            uri = self.binding_uri
            requests.append({'path': uri, 'method': self.patch_method_value, 'data': payload})

        return requests

    def get_single_afi_delete_requests(self, want, have):
        sent_commands = {}
        requests = []

        if want.get('enabled') is True and have.get('enabled') is True:
            # only need to send a request if want from playbook is set to non default value and the setting currently configured is non default
            sent_commands.update({"enabled": want.get("enabled")})
            requests.extend(self.get_delete_enabled_request(want))
        if want.get('verify_mac') is True and have.get('verify_mac') is True:
            sent_commands.update({"verify_mac": want.get("verify_mac")})
            requests.extend(self.get_delete_verify_mac_request(want))
        if want.get('vlans') is not None and have.get('vlans') is not None and have.get("vlans") != []:
            # gathering list of vlans to be deleted. this section also handles cases where empty list of vlans is passed in
            # which means delete all vlans
            to_delete_vlans = have["vlans"]
            if len(want["vlans"]) > 0:
                to_delete_vlans = list(set(have.get("vlans", [])).intersection(set(want.get("vlans", []))))
            to_delete = {"afi": want["afi"], "vlans": to_delete_vlans}
            if len(to_delete["vlans"]):
                sent_commands.update({"vlans": deepcopy(to_delete_vlans)})
                requests.extend(self.get_delete_vlans_requests(to_delete))
        if want.get('trusted') is not None and have.get('trusted') is not None and have.get('trusted') != []:
            # gathering list of interfaces to be deleted. this section also handles cases where empty list of interfaces is passed in which
            #  means delete all trusted interfaces
            to_delete_trusted = have["trusted"]
            if len(want["trusted"]) > 0:
                to_delete_trusted = want["trusted"]
                # removing interfaces that don't exist on device
                for intf in list(to_delete_trusted):
                    if intf not in have["trusted"]:
                        to_delete_trusted.remove(intf)
            to_delete = {"afi": want["afi"], "trusted": to_delete_trusted}
            if len(to_delete["trusted"]):
                sent_commands.update({"trusted": deepcopy(to_delete_trusted)})
                requests.extend(self.get_delete_trusted_requests(to_delete))
        if want.get('source_bindings') is not None and have.get('source_bindings') is not None and have.get('source_bindings') != []:
            # gathering list of source bindings to be deleted. this section also handles cases where empty list of bindings is passed in which
            #  means delete all trusted bindings
            to_delete_bindings = have["source_bindings"]
            if len(want["source_bindings"]) > 0:
                to_delete_bindings = want["source_bindings"]
                # removing bindings that don't exist on device
                for binding in list(to_delete_bindings):
                    if binding not in have["source_bindings"]:
                        to_delete_bindings.remove(binding)
            to_delete = {"afi": want["afi"], "source_bindings": to_delete_bindings}
            if len(to_delete["source_bindings"]):
                sent_commands.update({"source_bindings": deepcopy(to_delete_bindings)})
                requests.extend(self.get_delete_specific_source_bindings_requests(to_delete))

        return sent_commands, requests

    def get_delete_all_have_requests(self, afis):
        '''creates and builds list of requests to delete all current dhcp snooping config for ipv4 and ipv6'''
        requests = []
        requests.extend(self.get_single_afi_delete_requests(afis.get('have_ipv4'), afis.get('have_ipv4'))[1])
        requests.extend(self.get_single_afi_delete_requests(afis.get('have_ipv6'), afis.get('have_ipv6'))[1])

        return requests

    def get_single_afi_replace_requests(self, want, have):
        commands = {}
        requests = []
        to_merge = {}

        diff_requested = get_diff(want, have, test_keys=self.test_keys)
        diff_unwanted = get_diff(have, want, self.test_keys)
        if "enabled" in want and "enabled" in have:
            if want["enabled"] != have["enabled"]:
                to_merge["enabled"] = want["enabled"]
        elif "enabled" in want:
            to_merge["enabled"] = want["enabled"]

        if "verify_mac" in want and "verify_mac" in have:
            if want["verify_mac"] != have["verify_mac"]:
                to_merge["verify_mac"] = want["verify_mac"]
        elif "verify_mac" in want:
            to_merge["verify_mac"] = want["verify_mac"]

        if "vlans" in want and "vlans" in have:
            if diff_unwanted.get("vlans"):
                # delete any vlans that are different
                to_delete = {"afi": have["afi"], "vlans": diff_unwanted["vlans"]}
                commands["vlans"] = deepcopy(diff_unwanted["vlans"])
                requests.extend(self.get_delete_vlans_requests(to_delete))
                to_merge["vlans"] = want["vlans"]
        elif "vlans" in want:
            to_merge["vlans"] = want["vlans"]
        return commands, requests, to_merge
















































    def get_delete_specific_requests(self, afis):
        '''creates and returns list of requests to delete afi settings.
           Checks if clearing settings for a ip family or just matching fields in config'''
        modified_afi_commands = []
        requests = []

        want_ipv4 = afis.get('want_ipv4')
        want_ipv6 = afis.get('want_ipv6')
        have_ipv4 = afis.get('have_ipv4')
        have_ipv6 = afis.get('have_ipv6')

        if want_ipv4:
            if want_ipv4.keys() == set(["afi", "enabled", "verify_mac"])\
                    and self.defaults_unchanged(want_ipv4):
                # AFI dict specified in playbook looks like it's default, taking this to mean want to clear all settings for AFI
                modified_afi_commands.append(deepcopy(have_ipv4))
                requests.extend(self.get_delete_all_afi_requests(have_ipv4))
            else:
                ipv4_commands, ipv4_requests = self.get_delete_specific_afi_fields_requests(want_ipv4, have_ipv4)
                requests.extend(ipv4_requests)
                if ipv4_commands:
                    ipv4_commands["afi"] = want_ipv4["afi"]
                    modified_afi_commands.append(ipv4_commands)
        if want_ipv6:
            if want_ipv6.keys() == set(["afi", "enabled", "verify_mac"])\
                    and self.defaults_unchanged(want_ipv6):
                modified_afi_commands.append(deepcopy(have_ipv6))
                requests.extend(self.get_delete_all_afi_requests(have_ipv6))
            else:
                ipv6_commands, ipv6_requests = self.get_delete_specific_afi_fields_requests(want_ipv6, have_ipv6)
                requests.extend(ipv6_requests)
                if ipv6_commands:
                    ipv6_commands["afi"] = want_ipv6["afi"]
                    modified_afi_commands.append(ipv6_commands)

        sent_commands = []
        if modified_afi_commands:
            sent_commands = {"afis": modified_afi_commands}

        return sent_commands, requests

    def get_delete_all_afi_requests(self, afi_config):
        '''builds and return all requests needed to delete all config for one ip family of dhcp snooping'''
        requests = []
        if afi_config:
            if afi_config.get('enabled') is True:
                requests.extend(self.get_delete_enabled_request(afi_config))
            if afi_config.get('verify_mac') is True:
                requests.extend(self.get_delete_verify_mac_request(afi_config))
            if afi_config.get('vlans'):
                requests.extend(self.get_delete_vlans_requests(afi_config))
            if afi_config.get('trusted'):
                requests.extend(self.get_delete_trusted_requests(afi_config))
            if afi_config.get('source_bindings'):
                requests.extend(self.get_delete_all_source_bindings_request())
        return requests

    def get_delete_specific_afi_fields_requests(self, want_afi, have_afi):
        '''creates and builds list of requests for deleting some fields of dhcp snooping config for
        one ip family. Each field checked and deleted independently from each other depending on if
        it is specified in playbook and matches with current config'''
        sent_commands = {}
        requests = []

        if want_afi.get('enabled') is True and have_afi.get('enabled') is True:
            # only need to send a request if want from playbook is set to non default value and the setting currently configured is non default
            sent_commands.update({"enabled": want_afi.get("enabled")})
            requests.extend(self.get_delete_enabled_request(want_afi))
        if want_afi.get('verify_mac') is True and have_afi.get('verify_mac') is True:
            sent_commands.update({"verify_mac": want_afi.get("verify_mac")})
            requests.extend(self.get_delete_verify_mac_request(want_afi))
        if want_afi.get('vlans') is not None and have_afi.get('vlans') is not None and have_afi.get("vlans") != []:
            # gathering list of vlans to be deleted. this section also handles cases where empty list of vlans is passed in
            # which means delete all vlans
            to_delete_vlans = have_afi["vlans"]
            if len(want_afi["vlans"]) > 0:
                to_delete_vlans = list(set(have_afi.get("vlans", [])).intersection(set(want_afi.get("vlans", []))))
            to_delete = {"afi": want_afi["afi"], "vlans": to_delete_vlans}
            if len(to_delete["vlans"]):
                sent_commands.update({"vlans": deepcopy(to_delete_vlans)})
                requests.extend(self.get_delete_vlans_requests(to_delete))
        if want_afi.get('trusted') is not None and have_afi.get('trusted') is not None and have_afi.get('trusted') != []:
            # gathering list of interfaces to be deleted. this section also handles cases where empty list of interfaces is passed in which
            #  means delete all trusted interfaces
            to_delete_trusted = have_afi["trusted"]
            if len(want_afi["trusted"]) > 0:
                to_delete_trusted = want_afi["trusted"]
                # removing interfaces that don't exist on device
                for intf in list(to_delete_trusted):
                    if intf not in have_afi["trusted"]:
                        to_delete_trusted.remove(intf)
            to_delete = {"afi": want_afi["afi"], "trusted": to_delete_trusted}
            if len(to_delete["trusted"]):
                sent_commands.update({"trusted": deepcopy(to_delete_trusted)})
                requests.extend(self.get_delete_trusted_requests(to_delete))
        if want_afi.get('source_bindings') is not None and have_afi.get('source_bindings') is not None and have_afi.get('source_bindings') != []:
            # gathering list of source bindings to be deleted. this section also handles cases where empty list of bindings is passed in which
            #  means delete all trusted bindings
            to_delete_bindings = have_afi["source_bindings"]
            if len(want_afi["source_bindings"]) > 0:
                to_delete_bindings = want_afi["source_bindings"]
                # removing bindings that don't exist on device
                for binding in list(to_delete_bindings):
                    if binding not in have_afi["source_bindings"]:
                        to_delete_bindings.remove(binding)
            to_delete = {"afi": want_afi["afi"], "source_bindings": to_delete_bindings}
            if len(to_delete["source_bindings"]):
                sent_commands.update({"source_bindings": deepcopy(to_delete_bindings)})
                requests.extend(self.get_delete_specific_source_bindings_requests(to_delete))

        return sent_commands, requests

    def get_delete_enabled_request(self, afi):
        '''makes and returns request to "delete" aka reset to default the enabled setting for one afi family. returns as a list'''
        payload = {'openconfig-dhcp-snooping:dhcpv{v}-admin-enable'.format(v=self.afi_to_vnum(afi)): False}
        return [{'path': self.enable_uri.format(v=self.afi_to_vnum(afi)), 'method': self.patch_method_value, 'data': payload}]

    def get_delete_verify_mac_request(self, afi):
        '''makes and returns request to "delete" aka reset to default the config for one afi family's verify mac setting'''
        payload = {'openconfig-dhcp-snooping:dhcpv{v}-verify-mac-address'.format(v=self.afi_to_vnum(afi)): True}
        return [{'path': self.verify_mac_uri.format(v=self.afi_to_vnum(afi)), 'method': self.patch_method_value, 'data': payload}]

    def get_delete_vlans_requests(self, afi):
        '''makes and returns request to delete the given vlans for the given afi faimily.
        input expected as a dictionary of form {"afi": <ip_version>, "vlans": <list_of_vlans>}'''
        requests = []
        if afi.get('vlans'):
            for vlan_id in afi.get('vlans'):
                requests.append({
                    'path': self.vlans_uri.format(vlan_name='Vlan' + vlan_id, v=self.afi_to_vnum(afi)),
                    'method': self.delete_method_value
                })
        return requests

    def get_delete_trusted_requests(self, afi):
        '''makes and returns request to delete the given trusted interfaces for the given afi faimily.
        input expected as a dictionary of form {"afi": <ip_version>, "trusted": [{"intf_name": <name>}...]}'''
        requests = []
        if afi.get('trusted'):
            for intf in afi.get('trusted'):
                intf_name = intf.get('intf_name')
                if intf_name:
                    requests.append({
                        'path': self.trusted_uri.format(name=intf_name, v=self.afi_to_vnum(afi)),
                        'method': self.delete_method_value
                    })
        return requests

    def get_delete_all_source_bindings_request(self):
        '''creates request to delete the source bindings list'''
        return [{'path': self.binding_uri, 'method': self.delete_method_value}]

    def get_delete_specific_source_bindings_requests(self, afi):
        '''creates and builds a list of requests to delete the source bindings listed in the given afi family
        input expected as a dictionary of form to_delete = {"afi": <ip_version>, "source_bindings": <list of source_bindings>}'''
        requests = []
        for entry in afi.get('source_bindings'):
            if entry.get('mac_addr'):
                requests.append({
                    'path': self.binding_uri + '={mac},{ipv}'.format(mac=entry.get('mac_addr'), ipv=afi.get('afi')),
                    'method': self.delete_method_value
                })
        return requests

    def get_delete_individual_source_bindings_requests(self, afi, entry):
        '''create a request to delete the given source binding entry and address family specified
        by afi'''
        return [{'path': self.binding_uri + '={mac},{ipv}'.format(mac=entry.get('mac_addr'), ipv=afi.get('afi')), 'method': self.delete_method_value}]

    def get_delete_replaced_groupings(self, afis):
        '''builds list of requests to handle replaced state for both address families'''
        modified_afi_commands = []
        requests = []

        want_ipv4 = afis.get('want_ipv4')
        have_ipv4 = afis.get('have_ipv4')
        want_ipv6 = afis.get('want_ipv6')
        have_ipv6 = afis.get('have_ipv6')

        if want_ipv4 and have_ipv4:
            ipv4_commands, ipv4_requests = self.get_delete_replaced_groupings_afi(want_ipv4, have_ipv4)
            requests.extend(ipv4_requests)
            if ipv4_commands:
                ipv4_commands["afi"] = want_ipv4["afi"]
                modified_afi_commands.append(ipv4_commands)
        if want_ipv6 and have_ipv6:
            ipv6_commands, ipv6_requests = self.get_delete_replaced_groupings_afi(want_ipv6, have_ipv6)
            requests.extend(ipv6_requests)
            if ipv6_commands:
                ipv6_commands["afi"] = want_ipv6["afi"]
                modified_afi_commands.append(ipv6_commands)

        sent_commands = []
        if modified_afi_commands:
            sent_commands = {"afis": modified_afi_commands}

        return sent_commands, requests

    def get_delete_replaced_groupings_afi(self, want_afi, have_afi):
        '''creates and builds a list of requests to handle all parts that need to be deleted
        while handling the replaced state for an address family'''
        sent_commands = {}
        requests = []
        diff_requested = get_diff(have_afi, want_afi, self.test_keys)

        if diff_requested.get("vlans") and "vlans" in want_afi:
            # delete any vlans that are different
            to_delete = {"afi": have_afi["afi"], "vlans": diff_requested["vlans"]}
            sent_commands["vlans"] = deepcopy(diff_requested["vlans"])
            requests.extend(self.get_delete_vlans_requests(to_delete))
        if diff_requested.get('trusted') and 'trusted' in want_afi:
            # delete anything that has a difference, covers things that are
            # in have but not want and things in both but modified
            to_delete = {"afi": have_afi["afi"], "trusted": diff_requested["trusted"]}
            sent_commands["trusted"] = deepcopy(diff_requested["trusted"])
            requests.extend(self.get_delete_trusted_requests(to_delete))
        if diff_requested.get('source_bindings') and 'source_bindings' in want_afi:
            # assuming source bindings considered a replaceable subsection ie the list afterwards
            # should look exactly like what was passed into want
            if want_afi["source_bindings"] == []:
                sent_commands["source_bindings"] = deepcopy(have_afi["source_bindings"])
                requests.extend(self.get_delete_all_source_bindings_request())
            else:
                sent_commands["source_bindings"] = deepcopy(diff_requested["source_bindings"])
                for entry in diff_requested["source_bindings"]:
                    requests.extend(self.get_delete_individual_source_bindings_requests(have_afi, entry))
        return sent_commands, requests
    
    def prep_replaced_to_merge(self, diff, afis):
        print("getting replaced merged set up", diff)
        if not diff or not diff.get("afis"):
            return {}
        for diff_afi in diff["afis"]:
            if "source_bindings" in diff_afi:
                for binding in diff_afi["source_bindings"]:
                    binding.update(self.match_binding(binding["mac_addr"], afis["want_"+diff_afi["afi"]]["source_bindings"]))
            if "vlans" in afis["want_"+diff_afi["afi"]]:
                pass

    def match_binding(self, mac_addr, bindings):
        for binding in bindings:
            if binding["mac_addr"] == mac_addr:
                return binding
        return {}

    @staticmethod
    def defaults_unchanged(afi):
        if afi.get('enabled') is False and afi.get('verify_mac') is False:
            return True
        else:
            return False

    @staticmethod
    def afi_to_vnum(afi):
        if afi.get('afi') == 'ipv6':
            return '6'
        else:
            return '4'
