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

            snmp_dict.update(self.get_snmp_users(snmp_list.get("config")))
            snmp_dict.update(self.get_snmp_hosts(snmp_list.get("config")))
            snmp_dict.update(self.get_snmp_agentaddress(snmp_list.get("config")))

        if snmp_dict:
            snmp_configs.append(snmp_dict)

        return snmp_configs

    def get_snmp_users(self, snmp_list):
        """
        Get snmp users from the snmp list
        """
        user_dict = {}
        user = snmp_list.get("user")

        group = "SNMP_SERVER_GROUP/SNMP_SERVER_GROUP_LIST"
        group_member_list = "SNMP_SERVER_GROUP_MEMBER/SNMP_SERVER_GROUP_MEMBER_LIST/"

        user = "SNMP_SERVER_GROUP_USER/SNMP_SERVER_GROUP_USER_LIST"

        if user:
            self.update_dict(user_dict, "group", group_memmber_list.get("groupName"))
            self.update_dict(user_dict, "name", group_member_list.get("securityName"))
            self.update_dict(user_dict, "auth/auth_type", group_member_list.get(""))
            self.update_dict(user_dict, "auth/key", group_member_list.get(""))
            self.update_dict(user_dict, "priv/priv_type", group_member_list.get(""))
            self.update_dict(user_dict, "priv/key", group_member_list.get(""))
            #self.update_dict(user_dict, "encrypted", group_member_list.get("encrypted"))

        return user_dict

    def get_snmp_hosts(self, snmp_list):
        """
        Get snmp hosts from the snmp list
        """
        hosts_dict = {}
        host = snmp_list.get("host")

        server_params = "SNMP_SERVER_PARAMS/SNMP_SERVER_PARAMS_LIST"

        server_target = "SNMP_SERVER_TARGET/SNMP_SERVER_TARGET_LIST"

        if host:
            self.update_dict(host_dict, "user/name", server_params.get("user"))
            self.update_dict(host_dict, "user/security_level", server_params.get("security-level"))
            self.update_dict(host_dict, "ip", server_target.get("ip"))
            self.update_dict(host_dict, "retries", server_target.get("retries"))

        return hosts_dict

    def get_snmp_agentaddress(self, snmp_list):
        """
        Get snmp agent address from the snmp list
        """
        agentaddress_dict = {}
        agentaddress = snmp_list.get("agentaddress")

        agent_address_config = "SNMP_AGENT_ADDRESS_CONFIG/SNMP_AGENT_ADDRESS_CONFIG_LIST"

        if agenaddress:
            self.update_dict(agentaddress_dict, "interface", agent_address_config.get("interface"))
            self.update_dict(agentaddress_dict, "ip", agent_address_config.get("ip"))
            self.update_dict(agentaddress_dict, "name") # created
            self.update_dict(agentaddress_dict, "port", agent_address_config.get("port"))

        return agentaddress_dict



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