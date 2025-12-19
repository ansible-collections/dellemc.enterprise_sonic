#!/usr/bin/python
# -*- coding: utf-8 -*-
# © Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for sonic_vxlans
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
---
module: sonic_vxlans
version_added: 1.0.0
notes:
  - Tested against Enterprise SONiC Distribution by Dell Technologies.
  - Supports C(check_mode).
short_description: Manage VXLAN configuration on SONiC
description:
  - This module provides configuration management of VXLAN for devices running SONiC
author: Niraimadaiselvam M (@niraimadaiselvamm)
options:
  config:
    description:
      - A list of VXLAN configurations
    type: list
    elements: dict
    suboptions:
      name:
        description:
          - Name of the VXLAN
        type: str
        required: true
      evpn_nvo:
        description:
          - EVPN NVO name
        type: str
      source_ip:
        description:
          - Source IP address of the VTEP
        type: str
      primary_ip:
        description:
          - The VTEP MCLAG primary IP address for this node
        type: str
      external_ip:
        description:
          - The VTEP MCLAG external IP address for this node
        version_added: 2.5.0
        type: str
      qos_mode:
        description:
          - QoS mode to use for prioritizing the network traffic within a VXLAN tunnel
          - Functional default is C(pipe)
        version_added: 4.0.0
        type: str
        choices: [pipe, uniform]
      dscp:
        description:
          - DSCP value of the VXLAN tunnel outer IP header, range 0-63
          - Valid only when I(qos_mode=pipe)
          - Functional default is 0
        version_added: 4.0.0
        type: int
      vlan_map:
        description:
          - List of VNI VLAN map configuration
        type: list
        elements: dict
        suboptions:
          vni:
            description:
              - Specifies the VNI ID
            type: int
            required: true
          vlan:
            description:
              - VLAN ID for VNI VLAN map
            type: int
      vrf_map:
        description:
          - List of VNI VRF map configuration
        type: list
        elements: dict
        suboptions:
          vni:
            description: Specifies the VNI ID
            type: int
            required: true
          vrf:
            description:
              - VRF name for VNI VRF map
            type: str
      suppress_vlan_neigh:
        description:
          - List of suppress VLAN neighbor configuration
        version_added: 3.1.0
        type: list
        elements: dict
        suboptions:
          vlan_name:
            description: Name of VLAN
            type: str
  state:
    description:
      - The state of the configuration after module completion
    type: str
    choices: [merged, deleted, replaced, overridden]
    default: merged
"""

EXAMPLES = """
# Using "deleted" state
#
# Before state:
# -------------
#
# sonic# show running-configuration vxlan
#
# interface vxlan vteptest1
# source-ip 1.1.1.1
# primary-ip 2.2.2.2
# map vni 101 vlan 11
# map vni 102 vlan 12
# map vni 101 vrf Vrfcheck1
# map vni 102 vrf Vrfcheck2
# suppress vlan-neigh vlan_name Vlan11
# suppress vlan-neigh vlan_name Vlan12
# !

- name: "Test vxlans deleted state 01"
  dellemc.enterprise_sonic.sonic_vxlans:
    config:
      - name: vteptest1
        source_ip: 1.1.1.1
        vlan_map:
          - vni: 101
            vlan: 11
        vrf_map:
          - vni: 101
            vrf: Vrfcheck1
        suppress_vlan_neigh:
          - vlan_name: Vlan11
          - vlan_name: Vlan12
    state: deleted

# After state:
# ------------
#
# sonic# show running-configuration vxlan
#
# interface vxlan vteptest1
# source-ip 1.1.1.1
# map vni 102 vlan 12
# map vni 102 vrf Vrfcheck2
# !


# Using "deleted" state
#
# Before state:
# -------------
#
# sonic# show running-configuration vxlan
#
# interface vxlan vteptest1
# source-ip 1.1.1.1
# qos-mode pipe dscp 14
# map vni 102 vlan 12
# map vni 102 vrf Vrfcheck2
# !

