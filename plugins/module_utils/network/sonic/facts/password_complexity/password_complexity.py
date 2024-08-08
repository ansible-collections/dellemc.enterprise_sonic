#
# -*- coding: utf-8 -*-
# Copyright 2023 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic password_complexity fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from __future__ import absolute_import, division, print_function
__metaclass__ = type

from copy import deepcopy

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.password_complexity.password_complexity import (
    Password_complexityArgs,
)

from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)

from ansible.module_utils.connection import ConnectionError


GET = "get"


class Password_complexityFacts(object):
    """ The sonic password_complexity fact class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = Password_complexityArgs.argument_spec
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
        """ Populate the facts for password_complexity
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        if connection:  # just for linting purposes, remove
            pass

        objs = self.get_all_password_attribute_configs()

        ansible_facts['ansible_network_resources'].pop('password_complexity', None)
        facts = {}
        if objs:
            params = utils.validate_config(self.argument_spec, {'config': objs})
            facts['password_complexity'] = utils.remove_empties(params['config'])

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

    def get_all_password_attribute_configs(self):
        """Get all the password attribute configured in the device"""
        request = [{"path": "data/openconfig-system:system/openconfig-system-ext:login/password-attributes/config", "method": GET}]
        password_attribute_data = {}
        raw_password_attribute_data = {}
        try:
            response = edit_config(self._module, to_request(self._module, request))
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)
        password_attribute_data['min_lower_case'] = 0
        password_attribute_data['min_upper_case'] = 0
        password_attribute_data['min_numerals'] = 0
        password_attribute_data['min_special_char'] = 0
        password_attribute_data['min_len'] = 8

        if 'openconfig-system-ext:config' in response[0][1]:
            raw_password_attribute_data = response[0][1]['openconfig-system-ext:config']

        if 'min-lower-case' in raw_password_attribute_data:
            password_attribute_data['min_lower_case'] = raw_password_attribute_data['min-lower-case']
        if 'min-upper-case' in raw_password_attribute_data:
            password_attribute_data['min_upper_case'] = raw_password_attribute_data['min-upper-case']
        if 'min-numerals' in raw_password_attribute_data:
            password_attribute_data['min_numerals'] = raw_password_attribute_data['min-numerals']
        if 'min-special-char' in raw_password_attribute_data:
            password_attribute_data['min_special_char'] = raw_password_attribute_data['min-special-char']
        if 'min-len' in raw_password_attribute_data:
            password_attribute_data['min_len'] = raw_password_attribute_data['min-len']

        return password_attribute_data
