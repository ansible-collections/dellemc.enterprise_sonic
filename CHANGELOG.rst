=======================================
Dellemc.Enterprise\_Sonic Release Notes
=======================================

.. contents:: Topics

v2.5.1
======

Release Summary
---------------

| Release Date: 2024-0917
|
| This release provides bug fixes for problems present in the 2.5.0 release of the Dell
| Enterprise SONiC Ansible Collection. The most critical of the fixes included in this
| release is a fix to enable downward compatibility of the "sonic_system" resource module
| for SONiC releases earlier than SONiC release 4.4.0. Also included are fixes to enable
| correct handling for "Connection Error" exceptions and updating of documentation links
| for the README file in accordance with a new location for the module documentation files.
|
| The changelog describes changes made to the modules included in this collection since
| release 2.5.0.

Bugfixes
--------

- ConnectionError - Add the needed import of the Ansible ConnectionError exception class for all files where it was previously missing. (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/445).
- Update regex search expression for 'not found' error message in httpapi/sonic.py 'edit_config' method (https://github.com/ansible-collection/dellemc.enterprise_sonic/pull/443).
- sonic_system - Catch the ConnectionError exception caused by unconditional fetching of auditd and ip loadshare hash algorithm configuration, and return empty configuration instead of allowing the uncaught exception to abort all "system" operations on SONiC images older than version 4.4.0 (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/441).

v2.5.0
======

Release Summary
---------------

| Release Date: 2024-0812
|
| This release provides enhanced Dell Enterprise SONiC Ansible Collection support for SONiC 4.x images.
| In addition to new resource modules to support previously existing functionality, it provides
| support for several new features released in SONiC releases 4.1, 4.2, and 4.4.
| It also provides bug fixes and enhancements for support of features that were initially introduced
| in previous Enterprise SONiC Ansible releases. The changelog describes changes made to the modules
| included in this collection since release 2.0.0.
|
| Additional details are described below.
| 1) Update the "requires_ansible" version in the meta/runtime.yml file for this collection
| to the oldest supported version of ansible-core. (This was recently changed by Redhat/Ansible
| to version "2.15.0".)
| 2) Update the list of resource modules in the README file to include all currently available
| resource modules for this collection.

Minor Changes
-------------

