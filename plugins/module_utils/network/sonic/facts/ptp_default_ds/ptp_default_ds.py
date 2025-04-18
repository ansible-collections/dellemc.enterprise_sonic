#
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic ptp_default_ds fact class
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
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.ptp_default_ds.ptp_default_ds import Ptp_default_dsArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible.module_utils.connection import ConnectionError


class Ptp_default_dsFacts(object):
    """ The sonic ptp_default_ds fact class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = Ptp_default_dsArgs.argument_spec
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
        """ Populate the facts for ptp_default_ds
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        if connection:  # just for linting purposes, remove
            pass

        obj = self.get_ptp_default_ds()

        ansible_facts['ansible_network_resources'].pop('ptp_default_ds', None)
        facts = {}
        if obj:
            params = utils.validate_config(self.argument_spec, {'config': obj})
            facts['ptp_default_ds'] = utils.remove_empties(params['config'])

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

    def get_ptp_default_ds(self):
        """Get all the global ptp default ds configured in the device"""
        request = [{"path": "data/ietf-ptp:ptp/instance-list=0/default-ds", "method": "get"}]
        ptp_default_ds_data = {}
        try:
            response = edit_config(self._module, to_request(self._module, request))
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)

        if 'ietf-ptp:default-ds' in response[0][1]:
            raw_ptp_default_ds_data = response[0][1]['ietf-ptp:default-ds']
            if 'priority1' in raw_ptp_default_ds_data:
                ptp_default_ds_data['priority1'] = raw_ptp_default_ds_data['priority1']
            if 'priority2' in raw_ptp_default_ds_data:
                ptp_default_ds_data['priority2'] = raw_ptp_default_ds_data['priority2']
            if 'domain-number' in raw_ptp_default_ds_data:
                ptp_default_ds_data['domain_number'] = raw_ptp_default_ds_data['domain-number']
            if 'ietf-ptp-ext:log-announce-interval' in raw_ptp_default_ds_data:
                ptp_default_ds_data['log_announce_interval'] = raw_ptp_default_ds_data['ietf-ptp-ext:log-announce-interval']
            if 'ietf-ptp-ext:announce-receipt-timeout' in raw_ptp_default_ds_data:
                ptp_default_ds_data['announce_receipt_timeout'] = raw_ptp_default_ds_data['ietf-ptp-ext:announce-receipt-timeout']
            if 'ietf-ptp-ext:log-sync-interval' in raw_ptp_default_ds_data:
                ptp_default_ds_data['log_sync_interval'] = raw_ptp_default_ds_data['ietf-ptp-ext:log-sync-interval']
            if 'ietf-ptp-ext:log-min-delay-req-interval' in raw_ptp_default_ds_data:
                ptp_default_ds_data['log_min_delay_req_interval'] = raw_ptp_default_ds_data['ietf-ptp-ext:log-min-delay-req-interval']
            if 'two-step-flag' in raw_ptp_default_ds_data:
                ptp_default_ds_data['two_step_flag'] = raw_ptp_default_ds_data['two-step-flag']
            if 'ietf-ptp-ext:clock-type' in raw_ptp_default_ds_data and raw_ptp_default_ds_data['ietf-ptp-ext:clock-type'] != "":
                ptp_default_ds_data['clock_type'] = raw_ptp_default_ds_data['ietf-ptp-ext:clock-type']
            if 'ietf-ptp-ext:network-transport' in raw_ptp_default_ds_data and raw_ptp_default_ds_data['ietf-ptp-ext:network-transport'] != "":
                ptp_default_ds_data['network_transport'] = raw_ptp_default_ds_data['ietf-ptp-ext:network-transport']
            if 'ietf-ptp-ext:unicast-multicast' in raw_ptp_default_ds_data and raw_ptp_default_ds_data['ietf-ptp-ext:unicast-multicast'] != "":
                ptp_default_ds_data['unicast_multicast'] = raw_ptp_default_ds_data['ietf-ptp-ext:unicast-multicast']
            if 'ietf-ptp-ext:domain-profile' in raw_ptp_default_ds_data and raw_ptp_default_ds_data['ietf-ptp-ext:domain-profile'] != "":
                ptp_default_ds_data['domain_profile'] = raw_ptp_default_ds_data['ietf-ptp-ext:domain-profile']
            if 'ietf-ptp-ext:source-interface' in raw_ptp_default_ds_data:
                ptp_default_ds_data['source_interface'] = raw_ptp_default_ds_data['ietf-ptp-ext:source-interface']

        return ptp_default_ds_data
