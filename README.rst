The Ansible collection for Dell EMC Networking SONiC
----------------------------------------------------

Collection contents
-------------------

The sonic ansible collection includes the Ansible modules, plugins and
sample playbooks that can be used to work on SONiC switches. It also
includes documents that illustrates, how the collection can be used.

Ansible modules
~~~~~~~~~~~~~~~

Following Ansible modules are part of the sonic collection

***sonic\_command.py*** Run commands on remote devices running SONiC

***sonic\_config.py*** Manage configuration sections on remote devices
running SONiC

***sonic\_api.py*** Perform REST operations on remote devices running
SONiC

Playbooks
~~~~~~~~~

The playbooks directory includes sample playbooks that illustrate the
usage of sonic collections for provisioning device running SONiC.

Collection Installation
-----------------------

Install the latest version of sonic collection from Ansible Galaxy using
command, ***ansible-galaxy collection install
dellemc\_networking.sonic***

To install a specific version, a version range identifier shall be
specified. For example, to install the most recent version that is
greater than or equal to 1.0.0 and less than 2.0.0: ***ansible-galaxy
collection install 'dellemc\_networking.sonic:>=1.0.0,<2.0.0'***

Sample Playbook to show interface status
----------------------------------------

::

    ---

    - name: "Test sonic CLI"
      hosts: spine1
      gather_facts: no
      connection: network_cli
      collections:
        - dellemc_networking.sonic
      tasks:

        - name: Test sonic single command
          sonic_command:
            commands: 'show interface status'
          register: cmd_op

Sample Playbook to configure vlan entry
---------------------------------------

::

    ---

    - name: "Test sonic config "
      hosts: spine1
      gather_facts: no
      connection: network_cli
      collections:
        - dellemc_networking.sonic
      tasks:

        - name: Add vlan entry
          sonic_config:
            commands: ['interface Vlan 200','exit']
            save: yes
          register: config_op

Sample Playbook to use api module
---------------------------------

::

    ---

    - name: "Test sonic api "
      hosts: spine1
      gather_facts: no
      connection: httpapi
      collections:
        - dellemc_networking.sonic
      tasks:
        - name: Perform "PUT" operation to add vlan network instance
          sonic_api:
            url: data/openconfig-network-instance:network-instances/network-instance=Vlan100
            method: "PUT"
            body: {"openconfig-network-instance:network-instance": [{"name": "Vlan100","config": {"name": "Vlan100"}}]}
            status_code: 204
        - name: Perform "GET" operation to view vlan network instance
          sonic_api:
            url: data/openconfig-network-instance:network-instances/network-instance=Vlan100
            method: "GET"
            status_code: 200
          register: api_op

.. note:: 
    Environment variable ANSIBLE\_NETWORK\_GROUP\_MODULES
    should be set to 'sonic' for using sonic-collections in playbook to
    configure cli using 'src' option in sonic\_config module.

