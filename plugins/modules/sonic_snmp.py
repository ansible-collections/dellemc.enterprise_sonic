#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for sonic_snmp
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
module: sonic_snmp
version_added: 3.3.1
short_description: Manage SNMP configuration on SONiC
description:
  - This module provides configuration management of SNMP for devices running SONiC
author: Aida Shumburo (@aida-shumburo)
options:
  config:
    description:
      - SNMP configuration
    type: dict
    suboptions:
      agentaddress:
        description:
          - List of SNMP agent address configuration
          - I(interface) and I(vrf) are mutually exclusive.
        type: list
        elements: dict
        suboptions:
          interface:
            description:
              - Name of interface
            type: str
          ip:
            description:
              - IPv4 or IPv6 address
            type: str
            required: true
          port:
            description:
              - UDP listening port, range 1024-65535
            type: int
          vrf:
            description:
              - Name of VRF
            type: str
      community:
        description:
          - List of SNMP community configuration
        type: list
        elements: dict
        suboptions:
          group:
            description:
              - Name of community group
            type: str
          name:
            description:
              - Name of community
            type: str
            required: true
      contact:
        description:
          - SNMP server contact information
        type: str
      enable_trap:
        description:
          - Specify trap(s) to enable. The all choice indicates all traps should be enabled
        type: list
        elements: str
        choices:
          - auth-fail
          - bgp
          - config-change
          - link-down
          - link-up
          - ospf
          - all
      engine:
        description:
          - SNMP engine ID
          - Octet (hex) string with colon separated, 5 to 32 octets
        type: str
      group:
        description:
          - List of SNMP group configuration
        type: list
        elements: dict
        suboptions:
          access:
            description:
              - List of access rights configuration for a group
            type: list
            elements: dict
            suboptions:
              notify_view:
                description:
                  - Name of the notify view
                type: str
              read_view:
                description:
                  - Name of the read view
                type: str
              security_level:
                description:
                  -  When I(security_model=v3), specifies the minimum security level under which the access rights apply.
                choices:
                  - no-auth-no-priv
                  - auth-no-priv
                  - auth-priv
                type: str
              security_model:
                description:
                  - Security model used for user authentication
                type: str
                required: true
                choices:
                  - any
                  - v2c
                  - v3
              write_view:
                description:
                  - Name of the write view
                type: str
          name:
            description:
              - Name of the group
            type: str
            required: true
      host:
        description:
          - List of SNMP host configuration
        type: list
        elements: dict
        suboptions:
          community:
            description:
              - SNMP community for the host
            type: str
          ip:
            description:
              - IPv4 or IPv6 address
            type: str
            required: true
          port:
            description:
              - UDP destination port, range 1024-65535
            type: int
          retries:
            description:
              - Number of retries that is only used when "inform" choice is speccified.
              - Has a range between 1 and 255
            type: int
          source_interface:
            description:
              - Name of source interface
            type: str
          tag:
            description:
              - Notification type
              - If "inform" is selected, a "retries" value/option between 1 and 255 can be specified
            type: str
            choices:
              - inform
              - trap
          timeout:
            description:
              - Inform acknowledgement timeout period in seconds, range 1-300
            type: int
          user:
            description:
              - SNMP user
            type: dict
            suboptions:
              name:
                description:
                - Name of the user
                type: str
                required: true
              security_level:
                description:
                  - Security level of the user
                type: str
                choices:
                  - auth
                  - noauth
                  - priv
          vrf:
            description:
              - Name of VRF to be used for sending notifications
            type: str
      location:
        description:
          -SNMP server location information
        type: str
      user:
        description:
          - List of SNMP user configuration
        type: list
        elements: dict
        suboption:
          group:
            description:
              - Name of user group
            type: str
          name:
            description:
              - Name of user
            type: str
            required: true
          auth:
            description:
              - User authentication configuration
            type: dict
            suboptions:
              auth_type:
                description:
                  - Authentication type
                type: str
                choices:
                  - md5
                  - sha
                  - sha2-256
                  - sha2-384
                  - sha2-512
              key:
                description:
                  - Authentication key
                type: str
          priv:
            description:
              - Privacy configuration
            type: dict
            suboptions:
              priv_type:
                description:
                  - Type of encryption
                type: str
                choices:
                  - des
                  - aes
              key:
                description:
                  - Key for the priv_type
                type: str
          encrypted:
            description:
              - Enable/disable encryption for auth and priv keys. The type specified for
              - these keys (encrypted or unencrypted) must be consistent with the value
              - of the "encrypted" option.
            type: bool
      view:
        description:
         - List of SNMP view configuration
        type: list
        elements: dict
        suboptions:
          excluded:
            description:
              - List of OID trees excluded from the view
              - Each string in the list should contain a combination of up to 255 digits and dots ('.')
              - Example 1.27..367.80..8
            type: list
            elements: str
          included:
            description:
              - List of OID trees included in the view
              - Each string in the list should contain a combination of up to 255 digits and dots ('.')
              - Example 1.27..367.80..8
            type: list
            elements: str
          name:
            description:
              - Name of the view
            type: str
            required: true
  state:
    description:
      - The state of the configuration after module completion
    type: str
    choices: ['merged', 'deleted', 'replaced', 'overridden']
    default: merged
