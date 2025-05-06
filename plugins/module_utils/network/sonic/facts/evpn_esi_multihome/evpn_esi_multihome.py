#
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic evpn_esi_multihome fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from copy import deepcopy

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.evpn_esi_multihome.evpn_esi_multihome import Evpn_esi_multihomeArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    remove_empties
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible.module_utils.connection import ConnectionError


class Evpn_esi_multihomeFacts(object):
    """ The sonic evpn_esi_multihome fact class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = Evpn_esi_multihomeArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options],
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)

    def populate_facts(self, connection, ansible_facts, data=None):
        """ Populate the facts for evpn_esi_multihome
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """

        if not data:
            data = self.get_all_evpn_esi_mh()

        evpn_esi_mh = dict()
        self.render_config(self.generated_spec, data)
        evpn_esi_mh = data
        facts = {}
        if evpn_esi_mh:
            facts['evpn_esi_multihome'] = dict()
            params = utils.validate_config(self.argument_spec, {'config': evpn_esi_mh})

            if params:
                facts['evpn_esi_multihome'].update(remove_empties(params['config']))

        ansible_facts['ansible_network_resources'].update(facts)

        return ansible_facts

    def get_all_evpn_esi_mh(self):
        """ Get all evpn esi multihome servers in the device
        """
        path = "data/openconfig-network-instance:network-instances/network-instance=default/evpn/evpn-mh/config"
        method = "GET"
        request = {"path": path, "method": method}

        try:
            response = edit_config(self._module, to_request(self._module, request))
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)

        evpn_esi_mh_dict = dict()
        if len(response) == 0 or len(response[0]) == 0:
            return evpn_esi_mh_dict

        info_path = 'openconfig-network-instance:config'
        response_evpn_esi = response[0][1].get(info_path, {})
        if info_path in response[0][1] and response_evpn_esi:
            df_election_time = response_evpn_esi.get('df-election-time', None)
            if df_election_time:
                evpn_esi_mh_dict.update({'df_election_time': df_election_time})

            es_activation_delay = response_evpn_esi.get('es-activation-delay', None)
            if es_activation_delay:
                evpn_esi_mh_dict.update({'es_activation_delay': es_activation_delay})

            neigh_holdtime = response_evpn_esi.get('neigh-holdtime', None)
            if neigh_holdtime:
                evpn_esi_mh_dict.update({'neigh_holdtime': neigh_holdtime})

            mac_holdtime = response_evpn_esi.get('mac-holdtime', None)
            if mac_holdtime:
                evpn_esi_mh_dict.update({'mac_holdtime': mac_holdtime})

            startup_delay = response_evpn_esi.get('startup-delay', None)
            if startup_delay:
                evpn_esi_mh_dict.update({'startup_delay': startup_delay})

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