- bgp_af - Add support for 'import vrf' commands (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/351).
- sonic_bfd - Add playbook check and diff modes support for bfd module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/346).
- sonic_bgp - Add playbook check and diff modes support for bgp module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/350).
- sonic_bgp - Add support BGP Asn Notation (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/417).
- sonic_bgp - Fix GitHub issue# 416 (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/418).
- sonic_bgp_af - Add playbook check and diff modes support for bgp_af module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/350).
- sonic_bgp_af - Add support for BGP Asn Notation (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/417).
- sonic_bgp_af - Add support for aggregate address configuration(https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/398).
- sonic_bgp_af - Update replaced state handling (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/400)
- sonic_bgp_as_paths - Add playbook check and diff modes support for bgp_as_paths module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/350).
- sonic_bgp_communities - Add playbook check and diff modes support for bgp_communities module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/350).
- sonic_bgp_ext_communities - Add playbook check and diff modes support for bgp_ext_communities module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/350).
- sonic_bgp_neighbors - Add playbook check and diff modes support for bgp_neighbors module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/360).
- sonic_bgp_neighbors - Add support for BGP Asn Notation (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/417).
- sonic_bgp_neighbors - Add support for replaced and overridden states (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/335).
- sonic_bgp_neighbors - Add support for replaced and overridden states (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/336).
- sonic_bgp_neighbors - Add support for the "fabric_external" option (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/336).
- sonic_bgp_neighbors_af - Add playbook check and diff modes support for bgp_neighbors_af module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/360).
- sonic_bgp_neighbors_af - Add support for BGP Asn Notation (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/417).
- sonic_copp - Add playbook check and diff modes support for copp module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/346).
- sonic_dhcp_relay - Add playbook check and diff modes support for dhcp_relay module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/346).
- sonic_dhcp_snooping - Add playbook check and diff modes support for dhcp_snooping module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/346).
- sonic_interfaces - Add description, enabled option support for Loopback interfaces (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/364).
- sonic_interfaces - Fix GitHub issue 357 - set proper default value when deleted (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/366).
- sonic_interfaces - Update replaced state handling (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/364).
- sonic_l3_interfaces - Add playbook check and diff modes support for l3_interfaces module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/328).
- sonic_l3_interfaces - Add support for USGv6R1 related features (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/374).
- sonic_l3_interfaces - Fix IPv6 default dad configuration handling (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/428).
- sonic_lag_interfaces - Add evpn ethernet-segment support for LAG interfaces (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/403).
- sonic_lldp_global - Add playbook check and diff modes support for lldp_global module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/338).
- sonic_logging - Add support for protocol option in logging module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/317).
- sonic_mac - Add playbook check and diff modes support for mac module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/338).
- sonic_mclag - Add playbook check and diff modes support for mclag module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/337).
- sonic_mclag - Enable session-vrf command support in mclag(https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/299).
- sonic_port_breakout - Add playbook check and diff modes support for port_breakout module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/337).
- sonic_port_group - Make error message for port group facts gathering more descriptive (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/396).
- sonic_prefix_lists - Add playbook check and diff modes support for prefix_lists module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/331).
- sonic_qos_maps - Comment out PFC priority group map tests cases (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/395).
- sonic_qos_scheduler - Update states implementation (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/373).
- sonic_route_maps - Add UT for route maps module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/384).
- sonic_route_maps - Add playbook check and diff modes support for route_maps module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/331).
- sonic_route_maps - Add support for BGP Asn Notation (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/417).
- sonic_route_maps - Add support for the 'set tag' option and synchronize module documentation with argspec and model (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/413).
- sonic_stp - Add playbook check and diff modes support for stp module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/338).
- sonic_system - Add support for 'standard_extended' interface-naming mode (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/352).
- sonic_system - Add support for configuring auto-breakout feature (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/342).
- sonic_system - Adding Versatile Hash feature.(https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/401).
- sonic_system - Enable auditd command support(https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/405).
- sonic_system - Update replaced state handling (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/388).
- sonic_vxlan - Fix GitHub issue 376 - Change vxlan module get_fact function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/393).
- sonic_vxlans - Add playbook check and diff modes support for vxlans module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/337).
- sonic_vxlans - Add support for the "external_ip" vxlan option (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/330).

Bugfixes
--------

- sonic_bfd - Fix BFD states implementation bug (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/383).
- sonic_bgp_neighbors - Fix issues with deleted state (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/335).
- sonic_copp - Fix CoPP states implementation bug (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/381).
- sonic_interfaces - Fix exception when gathering facts (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/377).
- sonic_interfaces - Fix replaced and overridden state handling for Loopback interfaces (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/364).
- sonic_l2_interfaces - Fix exception when gathering facts (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/410).
- sonic_l3_interfaces - Fix replaced state handling (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/431).
- sonic_mac - Fix MAC states implementation bug (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/383).
- sonic_prefix_lists - Fix idempotency failure (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/354).
- sonic_prefix_lists - Fix replaced state handling (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/354).
- sonic_qos_pfc - Add back accidentally deleted line of code  (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/391).
- sonic_static_routes - Fix static routes states implementation bug (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/383).
- sonic_vlans - Fix exception when gathering facts (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/377).

New Modules
-----------

