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
The module file for sonic_logging
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = """
---
module: sonic_logging
version_added: 2.0.0
short_description: Manage logging configuration on SONiC.
description:
  - This module provides configuration management of logging for devices running SONiC.
author: "M. Zhang (@mingjunzhang2019)"
options:
  config:
    description:
      - Specifies logging related configurations.
    type: dict
    suboptions:
      remote_servers:
        type: list
        elements: dict
        description:
          - Remote logging sever configuration.
        suboptions:
          host:
            type: str
            description:
              - IPv4/IPv6 address or host name of the remote logging server.
            required: true
          remote_port:
            type: int
            description:
              - Destination port number for logging messages sent to the server.
              - remote_port can not be deleted.
          source_interface:
            type: str
            description:
              - Source interface used as source ip for sending logging packets.
              - source_interface can not be deleted.
          message_type:
            type: str
            description:
              - Type of messages that remote server receives.
              - message_type can not be deleted.
            choices:
              - log
              - event
          vrf:
            type: str
            description:
              - VRF name used by remote logging server.
  state:
    description:
      - The state of the configuration after module completion.
    type: str
    choices:
      - merged
      - replaced
      - overridden
      - deleted
    default: merged
"""
EXAMPLES = """
# Using deleted
#
# Before state:
# -------------
#
#sonic# show logging servers
#--------------------------------------------------------------------------------
#HOST            PORT      SOURCE-INTERFACE    VRF            MESSGE-TYPE
#--------------------------------------------------------------------------------
#10.11.0.2       5         Ethernet24          -              event
#10.11.1.1       616       Ethernet8           -              log
#log1.dell.com   6         Ethernet28          -              log
#
- name: Delete logging server configuration
  sonic_logging:
    config:
      remote_servers:
        - host: 10.11.0.2
        - host: log1.dell.com
    state: deleted

# After state:
# ------------
#
#sonic# show logging servers
#--------------------------------------------------------------------------------
#HOST            PORT      SOURCE-INTERFACE    VRF            MESSGE-TYPE
#--------------------------------------------------------------------------------
#10.11.1.1       616       Ethernet8           -              log
#
#
# Using merged
#
# Before state:
# -------------
#
#sonic# show logging servers
#--------------------------------------------------------------------------------
#HOST            PORT      SOURCE-INTERFACE    VRF            MESSGE-TYPE
#--------------------------------------------------------------------------------
#10.11.1.1       616       Ethernet8           -              log
#
- name: Merge logging server configuration
  sonic_logging:
    config:
      remote_servers:
        - host: 10.11.0.2
          remote_port: 5
          source_interface: Ethernet24
          message_type: event
        - host: log1.dell.com
          remote_port: 6
          source_interface: Ethernet28
    state: merged

# After state:
# ------------
#
#sonic# show logging servers
#--------------------------------------------------------------------------------
#HOST            PORT      SOURCE-INTERFACE    VRF            MESSGE-TYPE
#--------------------------------------------------------------------------------
#10.11.0.2       5         Ethernet24          -              event
#10.11.1.1       616       Ethernet8           -              log
#log1.dell.com   6         Ethernet28          -              log
#
#
# Using overridden
#
# Before state:
# -------------
#
#sonic# show logging servers
#--------------------------------------------------------------------------------
#HOST            PORT      SOURCE-INTERFACE    VRF            MESSGE-TYPE
#--------------------------------------------------------------------------------
#10.11.1.1       616       Ethernet8           -              log
#10.11.1.2       626       Ethernet16          -              event
#
- name: Replace logging server configuration
  sonic_logging:
    config:
      remote_servers:
        - host: 10.11.1.2
          remote_port: 622
          source_interface: Ethernet24
          message_type: event
    state: overridden
#
# After state:
# ------------
#
#sonic# show logging servers
#--------------------------------------------------------------------------------
#HOST            PORT      SOURCE-INTERFACE    VRF            MESSGE-TYPE
#--------------------------------------------------------------------------------
#10.11.1.2       622       Ethernet24          -              event
#
# Using replaced
#
# Before state:
# -------------
#
#sonic# show logging servers
#--------------------------------------------------------------------------------
#HOST            PORT      SOURCE-INTERFACE    VRF            MESSGE-TYPE
#--------------------------------------------------------------------------------
#10.11.1.1       616       Ethernet8           -              log
#10.11.1.2       626       Ethernet16          -              event
#
- name: Replace logging server configuration
  sonic_logging:
    config:
      remote_servers:
        - host: 10.11.1.2
          remote_port: 622
    state: replaced
#
# After state:
# ------------
#
# "MESSAGE-TYPE" has default value of "log"
#
#sonic# show logging servers
#--------------------------------------------------------------------------------
#HOST            PORT      SOURCE-INTERFACE    VRF            MESSGE-TYPE
#--------------------------------------------------------------------------------
#10.11.1.1       616       Ethernet8           -              log
#10.11.1.2       622       -                   -              log
#
"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  type: list
  returned: always
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
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.logging.logging import LoggingArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.logging.logging import Logging


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=LoggingArgs.argument_spec,
                           supports_check_mode=True)

    result = Logging(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
