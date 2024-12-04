#
# -*- coding: utf-8 -*-
# Copyright 2024 Dell Inc. or its subsidiaries. All Rights Reserved.
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
The arg spec for the sonic_fbs_classifiers module
"""
from __future__ import absolute_import, division, print_function
__metaclass__ = type


class Fbs_classifiersArgs(object):  # pylint: disable=R0903
    """The arg spec for the sonic_fbs_classifiers module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        'config': {
            'elements': 'dict',
            'mutually_exclusive': [['match_acl', 'match_hdr_fields']],
            'options': {
                'class_name': {'required': True, 'type': 'str'},
                'class_description': {'type': 'str'},
                'match_acl': {
                    'options': {
                        'acl_name': {'required': True, 'type': 'str'},
                        'acl_type': {'choices': ['ip', 'ipv6', 'mac'], 'required': True, 'type': 'str'}
                    },
                    'type': 'dict'
                },
                'match_hdr_fields': {
                    'mutually_exclusive': [['ipv4', 'ipv6']],
                    'options': {
                        'ip': {
                            'options': {
                                'dscp': {'type': 'int'},
                                'protocol': {
                                    'choices': ['auth', 'gre', 'icmp', 'icmpv6', 'igmp', 'l2tp', 'pim', 'rsvp', 'tcp', 'udp'],
                                    'type': 'str'
                                }
                            },
                            'type': 'dict'
                        },
                        'ipv4': {
                            'options': {
                                'destination_address': {'type': 'str'},
                                'source_address': {'type': 'str'}
                            },
                            'type': 'dict'
                        },
                        'ipv6': {
                            'options': {
                                'destination_address': {'type': 'str'},
                                'source_address': {'type': 'str'}
                            },
                            'type': 'dict'
                        },
                        'l2': {
                            'options': {
                                'dei': {'type': 'int'},
                                'destination_mac': {'type': 'str'},
                                'destination_mac_mask': {'type': 'str'},
                                'ethertype': {
                                    'choices': ['arp', 'ipv4', 'ipv6', 'lldp', 'mpls', 'roce', 'vlan'],
                                    'type': 'str'
                                },
                                'pcp': {'type': 'int'},
                                'source_mac': {'type': 'str'},
                                'source_mac_mask': {'type': 'str'},
                                'vlanid': {'type': 'int'}
                            },
                            'type': 'dict'
                        },
                        'transport': {
                            'options': {
                                'destination_port': {'type': 'str'},
                                'icmp_code': {'type': 'int'},
                                'icmp_type': {'type': 'int'},
                                'source_port': {'type': 'str'},
                                'tcp_flags': {
                                    'choices': ['ack', 'fin', 'psh', 'rst', 'syn', 'urg'],
                                    'elements': 'str',
                                    'type': 'list'
                                }
                            },
                            'type': 'dict'
                        }
                    },
                    'type': 'dict'
                },
                'match_type': {'choices': ['acl', 'fields'], 'type': 'str'}
            },
            'type': 'list'
        },
        'state': {
            'choices': ['merged', 'deleted', 'replaced', 'overridden'],
            'default': 'merged',
            'type': 'str'
        }
    }  # pylint: disable=C0301
