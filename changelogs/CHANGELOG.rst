=================================================================================
Ansible Network Collection for Enterprise SONiC Distribution by Dell Technologies
=================================================================================

.. contents:: Topics

v1.0.0
======

New Plugins
-----------

CLICONF
~~~~~~~

- sonic - Use Ansible CLICONF to run commands on Enterprise SONiC.

HTTPAPI
~~~~~~~

- sonic - Use Ansible HTTPAPI to run commands on Enterprise SONiC.


New Modules
-----------

- sonic_command - Run commands through Management Framework CLI.
- sonic_config - Manage configuration through the Management Framework CLI.
- sonic_api - Perform REST operations through the Management Framework REST API.

New Resource modules
--------------------

- sonic_interfaces - Interface resource module
- sonic_l2_interfaces - Layer 2 interface resource module
- sonic_l3_interfaces - Layer 3 interface resource module
- sonic_lag_interfaces - Link aggregation (LAG) resource module
- sonic_vlans - VLAN resource module
- sonic_bgp - BGP configuration
- sonic_bgp_af - BGP AF configuration
- sonic_bgp_neighbors - BGP neighbors configuration
- sonic_bgp_neighbors_af - BGP neighbors AF configuration
- sonic_bgp_as_paths - BGP AS path configuration
- sonic_bgp_communities - BGP communities configuration
- sonic_bgp_ext_communities - BGP Ext communities configuration
- sonic_mclag - MLAG configuration
- sonic_vrfs - VRF configuration
- sonic_vxlan - VxLAN EVPN configuration

(c) 2020 Dell Inc. or its subsidiaries. All Rights Reserved.