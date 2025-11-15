#
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The arg spec for the sonic_roce module
"""
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class RoceArgs(object):  # pylint: disable=R0903
    """The arg spec for the sonic_roce module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        'config': {
            'options': {
                'pfc_priority': {'type': 'str'},
                'roce_enable': {'type': 'bool'}
            },
            'type': 'dict'
        },
        'state': {
            'choices': ['merged'], 'default': 'merged', 'type': 'str'
        }
    }  # pylint: disable=C0301