- dellemc.enterprise_sonic.sonic_ldap - Configure global LDAP server settings on SONiC.
- dellemc.enterprise_sonic.sonic_login_lockout - Manage Global Login Lockout configurations on SONiC.
- dellemc.enterprise_sonic.sonic_mgmt_servers - Manage management servers configuration on SONiC.
- dellemc.enterprise_sonic.sonic_ospf_area - configure OSPF area settings on SONiC.
- dellemc.enterprise_sonic.sonic_ospfv2 - Configure global OSPFv2 protocol settings on SONiC.
- dellemc.enterprise_sonic.sonic_ospfv2_interfaces - Configure OSPFv2 interface mode protocol settings on SONiC.
- dellemc.enterprise_sonic.sonic_pim_global - Manage global PIM configurations on SONiC.
- dellemc.enterprise_sonic.sonic_pim_interfaces - Manage interface-specific PIM configurations on SONiC.
- dellemc.enterprise_sonic.sonic_poe - Manage PoE configuration on SONiC.
- dellemc.enterprise_sonic.sonic_qos_buffer - Manage QoS buffer configuration on SONiC.
- dellemc.enterprise_sonic.sonic_qos_interfaces - Manage QoS interfaces configuration on SONiC.
- dellemc.enterprise_sonic.sonic_qos_maps - Manage QoS maps configuration on SONiC.
- dellemc.enterprise_sonic.sonic_qos_pfc - Manage QoS PFC configuration on SONiC.
- dellemc.enterprise_sonic.sonic_qos_scheduler - Manage QoS scheduler configuration on SONiC.
- dellemc.enterprise_sonic.sonic_qos_wred - Manage QoS WRED profiles configuration on SONiC.
- dellemc.enterprise_sonic.sonic_roce - Manage RoCE QoS configuration on SONiC.
- dellemc.enterprise_sonic.sonic_sflow - configure sflow settings on SONiC.
- dellemc.enterprise_sonic.sonic_vrrp - Configure VRRP protocol settings on SONiC.

v2.4.0
======

Release Summary
---------------

| Release Date: 2024-0108
| This release provides an Ansible compliance change required on top of the changes included in
| the 2.3.0 release of the enterprise_sonic Ansible network resource module collection.
| It addresses an issue raised by the Ansible core team with the content of the 2.3.0 release,
| and provides accompanying documentation changes in the README file. Additional details are
| described below.
| 1) Update the "requires_ansible" version in the meta/runtime.yml file for this collection
| to the oldest supported version of ansible-core. (This was recently changed by Redhat/Ansible
| to version "2.14.0".)
| 2) Update the README file "Recommended version" values for Ansible and Python in accordance
| with the previous change item to modify the oldest supported version of ansible-core which,
| in turn, requires a Python version >= "3.9".
| 3) Update the list of resource modules in the README file to include all currently available
| resource modules for this collection.

Bugfixes
--------

- requirements - Update requires_ansible version in meta/runtime.yml to the oldest supported version (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/321).

v2.3.0
======

Release Summary
---------------

| Release Date: 2024-0103
| This release provides the functionality enhancements listed below, along with fixes for
| problems found in regression testing or reported by users. The main functionality enhancements
| provided are the following items.
| 1) Complete the support for "replaced" and "overridden" state handling for all resource modules except for the bgp_neighbors and bgp_neighbors_af modules.
| With this release, the required support has been added for any resource modules that were not
| provided with this support for the 2.1.0 release with the two exceptions noted above.
| 2) Provide initial support for the "--check" and "--diff" mode options for playbook execution. This
| release provides the common utility support for these options for use by all resource modules.
| It also provides the specific resource module changes required for implementation of the
| functionality in many of the existing resource modules. (The "--check" and "--diff" mode support
| for the remaining resource modules is planned for inclusion in the next release.)
| 3) New resource modules for "Public Key Infrastructure", STP, and DHCP Snooping.
| 4) Support for "ranges" of vlans (e.g '2-100') in tasks for the mclag resource module.
| Please refer to the "CHANGELOG.rst" file at the top directory level of this repo for additional
| details on the contents of this release.

Minor Changes
-------------

