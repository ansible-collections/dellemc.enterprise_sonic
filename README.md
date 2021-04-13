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
[**sonic_command**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/master/plugins/modules/sonic_command.py)|Run commands through the Management Framework CLI|network_cli
[**sonic_config**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/master/plugins/modules/sonic_config.py)|Manage configuration through the Management Framework CLI|network_cli
[**sonic_api**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/master/plugins/modules/sonic_api.py)|Perform REST operations through the Management Framework REST API|httpapi

Collection network resource modules
-----------------------------------
Listed are the SONiC Ansible network resource modules which need ***httpapi*** as the connection type. Supported operations are ***merged*** and ***deleted***.

| **Interfaces** | **BGP** | **VRF** | **Users** |
| -------------- | ------- | ------- | ------- |
| [**sonic_interfaces**](https://github.com/ansible-collections/dellemc.enterprise_sonic/blob/master/plugins/modules/sonic_interfaces.py)|[**sonic_bgp**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/plugins/modules/sonic_bgp.py)| [**sonic_vrfs**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/plugins/modules/sonic_vrfs.py)|[**sonic_users**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/plugins/modules/sonic_users.py)|
| [**sonic_l2_interfaces**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/plugins/modules/sonic_l2_interfaces.py)| [**sonic_bgp_af**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/plugins/modules/sonic_bgp_af.py)| **MCLAG** | **AAA** |
| [**sonic_l3_interfaces**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/plugins/modules/sonic_l3_interfaces.py) |[**sonic_bgp_as_paths**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/plugins/modules/sonic_bgp_as_paths.py)| [**sonic_mclag**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/plugins/modules/sonic_mclag.py)| [**sonic_aaa**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/plugins/modules/sonic_aaa.py)|
|**Port channel**|[**sonic_bgp_communities**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/plugins/modules/sonic_bgp_communities.py)| **VxLANs** |[**sonic_tacacs_server**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/plugins/modules/sonic_bgp_tacacs_server.py)|
|[**sonic_lag_interfaces**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/plugins/modules/sonic_lag_interfaces.py)|[**sonic_bgp_ext_communities**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/plugins/modules/sonic_bgp_ext_communities.py)| [**sonic_vxlans**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/plugins/modules/sonic_vxlans.py)|[**sonic_radius_server**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/plugins/modules/sonic_bgp_radius_server.py)|
|**VLANs**|[**sonic_bgp_neighbors**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/plugins/modules/sonic_bgp_neighbors.py)| **Port breakout** | **System** |
|[**sonic_vlans**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/plugins/modules/sonic_vlans.py)|[**sonic_bgp_neighbors_af**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/plugins/modules/sonic_bgp_neighbors_af.py)|[**sonic_port_breakout**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/plugins/modules/sonic_port_breakout.py) |[**sonic_system**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/plugins/modules/sonic_system.py) |

Sample use case playbooks
-------------------------
The playbooks directory includes this sample playbook that show end-to-end use cases.

Name | Description
--- | ---
[**BGP Layer 3 fabric**](https://github.com/ansible-collections/dellemc.enterprise_sonic/tree/master/playbooks/bgp_l3_fabric)|Example playbook to build a Layer 3 leaf-spine fabric

Version compatibility
----------------------
* Recommended Ansible version 2.10 or higher
* Enterprise SONiC Distribution by Dell Technologies version 3.1 or higher
* Recommended Python 3.5 or higher, or Python 2.7


> **NOTE**: Community SONiC versions that include the Management Framework container should work as well, however, this collection has not been tested nor validated 
        with community versions and is not supported.

Installation of Ansible 2.10+
-----------------------------
##### Dependencies for Ansible Enterprise SONiC collection

      pip3 install paramiko>=2.7
      pip3 install jinja2>=2.8
      pip3 install ansible-base
      
      
Installation of Ansible 2.9
---------------------------
##### Dependencies for Ansible Enterprise SONiC collection

      pip3 install paramiko>=2.7
      pip3 install jinja2>=2.8
      pip3 install ansible
      
##### Setting Enviroment Varibles

To use the Enterprise SONiC collection in Ansible 2.9, it is required to add one of the two available environment variables.

Option 1: Add the environment variable while running the playbook.


      ANSIBLE_NETWORK_GROUP_MODULES=sonic ansible-playbook sample_playbook.yaml -i inventory.yaml
      
      
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
      collections:
        - dellemc.enterprise_sonic
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

***sonic_httpapi.yaml***

    ---

    - name: SONiC Management Framework REST API examples
      hosts: sonic_switches
      gather_facts: no
      connection: httpapi
      collections:
        - dellemc.enterprise_sonic
      tasks:
        - name: Perform PUT operation to add a VLAN network instance
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

***sonic_resource_modules.yaml***

    ---

    - name: VLANs, Layer 2 and Layer 3 interfaces configuration using Enterprise SONiC resource modules
      hosts: sonic_switches
      gather_facts: no
      connection: httpapi
      collections:
        - dellemc.enterprise_sonic
      tasks:
       - name: Configure VLANs
         sonic_vlans:
            config:
             - vlan_id: 701
             - vlan_id: 702
             - vlan_id: 703
             - vlan_id: 704
            state: merged
         register: sonic_vlans_output
       - name: Configure Layer 2 interfaces
         sonic_l2_interfaces:
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
         sonic_l3_interfaces:
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
    ansible_pass: xxxx
    ansible_network_os: dellemc.enterprise_sonic.sonic

    # Additional parameters for connection type httpapi:
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false

***inventory.yaml***

    [sonic_sw1]
    sonic_sw1 ansible_host=100.104.28.119

    [sonic_sw2]
    sonic_sw2 ansible_host=100.104.28.120

    [sonic_switches:children]
    sonic_sw1
    sonic_sw2

Releasing, Versioning and Deprecation
-------------------------------------

This collection follows [Semantic Versioning](https://semver.org/). More details on versioning can be found [in the Ansible docs](https://docs.ansible.com/ansible/latest/dev_guide/developing_collections.html#collection-versions).

We plan to regularly release new minor or bugfix versions once new features or bugfixes have been implemented.

Releasing the current major version happens from the `main` branch. We will create a `stable-1` branch for 1.x.y versions once we start working on a 2.0.0 release, to allow backporting bugfixes and features from the 2.0.0 branch (`main`) to `stable-1`. A `stable-2` branch will be created once we work on a 3.0.0 release, and so on.

We currently are not planning any deprecations or new major releases like 2.0.0 containing backwards incompatible changes. If backwards incompatible changes are needed, we plan to deprecate the old behavior as early as possible. We also plan to backport at least bugfixes for the old major version for some time after releasing a new major version. We will not block community members from backporting other bugfixes and features from the latest stable version to older release branches, under the condition that these backports are of reasonable quality.

Code of Conduct
---------------

This repository adheres to the [Ansible Community code of conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)

(c) 2020-2021 Dell Inc. or its subsidiaries. All Rights Reserved.
