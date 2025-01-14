#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for sonic_lag_interfaces
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
---
module: sonic_lag_interfaces
version_added: 1.0.0
notes:
- Tested against Enterprise SONiC Distribution by Dell Technologies.
- Supports C(check_mode).
short_description: Manage link aggregation group (LAG) interface parameters
description:
  - This module manages attributes of link aggregation group (LAG) interfaces of
    devices running Enterprise SONiC Distribution by Dell Technologies.
author: Abirami N (@abirami-n)

options:
  config:
    description: A list of LAG configurations.
    type: list
    elements: dict
    suboptions:
      name:
        description:
          - ID of the LAG.
        type: str
        required: True
      members:
        description:
          - The list of interfaces that are part of the group.
        type: dict
        suboptions:
          interfaces:
            description:
              - The list of interfaces that are part of the group.
            type: list
            elements: dict
            suboptions:
              member:
                description:
                  - The interface name.
                type: str
      mode:
        description:
          - Specifies mode of the port-channel while creation.
        type: str
        choices:
          - static
          - lacp
      ethernet_segment:
        description:
          - Specifies Ethernet segment.
        version_added: 2.5.0
        type: dict
        suboptions:
          esi_type:
            description:
              - Specifies type of Ethernet Segment Identifier.
                esi_type and esi can not be deleted separately.
                If both esi and df_preference are not present,
                deleted state will delete whole ethernet segment.
            required: True
            type: str
            choices:
              - auto_lacp
              - auto_system_mac
              - ethernet_segment_id
          esi:
            description:
              - Specifies value of Ethernet Segment Identifier.
                Only "AUTO" is supported for auto_lacp and auto_system_mac.
            type: str
          df_preference:
            description:
              - The preference for Designated Forwarder election method.
                The range of df_preference value is from 1 to 65535.
            type: int
  state:
    description:
      - The state that the configuration should be left in.
    type: str
    choices:
     - merged
     - replaced
     - overridden
     - deleted
    default: merged
"""

EXAMPLES = """
# Using "merged" state
#
# Before state:
# -------------
#
# interface Eth1/10
#  mtu 9100
#  speed 100000
#  no shutdown
# !
# interface PortChannel10
#  no shutdown
#
- name: Merges provided configuration with device configuration
  dellemc.enterprise_sonic.sonic_lag_interfaces:
    config:
      - name: PortChannel10
        members:
          interfaces:
            - member: Eth1/10
        ethernet_segment:
          esi_type: auto_lacp
          df_preference: 2222
      - name: PortChannel12
        members:
          interfaces:
            - member: Eth1/15
    state: merged
#
# After state:
# ------------
#
# interface Eth1/10
#  channel-group 10
#  mtu 9100
#  speed 100000
#  no shutdown
# !
# interface Eth1/15
#  channel-group 12
#  mtu 9100
#  speed 100000
#  no shutdown
# !
# interface PortChannel10
#  no shutdown
#  !
#  evpn ethernet-segment auto-lacp
#  df-preference 2222
# !
# interface PortChannel12
#  no shutdown
#
#
# Using "replaced" state
#
# Before state:
# -------------
#
# interface Eth1/5
#   channel-group 10
#   mtu 9100
#   speed 100000
#   no shutdown
# !
# interface Eth1/7
#   no channel-group
#   mtu 9100
#   speed 100000
#   no shutdown
# !
# interface PortChannel10
#  no shutdown
#  !
#  evpn ethernet-segment auto-lacp
#   df-preference 2222
#
- name: Replace device configuration of specified LAG attributes
  dellemc.enterprise_sonic.sonic_lag_interfaces:
    config:
      - name: PortChannel20
        members:
          interfaces:
            - member: Eth1/6
        ethernet_segment:
          esi_type: auto_system_mac
          df_preference: 6666
      - name: PortChannel10
        members:
          interfaces:
            - member: Eth1/7
        ethernet_segment:
          esi_type: auto_system_mac
          df_preference: 3333
    state: replaced
