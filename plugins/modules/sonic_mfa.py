#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for sonic_mfa
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
---
module: sonic_mfa
version_added: 4.0.0
short_description: Manage Multi-factor authentication (MFA) configurations on SONiC.
description:
  - This module provides configuration management of MFA
    parameters for devices running SONiC.
  - Pre-configured host cert is required for MFA security profile, and
    ca-cert for RSA/CAC-PIV security profiles.
author: 'Divya Narendran (@Divya-N3)'
options:
  config:
    description:
      - Specifies MFA configurations.
    type: dict
    suboptions:
      mfa_global:
        description:
          - MFA Global configuration.
        type: dict
        suboptions:
          key_seed:
            description:
              - Seed for generating secure key in MFA service.
              - Plain text seed i.e. I(key_seed_encrypted=false) will be stored in encrypted format in
                running-config, so idempotency will not be maintained and hence the task output will
                always be I(changed=true).
            type: str
          key_seed_encrypted:
            description:
              - Indicates whether I(key_seed) is plain text or encrypted.
            type: bool
          security_profile:
            description:
              - Security profile contains the certificate for MFA service.
            type: str
          client_secret:
            description:
              - Password used in basic authorization header for MFA REST API.
              - Minimum 32 characters with atleast one symbol, digit, uppercase, and lowercase.
              - Plain text password i.e. I(client_secret_encrypted=false) will be stored in encrypted
                format in running-config, so idempotency will not be maintained and hence the task
                output will always be I(changed=true).
            type: str
          client_secret_encrypted:
            description:
              - Indicates whether I(client_secret) is plain text or encrypted.
            type: bool
      rsa_global:
        description:
          - RSA Global configuration.
        type: dict
        suboptions:
          security_profile:
            description:
              - Security profile with CA-cert for validating RSA SecurID server.
            type: str
      rsa_servers:
        description:
          - RSA Server configuration.
        type: list
        elements: dict
        suboptions:
          hostname:
            description:
              - RSA server's hostname or IP address.
            type: str
            required: True
          server_port:
            description:
              - Port number of the RSA SecurID server.
              - Range 1025-49151.
            type: int
          client_id:
            description:
              - Unique identifier of the system as a client of SecurID service, assigned by SecurID service.
            type: str
          client_key:
            description:
              - Key associated with the client-id, assigned by SecurID service.
              - Plain text key i.e. I(client_key_encrypted=false) will be stored in encrypted format
                in running-config, so idempotency will not be maintained and hence the task output
                will always be I(changed=true).
            type: str
          client_key_encrypted:
            description:
              - Indicates whether I(client_key) is plain text or encrypted.
            type: bool
          connection_timeout:
            description:
              - Timeout in seconds for connection to the SecurID server.
              - Range 1-30.
            type: int
          read_timeout:
            description:
              - Timeout in seconds to read from the SecurID server.
              - Range 1-150.
            type: int
      cac_piv_global:
        description:
          - CAC-PIV Global configuration.
        type: dict
        suboptions:
          security_profile:
            description:
              - Security profile for SSH access with CAC-PIV.
            type: str
          cert_username_field:
            description:
              - SSH user certificate field for matching with SSH login username.
            type: str
            choices:
              - common-name
              - common-name-or-user-principal-name
              - user-principal-name
          cert_username_match:
            description:
              - Match option to parse the username from respective certificate field.
            type: str
            choices:
              - 10digit-username
              - first-name
              - username-as-is
              - username-without-domain
  state:
    description:
      - The state of the configuration after module completion.
      - C(merged) - Merges provided MFA configuration with on-device configuration.
      - C(replaced) - Replaces on-device MFA configuration with provided configuration.
      - C(overridden) - Overrides all on-device MFA configurations with the provided configuration.
      - C(deleted) - Deletes on-device MFA configuration.
    type: str
    choices:
      - merged
      - deleted
      - replaced
      - overridden
    default: merged
"""

EXAMPLES = """
# Using "deleted" state
#
# Before state:
# -------------
#
# sonic# show running-configuration mfa
# mfa key-seed U2FsdGVkX1/caD7u0ZGRnb981G2DKyML/Gvyfexsurg= encrypted
# mfa client-secret U2FsdGVkX1+WlquxtZRbsgQhfS1lQBFbJKflxGAp6S3u+Ox5Hi+O16NmprjMVb3HQn1pNSgaaa0Cz1MHeTfDWhFR0WqdENbLU2PqkiRDHv0iVfl72xNPzhnGeO01kAu0 encrypted
# mfa security-profile mSecurityProfile
# mfa rsa-server security-profile rSecProfile
# mfa rsa-server host rsaserver.che-lab.it port 1030 client-id sonicdevtest.che-lab.it client-key
# U2FsdGVkX18QFJoB9dp8GJN92eP79FGOZDLgQakBmAasGYX77p6PtiiAfS/nGoOb2uEocUkryc+BLLYsg+Wz0gO+c1QsIbIhXk5Pt+aECoVgoFQ9QpxO9od9cTik+3Ot encrypted
# connection-timeout 29 read-timeout 149
#
# sonic# show running-configuration | grep "cac-piv"
# aaa cac-piv cert-user common-name
# aaa cac-piv cert-user-match 10digit-username
# aaa cac-piv security-profile cSecurityProfile
# sonic#


