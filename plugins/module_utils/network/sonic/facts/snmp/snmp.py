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
        if connection:  # just for linting purposes, remove
            pass

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



    def get_all_snmp(self):
        """
        TODO:
        Get all the configured SNMP resources by executing a REST "GET" API to fetch all
        of the current snmp configuration from the target device.
        snmp_fetch_spec = \
            "ietf-snmp:snmp/ietf-snmp-ext:system     "
        snmp_resp_key = ""
        url= 
        method = "GET"
        request = [{"path": url, "method": method}]

        try:
            response = edit_config(self._module, to_request(self._module, request))
            except ConnectionError as exc:
                self._module.fail_json(msg=str(exc))

        snmp_unparsed = []
        snmp=
        """
        # TODO: FINISH!!!!!!!

        snmps = []
        snmp_users = []
        snmp_hosts = []

        smmp_list = self.get_all_snmps()

        if snmp_list.get('SNMP_SERVER_USER'):
            if snmp_list['SNMP_SERVER_USER'].get('SNMP_SERVER_USER_LIST'):
                snmp_users.extend(snmp_users['SNMP_SERVER_USER']['SNMP_SERVER_USER_LIST'])
        if snmp_list.get('SNMP_SERVER_TARGET'):
            if snmp_list['SNMP_SERVER_TARGET'].get('SNMP_SERVER_TARGET_LIST'):
                snmp_hosts.extend(snmp_hosts['SNMP_SERVER_TARGET']['SNMP_SERVER_TARGET_LIST'])
        
        self.fill_snmp_users(snmps, snmp_users)
        self.fill_snmp_hosts(snmps, snmp_hosts)

        return snmps

    def get_all_snmps(self):
        """
        Get all the snmp servers in the device
        """
        request = [{"path": "data/sonic-snmp:sonic-snmp", "method": GET}]
        try:
            response = edit_config(self._module, to_request(self._module, request))
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)
        
        snmp_list = []
        if "sonic-snmp:sonic-snmp" in response[0][1]:
            snmp_list = response[0][1].get("sonic-snmp:sonic-snmp", {})

        return snmp_list

    def fill_snmp_users(self, snmps, snmp_users):
        """
        Add snmp users to the snmp list
        """
        for snmp_user in snmp_users:
            snmps.append(snmp_user)

    def fill_snmp_hosts(self, snmps, snmp_hosts):
        """
        Add snmp hosts to the snmp list
        """
        for snmp_host in snmp_hosts:
            snmps.append(snmp_host)

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
 