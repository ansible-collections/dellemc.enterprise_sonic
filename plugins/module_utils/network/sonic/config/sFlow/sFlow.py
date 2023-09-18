#
# -*- coding: utf-8 -*-
# Copyright 2023 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic_sFlow class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
import ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils as utils
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts import Facts

from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils \
    import (
        get_diff,
        update_states,
        to_request, 
        edit_config
    )

class Sflow(ConfigBase):
    """
    The sonic_sFlow class
    """

    gather_subset = [
        '!all',
        '!min',
    ]

    gather_network_resources = [
        'sFlow',
    ]

    sflow_uri = "data/openconfig-sampling-sflow:sampling/sflow"

    sflow_diff_test_keys = [{"collectors":{"port":"","address":"","network_instance":""}},
                      {"interfaces":{"name":""}}]

    def __init__(self, module):
        super(Sflow, self).__init__(module)

    def get_sFlow_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(self.gather_subset, self.gather_network_resources)
        sFlow_facts = facts['ansible_network_resources'].get('sFlow')
        if not sFlow_facts:
            return []
        return sFlow_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        warnings = list()

        existing_sFlow_facts = self.get_sFlow_facts()
        commands, requests =self.set_config(existing_sFlow_facts)
        if commands and len(requests) > 0:
            if not self._module.check_mode:
                try:
                    edit_config(self._module, to_request(self._module, requests))
                except ConnectionError as exc:
                    self._module.fail_json(msg=str(exc), code=exc.errno)
            result['changed'] = True
        result['commands'] = commands
        changed_sFlow_facts = self.get_sFlow_facts()

        result['before'] = existing_sFlow_facts
        if result['changed']:
            result['after'] = changed_sFlow_facts

        result['warnings'] = warnings
        return result

    def set_config(self, existing_sFlow_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']
        have = existing_sFlow_facts

        resp = self.set_state(want, have)
        return to_list(resp)

    def set_state(self, want, have):
        """ Select the appropriate function based on the state provided

        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :rtype: A tuple
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration, and REST requests that do it
        """
        commands = []
        requests = []
        state = self._module.params['state']
        if state == 'deleted':
            commands, requests = self._state_deleted(want, have)
        elif state == 'merged':
            commands, requests = self._state_merged(want, have)
        elif state == 'overridden':
            commands, requests = self._state_overridden(want, have)
        elif state == 'replaced':
            commands, requests = self._state_replaced(want, have)
        return commands, requests
    
    def _state_replaced(self, want, have):
        """ The command generator when state is replaced

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        requests = []
        return commands, requests

    def _state_overridden(self, want, have):
        """ The command generator when state is overridden

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        requests = []
        return commands, requests

    def _state_merged(self, want, have):
        """ The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """

        if want:
            want = utils.remove_empties(want)
            self.validate_sflow_args(want)
        else:
            want = {}

        #not sure if needed. seems like some validation already occured. 
        #   also adds a state field on which can't be sued for sending requests
        # logger.debug(f"validating config with spec <{self._module.argument_spec}>")
        commands = get_diff(want, have, test_keys=self.sflow_diff_test_keys)
        
        requests = self.create_patch_sFlow_root_request(commands, [])

        if commands and len(requests) > 0:
            commands = update_states(commands, "merged")
        else:
            commands = []
        return commands, requests


    def _state_deleted(self, want, have):
        """ The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        commands = {}
        requests = []

        for k,v in {**want}.items():
            if v is None:
                del want[k]
        # all top level keys have to have data (can be empty) or else should not be in list


        if (("enabled" in want and want["enabled"]) or len(want) == 0) and "enabled" in have and have["enabled"]:

            commands.update({"enabled":have["enabled"]})
            requests.append({"path":"data/openconfig-sampling-sflow:sampling/sflow/config/enabled", "method":"PUT", 
                             "data":{"openconfig-sampling-sflow:enabled": False}})

        if ("polling_interval" in want and "polling_interval" in have and want["polling_interval"] == have["polling_interval"])\
            or len(want) == 0 and "polling_interval" in have:
            commands.update({"polling_interval":have["polling_interval"]})
            requests.append({"path":"data/openconfig-sampling-sflow:sampling/sflow/config/polling-interval", "method":"DELETE"})

        if ("agent" in want and "agent" in have and want["agent"] == have["agent"])\
            or len(want) == 0 and "agent" in have:
            commands.update({"agent":have["agent"]})
            requests.append({"path":"data/openconfig-sampling-sflow:sampling/sflow/config/agent", "method":"DELETE"})
        
        if ("collectors" in want or len(want) == 0) and "collectors" in have:
            # here has to be either clear everything or want to clear certain collectors here. not both
            to_delete_list = have["collectors"]
            if len(want) > 0 and len(want["collectors"]) > 0:
                to_delete_list = want["collectors"]

            deleted_list=[]
            
            for collector in to_delete_list:
                found_match = len(want) == 0 or self.contains_collector(have["collectors"], collector)
                if found_match:
                    deleted_list.append(collector)
                    requests.append({"path":"data/openconfig-sampling-sflow:sampling/sflow/collectors/collector="+collector["address"]+","+str(collector["port"])+","+collector["network_instance"], "method":"DELETE"})
            if len(deleted_list) > 0: 
                commands.update({"collectors":deleted_list})

        if ("interfaces" in want or len(want) == 0) and "interfaces" in have:
            to_delete_list = have["interfaces"]
            if len(want) > 0 and len(want["interfaces"]) > 0:
                to_delete_list = want["interfaces"]

            deleted_list = []
            for interface in to_delete_list:
                if "name" not in interface:
                    continue

                found_interface = self.contains_interface(have["interfaces"], interface)

                if found_interface:
                    deleted_list.append(interface)
                    requests.append({"path":"data/openconfig-sampling-sflow:sampling/sflow/interfaces/interface="+interface["name"], "method":"DELETE"})    
            if len(deleted_list) > 0:
                commands.update({"interfaces":deleted_list})

        if commands and len(requests) > 0:
            commands = update_states(commands, "deleted")
        else:
            commands = []
        return commands, requests

    def contains_interface(self, list, search_interface):
        for interface in list:
            if interface["name"] == search_interface["name"]:
                return True
        return False

    def contains_collector(self, list, search_collector):
        for collector in list:
            if collector["address"] == search_collector["address"] and collector["network_instance"] == search_collector["network_instance"]\
                and collector["port"] == search_collector["port"]:
                return True
        return False

    def validate_sflow_args(self, config):
        '''validates passed in config'''
        validated = utils.validate_config(self._module.argument_spec, {"config":config})
        if config is not None and "polling_interval" in config and config["polling_interval"] is not None:
            if not (int(config["polling_interval"]) == 0 or int(config["polling_interval"]) in range(5,300)):
                raise Exception("polling interval out of range. must be 0 or in [5:300]")
    
    def create_patch_sFlow_root_request(self, config_dict, request_list):
        '''builds REST request for patching on sflow root, which can update all sflow information in one REST request, 
        from given config. adds request to passed in request list and returns it'''
        method = "PATCH"
        root_data_key = "openconfig-sampling-sflow:sflow"

        if len(config_dict) == 0:
            return request_list

        request_body = {}

        #config always requred in this endpoint
        request_body["config"] = self.create_config_request_body(config_dict)

        if "collectors" in config_dict:
            request_body.update({"collectors":{"collector":self.create_collectors_list_request_body(config_dict)}})

        if "interfaces" in config_dict:
            request_body.update({"interfaces":{"interface":self.create_interface_list_request_body(config_dict)}})

        request_list.append({"path": self.sflow_uri, "method": method, "data": {root_data_key:request_body}})
        return request_list
    
    def create_config_request_body(self, config_dict):
        '''creates the REST API format sflow global config info. '''
        request_config = {}
        if "enabled" in config_dict:
            # request_list.append({"path":"data/openconfig-sampling-sflow:sampling/sflow/config/enabled", "method":"PUT", "data":{"openconfig-sampling-sflow:enabled":config_dict["enabled"]}})
            request_config["enabled"] = config_dict["enabled"]
        if "polling_interval" in config_dict:
            # request_list.append({"path":"data/openconfig-sampling-sflow:sampling/sflow/config/polling-interval", "method":"PUT", "data":{"openconfig-sampling-sflow:polling-interval": config_dict["polling_interval"]}})
            request_config["polling-interval"] = config_dict["polling_interval"]
        if "agent" in config_dict:
            # request_list.append({"path":"data/openconfig-sampling-sflow:sampling/sflow/config/agent", "method":"PUT", "data":{"openconfig-sampling-sflow:agent": config_dict["agent"]}})
            request_config["agent"] = config_dict["agent"]
        return request_config

    def create_collectors_list_request_body(self, config_dict):
        '''creates and returns a list of sflow collectors where all collectors inside are formatted to REST API'''
        collector_list = []
        for collector in config_dict["collectors"]:
            collector_request = {"address":collector["address"], 
                                    "network-instance":collector["network_instance"],
                                    "port":collector["port"]}
            collector_list.append({**collector_request,"config":collector_request})
        return collector_list
    
    def create_interface_list_request_body(self, config_dict):
        '''creates and returns a list of sflow interfaces where
        all interfaces inside are formatted to REST API'''
        interface_list = []
        for interface in config_dict["interfaces"]:
            interface_config_request = {}
            if "enabled" in interface:
                interface_config_request["enabled"] = interface["enabled"]
            if "sampling_rate" in interface:
                interface_config_request["sampling-rate"] = interface["sampling_rate"]
            if len(interface_config_request) == 0:
                continue
            interface_config_request["name"] = interface["name"]
            interface_list.append({"name":interface["name"],
                                                            "config":interface_config_request})
        return interface_list
