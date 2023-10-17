#
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


def poe_enum2str(enum_name):
    poe_enum_to_ui_str_map = {
        "FOUR_PT_DOT3AF": "4pt-dot3af",
        "FOUR_PT_DOT3AF_LEG": "4pt-dot3af+legacy",
        "TWO_PT_DOT3AF": "2pt-dot3af",
        "TWO_PT_DOT3AF_LEG": "2pt-dot3af+legacy",
        "DOT3BT_LEG": "dot3bt+legacy",
        "STATIC_PRI": "static-priority",
        "DYNAMIC_PRI": "dynamic-priority",
        "AC": "type-ac",
        "DC": "type-dc",
        "DOT3AF": "dot3af",
        "IEEE_8023AF": "dot3af",
        "HIGH_INRUSH": "high-inrush",
        "PRE_8023AT": "pre-dot3at",
        "IEEE_8023AT": "dot3at",
        "PRE_8023BT": "pre-dot3bt",
        "IEEE_8023BT_TYPE3": "dot3bt-type3",
        "IEEE_8023BT_TYPE4": "dot3bt-type4",
        "IEEE_8023BT": "dot3bt",
        "DELIVERING_POWER": "Delivering",
        "OTHER_FAULT": "other-fault",
        "REQUESTING_POWER": "requesting-power",
        "OVLO": "OVLO",
        "MPS_ABSENT": "MPS-absent",
        "POWER_DENIED": "power-denied",
        "THERMAL_SHUTDOWN": "thermal-shutdown",
        "STARTUP_FAILURE": "startup-failure",
        "UVLO": "UVLO",
        "NO_ERROR": "No Error",
        "HW_PIN_DISABLE": "HW Pin Disable",
        "PORT_UNDEFINED": "Port Undefined",
        "INTERNAL_HW_FAULT": "Internal HW Fault",
        "USER_SETTING": "User Setting",
        "NON_STANDARD_PD": "Non-standard PD",
        "UNDERLOAD": "Underload",
        "PWR_BUDGET_EXCEEDED": "PWR Budget Exceeded",
        "OOR_CAPACITOR_VALUE": "OOR Capacitor Value",
        "CLASS_ERROR": "Class Error",
        "RESET_PRIM_CHANNEL": "reset-primary-channel",
        "RESET_ALT_CHANNEL": "reset-alternative-channel",
        "HIGH_30W": "high-30W",
        "HIGH_45W": "high-40w",
        "TYPE_4_BT_90W": "type4-bt-90W",
        "TYPE_3_BT_60W": "type3-bt-60W",
        "TYPE_2_BT_30W": "type2-bt-30W",
        "TYPE_1_BT_15W": "type1-bt-15W",
        "TYPE_4_BT_90W_LEGACY_DETECT": "type4-bt-90W+legacy",
        "TYPE_3_BT_60W_LEGACY_DETECT": "type3-bt-60W+legacy",
        "TYPE_2_BT_30W_LEGACY_DETECT": "type2-bt-30W+legacy",
        "TYPE_1_BT_15W_LEGACY_DETECT": "type1-bt-15W+legacy",
        "DYNAMIC_PRIORITY": "dynamic-priority",
        "STATIC_PRIORITY": "static-priority",
        "USER": "user-defined",
        "CLASS_BASED": "class-based",
    }

    if enum_name in poe_enum_to_ui_str_map:
        return poe_enum_to_ui_str_map[enum_name]
    else:
        return enum_name.capitalize()
