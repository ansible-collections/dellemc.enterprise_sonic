#
# -*- coding: utf-8 -*-
# Copyright 2024 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_ospf_area class
It is in this file where the current configuration (as list)
is compared to the provided configuration (as list) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from __future__ import (absolute_import, division, print_function)
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
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils \
    import (
        get_diff,
        update_states,
        to_request,
        edit_config,
        get_replaced_config
    )
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.formatted_diff_utils import (
    get_new_config,
    get_formatted_config_diff
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import Facts


class Ospf_area(ConfigBase):
    """
    The sonic_ospf_area class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'ospf_area',
    ]

    TEST_KEYS = [
        {"config": {"area_id": "", "vrf_name": ""}},
        {"ranges": {"prefix": ""}},
        {"virtual_links": {"router_id": ""}},
        {"message_digest_keys": {"key_id": ""}}
    ]

    ospf_uri = "data/openconfig-network-instance:network-instances/network-instance={vrf}/protocols/protocol=OSPF,ospfv2/ospfv2"
    # URI to ospf settings for one network_instance
    ospf_area_uri = ospf_uri + "/areas/area={area_id}"
    # URI to ospf area settings for one network_instance
    ospf_propagation_uri = ospf_uri + "/global/inter-area-propagation-policies/openconfig-ospfv2-ext:inter-area-policy={area_id}"
    ospf_key_extn = "openconfig-ospfv2-ext:"
    auth_type_conversion = {"message_digest": "MD5HMAC", "text": "TEXT", "none": "NONE"}

    def __init__(self, module):
        super(Ospf_area, self).__init__(module)

    def get_ospf_area_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A list
        :returns: The current configuration as a list of areas' config
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        ospf_area_facts = facts['ansible_network_resources'].get('ospf_area')
        if not ospf_area_facts:
            return []
        return ospf_area_facts["config"]

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = []
        commands = []

        existing_ospf_area_facts = self.get_ospf_area_facts()
        commands, requests = self.set_config(existing_ospf_area_facts)
        if commands and len(requests) > 0:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.code)
            result['changed'] = True
        result['commands'] = commands
        changed_ospf_area_facts = self.get_ospf_area_facts()

        result['before'] = existing_ospf_area_facts
        if result['changed']:
            result['after'] = changed_ospf_area_facts

        # new_config = changed_ospf_area_facts # TODO: check and diff mode not yet supported
        # old_config = existing_ospf_area_facts
        # if self._module.check_mode:
        #     result.pop('after', None)
        #     new_config = get_new_config(commands, existing_ospf_area_facts,
        #                                 self.TEST_KEYS_formatted_diff)
        #     result['after(generated)'] = new_config
        # if self._module._diff:
        #     self.sort_lists_in_config(new_config)
        #     self.sort_lists_in_config(old_config)
        #     result['diff'] = get_formatted_config_diff(old_config,
        #                                                new_config,
        #                                                self._module._verbosity)

        result['warnings'] = warnings
        return result

    def set_config(self, existing_ospf_area_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']
        have = existing_ospf_area_facts

        resp = self.set_state(want, have)
        return to_list(resp)

    def set_state(self, want, have):
        """ Select the appropriate function based on the state provided

        :param want: the desired configuration as a list
        :param have: the current configuration as a list
        :rtype: A tuple
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration, and REST requests that do it
        """
        commands = []
        requests = []
        want = self.validate_normalize_config(want)
        state = self._module.params['state']
        if state == 'deleted':
            commands, requests = self._state_deleted(want, have)
        elif state == 'merged':
            commands, requests = self._state_merged(want, have)
        elif state == 'overridden':
            commands, requests = self._state_overridden(want, have)
        else:
            commands, requests = self._state_replaced(want, have)
        return commands, requests

    def _state_merged(self, want, have):
        """ The command generator when state is merged

        :rtype: A tuple of lists
        :returns: A list of what commands and state necessary to merge the provided into
                  the current configuration, and a list of requests needed to make changes
        """
        commands = []
        requests = []
        if want is None:
            return commands, requests

        diff = get_diff(want, have, test_keys=self.TEST_KEYS)
        requests = self.build_areas_merge_requests(diff)
        commands = diff

        if commands and len(requests) > 0:
            commands = update_states(commands, "merged")
        else:
            commands = []
        return commands, requests

    def _state_deleted(self, want, have):
        """ The command generator when state is deleted

        :rtype: A tuple of lists
        :returns: A list of what commands and state necessary to remove the current configuration
                  of the provided objects, and a list of requests needed to make changes
        """
        commands = []
        requests = []
        if not have:
            return commands, requests
        if not want:
            # empty or None assume delete everything
            commands = have
            return commands, self.build_areas_delete_requests(commands, have, delete_everything=True)
        else:
            diff = get_diff(want, have, test_keys=self.TEST_KEYS)
            # diff is things in want that aren't or different in have
            commands = get_diff(want, diff, test_keys=self.TEST_KEYS)
            # commands is things in want that are in have and are not different aka same
            return commands, self.build_areas_delete_requests(commands, have)
        return commands, requests

    def _state_replaced(self, want, have):
        """ The command generator when state is replaced

        :rtype: A tuple of lists
        :returns: A list of what commands and state necessary to migrate the current configuration
                  to the desired configuration, and a list of requests needed to make changes
        """
        commands = []
        requests = []
        return commands, requests

    def _state_overridden(self, want, have):
        """ The command generator when state is overridden

        :rtype: A tuple of lists
        :returns: A list of what commands and state necessary to migrate the current configuration
                  to the desired configuration, and a list of requests needed to make changes
        """
        commands = []
        requests = []
        return commands, requests

    def validate_normalize_config(self, config):
        '''validates and normalizes interface names in passed in config
        :returns: config object that has been validated and normalized'''
        if not config:
            return []
        config = {"config": config}
        config = remove_empties(config)
        # validate returns validated config that is rooted at the root of argspec and with added nulls for fields of nested objects that
        # didn't have a value passed in but some fields in the object did
        config = validate_config(self._module.argument_spec, config)
        # not really using the none values in this module so getting thrown out. Use empty lists for clear
        config = remove_empties(config)["config"]
        try:
            for area in config:
                area['area_id'] = self.format_area_name(area['area_id'])
        except Exception as exc:
            self._module.fail_json(msg=str(exc))
        return config

    def format_area_name(self, area_id):
        """addresses in playbook can be single numbers or IP addresses, switch works with everything as IP addresses.
        make sure things are in IP format by applying formatting where needed"""
        if area_id.count(".") < 3:
            area_int = int(area_id)
            return ".".join([str(area_int >> 24 & 0xff), str(area_int >> 16 & 0xff), str(area_int >> 8 & 0xff), str(area_int & 0xff)])
        return area_id

    def build_areas_merge_requests(self, want):
        '''takes a list of areas and builds up all requests to patch in wanted changes'''
        requests = []
        formatted_bodies = {}
        # tracking all formatted lists that will go into the final requests for each vrf

        # list of areas not organized by VRF and requests are grouped into VRF so need to sort the areas
        # each area has config that gets mapped into two different subsections of the ospf settings of the VRF:
        # areas and global ospf inter-area-propagation-policies. Want to combine both into one request
        for area in want:
            formatted_area = self.format_area_options_to_rest(area)
            formatted_area_policy = self.format_area_policy_to_rest(area)
            if (formatted_area or formatted_area_policy) and area["vrf_name"] not in formatted_bodies:
                formatted_bodies[area["vrf_name"]] = {"areas": [], "propagation": []}
            if formatted_area:
                formatted_bodies[area["vrf_name"]]["areas"].append(formatted_area)
            if formatted_area_policy:
                formatted_bodies[area["vrf_name"]]["propagation"].append(formatted_area_policy)

        for vrf in formatted_bodies:
            vrf_request_body = {}
            if formatted_bodies[vrf]["areas"]:
                vrf_request_body[self.ospf_key_extn + "areas"] = {"area": formatted_bodies[vrf]["areas"]}
            if formatted_bodies[vrf]["propagation"]:
                vrf_request_body["global"] = {"inter-area-propagation-policies": {
                    self.ospf_key_extn + "inter-area-policy": formatted_bodies[vrf]["propagation"]
                }}
            if vrf_request_body:
                requests.append({"path": self.ospf_uri.format(vrf=vrf), "method": "PATCH", "data": {"openconfig-network-instance:ospfv2": vrf_request_body}})
        return requests

    def format_area_options_to_rest(self, want):
        '''takes a single area config and formats it for the body of an REST patch request.
        Only handles the part that fall under the area object in REST format'''
        formatted_area = {}

        formatted_config = self.format_area_config_to_rest(want)
        if formatted_config:
            formatted_area["config"] = formatted_config

        formatted_stub_config = {}
        if "stub" in want:
            # need enabled flag in stub so can make a stub without setting other settings
            if "enabled" in want["stub"]:
                formatted_stub_config[self.ospf_key_extn + "enable"] = want["stub"]["enabled"]
            if "no_summary" in want["stub"]:
                formatted_stub_config["no-summary"] = want["stub"]["no_summary"]
        if "default_cost" in want:
            formatted_stub_config[self.ospf_key_extn + "default-cost"] = want["default_cost"]

        # can't set default_cost on an area that isn't stub or NSAA. REST interface will fail if playbook does that

        if formatted_stub_config:
            formatted_area[self.ospf_key_extn + "stub"] = {"config": formatted_stub_config}

        if "virtual_links" in want:
            formatted_virtual_links = self.format_vlinks_to_rest(want["virtual_links"])
            if formatted_virtual_links:
                formatted_area["virtual-links"] = {"virtual-link": formatted_virtual_links}

        if formatted_area or len(want) == 2:
            # other settings that need to be merged, may pass in just key to create are, both need id
            formatted_area["identifier"] = want["area_id"]
        return formatted_area

    def format_area_config_to_rest(self, want):
        '''takes config wanting to be merged and formats the body of the area object's config in REST format'''
        formatted_config = {}
        if "authentication_type" in want:
            formatted_config[self.ospf_key_extn + "authentication-type"] = self.auth_type_conversion[want["authentication_type"]]
        if "shortcut" in want:
            formatted_config[self.ospf_key_extn + "shortcut"] = want["shortcut"].upper()
        formatted_config["identifier"] = want["area_id"]
        return formatted_config

    def format_vlinks_to_rest(self, want):
        '''takes a list of virtual link settings and formats it for REST requests'''
        formatted_vlinks = []
        for vlink_settings in want:
            formatted_vlink = {}
            formatted_vlink_config = {}
            # if not vlink_settings["enabled"]:
            #     # if enabled false, don't want to merge
            #     continue
            if "enabled" in vlink_settings:
                formatted_vlink_config[self.ospf_key_extn + "enable"] = vlink_settings["enabled"]
            if "dead_interval" in vlink_settings:
                formatted_vlink_config[self.ospf_key_extn + "dead-interval"] = vlink_settings["dead_interval"]
            if "hello_interval" in vlink_settings:
                formatted_vlink_config[self.ospf_key_extn + "hello-interval"] = vlink_settings["hello_interval"]
            if "retransmit_interval" in vlink_settings:
                formatted_vlink_config[self.ospf_key_extn + "retransmission-interval"] = vlink_settings["retransmit_interval"]
            if "transmit_delay" in vlink_settings:
                formatted_vlink_config[self.ospf_key_extn + "transmit-delay"] = vlink_settings["transmit_delay"]
            if "authentication" in vlink_settings:
                if "auth_type" in vlink_settings["authentication"]:
                    formatted_vlink_config[self.ospf_key_extn + "authentication-type"] = \
                        self.auth_type_conversion[vlink_settings["authentication"]["auth_type"]]
                if "key" in vlink_settings["authentication"]:
                    formatted_vlink_config[self.ospf_key_extn + "authentication-key"] = vlink_settings["authentication"]["key"]
                if "key_encrypted" in vlink_settings["authentication"]:
                    formatted_vlink_config[self.ospf_key_extn + "authentication-key-encrypted"] = vlink_settings["authentication"]["key_encrypted"]
            if "message_digest_keys" in vlink_settings:
                formatted_vlink[self.ospf_key_extn + "md-authentications"] = {"md-authentication":
                                                                              self.format_md_keys_to_rest(vlink_settings["message_digest_keys"])}
            if formatted_vlink_config:
                formatted_vlink_config["remote-router-id"] = vlink_settings["router_id"]
                formatted_vlink["config"] = formatted_vlink_config
            formatted_vlink["remote-router-id"] = vlink_settings["router_id"]
            formatted_vlinks.append(formatted_vlink)
        return formatted_vlinks

    def format_md_keys_to_rest(self, want):
        '''takes the list of messige digest keys in argspec format and formats it for REST body'''
        formatted_keys = []
        for message_key_settings in want:
            formatted_key_config = {}
            if "key_encrypted" in message_key_settings:
                formatted_key_config[self.ospf_key_extn + "authentication-key-encrypted"] = message_key_settings["key_encrypted"]
            formatted_key_config[self.ospf_key_extn + "authentication-key-id"] = message_key_settings["key_id"]
            if "key" in message_key_settings:
                formatted_key_config[self.ospf_key_extn + "authentication-md5-key"] = message_key_settings["key"]
            else:
                self._module.fail_json(msg="message digest key is required in md_authentications")
            formatted_keys.append({"authentication-key-id": message_key_settings["key_id"], "config": formatted_key_config})
        return formatted_keys

    def format_area_policy_to_rest(self, want):
        '''formats area's settings that should go into the inter-area-propagation-policies section of ospf'''
        formatted_area_policy = {}
        if "ranges" in want:
            formatted_ranges = self.format_ranges_to_rest(want["ranges"])
            if formatted_ranges:
                formatted_area_policy["ranges"] = {"range": formatted_ranges}
        if "filter_list_in" in want:
            formatted_area_policy["filter-list-in"] = {"config": {"name": want["filter_list_in"]}}
        if "filter_list_out" in want:
            formatted_area_policy["filter-list-out"] = {"config": {"name": want["filter_list_out"]}}
        if formatted_area_policy:
            formatted_area_policy["src-area"] = want["area_id"]
        return formatted_area_policy

    def format_ranges_to_rest(self, want):
        '''format the ranges an adrea advertises into REST body format. Takes a list of ranges'''
        formatted_ranges = []
        for range_settings in want:
            formatted_range_config = {}
            if "advertise" in range_settings:
                formatted_range_config[self.ospf_key_extn + "advertise"] = range_settings["advertise"]
            if "cost" in range_settings:
                formatted_range_config[self.ospf_key_extn + "metric"] = range_settings["cost"]
            if "substitute" in range_settings:
                # note it is mispelled in REST
                formatted_range_config[self.ospf_key_extn + "substitue-prefix"] = range_settings["substitute"]
            # can add range even without other settings
            formatted_range_config[self.ospf_key_extn + "address-prefix"] = range_settings["prefix"]
            formatted_ranges.append({"address-prefix": range_settings["prefix"], "config": formatted_range_config})
        return formatted_ranges

    def build_areas_delete_requests(self, commands, have, delete_everything=False):
        '''takes in a list of areas and builds all requests to delete the specified areas'''
        requests = []
        for area_c in commands:
            # want to match so can find out if commands specifies everything within existing area so can de a delete all of area
            matched_have = None
            for area_h in have:
                if area_h["area_id"] == area_c["area_id"] and area_h["vrf_name"] == area_c["vrf_name"]:
                    matched_have = area_h
            if not matched_have:
                # not found, just ignore. should not hit because all areas must be in both commands and have
                continue
            area_all_gone, area_delete_requests = self.build_area_delete_requests(area_c, matched_have)
            requests.extend(area_delete_requests)
        return requests

    def build_area_delete_requests(self, commands, have):
        '''builds the requests to delete configuration under the areas section of config for a single area. takes a pair of single area commands and have.
        returns tuple of whether everything in area was deleted and requests to cause changes'''
        requests = []
        # can't delete area directly, need to check for ranges, network, virtual links,
        # most of nested and complex settings and delete those first (and separately from area)
        delete_everything = False
        if len(commands) == 2:
            delete_everything = True

        vlink_all_gone, vlink_delete_requests = self.build_area_virtual_links_delete_requests(
            self.ospf_area_uri.format(vrf=commands["vrf_name"], area_id=commands["area_id"]),
            have.get("virtual_links", []) if delete_everything else commands.get("virtual_links", []),
            have.get("virtual_links", [])
        )

        ranges_all_gone, ranges_delete_requests = self.build_area_delete_ranges_requests(
            self.ospf_propagation_uri.format(vrf=commands["vrf_name"], area_id=commands["area_id"]),
            have.get("ranges", []) if delete_everything else commands.get("ranges", []),
            have.get("ranges", [])
        )

        # since ordered lists, just append the requests in order before checking if delete whole area
        requests.extend(vlink_delete_requests)
        requests.extend(ranges_delete_requests)

        # stub settings can be deleted by deleting area, so only need to append requests if not deleting area
        stub_all_gone, stub_delete_requests = self.build_area_stub_delete_requests(
            self.ospf_area_uri.format(vrf=commands["vrf_name"], area_id=commands["area_id"]), commands, have)

        if len(commands) == 2 or \
            (len(commands) == len(have) and stub_all_gone and vlink_all_gone and ranges_all_gone):
            # delete all settings for area.
            # either only area id was specified or all settings are named and for the more complex nested subsections of argspec,
            # those subsections also match and are cleared (need the extra flag since length only compares the subsections existence not contents)
            if not vlink_delete_requests or len(commands) != 3 or "virtual_links" not in commands:
                # clearing all vlinks when its just vlinks seems to clear the area
                requests.append({'path': self.ospf_area_uri.format(vrf=commands["vrf_name"], area_id=commands["area_id"]), 'method': 'DELETE'})
            return True, requests

        # propagation endpoint technicaly also contains the ranges but those don't get deleted on a 'delete area policy' request so must be separately
        # called no matter what happens to the whole policy.
        # Deleting the area needs to make sure ranges are gone, so ranges are always handled outside the propagation section handler.
        # the filter lists are grouped in root of argspec definition so they are captured by the length check of delete everything and a
        # propagation settings have been cleared flag is not needed to check if ok to delete the whole policy
        propagation_all_gone, propagation_delete_requests = self.build_area_delete_propagation_requests(commands, have, ranges_all_gone)
        requests.extend(propagation_delete_requests)
        requests.extend(stub_delete_requests)

        if "authentication_type" in commands:
            requests.append({"path": self.ospf_area_uri.format(vrf=commands["vrf_name"], area_id=commands["area_id"])
                             + "/config/openconfig-ospfv2-ext:authentication-type", "method": "DELETE"})
        if "shortcut" in commands:
            requests.append({"path": self.ospf_area_uri.format(vrf=commands["vrf_name"], area_id=commands["area_id"])
                            + "/config/openconfig-ospfv2-ext:shortcut", "method": "DELETE"})
        return False, requests

    def build_area_stub_delete_requests(self, request_root, commands, have):
        '''builds the requests to delete a single area's stub config. takes a pair of single area commands and have.
        returns a tuple of whether everything in stub config was deleted and requests to cause changes'''
        requests = []
        if "default_cost" in commands:
            requests.append({"path": request_root +
                             "/openconfig-ospfv2-ext:stub/config/default-cost", "method": "DELETE"})
        if "no_summary" in commands.get('stub', {}):
            requests.append({"path": request_root +
                             "/openconfig-ospfv2-ext:stub/config/no-summary", "method": "DELETE"})
        if "enabled" in commands.get('stub', {}):
            requests.append({"path": request_root +
                             "/openconfig-ospfv2-ext:stub/config/enable", "method": "DELETE"})
        if "no_summary" in have.get('stub', {}) and "no_summary" not in commands.get('stub', {}) or \
                "enabled" in have.get('stub', {}) and "enabled" not in commands.get('stub', {}) or \
                "default_cost" in have and "default_cost" not in commands:
            # cannot delete everything in stub only if there's some settings in have that aren't in listed as wanted to delete
            # field is in checks if no stub section, then it results in a false
            return False, requests
        if len(requests) > 0:
            # can't do a delete stub since that clears the whole area settings
            return True, requests
        return True, []

    def build_area_virtual_links_delete_requests(self, request_root, commands, have):
        '''builds the requests to delete a single area's virtual link config.
        takes a pair of an area's virtual link commands and have.
        returns a tuple of whether everything in area's virtual link config was deleted and requests to cause changes'''
        requests = []
        partial_deletes = False
        if len(commands) == 0:
            return True, []
        for vlink_c in commands:
            matched_vlink = None
            for vlink_h in have:
                if vlink_h["router_id"] == vlink_c["router_id"]:
                    matched_vlink = vlink_h
                    break
            if not matched_vlink:
                continue
            vlink_uri = request_root + "/virtual-links/virtual-link=" + vlink_c["router_id"]
            if len(vlink_c) == 1:
                # just the id specified so deleting everything inside a virtual link. don't need to process individual attribute delete requests
                # so delete the vlink and move to next
                requests.append({"path": request_root + "/virtual-links/virtual-link=" + vlink_c["router_id"], "method": "DELETE"})
                continue

            # check vlink subsections to see if they were also all deleted or need individual delete requests
            # doing this first as this is used to determine if can just do one request to delete this vlink
            if "message_digest_keys" in vlink_c:
                md_all_gone, md_auth_requests = self.build_area_md_auth_delete_requests(vlink_uri, vlink_c["message_digest_keys"],
                                                                                        matched_vlink["message_digest_keys"])
            else:
                # no message digest keys, means subsection does not need any work on it
                md_all_gone = True
                md_auth_requests = []

            if len(vlink_c) == len(matched_vlink) and md_all_gone:
                # deleting everything inside a virtual link. don't need to process individual attribute delete requests
                # so delete the vlink and move to next
                requests.append({"path": request_root + "/virtual-links/virtual-link=" + vlink_c["router_id"], "method": "DELETE"})
                continue
            partial_deletes = True
            # deleting individual attributes of a vlink, set flag for info that st least one interface needs to delete individual attributes
            requests.extend(md_auth_requests)
            if "enabled" in vlink_c:
                requests.append({"path": vlink_uri + "/config/openconfig-ospfv2-ext:enable", "method": "DELETE"})
            if "dead_interval" in vlink_c:
                requests.append({"path": vlink_uri + "/config/openconfig-ospfv2-ext:dead-interval", "method": "DELETE"})
            if "hello_interval" in vlink_c:
                requests.append({"path": vlink_uri + "/config/openconfig-ospfv2-ext:hello-interval", "method": "DELETE"})
            if "retransmit_interval" in vlink_c:
                requests.append({"path": vlink_uri + "/config/openconfig-ospfv2-ext:retransmission-interval", "method": "DELETE"})
            if "transmit_delay" in vlink_c:
                requests.append({"path": vlink_uri + "/config/openconfig-ospfv2-ext:transmit-delay", "method": "DELETE"})
            if "authentication" in vlink_c:
                if "auth_type" in vlink_c["authentication"]:
                    requests.append({"path": vlink_uri + "/config/openconfig-ospfv2-ext:authentication-type", "method": "DELETE"})
                if "key" in vlink_c["authentication"]:
                    requests.append({"path": vlink_uri + "/config/openconfig-ospfv2-ext:authentication-key", "method": "DELETE"})
                if "key_encrypted" in vlink_c["authentication"]:
                    requests.append({"path": vlink_uri + "/config/openconfig-ospfv2-ext:authentication-key-encrypted", "method": "DELETE"})
        if len(commands) == len(have) and not partial_deletes:
            return True, [{"path": request_root + "/virtual-links/virtual-link", "method": "DELETE"}]
        return False, requests

    def build_area_md_auth_delete_requests(self, request_root, commands, have):
        '''builds the requests to delete message digest keys for a single area's virtual link config.
        takes a pair of an area's virtual link's message digest commands and have
        returns a tuple of whether everything in message digest keys was deleted and requests to cause changes'''
        requests = []
        if len(commands) == 0:
            # nothing in message digest keys to delete
            return True, []
        elif len(commands) == len(have):
            # commands should only contain keys that are in have
            # deleted everything in have, just return one command to delete root
            return True, [{"path": request_root + "/openconfig-ospfv2-ext:md-authentications/authentication", "method": "DELETE"}]
        for md_c in commands:
            # there are two other fields but they don't seem to be deletable individually
            requests.append({"path": request_root + "/openconfig-ospfv2-ext:md-authentications/md-authentication=" + str(md_c["key_id"]), "method": "DELETE"})
        return False, requests

    def build_area_delete_propagation_requests(self, commands, have, ranges_all_gone):
        '''builds the requests to delete a single area's propagation config. takes a single area commands and have.
        This has a weird edge case. deleting area depends on deleting all of the ranges, so that is collected and handled in area.
        ranges are a part of inter-area-policy, but deleting on the specific inter-area-policy for this area in the REST API will not delete ranges as well.
        So this section won't be handling ranges also needs to know if ranges are cleared to check if ok to delete the whole policy.
        returns a tuple of if all propagation settings were deleted and requests to cause changes'''
        requests = []
        request_root = self.ospf_propagation_uri.format(vrf=commands["vrf_name"], area_id=commands["area_id"])

        if "filter_list_in" in commands:
            requests.append({"path": request_root + "/filter-list-in", "method": "DELETE"})
        if "filter_list_out" in commands:
            requests.append({"path": request_root + "/filter-list-out", "method": "DELETE"})

        if "filter_list_in" in have and "filter_list_in" not in commands or \
                "filter_list_out" in have and "filter_list_out" not in commands or \
                "ranges" in have and "ranges" not in commands or not ranges_all_gone:
            # if any of the fields important for this section are in have but not in commands, it means we didn't call to delete
            # everything in propagation policy
            return False, requests
        if len(requests) > 0:
            # ranges don't seem to get deleted when deleting individual policies
            delete_all_list = [{"path": request_root, "method": "DELETE"}]
            return True, delete_all_list
        return True, []

    def build_area_delete_ranges_requests(self, request_root, commands, have):
        '''builds list of requests to delete one area's settings for ranges. takes one area's commands and have list of ranges.
        Commands has to be a subset of have.
        returns a tuple of whether everything in ranges was deleted and requests to cause changes'''
        requests = []
        partial_deletes = False
        if len(commands) == 0:
            # nothing in ranges to delete
            return True, []
        for range_c in commands:
            matched_range = None
            for range_h in have:
                if range_h["prefix"] == range_c["prefix"]:
                    matched_range = range_h
                    break
            if not matched_range:
                # should not hit as commands must be a subset of have
                continue

            range_string = range_c["prefix"].replace("/", "%2F")
            if len(range_c) == 1 or len(range_c) == len(matched_range):
                # only the range prefix specified or same number of fields specified means delete the whoe range
                requests.append({"path": request_root + "/ranges/range=" + range_string, "method": "DELETE"})
                continue

            partial_deletes = True
            if "advertise" in range_c:
                requests.append({"path": request_root + "/ranges/range=" + range_string + "/config/advertise", "method": "DELETE"})
            if "cost" in range_c:
                requests.append({"path": request_root + "/ranges/range=" + range_string + "/config/metric", "method": "DELETE"})
            if "substitute" in range_c:
                # it actually is mispelled as substitue in REST
                requests.append({"path": request_root + "/ranges/range=" + range_string + "/config/substitue-prefix",
                                 "method": "DELETE"})
        if len(commands) == len(have) and not partial_deletes:
            # deleting all ranges
            return True, [{"path": request_root + "/ranges/range", "method": "DELETE"}]
        return False, requests
