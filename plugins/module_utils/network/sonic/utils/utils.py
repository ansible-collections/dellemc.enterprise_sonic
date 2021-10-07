#
# -*- coding: utf-8 -*-
# Copyright 2020 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# utils

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import socket
import re
import json
from ansible.module_utils.six import iteritems
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    is_masklen,
    to_netmask,
    remove_empties
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible.module_utils.connection import ConnectionError

DEFAULT_TEST_KEY = {'config': {'name': ''}}
GET = 'get'

intf_naming_mode = ""


def get_diff(base_data, compare_with_data, test_keys=None, is_skeleton=None):
    diff = []
    if is_skeleton is None:
        is_skeleton = False

    test_keys = normalize_testkeys(test_keys)

    if isinstance(base_data, list) and isinstance(compare_with_data, list):
        dict_diff = get_diff_dict({"config": base_data}, {"config": compare_with_data}, test_keys, is_skeleton)
        diff = dict_diff.get("config", [])

    else:
        new_base, new_compare = convert_dict_to_single_entry_list(base_data, compare_with_data, test_keys)
        diff = get_diff_dict(new_base, new_compare, test_keys, is_skeleton)
        if diff:
            diff = convert_single_entry_list_to_dict(diff)
        else:
            diff = {}

    return diff


def get_diff_dict(base_data, compare_with_data, test_keys=None, is_skeleton=None):
    if is_skeleton is None:
        is_skeleton = False

    if test_keys is None:
        test_keys = []

    if not base_data:
        return base_data

    planned_set = set(base_data.keys())
    discovered_set = set(compare_with_data.keys())
    intersect_set = planned_set.intersection(discovered_set)
    changed_dict = {}
    has_dict_item = None
    added_set = planned_set - intersect_set
    # Keys part of added are new and put into changed_dict
    if added_set:
        for key in added_set:
            if is_skeleton:
                changed_dict[key] = base_data[key]
            elif base_data[key] is not None:
                if isinstance(base_data[key], dict):
                    val_dict = remove_empties(base_data[key])
                    if val_dict:
                        changed_dict[key] = remove_empties(base_data[key])
                elif isinstance(base_data[key], list):
                    val_list = remove_empties_from_list(base_data[key])
                    if val_list:
                        changed_dict[key] = remove_empties_from_list(base_data[key])
                else:
                    changed_dict[key] = base_data[key]
    for key in intersect_set:
        has_dict_item = False
        value = base_data[key]
        if isinstance(value, list):
            p_list = base_data[key] if key in base_data else []
            d_list = compare_with_data[key] if key in compare_with_data else []
            keys_to_compare = next((test_key_item[key] for test_key_item in test_keys if key in test_key_item), None)
            changed_list = []
            if p_list and d_list:
                for p_list_item in p_list:
                    matched = False
                    has_diff = False
                    for d_list_item in d_list:
                        if (isinstance(p_list_item, dict) and isinstance(d_list_item, dict)):
                            if keys_to_compare:
                                key_matched_cnt = 0
                                test_keys_present_cnt = 0
                                common_keys = set(p_list_item).intersection(d_list_item)
                                for test_key in keys_to_compare:
                                    if test_key in common_keys:
                                        test_keys_present_cnt += 1
                                        if p_list_item[test_key] == d_list_item[test_key]:
                                            key_matched_cnt += 1
                                if key_matched_cnt and key_matched_cnt == test_keys_present_cnt:
                                    remaining_keys = [test_key_item for test_key_item in test_keys if key not in test_key_item]
                                    dict_diff = get_diff_dict(p_list_item, d_list_item, remaining_keys, is_skeleton)
                                    matched = True
                                    if dict_diff:
                                        has_diff = True
                                        for test_key in keys_to_compare:
                                            dict_diff.update({test_key: p_list_item[test_key]})
                                    break
                            else:
                                dict_diff = get_diff_dict(p_list_item, d_list_item, test_keys, is_skeleton)
                                if not dict_diff:
                                    matched = True
                                    break
                        else:
                            if p_list_item == d_list_item:
                                matched = True
                                break
                    if not matched:
                        if is_skeleton:
                            changed_list.append(p_list_item)
                        else:
                            if isinstance(p_list_item, dict):
                                val_dict = remove_empties(p_list_item)
                                if val_dict is not None:
                                    changed_list.append(val_dict)
                            elif isinstance(p_list_item, list):
                                val_list = remove_empties_from_list(p_list_item)
                                if val_list is not None:
                                    changed_list.append(val_list)
                            else:
                                if p_list_item is not None:
                                    changed_list.append(p_list_item)
                    elif has_diff and dict_diff:
                        changed_list.append(dict_diff)
                if changed_list:
                    changed_dict.update({key: changed_list})
            elif p_list and (not d_list):
                changed_dict[key] = p_list
        elif (isinstance(value, dict) and isinstance(compare_with_data[key], dict)):
            dict_diff = get_diff_dict(base_data[key], compare_with_data[key], test_keys, is_skeleton)
            if dict_diff:
                changed_dict[key] = dict_diff
        elif value is not None:
            if not is_skeleton:
                if compare_with_data[key] != base_data[key]:
                    changed_dict[key] = base_data[key]
    return changed_dict


