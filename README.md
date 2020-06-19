The Ansible collection for is Dell EMC Open Networking Powered by SONiC
=======================================================================

Collection contents
===================

The SONiC Ansible collection includes the Ansible modules, plugins and sample playbooks that can be used to work on Dell EMC PowerSwitch platforms running Dell EMC Open Networking Powered by SONiC. It also includes documents that illustrate how the collection can be used. This is the Beta version tested on Dell EMC Open Networking Powered by SONiC version 3.0.2

Ansible modules
---------------

Following Ansible modules are part of the sonic collection

**sonic\_command.py** Run commands from Management Framework CLI on remote devices running SONiC

**sonic\_config.py** Manage configuration sections of the Management Framework CLI on remote devices running SONiC

**sonic\_api.py** Perform REsT operations on remote devices running SONiC

Playbooks
---------

The playbooks directory includes sample playbooks that illustrate the usage of SONiC collections for provisioning devices running Dell EMC Open Networking Powered by SONiC

Collection Installation
=======================

Install the latest version of sonic collection from Ansible Galaxy using command
      
      ansible-galaxy collection install dellemc.sonic

To install a specific version, a version range identifier shall be specified. For example, to install the most recent version that is greater than or equal to 1.0.0 and less than 2.0.0

      ansible-galaxy collection install 'dellemc.sonic:\>=1.0.0,\<2.0.0'

Sample Playbook to show interface status
========================================

    ---

    - name: "Test Management Framework CLI show commands on SONiC"
      hosts: spine1
      gather_facts: no
      connection: network_cli
      collections:
        - dellemc.sonic
      tasks:
        - name: Test SONiC single command
          sonic_command:
            commands: 'show interface status'
          register: cmd_op

Sample Playbook to configure VLAN entry
=======================================

    ---

    - name: "Test Management Framework CLI configuration commands on SONiC"
      hosts: spine1
      gather_facts: no
      connection: network_cli
      collections:
        - dellemc.sonic
      tasks:

        - name: Add VLAN entry
          sonic_config:
            commands: ['interface Vlan 200','exit']
            save: yes
          register: config_op

Sample Playbook to configure VLAN using SONiC REsT API
======================================================

    ---

    - name: "To configure VLAN using SONiC REsT API"
      hosts: spine1
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

**Note**

Environment variable ANSIBLE_NETWORK_GROUP_MODULES should be set to 'sonic' for using the SONiC collection in playbooks to configure CLI using 'src' option in sonic_config module.
