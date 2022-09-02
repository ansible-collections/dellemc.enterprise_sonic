======================================
Dellemc.Enterprise_Sonic Release Notes
======================================

.. contents:: Topics


v2.0.0
======

Release Summary
---------------

This release provides Dell SONiC Enterprise Ansible Collection support for SONiC 4.x images. It is the first release for the 2.x branch of the collection. Subsequent enhancements for support of SONiC 4.x images will also be provided as needed on the 2.x branch. This release also contains bugfixes and enhancements to supplement the Ansible functionality provided previously for SONiC 3.x images. The changelog describes changes made to the modules and plugins included in this collection since release 1.1.0.


Major Changes
-------------

- Added 'static_routes' module to collection (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/82).
- Added a resource module for NTP support (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/99).
- Added a resource module for support of prefix lists (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/100).
- Updated backend REST API request formats in all applicable modules for compatibility with SONiC 4.x openconfig YANG compliant REST APIs. (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/53)

Minor Changes
-------------

- Added an execution-environment.yml file to the "meta" directory to enable use of Ansible execution environment infrastructure (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/88).
- bgp_af - Added support for BGP options to configure usage and advertisement of vxlan primary IP address related attributes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/62).
- bgp_as_paths - updated module examples with 'permit' attribute (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/102)
- bgp_neighbors - Add BGP peer group support for multiple attributes. The added attributes correspond to the same set of attributes added for BGP neighbors with PR 72 (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/81).
- bgp_neighbors - Add support for multiple attributes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/72).
- bgp_neighbors - add an auth_pwd dictionary and nbr_description attribute to the argspec (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/67).
- bgp_neighbors - added prefix-list related peer-group attributes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/101).
- bgp_neighbors_af - added prefix-list related neighbor attributes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/101).
- playbook - updated examples to reflect module changes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/102)
- sonic_vxlans - Add configuration capability for the primary IP address of a vxlan vtep to facilitate vxlan path redundundancy (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/58).
- vlans - Added support for the vlan "description" attribute (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/98).
- workflow - Added stable-2.13 to the sanity test matrix (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/90).

Breaking Changes / Porting Guide
--------------------------------

- bgp_af - Add the route_advertise_list dictionary to the argspec to replace the deleted, obsolete advertise_prefix attribute used for SONiC 3.x images on the 1.x branch of this collection. This change corresponds to a SONiC 4.0 OC YANG REST compliance change for the BGP AF REST API. It enables specification of a route map in conjunction with each route advertisement prefix (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/63).
- bgp_af - remove the obsolete 'advertise_prefix' attribute from argspec and config code. This and subsequent co-req replacement with the new route advertise list argument structure require corresponding changes in playbooks previoulsly used for configuring route advertise prefixes for SONiC 3.x images. (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/60)
- bgp_neighbors - Replace the previously defined standalone "bfd" attribute with a bfd dictionary containing multiple attributes. This change corresponds to the revised SONiC 4.x implementation of OC YANG compatible REST APIs. Playbooks previously using the bfd attributes for SONiC 3.x images must be modified for useon SONiC 4.0 images to use the new definition for the bfd attribute argspec structure (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/72).
- bgp_neighbors - Replace, for BGP peer groups, the previously defined standalone "bfd" attribute with a bfd dictionary containing multiple attributes. This change corresponds to the revised SONiC 4.x implementation of OC YANG compatible REST APIs. Playbooks previously using the bfd attributes for SONiC 3.x images must be modified for useon SONiC 4.0 images to use the new definition for the bfd attribute argspec structure (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/81).

Bugfixes
--------

- Fixed regression test bugs in multiple modules (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/103).
- Fixed regression test sequencing and other regression test bugs in multiple modules (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/85).
- aaa - Fixed a bug in facts gathering by providing required conditional branching (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/90)
- aaa - Modify regression test sequencing to enable correct testing of the functionality for this module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/78).
- bgp_neighbors - remove string conversion of timer attributes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/60)
- port_breakout - Fixed a bug in formulation of port breakout REST APIs (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/88).
- sonic - Fix a bug in handling of interface names in standard interface naming mode (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/103).
- sonic_command - Fix bugs in handling of CLI commands involving a prompt and answer sequence (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/76/files).
- users - Fixed a bug in facts gathering (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/90).
- vxlan - update Vxlan test cases to comply with SONiC behavior (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/105).

New Modules
-----------

- dellemc.enterprise_sonic.sonic_ntp - Manage NTP configuration on SONiC.
- dellemc.enterprise_sonic.sonic_prefix_lists - prefix list configuration handling for SONiC
- dellemc.enterprise_sonic.sonic_static_routes - Manage static routes configuration on SONiC

v1.1.0
======

New Modules
-----------

- dellemc.enterprise_sonic.sonic_aaa - AAA resource module.
- dellemc.enterprise_sonic.sonic_radius_server - RADIUS resource module.
- dellemc.enterprise_sonic.sonic_system - SYSTEM resource module.
- dellemc.enterprise_sonic.sonic_tacacs_server - TACACS Server resource module.

v1.0.0
======

New Plugins
-----------

Cliconf
~~~~~~~

- dellemc.enterprise_sonic.sonic - Use Ansible CLICONF to run commands on Enterprise SONiC.

Httpapi
~~~~~~~

- dellemc.enterprise_sonic.sonic - Use Ansible HTTPAPI to run commands on Enterprise SONiC.

New Modules
-----------

- dellemc.enterprise_sonic.sonic_api - Perform REST operations through the Management Framework REST API.
- dellemc.enterprise_sonic.sonic_bgp - BGP resource module.
- dellemc.enterprise_sonic.sonic_bgp_af - BGP AF resource module.
- dellemc.enterprise_sonic.sonic_bgp_as_paths - BGP AS path resource module.
- dellemc.enterprise_sonic.sonic_bgp_communities - BGP communities resource module.
- dellemc.enterprise_sonic.sonic_bgp_ext_communities - BGP Ext communities resource module.
- dellemc.enterprise_sonic.sonic_bgp_neighbors - BGP neighbors resource module.
- dellemc.enterprise_sonic.sonic_bgp_neighbors_af - BGP neighbors AF resource module.
- dellemc.enterprise_sonic.sonic_command - Run commands through Management Framework CLI.
- dellemc.enterprise_sonic.sonic_config - Manage configuration through the Management Framework CLI.
- dellemc.enterprise_sonic.sonic_interfaces - Interface resource module.
- dellemc.enterprise_sonic.sonic_l2_interfaces - Layer 2 interface resource module.
- dellemc.enterprise_sonic.sonic_l3_interfaces - Layer 3 interface resource module.
- dellemc.enterprise_sonic.sonic_lag_interfaces - Link aggregation (LAG) resource module.
- dellemc.enterprise_sonic.sonic_mclag - MCLAG resource module.
- dellemc.enterprise_sonic.sonic_port_breakout - port breakout resource module.
- dellemc.enterprise_sonic.sonic_users - USERS resource module.
- dellemc.enterprise_sonic.sonic_vlans - VLAN resource module.
- dellemc.enterprise_sonic.sonic_vrfs - VRF resource module.
- dellemc.enterprise_sonic.sonic_vxlans - VxLAN EVPN resource module.
