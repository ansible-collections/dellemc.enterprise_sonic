#
# -*- coding: utf-8 -*-
# Copyright 2023 Dell Inc. or its subsidiaries. All Rights Reserved
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
The arg spec for the sonic_vlan_mapping module
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class Vlan_mappingArgs(object):  # pylint: disable=R0903
    """The arg spec for the sonic_vlan_mapping module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        'config': {
            'elements': 'dict',
            'options': {
                'mapping': {
                    'elements': 'dict',
                    'options': {
                        'dot1q_tunnel': {'type': 'bool', 'default': False},
                        'inner_vlan': {'type': 'int'},
                        'priority': {'type': 'int'},
                        'service_vlan': {'required': True, 'type': 'int'},
                        'vlan_ids': {'elements': 'str', 'type': 'list'}
                    },
                    'type': 'list'
                },
                'name': {'required': True, 'type': 'str'}
            },
            'type': 'list'
        },
        'state': {
            'choices': ['merged', 'deleted', 'replaced', 'overridden'],
            'default': 'merged',
            'type': 'str'
        }
    }  # pylint: disable=C0301