- name: Delete specified mfa configuration
  dellemc.enterprise_sonic.sonic_mfa:
    config:
      mfa_global:
        key_seed: 'U2FsdGVkX1/caD7u0ZGRnb981G2DKyML/Gvyfexsurg='
        key_seed_encrypted: true
        client_secret: 'U2FsdGVkX1+WlquxtZRbsgQhfS1lQBFbJKflxGAp6S3u+Ox5Hi+O16NmprjMVb3HQn1pNSgaaa0Cz1MHeTfDWhFR0WqdENbLU2PqkiRDHv0iVfl72xNPzhnGeO01kAu0'
        client_secret_encrypted: true
      rsa_global:
        security_profile: 'rSecProfile'
      rsa_servers:
        hostname: 'rsaserver.che-lab.it'
        server_port: 1030
        client_id: 'sonicdevtest.che-lab.it'
        client_key: 'U2FsdGVkX18QFJoB9dp8GJN92eP79FGOZDLgQakBmAasGYX77p6PtiiAfS/nGoOb2uEocUkryc+BLLYsg+Wz0gO+c1QsIbIhXk5Pt+aECoVgoFQ9QpxO9od9cTik+3Ot'
        client_key_encrypted: true
        connection_timeout: 29
        read_timeout: 149
      cac_piv_global:
        security_profile: 'cSecurityProfile'
        cert_username_field: 'common-name'
    state: deleted


# After state:
# ------------
#
# sonic# show running-configuration mfa
# mfa security-profile mSecurityProfile
#
# sonic# show running-configuration | grep "cac-piv"
# aaa cac-piv cert-user-match 10digit-username
# sonic#


# Using "deleted" state
#
# Before state:
# -------------
#
# sonic# show running-configuration mfa
# mfa key-seed U2FsdGVkX1/caD7u0ZGRnb981G2DKyML/Gvyfexsurg= encrypted
# mfa client-secret U2FsdGVkX1+WlquxtZRbsgQhfS1lQBFbJKflxGAp6S3u+Ox5Hi+O16NmprjMVb3HQn1pNSgaaa0Cz1MHeTfDWhFR0WqdENbLU2PqkiRDHv0iVfl72xNPzhnGeO01kAu0 encrypted
# mfa security-profile mSecurityProfile
# mfa rsa-server security-profile rSecProfile
# mfa rsa-server host rsaserver.che-lab.it port 1030 client-id sonicdevtest.che-lab.it client-key
# U2FsdGVkX18QFJoB9dp8GJN92eP79FGOZDLgQakBmAasGYX77p6PtiiAfS/nGoOb2uEocUkryc+BLLYsg+Wz0gO+c1QsIbIhXk5Pt+aECoVgoFQ9QpxO9od9cTik+3Ot encrypted
# connection-timeout 29 read-timeout 149
#
# sonic# show running-configuration | grep "cac-piv"
# aaa cac-piv cert-user common-name
# aaa cac-piv cert-user-match 10digit-username
# aaa cac-piv security-profile cSecurityProfile
# sonic#


- name: Delete all mfa configurations
  dellemc.enterprise_sonic.sonic_mfa:
    config:
    state: deleted


# After state:
# ------------
#
# sonic# show running-configuration mfa
# sonic#
#
# sonic# show running-configuration | grep "cac-piv"
# sonic#


# Using "merged" state
#
# Before State:
# -------------
#
# sonic# show running-configuration mfa
# sonic#
#
# sonic# show running-configuration | grep "cac-piv"
# sonic#


- name: Merge provided MFA configurations
  dellemc.enterprise_sonic.sonic_mfa:
    config:
      mfa_global:
        security_profile: 'mSecurityProfile'
        key_seed: 'sonic'
        key_seed_encrypted: true
        client_secret: 'U2FsdGVkX18mPdwkM1z24i7lxMtqNZR9p2q3aa6YXR16OfDxQXCR9z9I0lQZpVjE!'
        client_secret_encrypted: true
      rsa_global:
        security_profile: 'rSecProfile'
      rsa_servers:
        hostname: 'rsaserver.che-lab.it'
        server_port: 1030
        client_id: 'sonicdevtest.che-lab.it'
        client_key: 'aplr05825jshusp80699scuv62u5l3lu63wxf66b0y883w92677ac0c9m0lwv6o8'
        client_key_encrypted: true
        connection_timeout: 29
        read_timeout: 149
      cac_piv_global:
        security_profile: 'cSecurityProfile'
        cert_username_field: 'user-principal-name'
        cert_username_match: '10digit-username'
    state: merged


