#
# -*- coding: utf-8 -*-
# Copyright 2024 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic lag_interfaces fact class
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
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.lag_interfaces.lag_interfaces import Lag_interfacesArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible.module_utils.connection import ConnectionError


class Lag_interfacesFacts(object):
    """ The sonic lag_interfaces fact class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = Lag_interfacesArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)

    def get_all_portchannels(self):
        """Get all the interfaces available in chassis"""
        data = []
        request = {'path': 'data/sonic-portchannel:sonic-portchannel', 'method': 'get'}
        try:
            response = edit_config(self._module, to_request(self._module, request))
            if response[0][1]:
                data = response[0][1].get('sonic-portchannel:sonic-portchannel', [])
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)

        return data

    def get_po_and_po_members(self, data):
        all_portchannels_list = []
        merged_portchannels = []

        if data:
            if 'PORTCHANNEL' in data:
                portchannel_list = data['PORTCHANNEL']['PORTCHANNEL_LIST']
                all_portchannels_list.extend(portchannel_list)
            if 'PORTCHANNEL_MEMBER' in data:
                portchannel_members_list = data['PORTCHANNEL_MEMBER']['PORTCHANNEL_MEMBER_LIST']
                all_portchannels_list.extend(portchannel_members_list)

            if all_portchannels_list:
                mode_dict = {True: 'static', False: 'lacp'}
                for portchannel in all_portchannels_list:
                    name = portchannel.get('name')
                    fallback = portchannel.get('fallback')
                    fast_rate = portchannel.get('fast_rate')
                    member = portchannel.get('ifname')
                    mode = portchannel.get('static')

                    # Find if portchannel already exists and update
                    matched = next((portchannel for portchannel in merged_portchannels if portchannel['name'] == name), None)
                    if matched:
                        if fallback is not None:
                            matched['fallback'] = fallback
                        if fast_rate is not None:
                            matched['fast_rate'] = fast_rate
                        if member:
                            if 'members' in matched and matched['members'].get('interfaces'):
                                matched['members']['interfaces'].append({'member': member})
                            else:
                                matched['members'] = {'interfaces': [{'member': member}]}
                        if mode is not None:
                            matched['mode'] = mode_dict[mode]
                    # Create new portchannel if it doesn't already exist
                    else:
                        new_portchannel = {}
                        if name:
                            new_portchannel['name'] = name
                        if fallback is not None:
                            new_portchannel['fallback'] = fallback
                        if fast_rate is not None:
                            new_portchannel['fast_rate'] = fast_rate
                        if member:
                            new_portchannel['members'] = {'interfaces': [{'member': member}]}
                        if mode is not None:
                            new_portchannel['mode'] = mode_dict[mode]
                        if new_portchannel:
                            merged_portchannels.append(new_portchannel)

        return merged_portchannels

    def get_ethernet_segments(self, data):
        es_list = []
        if data:
            if 'EVPN_ETHERNET_SEGMENT' in data:
                es_list = data["EVPN_ETHERNET_SEGMENT"]["EVPN_ETHERNET_SEGMENT_LIST"]
        return es_list

    def populate_facts(self, connection, ansible_facts, data=None):
        """ Populate the facts for lag_interfaces
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        objs = []
        if not data:
            data = self.get_all_portchannels()
            objs = self.get_po_and_po_members(data)

            es_data = self.get_ethernet_segments(data)
            for es in es_data:
                po_name = es['ifname']
                esi_t = es['esi_type']
                esi = es['esi']
                if 'df_pref' in es:
                    df_pref = es['df_pref']
                else:
                    df_pref = None

                if esi_t == 'TYPE_1_LACP_BASED':
                    esi_type = 'auto_lacp'
                elif esi_t == 'TYPE_3_MAC_BASED':
                    esi_type = 'auto_system_mac'
                elif esi_t == 'TYPE_0_OPERATOR_CONFIGURED':
                    esi_type = 'ethernet_segment_id'

                if df_pref:
                    es_dict = {'esi_type': esi_type, 'esi': esi, 'df_preference': df_pref}
                else:
                    es_dict = {'esi_type': esi_type, 'esi': esi}

                have_po_conf = next((po_conf for po_conf in objs if po_conf['name'] == po_name), {})
                if have_po_conf:
                    have_po_conf['ethernet_segment'] = es_dict
                else:
                    self._module.fail_json(msg='{0} does not exist for ethernet segment'.format(po_name))

        facts = {}
        if objs:
            facts['lag_interfaces'] = []
            params = utils.validate_config(self.argument_spec, {'config': objs})
            for cfg in params['config']:
                facts['lag_interfaces'].append(cfg)
        ansible_facts['ansible_network_resources'].update(facts)

        return ansible_facts
