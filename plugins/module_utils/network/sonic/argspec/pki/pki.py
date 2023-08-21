#
# -*- coding: utf-8 -*-
# Copyright 2022 Dell EMC
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
The arg spec for the sonic_pki module
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class PkiArgs(object):  # pylint: disable=R0903
    """The arg spec for the sonic_pki module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        'config': {
            'options': {
                'security_profiles': {
                    'elements': 'dict',
                    'options': {
                        'cdp_list': {'elements': 'str', 'type': 'list'},
                        'certificate_name': {'type': 'str'},
                        'key_usage_check': {'type': 'bool'},
                        'ocsp_responder_list': {
                            'elements': 'str',
                            'type': 'list'
                            },
                        'peer_name_check': {'type': 'bool'},
                        'profile_name': {'required': True, 'type': 'str'},
                        'revocation_check': {'type': 'bool'},
                        'trust_store': {'type': 'str'}
                        },
                    'type': 'list'
                },
                'trust_stores': {
                    'elements': 'dict',
                    'options': {
                        'ca_name': {'elements': 'str', 'type': 'list'},
                        'name': {'required': True, 'type': 'str'}
                    },
                    'type': 'list'
                }
            },
            'type': 'dict'
        },
        'state': {
            'choices': ['merged', 'deleted', 'replaced', 'overridden'],
            'default': 'merged',
            'type': 'str'
        }
    }  # pylint: disable=C0301
