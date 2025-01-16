#
# -*- coding: utf-8 -*-
# © Copyright 2020 Dell Inc. or its subsidiaries. All Rights Reserved
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
The arg spec for the sonic_interfaces module
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class InterfacesArgs(object):  # pylint: disable=R0903
    """The arg spec for the sonic_interfaces module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "config": {
            "elements": "dict",
            "options": {
                "description": {"type": "str"},
                "enabled": {"type": "bool"},
                "mtu": {"type": "int"},
                "name": {"required": True, "type": "str"},
                "speed": {"type": "str",
                          "choices": ["SPEED_10MB",
                                      "SPEED_100MB",
                                      "SPEED_1GB",
                                      "SPEED_2500MB",
                                      "SPEED_5GB",
                                      "SPEED_10GB",
                                      "SPEED_20GB",
                                      "SPEED_25GB",
                                      "SPEED_40GB",
                                      "SPEED_50GB",
                                      "SPEED_100GB",
                                      "SPEED_200GB",                                     
                                      "SPEED_400GB"]},
                "auto_negotiate": {"type": "bool"},
                "advertised_speed": {"type": "list", "elements": "str"},
                "fec": {"type": "str",
                        "choices": ["FEC_RS",
                                    "FEC_FC",
                                    "FEC_DISABLED",
                                    "FEC_DEFAULT",
                                    "FEC_AUTO"]},
                "unreliable_los": {"type": "str",
                                   "choices": ["UNRELIABLE_LOS_MODE_ON",
                                               "UNRELIABLE_LOS_MODE_OFF",
                                               "UNRELIABLE_LOS_MODE_AUTO"]}
            },
            "type": "list"
        },
        "state": {
            "choices": ["merged", "replaced", "overridden", "deleted"],
            "default": "merged",
            "type": "str"
        }
    }
