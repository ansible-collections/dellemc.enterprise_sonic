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
The arg spec for the sonic_l2_acls module
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class L2_aclsArgs(object):  # pylint: disable=R0903
    """The arg spec for the sonic_l2_acls module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        'config': {
            'elements': 'dict',
            'options': {
                'name': {'required': True, 'type': 'str'},
                'remark': {'type': 'str'},
                'rules': {
                    'elements': 'dict',
                    'mutually_exclusive': [['ethertype', 'vlan_tag_format']],
                    'options': {
                        'action': {
                            'choices': ['deny', 'discard', 'do-not-nat', 'permit', 'transit'],
                            'type': 'str'
                        },
                        'dei': {
                            'choices': [0, 1],
                            'type': 'int'
                        },
                        'destination': {
                            'mutually_exclusive': [['any', 'host', 'address']],
                            'options': {
                                'address': {'type': 'str'},
                                'address_mask': {'type': 'str'},
                                'any': {'type': 'bool'},
                                'host': {'type': 'str'}
                            },
                            'required_one_of': [['any', 'host', 'address']],
                            'required_together': [['address', 'address_mask']],
                            'type': 'dict'
                        },
                        'ethertype': {
                            'mutually_exclusive': [['value', 'arp', 'ipv4', 'ipv6']],
                            'options': {
                                'arp': {'type': 'bool'},
                                'ipv4': {'type': 'bool'},
                                'ipv6': {'type': 'bool'},
                                'value': {'type': 'str'}
                            },
                            'type': 'dict'
                        },
                        'pcp': {
                            'mutually_exclusive': [
                                ['value', 'traffic_type'],
                                ['mask', 'traffic_type']
                            ],
                            'options': {
                                'mask': {'type': 'int'},
                                'traffic_type': {
                                    'choices': ['be', 'bk', 'ee', 'ca', 'vi', 'vo', 'ic', 'nc'],
                                    'type': 'str'
                                },
                                'value': {'type': 'int'}
                            },
                            'required_by': {'mask': ['value']},
                            'type': 'dict'
                        },
                        'remark': {'type': 'str'},
                        'sequence_num': {'required': True, 'type': 'int'},
                        'source': {
                            'mutually_exclusive': [['any', 'host', 'address']],
                            'options': {
                                'address': {'type': 'str'},
                                'address_mask': {'type': 'str'},
                                'any': {'type': 'bool'},
                                'host': {'type': 'str'}
                            },
                            'required_one_of': [['any', 'host', 'address']],
                            'required_together': [['address', 'address_mask']],
                            'type': 'dict'
                        },
                        'vlan_id': {'type': 'int'},
                        'vlan_tag_format': {
                            'options': {
                                'multi_tagged': {'type': 'bool'}
                            },
                            'type': 'dict'
                        }
                    },
                    'required_together': [['action', 'source', 'destination']],
                    'type': 'list'
                }
            },
            'type': 'list'
        },
        'state': {
            'choices': ['merged', 'replaced', 'overridden', 'deleted'],
            'default': 'merged',
            'type': 'str'
        }
    }  # pylint: disable=C0301
