#
# -*- coding: utf-8 -*-
# Copyright 2023 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic login_timeout fact class
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
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.login_timeout.login_timeout import Login_timeoutArgs

from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)

from ansible.module_utils.connection import ConnectionError


GET = "get"


class Login_timeoutFacts(object):
    """ The sonic login_timeout fact class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = Login_timeoutArgs.argument_spec
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
        """ Populate the facts for login_timeout
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        if connection:  # just for linting purposes, remove
            pass

        objs = self.get_all_login_timeout_configs()

        ansible_facts['ansible_network_resources'].pop('login_timeout', None)
        facts = {}
        if objs:
            params = utils.validate_config(self.argument_spec, {'config': objs})
            facts['login_timeout'] = params['config']

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
        return conf

    def get_all_login_timeout_configs(self):
        """Get the login timeout configured in the device"""
        request = [{"path": "data/openconfig-system:system/openconfig-system-ext:login/session/config", "method": GET}]
        login_timeout_data = {}
        raw_login_timeout_data = {}
#        import epdb
#        epdb.serve(port=8989)
        try:
            response = edit_config(self._module, to_request(self._module, request))
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)
        login_timeout_data['exec_timeout'] = 0

        if 'openconfig-system-ext:config' in response[0][1]:
            raw_login_timeout_data = response[0][1]['openconfig-system-ext:config']

        if 'exec-timeout' in raw_login_timeout_data:
            login_timeout_data['exec_timeout'] = raw_login_timeout_data['exec-timeout']

        return login_timeout_data
