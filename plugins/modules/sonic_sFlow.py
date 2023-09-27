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
The module file for sonic_sFlow
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = """
---
module: sFlow
description: This module provides configuration for sFlow sampling on devices running SONiC 
version_added: "2.10"
short_description: configure sFlow settings on SONiC
author: "Xiao Han @Xiao_Han2"
options:
  config:
    description:
      - Defines configuration and operational state data related to data plane traffic sampling based on sFlow.
    type: dict
    suboptions:
      enabled:
        type: bool
        default: false
        description: Enables or disables sFlow sampling for the device.
      polling_interval:
        type: int
        description: 
          - sFlow polling interval.
          - must be 0 or in range 5-300
      agent: 
        type: str
        description: The Agent interface 
      collectors:
        description: Configuration data for sFlow collectors.
        type: list
        elements: dict
        suboptions:
          address:
            type: str
            description: IP address of the sFlow collector.
            required: true
          port:
            type: int
            description: UDP port number for the sFlow collector.
            default: 6343
          network_instance:
            type: str
            description: Reference to the network instance used to reach the sFlow collector
            default: "default"
      interfaces:
        description: Configuration data for sFlow data on interfaces.
        type: list
        elements: dict
        suboptions:
          name:
            type: str
            description: Reference to the interface
          enabled:
            type: bool
            description: If sFlow is globally enabled, enables or disables sFlow on the interface
          sampling_rate:
            type: int
            description: Override the global sampling rate for this interface
  state:
    description:
    - The state the configuration should be left in
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    default: merged
"""
EXAMPLES = """
# Examples using Deleted State to remove configuration
  # Before state:
    config:
      enabled: False
      polling_interval: 40
      collectors:
        - address: 1.1.1.1
          port: 6343
          network-instance: default 
      interfaces:
        - name: Ethernet0
          sampling_rate: 400000

  # Example
    - name: "clear all sFlow config and disable"
      sonic_sFlow:
      config: {}
      state: deleted

  # After state:
  # Note, enabled can't be deleted. It's just set to default. everything that can be cleared are deleted
    config:
      enabled: False
      (no other recorded config)
  ------

  # Before state:
    config:
      enabled: True
      polling_interval: 40
      collectors:
        - address: 1.1.1.1
          port: 6343
          network-instance: default 
      interfaces:
        - name: Ethernet0
          sampling_rate: 400000

  # Example
    - name: "clear all sFlow interfaces and collectors"
      sonic_sFlow:
      config:
        interfaces: []
        collectors: []
      state: deleted

  # After state:
    config:
      enabled: False
      polling_interval: 40
  # deletes items config if empty list is provided. The other fields need to be listed and values match to delete, see other Example
  ------

  # Before state:
    config:
      enabled: False
      polling_interval: 40
      collectors:
        - address: 1.1.1.1
          port: 6343
          network-instance: default 
      interfaces:
        - name: Ethernet0
          sampling_rate: 400000
        - name: Ethernet8
          enabled: False
        - name: Ethernet16
          sampling_rate: 400000

  # Example
  # note: to delete interfaces, only need to specify the name, doesn't care about other fields
    - name: "delete individual interfaces"
      sonic_sFlow:
      config:
        interfaces:
          - name: Ethernet8
          - name: Ethernet16
            enabled: False

      state: deleted

  # After state:
  # just listed interfaces deleted
    config:
      enabled: False
      polling_interval: 40
      collectors:
        - address: 1.1.1.1
          port: 6343
          network-instance: default 
      interfaces:
        - name: Ethernet0
          sampling_rate: 400000
  ------

  # Before state:
    config:
      enabled: False
      polling_interval: 40
      collectors:
        - address: 1.1.1.1
          port: 6343
          network-instance: default 
        - address: 1.1.1.2
          port: 6000
          network_instance: "vrf_1"
      interfaces:
        - name: Ethernet0
          sampling_rate: 400000

  # Example:
  # note, need all three fields to identify a collector. port and network instance has default values
    - name: "delete individual collectors"
      sonic_sFlow:
      config:
        collectors:
          - address: 1.1.1.2
            port: 6000
            network_instance: "vrf_1"
          - address: 1.1.1.1
      state: deleted
  
  # After state:
    config:
      enabled: False
      polling_interval: 40
      interfaces:
        - name: Ethernet0
          sampling_rate: 400000
  ------

  # Before state:
    config:
      enabled: True
      polling_interval: 30
      collectors:
        - address: 1.1.1.1
          port: 6343
          network-instance: default 
      interfaces:
        - name: Ethernet0
          sampling_rate: 400000

  # Example    
    - name: "clear other config if values match"
      sonic_sFlow:
      config:
        enabled: False
        polling_interval: 30
      state: deleted

  # After state:
    config:
      enabled: True
      collectors:
        - address: 1.1.1.1
          port: 6343
          network-instance: default 
      interfaces:
        - name: Ethernet0
          sampling_rate: 400000

------------


# Examples using merged state to add configuration
  # Before state:
    config:
      enabled: False

  # Example:
    - name: "add sflow collector, defualt port and network instance"
      sonic_sFlow:
        config:
          collectors:
            - address: 1.1.1.2
        state: merged
  # note there can only be two collectors configured at a time

  # After state:
    config:
      enabled: False
      collectors:
        - address: 1.1.1.2
          port: 6343
          network-instance: default
  ------

  # Before state:
    config:
      enabled: False
      interfaces:
        - name: Ethernet0
          samplig_rate: 400002
  
  # Example
    - name: "setting interface settings"
      sonic_sFlow:
        config:
          interfaces:
            - name: Ethernet0
              enabled: True
            - name: Ethernet8
              enabled: false
              sampling_rate: 400003
        state: merged
  # Note must set at least one of enabled or sampling_rate

  # After state
    config:
      enabled: False
      interfaces:
        - name: Ethernet0
          samplig_rate: 400002
          enabled: True
        - name: Ethernet8
          enabled: false
          sampling_rate: 400003
  ------

  # Before state:
    config:
      enabled: False

  # Example
    - name: "setting other settings"
      sonic_sFlow:
        config:
          polling_interval: 50
          enabled: true
          agent: Ethernet0
        state: merged

  # After state
    config:
      enabled: true
      polling_interval: 50
      agent: Ethernet0

-----------


# Examples using overridden state to set configuration
  # Before state:
    config:
      enabled: False
      polling_interval: 50
      collectors:
        - address: 1.1.1.1
          port: 6343
          network-instance: default 
      interfaces:
        - name: Ethernet0
          enabled: false
        - name: Ethernet8
          enabled: false
        - name: Ethernet16
          enabled: false
        - name: Ethernet24
          enabled: false

  # Example:
    - name: "override sets to passed in task"
      sonic_sFlow:
        config:
          enabled: True
          agent: Ethernet0
          interfaces:
            - name: Ethernet0
              enabled: True
        state: overridden

  # After state:
    config:
      enabled: True
      agent: Ethernet0
      interfaces:
        - name: Ethernet0
          enabled: true
------------


# Examples using replaced state
  # Before state:
    config:
      enabled: False
      polling_interval: 50
      collectors:
        - address: 1.1.1.1
          port: 6343
          network-instance: default 
      interfaces:
        - name: Ethernet0
          enabled: false
        - name: Ethernet8
          enabled: false
        - name: Ethernet16
          enabled: false
        - name: Ethernet24
          enabled: false

  # Example:
    - name: "replace interface subsection"
      sonic_sFlow:
        config:
          interfaces:
            - name: Ethernet0
              enabled: true
        state: replaced

  # After state:
    config:
      enabled: False
      polling_interval: 50
      collectors:
        - address: 1.1.1.1
          port: 6343
          network-instance: default 
      interfaces:
        - name: Ethernet0
          enabled: true
  -----------


"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
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
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.sFlow.sFlow import SflowArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.sFlow.sFlow import Sflow


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=SflowArgs.argument_spec,
                           supports_check_mode=True)

    result = Sflow(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
