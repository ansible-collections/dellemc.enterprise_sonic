#
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import traceback
import json
import re

from ansible.module_utils._text import to_native
from ansible.module_utils.connection import ConnectionError

try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote

try:
    import jinja2
    HAS_LIB = True
except Exception as e:
    HAS_LIB = False
    ERR_MSG = to_native(e)
    LIB_IMP_ERR = traceback.format_exc()

from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)

intf_speed_map = {
    0: 'SPEED_DEFAULT',
    10: "SPEED_10MB",
    100: "SPEED_100MB",
    1000: "SPEED_1GB",
    2500: "SPEED_2500MB",
    5000: "SPEED_5GB",
    10000: "SPEED_10GB",
    20000: "SPEED_20GB",
    25000: "SPEED_25GB",
    40000: "SPEED_40GB",
    50000: "SPEED_50GB",
    100000: "SPEED_100GB",
    200000: "SPEED_200GB",
    400000: "SPEED_400GB",
    800000: "SPEED_800GB"
}

intf_speed_to_number_map = {
    "SPEED_DEFAULT": 0,
    "SPEED_10MB": 10,
    "SPEED_100MB": 100,
    "SPEED_1GB": 1000,
    "SPEED_2500MB": 2500,
    "SPEED_5GB": 5000,
    "SPEED_10GB": 10000,
    "SPEED_20GB": 20000,
    "SPEED_25GB": 25000,
    "SPEED_40GB": 40000,
    "SPEED_50GB": 50000,
    "SPEED_100GB": 100000,
    "SPEED_200GB": 200000,
    "SPEED_400GB": 400000,
    "SPEED_800GB": 800000
}


# To create Loopback, VLAN interfaces
def build_interfaces_create_request(interface_name):
    url = "data/openconfig-interfaces:interfaces"
    method = "PATCH"
    payload_template = """{"openconfig-interfaces:interfaces": {"interface": [{"name": "{{interface_name}}", "config": {"name": "{{interface_name}}"}}]}}"""
    input_data = {"interface_name": interface_name}
    env = jinja2.Environment(autoescape=False)
    t = env.from_string(payload_template)
    intended_payload = t.render(input_data)
    ret_payload = json.loads(intended_payload)
    request = {"path": url,
               "method": method,
               "data": ret_payload}
    return request


def retrieve_port_group_interfaces(module):
    port_group_interfaces = []
    method = "get"
    port_num_regex = re.compile(r'[\d]{1,4}$')
    port_group_url = 'data/openconfig-port-group:port-groups'
    request = {"path": port_group_url, "method": method}
    try:
        response = edit_config(module, to_request(module, request))
    except ConnectionError as exc:
        module.fail_json(msg=str(exc), code=exc.code)

    if 'openconfig-port-group:port-groups' in response[0][1] and "port-group" in response[0][1]['openconfig-port-group:port-groups']:
        port_groups = response[0][1]['openconfig-port-group:port-groups']['port-group']
        for pg_config in port_groups:
            if 'state' in pg_config:
                member_start = pg_config['state'].get('member-if-start', '')
                member_start = re.search(port_num_regex, member_start)
                member_end = pg_config['state'].get('member-if-end', '')
                member_end = re.search(port_num_regex, member_end)
                if member_start and member_end:
                    member_start = int(member_start.group(0))
                    member_end = int(member_end.group(0))
                    port_group_interfaces.extend(range(member_start, member_end + 1))

    return port_group_interfaces


def retrieve_default_intf_speed(module, intf_name):
    """
    Retrieve the default speed of a given interface.

    Args:
        module (object): The Ansible module.
        intf_name (str): The name of the interface.

    Returns:
        str: The default speed of the interface.

    Raises:
        AnsibleFailJson: If unable to retrieve the default port speed.

    This function calls the `retrieve_valid_intf_speed` function to get a list of valid speeds for the interface.
    It then finds the maximum speed in the list and converts it to the corresponding default speed.
    If the default speed is not found, the function raises an AnsibleFailJson exception.
    """
    v_speeds_int_list = retrieve_valid_intf_speed(module, intf_name)
    dft_speed_int = 0
    if v_speeds_int_list:
        dft_speed_int = max(v_speeds_int_list)
    dft_intf_speed = intf_speed_map.get(dft_speed_int, 'SPEED_DEFAULT')

    if dft_intf_speed == 'SPEED_DEFAULT':
        module.fail_json(msg="Unable to retireve default port speed for the interface {0}".format(intf_name))

    return dft_intf_speed


def retrieve_valid_intf_speed(module, intf_name):
    """
    Use the sonic-port module to get the list of valid speeds an interface can be assigned.

    Args:
        module (object): The Ansible module.
        intf_name (str): The name of the interface.

    Returns:
        list: The list of valid speeds.

    Raises:
        ConnectionError: If unable to connect to the sonic-port module.
    """
    valid_speed_method = "get"
    valid_speed_sonic_port_url = 'data/sonic-port:sonic-port/PORT/PORT_LIST=%s'
    valid_speed_sonic_port_vs_url = (valid_speed_sonic_port_url + '/valid_speeds') % quote(intf_name, safe='')
    valid_speed_request = {"path": valid_speed_sonic_port_vs_url, "method": valid_speed_method}
    try:
        valid_speed_response = edit_config(module, to_request(module, valid_speed_request))
    except ConnectionError as exc:
        module.fail_json(msg=str(exc), code=exc.code)

    v_speeds_int_list = []
    if 'sonic-port:valid_speeds' in valid_speed_response[0][1]:
        v_speeds = valid_speed_response[0][1].get('sonic-port:valid_speeds', '')
        v_speeds_list = v_speeds.split(",")
        for vs in v_speeds_list:
            v_speeds_int_list.append(int(vs))

    if v_speeds_int_list:
        return v_speeds_int_list
    else:
        module.fail_json(msg="Unable to retrieve valid port speeds for the interface {0}".format(intf_name))