"""
EXAMPLES = """
# Using deleted
#
# Before state:
# ---------------
#
# show running-configuration | grep snmp
#
# snmp-server user user1 group group-lab auth
# md5 auth-password
# U2FsdGVkX18J+L+L9OyQYWpAkGUrTgcg/6xzZoDjCbQw1ISHJ5mxmxrYZgQypEUXDeNe6rBupsc9sVDJBKxrwA==
# priv aes-128 priv-password U2FsdGVkX1/Xs+ffZvdV9YzfyGHgIJ+zkLRPfF3/WgYIE1S4Ribvbzhu5chpHHI7ooCBpcVxYZotAXDzgetxvQ==
#
# snmp-server user user2 group group-lab
# auth sha auth-password U2FsdGVkX18J+L+L9OyQYWpAkGUrTgcg/6xzZoDjCbQw1ISHJ5mxmxrYZgQypEUXDeNe6rBupsc9sVDJBKxrwA==
# priv aes-128 priv-password U2FsdGVkX1/Xs+ffZvdV9YzfyGHgIJ+zkLRPfF3/WgYIE1S4Ribvbzhu5chpHHI7ooCBpcVxYZotAXDzgetxvQ==

- name: Delete specific option from snmp-server configuration
  sonic_snmp:
    config:
      user:
        - name: user1
    state: deleted

# After State:
# ---------------
#
# show running-configuration | grep snmp
#
# snmp-server user user2 group group-lab
# auth sha auth-password U2FsdGVkX18J+L+L9OyQYWpAkGUrTgcg/6xzZoDjCbQw1ISHJ5mxmxrYZgQypEUXDeNe6rBupsc9sVDJBKxrwA==
# priv aes-128 priv-password U2FsdGVkX1/Xs+ffZvdV9YzfyGHgIJ+zkLRPfF3/WgYIE1S4Ribvbzhu5chpHHI7ooCBpcVxYZotAXDzgetxvQ==


# Using deleted
#
# Before state:
# ---------------
#
# show running-configuration | grep snmp
#
# snmp-server user user1 group group-lab encrypted auth
# md5 auth-password
# U2FsdGVkX18J+L+L9OyQYWpAkGUrTgcg/6xzZoDjCbQw1ISHJ5mxmxrYZgQypEUXDeNe6rBupsc9sVDJBKxrwA==
# priv aes-128 priv-password U2FsdGVkX1/Xs+ffZvdV9YzfyGHgIJ+zkLRPfF3/WgYIE1S4Ribvbzhu5chpHHI7ooCBpcVxYZotAXDzgetxvQ==
# snmp-server group group-floor2 v3 priv read r_view write w_view notify n_view
# snmp-server community comm1 group group-lab
# snmp-server user user2 group group-lab
# auth sha auth-password U2FsdGVkX18J+L+L9OyQYWpAkGUrTgcg/6xzZoDjCbQw1ISHJ5mxmxrYZgQypEUXDeNe6rBupsc9sVDJBKxrwA==
# priv aes-128 priv-password U2FsdGVkX1/Xs+ffZvdV9YzfyGHgIJ+zkLRPfF3/WgYIE1S4Ribvbzhu5chpHHI7ooCBpcVxYZotAXDzgetxvQ==

- name: Delete all SNMP server configuration for the "user" sub-option.
  sonic_snmp:
    config:
      user:
    state: deleted

# After State:
# ---------------
#
# show running-configuration | grep snmp
#
# snmp-server group group-floor2 v3 priv read r_view write w_view notify n_view
# snmp-server community comm1 group group-lab


# Using merged
#
# Before state:
# ---------------
#
# show running-configuration | grep snmp
# (no snmp-server configuration present)
#

- name: Merge specific option snmp-server configuration
  sonic_snmp:
    config:
      user:
        - name: user2
          auth:
            auth_type: sha
            key: shakey5
          priv:
            priv_type: aes
            key: aes-128
          encrypted: false
    state: merged

