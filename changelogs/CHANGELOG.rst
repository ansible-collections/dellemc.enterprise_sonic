===============================================================================================
Ansible Network Collection for Enterprise SONiC Distribution by Dell Technologies Release Notes
===============================================================================================

.. contents:: Topics


v1.1.2
======

Release Summary
---------------

This is a bugfix release for the ``dellemc.enterprise_sonic``
collection on 2020-06-02. The changelog describes changes made to the modules
and plugins included in this collection since release 1.1.1.


Bugfixes
--------

- utils - Fixed regex expression in sonic.py to handle standard interface naming in port breakout mode  (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/110).

v1.1.1
======

Release Summary
---------------

This is a minor enhancement and bugfix release for the ``dellemc.enterprise_sonic``
collection on 2020-06-02. The changelog describes changes made to the modules
and plugins included in this collection since release 1.1.0.


Minor Changes
-------------

- README - describe branch naming conventions for the "main" and "1.x" branches (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/54).
- README - describe the mapping of SONiC release versions to the corresponding branch and release names in the Dell SONiC Enterprise Ansible collection. (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/84).
- bgp_as_paths - Add a 'permit/deny' attribute (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/52).
- bgp_neighbors - add 'password' and 'description' attributes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/69).
- meta - add the newly required execution_environment.yml file to the 'meta' directory (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/89).
- port_breakout - modify port numbers to match commonly available breakout ports (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/89).
- workflows - add stable-2.12 to the CI test matrix (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/51).
- workflows - add stable-2.13 to the CI test matrix (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/91).

Bugfixes
--------

- Fixes incorrect grouping of parameters to be used for invocation of the "send_command" API for sending commands to a device. (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/71).
- aaa - fix a logic mistake in validating authentication data (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/52).
- aaa - modify a 'delete' test case to eliminate a subsequent idempotency failure for a 'merge' test case restoring the deleted attribute. The attribute that was being used for the test case had a non-idempotent effect in the SONiC switch functional code. This did not allow verification of the correct idempotency logic in the Ansible handling of the attribute 'delete' and 'restore' functionality. (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/80).
- bgp - removed unnecessary brackets in a configuration handling instruction (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/52).
- bgp_neighbors - add a 'maxsplit' value in facts handling (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/52).
- bgp_neighbors - removed unnecessary brackets in configuration handling instructions (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/52).
- radius_server - add a missing 'get' in configuration handling (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/52).
- system - delete an initial test case requiring 'changed' state for deletion of final configuration attributes assuming 'leftover' configuration from previous execution. Replace this initial test case with cleanup of any residual state with no assumption of leftover residual state. Do the final deletion of configuration at the end of the test instead of at the beginning to retain verification that the deletion works correctly (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/87).
- tacacs_server - correct an argument spelling error in facts handling (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/52).

v1.1.0
======

New Modules
-----------

- sonic_aaa - AAA resource module.
- sonic_radius_server - RADIUS resource module.
- sonic_system - SYSTEM resource module.
- sonic_tacacs_server - TACACS Server resource module.

v1.0.0
======

New Plugins
-----------

Cliconf
~~~~~~~

- sonic - Use Ansible CLICONF to run commands on Enterprise SONiC.

Httpapi
~~~~~~~

- sonic - Use Ansible HTTPAPI to run commands on Enterprise SONiC.

New Modules
-----------

- sonic_api - Perform REST operations through the Management Framework REST API.
- sonic_bgp - BGP resource module.
- sonic_bgp_af - BGP AF resource module.
- sonic_bgp_as_paths - BGP AS path resource module.
- sonic_bgp_communities - BGP communities resource module.
- sonic_bgp_ext_communities - BGP Ext communities resource module.
- sonic_bgp_neighbors - BGP neighbors resource module.
- sonic_bgp_neighbors_af - BGP neighbors AF resource module.
- sonic_command - Run commands through Management Framework CLI.
- sonic_config - Manage configuration through the Management Framework CLI.
- sonic_interfaces - Interface resource module.
- sonic_l2_interfaces - Layer 2 interface resource module.
- sonic_l3_interfaces - Layer 3 interface resource module.
- sonic_lag_interfaces - Link aggregation (LAG) resource module.
- sonic_mclag - MCLAG resource module.
- sonic_port_breakout - port breakout resource module.
- sonic_users - USERS resource module.
- sonic_vlans - VLAN resource module.
- sonic_vrfs - VRF resource module.
- sonic_vxlans - VxLAN EVPN resource module.
