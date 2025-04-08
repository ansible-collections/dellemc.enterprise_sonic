#
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved
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
The arg spec for the sonic_br_l2pt module
"""


class Br_l2ptArgs(object):  # pylint: disable=R0903
    """The arg spec for the sonic_br_l2pt module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {'config': {'elements': 'dict',
            'options': {'name': {'required': True, 'type': 'str'},
                        'protocol': {'options': {'CDP': {'options': {'vlan_ids': {'elements': 'str',
                                                                                  'type': 'list'}},
                                                         'type': 'dict'},
                                                 'LACP': {'options': {'vlan_ids': {'elements': 'str',
                                                                                   'type': 'list'}},
                                                          'type': 'dict'},
                                                 'LLDP': {'options': {'vlan_ids': {'elements': 'str',
                                                                                   'type': 'list'}},
                                                          'type': 'dict'},
                                                 'STP': {'options': {'vlan_ids': {'elements': 'str',
                                                                                  'type': 'list'}},
                                                         'type': 'dict'}},
                                     'type': 'dict'}},
            'type': 'list'},
 'state': {'choices': ['merged', 'deleted', 'replaced', 'overridden'],
           'default': 'merged',
           'type': 'str'}}  # pylint: disable=C0301
