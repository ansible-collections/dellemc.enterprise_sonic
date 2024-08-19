#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2024 Dell Inc. or its subsidiaries. All Rights Reserved
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
The module file for sonic_lldp_interfaces
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
---
module: sonic_lldp_interfaces
version_added: '2.1.0'
short_description: Manage Inteface LLDP configurations on SONiC
description:
  - This module provides configuration management of interface LLDP parameters
    in devices running SONiC.
  - It is intended for use in conjunction with global LLDP.
author: 'Divya Balasubramanian(@divya-balasubramania)'
options:
  config:
    description: The set of link layer discovery protocol interface attribute configurations
    type: list
    elements: dict
    suboptions:
      name:
        description:
          - Interface name in which LLDP needs to be configured on.
        type: str
        required: true
      enable:
        description:
          - This argument is a boolean value to enable or disable LLDP.
          - This command is supported only on physical interfaces and not on logical interfaces.
        type: bool
      mode:
        description:
          - By default both transmit and receive of LLDP frames is enabled.
          - This command can be used to configure either in receive only or transmit only mode.
          - This command is supported on physical and logical interfaces.
        type: str
        choices:
           - 'receive'
           - 'transmit'
      med_tlv_select:
        description:
          - This command can be used to select whether to advertise the LLDP-MED TLVs or not.
            By default the LLDP-MED TLVs are advertised.
          - This command is supported only on physical interfaces and not on logical interfaces.
        type: dict
        suboptions:
          network_policy:
            description:
              - This command can be used to select whether to advertise network-policy
                LLDP-MED TLVs or not. By default network-policy LLDP-MED TLVs are advertised.
            type: bool
          power_management:
            description:
              - This command can be used to select whether to advertise power-management
                LLDP-MED TLVs or not. By default power-management LLDP-MED TLVs are advertised.
            type: bool
      tlv_select:
        description:
          - This command can be used to select whether to advertise the LLDP 802.3at or bt
            power management TLVs or not. By default this TLV is advertised.
          - This command is supported only on physical interfaces and not on logical interfaces.
        type: dict
        suboptions:
          power_management:
            description:
              - This command can be used to select whether to advertise power-management
                LLDP TLVs or not. By default power-management LLDP TLVs are advertised.
            type: bool
      tlv_set:
         description:
           - This command can be used to configure an IPv4 or IPv6 management address
            that will be used to advertise by LLDP on an interface
           - This command is supported only on physical interfaces and not on logical interfaces.
         type: dict
         suboptions:
           ipv4_management_address:
             description:
               - To configure IPv4 management address for LLDP in A.B.C.D format
             type: str
           ipv6_management_address:
             description:
               - To configure IPv6 management address for LLDP in A:B::C:D format
             type: str
  state:
    description:
      - The state specifies the type of configuration update to be performed on the device.
      - If the state is "merged", merge specified attributes with existing configured attributes.
      - For "deleted", delete the specified attributes from existing configuration.
      - For "replaced", replaces lldp interface configuration of the specified interfaces with provided configuration.
      - For "overridden", overrides all on-device lldp interface configurations with the provided configuration.
    type: str
    choices:
      - merged
      - deleted
      - replaced
      - overridden
    default: merged
"""
EXAMPLES = """
# Using deleted
#
# Before State:
# -------------
# sonic# show running-configuration interface Ethernet 1
# !
# interface Ethernet1
#  mtu 9100
#  speed 25000
#  unreliable-los auto
#  no shutdown
#  lldp transmit
#  lldp tlv-set management-address ipv4 10.1.1.2
# sonic#

  - name: Delete LLDP interface configurations
    dellemc.enterprise_sonic.sonic_lldp_interfaces:
      config:
        - name: Ethernet1
          mode: transmit
          tlv_set:
            ipv4_management_address: 10.1.1.2
      state: deleted

# After State:
# ------------
# sonic# show running-configuration interface Ethernet 1
# !
# interface Ethernet1
#  mtu 9100
#  speed 25000
#  unreliable-los auto
#  no shutdown
# sonic#


# Using deleted
#
# Before State:
# -------------
# sonic# show running-configuration interface
# !
# interface Ethernet0
#  mtu 9100
#  speed 25000
#  unreliable-los auto
#  no shutdown
# !
# interface Ethernet1
#  mtu 9100
#  speed 25000
#  unreliable-los auto
#  no shutdown
# !
# sonic#

  - name: Delete default LLDP Interface configurations
    dellemc.enterprise_sonic.sonic_lldp_interfaces:
      config:
        - name: Ethernet1
          tlv_select:
            power-management: true
          med_tlv_select:
            network_policy: true
      state: deleted

# After State:
# ------------
# sonic# show running-configuration interface
# !
# interface Ethernet0
#  mtu 9100
#  speed 25000
#  unreliable-los auto
#  no shutdown
# !
# interface Ethernet1
#  mtu 9100
#  speed 25000
#  unreliable-los auto
#  no shutdown
#  no lldp med-tlv-select network-policy
#  no lldp tlv-select power-management
# sonic#


