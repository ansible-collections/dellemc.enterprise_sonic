#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic bgp fact class
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
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    remove_empties_from_list
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.bgp.bgp import BgpArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.bgp_utils import (
    get_bgp_data,
)


class BgpFacts(object):
    """ The sonic bgp fact class
    """

    global_params_map = {
        'bgp_as': 'as',
        'router_id': 'router-id',
        'log_neighbor_changes': ['openconfig-bgp-ext:logging-options', 'log-neighbor-state-changes'],
        'as_path_confed': ['route-selection-options', 'openconfig-bgp-ext:compare-confed-as-path'],
        'as_path_ignore': ['route-selection-options', 'ignore-as-path-length'],
        'as_path_multipath_relax': ['use-multiple-paths', 'ebgp', 'config', 'allow-multiple-as'],
        'as_path_multipath_relax_as_set': ['use-multiple-paths', 'ebgp', 'config', 'openconfig-bgp-ext:as-set'],
        'compare_routerid': ['route-selection-options', 'external-compare-router-id'],
        'med_confed': ['route-selection-options', 'openconfig-bgp-ext:med-confed'],
        'med_missing_as_worst': ['route-selection-options', 'openconfig-bgp-ext:med-missing-as-worst'],
    }

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = BgpArgs.argument_spec
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
        """ Populate the facts for BGP
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        objs = list()
        if connection:  # just for linting purposes, remove
            pass

        if not data:
            data = get_bgp_data(self._module, self.global_params_map)
            self.normalise_bgp_data(data)

        # operate on a collection of resource x
        for conf in data:
            if conf:
                obj = self.render_config(self.generated_spec, conf)
        # split the config into instances of the resource
                if obj:
                    objs.append(obj)

        ansible_facts['ansible_network_resources'].pop('bgp', None)
        facts = {}
        if objs:
            params = utils.validate_config(self.argument_spec, {'config': remove_empties_from_list(objs)})
            facts['bgp'] = params['config']
        ansible_facts['ansible_network_resources'].update(facts)
        return ansible_facts

    def normalise_bgp_data(self, data):
        for conf in data:
            bestpath = {}
            med = {}
            as_path = {}

            conf['log_neighbor_changes'] = conf.get('log_neighbor_changes', False)

            as_path['confed'] = conf.get('as_path_confed', False)
            as_path['ignore'] = conf.get('as_path_ignore', False)
            as_path['multipath_relax'] = conf.get('as_path_multipath_relax', False)
            as_path['multipath_relax_as_set'] = conf.get('as_path_multipath_relax_as_set', False)
            bestpath['as_path'] = as_path

            med['confed'] = conf.get('med_confed', False)
            med['missing_as_worst'] = conf.get('med_missing_as_worst', False)
            bestpath['med'] = med

            bestpath['compare_routerid'] = conf.get('compare_routerid', False)

            conf['bestpath'] = bestpath

            keys = [
                'as_path_confed', 'as_path_ignore', 'as_path_multipath_relax', 'as_path_multipath_relax_as_set',
                'med_confed', 'med_missing_as_worst',
                'compare_routerid',
            ]
            for key in keys:
                if key in conf:
                    conf.pop(key)

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