#
# After state:
# ------------
#
# interface Eth1/5
#   mtu 9100
#   speed 100000
#   no shutdown
#
# interface Eth1/6
#   channel-group 20
#   mtu 9100
#   speed 100000
#   no shutdown
#
# interface Eth1/7
#   channel-group 10
#   mtu 9100
#   speed 100000
#   no shutdown
#
# interface PortChannel10
#  no shutdown
#  !
#  evpn ethernet-segment auto-system-mac
#   df-preference 3333
#
# interface PortChanne20
#  no shutdown
#  !
#  evpn ethernet-segment auto-system-mac
#   df-preference 6666
#
# Using "overridden" state
#
# Before state:
# -------------
#
# interface Eth1/5
#   channel-group 10
#   mtu 9100
#   speed 100000
#   no shutdown
#
# interface Eth1/6
#   no channel-group
#   mtu 9100
#   speed 100000
#   no shutdown
#
# interface PortChannel10
#   no shutdown
#   !
#   evpn ethernet-segment auto-system-mac
#    df-preference 2222
#
- name: Override device configuration of all LAG attributes
  dellemc.enterprise_sonic.sonic_lag_interfaces:
    config:
      - name: PortChannel20
        members:
          interfaces:
            - member: Eth1/6
        ethernet_segment:
          esi_type: auto_lacp
          df_preference: 3333
    state: overridden
#
# After state:
# ------------
#
# interface Eth1/5
#   mtu 9100
#   speed 100000
#   no shutdown
#
# interface Eth1/6
#   channel-group 20
#   mtu 9100
#   speed 100000
#   no shutdown
#
# interface PortChannel20
#  no shutdown
#  !
#  evpn ethernet-segment auto-lacp
#   df-preference 3333
#
# Using "deleted" state
#
# Before state:
# -------------
# interface PortChannel 10
#  no shutdown
#  !
#  evpn ethernet-segment auto-lacp
#   df-preference 2222
# !
# interface PortChannel 12
# !
# interface Eth1/10
#  channel-group 10
#  mtu 9100
#  speed 100000
#  no shutdown
# !
# interface Eth1/15
#  channel-group 12
#  mtu 9100
#  speed 100000
#  no shutdown
#
- name: Deletes all LAGs and LAG attributes of all interfaces
  dellemc.enterprise_sonic.sonic_lag_interfaces:
    config:
    state: deleted
#
# After state:
# -------------
#
# interface Eth1/10
#  mtu 9100
#  speed 100000
#  no shutdown
# !
# interface Eth1/15
#  mtu 9100
#  speed 100000
#  no shutdown
#
# Using "deleted" state
#
# Before state:
# -------------
# interface Eth1/10
#  channel-group 10
#  mtu 9100
#  speed 100000
#  no shutdown
# !
# interface PortChannel10
#  no shutdown
#  !
#  evpn ethernet-segment auto-lacp
#   df-preference 2222
#
- name: Deletes some LAGs and LAG attributes.
  sonic_lag_interfaces:
    config:
      - name: PortChannel10
        members:
          interfaces:
            - member: Eth1/10
        ethernet_segment:
          esi_type: auto_lacp
    state: deleted
#
# After state:
# -------------
#
# interface Eth1/10
#  mtu 9100
#  speed 100000
#  no shutdown
# !
# interface PortChannel10
#  no shutdown
#  !
#
"""

RETURN = """
before:
  description: The configuration prior to the module invocation.
  returned: always
  type: list
  sample: >
    The configuration that is returned is always in the same format
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
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.lag_interfaces.lag_interfaces import Lag_interfacesArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.lag_interfaces.lag_interfaces import Lag_interfaces


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=Lag_interfacesArgs.argument_spec,
                           supports_check_mode=True)

    result = Lag_interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
