#
# -*- coding: utf-8 -*-
# Copyright 2023 Dell Inc. or its subsidiaries. All Rights Reserved
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
The arg spec for the sonic_bgp_communities module
"""
from __future__ import absolute_import, division, print_function
__metaclass__ = type


class Bgp_communitiesArgs(object):  # pylint: disable=R0903
    """The arg spec for the sonic_bgp_communities module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "config": {
            "elements": "dict",
            "options": {
                "local_as": {"type": "bool"},
                "match": {
                    "choices": ["ALL", "ANY"],
                    "type": "str"
                },
                "members": {
                    "options": {
                        "aann": {"elements": "str", "type": "list"},
                        "regex": {"elements": "str", "type": "list"}
                    },
                    "type": "dict"
                },
                "name": {"required": True, "type": "str"},
                "no_advertise": {"type": "bool"},
                "no_export": {"type": "bool"},
                "no_peer": {"type": "bool"},
                "permit": {"type": "bool"},
                "type": {
                    "choices": ["standard", "expanded"],
                    "type": "str"
                }
            },
            "type": "list"
        },
        "state": {
            "choices": ["merged", "deleted", "replaced", "overridden"],
            "default": "merged",
            "type": "str"
        }
    }  # pylint: disable=C0301
