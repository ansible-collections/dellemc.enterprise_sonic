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
The arg spec for the sonic_logging module
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class LoggingArgs(object):  # pylint: disable=R0903
    """The arg spec for the sonic_logging module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        'config': {
            'options': {
                'remote_servers': {
                    'elements': 'dict',
                    'options': {
                        'host': {'required': True,
                                 'type': 'str'},
                        'message_type': {'choices': ['log', 'event', 'audit', 'auditd-system'],
                                         'type': 'str'},
                        'remote_port': {'type': 'int'},
                        'source_interface': {'type': 'str'},
                        'vrf': {'type': 'str'},
                        'protocol': {'choices': ['TCP', 'UDP', 'TLS'],
                                     'type': 'str'},
                    },
                    'type': 'list'
                }
            },
            'type': 'dict'
        },
        'state': {
            'choices': ['merged', "replaced", "overridden", 'deleted'],
            'default': 'merged',
            'type': 'str'
        }
    }  # pylint: disable=C0301
