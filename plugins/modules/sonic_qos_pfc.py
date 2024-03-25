#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2024 Dell Inc. or its subsidiaries. All Rights Reserved.
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
The module file for sonic_qos_pfc
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
---
module: sonic_qos_pfc
version_added: 2.5.0
notes:
- Tested against Enterprise SONiC Distribution by Dell Technologies.
- Supports C(check_mode).
short_description: Manage QoS PFC configuration on SONiC
description:
  - This module provides configuration management of QoS PFC for devices running SONiC
author: "Shade Talabi (@stalabi1)"
options:
  config:
    description:
      - QoS PFC configuration
    type: dict
    suboptions:
      counter_poll:
        description:
          - Enable or disable use of flex-counters for PFC watchdog
        type: str
        choices:
          - enable
          - disable
      poll_interval:
        description:
          - Polling interval for PFC watchdog
          - Range 100-3000
        type: int
  state:
    description:
      - The state of the configuration after module completion.
    type: str
    choices:
    - merged
    - deleted
    - overridden
    - replaced
    default: merged
"""
EXAMPLES = """
# Using Merged
#
# Before state:
# -------------
#
# sonic# show priority-flow-control watchdog
#
# Watchdog Summary
# ----------------
# Polling Interval:   : Not Available
# Flex Counters:      : Not Available

- name: Merge QoS PFC configurations
  dellemc.enterprise_sonic.sonic_qos_pfc:
    config:
      counter_poll: enabled
      poll_interval: 150
    state: merged

# After state:
# ------------
#
# sonic# show priority-flow-control watchdog
#
# Watchdog Summary
# ----------------
# Polling Interval:   : 150
# Flex Counters:      : enabled
#
#
# Using Replaced
#
# Before state:
# -------------
#
# sonic# show priority-flow-control watchdog
#
# Watchdog Summary
# ----------------
# Polling Interval:   : 150
# Flex Counters:      : enabled

- name: Replace QoS PFC configurations
  dellemc.enterprise_sonic.sonic_qos_pfc:
    config:
      poll_interval: 365
    state: replaced

# After state:
# ------------
#
# sonic# show priority-flow-control watchdog
#
# Watchdog Summary
# ----------------
# Polling Interval:   : 365
# Flex Counters:      : Not Available
#
#
# Using Overridden
# Before state:
# -------------
#
# sonic# show priority-flow-control watchdog
#
# Watchdog Summary
# ----------------
# Polling Interval:   : 365
# Flex Counters:      : Not Available

- name: Override QoS PFC configurations
  dellemc.enterprise_sonic.sonic_qos_pfc:
    config:
      counter_poll: disable
      poll_interval: 400
    state: overridden

# After state:
# ------------
#
# sonic# show priority-flow-control watchdog
#
# Watchdog Summary
# ----------------
# Polling Interval:   : 400
# Flex Counters:      : disabled
#
#
# Using deleted
#
# Before state:
# -------------
#
# sonic# show priority-flow-control watchdog
#
# Watchdog Summary
# ----------------
# Polling Interval:   : 400
# Flex Counters:      : disabled

- name: Delete QoS PFC configurations
  dellemc.enterprise_sonic.sonic_qos_pfc:
    config:
      counter_poll: disable
      poll_interval: 400
    state: deleted

# After state:
# ------------
#
# sonic# show priority-flow-control watchdog
#
# Watchdog Summary
# ----------------
# Polling Interval:   : Not Available
# Flex Counters:      : Not Available
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
after(generated):
  description: The generated configuration model invocation.
  returned: when C(check_mode)
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
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.qos_pfc.qos_pfc import Qos_pfcArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.qos_pfc.qos_pfc import Qos_pfc


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=Qos_pfcArgs.argument_spec,
                           supports_check_mode=True)

    result = Qos_pfc(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