# Using deleted
#
# Before State:
# -------------
# sonic# show running-configuration interface
# !
# interface Ethernet0
#  mtu 9100
#  speed 25000
#  unreliable-los auto
#  no shutdown
#  lldp receive
#  lldp tlv-set management-address ipv4 20.1.1.1
# !
# interface Ethernet1
#  mtu 9100
#  speed 25000
#  unreliable-los auto
#  no shutdown
#  lldp transmit
#  lldp tlv-set management-address ipv4 21.1.1.1
# !
# sonic#

  - name: Delete default LLDP Interface configurations
    dellemc.enterprise_sonic.sonic_lldp_interfaces:
      config:
        - name: Ethernet1
      state: deleted

# After State:
# ------------
# sonic# show running-configuration interface
# !
# interface Ethernet0
#  mtu 9100
#  speed 25000
#  unreliable-los auto
#  no shutdown
#  lldp receive
#  lldp tlv-set management-address ipv4 20.1.1.1
# !
# interface Ethernet1
#  mtu 9100
#  speed 25000
#  unreliable-los auto
#  no shutdown
# sonic#


# Using Merged
#
# Before State:
# -------------
# sonic# show running-configuration interface
# !
# interface Ethernet0
#  mtu 9100
#  speed 25000
#  unreliable-los auto
#  no shutdown
# !
# interface Ethernet1
#  mtu 9100
#  speed 25000
#  unreliable-los auto
#  no shutdown
#  no lldp enable
# !
# sonic#

  - name: Modify LLDP Interface configurations
    dellemc.enterprise_sonic.sonic_lldp_interfaces:
      config:
        - name: Ethernet1
          enable: true
          mode: transmit
          med_tlv_select:
            power_management: true
          tlv_set:
            ipv4_management_address: 10.1.1.2
      state: merged

# After State:
# ------------
# sonic# show running-configuration interface
# !
# interface Ethernet0
#  mtu 9100
#  speed 25000
#  unreliable-los auto
#  no shutdown
# !
# interface Ethernet1
#  mtu 9100
#  speed 25000
#  unreliable-los auto
#  no shutdown
#  lldp transmit
#  lldp tlv-set management-address ipv4 10.1.1.2
# sonic#

# Using replaced
#
# Before State:
# -------------
#
# sonic# show running-configuration interface
# !
# interface Eth1/5
#  mtu 9100
#  speed 10000
#  unreliable-los auto
#  no shutdown
#  lldp tlv-set management-address ipv6 10::1
#  no lldp med-tlv-select network-policy
#  no lldp med-tlv-select power-management
#
# !
# interface Eth1/6
#  mtu 9100
#  speed 10000
#  unreliable-los auto
#  no shutdown
#  no lldp med-tlv-select power-management
#  no lldp tlv-select power-management

  - name: Replace LLDP interface configurations
    dellemc.enterprise_sonic.sonic_lldp_interfaces:
      config:
        - name: Eth1/5
          mode: receive
          tlv_set:
            ipv6_management_address: '30::1'
          med_tlv_select:
            network_policy: False
      state: replaced

# After State:
# ------------
#
# sonic# show running-configuration interface
# !
# interface Eth1/5
#  mtu 9100
#  speed 10000
#  unreliable-los auto
#  no shutdown
#  lldp receive
#  lldp tlv-set management-address ipv6 30::1
#  no lldp med-tlv-select network-policy
# !
# interface Eth1/6
#  mtu 9100
#  speed 10000
#  unreliable-los auto
#  no shutdown
#  no lldp med-tlv-select power-management
#  no lldp tlv-select power-management

# Using overridden
#
# Before State:
# -------------
#
# sonic# show running-configuration interface
# interface Eth1/5
#  mtu 9100
#  speed 10000
#  unreliable-los auto
#  no shutdown
#  lldp transmit
#  lldp tlv-set management-address ipv6 30::2
# !
# interface Eth1/6
#  mtu 9100
#  speed 10000
#  unreliable-los auto
#  no shutdown
#  lldp transmit
#  lldp tlv-set management-address ipv4 40.1.1.1

  - name: Override LLDP interface configurations
    dellemc.enterprise_sonic.sonic_lldp_interfaces:
      config:
        - name: Eth1/5
          mode: receive
          tlv_set:
            ipv4_management_address: '10.1.1.2'
      state: overridden

# After State:
# ------------
#
# sonic# show running-configuration interface
# !
# interface Eth1/5
#  mtu 9100
#  speed 10000
#  unreliable-los auto
#  no shutdown
#  lldp receive
#  lldp tlv-set management-address ipv4 10.1.1.2
# !
# interface Eth1/6
#  mtu 9100
#  speed 10000
#  unreliable-los auto
#  no shutdown

"""
RETURN = """
before:
  description: The configuration prior to the module invocation.
  returned: always
  sample: >
    The configuration returned will always be in the same format
    as the parameters above.
  type: list
after:
  description: The resulting configuration module invocation.
  returned: when changed
  sample: >
    The configuration returned will always be in the same format
    as the parameters above.
  type: list
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.lldp_interfaces.lldp_interfaces import Lldp_interfacesArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.lldp_interfaces.lldp_interfaces import Lldp_interfaces


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=Lldp_interfacesArgs.argument_spec,
                           supports_check_mode=True)

    result = Lldp_interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