- sonic_aaa - Add support for playbook check and diff modes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/304).
- sonic_aaa - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- sonic_acl_interfaces - Add support for playbook check and diff modes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/306).
- sonic_acl_interfaces - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- sonic_bgp_as_paths - Add support for replaced and overridden states (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/290).
- sonic_bgp_communities - Add support for replaced and overridden states (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/251).
- sonic_bgp_ext_communities - Add support for replaced and overridden states (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/252).
- sonic_interfaces - Add support for playbook check and diff modes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/301).
- sonic_interfaces - Add support for replaced and overridden states (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/314).
- sonic_interfaces - Change deleted design for interfaces module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/310).
- sonic_interfaces - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- sonic_ip_neighbor - Add support for playbook check and diff modes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/285).
- sonic_ip_neighbor - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- sonic_l2_acls - Add support for playbook check and diff modes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/306).
- sonic_l2_acls - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- sonic_l2_interfaces - Add support for playbook check and diff modes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/303).
- sonic_l2_interfaces - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- sonic_l3_acls - Add support for playbook check and diff modes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/306).
- sonic_l3_acls - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- sonic_l3_interfaces - Add support for replaced and overridden states (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/241).
- sonic_lag_interfaces - Add support for playbook check and diff modes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/303).
- sonic_lag_interfaces - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- sonic_logging - Add support for playbook check and diff modes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/285).
- sonic_logging - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- sonic_mclag - Add VLAN range support for 'unique_ip' and 'peer_gateway' options (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/288).
- sonic_mclag - Add support for replaced and overridden states (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/288).
- sonic_ntp - Add support for playbook check and diff modes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/281).
- sonic_ntp - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- sonic_port_breakout - Add Ansible support for all port breakout modes now allowed in Enterprise SONiC (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/276).
- sonic_port_breakout - Add support for replaced and overridden states (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/291).
- sonic_port_group - Add support for playbook check and diff modes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/284).
- sonic_port_group - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- sonic_radius_server - Add support for playbook check and diff modes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/279).
- sonic_radius_server - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- sonic_static_routes - Add playbook check and diff modes support for static routes resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/313).
- sonic_static_routes - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- sonic_system - Add support for playbook check and diff modes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/284).
- sonic_system - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- sonic_tacacs_server - Add support for playbook check and diff modes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/281).
- sonic_tacacs_server - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- sonic_users - Add support for playbook check and diff modes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/304).
- sonic_users - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- sonic_vlans - Add support for playbook check and diff modes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/301).
- sonic_vlans - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- sonic_vrfs - Add mgmt VRF replaced state handling to sonic_vrfs module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/298).
- sonic_vrfs - Add mgmt VRF support to sonic_vrfs module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/293).
- sonic_vrfs - Add support for playbook check and diff modes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/285).
- sonic_vrfs - Enhance config diff generation function (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/318).
- tests - Add UTs for BFD, COPP, and MAC modules (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/287).
- tests - Enable contiguous execution of all regression integration tests on an S5296f (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/277).
- tests - Fix the bgp CLI test base_cfg_path derivation of the bgp role_path by avoiding relative pathing from the possibly external playbook_dir (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/283).

Bugfixes
--------

- sonic_bgp_communities - Fix incorrect "facts" handling for parsing of a BGP community list configured with an empty "members" list (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/319).
- sonic_bgp_neighbors - Fix prefix-limit issue (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/289).
- sonic_interfaces - Add warnings when speed and auto_negotiate is configured at same time (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/314).
- sonic_interfaces - Fix support for standard naming interfaces (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/314).
- sonic_interfaces - Prevent configuring speed in port group interfaces (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/314).
- sonic_stp - Correct the commands list for STP delete state (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/302).

New Modules
-----------

- dellemc.enterprise_sonic.sonic_dhcp_snooping - Manage DHCP Snooping on SONiC
- dellemc.enterprise_sonic.sonic_pki - Manages PKI attributes of Enterprise Sonic
- dellemc.enterprise_sonic.sonic_stp - Manage STP configuration on SONiC

v2.2.0
======

Release Summary
---------------

| Release Date: 2023-06-01
| This release provides Ansible compliance changes required on top of the changes included in
| the 2.1.0 release of the enterprise_sonic Ansible network resource module collection.
| It addresses two issues raised by the Ansible core team with the content of the 2.1.0 release.
| 1) Back out the "breaking_change" made in the sonic_aaa resource module to fix a functional
| shortcoming in the enterprise_sonic Ansible collection. Although the change is still needed,
| it will be deferred to a "major" release.
| 2) Re-enable installation of new Ansible Netcommon repo instances when installing the
| enterprise_sonic Ansible collection. The 2.1.0 enterprise_sonic Ansible release included a
| workaround for a bug introduced in the 5.0.0 version of the Ansible Netcommon repo. This
| workaround was implemented in the "galaxy.yml" file for the enterprise_sonic
| 2.1.0 release. New versions of Ansible Netcommon were published after the problematic 5.0.0
| version and the revised "galaxy.yml" file for this release enables installation of these
| newer versions.

