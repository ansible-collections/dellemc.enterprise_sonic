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
    poe_enum2str,
    poe_str2enum,
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
        commands = []
        requests = []
        return commands, requests

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
        return commands, requests
    
    def validate_poe_config(self, config):
        '''validate passed in config is argspec compliant. Also does checks on values in ranges that ansible might not do'''
        validated_config = validate_config(self._module.argument_spec, config)
        if "interfaces" in config and config["interfaces"] is not None:
            for interface in config["interfaces"]:
                if "power_limit" in interface and interface["power_limit"] is not None\
                    and interface["power_limit"] not in range(0,99900):
                    raise Exception("interface {intf_name} has invalid power limit, must be between 0 and 99900".format(intf_name=interface['name']))
        if "cards" in config and config["cards"] is not None:
            for card in config["cards"]:
                if "usage_threshold" in card and card["usage_threshold"] is not None\
                    and card["usage_threshold"] not in range(1,99):
                    raise Exception("card {id} has invalid usage threshold value, must be between 1 and 99".format(id=card["card_id"]))
        if "global" in config and config["global"] is not None:
            if "usage_threshold" in config["global"] and config["global"]["usage_threshold"] is not None\
                and config["global"]["usage_threshold"] not in range(1,99):
                raise Exception("global config has invalid usage threshold value, must be between 1 and 99")
        #TODO: check for other things that ansible won't be able to validate

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
        config_body["power-management-model"] = global_config.get("power_mgmt_model")
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
            card_body["power-management-model"] = card_config.get("power_mgmt_model")
            card_body["power-usage-threshold"] = card_config.get("usage_threshold")
            card_body = remove_empties(card_body)
            if len(card_body) > 0:
                # if none of settings that could be changed found to have values to change, don't want any entry recording it
                # that would throw off detecting if changes were made
                card_body["card-id"] = card_config["card_id"]
                card_list.append({"card-id": card_config["card_id"], "config": card_body})
        return card_list
    
    def make_interfaces_requests(self, interfaces_config):
        '''make request to patch in changes to multiple interfaces' PoE settings
        
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
            interface_body[self.poe_setting_prefix + "enabled"] = interface_config["enabled"]
        if "four_pair" in interface_config:
            interface_body[self.poe_setting_prefix + "four-pair-mode"] = interface_config["four_pair"]
        if "high_power" in interface_config:
            interface_body[self.poe_setting_prefix + "high-power-mode"] = interface_config["high_power"]
        if "power_classification" in interface_config:
            interface_body[self.poe_setting_prefix + "classification-mode"] = \
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
