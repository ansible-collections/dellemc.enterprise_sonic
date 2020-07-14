The Ansible collection for Enterprise SONiC Distribution by Dell Technologies
====================================================================
The SONiC Ansible collection includes resource modules, plugins, and sample playbooks that can be used to work on Dell EMC PowerSwitch platforms running Enterprise SONiC Distribution by Dell Technologies. It also includes information that shows how the collection can be used. This is the beta version tested on Enterprise SONiC Distribution by Dell Technologies, release 3.0.2.

Ansible version compatibility
=============================
This collection has been tested against Ansible versions >=2.9.10,<2.11.

Supported connections
=====================
The SONiC Ansible collection supports network_cli and httpapi connections.

## Included content
### Cliconf plugins
Name | Description
--- | ---
[network_cli](https://github.com/ansible-collections/dellemc.sonic)|Use Ansible `cliconf` to run commands on Enterprise SONiC platforms

### Httpapi plugins
Name | Description
--- | ---
[httpapi](https://github.com/ansible-collections/dellemc.sonic)|Perform REST operations on remote devices running Enterprise SONiC

Modules
-------
Name | Description
--- | ---
[**dellemc.sonic.sonic_interfaces**](https://github.com/ansible-collections/dellemc.sonic/blob/master/plugins/module_utils/network/sonic/config/interfaces/interfaces.py)|Enterprise SONiC interfaces resource module
[**dellemc.sonic.sonic_l2_interfaces**](https://github.com/ansible-collections/dellemc.sonic/tree/master/plugins/module_utils/network/sonic/config/l2_interfaces/l2_interfaces.py)|Enterprise SONiC l2_interfaces resource module
[**dellemc.sonic.sonic_l3_interfaces**](https://github.com/ansible-collections/dellemc.sonic/tree/master/plugins/module_utils/network/sonic/config/l3_interfaces/l3_interfaces.py)|Enterprise SONiC l3_interfaces resource module
[**dellemc.sonic.sonic_lag_interfaces**](https://github.com/ansible-collections/dellemc.sonic/tree/master/plugins/module_utils/network/sonic/config/lag_interfaces/lag_interfaces.py)|Enterprise  SONiC lag_interfaces resource module
[**dellemc.sonic.sonic_vlans**](https://github.com/ansible-collections/dellemc.sonic/tree/master/plugins/module_utils/network/sonic/config/vlans/vlans.py)|Enterprise SONiC VLANs resource module
[**sonic_command.py**](https://github.com/ansible-collections/dellemc.sonic/blob/master/plugins/modules/sonic_command.py)|Run commands from Management Framework CLI on remote devices running Enterprise SONiC
[**sonic_config.py**](https://github.com/ansible-collections/dellemc.sonic/blob/master/plugins/modules/sonic_config.py)|Manage configuration of the Management Framework CLI on remote devices running Enterprise SONiC
[**sonic_api.py**](https://github.com/ansible-collections/dellemc.sonic/blob/master/plugins/modules/sonic_api.py)|Perform REST operations on remote devices running Enterprise SONiC

Playbooks
---------

The playbooks directory includes sample playbooks that show how to use the SONiC collections for provisioning devices running Enterprise SONiC Distribution by Dell Technologies.

Installation
=======================

Install the latest version of the SONiC collection from Ansible Galaxy.

      ansible-galaxy collection install dellemc.sonic

To install a specific version, specify a version range identifier. For example, to install the most recent version that is greater than or equal to 1.0.0 and less than 2.0.0:

      ansible-galaxy collection install 'dellemc.sonic:>=1.0.0,<2.0.0'

Sample playbook to configure VLAN entry and show VLAN status
============================================================

    ---

    - name: "Test Management Framework CLI show commands on SONiC"
      hosts: sonic
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

Sample playbook to configure VLAN using SONiC REST API
======================================================

    ---

    - name: "To configure VLAN using SONiC REST API"
      hosts: sonic
      gather_facts: no
      connection: httpapi
      collections:
        - dellemc.sonic
      tasks:
        - name: Perform "PUT" operation to add VLAN network instance
          sonic_api:
            url: data/openconfig-network-instance:network-instances/network-instance=Vlan100
            method: "PUT"
            body: {"openconfig-network-instance:network-instance": [{"name": "Vlan100","config": {"name": "Vlan100"}}]}
            status_code: 204
        - name: Perform "GET" operation to view VLAN network instance
          sonic_api:
            url: data/openconfig-network-instance:network-instances/network-instance=Vlan100
            method: "GET"
            status_code: 200
          register: api_op

Sample playbook to configure VLAN, l2_interfaces, and l3_interfaces using SONiC resource module
==============================================================================================

    ---

    - name: "To configure interfaces using SONiC resources modules"
      hosts: sonic
      gather_facts: False
      connection: httpapi
      collections:
        - dellemc.sonic
      tasks:
       - name: "Configuring vlans"
         sonic_vlans:
            config:
             - vlan_id: 701
             - vlan_id: 702
             - vlan_id: 703
             - vlan_id: 704
            state: merged
         register: sonic_vlans_creation_output
       - name: "Configuring l2_interfaces"
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
       - name: "Configuring l3_interfaces"
         sonic_l3_interfaces:
           config:
            - name: Ethernet20
              ipv4:
                - address: 8.1.1.1/16
              ipv6:
                - address: 3333::1/16
           state: merged
         register: sonic_l3_interfaces_configuration_output

## Sample inventory.yaml
    [sonic]
    sonic_sw1 ansible_host=100.104.28.119 ansible_network_os=dellemc.sonic.sonic

(c) 2020 Dell Inc. or its subsidiaries. All rights reserved.
