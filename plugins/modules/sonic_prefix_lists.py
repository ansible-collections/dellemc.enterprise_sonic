#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2023 Dell Inc. or its subsidiaries. All Rights Reserved
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
The module file for sonic_prefix_lists
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
---
module: sonic_prefix_lists
version_added: "2.0.0"
author: Kerry Meyer (@kerry-meyer)
short_description: prefix list configuration handling for SONiC
description:
  - This module provides configuration management for prefix list parameters on devices running SONiC.
options:
  config:
    description:
      - Specifies a list of prefix set configuration dictionaries
    type: list
    elements: dict
    suboptions:
      name:
        description:
          - Name of a prefix set (a list of prefix entries)
        type: str
        required: true
      afi:
        description:
          - Specifies the Address Family for addresses in the prefix list entries
        type: str
        choices: ["ipv4", "ipv6"]
        default: "ipv4"
      prefixes:
        description:
          - A list of prefix entries
        type: list
        elements: dict
        suboptions:
          sequence:
            description:
              - Precedence for this prefix entry (unique within the prefix list)
            type: int
            required: true
          action:
            description:
                - Action to be taken for addresses matching this prefix entry
            type: str
            required: true
            choices: ["permit", "deny"]
          prefix:
            description:
              - IPv4 or IPv6 prefix in A.B.C.D/LEN or A:B::C:D/LEN format
            type: str
            required: true
          ge:
            description: Minimum prefix length to be matched
            type: int
          le:
            description: Maximum prefix length to be matched
            type: int
  state:
    description:
      - Specifies the type of configuration update to be performed on the device.
      - For "merged", merge specified attributes with existing configured attributes.
      - For "deleted", delete the specified attributes from existing configuration.
      - For "replaced", replace the specified existing configuration with the provided configuration.
      - For "overridden", override the existing configuration with the provided configuration.
    type: str
    choices:
      - merged
      - deleted
      - replaced
      - overridden
    default: merged
"""
EXAMPLES = """
# Using "merged" state to create initial configuration
#
# Before state:
# -------------
#
# sonic# show running-configuration ip prefix-list
# sonic#
# (No configuration present)
#
# -------------
#
- name: Merge initial prefix-list configuration
  dellemc.enterprise_sonic.sonic_prefix_lists:
     config:
       - name: pfx1
         afi: "ipv4"
         prefixes:
           - sequence: 10
             prefix: "1.2.3.4/24"
             action: "permit"
             ge: 26
             le: 30
     state: merged

# After state:
# ------------
#
# sonic# show running-configuration ip prefix-list
# !
# ip prefix-list pfx1 seq 10 permit 1.2.3.4/24 ge 26 le 30
# ------------
#
# ***************************************************************
# Using "merged" state to update and add configuration
#
# Before state:
# ------------
#
# sonic# show running-configuration ip prefix-list
# !
# ip prefix-list pfx1 seq 10 permit 1.2.3.4/24 ge 26 le 30
#
# sonic# show running-configuration ipv6 prefix-list
# sonic#
# (no IPv6 prefix-list configuration present)
#
# ------------
#
- name: Merge additional prefix-list configuration
  dellemc.enterprise_sonic.sonic_prefix_lists:
     config:
       - name: pfx1
         afi: "ipv4"
         prefixes:
           - sequence: 20
             action: "deny"
             prefix: "1.2.3.12/26"
           - sequence: 30
             action: "permit"
             prefix: "7.8.9.0/24"
       - name: pfx6
         afi: "ipv6"
         prefixes:
           - sequence: 25
             action: "permit"
             prefix: "40::300/124"
     state: merged