def convert_dict_to_single_entry_list(base_data, compare_with_data, test_keys):
    # if it is dict comparision convert dict into single entry list by adding 'config' as key
    new_base = {'config': [base_data]}
    new_compare = {'config': [compare_with_data]}

    # get testkey of 'config'
    config_testkey = None
    for item in test_keys:
        for key, val in item.items():
            if key == 'config':
                config_testkey = list(val)[0]
                break
        if config_testkey:
            break
    # if testkey of 'config' is not in base data, introduce single entry list
    # with 'temp_key' as config testkey and base_data as data.
    if config_testkey and base_data and config_testkey not in base_data:
        new_base = {'config': [{config_testkey: 'temp_key', 'data': base_data}]}
        new_compare = {'config': [{config_testkey: 'temp_key', 'data': compare_with_data}]}

    return new_base, new_compare


def convert_single_entry_list_to_dict(diff):
    diff = diff['config'][0]
    if 'data' in diff:
        diff = diff['data']
    return diff


def normalize_testkeys(test_keys):
    if test_keys is None:
        test_keys = []

    if not any(test_key_item for test_key_item in test_keys if "config" in test_key_item):
        test_keys.append(DEFAULT_TEST_KEY)

    return test_keys


def update_states(commands, state):
    ret_list = list()
    if commands:
        if isinstance(commands, list):
            for command in commands:
                ret = command.copy()
                ret.update({"state": state})
                ret_list.append(ret)
        elif isinstance(commands, dict):
            ret_list.append(commands.copy())
            ret_list[0].update({"state": state})
    return ret_list


def dict_to_set(sample_dict):
    # Generate a set with passed dictionary for comparison
    test_dict = dict()
    if isinstance(sample_dict, dict):
        for k, v in iteritems(sample_dict):
            if v is not None:
                if isinstance(v, list):
                    if isinstance(v[0], dict):
                        li = []
                        for each in v:
                            for key, value in iteritems(each):
                                if isinstance(value, list):
                                    each[key] = tuple(value)
                            li.append(tuple(iteritems(each)))
                        v = tuple(li)
                    else:
                        v = tuple(v)
                elif isinstance(v, dict):
                    li = []
                    for key, value in iteritems(v):
                        if isinstance(value, list):
                            v[key] = tuple(value)
                    li.extend(tuple(iteritems(v)))
                    v = tuple(li)
                test_dict.update({k: v})
        return_set = set(tuple(iteritems(test_dict)))
    else:
        return_set = set(sample_dict)
    return return_set


