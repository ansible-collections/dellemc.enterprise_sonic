#
# -*- coding: utf-8 -*-
# Copyright 2023 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic sflow fact class
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
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.sflow.sflow import SflowArgs

from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic \
    import to_request, edit_config

import logging
facts_logger = logging.getLogger("sflow Facts")
# This decides what is printed vv Only logging with higher priority gets printed. set to all caps level name
facts_logger.setLevel(logging.DEBUG)
# if not facts_logger.handlers:
#     # check just in case to prevent double calls from creating double output
#     logger_handler = logging.FileHandler('myLogs.txt', mode='a+', encoding='utf-8')
#     logging_format = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', '%Y-%m-%d %H:%M:%S', style='{')
#     logger_handler.setFormatter(logging_format)
#     facts_logger.addHandler(logger_handler)

class SflowFacts(object):
    """ The sonic sflow fact class
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
        """ Populate the facts for sflow
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """

        if not data:
            data = self.get_sflow_info()
            facts_logger.debug(f"returned from device data is <{data}>")
        
        data = self.format_to_argspec(data)
        facts_logger.debug(f"data formatted to argspec is <{data}>")

        #validate can add null values for things missing from device config, 
        #   so doing that before remove empties
        cleaned_data = utils.remove_empties(
            utils.validate_config(self.argument_spec, data)
        )

        facts_logger.debug(f"cleaned up and validated data is <{cleaned_data}>")

        ansible_facts['ansible_network_resources'].pop('sflow', None)
        if cleaned_data:
            ansible_facts['ansible_network_resources'].update({"sflow":cleaned_data["config"]})
        
        return ansible_facts
    
    def format_to_argspec(self, data):
        '''takes JSON data from sflow's top level data's get REST call and returns a copy 
            that is formatted like argspec for this module. Can have empty values in it
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
                if "config" in interface:
                    formatted_interface = {}
                    formatted_interface["name"] = deepcopy(interface.get("name", None))
                    formatted_interface["enabled"] = deepcopy(interface["config"].get("enabled", None))
                    formatted_interface["sampling_rate"] = deepcopy(interface["config"].get("sampling-rate", None))
                    formatted_data["config"]["interfaces"].append(formatted_interface)

        if "collectors" in data:
            formatted_data["config"]["collectors"] = []
            for collector in data["collectors"]["collector"]:
                if "config" in collector:
                    formatted_collector = {}
                    formatted_collector["address"] = deepcopy(collector.get("address", None))
                    formatted_collector["network_instance"] = deepcopy(collector["config"].get("network-instance", None))
                    formatted_collector["port"] = deepcopy(collector["config"].get("port", None))
                    formatted_data["config"]["collectors"].append(formatted_collector)

        return formatted_data


    def get_sflow_info(self):
        '''get the top level sflow configuration on device
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

        facts_logger.debug(f"REST response to get facts is <{response}>")
        response_body = {}
        try:
            response_body = response[0][1][response_key]
        except Exception:
            raise Exception("response from getting sflow facts not formed as expected")
        
        return response_body