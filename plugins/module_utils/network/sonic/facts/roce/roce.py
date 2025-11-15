#
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic roce fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from copy import deepcopy

from ansible.module_utils.connection import ConnectionError
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    remove_empties
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.roce.roce import RoceArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)


class RoceFacts(object):
    """ The sonic roce fact class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = RoceArgs.argument_spec
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
        """ Populate the facts for roce
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        if not data:
            cfg = self.get_config(self._module)
            data = self.render_config(cfg)
        facts = {}
        if data:
            params = utils.validate_config(self.argument_spec, {'config': data})
            facts['roce'] = remove_empties(params['config'])
        ansible_facts['ansible_network_resources'].update(facts)
        return ansible_facts

    def get_config(self, module):
        """Gets the 'SWITCH_LIST' configuration if present"""
        cfg = None
        get_path = '/data/sonic-switch:sonic-switch/SWITCH/SWITCH_LIST=switch'
        request = {'path': get_path, 'method': 'get'}

        try:
            response = edit_config(module, to_request(self._module, request))
            if 'sonic-switch:SWITCH_LIST' in response[0][1]:
                cfg = response[0][1].get('sonic-switch:SWITCH_LIST')
        except ConnectionError as exc:
            module.fail_json(msg=str(exc), code=exc.code)

        return cfg

    def render_config(self, cfg):
        """Transform SONiC data to argspec format"""
        config_dict = {}

        if cfg:
            roce_enable = cfg[0].get('roce_enable', False)
            pfc_priority = cfg[0].get('roce_pfc_priority')

            config_dict['roce_enable'] = roce_enable
            if pfc_priority:
                config_dict['pfc_priority'] = pfc_priority

        return config_dict
