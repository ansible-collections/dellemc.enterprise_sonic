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
The arg spec for the sonic_bgp module
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class BgpArgs(object):  # pylint: disable=R0903
    """The arg spec for the sonic_bgp module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        'config': {
            'elements': 'dict',
            'options': {
                'bestpath': {
                    'options': {
                        'as_path': {
                            'options': {
                                'confed': {'type': 'bool'},
                                'ignore': {'type': 'bool'},
                                'multipath_relax': {'type': 'bool'},
                                'multipath_relax_as_set': {'type': 'bool'}
                            },
                            'type': 'dict'
                        },
                        'compare_routerid': {'type': 'bool'},
                        'med': {
                            'options': {
                                'confed': {'type': 'bool'},
                                'missing_as_worst': {'type': 'bool'},
                                'always_compare_med': {'type': 'bool'}
                            },
                            'type': 'dict'
                        }
                    },
                    'type': 'dict'
                },
                'bgp_as': {'required': True, 'type': 'str'},
                'log_neighbor_changes': {'type': 'bool'},
                'router_id': {'type': 'str'},
                "max_med": {
                  "options": {
                  "on_startup": {
                    "options": {
                      "timer": {"type":"int"},
                      "med_val": {"type":"int"}
                    },
                    "type":"dict"
                    }
                    },
                  "type":"dict"
                },
                'timers': {
                  'options': {
                    'holdtime': {'type': 'int'},
                    'keepalive_interval': {'type': 'int'}
                  },
                  'type': 'dict'
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