# After state:
# ------------
#
# sonic# show running-configuration ip prefix-list
# !
# ip prefix-list pfx1 seq 10 permit 1.2.3.4/24 ge 26 le 30
# ip prefix-list pfx1 seq 20 deny 1.2.3.12/26
# ip prefix-list pfx1 seq 30 permit 7.8.9.0/24
#
# sonic# show running-configuration ipv6 prefix-list
# !
# ipv6 prefix-list pfx6 seq 25 permit 40::300/124
#
# ***************************************************************
# Using "deleted" state to remove configuration
#
# Before state:
# ------------
#
# sonic# show running-configuration ip prefix-list
# !
# ip prefix-list pfx1 seq 10 permit 1.2.3.4/24 ge 26 le 30
# ip prefix-list pfx1 seq 20 deny 1.2.3.12/26
# ip prefix-list pfx1 seq 30 permit 7.8.9.0/24
#
# sonic# show running-configuration ipv6 prefix-list
# !
# ipv6 prefix-list pfx6 seq 25 permit 40::300/124
#
# ------------
#
- name: Delete selected prefix-list configuration
  dellemc.enterprise_sonic.sonic_prefix_lists:
     config:
       - name: pfx1
         afi: "ipv4"
         prefixes:
           - sequence: 10
             prefix: "1.2.3.4/24"
             action: "permit"
             ge: 26
             le: 30
           - sequence: 20
             action: "deny"
             prefix: "1.2.3.12/26"
       - name: pfx6
         afi: "ipv6"
         prefixes:
           - sequence: 25
             action: "permit"
             prefix: "40::300/124"
     state: deleted

# After state:
# ------------
#
# sonic# show running-configuration ip prefix-list
# !
# ip prefix-list pfx1 seq 30 permit 7.8.9.0/24
#
# sonic# show running-configuration ipv6 prefix-list
# sonic#
# (no IPv6 prefix-list configuration present)
#
# ***************************************************************
# Using "overriden" state to override configuration
#
# Before state:
# ------------
#
# sonic# show running-configuration ip prefix-list
# !
# ip prefix-list pfx1 seq 10 permit 1.2.3.4/24 ge 26 le 30
# ip prefix-list pfx1 seq 20 deny 1.2.3.12/26
# ip prefix-list pfx1 seq 30 permit 7.8.9.0/24
#
# sonic# show running-configuration ipv6 prefix-list
# !
# ipv6 prefix-list pfx6 seq 25 permit 40::300/124
#
# ------------
#
- name: Override prefix-list configuration
  dellemc.enterprise_sonic.sonic_prefix_lists:
     config:
       - name: pfx2
         afi: "ipv4"
         prefixes:
           - sequence: 10
             prefix: "10.20.30.128/24"
             action: "deny"
             ge: 25
             le: 30
     state: overridden

# After state:
# ------------
#
# sonic# show running-configuration ip prefix-list
# !
# ip prefix-list pfx2 seq 10 deny 10.20.30.128/24 ge 25 le 30
#
# sonic# show running-configuration ipv6 prefix-list
# sonic#
# (no IPv6 prefix-list configuration present)
#
# ***************************************************************
# Using "replaced" state to replace configuration
#
# Before state:
# ------------
#
# sonic# show running-configuration ip prefix-list
# !
# ip prefix-list pfx2 seq 10 deny 10.20.30.128/24 ge 25 le 30
#
# sonic# show running-configuration ipv6 prefix-list
# sonic#
# (no IPv6 prefix-list configuration present)
#
# ------------
#
- name: Replace prefix-list configuration
  dellemc.enterprise_sonic.sonic_prefix_lists:
     config:
       - name: pfx2
         afi: "ipv4"
         prefixes:
           - sequence: 10
             prefix: "10.20.30.128/24"
             action: "permit"
             ge: 25
             le: 30
       - name: pfx3
         afi: "ipv6"
         prefixes:
           - sequence: 20
             action: "deny"
             prefix: "60::70/124"
     state: replaced

# After state:
# ------------
#
# sonic# show running-configuration ip prefix-list
# !
# ip prefix-list pfx2 seq 10 permit 10.20.30.128/24 ge 25 le 30
#
# sonic# show running-configuration ipv6 prefix-list
# sonic#
# !
# ipv6 prefix-list pfx3 seq 20 deny 60::70/124
#
"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: list
  sample: >

