#
# -*- coding: utf-8 -*-
# Copyright 2023 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_poe class
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
    validate_config,
    remove_empties,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import Facts
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils \
    import (
        get_diff,
        update_states,
        to_request,
        edit_config
    )
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.poe_utils import (
    poe_str2enum,
    remove_none
)

from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.formatted_diff_utils import (
    get_new_config,
    get_formatted_config_diff
)


class Poe(ConfigBase):
    """
    The sonic_poe class
    """

    diff_keys = [
        {"cards": {"card_id": ""}},
        {"interfaces": {"name": ""}}
    ]

    poe_root_uri = "data/openconfig-poe:poe"
    interfaces_root_uri = "data/openconfig-interfaces:interfaces"

    poe_setting_prefix = "openconfig-if-poe-ext:"
    '''prefix for interface's PoE settings'''

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'poe',
    ]

    def __init__(self, module):
        super(Poe, self).__init__(module)

    def get_poe_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        poe_facts = facts['ansible_network_resources'].get('poe')
        if not poe_facts:
            return []
        return poe_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = list()

        existing_poe_facts = self.get_poe_facts()
        commands, requests = self.set_config(existing_poe_facts)

        if commands and len(requests) > 0:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.errno)
            result['changed'] = True
        result['commands'] = commands

        changed_poe_facts = self.get_poe_facts()

        result['before'] = existing_poe_facts
        if result['changed']:
            result['after'] = changed_poe_facts

        new_config = changed_poe_facts
        if self._module.check_mode:
            result.pop('after', None)
            new_config = get_new_config(commands, existing_poe_facts,
                                        self.diff_keys)
            result['after(generated)'] = new_config

        if self._module._diff:
            result['config_diff'] = get_formatted_config_diff(existing_poe_facts,
                                                              new_config)

        result['warnings'] = warnings
        return result

    def set_config(self, existing_poe_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']
        have = existing_poe_facts
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
        want = remove_none(want)
        if state == 'overridden':
            result = self._state_overridden(want, have)
        elif state == 'deleted':
            result = self._state_deleted(want, have)
        elif state == 'merged':
            result = self._state_merged(want, have)
        elif state == 'replaced':
            result = self._state_replaced(want, have)
        return result

    def _state_replaced(self, want, have):
        """ The command generator when state is replaced

        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        # is like override but only want to override sections that were specified in playbook, so reusing override and supplimenting with have values
        # where overridde should ignore
        if "global" in have:
            if "global" not in want:
                want["global"] = {}
            if "auto_reset" in have["global"] and "auto_reset" not in want.get("global", {}):
                want["global"]["auto_reset"] = have["global"]["auto_reset"]
            if "power_mgmt_model" in have["global"] and "power_mgmt_model" not in want.get("global", {}):
                want["global"]["power_mgmt_model"] = have["global"]["power_mgmt_model"]
            if "usage_threshold" in have["global"] and "usage_threshold" not in want.get("global", {}):
                want["global"]["usage_threshold"] = have["global"]["usage_threshold"]
        if "cards" in have and "cards" not in want:
            want["cards"] = have["cards"]
        if "interfaces" in have and "interfaces" not in want:
            want["interfaces"] = have["interfaces"]

        return self._state_overridden(want, have)

    def _state_overridden(self, want, have):
        """ The command generator when state is overridden

        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        requests = []
        remove_diff = get_diff(have, want, test_keys=self.diff_keys)
        introduced_diff = get_diff(want, have, test_keys=self.diff_keys)

        remove_diff = self.find_substitution_deletes(remove_diff, introduced_diff)
        self.prep_merge_diff(introduced_diff, want)

        if remove_diff is not None and len(remove_diff) > 0:
            # deleted will take empty as clear all, override having empty remove differences is do nothing.
            # so need to check
            commands, requests = self._state_deleted(remove_diff, have)
        commandsTwo, requestsTwo = self._state_merged(introduced_diff, have)
        commands.extend(commandsTwo)
        requests.extend(requestsTwo)
        return commands, requests

    def _state_merged(self, want, have):
        """ The generator that builds commands and requests needed when state is merged

        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :rtype: A tuple of lists
        :returns: first element is the commands that caused changes to device config,
                  the second element is the list of requests needed to get to desired state
        """
        commands = []
        requests = []
        if want is None:
            # just in case no value for config
            want = {}
        else:
            want = remove_empties(want)
            self.validate_poe_config({"config": want})

        # merged only cares about things in want that are different from have. that's the exact list of changes
        commands = get_diff(want, have, test_keys=self.diff_keys)
        self.prep_merge_diff(commands, want)
        requests = self.make_merged_requests(commands, [])

        if commands and len(requests) > 0:
            commands = update_states(commands, "merged")
        else:
            commands = []
        return commands, requests

    def _state_deleted(self, want, have):
        """ The command generator when state is deleted

        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        commands = []
        requests = []
        if not have:
            # nothing that could be deleted
            return commands, requests
        elif not want:
            # giving an option to clear all, either None or empty config dict
            want = deepcopy(have)

        commands, requests = self.make_delete_requests(want, have)

        if commands and len(requests) > 0:
            commands = update_states(commands, "deleted")
        else:
            commands = []
        return commands, requests

    def validate_poe_config(self, config):
        '''validate passed in config is argspec compliant. Also does checks on values in ranges that ansible might not do'''
        validate_config(self._module.argument_spec, config)
        if "interfaces" in config and config["interfaces"] is not None:
            for interface in config["interfaces"]:
                if "power_limit" in interface and interface["power_limit"] is not None\
                        and interface["power_limit"] not in range(0, 99900):
                    raise Exception("interface {intf_name} has invalid power limit, must be between 0 and 99900".format(intf_name=interface['name']))
        if "cards" in config and config["cards"] is not None:
            for card in config["cards"]:
                if "usage_threshold" in card and card["usage_threshold"] is not None\
                        and card["usage_threshold"] not in range(1, 99):
                    raise Exception("card {id} has invalid usage threshold value, must be between 1 and 99".format(id=card["card_id"]))
        if "global" in config and config["global"] is not None:
            if "usage_threshold" in config["global"] and config["global"]["usage_threshold"] is not None\
                    and config["global"]["usage_threshold"] not in range(1, 99):
                raise Exception("global config has invalid usage threshold value, must be between 1 and 99")
        # TODO: check for other things that ansible won't be able to validate

    def make_merged_requests(self, commands, requests):
        '''append all requests needed to merge in requested changes

        :param commands: requested changes to all PoE config in PoE argspec format'''
        requests.extend(self.make_patch_poe_root_request(commands))

        if "interfaces" in commands:
            requests.extend(self.make_interfaces_requests(commands["interfaces"]))
        return requests

    def make_patch_poe_root_request(self, commands):
        '''builds request to patch changes to PoE root, and adds to request list if there's data to change

        :param commands: requested changes to all PoE config in PoE argspec format'''
        requests = []
        root_request_body = {}
        cards_list_body = self.make_cards_list_request_body(commands.get("cards", {}))
        if len(cards_list_body) > 0:
            root_request_body.update({"cards": {"card": cards_list_body}})
        global_config_body = self.make_global_config_request_body(commands.get("global", {}))
        if len(global_config_body) > 0:
            root_request_body.update({"global": {"config": global_config_body}})

        if len(root_request_body) > 0:
            requests.append(
                {
                    "path": self.poe_root_uri,
                    "method": "patch",
                    "data": {"openconfig-poe:poe": root_request_body}
                }
            )
        return requests

    def make_global_config_request_body(self, global_config):
        '''make the body for a patch/put request that changes global PoE config.

        :param global_config: the global section of PoE config in PoE argspec format

        :rtype: a dictionary
        :returns: REST API format dictionary holding the global PoE settings passed in'''
        config_body = {}
        config_body["auto-reset-mode"] = global_config.get("auto_reset")
        config_body["power-management-model"] = poe_str2enum(global_config.get("power_mgmt_model"))
        config_body["power-usage-threshold"] = global_config.get("usage_threshold")
        return remove_empties(config_body)

    def make_cards_list_request_body(self, cards_config):
        '''make the body for a patch/put request that changes cards.

        :param cards_config: list of PoE cards' config dictionaries in PoE argspec format

        :rtype: list
        :returns: a list of cards and config in the REST API's format for PoE cards'''
        card_list = []
        for card_config in cards_config:
            card_body = {}
            card_body["auto-reset-mode"] = card_config.get("auto_reset")
            card_body["power-management-model"] = poe_str2enum(card_config.get("power_mgmt_model"))
            card_body["power-usage-threshold"] = card_config.get("usage_threshold")
            card_body = remove_empties(card_body)
            if len(card_body) > 0:
                # if none of settings that could be changed found to have values to change, don't want any entry recording it
                # that would throw off detecting if changes were made
                card_body["card-id"] = card_config["card_id"]
                card_list.append({"card-id": card_config["card_id"], "config": card_body})
        return card_list

    def make_interfaces_requests(self, interfaces_config):
        '''build the request to patch in changes to multiple interfaces' PoE settings

        :param interfaces_config: list of interfaces' PoE config dictionaries in PoE argspec format

        :rtype: list
        :returns: A list of requests needed to patch in the requested changes to interfaces' PoE config'''
        requests = []
        interfaces_body = []

        for interface_config in interfaces_config:
            interface_body = self.make_interface_request_body(interface_config)
            if len(interface_body) > 0:
                # module knowing whether or not changes were made depends on if there are requests,
                # so need to make sure all data and requests are in fact making changes
                interfaces_body.append(
                    {
                        "name": interface_config["name"],
                        "openconfig-if-ethernet:ethernet": {
                            "openconfig-if-poe:poe": {"config": interface_body}
                        }
                    }
                )
        if len(interfaces_body) > 0:
            requests.append(
                {
                    "path": self.interfaces_root_uri,
                    # don't use PUT. PoE is only a subsection of all interface settings and this resource
                    # module will only ever handling that subsection and PUT will erase all other subsections
                    "method": "patch",
                    "data": {
                        "openconfig-interfaces:interfaces": {
                            "interface": interfaces_body
                        }
                    }
                }
            )
        return requests

    def make_interface_request_body(self, interface_config):
        '''make the body for a patch/put request that changes PoE settings on an interface.

        :param interface_confg: dictionary in PoE argspec format that holds the PoE config for one interface

        :rtype: dictionary
        :returns: REST API format dictionary holding the PoE settings passed in'''
        interface_body = {}
        # doing a bunch of if checks because only some of these need translation function calls
        if "detection" in interface_config:
            interface_body[self.poe_setting_prefix + "detection-mode"] = poe_str2enum("detection-" + interface_config["detection"])
        if "disconnect_type" in interface_config:
            interface_body[self.poe_setting_prefix + "disconnect-type"] = poe_str2enum(interface_config["disconnect_type"])
        if "enabled" in interface_config:
            interface_body["enabled"] = interface_config["enabled"]
        if "four_pair" in interface_config:
            interface_body[self.poe_setting_prefix + "four-pair-mode"] = interface_config["four_pair"]
        if "high_power" in interface_config:
            interface_body[self.poe_setting_prefix + "high-power-mode"] = interface_config["high_power"]
        if "power_classification" in interface_config:
            interface_body[self.poe_setting_prefix + "power-classification-mode"] = \
                poe_str2enum(interface_config["power_classification"])
        if "power_limit" in interface_config:
            interface_body[self.poe_setting_prefix + "power-limit"] = interface_config["power_limit"]
        if "power_limit_type" in interface_config:
            interface_body[self.poe_setting_prefix + "power-limit-type"] = \
                poe_str2enum(interface_config["power_limit_type"])
        if "power_limit_type" in interface_config:
            interface_body[self.poe_setting_prefix + "power-pairs"] = poe_str2enum(interface_config["power_pairs"])
        if "power_up_mode" in interface_config:
            interface_body[self.poe_setting_prefix + "powerup-mode"] = poe_str2enum(interface_config["power_up_mode"])
        if "priority" in interface_config:
            interface_body[self.poe_setting_prefix + "priority"] = interface_config["priority"].upper()
        if "use_spare_pair" in interface_config:
            interface_body[self.poe_setting_prefix + "use-spare-pair"] = interface_config["use_spare_pair"]
        return interface_body

    def make_delete_requests(self, want, have):
        deleted_config = {}
        deleted_requests = []

        if want.get("cards") is not None and have.get("cards"):
            # if there's no existing cards or empty list, nothing to delete. can skip
            # accepting empty list for want though, as a clear everthing command.
            cards_delete_commands, cards_delete_requests = \
                make_list_delete_requests(
                    want.get("cards", []),
                    have.get("cards", []),
                    self.make_delete_card_requests,
                    self.diff_keys[0]['cards'])
            if cards_delete_commands:
                deleted_config["cards"] = cards_delete_commands
                deleted_requests.extend(cards_delete_requests)

        if want.get("interfaces") is not None and have.get("interfaces"):
            # only need to consider what requests are needed to delete card settings if both want and have have interfaces
            interfaces_delete_commands, interfaces_delete_requests = \
                make_list_delete_requests(
                    want.get("interfaces", []),
                    have.get("interfaces", []),
                    self.make_delete_interface_requests,
                    self.diff_keys[1]['interfaces'])
            if interfaces_delete_commands:
                deleted_config["interfaces"] = interfaces_delete_commands
                deleted_requests.extend(interfaces_delete_requests)

        if "global" in want and "global" in have:
            deleted_global_settings = {}
            if "auto_reset" in want["global"] and "auto_reset" in have["global"] and want["global"]["auto_reset"] == have["global"]["auto_reset"]:
                # want to make sure setting specified and match
                deleted_global_settings.update({"auto_reset": have["global"]["auto_reset"]})
                deleted_requests.append({"path": "data/openconfig-poe:poe/global/config/auto-reset-mode", "method": "DELETE"})
            if "power_mgmt_model" in want["global"] and "power_mgmt_model" in have["global"] and \
                    want["global"]["power_mgmt_model"] == have["global"]["power_mgmt_model"]:
                # want to make sure setting specified and match
                deleted_global_settings.update({"power_mgmt_model": have["global"]["power_mgmt_model"]})
                deleted_requests.append({"path": "data/openconfig-poe:poe/global/config/power-management-model", "method": "DELETE"})
            if "usage_threshold" in want["global"] and "usage_threshold" in have["global"] and \
                    want["global"]["usage_threshold"] == have["global"]["usage_threshold"]:
                # want to make sure setting specified and match
                deleted_global_settings.update({"usage_threshold": have["global"]["usage_threshold"]})
                deleted_requests.append({"path": "data/openconfig-poe:poe/global/config/power-usage-threshold", "method": "DELETE"})
            if len(deleted_global_settings) > 0:
                deleted_config["global"] = deleted_global_settings
        return deleted_config, deleted_requests

    def make_delete_card_requests(self, have_card):
        commands = have_card
        requests = [{"path": "data/openconfig-poe:poe/cards/card={card_id}".format(card_id=have_card["card_id"]), "method": "delete"}]

        return commands, requests

    def make_delete_interface_requests(self, have_interface):
        commands = have_interface
        requests = [
            {
                "path": "data/openconfig-interfaces:interfaces/interface=" + have_interface["name"] +
                "/openconfig-if-ethernet:ethernet/openconfig-if-poe:poe",
                "method": "delete"
            }]

        return commands, requests

    def find_substitution_deletes(self, remove_diff, introduced_diff):
        '''specifically for overridden and replaced states, finds and builds collection of which config settings need to be deleted and without anything that is
        getting replaced with new values. `get_diff` will return collection of both things that need to be deleted and things that will have new values.'''
        result = {}
        if "global" in remove_diff:
            # possible to have global section in only one of two inputs
            result["global"] = {}
            if "auto_reset" in remove_diff["global"] and "auto_reset" not in introduced_diff.get("global", {}):
                result["global"]["auto_reset"] = remove_diff["global"]["auto_reset"]
            if "power_mgmt_model" in remove_diff["global"] and "power_mgmt_model" not in introduced_diff.get("global", {}):
                result["global"]["power_mgmt_model"] = remove_diff["global"]["power_mgmt_model"]
            if "usage_threshold" in remove_diff["global"] and "usage_threshold" not in introduced_diff.get("global", {}):
                result["global"]["usage_threshold"] = remove_diff["global"]["usage_threshold"]
        if "cards" in remove_diff:
            result["cards"] = remove_diff["cards"]
        if "interfaces" in remove_diff:
            result["interfaces"] = remove_diff["interfaces"]
        return result

    def prep_merge_diff(self, diff, want):
        if "cards" in diff:
            searched_test_keys = None
            for item in self.diff_keys:
                for k, v in item.items():
                    if k == "cards":
                        searched_test_keys = v
                        break
            want_index = build_ref_dict(want["cards"], searched_test_keys)
            for card in diff["cards"]:
                item_key = find_item_key(card, searched_test_keys)
                card.update(want_index.get(item_key, {}))

        if "interfaces" in diff:
            searched_test_keys = None
            for item in self.diff_keys:
                for k, v in item.items():
                    if k == "interfaces":
                        searched_test_keys = v
                        break
            want_index = build_ref_dict(want["interfaces"], searched_test_keys)
            for interface in diff["interfaces"]:
                item_key = find_item_key(interface, searched_test_keys)
                interface.update(want_index.get(item_key, {}))


def make_list_delete_requests(want_list, have_list, delete_callback, test_keys=None):
    '''generic helper for a list'''
    deleted_config = []
    deleted_requests = []
    # making it easier to find have items
    have_dict = build_ref_dict(have_list, test_keys)

    # to de-duplicate any incoming values
    to_delete_list = build_ref_dict(want_list if len(want_list) > 0 else have_list, test_keys)

    for to_delete_key, to_delete_item in to_delete_list.items():
        if to_delete_key in have_dict:
            # only deleting if key is in both
            item_commands, item_requests = delete_callback(have_dict[to_delete_key])

            if item_commands:
                # each item could have multiple changes needed, after each one collect results and add to reports
                deleted_config.append(item_commands)
                deleted_requests.extend(item_requests)

    return deleted_config, deleted_requests


def build_ref_dict(item_list, test_keys=None):
    '''helper that builds a dictionary that acts as an index for a list of config entries.
    If an item is found to appear more than once, merges dictionary config (doesn't merge any sub containers) and replaces existing values for other types.
    helpful when working with config that has a list of items and need to loop through or search multiple times.

    :param item_list: the list of config items to make a dictionary for. items can be primitive or dictionaries. All items must have all fields used as part
    of the key present inside.
    :param test_keys: defines what fields of each list item act as the key to identify the item.
        Pass in None for primitive types or if key is the item itself, otherwise pass in a dictionary where keys are the field names.
    :rtype: a dictionary
    :return: a dictionary where key is a tuple formed from the values of the key fields or the item itself
        and value is the item in the list with duplicate occurances merged.
        does not merge differences in nested dictionaries or lists'''
    search_dict = {}
    if item_list is None:
        # just in case, early break. nothing to build here
        return search_dict

    for item in item_list:
        item_key = find_item_key(item, test_keys)

        if item_key in search_dict and isinstance(search_dict[item_key], dict):
            search_dict[item_key].update(item)
        else:
            search_dict[item_key] = item
    return search_dict


def find_item_key(entry, test_keys=None):
    if test_keys is None:
        return deepcopy(entry)
    else:
        return tuple(entry[k] for k in test_keys)
