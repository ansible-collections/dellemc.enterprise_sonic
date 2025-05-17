#
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The arg spec for the sonic_mfa module
"""

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class MfaArgs(object):  # pylint: disable=R0903
    """The arg spec for the sonic_mfa module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        'config': {
            'options': {
                'cac_piv_global': {
                    'options': {
                        'cert_username_field': {
                            'choices': [
                                'common-name',
                                'common-name-or-user-principal-name',
                                'user-principal-name'
                            ],
                            'type': 'str'
                        },
                        'cert_username_match': {
                            'choices': [
                                '10digit-username',
                                'first-name',
                                'username-as-is',
                                'username-without-domain'
                            ],
                            'type': 'str'
                        },
                        'security_profile': {'type': 'str'}
                    },
                    'type': 'dict'
                },
                'mfa_global': {
                    'options': {
                        'client_secret': {'no_log': True, 'type': 'str'},
                        'client_secret_encrypted': {'type': 'bool'},
                        'key_seed': {'no_log': True, 'type': 'str'},
                        'key_seed_encrypted': {'type': 'bool'},
                        'security_profile': {'type': 'str'}
                    },
                    'type': 'dict'
                },
                'rsa_global': {
                    'options': {
                        'security_profile': {'type': 'str'}
                    },
                    'type': 'dict'
                },
                'rsa_servers': {
                    'elements': 'dict',
                    'options': {
                        'client_id': {'type': 'str'},
                        'client_key': {'no_log': True, 'type': 'str'},
                        'client_key_encrypted': {'type': 'bool'},
                        'connection_timeout': {'type': 'int'},
                        'hostname': {'required': True, 'type': 'str'},
                        'read_timeout': {'type': 'int'},
                        'server_port': {'type': 'int'}
                    },
                    'type': 'list'
                }
            },
            'type': 'dict'
        },
        'state': {
            'choices': ['merged', 'deleted', 'replaced', 'overridden'],
            'default': 'merged', 'type': 'str'
        }
    }  # pylint: disable=C0301
