#
# -*- coding: utf-8 -*-
# © Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
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
                    'default': 'pap',
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
                                'port': {'type': 'int', 'default': 1812},
                                'priority': {'type': 'int'},
                                'retransmit': {'type': 'int'},
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
                'timeout': {'type': 'int', 'default': 5}
            },
            'type': 'dict'
        },
        'state': {
            'choices': ['merged', 'replaced', 'overridden', 'deleted'],
            'default': 'merged'
        }
    }  # pylint: disable=C0301
