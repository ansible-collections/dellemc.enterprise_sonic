#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for sonic_fbs_interfaces
"""
from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = """
---
module: sonic_fbs_interfaces
version_added: 4.0.0
notes:
  - Tested against Enterprise SONiC Distribution by Dell Technologies.
  - Supports C(check_mode).
short_description: Manage flow based services (FBS) interfaces configuration on SONiC
description:
  - This module provides configuration management of FBS interfaces for devices running SONiC
author: S. Talabi (@stalabi1)
options:
  config:
    description:
      - FBS interfaces configuration
    type: list
    elements: dict
    suboptions:
      name:
        description:
          - Name of interface
        type: str
        required: true
      ingress_policies:
        description:
          - Ingress policies configuration for the interface
        type: dict
        suboptions:
          forwarding:
            description:
              - Forwarding policy
            type: dict
            suboptions:
              policy_name:
                description:
                  - Name of forwarding policy
                type: str
          monitoring:
            description:
              - Monitoring policy
            type: dict
            suboptions:
              policy_name:
                description:
                  - Name of monitoring policy
                type: str
          qos:
            description:
              - QoS policy
            type: dict
            suboptions:
              policy_name:
                description:
                  - Name of QoS policy
                type: str

      egress_policies:
        description:
          - Egress policies configuration for the interface
        type: dict
        suboptions:
          qos:
            description:
              - QoS policy
            type: dict
            suboptions:
              policy_name:
                description:
                  - Name of QoS policy
                type: str
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
  description: The configuration prior to the module invocation.
  returned: always
  type: list
after:
  description: The resulting configuration module invocation.
  returned: when changed
  type: list
after(generated):
  description: The generated configuration from module invocation.
  returned: when C(check_mode)
  type: list
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.fbs_interfaces.fbs_interfaces import Fbs_interfacesArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.fbs_interfaces.fbs_interfaces import Fbs_interfaces


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=Fbs_interfacesArgs.argument_spec,
                           supports_check_mode=True)

    result = Fbs_interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
