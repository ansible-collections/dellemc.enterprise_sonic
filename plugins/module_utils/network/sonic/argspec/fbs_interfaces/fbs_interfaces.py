#
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The arg spec for the sonic_fbs_interfaces module
"""
from __future__ import absolute_import, division, print_function
__metaclass__ = type


class Fbs_interfacesArgs(object):  # pylint: disable=R0903
    """The arg spec for the sonic_fbs_interfaces module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        'config': {
            'elements': 'dict',
            'options': {
                'egress_policies': {
                    'options': {
                        'qos': {
                            'options': {
                                'policy_name': {'type': 'str'}
                            },
                            'type': 'dict'
                        }
                    },
                    'type': 'dict'
                },
                'ingress_policies': {
                    'options': {
                        'forwarding': {
                            'options': {
                                'policy_name': {'type': 'str'}
                            },
                            'type': 'dict'
                        },
                        'monitoring': {
                            'options': {
                                'policy_name': {'type': 'str'}
                            },
                            'type': 'dict'
                        },
                        'qos': {
                            'options': {
                                'policy_name': {'type': 'str'}
                            },
                            'type': 'dict'
                        }
                    },
                    'type': 'dict'
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
