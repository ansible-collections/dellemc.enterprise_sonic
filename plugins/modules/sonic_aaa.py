#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2024 Dell Inc. or its subsidiaries. All Rights Reserved
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
The module file for sonic_aaa
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = """
---
module: sonic_aaa
version_added: 1.1.0
notes:
- Tested against Enterprise SONiC Distribution by Dell Technologies
- Supports C(check_mode)
author: Shade Talabi (@stalabi1)
short_description: Manage AAA configuration on SONiC
description:
  - This module provides configuration management of AAA for devices running SONiC.
options:
  config:
    description:
      - AAA configuration
    type: dict
    suboptions:
      authentication:
        description:
          - AAA authentication configuration
        type: dict
        version_added: 3.0.0
        suboptions:
          auth_method:
            description:
              - Specifies the order of the methods in which to authenticate login
            type: list
            elements: str
            choices: ['ldap', 'local', 'radius', 'tacacs+']
          console_auth_local :
            description:
              Enable/disable local authentication on console
            type: bool
            default: False
          failthrough:
            description:
              - Enable/disable failthrough
            type: bool
      authorization:
        description:
          - AAA authorization configuration
        type: dict
        version_added: 3.0.0
        suboptions:
          commands_auth_method:
            description:
              - Specifies the order of the methods in which to authorize commands
            type: list
            elements: str
            choices: ['local', 'tacacs+']
          login_auth_method:
            description:
              - Specifies the order of the methods in which to authorize login
            type: list
            elements: str
            choices: ['ldap', 'local']
  state:
    description:
      - The state of the configuration after module completion
    choices: ['merged', 'deleted', 'overridden', 'replaced']
    default: merged
    type: str
"""
EXAMPLES = """
# Using Merged
#
# Before state:
# -------------
#
# sonic# show aaa
# (No AAA configuration present)

- name: Merge AAA configuration
  dellemc.enterprise_sonic.sonic_aaa:
    config:
      authentication:
        auth_method:
          - local
          - ldap
          - radius
          - tacacs+
        console_auth_local: True
        failthrough: True
      authorization:
        commands_auth_method:
          - local
          - tacacs+
        login_auth_method:
          - local
          - ldap
    state: merged

# After state:
# ------------
#
# sonic# show aaa
# ---------------------------------------------------------
# AAA Authentication Information
# ---------------------------------------------------------
# failthrough  : True
# login-method : local, ldap, radius, tacacs+
# console authentication  : local
# ---------------------------------------------------------
# AAA Authorization Information
# ---------------------------------------------------------
# login        : local, ldap
# commands     : local, tacacs+


# Using Replaced
#
# Before state:
# -------------
#
# sonic# show aaa
# ---------------------------------------------------------
# AAA Authentication Information
# ---------------------------------------------------------
# failthrough  : True
# login-method : local, ldap, radius, tacacs+
# console authentication  : local
# ---------------------------------------------------------
# AAA Authorization Information
# ---------------------------------------------------------
# login        : local, ldap
# commands     : local, tacacs+

- name: Replace AAA configuration
  dellemc.enterprise_sonic.sonic_aaa:
    config:
      authentication:
        console_auth_local: True
        failthrough: False
      authorization:
        commands_auth_method:
          - local
    state: replaced

# After state:
# ------------
#
# sonic# show aaa
# ---------------------------------------------------------
# AAA Authentication Information
# ---------------------------------------------------------
# failthrough  : False
# login-method :
# console authentication  : local
# ---------------------------------------------------------
# AAA Authorization Information
# ---------------------------------------------------------
# login        : local


# Using Overridden
#
# Before state:
# -------------
#
# sonic# show aaa
# ---------------------------------------------------------
# AAA Authentication Information
# ---------------------------------------------------------
# failthrough  : True
# login-method : local, ldap, radius, tacacs+
# console authentication  : local
# ---------------------------------------------------------
# AAA Authorization Information
# ---------------------------------------------------------
# login        : local, ldap
# commands     : local, tacacs+

- name: Override AAA configuration
  dellemc.enterprise_sonic.sonic_aaa:
    config:
      authentication:
        auth_method:
          - tacacs+
        console_auth_local: True
        failthrough: True
    state: overridden

# After state:
# ------------
#
# sonic# show aaa
# ---------------------------------------------------------
# AAA Authentication Information
# ---------------------------------------------------------
# failthrough  : True
# login-method : tacacs+
# console authentication  : local


# Using Deleted
#
# Before state:
# -------------
#
# sonic# show aaa
# ---------------------------------------------------------
# AAA Authentication Information
# ---------------------------------------------------------
# failthrough  : True
# login-method : local, ldap, radius, tacacs+
# console authentication  : local
# ---------------------------------------------------------
# AAA Authorization Information
# ---------------------------------------------------------
# login        : local, ldap
# commands     : local, tacacs+

- name: Delete AAA individual attributes
  dellemc.enterprise_sonic.sonic_aaa:
    config:
      authentication:
        auth_method:
          - local
          - ldap
          - radius
          - tacacs+
        console_auth_local: True
        failthrough: True
      authorization:
        commands_auth_method:
          - local
          - tacacs+
        login_auth_method:
          - local
          - ldap
    state: deleted

# After state:
# ------------
#
# sonic# show aaa
# (No AAA configuration present)


# Using Deleted
#
# Before state:
# -------------
#
# sonic# show aaa
# ---------------------------------------------------------
# AAA Authentication Information
# ---------------------------------------------------------
# failthrough  : True
# login-method : local, ldap, radius, tacacs+
# console authentication  : local
# ---------------------------------------------------------
# AAA Authorization Information
# ---------------------------------------------------------
# login        : local, ldap
# commands     : local, tacacs+

- name: Delete all AAA configuration
  dellemc.enterprise_sonic.sonic_aaa:
    config: {}
    state: deleted

# After state:
# ------------
#
# sonic# show aaa
# (No AAA configuration present)
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
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.aaa.aaa import AaaArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.aaa.aaa import Aaa


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=AaaArgs.argument_spec,
                           supports_check_mode=True)

    result = Aaa(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