- name: "Test vxlans deleted state 02"
  dellemc.enterprise_sonic.sonic_vxlans:
    config:
    state: deleted

# After state:
# ------------
#
# sonic# show running-configuration vxlan
#
# !


# Using "merged" state
#
# Before state:
# -------------
#
# sonic# show running-configuration vxlan
#
# !

- name: "Test vxlans merged state 01"
  dellemc.enterprise_sonic.sonic_vxlans:
    config:
      - name: vteptest1
        source_ip: 1.1.1.1
        primary_ip: 2.2.2.2
        evpn_nvo: nvo1
        qos_mode: pipe
        dscp: 14
        vlan_map:
          - vni: 101
            vlan: 11
          - vni: 102
            vlan: 12
        vrf_map:
          - vni: 101
            vrf: Vrfcheck1
          - vni: 102
            vrf: Vrfcheck2
        suppress_vlan_neigh:
          - vlan_name: Vlan11
          - vlan_name: Vlan12
    state: merged

# After state:
# ------------
#
# sonic# show running-configuration vxlan
#
# interface vxlan vteptest1
# source-ip 1.1.1.1
# primary-ip 2.2.2.2
# qos-mode pipe dscp 14
# map vni 101 vlan 11
# map vni 102 vlan 12
# map vni 101 vrf Vrfcheck1
# map vni 102 vrf Vrfcheck2
# suppress vlan-neigh vlan-name Vlan11
# suppress vlan-neigh vlan-name Vlan12
# !


# Using "overridden" state
#
# Before state:
# -------------
#
# sonic# show running-configuration vxlan
#
# interface vxlan vteptest1
# source-ip 1.1.1.1
# primary-ip 2.2.2.2
# map vni 101 vlan 11
# map vni 102 vlan 12
# map vni 101 vrf Vrfcheck1
# map vni 102 vrf Vrfcheck2
# !

- name: "Test vxlans overridden state 01"
  dellemc.enterprise_sonic.sonic_vxlans:
    config:
      - name: vteptest2
        source_ip: 3.3.3.3
        primary_ip: 4.4.4.4
        evpn_nvo: nvo2
        vlan_map:
          - vni: 101
            vlan: 11
        vrf_map:
          - vni: 101
            vrf: Vrfcheck1
    state: overridden

# After state:
# ------------
#
# sonic# show running-configuration vxlan
#
# interface vxlan vteptest2
# source-ip 3.3.3.3
# primary-ip 4.4.4.4
# map vni 101 vlan 11
# map vni 101 vrf Vrfcheck1
# !


# Using "replaced" state
#
# Before state:
# -------------
#
# sonic# show running-configuration vxlan
#
# interface vxlan vteptest2
# source-ip 3.3.3.3
# primary-ip 4.4.4.4
# map vni 101 vlan 11
# map vni 101 vrf Vrfcheck
# !

- name: "Test vxlans replaced state 01"
  dellemc.enterprise_sonic.sonic_vxlans:
    config:
      - name: vteptest2
        source_ip: 5.5.5.5
        vlan_map:
          - vni: 101
            vlan: 12
    state: replaced

# After state:
# ------------
#
# sonic# show running-configuration vxlan
#
# interface vxlan vteptest2
# source-ip 5.5.5.5
# primary-ip 4.4.4.4
# map vni 101 vlan 12
# map vni 101 vrf Vrfcheck1
# !
"""
RETURN = """
before:
  description: The configuration prior to the module invocation.
  returned: always
  type: list
after:
  description: The resulting configuration from module invocation.
  returned: when changed
  type: list
after_generated:
  description: The generated configuration from module invocation.
  returned: when C(check_mode)
  type: list
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.vxlans.vxlans import VxlansArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.vxlans.vxlans import Vxlans


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=VxlansArgs.argument_spec,
                           supports_check_mode=True)

    result = Vxlans(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
