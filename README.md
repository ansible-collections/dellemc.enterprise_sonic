Ansible Network Collection for Enterprise SONiC Distribution by Dell Technologies
=================================================================================

This collection includes Ansible core modules, network resource modules, and plugins needed to provision and manage Dell Inc PowerSwitch platforms running Enterprise SONiC Distribution by Dell Technologies. Sample playbooks and documentation are also included to show how the collection can be used.

Supported connections
---------------------
The SONiC Ansible collection supports network_cli and httpapi connections.

Plugins
--------
**CLICONF plugin**

Name | Description
--- | ---
[network_cli](https://github.com/ansible-collections/dellemc.sonic)|Use Ansible CLICONF to run commands on Enterprise SONiC

**HTTPAPI plugin**

Name | Description
--- | ---
[httpapi](https://github.com/ansible-collections/dellemc.sonic)|Use Ansible HTTPAPI to run commands on Enterprise SONiC

Collection core modules
------------------------
Name | Description | Connection type
--- | --- | ---
[**sonic_command**](https://github.com/ansible-collections/dellemc.sonic/blob/master/plugins/modules/sonic_command.py)|Run commands through the Management Framework CLI|network_cli
[**sonic_config**](https://github.com/ansible-collections/dellemc.sonic/blob/master/plugins/modules/sonic_config.py)|Manage configuration through the Management Framework CLI|network_cli
[**sonic_api**](https://github.com/ansible-collections/dellemc.sonic/blob/master/plugins/modules/sonic_api.py)|Perform REST operations through the Management Framework REST API|httpapi

Collection network resource modules
-----------------------------------
The SONiC Ansible network resource modules are listed below and they need ***httpapi*** as the connection type.

| Interfaces | BGP |
| ----- | ----- |
| [**sonic_interfaces**](https://github.com/ansible-collections/dellemc.sonic/blob/master/plugins/modules/sonic_interfaces.py)|[**sonic_bgp**](https://github.com/ansible-collections/dellemc.sonic/tree/master/plugins/modules/sonic_bgp.py)|
| [**sonic_l2_interfaces**](https://github.com/ansible-collections/dellemc.sonic/tree/master/plugins/modules/sonic_l2_interfaces.py)| [**sonic_bgp_af**](https://github.com/ansible-collections/dellemc.sonic/tree/master/plugins/modules/sonic_bgp_af.py)|
| [**sonic_l3_interfaces**](https://github.com/ansible-collections/dellemc.sonic/tree/master/plugins/modules/sonic_l3_interfaces.py) |[**sonic_as_paths**](https://github.com/ansible-collections/dellemc.sonic/tree/master/plugins/modules/sonic_bgp_as_paths.py)|
|**Port channel**|[**sonic_bgp_communities**](https://github.com/ansible-collections/dellemc.sonic/tree/master/plugins/modules/sonic_bgp_communities.py)|
|[**sonic_lag_interfaces**](https://github.com/ansible-collections/dellemc.sonic/tree/master/plugins/modules/sonic_lag_interfaces.py)|[**sonic_bgp_ext_communities**](https://github.com/ansible-collections/dellemc.sonic/tree/master/plugins/modules/sonic_bgp_ext_communities.py)|
|**VLANs**|[**sonic_bgp_neighbors**](https://github.com/ansible-collections/dellemc.sonic/tree/master/plugins/modules/sonic_bgp_neighbors.py)|
|[**sonic_vlans**](https://github.com/ansible-collections/dellemc.sonic/tree/master/plugins/modules/sonic_vlans.py)|[**sonic_bgp_neighbors_af**](https://github.com/ansible-collections/dellemc.sonic/tree/master/plugins/modules/sonic_bgp_neighbors_af.py)|

Sample use case playbooks
-------------------------
The playbooks directory includes the following sample playbook that show end-to-end use cases.

Name | Description
--- | ---
[**CLOS fabric**](https://github.com/ansible-collections/dellemc.sonic/tree/master/playbooks/clos_fabric)|Example playbook to build a Layer 3 leaf-spine fabric

Installation
----------------
Install the latest version of the SONiC collection from Ansible Galaxy.

      ansible-galaxy collection install dellemc.sonic

To install a specific version, specify a version range identifier. For example, to install the most recent version that is greater than or equal to 1.0.0 and less than 2.0.0.

      ansible-galaxy collection install 'dellemc.sonic:>=1.0.0,<2.0.0'

Version compatibility
----------------------
* Ansible version 2.10 or later
* Enterprise SONiC Distribution by Dell Technologies version 3.1 or later
* Python 3

> NOTE: Community SONiC versions that include the Management Framework container should work as well, however, this collection has not been tested nor validated with community versions, nor is it supported.

Sample playbooks
-----------------
**VLAN configuration using CLICONF**

**sonic_network_cli.yaml**

    ---

    - name: "Configuration using the SONiC Management Framework CLI"
      hosts: sonic_switches
      gather_facts: no
      connection: network_cli
      collections:
        - dellemc.sonic
      tasks:
        - name: Add VLAN entry
          sonic_config:
            commands: ['interface Vlan 700','exit']
            save: yes
          register: config_op
        - name: Test SONiC single command
          sonic_command:
            commands: 'show vlan'
          register: cmd_op

**VLAN configuration using HTTPAPI**

**sonic_httpapi.yaml**

    ---

    - name: "Configuration using the SONiC Management Framework REST API"
      hosts: sonic_switches
      gather_facts: no
      connection: httpapi
      collections:
        - dellemc.sonic
      tasks:
        - name: Perform PUT operation to add VLAN network instance
          sonic_api:
            url: data/openconfig-network-instance:network-instances/network-instance=Vlan100
            method: "PUT"
            body: {"openconfig-network-instance:network-instance": [{"name": "Vlan100","config": {"name": "Vlan100"}}]}
            status_code: 204
        - name: Perform GET operation to view VLAN network instance
          sonic_api:
            url: data/openconfig-network-instance:network-instances/network-instance=Vlan100
            method: "GET"
            status_code: 200
          register: api_op

**Configuration using network resource modules**

**sonic_resource_modules.yaml**

    ---

    - name: "Configuration of VLANs, L2 and L3 interfaces using SONiC resource modules"
      hosts: sonic_switches
      gather_facts: False
      connection: httpapi
      collections:
        - dellemc.sonic
      tasks:
       - name: "Configuring VLANs"
         sonic_vlans:
            config:
             - vlan_id: 701
             - vlan_id: 702
             - vlan_id: 703
             - vlan_id: 704
            state: merged
         register: sonic_vlans_creation_output
       - name: "Configuring L2 interfaces"
         sonic_l2_interfaces:
            config:
            - name: Ethernet28
              access:
                vlan: 701
              trunk:
                allowed_vlans:
                  - vlan: 702
                  - vlan: 703
            state: merged
         register: sonic_l2_interfaces_configurarion_output
       - name: "Configuring L3 interfaces"
         sonic_l3_interfaces:
           config:
            - name: Ethernet20
              ipv4:
                - address: 8.1.1.1/16
              ipv6:
                - address: 3333::1/16
           state: merged
         register: sonic_l3_interfaces_configuration_output

**host_vars/sonic_sw1.yaml**

    hostname: sonic_sw1

    # Common parameters for connection type httpapi or network_cli
    ansible_ssh_user: xxxx
    ansible_ssh_pass: xxxx
    ansible_network_os: dellemc.sonic.sonic

    # Additional parameters for connection type httpapi
    ansible_httpapi_use_ssl=true
    ansible_httpapi_validate_certs=false

**inventory.yaml**

    [sonic_sw1]
    sonic_sw1 ansible_host=100.104.28.119

    [sonic_sw2]
    sonic_sw2 ansible_host=100.104.28.120

    [sonic_switches:children]
    sonic_sw1
    sonic_sw2


(c) 2020 Dell Inc. or its subsidiaries. All rights reserved.
