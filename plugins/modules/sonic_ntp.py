#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2022 Dell Inc. or its subsidiaries. All Rights Reserved
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
The module file for sonic_ntp
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = """
---
module: sonic_ntp
version_added: 2.0.0
short_description: Manage NTP configuration on SONiC.
description:
  - This module provides configuration management of NTP for devices running SONiC.
author: "M. Zhang (@mingjunzhang2019)"
options:
  config:
    description:
      - Specifies NTP related configurations.
    type: dict
    suboptions:
      source_interfaces:
        type: list
        elements: str
        description:
          - List of names of NTP source interfaces.
      vrf:
        type: str
        description:
          - VRF name on which NTP is enabled.
      servers:
        type: list
        elements: dict
        description:
          - List of NTP servers.
        suboptions:
          address:
            type: str
            description:
              - IPv4/IPv6 address or host name of NTP server.
            required: true
          minpoll:
            type: int
            description:
              - Minimum poll interval to poll NTP server.
          maxpoll:
            type: int
            description:
              - Maximum poll interval to poll NTP server.

  state:
    description:
      - The state of the configuration after module completion.
    type: str
    choices:
    - merged
    - deleted
    default: merged
"""
EXAMPLES = """
# Using deleted
#
# Before state:
# -------------
#
#sonic# show ntp server
#----------------------------------------------------------------------
#NTP Servers                     minpoll maxpoll Authentication key ID
#----------------------------------------------------------------------
#10.11.0.1                       6       10
#10.11.0.2                       5       9
#dell.com                        6       9
#dell.org                        7       10
#
- name: Delete NTP server configuration
  ntp:
    config:
      servers:
        - address: 10.11.0.2
        - address: dell.org
    state: deleted

# After state:
# ------------
#
#sonic# show ntp server
#----------------------------------------------------------------------
#NTP Servers                     minpoll maxpoll Authentication key ID
#----------------------------------------------------------------------
#10.11.0.1                       6       10
#dell.com                        6       9
#
#
# Using deleted
#
# Before state:
# -------------
#
#sonic# show ntp global
#----------------------------------------------
#NTP Global Configuration
#----------------------------------------------
#NTP source-interfaces:  Ethernet0, Ethernet4, Ethernet8, Ethernet16
#
- name: Delete NTP source-interface configuration
  ntp:
    config:
      source_interfaces:
        - Ethernet8
        - Ethernet16
    state: deleted

# After state:
# ------------
#
#sonic# show ntp global
#----------------------------------------------
#NTP Global Configuration
#----------------------------------------------
#NTP source-interfaces:  Ethernet0, Ethernet4
#
#
# Using merged
#
# Before state:
# -------------
#
#sonic# show ntp server
#----------------------------------------------------------------------
#NTP Servers                     minpoll maxpoll Authentication key ID
#----------------------------------------------------------------------
#10.11.0.1                       6       10
#dell.com                        6       9
#
- name: Merge NTP server configuration
  ntp:
    config:
      servers:
        - address: 10.11.0.2
          minpoll: 5
        - address: dell.org
          minpoll: 7
          maxpoll: 10
    state: merged

# After state:
# ------------
#
#sonic# show ntp server
#----------------------------------------------------------------------
#NTP Servers                     minpoll maxpoll Authentication key ID
#----------------------------------------------------------------------
#10.11.0.1                       6       10
#10.11.0.2                       5       9
#dell.com                        6       9
#dell.org                        7       10
#
#
# Using merged
#
# Before state:
# -------------
#
#sonic# show ntp global
#----------------------------------------------
#NTP Global Configuration
#----------------------------------------------
#NTP source-interfaces:  Ethernet0, Ethernet4
#
- name: Merge NTP source-interface configuration
  ntp:
    config:
      source_interfaces:
        - Ethernet8
        - Ethernet16
    state: merged
#
# After state:
# ------------
#
#sonic# show ntp global
#----------------------------------------------
#NTP Global Configuration
#----------------------------------------------
#NTP source-interfaces:  Ethernet0, Ethernet4, Ethernet8, Ethernet16
#
#
"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.ntp.ntp import NtpArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.ntp.ntp import Ntp


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=NtpArgs.argument_spec,
                           supports_check_mode=True)

    result = Ntp(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