Minor Changes
-------------

- galaxy_yml - Enable installation of Ansible Netcomon versions after 5.0.0 and update the enterprise_sonic release version (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/270).
- sonic_aaa - Revert breaking changes for AAA nodule (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/269).

v2.1.0
======

Release Summary
---------------

| Release Date: 2023-0515
| This release provides enhanced Dell Enterprise SONiC Ansible Collection support for SONiC 4.x images.
| In addition to new resource modules to support previously existing functionality, it provides
| support for the "QinQ" (Vlan Mapping) function introduced with SONiC release 4.1. It also provides
| bug fixes and enhancements for support of features that were initially introduced in previous
| Enterprise SONiC Ansible releases. The changelog describes changes made to the modules and plugins
| included in this collection since release 2.0.0.

Minor Changes
-------------

- module_utils - Change the location for importing remove_empties from the obsolete Netcommon location to the offically required Ansible library location to fix sanity errors (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/172).
- sonic_aaa - Add replaced and overridden states support for AAA resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/237).
- sonic_aaa - Add unit tests for AAA resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/198).
- sonic_api - Add unit tests for api resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/218).
- sonic_bfd, sonic_copp - Update replaced methods (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/254).
- sonic_bgp - Add rt_delay attribute to module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/244).
- sonic_bgp - Add support for replaced and overridden states (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/240).
- sonic_bgp - Add unit tests for BGP resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/182).
- sonic_bgp_af - Add several attributes to support configuration of route distinguisher and route target (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/141).
- sonic_bgp_af - Add support for replaced and overridden states (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/246).
- sonic_bgp_af - Add unit tests for BGP AF resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/183).
- sonic_bgp_af - Modify BGP AF resource module unit tests to adjust for changes in the resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/191).
- sonic_bgp_as_paths - Add unit tests for BGP AS paths resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/184).
- sonic_bgp_communities - Add unit tests for BGP communities resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/185).
- sonic_bgp_ext_communities - Add unit tests for BGP ext communities resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/186).
- sonic_bgp_neighbors - Add unit tests for BGP neighbors resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/187).
- sonic_bgp_neighbors - Enhance unit tests for BGP Neighbors resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/245).
- sonic_bgp_neighbors_af - Add unit tests for BGP neighbors AF resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/188).
- sonic_command - Add unit tests for command resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/219).
- sonic_config - Add unit tests for config resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/220).
- sonic_dhcp_relay - Add a common unit tests module and unit tests for dhcp relay module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/148).
- sonic_dhcp_relay - Add support for replaced and overridden states (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/249).
- sonic_facts - Add unit tests for facts resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/222).
- sonic_interfaces - Add speed, auto-negotiate, advertised-speed and FEC to interface resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/128).
- sonic_interfaces - Add unit tests for interfaces resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/197).
- sonic_ip_neighbor - Add unit tests for IP neighbor resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/225).
- sonic_ip_neighbor - Change the replaced function in ip_neighbor resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/253).
- sonic_l2_interfaces - Add support for parsing configuration containing the OC Yang vlan range syntax (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/124).
- sonic_l2_interfaces - Add support for replaced and overridden states (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/221).
- sonic_l2_interfaces - Add support for specifying vlan trunk ranges in Ansible playbooks (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/149).
- sonic_l2_interfaces - Add unit tests for l2_interfaces resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/200).
- sonic_l3_interfaces - Add unit tests for l3_interfaces resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/202).
- sonic_lag_interface - Add replaced and overridden states support for LAG interface resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/196).
- sonic_lag_interfaces - Add unit tests for lag_interfaces resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/203).
- sonic_logging - Add replaced and overridden states support for logging resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/150).
- sonic_logging - Add unit tests for logging resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/226).
- sonic_logging - Change logging get facts for source_interface naming (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/258).
- sonic_mclag - Add delay_restore, gateway_mac, and peer_gateway attributes to module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/145).
- sonic_ntp - Add prefer attribute to NTP resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/118).
- sonic_ntp - Add replaced and overridden states support for NTP resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/151).
- sonic_ntp - Add unit tests for NTP resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/207).
- sonic_ntp - Change NTP get facts to get default parameters (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/106).
- sonic_ntp - Change NTP key values in NTP regression test script (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/107).
- sonic_ntp - Change NTP module name (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/113).
- sonic_ntp - Change NTP module names in NTP regression test script (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/114).
- sonic_ntp - Change NTP resource module to make minpoll and maxpoll be configured together (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/129).
- sonic_port_breakout - Add unit tests for port breakout resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/229).
- sonic_port_group - Add replaced and overridden states support for port group resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/227).
- sonic_port_group - Add unit tests for port group resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/228).
- sonic_prefix_lists - Add support for replaced and overridden states (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/255).
- sonic_prefix_lists - Add unit tests for prefix lists resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/209).
- sonic_radius_server - Add replaced and overridden states support for RADIUS server resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/239).
- sonic_radius_server - Add unit tests for RADIUS server resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/210).
- sonic_static_routes - Add support for replaced and overridden states (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/236).
- sonic_static_routes - Add unit tests for static routes resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/212).
- sonic_system - Add replaced and overridden states support for system resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/159).
- sonic_system - Add unit tests for system resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/223).
- sonic_tacacs_server - Add replaced and overridden states support for TACACS server resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/235).
- sonic_tacacs_server - Add unit tests for TACACS server resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/208).
- sonic_users - Add replaced and overridden states support for users resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/242).
- sonic_users - Add unit tests for users resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/213).
- sonic_vlans - Add replaced and overridden states support for VLAN resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/217).
- sonic_vlans - Add unit tests for Vlans resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/214).
- sonic_vrfs - Add replaced and overridden states support for VRF resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/156).
- sonic_vrfs - Add unit tests for VRFS resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/216).
- sonic_vxlans - Add support for replaced and overridden states (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/247).
- sonic_vxlans - Add unit tests for VxLans resource module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/215).

