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
The arg spec for the sonic_bfd module
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class BfdArgs(object):  # pylint: disable=R0903
    """The arg spec for the sonic_bfd module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        'config': {
            'options': {
                'multi_hops': {
                    'elements': 'dict',
                    'options': {
                        'detect_multiplier': {'default': 3, 'type': 'int'},
                        'enabled': {'default': True, 'type': 'bool'},
                        'local_address': {'required': True, 'type': 'str'},
                        'min_ttl': {'default': 254, 'type': 'int'},
                        'passive_mode': {'default': False, 'type': 'bool'},
                        'profile_name': {'type': 'str'},
                        'receive_interval': {'default': 300, 'type': 'int'},
                        'remote_address': {'required': True, 'type': 'str'},
                        'transmit_interval': {'default': 300, 'type': 'int'},
                        'vrf': {'required': True, 'type': 'str'}},
                    'type': 'list'},
                'profiles': {
                    'elements': 'dict',
                    'options': {
                        'detect_multiplier': {'default': 3, 'type': 'int'},
                        'echo_interval': {'default': 300, 'type': 'int'},
                        'echo_mode': {'default': False, 'type': 'bool'},
                        'enabled': {'default': True, 'type': 'bool'},
                        'min_ttl': {'default': 254, 'type': 'int'},
                        'passive_mode': {'default': False, 'type': 'bool'},
                        'profile_name': {'required': True, 'type': 'str'},
                        'receive_interval': {'default': 300, 'type': 'int'},
                        'transmit_interval': {'default': 300, 'type': 'int'}},
                    'type': 'list'},
                'single_hops': {
                    'elements': 'dict',
                    'options': {
                        'detect_multiplier': {'default': 3, 'type': 'int'},
                        'echo_interval': {'default': 300, 'type': 'int'},
                        'echo_mode': {'default': False, 'type': 'bool'},
                        'enabled': {'default': True, 'type': 'bool'},
                        'interface': {'required': True, 'type': 'str'},
                        'local_address': {'required': True, 'type': 'str'},
                        'passive_mode': {'default': False, 'type': 'bool'},
                        'profile_name': {'type': 'str'},
                        'receive_interval': {'default': 300, 'type': 'int'},
                        'remote_address': {'required': True, 'type': 'str'},
                        'transmit_interval': {'default': 300, 'type': 'int'},
                        'vrf': {'required': True, 'type': 'str'}},
                    'type': 'list'}
            },
            'type': 'dict'
        },
        'state': {'choices': ['merged', 'deleted', 'replaced', 'overridden'], 'default': 'merged', 'type': 'str'}
    }  # pylint: disable=C0301
