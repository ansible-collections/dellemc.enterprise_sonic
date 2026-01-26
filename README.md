Ansible Network Collection for Enterprise SONiC Distribution by Dell Technologies
=================================================================================

This collection includes Ansible core modules, network resource modules, and plugins needed to provision and manage Dell EMC PowerSwitch platforms running Enterprise SONiC Distribution by Dell Technologies. Sample playbooks and documentation are also included to show how the collection can be used.

Supported connections
---------------------
The SONiC Ansible collection supports network_cli and httpapi connections.

Plugins
--------
**CLICONF plugin**

Name | Description
--- | ---
[network_cli](https://github.com/ansible-collections/dellemc.enterprise_sonic)|Use Ansible CLICONF to run commands on Enterprise SONiC

**HTTPAPI plugin**

Name | Description
--- | ---
[httpapi](https://github.com/ansible-collections/dellemc.enterprise_sonic)|Use Ansible HTTPAPI to run commands on Enterprise SONiC

Collection core modules
------------------------
Name | Description | Connection type
--- | --- | ---
[**sonic_command**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_command.py)|Run commands through the Management Framework CLI|network_cli
[**sonic_config**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_config.py)|Manage configuration through the Management Framework CLI|network_cli
[**sonic_api**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_api.py)|Perform REST operations through the Management Framework REST API|httpapi
[**sonic_api**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_facts.py)|Collect "facts" (configuration) in argspec format for selected modules|httpapi

Collection network resource modules
-----------------------------------
Listed are the SONiC Ansible network resource modules which need ***httpapi*** as the connection type. Supported operations are ***merged***, ***deleted***, ***replaced*** and ***overridden***.

Name | Description
--- | ---
[**sonic_aaa**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_aaa.py)| Manage AAA and its parameters
[**sonic_acl_interfaces**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_acl_interfaces.py)| Manage access control list (ACL) to interface binding
[**sonic_ars**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_ars.py)| Manage adaptive routing and switching (ARS) configuration on SONiC
[**sonic_bfd**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_bfd.py)| Manage BFD configuration
[**sonic_bgp**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_bgp.py)| Manage global BGP and its parameters
[**sonic_bgp_af**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_bgp_af.py)| Manage global BGP address-family and its parameters
[**sonic_bgp_as_paths**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_bgp_as_paths.py)| Manage BGP autonomous system path (or as-path-list) and its parameters
[**sonic_bgp_communities**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_bgp_communities.py)| Manage BGP community and its parameters
[**sonic_bgp_ext_communities**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_bgp_ext_communities.py)| Manage BGP extended community-list and its parameters
[**sonic_bgp_neighbors**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_bgp_neighbors.py)| Manage a BGP neighbor and its parameters
[**sonic_bgp_neighbors_af**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_bgp_neighbors_af.py)| Manage the BGP neighbor address-family and its parameters
[**sonic_br_l2pt**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_br_l2pt.py)| Manage L2PT configurations on SONiC
[**sonic_copp**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_copp.py)| Manage CoPP configuration
[**sonic_dcbx**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_dcbx.py)| Manage DCBx configurations on SONiC
[**sonic_dhcp_relay**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_dhcp_relay.py)| Manage DHCP and DHCPv6 relay configurations
[**sonic_dhcp_snooping**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_dhcp_snooping.py)| Manage DHCP Snooping
[**sonic_drop_counter**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_drop_counter.py)| Manage drop counter configuration on SONiC
[**sonic_ecmp_load_share**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_ecmp_load_share.py)| IP ECMP load share mode configuration handling for SONiC
[**sonic_evpn_esi_multihome**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_evpn_esi_multihome.py)| Manage EVPN ESI multihoming configuration on SONiC
[**sonic_fbs_classifiers**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_fbs_classifiers.py)| Manage flow based services (FBS) classifiers configuration on SONiC
[**sonic_fbs_groups**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_fbs_groups.py)| Manage flow based services (FBS) groups configuration on SONiC
[**sonic_fbs_interfaces**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_fbs_interfaces.py)| Manage flow based services (FBS) interfaces configuration on SONiC
[**sonic_fbs_policies**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_fbs_policies.py)| Manage flow based services (FBS) policies configuration on SONiC
[**sonic_fips**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_fips.py)| Manage FIPS configurations
[**sonic_image_management**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_image_management.py)| Manage installation of Enterprise SONiC image, software patch and firmware updater.
[**sonic_interfaces**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_interfaces.py)| Configure Interface attributes
[**sonic_ip_neighbor**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_ip_neighbor.py)| Manage IP neighbor global configuration
[**sonic_ip_neighbor_interfaces**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_ip_neighbor_interfaces.py)| Manage interface-specific IP neighbor configurations on SONiC
[**sonic_ipv6_router_advertisement**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_ipv6_router_advertisement.py)| Manage interface-specific IPv6 Router Advertisement configurations on SONiC
[**sonic_l2_acls**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_l2_acls.py)| Manage Layer 2 access control lists (ACL) configurations
[**sonic_l2_interfaces**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_l2_interfaces.py)| Configure interface-to-VLAN association
[**sonic_l3_acls**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_l3_acls.py)| Manage Layer 3 access control lists (ACL) configurations
[**sonic_l3_interfaces**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_l3_interfaces.py)| Configure the IPv4 and IPv6 parameters on Interfaces
[**sonic_lag_interfaces**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_lag_interfaces.py)| Manage link aggregation group (LAG) interface parameters
[**sonic_ldap**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_ldap.py)| Configure global LDAP server settings
[**sonic_lldp_global**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_lldp_global.py)| Manage Global LLDP configurations
[**sonic_lldp_interfaces**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_lldp_interfaces.py)| Manage interface LLDP configurations
[**sonic_logging**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_logging.py)| Manage logging configuration
[**sonic_login_lockout**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_login_lockout.py)| Manage Global Login Lockout configuration
[**sonic_lst**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_lst.py)| Manage link state tracking (LST) configuration on SONiC
[**sonic_mac**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_mac.py)| Manage MAC configuration
[**sonic_mclag**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_mclag.py)| Manage multi chassis link aggregation groups domain (MCLAG) and its parameters
[**sonic_mfa**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_mfa.py)| Manage Multi-factor authentication (MFA) configurations on SONiC
[**sonic_mgmt_servers**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_mgmt_servers.py)| Manage management servers configuration
[**sonic_mirroring**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_mirroring.py)| Manage port mirroring configuration on SONiC
[**sonic_network_policy**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_network_policy.py)| Manage network policy configuration on SONiC
[**sonic_ntp**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_ntp.py)| Manage NTP configuration
[**sonic_ospf_area**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_ospf_area.py)| Configure OSPF area setting
[**sonic_ospfv2**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_ospfv2.py)| Configure global OSPFv2 protocol settings
[**sonic_ospfv2_interfaces**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_ospfv2_interfaces.py)| Configure OSPFv2 interface mode protocol settings
[**sonic_ospfv3**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_ospfv3.py)| Configure global OSPFv3 protocol settings on SONiC
[**sonic_ospfv3_area**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_ospfv3_area.py)| Configure OSPFv3 area settings on SONiC
[**sonic_ospfv3_interfaces**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_ospfv3_interfaces.py)| Configure OSPFv3 interface mode protocol settings on SONiC
[**sonic_pim_global**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_pim_global.py)| Manage global PIM configuration
[**sonic_pim_interfaces**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_pim_interfaces.py)| Manage interface-specific PIM configurations
[**sonic_pki**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_pki.py)| Manages PKI attributes
[**sonic_pms**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_pms.py)| Configure interface mode port security settings on SONiC
[**sonic_poe**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_poe.py)| Manage Power over Ethernet PoE configuration
[**sonic_port_breakout**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_port_breakout.py)| Configure port breakout settings on physical interfaces
[**sonic_port_group**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_port_group.py)| Manage port group configuration
[**sonic_prefix_lists**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_prefix_lists.py)| Manage prefix list configuration
[**sonic_ptp_default_ds**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_ptp_default_ds.py)| Manage global PTP configurations on SONiC
[**sonic_ptp_port_ds**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_ptp_port_ds.py)| Manage port specific PTP configurations on SONiC
[**sonic_qos_buffer**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_qos_buffer.py)| Manage QoS buffer configuration
[**sonic_qos_interfaces**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_qos_interfaces.py)| Manage QoS interfaces configuration
[**sonic_qos_maps**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_qos_maps.py)| Manage QoS maps configuration
[**sonic_qos_pfc**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_qos_pfc.py)| Manage QoS PFC configuration
[**sonic_qos_scheduler**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_qos_scheduler.py)| Manage QoS scheduler configuration
[**sonic_qos_wred**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_qos_wred.py)| Manage QoS WRED profiles configuration
[**sonic_radius_server**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_radius_server.py)| Manage RADIUS server and its parameters
[**sonic_roce**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_roce.py)| Manage RoCE QoS configuration
[**sonic_route_maps**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_route_maps.py)| Manage route map configuration
[**sonic_sflow**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_sflow.py)| Manage sflow configuration settings
[**sonic_ssh**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_ssh.py)| Manage SSH configuration settings
[**sonic_ssh_server**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_ssh_server.py)| Manage SSH server configurations on SONiC
[**sonic_static_routes**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_static_routes.py)| Manage static routes configuration
[**sonic_stp**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_stp.py)| Manage STP configuration
[**sonic_system**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_system.py)| Configure system parameters
[**sonic_tacacs_server**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_tacacs_server.py)| Manage TACACS server and its parameters
[**sonic_users**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_users.py)| Manage users and its parameters
[**sonic_vlan_mapping**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_vlan_mapping.py)| Configure vlan mappings
[**sonic_vlans**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_vlans.py)| Manage VLAN and its parameters
[**sonic_vrfs**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_vrfs.py)| Manage VRFs and associate VRFs to interfaces
[**sonic_vrrp**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_vrrp.py)| Manage VRRP protocol configuration settings
[**sonic_vxlans**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/plugins/modules/sonic_vxlans.py)| Manage VxLAN EVPN and its parameters

Sample use case playbooks
-------------------------
The playbooks directory includes this sample playbook that shows end-to-end use cases.

Name | Description
--- | ---
[**BGP Layer 3 fabric**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/playbooks/bgp_l3_fabric)|Example playbook to build a Layer 3 leaf-spine fabric

Version compatibility
----------------------
* Recommended Ansible version 2.17 or higher (This is required for enterprise_sonic collection version >= 3.2.0).
* Enterprise SONiC Distribution by Dell Technologies version 3.1 or higher
* Recommended Python 3.10 or higher (This is required for enterprise_sonic collection version >= 3.2.0.).
* Dell Enterprise SONiC images for releases 3.1 - 3.5: Use Ansible Enterprise SONiC collection version 1.1.0 or later 1.m.n versions (from the 1.x branch of this repo)
* Dell Enterprise SONiC images for release 4.0 and later 4.x.y releases before 4.4.0: Use Ansible Enterprise SONiC collection version 2.0.0 or later 2.m.n releases (from the "2.x" branch of this repo).
* Dell Enterprise SONiC images for release 4.4.0 and later 4.x.y releases: Use Ansible Enterprise SONiC collection version 3.0.0 or later 3.m.n releases (from the "main" branch of this repo).


> **NOTE**: Community SONiC versions that include the Management Framework container should work as well, however, this collection has not been tested nor validated 
        with community versions and is not supported.

##### Setting Environment Variables

Option 1: Add the environment variable while running the playbook.


      ANSIBLE_NETWORK_GROUP_MODULES=sonic ansible-playbook sample_playbook.yaml -i inventory.ini
      
      
Option 2: Add the environment variable in user profile.


      ANSIBLE_NETWORK_GROUP_MODULES=sonic
      

Installation of Enterprise SONiC collection from Ansible Galaxy
---------------------------------------------------------------

Install the latest version of the Enterprise SONiC collection from Ansible Galaxy.

      ansible-galaxy collection install dellemc.enterprise_sonic

To install a specific version, specify a version range identifier. For example, to install the most recent version that is greater than or equal to 1.0.0 and less than 2.0.0.

      ansible-galaxy collection install 'dellemc.enterprise_sonic:>=1.0.0,<2.0.0'


Sample playbooks
-----------------
**VLAN configuration using CLICONF**

***sonic_network_cli.yaml***

    ---

    - name: SONiC Management Framework CLI configuration examples
      hosts: sonic_switches
      gather_facts: no
      connection: network_cli
      tasks:
        - name: Add VLAN entry
          dellemc.enterprise_sonic.sonic_config:
            commands: ['interface Vlan 700','exit']
            save: yes
          register: config_op
        - name: Test SONiC single command
          dellemc.enterprise_sonic.sonic_command:
            commands: 'show vlan'
          register: cmd_op

**VLAN configuration using HTTPAPI**

***sonic_httpapi.yaml***

    ---

    - name: SONiC Management Framework REST API examples
      hosts: sonic_switches
      gather_facts: no
      connection: httpapi
      tasks:
        - name: Perform PUT operation to add a VLAN network instance
          dellemc.enterprise_sonic.sonic_api:
            url: data/openconfig-network-instance:network-instances/network-instance=Vlan100
            method: "PUT"
            body: {"openconfig-network-instance:network-instance": [{"name": "Vlan100","config": {"name": "Vlan100"}}]}
            status_code: 204
        - name: Perform GET operation to view VLAN network instance
          dellemc.enterprise_sonic.sonic_api:
            url: data/openconfig-network-instance:network-instances/network-instance=Vlan100
            method: "GET"
            status_code: 200
          register: api_op

**Configuration using network resource modules**

***sonic_resource_modules.yaml***

    ---

    - name: VLANs, Layer 2 and Layer 3 interfaces configuration using Enterprise SONiC resource modules
      hosts: sonic_switches
      gather_facts: no
      connection: httpapi
      tasks:
       - name: Configure VLANs
         dellemc.enterprise_sonic.sonic_vlans:
            config:
             - vlan_id: 701
             - vlan_id: 702
             - vlan_id: 703
             - vlan_id: 704
            state: merged
         register: sonic_vlans_output
       - name: Configure Layer 2 interfaces
         dellemc.enterprise_sonic.sonic_l2_interfaces:
            config:
            - name: Eth1/2
              access:
                vlan: 701
              trunk:
                allowed_vlans:
                  - vlan: 702
                  - vlan: 703
            state: merged
         register: sonic_l2_interfaces_output
       - name: Configure Layer 3 interfaces
         dellemc.enterprise_sonic.sonic_l3_interfaces:
           config:
            - name: Eth1/3
              ipv4:
                - address: 8.1.1.1/16
              ipv6:
                - address: 3333::1/16
           state: merged
         register: sonic_l3_interfaces_output

***host_vars/sonic_sw1.yaml***

    hostname: sonic_sw1

    # Common parameters for connection type httpapi or network_cli:
    ansible_user: xxxx
    ansible_password: xxxx
    ansible_network_os: dellemc.enterprise_sonic.sonic

    # Additional parameters for connection type httpapi:
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false

***inventory.ini***

    [sonic_sw1]
    sonic_sw1 ansible_host=100.104.28.119

    [sonic_sw2]
    sonic_sw2 ansible_host=100.104.28.120

    [sonic_switches:children]
    sonic_sw1
    sonic_sw2

Support
-------

Support is provided for all of the collection modules for Ansible version 2.17 or higher.

To submit a support request for this collection, open a [GitHub issue](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues) under the collection repository.

Releasing, Versioning and Deprecation
-------------------------------------

This collection follows [Semantic Versioning](https://semver.org/). More details on versioning can be found [in the Ansible docs](https://docs.ansible.com/ansible/latest/dev_guide/developing_collections.html#collection-versions).

We plan to regularly release new minor or bugfix versions once new features or bugfixes have been implemented.

Enterprise SONiC Ansible Modules deprecation cycle is aligned with [Ansible](https://docs.ansible.com/ansible/latest/dev_guide/module_lifecycle.html).

Source control branches on Github:
  - Released code versions are located on "release" branches with names of the form "M.x", where "M" specifies the "major" release version for releases residing on the branch.
  - Unreleased and pre-release code versions are located on sub-branches of the "main" branch. This is a development branch, and is not intended for use in production environments.

Code of Conduct
---------------

This repository adheres to the [Ansible Community code of conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)

Communication
-------------

* Join the Ansible forum:
  * [Get Help](https://forum.ansible.com/c/help/6): get help or help others.
  * [Social Spaces](https://forum.ansible.com/c/chat/4): gather and interact with fellow enthusiasts.
  * [News & Announcements](https://forum.ansible.com/c/news/5): track project-wide announcements including social events.

* The Ansible [Bullhorn newsletter](https://docs.ansible.com/ansible/devel/community/communication.html#the-bullhorn): used to announce releases and important changes.

For more information about communication, see the [Ansible communication guide](https://docs.ansible.com/ansible/devel/community/communication.html).

License Information
-------------------

This collection is published under the [GNU General Public License](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/main/LICENSE).


© Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved.
