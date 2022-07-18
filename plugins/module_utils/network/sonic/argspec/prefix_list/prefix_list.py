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
The arg spec for the sonic_prefix_list module
"""


class Prefix_listArgs(object):  # pylint: disable=R0903
    """The arg spec for the sonic_prefix_list module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {'config': {
                         'elements': 'dict',
                         'options': {
                             'afi': {
                                 'choices': ['ipv4', 'ipv6'],
                                 'default': 'ipv4',
                                 'type': 'str'
                             },
                             'name': {'required': True, 'type': 'str'},
                             'prefixes': {
                                 'elements': 'dict',
                                 'options': {
                                     'action': {
                                         'choices': ['permit', 'deny'],
                                         'required': True,
                                         'type': 'str'
                                     },
                                     'ge': {'type': 'int'},
                                     'le': {'type': 'int'},
                                     'prefix': {'required': True, 'type': 'str'},
                                     'sequence': {'required': True, 'type': 'int'}},
                                     'type': 'list'
                                 }
                             },
                             'type': 'list'
                         },
                     'state': {
                         'choices': ['merged', 'deleted'],
                         'default': 'merged',
                         'type': 'str'
                     }
                 }  # pylint: disable=C0301