# After State:
# ------------
#
# sonic# show running-configuration mfa
# mfa key-seed U2FsdGVkX1/caD7u0ZGRnb981G2DKyML/Gvyfexsurg= encrypted
# mfa client-secret U2FsdGVkX1+WlquxtZRbsgQhfS1lQBFbJKflxGAp6S3u+Ox5Hi+O16NmprjMVb3HQn1pNSgaaa0Cz1MHeTfDWhFR0WqdENbLU2PqkiRDHv0iVfl72xNPzhnGeO01kAu0 encrypted
# mfa security-profile mSecurityProfile
# mfa rsa-server security-profile rSecProfile
# mfa rsa-server host rsaserver.che-lab.it port 1030 client-id sonicdevtest.che-lab.it client-key
# U2FsdGVkX18QFJoB9dp8GJN92eP79FGOZDLgQakBmAasGYX77p6PtiiAfS/nGoOb2uEocUkryc+BLLYsg+Wz0gO+c1QsIbIhXk5Pt+aECoVgoFQ9QpxO9od9cTik+3Ot encrypted
# connection-timeout 29 read-timeout 149
#
# sonic# show running-configuration | grep "cac-piv"
# aaa cac-piv cert-user user-principal-name
# aaa cac-piv cert-user-match 10digit-username
# aaa cac-piv security-profile cSecurityProfile


# Using "replaced" state
#
# Before state:
# -------------
#
# sonic# show running-configuration mfa
# mfa key-seed U2FsdGVkX1/caD7u0ZGRnb981G2DKyML/Gvyfexsurg= encrypted
# mfa rsa-server host rsaserver.che-lab.it port 1030 client-id sonicdevtest.che-lab.it client-key
# U2FsdGVkX1+xnsxfUrqCvBQg0KkPUm11R8Vpn2cXLHCWzL59k3Jm4/OrRiMOemPJccnEa8sMuynOAaySpHkaMOePtpedW0aApp+qicIF2Hz32LR4vB07b7OSx7OaEZBj encrypted
# connection-timeout 16 read-timeout 129


- name: Replace specified mfa rsa-server configuration
  dellemc.enterprise_sonic.sonic_mfa:
    config:
      rsa_servers:
        - hostname: 'rsaserver.che-lab.it'
          server_port: 1050
          client_id: 'sonicdevtest.che-lab.it'
          client_key: 'aplr05825jshusp80699scuv62u5l3lu63wxf66b0y883w92677ac0c9m0lwv6o8'
          client_key_encrypted: true
          connection_timeout: 29
          read_timeout: 149
    state: replaced


# After state:
# ------------
#
# sonic# show running-configuration mfa
# mfa key-seed U2FsdGVkX1/caD7u0ZGRnb981G2DKyML/Gvyfexsurg= encrypted
# mfa rsa-server host rsaserver.che-lab.it port 1050 client-id sonicdevtest.che-lab.it client-key
# U2FsdGVkX1/b1Tjka6pWv1BjwGd1I8cfjXxBIIJ6ZK/JaZpGgPbNAnw6WmdstRWJz49A+bymj6gJfkGjbzlWQhGCGi4VofPStOdNktqDcIyk33AaDkO+awkzyi7HRxcB encrypted
# connection-timeout 29 read-timeout 149


# Using "overridden" state
#
# Before state:
# -------------
#
# sonic# show running-configuration mfa
# mfa key-seed U2FsdGVkX1/caD7u0ZGRnb981G2DKyML/Gvyfexsurg= encrypted
# mfa client-secret U2FsdGVkX1+WlquxtZRbsgQhfS1lQBFbJKflxGAp6S3u+Ox5Hi+O16NmprjMVb3HQn1pNSgaaa0Cz1MHeTfDWhFR0WqdENbLU2PqkiRDHv0iVfl72xNPzhnGeO01kAu0 encrypted
# mfa security-profile mSecurityProfile
# mfa rsa-server security-profile rSecProfile
# mfa rsa-server host sonicrsaserver.che-lab.it port 1030 client-id sonic.che-lab.it client-key
# U2FsdGVkX18QFJoB9dp8GJN92eP79FGOZDLgQakBmAasGYX77p6PtiiAfS/nGoOb2uEocUkryc+BLLYsg+Wz0gO+c1QsIbIhXk5Pt+aECoVgoFQ9QpxO9od9cTik+3Ot encrypted
# connection-timeout 29 read-timeout 149
#
# sonic# show running-configuration | grep "cac-piv"
# aaa cac-piv cert-user user-principal-name
# aaa cac-piv cert-user-match 10digit-username
# aaa cac-piv security-profile cSecurityProfile


- name: Override device configuration of mfa with provided configuration
  dellemc.enterprise_sonic.sonic_mfa:
    config:
      cac_piv_global:
        cert_username_match: 'first-name'
    state: overridden


# After state:
# ------------
#
# sonic# show running-configuration | grep "cac-piv"
# aaa cac-piv cert-user-match first-name
"""
RETURN = """
before:
  description: The configuration prior to module invocation.
  returned: always
  type: dict
after:
  description: The configuration resulting from module invocation.
  returned: when changed
  type: dict
generated_after:
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
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.mfa.mfa import MfaArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.mfa.mfa import Mfa


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=MfaArgs.argument_spec,
                           supports_check_mode=True)

    result = Mfa(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
