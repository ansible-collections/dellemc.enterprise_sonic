#
# -*- coding: utf-8 -*-
# Copyright 2022 Dell Inc. or its subsidiaries. All Rights Reserved
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
The arg spec for the sonic_lldp_interfaces module
"""
from __future__ import absolute_import, division, print_function
__metaclass__ = type


class Lldp_interfacesArgs(object):  # pylint: disable=R0903
    """The arg spec for the sonic_lldp_interfaces module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        'config': {
            'elements': 'dict',
            'options': {
                'name': {
                    'required': True,
                    'type': 'str'
                },
                'enable': {
                    'type': 'bool'
                },
                'med_tlv_select': {
                    'options': {
                        'network_policy': {
                            'type': 'bool'
                        },
                        'power_management': {
                            'type': 'bool'
                        }
                    },
                    'type': 'dict'
                },
                'mode': {
                    'choices': ['receive', 'transmit'],
                    'type': 'str'
                },
                'tlv_select': {
                    'options': {
                        'power_management': {
                            'type': 'bool'
                        }
                    },
                    'type': 'dict'
                },
                'tlv_set': {
                    'options': {
                        'ipv4_management_address': {
                            'type': 'str'
                        },
                        'ipv6_management_address': {
                            'type': 'str'
                        }
                    },
                    'type': 'dict'
                }
            },
            'type': 'list'
        },
        'state': {
            'choices': ['merged', 'deleted', 'overridden','replaced'],
            'default': 'merged',
            'type': 'str'
        }
    }  # pylint: disable=C0301
