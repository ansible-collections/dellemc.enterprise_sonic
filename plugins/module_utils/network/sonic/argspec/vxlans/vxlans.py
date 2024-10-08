#
# -*- coding: utf-8 -*-
# © Copyright 2024 Dell Inc. or its subsidiaries. All Rights Reserved
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
The arg spec for the sonic_vxlans module
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class VxlansArgs(object):  # pylint: disable=R0903
    """The arg spec for the sonic_vxlans module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        'config': {
            'elements': 'dict',
            'options': {
                'evpn_nvo': {'type': 'str'},
                'name': {'required': True, 'type': 'str'},
                'source_ip': {'type': 'str'},
                'primary_ip': {'type': 'str'},
                'external_ip': {'type': 'str'},
                'vlan_map': {
                    'elements': 'dict',
                    'options': {
                        'vlan': {'type': 'int'},
                        'vni': {'required': True, 'type': 'int'}
                    },
                    'type': 'list'
                },
                'vrf_map': {
                    'elements': 'dict',
                    'options': {
                        'vni': {'required': True, 'type': 'int'},
                        'vrf': {'type': 'str'}
                    },
                    'type': 'list'
                },
                'suppress_vlan_neigh': {
                    'elements': 'dict',
                    'options': {
                        'vlan_name': {'type': 'str'},
                    },
                    'type': 'list'
                }
            },
            'type': 'list'
        },
        'state': {
            'choices': ['merged', 'deleted', 'replaced', 'overridden'],
            'default': 'merged',
            'type': 'str'
        }
    }  # pylint: disable=C0301
