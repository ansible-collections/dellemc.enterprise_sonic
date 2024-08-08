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
The module file for sonic_password_complexity
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
module: sonic_password_complexity
version_added: '2.5.0'
short_description: Manage Global Login Password Attribute configurations on SONiC
description:
  - This module provides configuration management of login password parameters.
  - Password Complexity is used to configure the user password attributes.
    The password attributes include the number of lower-case characters, 
    upper-case characters, numeric characters, special characters, and
    the minimum length of the password.
author: 'Arul Kumar Shankara Narayanan(@arulkumar9690)'
options:
  config:
    description: The set of login password attribute configurations
    type: dict
    suboptions:
      min_upper_case:
        description:
          - Minimum number of uppercase characters required
          - The range is from 0 to 31
        type: int
      min_lower_case:
        description:
          - Minimum number of lowercase characters required
          - The range is from 0 to 31
        type: int
      min_numerals:
        description:
          - Minimum number of numeric characters required
          - The range is from 0 to 31
        type: int
      min_spl_char:
        description:
          - Minimum number of special characters required
          - The range is from 0 to 31
        type: int
      min_length:
        description:
          - Minimum number of required alphanumeric characters
          - The range is from 6 to 32
        type: int
  state:
    description:
      - Specifies the operation to be performed on the login password attributes configured on the device.
      - If the state is "merged", merge specified attributes with existing configured login password attributes.
      - For "deleted", delete the specified login password attributes from the existing configuration.
      - For "overridden", Overrides all on-device login password attribute configurations with the provided configuration.
      - For "replaced", Replaces on-device login password attribute configurations with the provided configuration.
    type: str
    choices:
      - merged
      - deleted
      - overridden
      - replaced
    default: merged
"""
EXAMPLES = """
# Using deleted
#
# Before State:
# -------------
#
# sonic# show running-configuration | grep password-attribute
# !
# login password-attribute character-restriction numeric 2
# login password-attribute min-length 9
# !
# sonic#

  - name: Delete Login Password attribute configurations
    dellemc.enterprise_sonic.sonic_password_complexity:
      config:
              min_numerals: 2
      state: deleted

# After State:
# ------------
# sonic# show running-configuration | grep password-attribute
# !
# login password-attribute min-length 9
# !


# Using Merged
#
# Before State:
# -------------
#
# sonic# show running-configuration | grep password-attribute
# sonic#

  - name: Modify Login Password Attribute configurations
    dellemc.enterprise_sonic.sonic_password_complexity:
      config:
              min_length: 9
              min_lower_case: 2
      state: merged 

# After State:
# ------------
# sonic# show running-configuration | grep password-attribute
# !
# login password-attribute character-restriction lower 2
# login password-attribute min-length 9
# !


# Using overridden
#
# Before State:
# -------------
#
# sonic# show running-configuration | grep password-attribute
# !
# login password-attribute character-restriction lower 2
# login password-attribute min-length 9
# !
# sonic#

  - name: Modify Login Password attribute configurations
    dellemc.enterprise_sonic.sonic_password_complexity:
      config:
              min_length: 10
              min_upper_case: 2
              min_lower_case: 3
      state: overridden

# After State:
# ------------
# sonic# show running-configuration | grep password-attribute
# !
# login password-attribute character-restriction lower 3
# login password-attribute character-restriction upper 2
# login password-attribute min-length 10
# !


# Using replaced
#
# Before State:
# -------------
#
# sonic# show running-configuration | grep password-attribute
# !
# login password-attribute character-restriction numeric 2
# login password-attribute min-length 9
# !
# sonic#

  - name: Modify Login Password attribute configurations
    dellemc.enterprise_sonic.sonic_password_complexity:
      config:
              min_spl_char: 1
      state: replaced

# After State:
# ------------
# sonic# show running-configuration | grep password-attribute
# !
# login password-attribute character-restriction special-char 1
# !


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
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.password_complexity.password_complexity import Password_complexityArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.password_complexity.password_complexity import Password_complexity


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=Password_complexityArgs.argument_spec,
                           supports_check_mode=True)

    result = Password_complexity(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
