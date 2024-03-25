#
# -*- coding: utf-8 -*-
# Copyright 2024 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic qos_buffer fact class
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
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    remove_empties
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.qos_buffer.qos_buffer import Qos_bufferArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)


class Qos_bufferFacts(object):
    """ The sonic qos_buffer fact class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = Qos_bufferArgs.argument_spec
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
        """ Populate the facts for qos_buffer
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        objs = []

        if not data:
            cfg = self.get_config(self._module)
            data = self.update_qos_buffer(cfg)
        objs = self.render_config(self.generated_spec, data)
        facts = {}
        if objs:
            params = utils.validate_config(self.argument_spec, {'config': remove_empties(objs)})
            facts['qos_buffer'] = params['config']
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

    def get_config(self, module):
        cfg = None
        get_path = '/data/openconfig-qos:qos/openconfig-qos-buffer:buffer'
        request = {'path': get_path, 'method': 'get'}

        try:
            response = edit_config(module, to_request(module, request))
            if 'openconfig-qos-buffer:buffer' in response[0][1]:
                cfg = response[0][1].get('openconfig-qos-buffer:buffer')
        except ConnectionError as exc:
            module.fail_json(msg=str(exc), code=exc.code)

        return cfg

    def update_qos_buffer(self, cfg):

        config_dict = {}
        if cfg:
            buffer_pools = cfg.get('buffer-pools')
            if buffer_pools:
                pool_list = buffer_pools.get('buffer-pool')
                if pool_list:
                    buffer_pool_list = []
                    for pool in pool_list:
                        pool_dict = {}
                        name = pool.get('name')
                        config = pool.get('config')
                        xoff = config.get('xoff')

                        if name and name == 'ingress_lossless_pool':
                            pool_dict['name'] = name
                            if xoff:
                                pool_dict['xoff'] = xoff
                        if pool_dict:
                            buffer_pool_list.append(pool_dict)
                    if buffer_pool_list:
                        config_dict['buffer_pools'] = buffer_pool_list

            buffer_profiles = cfg.get('buffer-profiles')
            if buffer_profiles:
                profile_list = buffer_profiles.get('buffer-profile')
                if profile_list:
                    buffer_profile_list = []
                    for profile in profile_list:
                        profile_dict = {}
                        name = profile.get('name')
                        config = profile.get('config')
                        pool = config.get('pool')
                        size = config.get('size')
                        static_threshold = config.get('static-threshold')
                        dynamic_threshold = config.get('dynamic-threshold')
                        pause_threshold = config.get('pause-threshold')

                        if name:
                            profile_dict['name'] = name
                        if pool:
                            profile_dict['pool'] = pool
                        if size:
                            profile_dict['size'] = size
                        if static_threshold:
                            profile_dict['static_threshold'] = static_threshold
                        if dynamic_threshold:
                            profile_dict['dynamic_threshold'] = dynamic_threshold
                        if pause_threshold:
                            profile_dict['pause_threshold'] = pause_threshold
                        if profile_dict:
                            buffer_profile_list.append(profile_dict)
                    if buffer_profile_list:
                        config_dict['buffer_profiles'] = buffer_profile_list

        return config_dict