def validate_ipv4(value, module):
    if value:
        address = value.split("/")
        if len(address) != 2:
            module.fail_json(
                msg="address format is <ipv4 address>/<mask>, got invalid format {0}".format(
                    value
                )
            )

        if not is_masklen(address[1]):
            module.fail_json(
                msg="invalid value for mask: {0}, mask should be in range 0-32".format(
                    address[1]
                )
            )


def validate_ipv6(value, module):
    if value:
        address = value.split("/")
        if len(address) != 2:
            module.fail_json(
                msg="address format is <ipv6 address>/<mask>, got invalid format {0}".format(
                    value
                )
            )
        else:
            if not 0 <= int(address[1]) <= 128:
                module.fail_json(
                    msg="invalid value for mask: {0}, mask should be in range 0-128".format(
                        address[1]
                    )
                )


def validate_n_expand_ipv4(module, want):
    # Check if input IPV4 is valid IP and expand IPV4 with its subnet mask
    ip_addr_want = want.get("address")
    if len(ip_addr_want.split(" ")) > 1:
        return ip_addr_want
    validate_ipv4(ip_addr_want, module)
    ip = ip_addr_want.split("/")
    if len(ip) == 2:
        ip_addr_want = "{0} {1}".format(ip[0], to_netmask(ip[1]))

    return ip_addr_want


def netmask_to_cidr(netmask):
    bit_range = [128, 64, 32, 16, 8, 4, 2, 1]
    count = 0
    cidr = 0
    netmask_list = netmask.split(".")
    netmask_calc = [i for i in netmask_list if int(i) != 255 and int(i) != 0]
    if netmask_calc:
        netmask_calc_index = netmask_list.index(netmask_calc[0])
    elif sum(list(map(int, netmask_list))) == 0:
        return "32"
    else:
        return "24"
    for each in bit_range:
        if cidr == int(netmask.split(".")[2]):
            if netmask_calc_index == 1:
                return str(8 + count)
            elif netmask_calc_index == 2:
                return str(8 * 2 + count)
            elif netmask_calc_index == 3:
                return str(8 * 3 + count)
            break
        cidr += each
        count += 1


def remove_empties_from_list(config_list):
    ret_config = []
    if not config_list:
        return ret_config
    for config in config_list:
        ret_config.append(remove_empties(config))
    return ret_config


def get_device_interface_naming_mode(module):
    intf_naming_mode = ""
    request = {"path": "data/sonic-device-metadata:sonic-device-metadata/DEVICE_METADATA/DEVICE_METADATA_LIST=localhost", "method": GET}
    try:
        response = edit_config(module, to_request(module, request))
    except ConnectionError as exc:
        module.fail_json(msg=str(exc), code=exc.code)

    if 'sonic-device-metadata:DEVICE_METADATA_LIST' in response[0][1]:
        device_meta_data = response[0][1].get('sonic-device-metadata:DEVICE_METADATA_LIST', [])
        if device_meta_data:
            intf_naming_mode = device_meta_data[0].get('intf_naming_mode', 'native')

    return intf_naming_mode


STANDARD_ETH_REGEXP = r"[e|E]th\s*\d+/\d+"
NATIVE_ETH_REGEXP = r"[e|E]th*\d+$"
NATIVE_MODE = "native"
STANDARD_MODE = "standard"


def find_intf_naming_mode(intf_name):
    ret_intf_naming_mode = NATIVE_MODE

    if re.search(STANDARD_ETH_REGEXP, intf_name):
        ret_intf_naming_mode = STANDARD_MODE

    return ret_intf_naming_mode


def validate_intf_naming_mode(intf_name, module):
    global intf_naming_mode
    if intf_naming_mode == "":
        intf_naming_mode = get_device_interface_naming_mode(module)

    if intf_naming_mode != "":
        ansible_intf_naming_mode = find_intf_naming_mode(intf_name)
        if intf_naming_mode != ansible_intf_naming_mode:
            err = "Interface naming mode configured on switch {naming_mode}, {intf_name} is not valid".format(naming_mode=intf_naming_mode, intf_name=intf_name)
            module.fail_json(msg=err, code=400)


