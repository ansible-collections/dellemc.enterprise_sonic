#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for sonic_dcbx
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community',
    'license': 'Apache 2.0'
}

DOCUMENTATION = """
---
module: sonic_dcbx
version_added: '2.1.0'
short_description: Manage DCBx configurations on SONiC
description:
  - This module provides configuration management of DCBx parameters
    in devices running SONiC.
author: 'Bing Sun(@bsun-sudo), Haemanthi Sree KR (@haemanthisree)'
options:
  config:
    description: The set of DCBx attribute configurations
    type: dict
    suboptions:
      global:
        description:
          - Global DCBx configuration
        type: dict
        suboptions:
          enabled:
            description:
              - This argument is a boolean value to enable or disable DCBx.
            type: bool
      interfaces:
        description:
          - Interfaces DCBx configuration
        type: list
        elements: dict
        suboptions:
          name:
            description:
              - Interface name in which DCBx needs to be configured on.
            type: str
            required: true
          enabled:
            description:
              - This argument is a boolean value to enable or disable DCBx.
                By default interface level DCBx is enabled.
              - This command is supported only on physical interfaces and not on logical interfaces.
            type: bool
          pfc_tlv_enabled:
            description:
              - This command can be used to select whether to advertise and receive PFC TLV.
                By default PFC TLV is advertised and received.
            type: bool
          ets_configuration_tlv_enabled:
            description:
              - This command can be used to select whether to advertise and receive ETS configuration TLV.
                By default ETS configuration TLV is advertised and received.
            type: bool
          ets_recommendation_tlv_enabled:
            description:
              - This command can be used to select whether to advertise and receive ETS recommendation TLV.
                By default ETS recommendation TLV is advertised and received.
            type: bool
  state:
    description:
      - The state specifies the type of configuration update to be performed on the device.
      - If the state is "merged", merge specified attributes with existing configured attributes.
      - For "deleted", delete the specified attributes from existing configuration.
    type: str
    choices:
      - merged
      - deleted
    default: merged
"""
EXAMPLES = """
# Using Merged
#
# Before State:
# -------------
# sonic# show running-configuration interface Ethernet9
# !
# interface Ethernet0
#  mtu 9100
#  speed 25000
#  unreliable-los auto
#  no shutdown

  - name: Modify DCBx Interface configurations
    dellemc.enterprise_sonic.sonic_dcbx:
      config:
        -interfaces:
          - name: Ethernet0
            enabled: False
            pfc_tlv_enabled: False
            ets_configuration_tlv_enabled: False
            ets_recommendation_tlv_enabled: False
      state: merged

# After State:
# ------------
# sonic# show running-configuration interface Ethernet0
# !
# interface Ethernet0
#  mtu 9100
#  speed 25000
#  unreliable-los auto
#  no shutdown
#  no dcbx enable
#  no dcbx tlv-select pfc
#  no dcbx tlv-select ets-conf
#  no dcbx tlv-select ets-reco

# Before State:
# -------------
#
# sonic# show running-configuration | grep dcbx
# sonic#

  - name: Modify DCBX configurations
    dellemc.enterprise_sonic.sonic_dcbx:
      config:
        global:
          enabled: true
      state: merged

# After State:
# ------------
# sonic# show running-configuration | grep dcbx
# !
# dcbx enable
# !


# Using Merged
#
# Before State:
# -------------
# sonic# show running-configuration interface Ethernet 0
# !
# interface Ethernet0
#  mtu 9100
#  speed 25000
#  unreliable-los auto
#  no shutdown
#  no dcbx enable
#  no dcbx tlv-select pfc
#  no dcbx tlv-select ets-conf
#  no dcbx tlv-select ets-reco


  - name: Modify DCBx Interface configurations
    dellemc.enterprise_sonic.sonic_dcbx:
      config:
        interfaces:
          - name: Ethernet0
            enabled: True
            pfc_tlv_enabled: True
            ets_configuration_tlv_enabled: True
            ets_recommendation_tlv_enabled: True
      state: deleted

# After State:
# ------------
# sonic# show running-configuration interface Ethernet0
# !
# interface Ethernet0
#  mtu 9100
#  speed 25000
#  unreliable-los auto
#  no shutdown


# Using Merged
#
# Before State:
# -------------
#
# sonic# show running-configuration | grep dcbx
# sonic#

  - name: Modify DCBX configurations
    dellemc.enterprise_sonic.sonic_dcbx:
      config:
        global:
            enabled: true
      state: merged

# After State:
# ------------
# sonic# show running-configuration | grep dcbx
# !
# dcbx enable
# !


# Using Merged
#
# Before State:
# -------------
# sonic# show running-configuration interface Ethernet 0
# !
# interface Ethernet0
#  mtu 9100
#  speed 25000
#  unreliable-los auto
#  no shutdown
#  no dcbx enable
#  no dcbx tlv-select pfc
#  no dcbx tlv-select ets-conf
#  no dcbx tlv-select ets-reco


  - name: Delete and set default DCBx Interface configurations
    dellemc.enterprise_sonic.sonic_dcbx:
      config:
        interfaces:
          - name: Ethernet0
            enabled: False
            pfc_tlv_enabled: False
            ets_configuration_tlv_enabled: False
            ets_recommendation_tlv_enabled: False
      state: deleted

# After State:
# ------------
# sonic# show running-configuration interface Ethernet0
# !
# interface Ethernet0
#  mtu 9100
#  speed 25000
#  unreliable-los auto
#  no shutdown


# Using Merged
#
# Before State:
# -------------
# sonic# show running-configuration interface Ethernet 24
# !
# interface Ethernet24
#  mtu 9100
#  speed 25000
#  unreliable-los auto
#  no shutdown
#  no dcbx enable
#  no dcbx tlv-select pfc
#  no dcbx tlv-select ets-conf
#  no dcbx tlv-select ets-reco


  - name: Delete and set default DCBx Interface configurations
    dellemc.enterprise_sonic.sonic_dcbx:
      config:
        interfaces:
          - name: Ethernet0
            pfc_tlv_enabled: False
      state: deleted

# After State:
# ------------
# sonic# show running-configuration interface Etherneti 24
# !
# interface Ethernet24
#  mtu 9100
#  speed 25000
#  unreliable-los auto
#  no shutdown
#  no dcbx enable
#  no dcbx tlv-select ets-conf
#  no dcbx tlv-select ets-reco


# Using deleted
#
# Before State:
# -------------
#
# sonic# show running-configuration | grep dcbx
# !
# dcbx enable
# !

  - name: Delete DCBX mode configuration
    dellemc.enterprise_sonic.sonic_dcbx:
      config:
        global:
            enabled: true
      state: deleted

# After State:
# ------------
# sonic# show running-configuration | grep dcbx
# sonic#
"""

RETURN = """
before:
  description: The configuration prior to the module invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
    as the parameters above.
after:
  description: The resulting configuration from module invocation.
  returned: when changed, if C(check_mode) is not set
  type: list
  sample: >
    The configuration returned will always be in the same format
    as the parameters above.
after(generated):
  description: The generated (simulated) configuration from module invocation.
  returned: when C(check_mode)
  type: list
  sample: >
    The configuration returned will always be in the same format
     as the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.dcbx.dcbx import DcbxArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.dcbx.dcbx import Dcbx


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=DcbxArgs.argument_spec,
                           supports_check_mode=True)

    result = Dcbx(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