#                       "before": [
#                           {
#                               "afi": "ipv6",
#                               "name": "pf4",
#                               "prefixes": [
#                                   {
#                                       "action": "permit",
#                                       "ge": null,
#                                       "le": null,
#                                       "prefix": "50:60::/64",
#                                       "sequence": 40
#                                   }
#                               ]
#                           },
#                           {
#                               "afi": "ipv4",
#                               "name": "pf3",
#                               "prefixes": [
#                                   {
#                                       "action": "deny",
#                                       "ge": null,
#                                       "le": 27,
#                                       "prefix": "1.2.3.128/25",
#                                       "sequence": 30
#                                   }
#                               ]
#                           },
#                           {
#                               "afi": "ipv4",
#                               "name": "pf2",
#                               "prefixes": [
#                                   {
#                                       "action": "permit",
#                                       "ge": 27,
#                                       "le": 29,
#                                       "prefix": "10.20.30.128/25",
#                                       "sequence": 50
#                                   },
#                                   {
#                                       "action": "deny",
#                                       "ge": 26,
#                                       "le": null,
#                                       "prefix": "10.20.30.0/24",
#                                       "sequence": 20
#                                   }
#                               ]
#                           },
#                           {
#                               "afi": "ipv4",
#                               "name": "pf1",
#                               "prefixes": [
#                                   {
#                                       "action": "deny",
#                                       "ge": 25,
#                                       "le": 27,
#                                       "prefix": "1.2.3.0/24",
#                                       "sequence": 10
#                                   }
#                               ]
#                           }
#                       ]

after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: list
  sample: >

#                       "after": [
#                           {
#                               "afi": "ipv4",
#                               "name": "pf5",
#                               "prefixes": [
#                                   {
#                                       "action": "permit",
#                                       "ge": null,
#                                       "le": null,
#                                       "prefix": "15.25.35.0/24",
#                                       "sequence": 15
#                                   }
#                               ]
#                           },
#                           {
#                               "afi": "ipv4",
#                               "name": "pf1",
#                               "prefixes": [
#                                   {
#                                       "action": "deny",
#                                       "ge": 25,
#                                       "le": 27,
#                                       "prefix": "1.2.3.0/24",
#                                       "sequence": 10
#                                   }
#                               ]
#                           },
#                           {
#                               "afi": "ipv6",
#                               "name": "pf4",
#                               "prefixes": [
#                                   {
#                                       "action": "permit",
#                                       "ge": null,
#                                       "le": null,
#                                       "prefix": "50:60::/64",
#                                       "sequence": 40
#                                   }
#                               ]
#                           },
#                           {
#                               "afi": "ipv4",
#                               "name": "pf3",
#                               "prefixes": [
#                                   {
#                                       "action": "deny",
#                                       "ge": null,
#                                       "le": 27,
#                                       "prefix": "1.2.3.128/25",
#                                       "sequence": 30
#                                   }
#                               ]
#                           },
#                           {
#                               "afi": "ipv4",
#                               "name": "pf2",
#                               "prefixes": [
#                                   {
#                                       "action": "permit",
#                                       "ge": 27,
#                                       "le": 29,
#                                       "prefix": "10.20.30.128/25",
#                                       "sequence": 50
#                                   },
#                                   {
#                                       "action": "deny",
#                                       "ge": 26,
#                                       "le": null,
#                                       "prefix": "10.20.30.0/24",
#                                       "sequence": 20
#                                   }
#                               ]
#                           }
#                       ]

commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample:

#                       "commands": [
#                           {
#                               "afi": "ipv4",
#                               "name": "pf5",
#                               "prefixes": [
#                                   {
#                                       "action": "permit",
#                                       "prefix": "15.25.35.0/24",
#                                       "sequence": 15
#                                   }
#                               ],
#                               "state": "merged"
#                           }
#                       ],
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.prefix_lists.prefix_lists import Prefix_listsArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.prefix_lists.prefix_lists import Prefix_lists


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=Prefix_listsArgs.argument_spec,
                           supports_check_mode=True)

    result = Prefix_lists(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
