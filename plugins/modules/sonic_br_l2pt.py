#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for sonic_br_l2pt
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
module: sonic_br_l2pt
version_added: '2.1.0'
short_description: Manage L2PT configurations on SONiC
description:
  - This module provides configuration management of L2PT parameters
    in devices running SONiC. 
author: 'Allen Ting (@allenkting)'
options:
  config:
    description: A list of L2PT configurations.
    type: list
    elements: dict
    suboptions:
      name:
        description: Interface name for L2PT configuration.
        type: str
        required: true
      protocol:
        description:
          - This defines which protocol to be used for tunneling L2 Protocol packets. 
        type: dict  
        suboptions:
          LLDP:
            description: Configuration for the LLDP protocol
            type: dict
            suboptions:
              vlan_ids:
                description: 
                  - List of VLAN IDs on which the L2 Protocol packets are to be tunneled.
                type: list
                elements: str
          LACP:
            description: Configuration for the LACP protocol
            type: dict
            suboptions:
              vlan_ids:
                description: 
                  - List of VLAN IDs on which the L2 Protocol packets are to be tunneled.
                type: list
                elements: str
          STP:
            description: Configuration for the STP protocol
            type: dict
            suboptions:
              vlan_ids:
                description:
                  - List of VLAN IDs on which the L2 Protocol packets are to be tunneled.
                type: list
                elements: str
          CDP:
            description: Configuration for the CDP protocol
            type: dict
            suboptions:
              vlan_ids:
                description:
                  - List of VLAN IDs on which the L2 Protocol packets are to be tunneled.
                type: list
                elements: str
  state:
    description:
      - The state specifies the type of configuration update to be performed on the device.
      - If the state is "merged", merge specified attributes with existing configured attributes.
      - For "deleted", delete the specified attributes from existing configuration. 
    type: str
    choices:
      - merged
    default: merged
"""
EXAMPLES = """
# Using Merged
#
# Before State:
# -------------
# sonic# show running-configuration interface Ethernet 0
# !
# interface Ethernet0
#  mtu 9100
#  speed 400000
#  fec RS
#  unreliable-los auto
#  no shutdown
#  switchport l2proto-tunnel lldp Vlan 10

  - name: Modify interface L2PT configurations
    dellemc.enterprise_sonic.sonic_br_l2pt:
      config:
        - name: Ethernet0
          protocol:
            LACP:
              vlan_ids:
                - 10-12
            CDP:
              vlan_ids:
                - 20
                - 40-60
            STP:
              vlan_ids:
                - 25-26
      state: merged

# After State:
# ------------
# sonic# show running-configuration interface Ethernet0
# !
# interface Ethernet0
#  mtu 9100
#  speed 400000
#  fec RS
#  unreliable-los auto
#  no shutdown
#  switchport l2proto-tunnel cdp Vlan 20,40-60
#  switchport l2proto-tunnel lacp Vlan 10-12
#  switchport l2proto-tunnel lldp Vlan 10
#  switchport l2proto-tunnel stp Vlan 25-26


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
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.br_l2pt.br_l2pt import Br_l2ptArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.br_l2pt.br_l2pt import Br_l2pt


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=Br_l2ptArgs.argument_spec,
                           supports_check_mode=True)

    result = Br_l2pt(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()