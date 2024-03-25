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
The arg spec for the sonic_sflow module
"""
from __future__ import absolute_import, division, print_function
__metaclass__ = type


class SflowArgs(object):  # pylint: disable=R0903
    """The arg spec for the sonic_sflow module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        'config': {
            'options': {
                'agent': {'type': 'str'},
                'collectors': {
                    'elements': 'dict',
                    'options': {
                        'address': {'required': True, 'type': 'str'},
                        'network_instance': {'default': 'default', 'type': 'str'},
                        'port': {'default': 6343, 'type': 'int'}
                    },
                    'type': 'list'
                },
                'enabled': {'type': 'bool'},
                'interfaces': {
                    'elements': 'dict',
                    'options': {
                        'enabled': {'type': 'bool'},
                        'name': {'required': True, 'type': 'str'},
                        'sampling_rate': {'type': 'int'}
                    },
                    'type': 'list'
                },
                'polling_interval': {'type': 'int'},
                "sampling_rate": {'type': 'int'}
            },
            'type': 'dict'
        },
        'state': {
            'choices': ['merged', 'replaced', 'overridden', 'deleted'],
            'default': 'merged',
            'type': 'str'
        }
    }  # pylint: disable=C0301
