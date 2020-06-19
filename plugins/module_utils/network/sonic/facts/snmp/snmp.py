#
# -*- coding: utf-8 -*-
# Copyright 2020 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic snmp fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import re
from copy import deepcopy

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.dellemc.sonic.plugins.module_utils.network.sonic.argspec.snmp.snmp import SnmpArgs
from ansible_collections.dellemc.sonic.plugins.module_utils.network.sonic.sonic import send_requests


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

    def get_snmp(self):
        url = "data/sonic-snmp:sonic-snmp/SNMP_SERVER_COMMUNITY"
        method = "GET"
        request = [{"path": url, "method": method}]

        try:
            response = send_requests(self._module, requests=request)
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)
        # with open('/root/snmp.log', 'a+') as fp:
        #     fp.write('facts : response0: ' + str(response[0]) + '\n')
        #     fp.write('facts : response[0][1]: ' + str(response[0][1]) + '\n')
        snmp_lists = []
        if "sonic-snmp:SNMP_SERVER_COMMUNITY" in response[0][1]:
            snmp_lists = response[0][1]["sonic-snmp:SNMP_SERVER_COMMUNITY"]["SNMP_SERVER_COMMUNITY_LIST"]
        snmp_configs = []
        for snmp in snmp_lists:
            snmp_configs.append({"community": snmp["index"], "access": snmp["securityName"]})

        return snmp_configs

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
            snmp_all = self.get_snmp()
        objs = []
        for snmp in snmp_all:
            if snmp:
                obj = self.render_config(self.generated_spec, snmp)
                if obj:
                    objs.append(obj)
        ansible_facts['ansible_network_resources'].pop('snmp', None)
        facts = {}
        if objs:
            params = utils.validate_config(self.argument_spec, {'config': objs})
            facts['snmp'] = params['config']

        ansible_facts['ansible_network_resources'].update(facts)
        return ansible_facts

    def render_config(self, spec, conf):
        """
        Render config as dictionary structure and delete keys
          from spec for null values

        :param spec: The facts tree, generated from the argspec
        :param conf: The configuration
        :rtype: dictionary
        :returns: The generated config
        """
        config = deepcopy(spec)
        try:
            config['community'] = str(conf['community'])
            config['access'] = str(conf['access'])
        except TypeError:
            config['community'] = None
            config['access'] = None
        return utils.remove_empties(config)
