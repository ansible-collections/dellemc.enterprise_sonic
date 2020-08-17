=================================================================================
Ansible Network Collection for Enterprise SONiC Distribution by Dell Technologies
=================================================================================

.. contents:: Topics

v1.0.1
======

Release Summary
---------------

Added changelog.

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

\(c) 2020 Dell Inc. or its subsidiaries. All Rights Reserved.
