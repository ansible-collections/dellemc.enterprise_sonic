#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for sonic_copp
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
---
module: sonic_copp
version_added: "2.1.0"
notes:
  - Tested against Enterprise SONiC Distribution by Dell Technologies.
  - Supports C(check_mode).
short_description: Manage CoPP configuration on SONiC
description:
  - This module provides configuration management of CoPP for devices running SONiC
author: "Shade Talabi (@stalabi1)"
options:
  config:
    description:
      - Specifies CoPP configurations
    type: dict
    suboptions:
      copp_groups:
        description:
          - List of CoPP entries that comprise a CoPP group
        type: list
        elements: dict
        suboptions:
          copp_name:
            description:
              - Name of CoPP classifier
            type: str
            required: True
          trap_priority:
            description:
              - CoPP trap priority
            type: int
          trap_action:
            description:
              - CoPP trap action
            type: str
          queue:
            description:
              - CoPP queue ID
            type: int
          cir:
            description:
              - Committed information rate in bps or pps (packets per second)
            type: str
          cbs:
            description:
              - Committed bucket size in packets or bytes
            type: str
  state:
    description:
      - The state of the configuration after module completion
    type: str
    choices: ['merged', 'deleted', 'replaced', 'overridden']
    default: merged
"""

EXAMPLES = """
# Using "merged" state
#
# Before state:
# -------------
#
# sonic# show copp actions
# (No "copp actions" configuration present)

- name: Merge CoPP groups configuration
  dellemc.enterprise_sonic.sonic_copp:
  config:
    copp_groups:
      - copp_name: 'copp-1'
        trap_priority: 1
        trap_action: 'DROP'
        queue: 1
        cir: '45'
        cbs: '45'
      - copp_name: 'copp-2'
        trap_priority: 2
        trap_action: 'FORWARD'
        queue: 2
        cir: '90'
        cbs: '90'
  state: merged

# After state:
# ------------
#
# sonic# show copp actions
# CoPP action group copp-1
#    trap-action drop
#    trap-priority 1
#    trap-queue 1
#    police cir 45 cbs 45
# CoPP action group copp-2
#    trap-action forward
#    trap-priority 2
#    trap-queue 2
#    police cir 90 cbs 90
#
#
# Using "replaced" state
#
# Before state:
# -------------
#
# sonic# show copp actions
# CoPP action group copp-1
#    trap-action drop
#    trap-priority 1
#    trap-queue 1
#    police cir 45 cbs 45

- name: Replace CoPP groups configuration
  dellemc.enterprise_sonic.sonic_copp:
  config:
    copp_groups:
      - copp_name: 'copp-1'
        trap_priority: 2
        trap_action: 'FORWARD'
        queue: 2
      - copp_name: 'copp-3'
        trap_priority: 3
        trap_action: 'DROP'
        queue: 3
        cir: '1000'
        cbs: '1000'
  state: replaced

# After state:
# ------------
#
# sonic# show copp actions
# CoPP action group copp-1
#    trap-action forward
#    trap-priority 2
#    trap-queue 2
# CoPP action group copp-3
#    trap-action drop
#    trap-priority 3
#    trap-queue 3
#    police cir 1000 cbs 1000
#
#
# Using "overridden" state
#
# Before state:
# -------------
#
# sonic# show copp actions
# CoPP action group copp-1
#    trap-action forward
#    trap-priority 2
#    trap-queue 2
# CoPP action group copp-3
#    trap-action drop
#    trap-priority 3
#    trap-queue 3
#    police cir 1000 cbs 1000

- name: Override CoPP groups configuration
  dellemc.enterprise_sonic.sonic_copp:
  config:
    copp_groups:
      - copp_name: 'copp-4'
        trap_priority: 4
        trap_action: 'FORWARD'
        queue: 4
        cir: 200
        cbs: 200
  state: overridden

# After state:
# ------------
#
# sonic# show copp actions
# CoPP action group copp-4
#    trap-action forward
#    trap-priority 4
#    trap-queue 4
#    police cir 200 cbs 200
#
#
# Using "deleted" state
#
# Before state:
# -------------
#
# sonic# show copp actions
# CoPP action group copp-1
#    trap-action drop
#    trap-priority 1
#    trap-queue 1
#    police cir 45 cbs 45
# CoPP action group copp-2
#    trap-action forward
#    trap-priority 2
#    trap-queue 2
#    police cir 90 cbs 90

- name: Delete CoPP groups configuration
  dellemc.enterprise_sonic.sonic_copp:
  config:
    copp_groups:
      - copp_name: 'copp-1'
        trap_action: 'DROP'
        cir: '45'
        cbs: '45'
      - copp_name: 'copp-2'
  state: deleted

# After state:
# ------------
#
# sonic# show copp actions
# CoPP action group copp-1
#    trap-action drop
#    police cir 45 cbs 45
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
  description: The resulting configuration module invocation.
  returned: when changed
  type: list
  sample: >
    The configuration returned will always be in the same format
    as the parameters above.
after(generated):
  description: The generated configuration module invocation.
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
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.copp.copp import CoppArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.copp.copp import Copp


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=CoppArgs.argument_spec,
                           supports_check_mode=True)

    result = Copp(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
