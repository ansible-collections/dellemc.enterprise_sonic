#
# -*- coding: utf-8 -*-
# Copyright 2023 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic banner fact class
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
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.banner.banner import BannerArgs

from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)

from ansible.module_utils.connection import ConnectionError

GET = "get"


class BannerFacts(object):
    """ The sonic banner fact class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = BannerArgs.argument_spec
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
        """ Populate the facts for banner
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        if connection:  # just for linting purposes, remove
            pass

        objs = self.get_all_banner_configs()

        ansible_facts['ansible_network_resources'].pop('banner', None)
        facts = {}
        if objs:
            params = utils.validate_config(self.argument_spec, {'config': objs})
            facts['banner'] = utils.remove_empties(params['config'])

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

    def get_all_banner_configs(self):
        """Get all the banner configured in the device"""
        request = [{"path": "data/openconfig-system:system/openconfig-system-ext:banner/config", "method": GET}]
        banner_data = {}
        raw_banner_data = {}
        try:
            response = edit_config(self._module, to_request(self._module, request))
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)
        banner_data['login'] = ""
        banner_data['motd'] = ""
        banner_data['login_banner_disable'] = False
        banner_data['motd_banner_disable'] = False

        if 'openconfig-system-ext:config' in response[0][1]:
            raw_banner_data = response[0][1]['openconfig-system-ext:config']

        if 'login-banner' in raw_banner_data:
            banner_data['login'] = raw_banner_data['login-banner']
        if 'motd-banner' in raw_banner_data:
            banner_data['motd'] = raw_banner_data['motd-banner']
        if 'login-banner-disable' in raw_banner_data:
            banner_data['login_banner_disable'] = raw_banner_data['login-banner-disable']
        if 'motd-banner-disable' in raw_banner_data:
            banner_data['motd_banner_disable'] = raw_banner_data['motd-banner-disable']

        return banner_data
