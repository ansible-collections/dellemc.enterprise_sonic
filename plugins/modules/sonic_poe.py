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
The module file for sonic_poe
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
---
module: sonic_poe
version_added: "2.3.0"
short_description: Manage PoE configuration on SONiC
description:
  - This module provides configuration management of PoE at global and card level for devices running SONiC
author: "Shade Talabi (@stalabi1), Xiao Han (@Xiao_Han2)"
options:
  config:
    description:
      - Specifies PoE configurations
    type: dict
    suboptions:
      global:
        description: PoE global configuration
        type: dict
        suboptions:
          power_mgmt_model:
            description: |
              the power management algorithm. dynamic means that power consumption of each port
              is measured and calculated in real-time. static means that power allocated for each port depends
              on the type of power threshold configured on the port
            type: str
            choices: ['dynamic', 'dynamic-priority', 'static', 'static-priority', 'class']
          usage_threshold:
            description: Inline Power Usage Threshold
            type: int
          auto_reset:
            description: Enable or disable PoE Auto Reset Mode
            type: bool
      cards:
        description: PoE card (power controller hardware) configuration
        type: list
        elements: dict
        suboptions:
          card_id:
            description:
              - Identifier for the card
            type: int
            required: True
          power_mgmt_model:
            description: |
              the power management algorithm. dynamic means that power consumption of each port
              is measured and calculated in real-time. static means that power allocated for each port depends
              on the type of power threshold configured on the port
            type: str
            choices: ['dynamic', 'dynamic-priority', 'static', 'static-priority', 'class']
          usage_threshold:
            description: Inline power usage threshold value
            type: int
          auto_reset:
            description: Enable or disable PoE Auto Reset Mode
            type: bool
      interfaces:
        description: PoE configuration for ethernet interfaces
        type: list
        elements: dict
        suboptions:
          name:
            description: Name of the interface
            type: str
            required: True
          enabled:
            description: enable PoE per port
            type: bool
          priority:
            description:
              - PoE port priority in power management algorithm.
              - Priority could be used by a control mechanism
                that prevents over current situations by disconnecting first
                ports with lower power priority.
              - Ports that connect devices
                critical to the operation of the network - like the E911
                telephones ports - should be set to higher priority.
            type: str
            choices: ['low', 'medium', 'high', 'critical']
          detection:
            description:
              - Device detection mechanism performed by this PSE port.
              - Legacy is capacitive detection scheme, which can be used alone or as a backup if other detection schemes fail.
              - Those schemes are IEEE 802 standard schemes.
              - None cannot be forcibly set by adminstrator.
            type: str
            choices: ['2pt-dot3af', '2pt-dot3af+legacy', '4pt-dot3af', '4pt-dot3af+legacy', 'dot3bt', 'dot3bt+legacy', 'legacy']
          power_up_mode:
            description:
              - The mode configured for a PSE port to deliver high power.
              - pre-dot3at means that a port is powered in the IEEE 802.3af mode initially, switched to the high-power IEEE 802.3at mode
              - dot3at means that a port is powered in the IEEE 802.3at mode.
              - dot3bt, type3 and pre-dot3bt are to support 802.3bt interfaces.
            type: str
            choices: ['dot3af', 'dot3at', 'dot3bt', 'dot3bt-type3', 'dot3bt-type4', 'high-inrush', 'pre-dot3at', 'pre-dot3bt']
          power_pairs:
            description:
              - PoE port power-pairs settings
            type: str
            choices: ['signal', 'spare']
          power_limit_type:
            description:
              - Controls the maximum power that a port can deliver.
              - Class based means means that the port power limit is as per the dot3af class of the powered device attached.
              - User means specified by config
            type: str
            choices: ['class-based', 'user-defined']
          power_limit:
            description:
              - The configured maximum power this port can provide to an attached device measured in Milliwatts.
              - Range 0-99900
            type: int
          high_power:
            description:
              - Enables high power mode on a PSE port
            type: bool
          disconnect_type:
            description: PoE port disconnect type
            type: str
            choices: ['ac', 'dc']
          four_pair:
            description:
              - Enables four pair mode for port
            type: bool
          use_spare_pair:
            description:
              - Enables spare pair power for port
            type: bool
          power_classification:
            description: PoE power-classification mode for port
            type: str
            choices: ['normal', 'bypass']
  state:
    description:
      - The state of the configuration after module completion
    type: str
    choices: ['merged', 'deleted', 'replaced', 'overridden']
    default: merged
"""
EXAMPLES = """
"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: dict
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: dict
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
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.poe.poe import PoeArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.poe.poe import Poe


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=PoeArgs.argument_spec,
                           supports_check_mode=True)

    result = Poe(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
