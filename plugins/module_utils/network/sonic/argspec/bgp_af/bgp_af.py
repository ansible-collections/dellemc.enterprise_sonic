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
The arg spec for the sonic_bgp_af module
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class Bgp_afArgs(object):  # pylint: disable=R0903
    """The arg spec for the sonic_bgp_af module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        'config': {
            'elements': 'dict',
            'options': {
                'address_family': {
                    'options': {
                        'afis': {
                            'elements': 'dict',
                            'options': {
                                'advertise_pip': {'type': 'bool'},
                                'advertise_pip_ip': {'type': 'str'},
                                'advertise_pip_peer_ip': {'type': 'str'},
                                'advertise_svi_ip': {'type': 'bool'},
                                'advertise_all_vni': {'type': 'bool'},
                                'advertise_default_gw': {'type': 'bool'},
                                'afi': {
                                    'choices': ['ipv4', 'ipv6', 'l2vpn'],
                                    'required': True,
                                    'type': 'str'
                                },
                                'max_path': {
                                    'options': {
                                        'ebgp': {'type': 'int'},
                                        'ibgp': {'type': 'int'}
                                    },
                                    'type': 'dict'
                                },
                                'network': {'type': 'list', 'elements': 'str'},
                                'dampening': {'type': 'bool'},
                                'redistribute': {
                                    'elements': 'dict',
                                    'options': {
                                        'metric': {'type': 'str'},
                                        'protocol': {
                                            'choices': ['ospf', 'static', 'connected'],
                                            'required': True,
                                            'type': 'str'
                                        },
                                        'route_map': {'type': 'str'}
                                    },
                                    'type': 'list'
                                },
                                'safi': {
                                    'choices': ['unicast', 'evpn'],
                                    'default': 'unicast',
                                    'type': 'str'
                                }
                            },
                            'required_together': [['afi', 'safi']],
                            'type': 'list'
                        }
                    },
                    'type': 'dict'
                },
                'bgp_as': {'required': True, 'type': 'str'},
                'vrf_name': {'default': 'default', 'type': 'str'}
            },
            'type': 'list'
        },
        'state': {
            'choices': ['merged', 'deleted'],
            'default': 'merged'
        }
    }  # pylint: disable=C0301
