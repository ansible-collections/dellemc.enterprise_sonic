#!/usr/bin/python
# -*- coding: utf-8 -*-
# © Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for sonic_radius_server
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
---
module: sonic_radius_server
version_added: 1.0.0
notes:
  - Tested against Enterprise SONiC Distribution by Dell Technologies.
  - Supports C(check_mode).
author: Niraimadaiselvam M (@niraimadaiselvamm)
short_description: Manage RADIUS server configuration on SONiC
description:
  - This module provides configuration management of radius server for  devices running Enterprise SONiC.
options:
  config:
    description:
      - Specifies the radius server related configuration.
    type: dict
    suboptions:
      auth_type:
        description:
          - Specifies the authentication type of the radius server.
          - The default is C(pap).
        type: str
        choices:
          - pap
          - chap
          - mschapv2
      key:
        description:
          - Specifies the key of the radius server.
        type: str
      nas_ip:
        description:
          - Specifies the network access server of the radius server.
        type: str
      statistics:
        description:
          - Specifies the statistics flag of the radius server.
        type: bool
      timeout:
        description:
          - Specifies the timeout of the radius server.
          - The range is 3 to 60.
          - The default is 5.
        type: int
      retransmit:
        description:
          - Specifies the re-transmit value of the radius server.
          - The range is 0 to 10.
        type: int
      servers:
        description:
          - Specifies the servers list of the radius server.
        type: dict
        suboptions:
          host:
            description:
              - Specifies the host details of the radius servers list.
            type: list
            elements: dict
            suboptions:
              name:
                description:
                  - Specifies the IP address or name of the radius server host.
                type: str
                required: true
              auth_type:
                description:
                  - Specifies the authentication type of the radius server host.
                type: str
                choices:
                  - pap
                  - chap
                  - mschapv2
              key:
                description:
                  - Specifies the key of the radius server host.
                type: str
              priority:
                description:
                  - Specifies the priority of the radius server host.
                  - The range is 1 to 64.
                type: int
              protocol:
                version_added: 4.0.0
                description:
                  - Specifies the protocol of the radius server host.
                  - The functional default is C(UDP).
                type: str
                choices:
                  - TLS
                  - UDP
              port:
                description:
                  - Specifies the port of the radius server host.
                  - The range is 1 to 65535.
                  - The default is 1812.
                type: int
              timeout:
                description:
                  - Specifies the timeout of the radius server host.
                  - The range is 3 to 60.
                type: int
              retransmit:
                description:
                  - Specifies the retransmit of the radius server host.
                  - The range is 0 to 10.
                type: int
              security_profile:
                version_added: 4.0.0
                description:
                  - Specifies the security profile for the radius server host.
                type: str
              source_interface:
                description:
                  - Specifies the source interface of the radius server host.
                type: str
              vrf:
                description:
                  - Specifies the vrf of the radius server host.
                type: str
  state:
    description:
      - Specifies the operation to be performed on the radius server configured on the device.
      - In case of merged, the input mode configuration will be merged with the existing radius server configuration on the device.
      - In case of deleted the existing radius server mode configuration will be removed from the device.
      - In case of replaced, the existing radius server configuration will be replaced with provided configuration.
      - In case of overridden, the existing radius server configuration will be overridden with the provided configuration.
    default: merged
    choices: ['merged', 'replaced', 'overridden', 'deleted']
    type: str
"""

EXAMPLES = """
# Using "deleted" state
#
# Before state:
# -------------
#
# sonic# show running-configuration | grep radius-server
# radius-server nas-ip 10.11.12.13
# radius-server statistics enable
# radius-server timeout 12
# radius-server retransmit 5
# radius-server auth-type chap
# radius-server host 10.10.10.10 protocol TLS security-profile rad-sec-prof
# radius-server host my-host1.dell auth-port 55 timeout 12 retransmit 7 auth-type chap priority 3 vrf VrfAnsibleTest source-interface Ethernet100

- name: Delete specified radius server configuration
  dellemc.enterprise_sonic.sonic_radius_server:
    config:
      auth_type: chap
      nas_ip: 10.11.12.13
      timeout: 12
      servers:
        host:
          - name: 10.10.10.10
    state: deleted

# After state:
# ------------
#
# sonic# show running-configuration | grep radius-server
# radius-server statistics enable
# radius-server retransmit 5
# radius-server host my-host1.dell auth-port 55 timeout 12 retransmit 7 auth-type chap priority 3 vrf VrfAnsibleTest source-interface Ethernet100