Breaking Changes / Porting Guide
--------------------------------

- sonic_aaa - Add default_auth attribute to the argspec to replace the deleted group and local attributes. This change allows for ordered login authentication. (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/195).

Bugfixes
--------

- Fix regression test bugs in multiple modules (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/180).
- Fix sanity check errors in the collection caused by Ansible library changes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/160).
- install - Update the required ansible.netcommon version (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/176).
- sonic_bgp_af - Fix issue with vnis and advertise modification for a single BGP AF (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/201).
- sonic_bgp_as_paths - Fix issues with merged and deleted states (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/250).
- sonic_interfaces - Fix command timeout issue (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/261).
- sonic_l3_interfaces - Fix IP address deletion issue (GitHub issue#170) (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/231).
- sonic_lag_interfaces - Fix port name issue (GitHub issue#153) (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/119).
- sonic_neighbors - Fix handling of default attributes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/233).
- sonic_ntp - Fix the issue (GitHub issue#205) with NTP clear all without config given (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/224).
- sonic_vlan_mapping - Remove platform checks (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/262).
- sonic_vrfs - Add tasks as a workaround to mgmt VRF bug (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/146).
- sonic_vrfs - Fix spacing issue in CLI test case (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/257).
- sonic_vrfs - Fix the issue (GitHub issue#194) with VRF when deleting interface(https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/230).
- sonic_vxlans - Remove required_together restriction for evpn_nvo and source_ip attributes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/130).
- workflows - Fix dependency installation issue in the code coverage workflow (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/199).

New Modules
-----------

- dellemc.enterprise_sonic.sonic_acl_interfaces - Manage access control list (ACL) to interface binding on SONiC
- dellemc.enterprise_sonic.sonic_bfd - Manage BFD configuration on SONiC
- dellemc.enterprise_sonic.sonic_copp - Manage CoPP configuration on SONiC
- dellemc.enterprise_sonic.sonic_dhcp_relay - Manage DHCP and DHCPv6 relay configurations on SONiC
- dellemc.enterprise_sonic.sonic_ip_neighbor - Manage IP neighbor global configuration on SONiC
- dellemc.enterprise_sonic.sonic_l2_acls - Manage Layer 2 access control lists (ACL) configurations on SONiC
- dellemc.enterprise_sonic.sonic_l3_acls - Manage Layer 3 access control lists (ACL) configurations on SONiC
- dellemc.enterprise_sonic.sonic_lldp_global - Manage Global LLDP configurations on SONiC
- dellemc.enterprise_sonic.sonic_logging - Manage logging configuration on SONiC
- dellemc.enterprise_sonic.sonic_mac - Manage MAC configuration on SONiC
- dellemc.enterprise_sonic.sonic_port_group - Manages port group configuration on SONiC
- dellemc.enterprise_sonic.sonic_route_maps - route map configuration handling for SONiC
- dellemc.enterprise_sonic.sonic_vlan_mapping - Configure vlan mappings on SONiC

v2.0.0
======

Release Summary
---------------

This release provides Dell SONiC Enterprise Ansible Collection support for SONiC 4.x images. It is the first release for the 2.x branch of the collection. Subsequent enhancements for support of SONiC 4.x images will also be provided as needed on the 2.x branch. This release also contains bugfixes and enhancements to supplement the Ansible functionality provided previously for SONiC 3.x images. The changelog describes changes made to the modules and plugins included in this collection since release 1.1.0.

Minor Changes
-------------

- Add an execution-environment.yml file to the "meta" directory to enable use of Ansible execution environment infrastructure (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/88).
- bgp_af - Add support for BGP options to configure usage and advertisement of vxlan primary IP address related attributes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/62).
- bgp_as_paths - Update module examples with 'permit' attribute (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/102).
- bgp_neighbors - Add BGP peer group support for multiple attributes. The added attributes correspond to the same set of attributes added for BGP neighbors with PR 72 (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/81).
- bgp_neighbors - Add an auth_pwd dictionary and nbr_description attribute to the argspec (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/67).
- bgp_neighbors - Add prefix-list related peer-group attributes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/101).
- bgp_neighbors - Add support for multiple attributes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/72).
- bgp_neighbors_af - Add prefix-list related neighbor attributes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/101).
- playbook - Update examples to reflect module changes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/102).
- sonic_vxlans - Add configuration capability for the primary IP address of a vxlan vtep to facilitate vxlan path redundundancy (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/58).
- vlans - Add support for the vlan "description" attribute (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/98).
- workflow - Add stable-2.13 to the sanity test matrix (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/90).

