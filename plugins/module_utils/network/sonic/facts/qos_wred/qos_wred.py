#
# -*- coding: utf-8 -*-
# Copyright 2024 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic qos_wred fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from copy import deepcopy

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible.module_utils.connection import ConnectionError
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    remove_empties_from_list
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.qos_wred.qos_wred import Qos_wredArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)


class Qos_wredFacts(object):
    """ The sonic qos_wred fact class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = Qos_wredArgs.argument_spec
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
        """ Populate the facts for qos_wred
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        objs = []

        if not data:
            cfg = self.get_config(self._module)
            data = self.update_qos_wred(cfg)
        objs = data
        facts = {}
        if objs:
            params = utils.validate_config(self.argument_spec, {'config': objs})
            facts['qos_wred'] = remove_empties_from_list(params['config'])
        ansible_facts['ansible_network_resources'].update(facts)
        return ansible_facts

    def update_qos_wred(self, cfg):

        config_list = []
        lookup_dict = {'ECN_ALL': 'all', 'ECN_NONE': 'none'}
        colors = ['green', 'red', 'yellow']
        attributes = ['enable', 'min_threshold', 'max_threshold', 'drop_probability']

        if cfg:
            wred_profiles = cfg.get('wred-profile')
            if wred_profiles:
                for profile in wred_profiles:
                    wred_dict = {}
                    name = profile.get('name')
                    config = profile.get('config')
                    if config:
                        ecn = config.get('ecn')
                        if ecn:
                            wred_dict['ecn'] = lookup_dict[ecn]

                        for color in colors:
                            color_dict = {}
                            wred_enable = config.get(f'wred-{color}-enable')
                            min_threshold = config.get(f'{color}-min-threshold')
                            max_threshold = config.get(f'{color}-max-threshold')
                            drop_probability = config.get(f'{color}-drop-probability')

                            if wred_enable is not None:
                                color_dict['enable'] = wred_enable
                            if min_threshold:
                                color_dict['min_threshold'] = min_threshold
                            if max_threshold:
                                color_dict['max_threshold'] = max_threshold
                            if drop_probability:
                                color_dict['drop_probability'] = drop_probability
                            if color_dict:
                                wred_dict[color] = color_dict

                    if name:
                        wred_dict['name'] = name
                    if wred_dict:
                        config_list.append(wred_dict)

        return config_list

    def get_config(self, module):
        cfg = None
        get_path = '/data/openconfig-qos:qos/wred-profiles'
        request = {'path': get_path, 'method': 'get'}

        try:
            response = edit_config(module, to_request(module, request))
            if 'openconfig-qos:wred-profiles' in response[0][1]:
                cfg = response[0][1].get('openconfig-qos:wred-profiles', None)
        except ConnectionError as exc:
            module.fail_json(msg=str(exc), code=exc.code)
        return cfg
