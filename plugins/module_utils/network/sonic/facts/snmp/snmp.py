#
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved.
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
import secrets
import string

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.snmp.snmp import SnmpArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible.module_utils.connection import ConnectionError


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
            snmp_dict.update(self.get_snmp_users(snmp_list))
            snmp_dict.update(self.get_snmp_view(snmp_list))
            snmp_dict.update(self.get_snmp_contact(snmp_list))
            snmp_dict.update(self.get_snmp_location(snmp_list))
            snmp_dict.update(self.get_snmp_enable_trap(snmp_list))
            snmp_dict.update(self.get_snmp_group(snmp_list))

            host, target = self.get_snmp_hosts_targets(snmp_list)
            snmp_dict.update(host)
            snmp_dict.update(target)

        if snmp_dict:
            snmp_configs.append(snmp_dict)

        return snmp_configs

    def get_snmp_agentaddress(self, snmp_list):
        """
        Get snmp agent address from the snmp list
        """
        agentaddress_dict = {}
        num_agentadddress = 0
        agent_address_config = "SNMP_AGENT_ADDRESS_CONFIG/SNMP_AGENT_ADDRESS_CONFIG_LIST"
        agentaddress_config = self.get_config(self._module, snmp_list, agent_address_config)

        for agentaddress in agentaddress_config:
            self.update_dict(agentaddress_dict, "interface", agentaddress.get("interface"))
            self.update_dict(agentaddress_dict, "ip", agentaddress.get("ip"))
            self.update_dict(agentaddress_dict, "name", "agentEntry" + str(num_agentadddress +1)) # created
            self.update_dict(agentaddress_dict, "port", agentaddress.get("port"))
            num_agentadddress = num_agentadddress + 1

        return agentaddress_dict

    def get_snmp_community(self, snmp_list):
        """
        Get snmp community from the snmp list
        """
        community_dict = {}

        community_list = "SNMP_SERVER_COMMUNITY/SNMP_SERVER_COMMUNITY_LIST"

        community_config = self.get_config(self._module, snmp_list, community_list)

        for community in community_config:
            self.update_dict(community_dict, "name", community.get("index"))
            self.update_dict(community_dict, "group", community.get("securityName"))
            self.update_dict(community_dict, "security_model", "v2c", "group")
        
        return community_dict

    def get_snmp_engine(self, snmp_list):
        """
        Get snmp engine from the snmp list
        """
        engine_dict = {}

        engine_path = "SNMP_SERVER_ENGINE/SNMP_SERVER_ENGINE_LIST"

        engine_config = self.get_config(self._module, snmp_list, engine_path)

        for engine in engine_config:
            self.update_dict(engine_dict, "id", engine.get("engine-id"))
            self.update_dict(engine_dict, "listen/name", ) ##        
            self.update_dict(engine_dict, "listen/udp/ip", )##
            self.update_dict(engine_dict, "listen/udp/port", )##
            self.update_dict(engine_dict, "listen/udp/interface", ) ##

        return engine_dict

    def get_snmp_users(self, snmp_list):
        """
        Get snmp users from the snmp list

        TODO: finish
        """
        user_dict = {}
        num_user = 0

        group = "SNMP_SERVER_GROUP/SNMP_SERVER_GROUP_LIST"
        group_config = self.get_config(self._module, snmp_list, group)

        user = "SNMP_SERVER_USER/SNMP_SERVER_USER_LIST"
        user_config = self.get_config(self._module, snmp_list, user)

        for user in group_config:
            self.update_dict(user_dict, "group", user.get("name"))
            self.update_dict(user_dict, "name", user_config.get(num_user).get("name"))
            auth_type = "md6"
            if user_config.get("md5Key") is None:
                auth_type = "sha"
            self.update_dict(user_dict, "auth_type", auth_type, "auth")

            characters = string.ascii_letters + string.digits + string.punctuation
            random_auth_key = ''.join(secrets.choice(characters) for _ in range(length))
            self.update_dict(user_dict, "key", random_auth_key, "auth")
            priv_type = "aes"
            if user_config.get("aesKey") is None:
                priv_type = "des"
            self.update_dict(user_dict, "priv_type", priv_type, "priv")

            characters = string.ascii_letters + string.digits + string.punctuation
            random_priv_key = ''.join(secrets.choice(characters) for _ in range(length))
            self.update_dict(user_dict, "key", random_priv_key, "priv")


            ### not sure where to get the 'encrypted' bool value from
            self.update_dict(user_dict, "encrypted", 'False')

            num_user = num_user + 1

        return user_dict

    
    def get_snmp_view(self, snmp_list):
        """
        Get snmp view from the snmp list
        """
        view_dict = {}
        view = snmp_list.get("view")

        view_list = "SNMP_SERVER_GROUP_MEMBER/SNMP_SERVER_GROUP_MEMBER_LIST"

        view_config = self.get_config(self._module, snmp_list, view_list)

        for view in view_config:
            self.update_dict(view, "name", view.get("name"))
            self.update_dict(view, "included", view.get("included"))
            self.update_dict(view, "excluded", view.get("excluded"))
        
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

        for server in snmp_server_config:
            auth_fail_trap = server.get("authenticationFailureTrap")
            bgp_trap = server.get("bgpTraps")
            config_change_trap = server.get("configChangeTrap")
            link_down_trap = server.get("linkDownTrap")
            link_up_trap = server.get("linkUpTrap")
            ospf_trap = server.get("ospfTraps")
            all_trap = server.get("traps")

            if trap is None:
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

        group_access_list = "SNMP_SERVER_GROUP_ACCESS/SNMP_SERVER_GROUP_ACCESS_LIST"
        group_access_config = self.get_config(self._module, snmp_list, group_access_list)

        for group in group_access_config:
            self.update_dict(group_dict, "name", group.get("groupName"))
            self.update_dict(group_dict, "security_model", group.get("securityModel"), "access")
            self.update_dict(group_dict, "security_level", group.get("securityLevel"), "access")
            self.update_dict(group_dict, "read_view", group.get("readView"), "access")
            self.update_dict(group_dict, "write_view", group.get("writeView"), "access")
            self.update_dict(group_dict, "notify_view", group.get("notifyView"), "access")
            self.update_dict(group_dict, "context", "Default", "access")


        return group_dict

    def get_snmp_hosts_targets(self, snmp_list):
        """
        Get snmp hosts and targets from the snmp list
        """
        hosts_dict = {}
        targets_dict = {}
        target_params = {}
        num_host = 0
        v2 = True

        server_params = "SNMP_SERVER_PARAMS/SNMP_SERVER_PARAMS_LIST"
        server_params_config = self.get_config(self._module, snmp_list, server_params)

        server_target = "SNMP_SERVER_TARGET/SNMP_SERVER_TARGET_LIST"
        server_target_config = self.get_config(self._module, snmp_list, server_target)
        
        for host in server_target_config:
            user = server_params_config.get(num_host).get("host")
            if user is None:
                self.update_dict(host_dict, "community", server_params_config.get(num_host).get("securityNameV2"))
            else:
                v2 = False
                self.update_dict(host_dict, "name", user, "user")
                self.update_dict(host_dict, "security_level", server_params_config.get(num_host).get("security-level"), "user")
            
            self.update_dict(host_dict, "ip", host.get("ip"))
            self.update_dict(host_dict, "retries", host.get("retries"))
            self.update_dict(host_dict, "timeout", host.get("timeout"))
    
            if server_target_config.get("tag")[0] is "informNotify":
                self.update_dict(host_dict, "tag", "inform")
            else:
                self.update_dict(host_dict, "tag", "trap")
        
            self.update_dict(host_dict, "port", host.get("port"))
            self.update_dict(host_dict, "source_interface", host.get("src_intf"))
            self.update_dict(host_dict, "vrf", host.get("tag")[1])

            targets_dict, target_params = self.get_snmp_target(v2, targets_dict, target_params, server_target_config, server_params_config, num_host)

            num_host = num_host + 1

        return hosts_dict, targets_dict, target_params
    
    def get_snmp_target(self, v2, targets_dict, target_params, server_target_config, server_params_config, num_host):
        """
        Get snmp target from the snmp list
        """

        self.update_dict(targets_dict, "name", "targetEntry" + str(num_host))
        self.update_dict(targets_dict, "port", server_target_config.get(num_host).get("port"), "udp")
        self.update_dict(targets_dict, "tag", ["trapNotify"])
        self.update_dict(targets_dict, "targetParams", "targetEntry" + str(num_host))
        self.update_dict(targets_dict, "source_interface", server_target_config.get(num_host).get("src_intf"))

        self.update_dict(target_params, "name", "targetEntry" + str(num_host))
        self.update_dict(target_params, "security_name", server_params_config.get(num_host).get("securityNameV2"), "v2c")
        
        security_level = "no-auth-no-priv"
        if not v2:
            self.update_dict(target_params, "user_name", server_params_config.get(num_host).get("user"), "usm")
            security_level = server_params_config.get(num_host).get("security-level")
        
        self.update_dict(target_params, "security_level", security_level, "usm")

        return targets_dict, target_params

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