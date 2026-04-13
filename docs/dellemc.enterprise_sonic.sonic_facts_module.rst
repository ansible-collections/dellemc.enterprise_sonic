.. _dellemc.enterprise_sonic.sonic_facts_module:


************************************
dellemc.enterprise_sonic.sonic_facts
************************************

**Collects facts on devices running Enterprise SONiC**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Collects facts from devices running Enterprise SONiC Distribution by Dell Technologies. This module places the facts gathered in the fact tree keyed by the respective resource name. The facts module always collects a base set of facts from the device and can enable or disable collection of additional facts.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>gather_network_resources</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>all</li>
                                    <li>vlans</li>
                                    <li>interfaces</li>
                                    <li>l2_interfaces</li>
                                    <li>l3_interfaces</li>
                                    <li>ipv6_router_advertisement</li>
                                    <li>lag_interfaces</li>
                                    <li>bgp</li>
                                    <li>bgp_af</li>
                                    <li>bgp_neighbors</li>
                                    <li>bgp_neighbors_af</li>
                                    <li>bgp_as_paths</li>
                                    <li>bgp_communities</li>
                                    <li>bgp_ext_communities</li>
                                    <li>ospfv2_interfaces</li>
                                    <li>ospfv2</li>
                                    <li>ospfv3</li>
                                    <li>ospfv3_area</li>
                                    <li>ospfv3_interfaces</li>
                                    <li>mclag</li>
                                    <li>prefix_lists</li>
                                    <li>vlan_mapping</li>
                                    <li>vrfs</li>
                                    <li>vrrp</li>
                                    <li>vxlans</li>
                                    <li>users</li>
                                    <li>system</li>
                                    <li>port_breakout</li>
                                    <li>pms</li>
                                    <li>aaa</li>
                                    <li>ldap</li>
                                    <li>tacacs_server</li>
                                    <li>radius_server</li>
                                    <li>static_routes</li>
                                    <li>ntp</li>
                                    <li>logging</li>
                                    <li>pki</li>
                                    <li>ip_neighbor</li>
                                    <li>ip_neighbor_interfaces</li>
                                    <li>port_group</li>
                                    <li>dhcp_relay</li>
                                    <li>acl_interfaces</li>
                                    <li>l2_acls</li>
                                    <li>l3_acls</li>
                                    <li>lldp_global</li>
                                    <li>ptp_default_ds</li>
                                    <li>mac</li>
                                    <li>bfd</li>
                                    <li>copp</li>
                                    <li>route_maps</li>
                                    <li>lldp_interfaces</li>
                                    <li>stp</li>
                                    <li>poe</li>
                                    <li>dhcp_snooping</li>
                                    <li>sflow</li>
                                    <li>fips</li>
                                    <li>roce</li>
                                    <li>qos_buffer</li>
                                    <li>qos_pfc</li>
                                    <li>qos_maps</li>
                                    <li>qos_scheduler</li>
                                    <li>qos_wred</li>
                                    <li>qos_interfaces</li>
                                    <li>pim_global</li>
                                    <li>pim_interfaces</li>
                                    <li>login_lockout</li>
                                    <li>mgmt_servers</li>
                                    <li>ospf_area</li>
                                    <li>ssh</li>
                                    <li>lst</li>
                                    <li>ptp_port_ds</li>
                                    <li>fbs_classifiers</li>
                                    <li>fbs_groups</li>
                                    <li>fbs_policies</li>
                                    <li>ars</li>
                                    <li>network_policy</li>
                                    <li>br_l2pt</li>
                                    <li>dcbx</li>
                                    <li>mirroring</li>
                                    <li>mfa</li>
                                    <li>drop_counter</li>
                                    <li>evpn_esi_multihome</li>
                                    <li>ssh_server</li>
                                    <li>ecmp_load_share</li>
                                    <li>fbs_interfaces</li>
                        </ul>
                </td>
                <td>
                        <div>When supplied, this argument restricts the facts collected to a given subset. Possible values for this argument include all and the resources like &#x27;all&#x27;, &#x27;interfaces&#x27;, &#x27;vlans&#x27;, &#x27;lag_interfaces&#x27;, &#x27;l2_interfaces&#x27;, &#x27;l3_interfaces&#x27;. Can specify a list of values to include a larger subset. Values can also be used with an initial &#x27;!&#x27; to specify that a specific subset should not be collected.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>gather_subset</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">"!config"</div>
                </td>
                <td>
                        <div>When supplied, this argument restricts the facts collected to a given subset. Possible values for this argument include all, min, hardware, config, legacy, and interfaces. Can specify a list of values to include a larger subset. Values can also be used with an initial &#x27;!&#x27; to specify that a specific subset should not be collected.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - Tested against Enterprise SONiC Distribution by Dell Technologies.
   - Supports ``check_mode``.



Examples
--------

.. code-block:: yaml

    - name: Gather all facts
      dellemc.enterprise_sonic.sonic_facts:
        gather_subset: all
        gather_network_resources: all
    - name: Collects VLAN and interfaces facts
      dellemc.enterprise_sonic.sonic_facts:
        gather_subset:
          - min
        gather_network_resources:
          - vlans
          - interfaces
    - name: Do not collects VLAN and interfaces facts
      dellemc.enterprise_sonic.sonic_facts:
        gather_network_resources:
          - "!vlans"
          - "!interfaces"
    - name: Collects VLAN and minimal default facts
      dellemc.enterprise_sonic.sonic_facts:
        gather_subset: min
        gather_network_resources: vlans
    - name: Collect lag_interfaces and minimal default facts
      dellemc.enterprise_sonic.sonic_facts:
        gather_subset: min
        gather_network_resources: lag_interfaces




Status
------


Authors
~~~~~~~

- Mohamed Javeed (@javeedf)
- Abirami N (@abirami-n)