def normalize_interface_name(configs, module, namekey=None):
    if not namekey:
        namekey = 'name'

    if configs:
        for conf in configs:
            if conf.get(namekey, None):
                conf[namekey] = get_normalize_interface_name(conf[namekey], module)


def get_normalize_interface_name(intf_name, module):
    change_flag = False
    # remove the space in the given string
    ret_intf_name = re.sub(r"\s+", "", intf_name, flags=re.UNICODE)
    ret_intf_name = ret_intf_name.capitalize()

    # serach the numeric charecter(digit)
    match = re.search(r"\d", ret_intf_name)
    if match:
        change_flag = True
        start_pos = match.start()
        name = ret_intf_name[0:start_pos]
        intf_id = ret_intf_name[start_pos:]

        # Interface naming mode affects only ethernet ports
        if name.startswith("Eth"):
            validate_intf_naming_mode(intf_name, module)

        if ret_intf_name.startswith("Management") or ret_intf_name.startswith("Mgmt"):
            name = "eth"
            intf_id = "0"
        elif re.search(STANDARD_ETH_REGEXP, ret_intf_name):
            name = "Eth"
        elif re.search(NATIVE_ETH_REGEXP, ret_intf_name):
            name = "Ethernet"
        elif name.startswith("Po"):
            name = "PortChannel"
        elif name.startswith("Vlan"):
            name = "Vlan"
        elif name.startswith("Lo"):
            name = "Loopback"
        else:
            change_flag = False

        ret_intf_name = name + intf_id

    if not change_flag:
        ret_intf_name = intf_name

    return ret_intf_name


def get_speed_from_breakout_mode(breakout_mode):
    speed = None
    speed_breakout_mode_map = {
        "4x10G": "SPEED_10GB", "1x100G": "SPEED_100GB", "1x40G": "SPEED_40GB", "4x25G": "SPEED_25GB", "2x50G": "SPEED_50GB",
        "1x400G": "SPEED_400GB", "4x100G": "SPEED_100GB", "4x50G": "SPEED_50GB", "2x100G": "SPEED_100GB", "2x200G": "SPEED_200GB"
    }
    if breakout_mode in speed_breakout_mode_map:
        speed = speed_breakout_mode_map[breakout_mode]
    return speed


def get_breakout_mode(module, name):
    response = None
    mode = None
    component_name = name
    if "/" in name:
        component_name = name.replace("/", "%2f")
    url = "data/openconfig-platform:components/component=%s" % (component_name)
    request = [{"path": url, "method": GET}]
    try:
        response = edit_config(module, to_request(module, request))
    except ConnectionError as exc:
        try:
            json_obj = json.loads(str(exc).replace("'", '"'))
            if json_obj and type(json_obj) is dict and 404 == json_obj['code']:
                response = None
            else:
                module.fail_json(msg=str(exc), code=exc.code)
        except Exception as err:
            module.fail_json(msg=str(exc), code=exc.code)

    if response and "openconfig-platform:component" in response[0][1]:
        raw_port_breakout = response[0][1]['openconfig-platform:component'][0]
        port_name = raw_port_breakout.get('name', None)
        port_data = raw_port_breakout.get('port', None)
        if port_name and port_data and 'openconfig-platform-port:breakout-mode' in port_data:
            if 'config' in port_data['openconfig-platform-port:breakout-mode']:
                cfg = port_data['openconfig-platform-port:breakout-mode']['config']
                channel_speed = cfg.get('channel-speed', None)
                num_channels = cfg.get('num-channels', None)
                if channel_speed and num_channels:
                    speed = channel_speed.replace('openconfig-if-ethernet:SPEED_', '')
                    speed = speed.replace('GB', 'G')
                    mode = str(num_channels) + 'x' + speed
    return mode