Breaking Changes / Porting Guide
--------------------------------

- bgp_af - Add the route_advertise_list dictionary to the argspec to replace the deleted, obsolete advertise_prefix attribute used for SONiC 3.x images on the 1.x branch of this collection. This change corresponds to a SONiC 4.0 OC YANG REST compliance change for the BGP AF REST API. It enables specification of a route map in conjunction with each route advertisement prefix (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/63).
- bgp_af - Remove the obsolete 'advertise_prefix' attribute from argspec and config code. This and subsequent co-req replacement with the new route advertise list argument structure require corresponding changes in playbooks previoulsly used for configuring route advertise prefixes for SONiC 3.x images. (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/60).
- bgp_neighbors - Replace the previously defined standalone "bfd" attribute with a bfd dictionary containing multiple attributes. This change corresponds to the revised SONiC 4.x implementation of OC YANG compatible REST APIs. Playbooks previously using the bfd attributes for SONiC 3.x images must be modified for use on SONiC 4.0 images to use the new definition for the bfd attribute argspec structure (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/72).
- bgp_neighbors - Replace, for BGP peer groups, the previously defined standalone "bfd" attribute with a bfd dictionary containing multiple attributes. This change corresponds to the revised SONiC 4.x implementation of OC YANG compatible REST APIs. Playbooks previously using the bfd attributes for SONiC 3.x images must be modified for use on SONiC 4.0 images to use the new definition for the bfd attribute argspec structure (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/81).