# Using "deleted" state
#
# Before state:
# -------------
#
# sonic# show running-configuration | grep radius-server
# radius-server nas-ip 10.11.12.13
# radius-server statistics enable
# radius-server timeout 12
# radius-server retransmit 5
# radius-server auth-type chap
# radius-server host 10.10.10.10 protocol TLS security-profile rad-sec-prof
# radius-server host my-host1.dell auth-port 55 timeout 12 retransmit 7 auth-type chap priority 3 vrf VrfAnsibleTest source-interface Ethernet100

- name: Delete all radius server configuration
  dellemc.enterprise_sonic.sonic_radius_server:
    config:
    state: deleted

# After state:
# ------------
#
# sonic# show running-configuration | grep radius-server
# (No radius-server configuration present)


# Using "merged" state
#
# Before state:
# -------------
#
# sonic# show running-configuration | grep radius-server
# (No radius-server configuration present)

- name: Merge radius server configuration
  dellemc.enterprise_sonic.sonic_radius_server:
    config:
      auth_type: chap
      timeout: 12
      nas_ip: 10.11.12.13
      retransmit: 5
      statistics: true
      servers:
        host:
          - name: my-host1.dell
            auth_type: chap
            priority: 3
            vrf: VrfAnsibleTest
            timeout: 12
            port: 55
            source_interface: Ethernet100
            retransmit: 7
          - name: "10.10.10.10"
            protocol: "TLS"
            security_profile: "rad-sec-prof"
    state: merged

# After state:
# ------------
#
# sonic# show running-configuration | grep radius-server
# radius-server nas-ip 10.11.12.13
# radius-server statistics enable
# radius-server timeout 12
# radius-server retransmit 5
# radius-server auth-type chap
# radius-server host 10.10.10.10 protocol TLS security-profile rad-sec-prof
# radius-server host my-host1.dell auth-port 55 timeout 12 retransmit 7 auth-type chap priority 3 vrf VrfAnsibleTest source-interface Ethernet100


# Using "replaced" state
#
# Before state:
# -------------
#
# sonic# show running-configuration | grep radius-server
# radius-server nas-ip 10.11.12.13
# radius-server statistics enable
# radius-server timeout 12
# radius-server retransmit 5
# radius-server auth-type chap
# radius-server host 10.10.10.10 protocol TLS security-profile rad-sec-prof
# radius-server host my-host1.dell auth-port 55 timeout 12 retransmit 7 auth-type chap priority 3 vrf VrfAnsibleTest source-interface Ethernet100

- name: Replace specified radius server host configuration
  sonic_radius_server:
    config:
      servers:
        - host:
            name: my-host1.dell
            auth_type: mschapv2
            source_interface: Ethernet12
    state: replaced

# After state:
# ------------
#
# sonic# show running-configuration | grep radius-server
# radius-server nas-ip 10.11.12.13
# radius-server statistics enable
# radius-server timeout 12
# radius-server retransmit 5
# radius-server auth-type chap
# radius-server host 10.10.10.10 protocol TLS security-profile rad-sec-prof
# radius-server host my-host1.dell auth-type mschapv2 source-interface Ethernet12

# Using "overridden" state
#
# Before state:
# -------------
#
# sonic# show running-configuration | grep radius-server
# radius-server nas-ip 10.11.12.13
# radius-server statistics enable
# radius-server timeout 12
# radius-server retransmit 5
# radius-server auth-type chap
# radius-server host 10.10.10.10 protocol TLS security-profile rad-sec-prof
# radius-server host my-host1.dell auth-type mschapv2 source-interface Ethernet12

- name: Override radius server configuration
  sonic_radius_server:
    config:
      servers:
        - host:
            name: 20.20.20.20
            protocol: TLS
            security_profile: rad-sec-prof
    state: overridden

# After state:
# ------------
#
# sonic# show running-configuration | grep radius-server
# radius-server host 20.20.20.20 protocol TLS security-profile rad-sec-prof
"""

RETURN = """
before:
  description: The configuration prior to the module invocation.
  returned: always
  type: dict
after:
  description: The resulting configuration module invocation.
  returned: when changed
  type: dict
after_generated:
  description: The generated configuration from module invocation.
  returned: when C(check_mode)
  type: dict
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.radius_server.radius_server import Radius_serverArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.radius_server.radius_server import Radius_server


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=Radius_serverArgs.argument_spec,
                           supports_check_mode=True)

    result = Radius_server(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
