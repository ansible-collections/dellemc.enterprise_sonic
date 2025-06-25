#
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The sonic snmp fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from __future__ import absolute_import, division, print_function
__metaclass__ = type
from copy import deepcopy

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import utils
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    remove_empties
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.snmp.snmp import SnmpArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    to_request,
    edit_config
)
from ansible.module_utils.connection import ConnectionError

class SnmpFacts(object):
    """ The sonic snmp fact class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = SnmpArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)

    def populate_facts(self, connection, ansible_facts, data=None):
        """ Populate the facts for snmp
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        if connection:
            pass

        if not data:
            # Fetch data from the current device configuration
            # (Skip if operating on previously fetched configuraation)
            data = self.get_all_snmps()

        snmps = data

        facts = {}
        if snmps:
            facts['snmp'] = {}
            params = utils.validate_config(self.argument_spec, {'config': snmps})

            if params:
                facts['snmp'].update(remove_empties(params['config']))
        ansible_facts['ansible_network_resources'].update(facts)

        return ansible_facts

    def get_all_snmps(self):
        """
        Get all the snmp server configuration in the device.
        """
        path = "data/ietf-snmp:snmp"
        method = "GET"
        request = [{"path": path, "method": method}]
        try:
            response = edit_config(self._module, to_request(self._module, request))
        except ConnectionError as exc:
            self._module.fail_json(msg=str(exc), code=exc.code)

        snmp_dict = {}
        if len(response) == 0 or len(response[0]) == 0:
            return snmp_dict

        snmp_list = response[0][1].get("ietf-snmp:snmp", {})
        if "ietf-snmp:snmp" in response[0][1] and snmp_list:
            snmp_dict.update({'agentaddress': self.get_snmp_agentaddress(snmp_list)})
            snmp_dict.update({'community': self.get_snmp_community(snmp_list)})
            snmp_dict.update({'engine': self.get_snmp_engine(snmp_list)})
            snmp_dict.update({'user': self.get_snmp_users(snmp_list)})
            snmp_dict.update({'view': self.get_snmp_view(snmp_list)})
            snmp_dict.update({'contact': self.get_snmp_contact(snmp_list)})
            snmp_dict.update({'location': self.get_snmp_location(snmp_list)})
            snmp_dict.update({'enable_trap': list(self.get_snmp_enable_trap(snmp_list))})
            snmp_dict.update({'group': self.get_snmp_group(snmp_list)})
            host = self.get_snmp_hosts_targets(snmp_list)
            snmp_dict.update({'host': host})

        return snmp_dict

    def get_snmp_agentaddress(self, snmp_list):
        """
        Get snmp agent address from the snmp list
        """
        agentaddress_list = []
        agentaddress_udp_option_paths = {'interface': "ietf-snmp-ext:interface", 'ip': "ip", 'port': "port"}

        if not snmp_list.get('engine') or not snmp_list.get('engine').get('listen'):
            return agentaddress_list
        agentaddress_config = snmp_list['engine']['listen']

        for agentaddress in agentaddress_config:
            agentaddress_dict = {}
            agentaddress_udp = agentaddress.get('udp')
            if not agentaddress_udp:
                continue
            for option, path in agentaddress_udp_option_paths.items():
                option_val = agentaddress_udp.get(path)
                if option_val is not None:
                    agentaddress_dict[option] = option_val
            agentaddress_dict['name'] = agentaddress.get('name')
            agentaddress_list.append(agentaddress_dict)
        return agentaddress_list

    def get_snmp_community(self, snmp_list):
        """
        Get snmp community from the snmp list
        """
        community_list = []

        if not snmp_list.get('community'):
            return community_list
        community_config = snmp_list['community']

        for community in community_config:
            if community is None:
                continue
            community_list.append({"name": community.get("index"), "group": community.get("security-name")})

        return community_list

    def get_snmp_engine(self, snmp_list):
        """
        Get snmp engine from the snmp list
        """
        engine = ''

        if not snmp_list.get('engine') or not snmp_list.get('engine').get('engine-id'):
            return engine

        engine_config = snmp_list['engine']

        return engine_config.get('engine-id')

    def get_snmp_users(self, snmp_list):
        """
        Get snmp users from the snmp list
        """
        user_list = []
        group_config = []

        if not snmp_list.get('usm') or not snmp_list.get('usm').get('local') or not snmp_list.get('usm').get('local').get('user'):
            return user_list

        if snmp_list.get('vacm') and snmp_list.get('vacm').get('group'):
            group_config = snmp_list['vacm']['group']

        user_config = snmp_list['usm']['local'].get('user')

        for user in user_config:
            user_dict = {}
            if user.get('auth'):
                auth_type_path = list(user['auth'].keys())[0]
                auth_type = auth_type_path
                if ":" in auth_type:
                    part = auth_type_path.split(':')
                    auth_type = part[1].strip()
                    auth_type = auth_type.replace("_", "-")
                user_dict['auth'] = {
                    'auth_type': auth_type,
                    'key': user['auth'][auth_type_path].get('key')
                }
            if user.get('priv'):
                priv_type = list(user['priv'].keys())[0]
                user_dict['priv'] = {
                    'priv_type': priv_type,
                    'key': user['priv'][priv_type].get('key')
                }
            matched_user = None
            group_name = ""
            for group in group_config:
                if group.get('member') is not None:
                    matched_user = next((member for member in group['member'] if member['security-name'] == user['name']), None)
                    if matched_user is not None:
                        group_name = group['name']
                        break
            user_dict['group'] = group_name
            user_dict['name'] = user.get('name')
            user_dict['encrypted'] = user.get('ietf-snmp-ext:encrypted')

            user_list.append(user_dict)
        return user_list

    def get_snmp_view(self, snmp_list):
        """
        Get snmp view from the snmp list
        """
        view_list = []

        if not snmp_list.get('vacm') or not snmp_list.get('vacm').get('view'):
            return view_list

        view_config = snmp_list['vacm']['view']

        for view in view_config:
            view_list.append({"name": view.get("name"), "included": view.get("include"), "excluded": view.get("exclude")})

        return view_list

    def get_snmp_contact(self, snmp_list):
        """
        Get snmp contact from the snmp list
        """
        contact_str = ""

        if not snmp_list.get('ietf-snmp-ext:system') or not snmp_list.get('ietf-snmp-ext:system').get('contact'):
            return contact_str

        snmp_server_config = snmp_list['ietf-snmp-ext:system']['contact']

        if snmp_server_config:
            contact_str = snmp_server_config

        return str(contact_str)

    def get_snmp_location(self, snmp_list):
        """
        Get snmp location from the snmp list
        """
        location_str = ""
        if not snmp_list.get('ietf-snmp-ext:system') or not snmp_list.get('ietf-snmp-ext:system').get('location'):
            return location_str

        location = snmp_list['ietf-snmp-ext:system']['location']

        if location:
            return location

        return str(location_str)

    def get_snmp_enable_trap(self, snmp_list):
        """
        Get snmp enable trap from the snmp list
        """
        enable_trap = []
        if not snmp_list.get('ietf-snmp-ext:system'):
            return enable_trap
        server = snmp_list.get('ietf-snmp-ext:system')

        if server.get('trap-enable'):
            enable_trap.append("all")
        elif server.get('notifications'):
            auth_fail_trap = server.get('notifications').get('authentication-failure-trap')
            bgp_trap = server.get('notifications').get('bgp-traps')
            config_change_trap = server.get('notifications').get('config-change-trap')
            link_down_trap = server.get('notifications').get('link-down-trap')
            link_up_trap = server.get('notifications').get('link-up-trap')
            ospf_trap = server.get('notifications').get('ospf-traps')

            if auth_fail_trap:
                enable_trap.append('auth-fail')
            if bgp_trap:
                enable_trap.append('bgp')
            if config_change_trap:
                enable_trap.append('config-change')
            if link_down_trap:
                enable_trap.append('link-down')
            if link_up_trap:
                enable_trap.append('link-up')
            if ospf_trap:
                enable_trap.append('ospf')

        return enable_trap

    def get_snmp_group(self, snmp_list):
        """
        Get snmp group from the snmp list
        """
        group_list = []

        if not snmp_list.get('vacm') or not snmp_list.get('vacm').get('group'):
            return group_list

        snmp_group_list = snmp_list.get('vacm').get('group')

        for group in snmp_group_list:
            group_dict = {}
            name = group.get('name')
            if name is None:
                break
            group_dict['name'] = name
            access_list = []
            if group.get('access'):
                access_list = self.get_group_access(group.get('access'))
            group_dict['access'] = access_list
            group_list.append(group_dict)

        return group_list

    def get_group_access(self, access_list):
        """ Get the access list from given access list
        """
        access_l = []

        for access in access_list:
            access_dict = {}

            access_dict['notify_view'] = access.get('notify-view')
            access_dict['read_view'] = access.get('read-view')
            access_dict['write_view'] = access.get('write-view')
            if access.get('security-model') is None:
                break
            if access.get("security-level"):
                access_dict['security_level'] = access.get('security-level')
            if access.get("security-model"):
                access_dict['security_model'] = access.get('security-model')

            access_l.append(access_dict)

        return access_l

    def get_snmp_hosts_targets(self, snmp_list):
        """
        Get snmp hosts and targets from the snmp list
        """
        host_list = []

        if not snmp_list.get('target') or not snmp_list.get('target-params'):
            return host_list

        target_config = snmp_list.get('target')
        target_params_config = snmp_list.get('target-params')

        for host in target_config:
            current_target_param = host.get('target-params')
            host_dict = {}

            matched_target_param = next((each_tp for each_tp in target_params_config if each_tp['name'] == current_target_param), None)
            if matched_target_param is None:
                continue
            user = matched_target_param.get("usm")
            if user is None:
                vc = matched_target_param.get('v2c')
                if vc:
                    host_dict["community"] = matched_target_param.get('v2c').get("security-name")
            else:
                user_dict = {}
                security_level = matched_target_param.get('usm').get("security-level")
                user_security_level = "auth"
                if security_level == 'no-auth-no-priv':
                    user_security_level = "noauth"
                if security_level == "no-auth-priv":
                    user_security_level = "priv"
                user_dict["security_level"] = user_security_level
                user_dict["name"] = matched_target_param.get('usm').get("user-name") if matched_target_param.get('usm') else None
                host_dict["user"] = user_dict

            if host.get('udp'):
                host_dict['ip'] = host['udp'].get('ip')
                host_dict['port'] = host['udp'].get('port')

            host_dict['retries'] = host.get("retries")
            host_dict['tag'] = host['tag'][0][:-6] if host.get('tag') else None
            host_dict['timeout'] = host.get("timeout")
            host_dict['source_interface'] = host.get("ietf-snmp-ext:source-interface")
            host_dict['vrf'] = host.get('udp').get('ietf-snmp-ext:vrf-name')

            host_list.append(host_dict)

        current_host = {}
        current_host['host-info'] = host_list
        current_host['target-entry'] = host.get('name')
        return host_list