# After State:
# ---------------
#
# show running-configuration | grep snmp
#
# snmp-server user user2 group group-lab
# auth sha auth-password U2FsdGVkX18J+L+L9OyQYWpAkGUrTgcg/6xzZoDjCbQw1ISHJ5mxmxrYZgQypEUXDeNe6rBupsc9sVDJBKxrwA==
# priv aes-128 priv-password U2FsdGVkX1/Xs+ffZvdV9YzfyGHgIJ+zkLRPfF3/WgYIE1S4Ribvbzhu5chpHHI7ooCBpcVxYZotAXDzgetxvQ==


# Using merged
#
# Before state:
# ---------------
#
# show running-configuration | grep snmp
# (no snmp-server configuration present)
#

- name: Merge specific option snmp-server configuration
  sonic_snmp:
    config:
      group:
        - name: group-floor2
          access:
            security_model: v3
            security_level: auth-priv
            read_view: r_view
            write_view: w_view
            notify_view: n_view
      community:
        - group: group-lab
          name: comm1
    state: merged

# After State:
# ---------------
#
# show running-configuration | grep snmp
#
# snmp-server community comm1 group group-lab
# snmp-server group group-floor2 v3 priv read r_view write w_view notify n_view


# Using merged
#
# Before state:
# ---------------
#
# show running-configuration | grep snmp
# (no snmp-server configuration present)
#

- name: Merge specific option snmp-server configuration
  sonic_snmp:
    config:
      user:
        - name: user2
          auth:
            auth_type: sha2-256
            key: shakey5
          priv:
            priv_type: aes
            key: aes-128
          encrypted: false
    state: merged

# After State:
# ---------------
#
# show running-configuration | grep snmp
#
# snmp-server user user2 group group-lab
# auth sha2-256 auth-password U2FsdGVkX18J+L+L9OyQYWpAkGUrTgcg/6xzZoDjCbQw1ISHJ5mxmxrYZgQypEUXDeNe6rBupsc9sVDJBKxrwA==
# priv aes-128 priv-password U2FsdGVkX1/Xs+ffZvdV9YzfyGHgIJ+zkLRPfF3/WgYIE1S4Ribvbzhu5chpHHI7ooCBpcVxYZotAXDzgetxvQ==


# Using replaced
#
# Before state:
# ---------------
#
# show running-configuration | grep snmp
#
# snmp-server agentaddress 1.2.3.5 port 1024 interface Eth1/10
# snmp-server user user1 group group-lab encrypted auth
# md5 auth-password
# U2FsdGVkX18J+L+L9OyQYWpAkGUrTgcg/6xzZoDjCbQw1ISHJ5mxmxrYZgQypEUXDeNe6rBupsc9sVDJBKxrwA==
# priv aes-128 priv-password U2FsdGVkX1/Xs+ffZvdV9YzfyGHgIJ+zkLRPfF3/WgYIE1S4Ribvbzhu5chpHHI7ooCBpcVxYZotAXDzgetxvQ==
#

- name: Replace snmp-server configuration
  sonic_snmp:
    config:
      agentaddress:
        - ip: 1.2.3.5
          port: 1024
          interface: Eth1/30
    state: replaced

# After State:
# ---------------
#
# show running-configuration | grep snmp
#
# snmp-server agentaddress 1.2.3.5 port 1024 interface Eth1/30
#


# Using overridden
#
# Before state:
# ---------------
#
# show running-configuration | grep snmp
#
# snmp-server agentaddress 1.2.3.5 port 1024 interface Eth1/10
# snmp-server user user1 group group-lab encrypted auth
# md5 auth-password
# U2FsdGVkX18J+L+L9OyQYWpAkGUrTgcg/6xzZoDjCbQw1ISHJ5mxmxrYZgQypEUXDeNe6rBupsc9sVDJBKxrwA==
# priv aes-128 priv-password U2FsdGVkX1/Xs+ffZvdV9YzfyGHgIJ+zkLRPfF3/WgYIE1S4Ribvbzhu5chpHHI7ooCBpcVxYZotAXDzgetxvQ==
#

- name: Override snmp-server configuration
  sonic_snmp:
    config:
      agentaddress:
        - ip: 1.2.3.5
          port: 1024
          interface: Eth1/30
    state: overridden

# After State:
# ---------------
#
# show running-configuration | grep snmp
#
# snmp-server agentaddress 1.2.3.5 port 1024 interface Eth1/30
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
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.snmp.snmp import SnmpArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.snmp.snmp import Snmp


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=SnmpArgs.argument_spec,
                           supports_check_mode=True)

    result = Snmp(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
