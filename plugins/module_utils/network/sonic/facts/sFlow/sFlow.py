#
# -*- coding: utf-8 -*-
# Copyright 2023 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic sFlow fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
import re
import json
from copy import deepcopy

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.sFlow.sFlow import SflowArgs

from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic \
    import to_request, edit_config

class SflowFacts(object):
    """ The sonic sFlow fact class
    """

    def __init__(self, module, subspec = 'config', options = 'options'):
        self._module = module
        self.argument_spec = SflowArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)

    def populate_facts(self, connection, ansible_facts, data = None):
        """ Populate the facts for sFlow
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """

        if not data:
            data = self.get_sFlow_info()
        
        data = self.farmat_to_argspec(data)

        #validate can add null values for things missing from device config, 
        #   so doing that before remove empties
        cleaned_data = utils.remove_empties(
            utils.validate_config(self.argument_spec, data)
        )

        ansible_facts['ansible_network_resources'].pop('sFlow', None)
        if cleaned_data:
            ansible_facts['ansible_network_resources'].update({"sFlow":cleaned_data["config"]})
        
        return ansible_facts
    
    def farmat_to_argspec(self, data):
        '''takes JSON data from sFlow's top level data's get REST call and returns a copy 
            that is formatted like argspec for this module
            :rtype: dictionary
            :returns: dictionary that has options in same format as defined in argspec.
            format looks something like: {"config": {"enabled":false, "interfaces":[{"name":"Etnernet0",
            enabled: None...}], ...}}'''
        formatted_data = {"config":{}}

        formatted_data["config"]["agent"] = deepcopy(data["config"].get("agent", None))
        formatted_data["config"]["enabled"] = deepcopy(data["config"].get("enabled", None))
        formatted_data["config"]["polling_interval"] = deepcopy(data["config"].get("polling-interval", None))
        
        if "interfaces" in data:
            formatted_data["config"]["interfaces"] = []
            for interface in data["interfaces"]["interface"]:
                formatted_interface = {}
                formatted_interface["name"] = deepcopy(interface.get("name", None))
                if "config" in interface:
                    formatted_interface["enabled"] = deepcopy(interface["config"].get("enabled", None))
                    formatted_interface["sampling_rate"] = deepcopy(interface["config"].get("sampling-rate", None))
                else:
                    formatted_interface["enabled"] = deepcopy(interface["state"].get("enabled", None))
                    formatted_interface["sampling_rate"] = deepcopy(interface["state"].get("sampling-rate", None))
                formatted_data["config"]["interfaces"].append(formatted_interface)
        else:
            formatted_data["config"]["interfaces"] = None

        if "collectors" in data:
            formatted_data["config"]["collectors"] = []
            for collector in data["collectors"]["collector"]:
                formatted_collector = {}
                formatted_collector["address"] = deepcopy(collector.get("address", None))
                if "config" in collector:
                    formatted_collector["network_instance"] = deepcopy(collector["config"].get("network-instance", None))
                    formatted_collector["port"] = deepcopy(collector["config"].get("port", None))
                else:
                    formatted_collector["network_instance"] = deepcopy(collector["state"].get("network-instance", None))
                    formatted_collector["port"] = deepcopy(collector["state"].get("port", None))
                formatted_data["config"]["collectors"].append(formatted_collector)
        else:
            formatted_data["config"]["collectors"] = None

        return formatted_data


    def get_sFlow_info(self):
        '''get the top level sFlow configuration on device
        :rtype: dictionary
        :returns: everything listed in resource's config
        '''
        uri_path = "data/openconfig-sampling-sflow:sampling/sflow"
        method = "GET"
        request = [{"path": uri_path, "method": method}]
        # facts get request returns a dictionary, key to get facts data we care about
        response_key = 'openconfig-sampling-sflow:sflow'

        try:
            response = edit_config(self._module, to_request(self._module, request))
        except ConnectionError as exc:
            self._module.fail_json(msg = str(exc))

        response_body = {}
        try:
            response_body = response[0][1][response_key]
        except Exception as e:
            raise Exception("response from getting sFlow facts not formed as expected")
        
        return response_body