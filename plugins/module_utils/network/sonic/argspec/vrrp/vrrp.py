#
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
The arg spec for the sonic_vrrp module
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class VrrpArgs(object):  # pylint: disable=R0903
    """The arg spec for the sonic_vrrp module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        'config': {
            'elements': 'dict',
            'options': {
                'group': {
                    'elements': 'dict',
                    'options': {
                        'advertisement_interval': {'type': 'int'},
                        'afi': {
                            'choices': ['ipv4', 'ipv6'],
                            'required': True,
                            'type': 'str'
                        },
                        'preempt': {'type': 'bool'},
                        'priority': {'type': 'int'},
                        'track_interface': {
                            'elements': 'dict',
                            'options': {
                                'interface': {
                                    'required': True,
                                    'type': 'str'
                                },
                                'priority_increment': {'type': 'int'}
                            },
                            'required_together': [['interface', 'priority_increment']],
                            'type': 'list'
                        },
                        'use_v2_checksum': {'type': 'bool'},
                        'version': {
                            'choices': [2, 3],
                            'type': 'int'
                        },
                        'virtual_address': {
                            'elements': 'dict',
                            'options': {
                                'address': {'type': 'str'}
                            },
                            'type': 'list'
                        },
                        'virtual_router_id': {
                            'required': True,
                            'type': 'int'
                        }
                    },
                    'type': 'list'
                },
                'name': {
                    'required': True,
                    'type': 'str'
                }
            },
            'type': 'list'
        },
        'state': {
            'choices': ['merged', 'deleted', 'overridden', 'replaced'],
            'default': 'merged',
            'type': 'str'
        }
    }  # pylint: disable=C0301
