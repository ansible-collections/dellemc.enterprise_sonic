#
# -*- coding: utf-8 -*-
# Copyright 2020 Dell Inc. or its subsidiaries. All Rights Reserved
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

GET = "get"


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
        request = [{"path": "data/sonic-portchannel:sonic-portchannel", "method": GET}]
        try:
            response = edit_config(self._module, to_request(self._module, request))
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)
        if response[0][1]:
            data = response[0][1]['sonic-portchannel:sonic-portchannel']
        else:
            data = []

        return data

    def get_po_and_po_members(self, data):
        if data is not None:
            if "PORTCHANNEL_MEMBER" in data:
                portchannel_members_list = data["PORTCHANNEL_MEMBER"]["PORTCHANNEL_MEMBER_LIST"]
            else:
                portchannel_members_list = []
            if "PORTCHANNEL" in data:
                portchannel_list = data["PORTCHANNEL"]["PORTCHANNEL_LIST"]
            else:
                portchannel_list = []
            if portchannel_list:
                for i in portchannel_list:
                    if not any(d["name"] == i["name"] for d in portchannel_members_list):
                        portchannel_members_list.append({'ifname': None, 'name': i['name']})
        if data:
            return portchannel_members_list
        else:
            return []

    def get_ethernet_segments(self, data):
        es_list = []
        if data:
            if "EVPN_ETHERNET_SEGMENT" in data:
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

        po_data = self.get_po_and_po_members(data)
        for conf in po_data:
            if conf:
                obj = self.render_config(self.generated_spec, conf)
                obj = self.transform_config(obj)
                if obj:
                    self.merge_portchannels(objs, obj)

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

    def render_config(self, spec, conf):
        return conf

    def transform_config(self, conf):
        trans_cfg = dict()
        trans_cfg['name'] = conf['name']
        trans_cfg['members'] = dict()
        if conf['ifname']:
            interfaces = list()
            interface = {'member': conf['ifname']}
            interfaces.append(interface)
            trans_cfg['members'] = {'interfaces': interfaces}
        return trans_cfg

    def merge_portchannels(self, configs, conf):
        if len(configs) == 0:
            configs.append(conf)
        else:
            new_interface = None
            if conf.get('members') and conf['members'].get('interfaces'):
                new_interface = conf['members']['interfaces'][0]
            else:
                configs.append(conf)
            if new_interface:
                matched = next((cfg for cfg in configs if cfg['name'] == conf['name']), None)
                if matched and matched.get('members'):
                    ext_interfaces = matched.get('members').get('interfaces', [])
                    ext_interfaces.append(new_interface)
                else:
                    configs.append(conf)
