#
# -*- coding: utf-8 -*-
# Copyright 2024 Dell Inc. or its subsidiaries. All Rights Reserved.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic snmp fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
import re
from copy import deepcopy

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.snmp.snmp import SnmpArgs


class SnmpFacts(object):
    """ The sonic snmp fact class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = SnmpArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)

    def populate_facts(self, connection, ansible_facts, data=None):
        """ Populate the facts for snmp
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """

        if not data:
            # Fetch data from the current device configuration
            # (Skip if operating on previously fetched configuraation)
            data = self.get_all_snmp()

        snmps = list()
        for conf in data:
            if conf:
                snmp = self.render_config(self.generated_spec, conf)
                if snmp:
                    snmps.append(snmp)
        
        ansible_fact['ansibe_network_resources'].pop('snmp', None)
        facts = {}

        if snmps:
            facts['snmp'] = []
            params = utils.validate_confi(self.argument_spec,
                                          {'config': snmps})
            if params:
                facts['snmp'].extend(params['config'])
        ansible_facts['ansible_network_resources'].update(facts)

        return ansible_facts

    def get_all_snmps(self):
        """
        Get all the snmp servers in the device
        """
        request = [{"path": "data/sonic-snmp:sonic-snmp", "method": GET}]
        try:
            response = edit_config(self._module, to_request(self._module, request))
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)
        
        snmp_dict = {}
        snmp_configs = []
        if "sonic-snmp:sonic-snmp" in response[0][1]:
            snmp_list = response[0][1].get("sonic-snmp:sonic-snmp", {})

            snmp_dict.update(self.get_snmp_agentaddress(snmp_list))
            snmp_dict.update(self.get_snmp_community(snmp_list))
            snmp_dict.update(self.get_snmp_engine(snmp_list))
            snmp_dict.update(self.get_snmp_users(snmp_list.get("config")))
            snmp_dict.update(self.get_snmp_view(snmp_list.get("config")))
            snmp_dict.update(self.get_snmp_contact(snmp_list.get("config")))
            snmp_dict.update(self.get_snmp_location(snmp_list.get("config")))
            snmp_dict.update(self.get_snmp_enable_trap(snmp_list.get("config")))
            snmp_dict.update(self.get_snmp_group(snmp_list.get("config")))
            snmp_dict.update(self.get_snmp_hosts(snmp_list.get("config")))

        if snmp_dict:
            snmp_configs.append(snmp_dict)

        return snmp_configs

    def get_snmp_agentaddress(self, snmp_list):
        """
        Get snmp agent address from the snmp list

        TODO: WORK ON
        """
        agentaddress_dict = {}
        agentaddress = snmp_list.get("agentaddress")

        agent_address_config = "SNMP_AGENT_ADDRESS_CONFIG/SNMP_AGENT_ADDRESS_CONFIG_LIST"

        agentaddress_config = self.get_config(self._module, snmp_list, agent_address_config)

        if agenaddress_config:
            self.update_dict(agentaddress_dict, "interface", agentaddress_config.get("interface"))
            self.update_dict(agentaddress_dict, "ip", agentaddress_config.get("ip"))
            self.update_dict(agentaddress_dict, "name") # created
            self.update_dict(agentaddress_dict, "port", agentaddress_config.get("port"))

        return agentaddress_dict

    def get_snmp_community(self, snmp_list):
        """
        Get snmp community from the snmp list
        """
        community_dict = {}
        community = snmp_list.get("community")

        community_list = "SNMP_SERVER_COMMUNITY/SNMP_SERVER_COMMUNITY_LIST"

        community_config = self.get_config(self._module, snmp_list, community_list)

        if community_config:
            self.update_dict(community_dict, "name", community_config.get("index"))
            self.update_dict(community_dict, "group", community_config.get("securityName"))
        
        return community_dict

    def get_snmp_engine(self, snmp_list):
        """
        Get snmp engine from the snmp list
        """
        engine_str = ""
        engine = snmp_list.get("engine")

        engine_path = "SNMP_SERVER_ENGINE/SNMP_SERVER_ENGINE_LIST"

        engine_config = self.get_config(self._module, snmp_list, engine_path)

        if engine_config:
            engine_str = engine_config.get("engine-id")

        return engine_str

    def get_snmp_users(self, snmp_list):
        """
        Get snmp users from the snmp list
        """
        user_dict = {}
        user = snmp_list.get("user")

        group = "SNMP_SERVER_GROUP/SNMP_SERVER_GROUP_LIST"
        group_config = self.get_config(self._module, snmp_list, group)

        user = "SNMP_SERVER_GROUP_USER/SNMP_SERVER_GROUP_USER_LIST"
        user_config = self.get_config(self._module, snmp_list, user)

        if user_config:
            self.update_dict(user_dict, "group", group_config.get("name"))
            self.update_dict(user_dict, "name", user_config.get("name"))
            self.update_dict(user_dict, "auth:auth_type", group_member_list.get(""))
            self.update_dict(user_dict, "auth:key", group_member_list.get(""))
            self.update_dict(user_dict, "priv:priv_type", group_member_list.get(""))
            self.update_dict(user_dict, "priv:key", group_member_list.get(""))
            #self.update_dict(user_dict, "encrypted", group_member_list.get("encrypted"))

        return user_dict

    
    def get_snmp_view(self, snmp_list):
        """
        Get snmp view from the snmp list
        """
        view_dict = {}
        view = snmp_list.get("view")

        view_list = "SNMP_SERVER_GROUP_MEMBER/SNMP_SERVER_GROUP_MEMBER_LIST"

        view_config = self.get_config(self._module, snmp_list, view_list)

        if view_config:
            self.update_dict(view_dict, "name", view_config.get("name"))
            self.update_dict(view_dict, "included", view_config.get("included"))
            self.update_dict(view_dict, "excluded", view_config.get("excluded"))
        
        return view_dict

    def get_snmp_contact(self, snmp_list):
        """
        Get snmp contact from the snmp list
        """
        contact_str = ""
        contact = snmp_list.get("contact")

        snmp_server_list = "SNMP_SERVER/SNMP_SERVER_LIST"
        snmp_server_config = self.get_config(self._module, snmp_list, snmp_server_list)

        if snmp_server_config:
            contact_str = snmp_server_config.get("sysContact")

        return contact_str
    
    def get_snmp_location(self, snmp_list):
        """
        Get snmp location from the snmp list
        """
        location_str = ""
        location = snmp_list.get("location")

        snmp_server_list = "SNMP_SERVER/SNMP_SERVER_LIST"
        snmp_server_config = self.get_config(self._module, snmp_list, snmp_server_list)

        if snmp_server_config:
            location_str = snmp_server_config.get("sysLocation")

        return location_str
        
    def get_snmp_enable_trap(self, snmp_list):
        """
        Get snmp enable trap from the snmp list
        """
        enable_trap_str = ""
        enable_trap = snmp_list.get("enable-trap")

        snmp_server_list = "SNMP_SERVER/SNMP_SERVER_LIST"
        snmp_server_config = self.get_config(self._module, snmp_list, snmp_server_list)

        if snmp_server_config:
            auth_fail_trap = snmp_server_config.get("authenticationFailureTrap")
            bgp_trap = snmp_server_config.get("bgpTraps")
            config_change_trap = snmp_server_config.get("configChangeTrap")
            link_down_trap = snmp_server_config.get("linkDownTrap")
            link_up_trap = snmp_server_config.get("linkUpTrap")
            ospf_trap = snmp_server_config.get("ospfTraps")
            all_trap = snmp_server_config.get("traps")

            if trap == NULL:
                if auth_fail_trap:
                    enable_trap_str = "auth-fail"
                elif bgp_trap:
                    enable_trap_str = "bgp"
                elif config_change_trap:
                    enable_trap_str = "config-change"
                elif link_down_trap:
                    enable_trap_str = "link-down"
                elif link_up_trap:
                    enable_trap_str = "link-up"
                elif ospf_trap:
                    enable_trap_str = "ospf"
            else:
                enable_trap_str = "all"
        
        return enable_trap_str
            
    
    def get_snmp_group(self, snmp_list):
        """
        Get snmp group from the snmp list
        """
        group_dict = {}
        group = snmp_list.get("group")

        group_access_list = "SNMP_SERVER_GROUP_ACCESS/SNMP_SERVER_GROUP_ACCESS_LIST"
        group_access_config = self.get_config(self._module, snmp_list, group_access_list)

        if group_access_config:
            self.update_dict(group_dict, "name", group_access_config.get("groupName"))
            self.update_dict(group_dict, "access/security_model", group_access_config.get("securityModel"))
            self.update_dict(group_dict, "access/security_level", group_access_config.get("securityLevel"))
            self.update_dict(group_dict, "access/read_view", group_access_config.get("readView"))
            self.update_dict(group_dict, "access/write_view", group_access_config.get("writeView"))
            self.update_dict(group_dict, "access/notify_view", group_access_config.get("notifyView"))

        return group_dict

    def get_snmp_hosts(self, snmp_list):
        """
        Get snmp hosts from the snmp list
        """
        hosts_dict = {}
        host = snmp_list.get("host")

        server_params = "SNMP_SERVER_PARAMS/SNMP_SERVER_PARAMS_LIST"
        server_params_config = self.get_config(self._module, snmp_list, server_params)

        server_target = "SNMP_SERVER_TARGET/SNMP_SERVER_TARGET_LIST"
        server_target_config = self.get_config(self._module, snmp_list, server_target)

        if host:
            self.update_dict(host_dict, "user/name", server_params_config.get("user"))
            self.update_dict(host_dict, "user/security_level", server_params_config.get("security-level"))
            self.update_dict(host_dict, "ip", server_target_config.get("ip"))
            self.update_dict(host_dict, "retries", server_target_config.get("retries"))
            self.update_dict(host_dict, "timeout", server_target_config.get("timeout"))
            self.update_dict(host_dict, "community", server_params.get(""))
            if server_target_config.get("tag")[0] = "informNotify":
                self.update_dict(host_dict, "tag", "inform")
            else:
                self.update_dict(host_dict, "tag", "trap")
        
            self.update_dict(host_dict, "port", server_target_config.get("port"))
            self.update_dict(host_dict, "source_interface", server_target_config.get("src_intf"))
            self.update_dict(host_dict, "vrf", server_target.get(""))

        return hosts_dict

    def render_config(self, spec, conf):
        """
        Render config as dictionary structure and delete keys
          from spec for null values

        :param spec: The facts tree, generated from the argspec
        :param conf: The configuration
        :rtype: dictionary
        :returns: The generated config
        """
        return conf
 
     def update_dict(self, dict, key, value, parent_key=None):
        if value not in [None, {}, [], ()]:
            if parent_key:
                dict.setdefault(parent_key, {})
                dict[parent_key][key] = value
            else:
                dict[key] = value
    
    def get_config(self,, path, key_name):
        """Retrieve configuration from device"""
        cfg = None
        request = {'path': path, 'method': 'get'}

        try:
            response = edit_config(module, to_requsst(module, request))
            if key_name in response[0][1]:
                cfg = response[0][1].get(key_name)
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)
        
        return cfg