Bugfixes
--------

- Fixed regression test bugs in multiple modules (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/103).
- Fixed regression test sequencing and other regression test bugs in multiple modules (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/85).
- bgp_neighbors - Remove string conversion of timer attributes (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/60).
- port_breakout - Fixed a bug in formulation of port breakout REST APIs (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/88).
- sonic - Fix a bug in handling of interface names in standard interface naming mode (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/103).
- sonic_aaa - Fix a bug in facts gathering by providing required conditional branching (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/90).
- sonic_aaa - Modify regression test sequencing to enable correct testing of the functionality for this module (https://github.com/ansible-collections/dellemc.enterprise_sonic/pull/78).
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

- dellemc.enterprise_sonic.sonic_aaa - Manage AAA and its parameters
- dellemc.enterprise_sonic.sonic_radius_server - Manage RADIUS server and its parameters
- dellemc.enterprise_sonic.sonic_system - Configure system parameters
- dellemc.enterprise_sonic.sonic_tacacs_server - Manage TACACS server and its parameters

v1.0.0
======

New Plugins
-----------

Cliconf
~~~~~~~

- dellemc.enterprise_sonic.sonic - Use sonic cliconf to run command on Dell OS10 platform

Httpapi
~~~~~~~

- dellemc.enterprise_sonic.sonic - HttpApi Plugin for devices supporting Restconf SONIC API

New Modules
-----------

- dellemc.enterprise_sonic.sonic_api - Manages REST operations on devices running Enterprise SONiC
- dellemc.enterprise_sonic.sonic_bgp - Manage global BGP and its parameters
- dellemc.enterprise_sonic.sonic_bgp_af - Manage global BGP address-family and its parameters
- dellemc.enterprise_sonic.sonic_bgp_as_paths - Manage BGP autonomous system path (or as-path-list) and its parameters
- dellemc.enterprise_sonic.sonic_bgp_communities - Manage BGP community and its parameters
- dellemc.enterprise_sonic.sonic_bgp_ext_communities - Manage BGP extended community-list and its parameters
- dellemc.enterprise_sonic.sonic_bgp_neighbors - Manage a BGP neighbor and its parameters
- dellemc.enterprise_sonic.sonic_bgp_neighbors_af - Manage the BGP neighbor address-family and its parameters
- dellemc.enterprise_sonic.sonic_command - Runs commands on devices running Enterprise SONiC
- dellemc.enterprise_sonic.sonic_config - Manages configuration sections on devices running Enterprise SONiC
- dellemc.enterprise_sonic.sonic_interfaces - Configure Interface attributes on interfaces such as, Eth, LAG, VLAN, and loopback. (create a loopback interface if it does not exist.)
- dellemc.enterprise_sonic.sonic_l2_interfaces - Configure interface-to-VLAN association that is based on access or trunk mode
- dellemc.enterprise_sonic.sonic_l3_interfaces - Configure the IPv4 and IPv6 parameters on Interfaces such as, Eth, LAG, VLAN, and loopback
- dellemc.enterprise_sonic.sonic_lag_interfaces - Manage link aggregation group (LAG) interface parameters
- dellemc.enterprise_sonic.sonic_mclag - Manage multi chassis link aggregation groups domain (MCLAG) and its parameters
- dellemc.enterprise_sonic.sonic_port_breakout - Configure port breakout settings on physical interfaces
- dellemc.enterprise_sonic.sonic_users - Manage users and its parameters
- dellemc.enterprise_sonic.sonic_vlans - Manage VLAN and its parameters
- dellemc.enterprise_sonic.sonic_vrfs - Manage VRFs and associate VRFs to interfaces such as, Eth, LAG, VLAN, and loopback
- dellemc.enterprise_sonic.sonic_vxlans - Manage VxLAN EVPN and its parameters
