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
The module file for sonic_dcbx_global
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
module: sonic_dcbx_global
version_added: '2.1.0'
short_description: Manage DCBX global configurations on SONiC
description:
  - This module provides DCBX global configuration management.
author: 'Haemanthi Sree KR(@haemanthisree)'
options:
  config:
    description: The set of DCBx global attribute configurations
    type: dict
    suboptions:
      enabled:
        description:
          - This argument is a boolean value to enable or disable DCBx.
        type: bool
  state:
    description:
      - The state specifies the type of configuration update to be performed on the device.
        If the state is "merged", merge specified attributes with existing configured attributes.
        For "deleted", delete the specified attributes from existing configuration.
    type: str
    choices:
      - merged
      - deleted
    default: merged
"""
EXAMPLES = """
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
    dellemc.enterprise_sonic.sonic_dcbx_global:
      config:
        enabled: false
      state: deleted

# After State:
# ------------
# sonic# show running-configuration | grep dcbx
# sonic#


# Using Merged
#
# Before State:
# -------------
#
# sonic# show running-configuration | grep dcbx
# sonic#

  - name: Modify DCBX configurations
    dellemc.enterprise_sonic.sonic_dcbx_global:
      config:
        enabled: true
      state: merged

# After State:
# ------------
# sonic# show running-configuration | grep dcbx
# !
# dcbx enable
# !

"""
RETURN = """
before:
  description: The configuration prior to the module invocation.
  returned: always
  type: list
  sample: >
    The configuration returned is always in the same format
    as the parameters above.
after:
  description: The resulting configuration module invocation.
  returned: when changed
  type: list
  sample: >
    The configuration returned is always in the same format
    as the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.dcbx_global.dcbx_global import Dcbx_global
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.dcbx_global.dcbx_global import Dcbx_globalArgs


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=Dcbx_globalArgs.argument_spec,
                           supports_check_mode=True)

    result = Dcbx_global(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
