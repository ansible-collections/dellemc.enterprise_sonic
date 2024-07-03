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
The arg spec for the sonic_qos_interfaces module
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class Qos_interfacesArgs(object):  # pylint: disable=R0903
    """The arg spec for the sonic_qos_interfaces module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        'config': {
            'elements': 'dict',
            'options': {
                'name': {'required': True, 'type': 'str'},
                'pfc': {
                    'options': {
                        'asymmetric': {'type': 'bool', 'default': False},
                        'priorities': {
                            'elements': 'dict',
                            'options': {
                                'dot1p': {'required': True, 'type': 'int'},
                                'enable': {'type': 'bool', 'default': False}
                            },
                            'type': 'list'
                        },
                        'watchdog_action': {'choices': ['drop', 'forward', 'alert'], 'default': 'drop', 'type': 'str'},
                        'watchdog_detect_time': {'type': 'int'},
                        'watchdog_restore_time': {'type': 'int'}
                    },
                    'type': 'dict'
                },
                'qos_maps': {
                    'options': {
                        'dot1p_fwd_group': {'type': 'str'},
                        'dscp_fwd_group': {'type': 'str'},
                        'fwd_group_dot1p': {'type': 'str'},
                        'fwd_group_dscp': {'type': 'str'},
                        'fwd_group_pg': {'type': 'str'},
                        'fwd_group_queue': {'type': 'str'},
                        'pfc_priority_pg': {'type': 'str'},
                        'pfc_priority_queue': {'type': 'str'}
                    },
                    'type': 'dict'
                },
                'queues': {
                    'elements': 'dict',
                    'options': {
                        'id': {'required': True, 'type': 'int'},
                        'wred_profile': {'type': 'str'}
                    },
                    'type': 'list'
                },
                'scheduler_policy': {'type': 'str'}
            },
            'type': 'list'
        },
        'state': {'choices': ['merged', 'deleted'], 'default': 'merged', 'type': 'str'}
    }  # pylint: disable=C0301
