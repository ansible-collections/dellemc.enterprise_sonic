#
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The arg spec for the sonic_radius_server module
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class Radius_serverArgs(object):  # pylint: disable=R0903
    """The arg spec for the sonic_radius_server module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        'config': {
            'options': {
                'auth_type': {
                    'choices': ['pap', 'chap', 'mschapv2'],
                    'type': 'str'
                },
                'key': {'type': 'str', 'no_log': True},
                'nas_ip': {'type': 'str'},
                'retransmit': {'type': 'int'},
                'servers': {
                    'options': {
                        'host': {
                            'elements': 'dict',
                            'options': {
                                'auth_type': {
                                    'choices': ['pap', 'chap', 'mschapv2'],
                                    'type': 'str'
                                },
                                'key': {'type': 'str', 'no_log': True},
                                'name': {'type': 'str'},
                                'port': {'type': 'int'},
                                'priority': {'type': 'int'},
                                'protocol': {
                                    'choices': ['TLS', 'UDP'],
                                    'type': 'str'
                                },
                                'retransmit': {'type': 'int'},
                                'security_profile': {'type': 'str'},
                                'source_interface': {'type': 'str'},
                                'timeout': {'type': 'int'},
                                'vrf': {'type': 'str'}
                            },
                            'type': 'list'
                        }
                    },
                    'type': 'dict'
                },
                'statistics': {'type': 'bool'},
                'timeout': {'type': 'int'}
            },
            'type': 'dict'
        },
        'state': {
            'choices': ['merged', 'replaced', 'overridden', 'deleted'],
            'default': 'merged'
        }
    }  # pylint: disable=C0301
