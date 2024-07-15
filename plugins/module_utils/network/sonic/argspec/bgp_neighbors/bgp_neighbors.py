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
The arg spec for the sonic_bgp_neighbors module
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class Bgp_neighborsArgs(object):  # pylint: disable=R0903
    """The arg spec for the sonic_bgp_neighbors module
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
                        'neighbor': {'required': True, 'type': 'str'},
                        'remote_as': {
                            'mutually_exclusive': [['peer_type', 'peer_as']],
                            'options': {
                                'peer_type': {'type': 'str', 'choices': ['internal', 'external']},
                                'peer_as': {'type': 'str'},
                            },
                            'type': 'dict'
                        },
                        'peer_group': {'type': 'str'},
                        'bfd': {
                            'options': {
                                'enabled': {'type': 'bool'},
                                'check_failure': {'type': 'bool'},
                                'profile': {'type': 'str'}
                            },
                            'type': 'dict'
                        },
                        'advertisement_interval': {'type': 'int'},
                        'timers': {
                            'options': {
                                'holdtime': {'type': 'int'},
                                'keepalive': {'type': 'int'},
                                'connect_retry': {'type': 'int'}
                            },
                            'type': 'dict'
                        },
                        'capability': {
                            'options': {
                                'dynamic': {'type': 'bool'},
                                'extended_nexthop': {'type': 'bool'},
                            },
                            'type': 'dict'
                        },
                        'auth_pwd': {
                            'options': {
                                'pwd': {'required': True, 'type': 'str'},
                                'encrypted': {'default': 'False', 'type': 'bool'},
                            },
                            'type': 'dict'
                        },
                        'nbr_description': {'type': 'str'},
                        'disable_connected_check': {'type': 'bool'},
                        'dont_negotiate_capability': {'type': 'bool'},
                        'ebgp_multihop': {
                            'options': {
                                'enabled': {'default': 'False', 'type': 'bool'},
                                'multihop_ttl': {'type': 'int'}
                            },
                            'type': 'dict'
                        },
                        'enforce_first_as': {'type': 'bool'},
                        'enforce_multihop': {'type': 'bool'},
                        'local_address': {'type': 'str'},
                        'local_as': {
                            'options': {
                                'as': {'required': True, 'type': 'str'},
                                'no_prepend': {'type': 'bool'},
                                'replace_as': {'type': 'bool'},
                            },
                            'type': 'dict'
                        },
                        'override_capability': {'type': 'bool'},
                        'passive': {'default': 'False', 'type': 'bool'},
                        'port': {'type': 'int'},
                        'shutdown_msg': {'type': 'str'},
                        'solo': {'type': 'bool'},
                        'strict_capability_match': {'type': 'bool'},
                        'ttl_security': {'type': 'int'},
                        'v6only': {'type': 'bool'}
                    },
                    'type': 'list'
                },
                'peer_group': {
                    'elements': 'dict',
                    'options': {
                        'name': {'required': True, 'type': 'str'},
                        'remote_as': {
                            'mutually_exclusive': [['peer_type', 'peer_as']],
                            'options': {
                                'peer_type': {'type': 'str', 'choices': ['internal', 'external']},
                                'peer_as': {'type': 'str'},
                            },
                            'type': 'dict'
                        },
                        'address_family': {
                            'options': {
                                'afis': {
                                    'elements': 'dict',
                                    'options': {
                                        'activate': {'type': 'bool'},
                                        'afi': {
                                            'choices': ['ipv4', 'ipv6', 'l2vpn'],
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
                                                'restart_timer': {'type': 'int'}
                                            },
                                            'type': 'dict'
                                        },
                                        'prefix_list_in': {'type': 'str'},
                                        'prefix_list_out': {'type': 'str'},
                                        'safi': {
                                            'choices': ['unicast', 'evpn'],
                                            'type': 'str'
                                        },
                                    },
                                    'required_together': [['afi', 'safi']],
                                    'type': 'list'
                                },
                            },
                            'type': 'dict'
                        },
                        'bfd': {
                            'options': {
                                'enabled': {'type': 'bool'},
                                'check_failure': {'type': 'bool'},
                                'profile': {'type': 'str'}
                            },
                            'type': 'dict'
                        },
                        'advertisement_interval': {'type': 'int'},
                        'timers': {
                            'options': {
                                'holdtime': {'type': 'int'},
                                'keepalive': {'type': 'int'},
                                'connect_retry': {'type': 'int'}
                            },
                            'type': 'dict'
                        },
                        'capability': {
                            'options': {
                                'dynamic': {'type': 'bool'},
                                'extended_nexthop': {'type': 'bool'},
                            },
                            'type': 'dict'
                        },
                        'auth_pwd': {
                            'options': {
                                'pwd': {'required': True, 'type': 'str'},
                                'encrypted': {'default': 'False', 'type': 'bool'},
                            },
                            'type': 'dict'
                        },
                        'pg_description': {'type': 'str'},
                        'disable_connected_check': {'type': 'bool'},
                        'dont_negotiate_capability': {'type': 'bool'},
                        'ebgp_multihop': {
                            'options': {
                                'enabled': {'default': 'False', 'type': 'bool'},
                                'multihop_ttl': {'type': 'int'}
                            },
                            'type': 'dict'
                        },
                        'enforce_first_as': {'type': 'bool'},
                        'enforce_multihop': {'type': 'bool'},
                        'local_address': {'type': 'str'},
                        'local_as': {
                            'options': {
                                'as': {'required': True, 'type': 'str'},
                                'no_prepend': {'type': 'bool'},
                                'replace_as': {'type': 'bool'},
                            },
                            'type': 'dict'
                        },
                        'override_capability': {'type': 'bool'},
                        'passive': {'default': 'False', 'type': 'bool'},
                        'shutdown_msg': {'type': 'str'},
                        'solo': {'type': 'bool'},
                        'strict_capability_match': {'type': 'bool'},
                        'ttl_security': {'type': 'int'}
                    },
                    'type': 'list'
                },
                'vrf_name': {'default': 'default', 'type': 'str'}
            },
            'type': 'list'
        },
        'state': {
            'choices': ['merged', 'deleted'],
            'default': 'merged'
        }
    }  # pylint: disable=C0301
