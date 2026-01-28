.. _dellemc.enterprise_sonic.sonic_bgp_neighbors_af_module:


***********************************************
dellemc.enterprise_sonic.sonic_bgp_neighbors_af
***********************************************

**Manage the BGP neighbor address-family and its parameters**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of BGP neighbors address-family parameters on devices running Enterprise SONiC.
- bgp_as, vrf_name and neighbors need be created in advance on the device.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="5">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>config</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the BGP neighbors address-family related configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>bgp_as</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the BGP autonomous system (AS) number which is already configured on the device.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>neighbors</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies BGP neighbor related configurations in address-family configuration mode.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address_family</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies BGP address-family related configurations.</div>
                        <div>afi and safi are required together.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>activate</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Enables the address-family for this neighbor.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>afi</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ipv4</li>
                                    <li>ipv6</li>
                                    <li>l2vpn</li>
                        </ul>
                </td>
                <td>
                        <div>Type of address-family to configure.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>allowas_in</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Criterion for accepting received advertisements containing the AS number</div>
                        <div>of this BGP router intance in the AS PATH of received advertisements.</div>
                        <div>The &#x27;origin&#x27; option can not be set to true when a &#x27;value&#x27; is set.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>origin</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Accept this BGP router instance&#x27;s set AS as the origin.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Accept up to this number of occurrences of this BGP router&#x27;s</div>
                        <div>set AS in the AS-PATH of received advertisements.</div>
                        <div>(Specify a number in the range 1-10.)</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>fabric_external</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Configure a neighbor as fabric-external.</div>
                        <div>Fabric external is supported only for l2vpn address family.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ip_afi</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Common configuration attributes for IPv4 and IPv6 unicast address families.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>default_policy_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies routing policy definition.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>send_default_route</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Enable or disable sending of default-route to the neighbor.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>prefix_limit</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies prefix limit attributes for ipv4-unicast and ipv6-unicast.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>discard_extra</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Enable or disable discard extra of BGP session when maximum prefix limit is exceeded.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>max_prefixes</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Maximum number of prefixes that will be accepted from the neighbor.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>prevent_teardown</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Enable or disable teardown of BGP session when maximum prefix limit is exceeded.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>restart_timer</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Time interval in seconds after which the BGP session is re-established after being torn down.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>warning_threshold</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Threshold on number of prefixes that can be received from a neighbor before generation of warning messages.</div>
                        <div>Expressed as a percentage of max-prefixes.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>prefix_list_in</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Inbound route filtering policy for a neighbor.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>prefix_list_out</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Outbound route filtering policy for a neighbor.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>route_map</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the route-map.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>direction</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the direction of the route-map.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the name of the route-map.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>route_reflector_client</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies a neighbor as a route-reflector client.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>route_server_client</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies a neighbor as a route-server client.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>safi</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>unicast</b>&nbsp;&larr;</div></li>
                                    <li>evpn</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the type of cast for the address-family.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>neighbor</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Neighbor router address which is already configured on the device.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vrf_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">"default"</div>
                </td>
                <td>
                        <div>Specifies the VRF name which is already configured on the device.</div>
                </td>
            </tr>

            <tr>
                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>merged</b>&nbsp;&larr;</div></li>
                                    <li>deleted</li>
                                    <li>replaced</li>
                                    <li>overridden</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the operation to be performed on the BGP process that is configured on the device.</div>
                        <div>In case of merged, the input configuration is merged with the existing BGP configuration on the device.</div>
                        <div>In case of deleted, the existing BGP configuration is removed from the device.</div>
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

    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration bgp neighbor vrf default
    # !
    # neighbor interface Eth1/3
    #  !
    #  address-family ipv4 unicast
    #   activate
    #   allowas-in 4
    #   route-map aa in
    #   route-map aa out
    #   route-reflector-client
    #   route-server-client
    #   send-community both
    # !

    - name: Delete specific BGP neighbors AF attributes
      dellemc.enterprise_sonic.sonic_bgp_neighbors_af:
         config:
            - bgp_as: 4
              neighbors:
                 - neighbor: Eth1/3
                   address_family:
                      - afi: ipv4
                        safi: unicast
                        allowas_in:
                           value: 4
                        route_map:
                           - name: aa
                             direction: in
                           - name: aa
                             direction: out
                        route_reflector_client: true
                        route_server_client: true
         state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration bgp neighbor vrf default
    # !
    # neighbor interface Eth1/3
    #  !
    #  address-family ipv4 unicast
    #   send-community both
    # !


    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration bgp neighbor vrf default 1.1.1.1
    # (No bgp neighbor configuration present)
    - name: "Configure BGP neighbor prefix-list attributes"
      dellemc.enterprise_sonic.sonic_bgp_neighbors_af:
         config:
            - bgp_as: 51
              neighbors:
                 - neighbor: 1.1.1.1
                   address_family:
                      - afi: ipv4
                        safi: unicast
                        ip_afi:
                           default_policy_name: rmap_reg1
                           send_default_route: true
                        prefix_limit:
                           max_prefixes: 2
                           discard_extra: true
                           warning_threshold: 60
                        prefix_list_in: p1
                        prefix_list_out: p2
         state: merged
    # After state:
    # ------------
    #
    # sonic# show running-configuration bgp neighbor vrf default 1.1.1.1
    # !
    # neighbor 1.1.1.1
    #  !
    #  address-family ipv4 unicast
    #   default-originate route-map rmap_reg1
    #   prefix-list p1 in
    #   prefix-list p2 out
    #   send-community both
    #   maximum-prefix 2 60 discard-extra


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration bgp neighbor vrf default
    # !
    # neighbor 1.1.1.1
    #  !
    #  address-family ipv6 unicast
    #   default-originate route-map rmap_reg2
    #   prefix-list p1 in
    #   prefix-list p2 out
    #   send-community both
    #   maximum-prefix 5 90 restart 2

    - name: Delete BGP neighbors AF prefix-list attributes
      dellemc.enterprise_sonic.sonic_bgp_neighbors_af:
         config:
            - bgp_as: 51
              neighbors:
                 - neighbor: 1.1.1.1
                   address_family:
                      - afi: ipv6
                        safi: unicast
                        ip_afi:
                           default_policy_name: rmap_reg2
                           send_default_route: true
                        prefix_limit:
                           max_prefixes: 5
                           warning_threshold: 90
                           restart-timer: 2
                        prefix_list_in: p1
                        prefix_list_out: p2
         state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration bgp neighbor vrf default
    # !
    # neighbor 1.1.1.1
    # !


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration bgp neighbor vrf default
    # !
    # neighbor interface Eth1/3
    #  !
    #  address-family ipv4 unicast
    #   activate
    #   allowas-in 4
    #   route-map aa in
    #   route-map aa out
    #   route-reflector-client
    #   route-server-client
    #   send-community both
    # !
    # neighbor interface Eth1/5
    #  !
    #  address-family ipv4 unicast
    #   activate
    #   allowas-in origin
    #   send-community both
    # !

    - name: Delete all BGP neighbors AF configuration
      dellemc.enterprise_sonic.sonic_bgp_neighbors_af:
         config:
         state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration bgp neighbor vrf default
    # (No bgp neighbor configuration present)


    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration bgp neighbor vrf default
    # !
    # neighbor interface Eth1/3
    # !

    - name: Merge BGP neighbors AF configuration
      dellemc.enterprise_sonic.sonic_bgp_neighbors_af:
         config:
            - bgp_as: 4
              neighbors:
                 - neighbor: Eth1/3
                   address_family:
                      - afi: ipv4
                        safi: unicast
                        allowas_in:
                           value: 4
                        route_map:
                           - name: aa
                             direction: in
                           - name: aa
                             direction: out
                        route_reflector_client: true
                        route_server_client: true
         state: merged

    # After state:
    # ------------
    #
    # sonic# show running-configuration bgp neighbor vrf default
    # !
    # neighbor interface Eth1/3
    #  !
    #  address-family ipv4 unicast
    #   activate
    #   allowas-in 4
    #   route-map aa in
    #   route-map aa out
    #   route-reflector-client
    #   route-server-client
    #   send-community both
    # !


    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration bgp neighbor vrf default
    # (No bgp neighbor configuration present)

    - name: Configure BGP neighbors AF prefix-list attributes
      dellemc.enterprise_sonic.sonic_bgp_neighbors_af:
         config:
            - bgp_as: 51
              neighbors:
                 - neighbor: 1.1.1.1
                   address_family:
                      - afi: ipv4
                        safi: unicast
                        ip_afi:
                           default_policy_name: rmap_reg1
                           send_default_route: true
                        prefix_limit:
                           max_prefixes: 1
                           prevent_teardown: true
                           warning_threshold: 80
                        prefix_list_in: p1
                        prefix_list_out: p2
         state: merged

    # After state:
    # ------------
    #
    # sonic# show running-configuration bgp neighbor vrf default
    # !
    # neighbor 1.1.1.1
    #  !
    #  address-family ipv4 unicast
    #   default-originate route-map rmap_reg1
    #   prefix-list p1 in
    #   prefix-list p2 out
    #   send-community both
    #   maximum-prefix 1 80 warning-only
    # !


    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration bgp neighbor vrf default
    # !
    # neighbor 1.1.1.1
    #  !
    #  address-family ipv6 unicast
    #   default-originate route-map rmap_reg2
    #   prefix-list p1 in
    #   prefix-list p2 out
    #   send-community both
    #   maximum-prefix 5 90 restart 2
    # !

    - name: Replace BGP neighbors AF attributes
      dellemc.enterprise_sonic.sonic_bgp_neighbors_af:
         config:
            - bgp_as: 51
              neighbors:
                 - neighbor: 1.1.1.1
                   address_family:
                      - afi: ipv4
                        safi: unicast
                        ip_afi:
                           default_policy_name: rmap_reg1
                           send_default_route: true
                        prefix_limit:
                           max_prefixes: 1
                           prevent_teardown: true
                           warning_threshold: 80
                        prefix_list_in: p1
                        prefix_list_out: p2
         state: replaced

    # After state:
    # ------------
    #
    # sonic# show running-configuration bgp neighbor vrf default
    # !
    # neighbor 1.1.1.1
    #  !
    #  address-family ipv4 unicast
    #   default-originate route-map rmap_reg1
    #   prefix-list p1 in
    #   prefix-list p2 out
    #   send-community both
    #   maximum-prefix 1 80 warning-only
    # !


    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration bgp neighbor vrf default
    # !
    # neighbor 1.1.1.1
    #  !
    #  address-family ipv6 unicast
    #   default-originate route-map rmap_reg2
    #   prefix-list p1 in
    #   prefix-list p2 out
    #   send-community both
    #   maximum-prefix 5 90 restart 2
    # !

    - name: Override BGP neighbors AF configuration
      dellemc.enterprise_sonic.sonic_bgp_neighbors_af:
         config:
            - bgp_as: 51
              neighbors:
                 - neighbor: 2.2.2.2
                   address_family:
                      - afi: ipv4
                        safi: unicast
                        ip_afi:
                           default_policy_name: rmap_reg1
                           send_default_route: true
                        prefix_limit:
                           max_prefixes: 1
                           prevent_teardown: true
                           warning_threshold: 80
                        prefix_list_in: p1
                        prefix_list_out: p2
         state: overridden

    # After state:
    # ------------
    #
    # sonic# show running-configuration bgp neighbor vrf default
    # !
    # neighbor 2.2.2.2
    #  !
    #  address-family ipv4 unicast
    #   default-originate route-map rmap_reg1
    #   prefix-list p1 in
    #   prefix-list p2 out
    #   send-community both
    #   maximum-prefix 1 80 warning-only
    # !



Return Values
-------------
Common return values are documented `here <https://docs.ansible.com/projects/ansible/latest/reference_appendices/common_return_values.html#common-return-values>`_, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>after</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>when changed</td>
                <td>
                            <div>The resulting configuration module invocation.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned is always in the same format as the parameters above.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>after_generated</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>when <code>check_mode</code></td>
                <td>
                            <div>The generated configuration module invocation.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format as the parameters above.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>before</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The configuration prior to the module invocation.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned is always in the same format as the parameters above.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>commands</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The set of commands pushed to the remote device.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;command 1&#x27;, &#x27;command 2&#x27;, &#x27;command 3&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Niraimadaiselvam M (@niraimadaiselvamm)
