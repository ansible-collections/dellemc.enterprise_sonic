#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
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
The arg spec for the sonic_bgp_neighbors_af module
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class Bgp_neighbors_afArgs(object):  # pylint: disable=R0903
    """The arg spec for the sonic_bgp_neighbors_af module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        'config': {
            'elements': 'dict',
            'options': {
                'bgp_as': {'required': True, 'type': 'str'},
                'neighbors': {
                    'elements': 'dict',
                    'options': {
                        'address_family': {
                            'elements': 'dict',
                            'options': {
                                'activate': {'type': 'bool'},
                                'afi': {
                                    'choices': ['ipv4', 'ipv6', 'l2vpn'],
                                    'required': True,
                                    'type': 'str'
                                },
                                'allowas_in': {
                                    'mutually_exclusive': [['origin', 'value']],
                                    'options': {
                                        'origin': {'type': 'bool'},
                                        'value': {'type': 'int'}
                                    },
                                    'type': 'dict'
                                },
                                'fabric_external': {'type': 'bool'},
                                'ip_afi': {
                                    'options': {
                                        'default_policy_name': {'type': 'str'},
                                        'send_default_route': {'default': False, 'type': 'bool'}
                                    },
                                    'type': 'dict'
                                },
                                'prefix_limit': {
                                    'options': {
                                        'max_prefixes': {'type': 'int'},
                                        'prevent_teardown': {'default': False, 'type': 'bool'},
                                        'warning_threshold': {'type': 'int'},
                                        'restart_timer': {'type': 'int'},
                                        'discard_extra': {'default': False, 'type': 'bool'}
                                    },
                                    'type': 'dict'
                                },
                                'prefix_list_in': {'type': 'str'},
                                'prefix_list_out': {'type': 'str'},
                                'route_map': {
                                    'elements': 'dict',
                                    'options': {
                                        'direction': {'type': 'str'},
                                        'name': {'type': 'str'}
                                    },
                                    'type': 'list'
                                },
                                'route_reflector_client': {'type': 'bool'},
                                'route_server_client': {'type': 'bool'},
                                'safi': {
                                    'choices': ['unicast', 'evpn'],
                                    'default': 'unicast',
                                    'type': 'str'
                                }
                            },
                            'required_together': [['afi', 'safi']],
                            'type': 'list'
                        },
                        'neighbor': {'required': True, 'type': 'str'}
                    },
                    'type': 'list'
                },
                'vrf_name': {'default': 'default', 'type': 'str'}
            },
            'type': 'list'
        },
        'state': {
            'choices': ['merged', 'deleted', 'replaced', 'overridden'],
            'default': 'merged'
        }
    }  # pylint: disable=C0301
