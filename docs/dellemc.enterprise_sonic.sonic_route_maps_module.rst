.. _dellemc.enterprise_sonic.sonic_route_maps_module:


*****************************************
dellemc.enterprise_sonic.sonic_route_maps
*****************************************

**route map configuration handling for SONiC**


Version added: 2.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management for route map parameters on devices running SONiC.




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
                        <div>Specifies a list of route map configuration dictionaries</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>action</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>permit</li>
                                    <li>deny</li>
                        </ul>
                </td>
                <td>
                        <div>action type for the route map (permit or deny)</div>
                        <div>This value is required for creation and modification of a route</div>
                        <div>map or route map attributes as well as for deletion of route map</div>
                        <div>attributes. It can be omitted only when requesting deletion of a</div>
                        <div>route map statement or all route map statements for a given route</div>
                        <div>map map_name.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>call</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of a route map to jump to after executing &#x27;match&#x27; and &#x27;set&#x27;</div>
                        <div>statements for the current route map.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>map_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of a route map</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>match</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Criteria for matching the route map to a route</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>as_path</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of a configured BGP AS path list to be checked for</div>
                        <div>a match with the target route</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>community</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of a configured BGP &quot;community&quot; to be checked for</div>
                        <div>a match with the target route</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>evpn</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BGP Ethernet Virtual Private Network to be checked for</div>
                        <div>a match with the target route</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>default_route</b>
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
                        <div>Default EVPN type-5 route</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>route_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>macip</li>
                                    <li>multicast</li>
                                    <li>prefix</li>
                        </ul>
                </td>
                <td>
                        <div>Non-default route type: One of the following:</div>
                        <div>mac-ip route, EVPN Type 3 Inclusive Multicast Ethernet</div>
                        <div>Tag (IMET) route, or prefix route</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vni</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>VNI ID to be checked for a match; specified by a value in the</div>
                        <div>range 1-16777215</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ext_comm</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of a configured BGP &#x27;extended community&#x27; to be checked for</div>
                        <div>a match with the target route</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interface</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Next hop interface name (type and number) to be checked for a</div>
                        <div>match with the target route. The interface type can be any</div>
                        <div>of the following; &#x27;Ethernet/Eth&#x27; interface or sub-interface,</div>
                        <div>&#x27;Loopback&#x27; interface, &#x27;PortChannel&#x27; interface or</div>
                        <div>sub-interface, &#x27;Vlan&#x27; interface.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ip</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IP addresses or IP next hops to be checked for a match with the</div>
                        <div>target route</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>name of an IPv4 prefix list containing a list of address</div>
                        <div>prefixes to be checked for a match with the target route</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>next_hop</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>name of a prefix list containing a list of next-hop</div>
                        <div>prefixes to be checked for a match with the target route</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ipv6</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IPv6 addresses to be checked for a match with the</div>
                        <div>target route</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>name of an IPv6 prefix list containing a list of address</div>
                        <div>prefixes to be checked for a match with the target route</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>local_preference</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>local-preference value to be checked for a match with the</div>
                        <div>target route. This is a value in the range 0-4294967295.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>metric</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>metric value to be checked for a match with the target route.</div>
                        <div>This is a value in the range 0-4294967295.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>origin</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>egp</li>
                                    <li>igp</li>
                                    <li>incomplete</li>
                        </ul>
                </td>
                <td>
                        <div>BGP origin to be checked for a match with the target route</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>peer</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BGP routing peer/neighbor required for a matching route</div>
                        <div><em>ip</em>, <em>ipv6</em>, and <em>interface</em> are mutually exclusive.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interface</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name (type and number) of a BGP peer interface</div>
                        <div>Allowed interface types are Ethernet or Eth (depending</div>
                        <div>on the configured interface-naming mode),</div>
                        <div>Vlan, and Portchannel</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ip</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IPv4 address of a BGP peer</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ipv6</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IPv6 address of a BGP peer</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>source_protocol</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>bgp</li>
                                    <li>connected</li>
                                    <li>ospf</li>
                                    <li>static</li>
                        </ul>
                </td>
                <td>
                        <div>Source protocol required for a matching route</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>source_vrf</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of the source VRF required for a matching route</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>tag</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Tag value required for a matching route</div>
                        <div>The value must be in the range 1-4294967295</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>sequence_num</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>unique number in the range 1-66535 to specify priority of the map</div>
                        <div>This value is required for creation and modification of a route</div>
                        <div>map or route map attributes as well as for deletion of route map</div>
                        <div>attributes. It can be omitted only when requesting deletion of all</div>
                        <div>route map &quot;statements&quot; for a given route map &quot;map_name&quot;.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>set</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Information to set into a matching route for re-distribution</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ars_object</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.1.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>Adaptive Routing and Switching object</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>as_path_prepend</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>String specifying a comma-separated list of AS-path numbers</div>
                        <div>to prepend to the BGP AS-path attribute in a matched route.</div>
                        <div>AS-path values in the list must be in the range</div>
                        <div>1-4294967295; for example, 2000,3000</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>comm_list_delete</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>String specifying the name of a BGP community list containing</div>
                        <div>BGP Community values to be deleted from matching routes.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>community</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BGP community attributes to add to or replace the BGP</div>
                        <div>community attributes in a matching route. Specifying the</div>
                        <div>&#x27;additive&#x27; attribute is allowed only if one of</div>
                        <div>the other attributes (other than &#x27;none&#x27;) is specified.</div>
                        <div>It causes the specified &#x27;set community&#x27; attributes</div>
                        <div>to be added to the already existing community</div>
                        <div>attributes in the matching route. If the &#x27;additive&#x27; attribute</div>
                        <div>is not specified, the previously existing community attributes</div>
                        <div>in the matching route are replaced by the configured</div>
                        <div>&#x27;set community&#x27; attributes. Specifying a &#x27;set community&#x27; attribute</div>
                        <div>of &#x27;none&#x27; is mutually exclusive with setting of other community</div>
                        <div>attributes and causes any community attributes in the matching</div>
                        <div>route to be removed.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>community_attributes</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>local_as</li>
                                    <li>no_advertise</li>
                                    <li>no_export</li>
                                    <li>no_peer</li>
                                    <li>additive</li>
                                    <li>none</li>
                        </ul>
                </td>
                <td>
                        <div>A list of one or more BGP community attributes. The allowed</div>
                        <div>values are the following:</div>
                        <div>local_as</div>
                        <div>Do not send outside local AS (well-known community)</div>
                        <div>no_advertise</div>
                        <div>Do not advertise to any peer (well-known community)</div>
                        <div>no_export</div>
                        <div>Do not export to next AS (well-known community)</div>
                        <div>no_peer</div>
                        <div>The route does not need to be advertised to peers.</div>
                        <div>(Advertisement of the route can be suppressed based</div>
                        <div>on other criteria.)</div>
                        <div>additive</div>
                        <div>Add the configured &#x27;set community&#x27; attributes to</div>
                        <div>the matching route (if set to &#x27;true&#x27;); Previously existing</div>
                        <div>attributes in the matching route are, instead, replaced</div>
                        <div>by the configured attributes if this attribute is</div>
                        <div>not specified or if it is set to &#x27;false&#x27;.</div>
                        <div>none</div>
                        <div>Do not send any community attribute. This attribute</div>
                        <div>is mutually exclusive with all other &#x27;set community&#x27;</div>
                        <div>attributes. It causes all attributes to be removed</div>
                        <div>from the matching route.</div>
                        <div><em>none</em> is mutually exclusive with all of the other attributes:</div>
                        <div><em>local_as</em>, <em>no_advertise</em>, <em>no_export</em>, <em>no_peer</em>, <em>additive</em>,</div>
                        <div>and <em>additive</em>.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>community_number</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A list of one or more BGP community numbers in the</div>
                        <div>form AA:NN where AA and NN are integers in the range</div>
                        <div>0-65535.</div>
                        <div>Note: Each community number in the list must be enclosed</div>
                        <div>in double quotes to avoid YAML parsing errors due to the</div>
                        <div>list values containing an embedded &#x27;:&#x27; character.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>extcommunity</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BGP extended community attributes to set into a matching route.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>bandwidth</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.1.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>Link bandwidth extended community</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>bandwidth_value</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Options are one of the following values</div>
                        <div>&lt;1..4294967295&gt;  Cumulative bandwidth of all multipaths (outbound-only)</div>
                        <div>num-multipaths   Internally computed bandwidth based on number of multipaths (outbound-only)</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>transitive_value</b>
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
                        <div>The operational default is false if this option is not specified.</div>
                        <div>True for transitive, false for non-transitive. If true, include the</div>
                        <div>link bandwidth extcommunity in route advertisements sent to</div>
                        <div>neighbors across AS boundaries (eBGP neighbors). If false,</div>
                        <div>drop the link bandwidth extcommunity from route advertisements</div>
                        <div>sent across AS boundaries.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>rt</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Route Target VPN extended communities in the format</div>
                        <div>ASN:NN or IP-ADDRESS:NN</div>
                        <div>Note: Each rt value in the list must be enclosed</div>
                        <div>in double quotes to avoid YAML parsing errors due to the</div>
                        <div>list values containing an embedded &#x27;:&#x27; character.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>soo</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Site-of-Origin VPN extended communities in the format</div>
                        <div>ASN:NN or IP-ADDRESS:NN</div>
                        <div>Note: Each rt value in the list must be enclosed</div>
                        <div>in double quotes to avoid YAML parsing errors due to the</div>
                        <div>list values containing an embedded &#x27;:&#x27; character.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ip_next_hop</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IPv4 next hop address attributes to set into a matching route</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IPv4 next hop address to set into a matching route in the</div>
                        <div>dotted decimal format A.B.C.D</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>native</b>
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
                        <div>Set native or underlay nexthop</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ipv6_next_hop</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IPv6 next hop address attributes to set into a matching route</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>global_addr</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IPv6 global next hop address to set into a matching</div>
                        <div>route in the format A::B</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>native</b>
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
                        <div>Set native or underlay nexthop</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>prefer_global</b>
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
                        <div>Set the corresponding attribute into a matching route</div>
                        <div>if the value of this Ansible attribute is &#x27;true&#x27;.</div>
                        <div>The attribute indicates that the routing algorithm must</div>
                        <div>prefer the global next-hop address over the link-local</div>
                        <div>address if both exist.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>local_preference</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BGP local preference path attribute; integer value in</div>
                        <div>the range 0-4294967295</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>metric</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>route metric value actions</div>
                        <div><em>value</em> and <em>rtt_action</em> are mutually exclusive.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>rtt_action</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>set</li>
                                    <li>add</li>
                                    <li>subtract</li>
                        </ul>
                </td>
                <td>
                        <div>Action to take for modifying the metric for a matched</div>
                        <div>route using the Round Trip Time (rtt);</div>
                        <div><code>set</code> causes the route metric to be set to the</div>
                        <div>rtt value.</div>
                        <div><code>add</code> causes the rtt value to be added</div>
                        <div>to the route metric.</div>
                        <div><code>subtract</code> causes the rtt value to be</div>
                        <div>subtracted from route metric.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>metric value to be set into a matching route;</div>
                        <div>value in the range 0-4294967295</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>origin</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>egp</li>
                                    <li>igp</li>
                                    <li>incomplete</li>
                        </ul>
                </td>
                <td>
                        <div>BGP route origin; One of the following must be selected.</div>
                        <div>egp (External; remote EGP)</div>
                        <div>igp (Internal; local IGP)</div>
                        <div>incomplete (Unknown origin)</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>tag</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Tag value to be set for a matching route</div>
                        <div>The value must be in the range 1-4294967295</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>weight</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BGP weight to be set for a matching route: The weight must be</div>
                        <div>an integer in the range 0-4294967295</div>
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
                        <div>Specifies the type of configuration update to be performed on the device.</div>
                        <div>For <code>merged</code>, merge specified attributes with existing configured attributes.</div>
                        <div>For <code>deleted</code>, delete the specified attributes from existing configuration.</div>
                        <div>For <code>replaced</code>, replace each modified list or dictionary with the</div>
                        <div>specified items.</div>
                        <div>For <code>overridden</code>, replace all current configuration for this resource</div>
                        <div>module with the specified configuration.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - Supports ``check_mode``.



Examples
--------

.. code-block:: yaml

    # Using "merged" state to create initial configuration
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration route-map
    # sonic#
    # (No configuration present)
    #
    # -------------
    #
    - name: Merge initial route_maps configuration
      dellemc.enterprise_sonic.sonic_route_maps:
        config:
          - map_name: rm1
            action: permit
            sequence_num: 80
            match:
              as_path: bgp_as1
              community: bgp_comm_list1
              evpn:
                default_route: true
                vni: 735
              ext_comm: bgp_ext_comm1
              interface: Ethernet4
              ip:
                address: ip_pfx_list1
              ipv6:
                address: ipv6_pfx_list1
              local_preference: 8000
              metric: 400
              origin: egp
              peer:
                ip: 10.20.30.40
              source_protocol: bgp
              source_vrf: Vrf1
              tag: 7284
            set:
              as_path_prepend: 200,315,7135
              comm_list_delete: bgp_comm_list2
              community:
                community_number:
                  - "35:58"
                  - "79:150"
                  - "308:650"
                community_attributes:
                  - local_as
                  - no_advertise
                  - no_export
                  - no_peer
                  - additive
              extcommunity:
                rt:
                  - "30:40"
                soo:
                  - "10.73.14.9:78"
              ip_next_hop:
                address: 10.48.16.18
                native: true
              ipv6_next_hop:
                global_addr: 30::30
                prefer_global: true
                native: true
              local_preference: 635
              metric:
                metric_value: 870
              origin: egp
              weight: 93471
              tag: 65
          - map_name: rm1
            action: deny
            sequence_num: 3047
            match:
              evpn:
                route_type: multicast
              origin: incomplete
              peer:
                interface: Ethernet6
              source_protocol: ospf
            set:
              metric:
                rtt_action: add
              origin: incomplete
          - map_name: rm3
            action: deny
            sequence_num: 285
            match:
              evpn:
                route_type: macip
              origin: igp
              peer:
                ipv6: 87:95:15::53
              source_protocol: connected
            set:
              community:
                community_attributes:
                  - none
              metric:
                rtt_action: set
              origin: igp
            call: rm1
          - map_name: rm4
            action: permit
            sequence_num: 480
            match:
              evpn:
                route_type: prefix
              source_protocol: static
            set:
              metric:
                rtt_action: subtract
        state: merged

    # After state:
    # ------------
    #
    # sonic# show running-configuration route-map
    # !
    # route-map rm1 permit 80
    #  match as-path bgp_as1
    #  match evpn default-route
    #  match evpn vni 735
    #  match ip address prefix-list ip_pfx_list1
    #  match ipv6 address prefix-list ipv6_pfx_list1
    #  match interface Ethernet4
    #  match community bgp_comm_list1
    #  match ext-community bgp_ext_comm1
    #  match tag 7284
    #  match local-preference 8000
    #  match source-vrf Vrf1
    #  match peer 10.20.30.40
    #  match source-protocol bgp
    #  match metric 400
    #  match origin egp
    #  set as-path prepend 200,315,7135
    #  set community 35:58 79:150 308:650 local-AS no-advertise no-export no-peer additive
    #  set extcommunity rt 30:40
    #  set extcommunity soo 10.73.14.9:78
    #  set comm-list bgp_comm_list2 delete
    #  set metric 870
    #  set ip next-hop 10.48.16.18
    #  set ip next-hop native true
    #  set ipv6 next-hop global 30::30
    #  set ipv6 next-hop prefer-global
    # set ipv6 next-hop native true
    #  set local-preference 635
    #  set origin egp
    #  set weight 93471
    #  set tag 65
    # !
    # route-map rm1 deny 3047
    #  match evpn route-type multicast
    #  match peer Ethernet6
    #  match source-protocol ospf
    #  match origin incomplete
    #  set metric +rtt
    #  set origin incomplete
    # !
    # route-map rm3 deny 285
    #  match evpn route-type macip
    #  call rm1
    #  match peer 87:95:15::53
    #  match source-protocol connected
    #  match origin igp
    #  set community none
    #  set metric rtt
    #  set origin igp
    # !
    # route-map rm4 permit 480
    #  match evpn route-type prefix
    #  match source-protocol static
    #  set metric -rtt
    # ------------


    # Using "merged" state to update and add configuration
    #
    # Before state:
    # ------------
    #
    # sonic# show running-configuration route-map
    # !
    # route-map rm1 permit 80
    #  match as-path bgp_as1
    #  match evpn default-route
    #  match evpn vni 735
    #  match ip address prefix-list ip_pfx_list1
    #  match ipv6 address prefix-list ipv6_pfx_list1
    #  match interface Ethernet4
    #  match community bgp_comm_list1
    #  match ext-community bgp_ext_comm1
    #  match tag 7284
    #  match local-preference 8000
    #  match source-vrf Vrf1
    #  match peer 10.20.30.40
    #  match source-protocol bgp
    #  match metric 400
    #  match origin egp
    #  set as-path prepend 200,315,7135
    #  set community 35:58 79:150 308:650 local-AS no-advertise no-export no-peer additive
    #  set extcommunity rt 30:40
    #  set extcommunity soo 10.73.14.9:78
    #  set comm-list bgp_comm_list2 delete
    #  set metric 870
    #  set ip next-hop 10.48.16.18
    #  set ipv6 next-hop global 30::30
    #  set ipv6 next-hop prefer-global
    #  set local-preference 635
    #  set origin egp
    #  set weight 93471
    #  set tag 65
    # !
    # route-map rm1 deny 3047
    #  match evpn route-type multicast
    #  match peer Ethernet6
    #  match source-protocol ospf
    #  match origin incomplete
    #  set metric +rtt
    #  set origin incomplete
    # !
    # route-map rm3 deny 285
    #  match evpn route-type macip
    #  call rm1
    #  match peer 87:95:15::53
    #  match source-protocol connected
    #  match origin igp
    #  set community none
    #  set metric rtt
    #  set origin igp
    # !
    # route-map rm4 permit 480
    #  match evpn route-type prefix
    #  match source-protocol static
    #  set metric -rtt
    # ------------
    #
    - name: Merge additional and modified route map configuration
      dellemc.enterprise_sonic.sonic_route_maps:
        config:
          - map_name: rm1
            action: permit
            sequence_num: 80
            match:
              as_path: bgp_as2
              community: bgp_comm_list3
              evpn:
                route_type: prefix
                vni: 850
              interface: Vlan7
              ip:
                address: ip_pfx_list2
                next_hop: ip_pfx_list3
              peer:
                interface: Portchannel14
            set:
              as_path_prepend: 188,257
              community:
                community_number:
                  - "45:736"
              ipv6_next_hop:
                prefer_global: false
              metric:
                rtt_action: add
          - map_name: rm1
            action: deny
            sequence_num: 3047
            match:
              as_path: bgp_as3
              ext_comm: bgp_ext_comm2
              origin: igp
            set:
              metric:
                rtt_action: subtract
          - map_name: rm2
            action: permit
            sequence_num: 100
            match:
              interface: Ethernet16
            set:
              as_path_prepend: 200,300,400
              ipv6_next_hop:
                global_addr: 37::58
                prefer_global: true
              metric: 8000
          - map_name: rm3
            action: deny
            sequence_num: 285
            match:
              local_preference: 14783
              source_protocol: bgp
            set:
              community:
                community_attributes:
                  - no_advertise
        state: merged

    # After state:
    # ------------
    #
    # sonic# show running-configuration route-map
    # !
    # route-map rm1 permit 80
    #  match as-path bgp_as2
    #  match evpn default-route
    #  match evpn route-type prefix
    #  match evpn vni 850
    #  match ip address prefix-list ip_pfx_list2
    #  match ipv6 address prefix-list ipv6_pfx_list1
    #  match interface Vlan7
    #  match community bgp_comm_list3
    #  match ext-community bgp_ext_comm1
    #  match tag 7284
    #  match local-preference 8000
    #  match source-vrf Vrf1
    #  match ip next-hop prefix-list ip_pfx_list3
    #  match peer PortChannel 14
    #  match source-protocol bgp
    #  match metric 400
    #  match origin egp
    #  set as-path prepend 188,257
    #  set community 35:58 79:150 308:650 45:736 local-AS no-advertise no-export no-peer additive
    #  set extcommunity rt 30:40
    #  set extcommunity soo 10.73.14.9:78
    #  set comm-list bgp_comm_list2 delete
    #  set metric +rtt
    #  set ip next-hop 10.48.16.18
    #  set ipv6 next-hop global 30::30
    #  set local-preference 635
    #  set origin egp
    #  set weight 93471
    #  set tag 65
    # !
    # route-map rm1 deny 3047
    #  match as-path bgp_as3
    #  match evpn route-type multicast
    #  match ext-community bgp_ext_comm2
    #  match peer Ethernet6
    #  match source-protocol ospf
    #  match origin igp
    #  set metric -rtt
    #  set origin incomplete
    # !
    # route-map rm2 permit 100
    #  match interface Ethernet16
    #  set as-path prepend 200,300,400
    #  set ipv6 next-hop global 37::58
    #  set ipv6 next-hop prefer-global
    #  set metric 8000
    # !
    # route-map rm3 deny 285
    #  match evpn route-type macip
    #  match local-preference 14783
    #  call rm1
    #  match peer 87:95:15::53
    #  match source-protocol bgp
    #  match origin igp
    #  set community no-advertise
    #  set metric rtt
    #  set origin igp
    # !
    # route-map rm4 permit 480
    #  match evpn route-type prefix
    #  match source-protocol static
    #  set metric -rtt


    # Using "replaced" state to replace the contents of a list
    #
    # Before state:
    # ------------
    #
    # sonic(config-route-map)# do show running-configuration route-map rm1 80
    # !
    # route-map rm1 permit 80
    #  match as-path bgp_as2
    #  match evpn default-route
    #  match evpn route-type prefix
    #  match evpn vni 850
    #  match ip address prefix-list ip_pfx_list2
    #  match ipv6 address prefix-list ipv6_pfx_list1
    #  match interface Vlan7
    #  match community bgp_comm_list3
    #  match ext-community bgp_ext_comm1
    #  match tag 7284
    #  match local-preference 8000
    #  match source-vrf Vrf1
    #  match ip next-hop prefix-list ip_pfx_list3
    #  match peer PortChannel 14
    #  match source-protocol bgp
    #  match metric 400
    #  match origin egp
    #  set as-path prepend 188,257
    #  set community 35:58 79:150 308:650 45:736 local-AS no-export no-peer additive
    #  set extcommunity rt 30:40
    #  set extcommunity soo 10.73.14.9:78
    #  set comm-list bgp_comm_list2 delete
    #  set metric +rtt
    #  set ip next-hop 10.48.16.18
    #  set ipv6 next-hop global 30::30
    #  set local-preference 635
    #  set origin egp
    #  set weight 93471
    #  set tag 65
    # ------------
    - name: Replace a list
      dellemc.enterprise_sonic.sonic_route_maps:
        config:
          - map_name: rm1
            action: permit
            sequence_num: 80
            set:
              community:
                community_number:
                  - "15:30"
                  - "26:54"
        state: replaced

    # After state:
    # ------------
    #
    # sonic#show running-configuration route-map rm1 80
    # !
    # route-map rm1 permit 80
    #  match as-path bgp_as2
    #  match evpn default-route
    #  match evpn route-type prefix
    #  match evpn vni 850
    #  match ip address prefix-list ip_pfx_list2
    #  match ipv6 address prefix-list ipv6_pfx_list1
    #  match interface Vlan7
    #  match community bgp_comm_list3
    #  match ext-community bgp_ext_comm1
    #  match tag 7284
    #  match local-preference 8000
    #  match source-vrf Vrf1
    #  match ip next-hop prefix-list ip_pfx_list3
    #  match peer PortChannel 14
    #  match source-protocol bgp
    #  match metric 400
    #  match origin egp
    #  set as-path prepend 188,257
    #  set community 15:30 26:54 local-AS no-export no-peer additive
    #  set extcommunity rt 30:40
    #  set extcommunity soo 10.73.14.9:78
    #  set comm-list bgp_comm_list2 delete
    #  set metric +rtt
    #  set ip next-hop 10.48.16.18
    #  set ipv6 next-hop global 30::30
    #  set local-preference 635
    #  set origin egp
    #  set weight 93471
    #  set tag 65


    # Using "replaced" state to replace the contents of dictionaries
    #
    # Before state:
    # ------------
    # sonic# show running-configuration route-map
    # !
    # route-map rm1 permit 80
    #  match as-path bgp_as2
    #  match evpn default-route
    #  match evpn route-type prefix
    #  match evpn vni 850
    #  match ip address prefix-list ip_pfx_list2
    #  match ipv6 address prefix-list ipv6_pfx_list1
    #  match interface Vlan7
    #  match community bgp_comm_list3
    #  match ext-community bgp_ext_comm1
    #  match tag 7284
    #  match local-preference 8000
    #  match source-vrf Vrf1
    #  match ip next-hop prefix-list ip_pfx_list3
    #  match peer PortChannel 14
    #  match source-protocol bgp
    #  match metric 400
    #  match origin egp
    #  set as-path prepend 188,257
    #  set community 15:30 26:54 local-AS no-export no-peer additive
    #  set extcommunity rt 30:40
    #  set extcommunity soo 10.73.14.9:78
    #  set comm-list bgp_comm_list2 delete
    #  set metric +rtt
    #  set ip next-hop 10.48.16.18
    #  set ipv6 next-hop global 30::30
    #  set local-preference 635
    #  set origin egp
    #  set weight 93471
    #  set tag 65
    # !
    # route-map rm1 deny 3047
    #  match as-path bgp_as3
    #  match evpn route-type multicast
    #  match ext-community bgp_ext_comm2
    #  match peer Ethernet6
    #  match source-protocol ospf
    #  match origin igp
    #  set metric -rtt
    #  set origin incomplete
    # !
    # route-map rm2 permit 100
    #  match interface Ethernet16
    #  set as-path prepend 200,300,400
    #  set ipv6 next-hop global 37::58
    #  set ipv6 next-hop prefer-global
    #  set metric 8000
    # !
    # route-map rm3 deny 285
    #  match evpn route-type macip
    #  match local-preference 14783
    #  call rm1
    #  match peer 87:95:15::53
    #  match source-protocol bgp
    #  match origin igp
    #  set community no-advertise
    #  set metric rtt
    #  set origin igp
    # !
    # route-map rm4 permit 480
    #  match evpn route-type prefix
    #  match source-protocol static
    #  set metric -rtt
    # ------------
    - name: Replace dictionaries
      dellemc.enterprise_sonic.sonic_route_maps:
        config:
          - map_name: rm1
            action: permit
            sequence_num: 80
            match:
              evpn:
                route_type: multicast
              ip:
                address: ip_pfx_list1
            set:
              community:
                community_attributes:
                  - no_advertise
              extcommunity:
                rt:
                  - "20:20"
          - map_name: rm2
            action: permit
            sequence_num: 100
            set:
              ipv6_next_hop:
                global_addr: 45::90
                native: true
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show running-configuration route-map
    # !
    # route-map rm1 permit 80
    #  match as-path bgp_as2
    #  match evpn route-type multicast
    #  match ip address prefix-list ip_pfx_list1
    #  match ipv6 address prefix-list ipv6_pfx_list1
    #  match interface Vlan7
    #  match community bgp_comm_list3
    #  match ext-community bgp_ext_comm1
    #  match tag 7284
    #  match local-preference 8000
    #  match source-vrf Vrf1
    #  match peer PortChannel 14
    #  match source-protocol bgp
    #  match metric 400
    #  match origin egp
    #  set as-path prepend 188,257
    #  set community no-advertise
    #  set extcommunity rt 20:20
    #  set comm-list bgp_comm_list2 delete
    #  set metric +rtt
    #  set ip next-hop 10.48.16.18
    #  set ipv6 next-hop global 30::30
    #  set local-preference 635
    #  set origin egp
    #  set weight 93471
    #  set tag 65
    # !
    # route-map rm1 deny 3047
    #  match as-path bgp_as3
    #  match evpn route-type multicast
    #  match ext-community bgp_ext_comm2
    #  match peer Ethernet6
    #  match source-protocol ospf
    #  match origin igp
    #  set metric -rtt
    #  set origin incomplete
    # !
    # route-map rm2 permit 100
    #  match interface Ethernet16
    #  set as-path prepend 200,300,400
    #  set metric 8000
    #  set ipv6 next-hop global 45::90
    # set ipv6 next-hop native true
    # !
    # route-map rm3 deny 285
    #  match evpn route-type macip
    #  match local-preference 14783
    #  call rm1
    #  match peer 87:95:15::53
    #  match source-protocol bgp
    #  match origin igp
    #  set community no-advertise
    #  set metric rtt
    #  set origin igp
    # !
    # route-map rm4 permit 480
    #  match evpn route-type prefix
    #  match source-protocol static
    #  set metric -rtt


    # Using "overridden" state to override all existing configuration with new
    # configuration
    #
    # Before state:
    # ------------
    #
    # sonic# show running-configuration route-map
    # !
    # route-map rm1 permit 80
    #  match as-path bgp_as2
    #  match evpn route-type multicast
    #  match ip address prefix-list ip_pfx_list1
    #  match ipv6 address prefix-list ipv6_pfx_list1
    #  match interface Vlan7
    #  match community bgp_comm_list3
    #  match ext-community bgp_ext_comm1
    #  match tag 7284
    #  match local-preference 8000
    #  match source-vrf Vrf1
    #  match peer PortChannel 14
    #  match source-protocol bgp
    #  match metric 400
    #  match origin egp
    #  set as-path prepend 188,257
    #  set community no-advertise
    #  set extcommunity rt 30:40
    #  set extcommunity rt 20:20
    #  set comm-list bgp_comm_list2 delete
    #  set metric +rtt
    #  set ip next-hop 10.48.16.18
    #  set ipv6 next-hop global 30::30
    #  set local-preference 635
    #  set origin egp
    #  set weight 93471
    #  set tag 65
    # !
    # route-map rm1 deny 3047
    #  match as-path bgp_as3
    #  match evpn route-type multicast
    #  match ext-community bgp_ext_comm2
    #  match peer Ethernet6
    #  match source-protocol ospf
    #  match origin igp
    #  set metric -rtt
    #  set origin incomplete
    # !
    # route-map rm2 permit 100
    #  match interface Ethernet16
    #  set as-path prepend 200,300,400
    #  set metric 8000
    #  set ipv6 next-hop global 45::90
    # !
    # route-map rm3 deny 285
    #  match evpn route-type macip
    #  match local-preference 14783
    #  call rm1
    #  match peer 87:95:15::53
    #  match source-protocol bgp
    #  match origin igp
    #  set community no-advertise
    #  set metric rtt
    #  set origin igp
    # !
    # route-map rm4 permit 480
    #  match evpn route-type prefix
    #  match source-protocol static
    #  set metric -rtt
    # ------------
    - name: Override all route map configuration with new configuration
      dellemc.enterprise_sonic.sonic_route_maps:
        config:
          - map_name: rm5
            action: permit
            sequence_num: 250
            match:
              interface: Ethernet28
            set:
              as_path_prepend: 150,275
              metric: 7249
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show running-configuration route-map
    # !
    # route-map rm5 permit 250
    #  match interface Ethernet28
    #  set as-path prepend 150,275
    #  set metric 7249


    # Using "overridden" state to override all existing configuration with new
    # configuration. (Restore previous configuration.)
    #
    # Before state:
    # ------------
    #
    # sonic# show running-configuration route-map
    # !
    # route-map rm5 permit 250
    #  match interface Ethernet28
    #  set as-path prepend 150,275
    #  set metric 7249
    # ------------
    - name: Override (restore) all route map configuration with older configuration
      dellemc.enterprise_sonic.sonic_route_maps:
        config:
          - map_name: rm1
            action: permit
            sequence_num: 80
            match:
              as_path: bgp_as2
              community: bgp_comm_list3
              evpn:
                default_route: true
                route_type: prefix
                vni: 850
              ext_comm: bgp_ext_comm1
              interface: Vlan7
              ip:
                address: ip_pfx_list2
                next_hop: ip_pfx_list3
              ipv6:
                address: ipv6_pfx_list1
              local_preference: 8000
              metric: 400
              origin: egp
              peer:
                interface: Portchannel14
              source_protocol: bgp
              source_vrf: Vrf1
              tag: 7284
            set:
              as_path_prepend: 188,257
              comm_list_delete: bgp_comm_list2
              community:
                community_number:
                  - "35:58"
                  - "79:150"
                  - "308:650"
                  - "45:736"
                community_attributes:
                  - local_as
                  - no_export
                  - no_peer
                  - additive
              extcommunity:
                rt:
                  - "30:40"
                soo:
                  - "10.73.14.9:78"
              ip_next_hop:
                address: 10.48.16.18
                native: false
              ipv6_next_hop:
                global_addr: 30::30
                native: false
              local_preference: 635
              metric:
                rtt_action: add
              origin: egp
              weight: 93471
              tag: 65
          - map_name: rm1
            action: deny
            sequence_num: 3047
            match:
              as_path: bgp_as3
              evpn:
                route_type: multicast
              ext_comm: bgp_ext_comm2
              origin: igp
              peer:
                interface: Ethernet6
              source_protocol: ospf
            set:
              metric:
                rtt_action: subtract
              origin: incomplete
          - map_name: rm2
            action: permit
            sequence_num: 100
            match:
              interface: Ethernet16
            set:
              as_path_prepend: 200,300,400
              ipv6_next_hop:
                global_addr: 37::58
                prefer_global: true
              metric: 8000
          - map_name: rm3
            action: deny
            sequence_num: 285
            match:
              evpn:
                route_type: macip
              origin: igp
              peer:
                ipv6: 87:95:15::53
              local_preference: 14783
              source_protocol: bgp
            set:
              community:
                community_attributes:
                  - no_advertise
              metric:
                rtt_action: set
              origin: igp
            call: rm1
          - map_name: rm4
            action: permit
            sequence_num: 480
            match:
              evpn:
                route_type: prefix
              source_protocol: static
            set:
              metric:
                rtt_action: subtract
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show running-configuration route-map
    # !
    # route-map rm1 permit 80
    #  match as-path bgp_as2
    #  match evpn default-route
    #  match evpn route-type prefix
    #  match evpn vni 850
    #  match ip address prefix-list ip_pfx_list2
    #  match ipv6 address prefix-list ipv6_pfx_list1
    #  match interface Vlan7
    #  match community bgp_comm_list3
    #  match ext-community bgp_ext_comm1
    #  match tag 7284
    #  match local-preference 8000
    #  match source-vrf Vrf1
    #  match ip next-hop prefix-list ip_pfx_list3
    #  match peer PortChannel 14
    #  match source-protocol bgp
    #  match metric 400
    #  match origin egp
    #  set as-path prepend 188,257
    #  set community 35:58 79:150 308:650 45:736 local-AS no-export no-peer additive
    #  set extcommunity rt 30:40
    #  set extcommunity soo 10.73.14.9:78
    #  set comm-list bgp_comm_list2 delete
    #  set metric +rtt
    #  set ip next-hop 10.48.16.18
    #  set ip next-hop native false
    #  set ipv6 next-hop global 30::30
    #  set ipv6 next-hop native false
    #  set local-preference 635
    #  set origin egp
    #  set weight 93471
    #  set tag 65
    # !
    # route-map rm1 deny 3047
    #  match as-path bgp_as3
    #  match evpn route-type multicast
    #  match ext-community bgp_ext_comm2
    #  match peer Ethernet6
    #  match source-protocol ospf
    #  match origin igp
    #  set metric -rtt
    #  set origin incomplete
    # !
    # route-map rm2 permit 100
    #  match interface Ethernet16
    #  set as-path prepend 200,300,400
    #  set ipv6 next-hop global 37::58
    #  set ipv6 next-hop prefer-global
    #  set metric 8000
    # !
    # route-map rm3 deny 285
    #  match evpn route-type macip
    #  match local-preference 14783
    #  call rm1
    #  match peer 87:95:15::53
    #  match source-protocol bgp
    #  match origin igp
    #  set community no-advertise
    #  set metric rtt
    #  set origin igp
    # !
    # route-map rm4 permit 480
    #  match evpn route-type prefix
    #  match source-protocol static
    #  set metric -rtt


    # Using "deleted" state to remove configuration
    #
    # Before state:
    # ------------
    #
    # sonic# show running-configuration route-map rm1 80
    # !
    # route-map rm1 permit 80
    #  match as-path bgp_as2
    #  match evpn default-route
    #  match evpn route-type prefix
    #  match evpn vni 850
    #  match ip address prefix-list ip_pfx_list2
    #  match ipv6 address prefix-list ipv6_pfx_list1
    #  match interface Vlan7
    #  match community bgp_comm_list3
    #  match ext-community bgp_ext_comm1
    #  match tag 7284
    #  match local-preference 8000
    #  match source-vrf Vrf1
    #  match ip next-hop prefix-list ip_pfx_list3
    #  match peer PortChannel 14
    #  match source-protocol bgp
    #  match metric 400
    #  match origin egp
    #  set as-path prepend 188,257
    #  set community 35:58 79:150 308:650 45:736 local-AS no-export no-peer additive
    #  set extcommunity rt 30:40
    #  set extcommunity soo 10.73.14.9:78
    #  set comm-list bgp_comm_list2 delete
    #  set metric +rtt
    #  set ip next-hop 10.48.16.18
    #  set ip next-hop native true
    #  set ipv6 next-hop global 30::30
    #  set local-preference 635
    #  set origin egp
    #  set weight 93471
    #  set tag 65
    # ------------
    - name: Delete selected route map configuration
      dellemc.enterprise_sonic.sonic_route_maps:
        config:
          - map_name: rm1
            action: permit
            sequence_num: 80
            match:
              as_path: bgp_as2
              community: bgp_comm_list3
              evpn:
                vni: 850
              ip:
                address: ip_pfx_list2
            set:
              as_path_prepend: 188,257
              ip_next_hop:
              address: 10.48.16.18
              native: true
              ipv6_next_hop:
                native: true
              community:
                community_number:
                  - "35:58"
                community_attributes:
                  - local_as
              extcommunity:
                rt:
                  - "30:40"
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration route-map rm1 80
    # !
    # route-map rm1 permit 80
    #  match evpn default-route
    #  match evpn route-type prefix
    #  match ipv6 address prefix-list ipv6_pfx_list1
    #  match interface Vlan7
    #  match ext-community bgp_ext_comm1
    #  match tag 7284
    #  match local-preference 8000
    #  match source-vrf Vrf1
    #  match ip next-hop prefix-list ip_pfx_list3
    #  match peer PortChannel 14
    #  match source-protocol bgp
    #  match metric 400
    #  match origin egp
    #  set community 79:150 308:650 45:736 no-export no-peer additive
    #  set extcommunity soo 10.73.14.9:78
    #  set comm-list bgp_comm_list2 delete
    #  set metric +rtt
    #  set ipv6 next-hop global 30::30
    #  set local-preference 635
    #  set origin egp
    #  set weight 93471
    #  set tag 65


    # Using "deleted" state to remove a route map or route map subset
    #
    # Before state:
    # ------------
    #
    # sonic# show running-configuration route-map
    # !
    # route-map rm1 permit 80
    #  match evpn default-route
    #  match evpn route-type prefix
    #  match ipv6 address prefix-list ipv6_pfx_list1
    #  match interface Vlan7
    #  match ext-community bgp_ext_comm1
    #  match tag 7284
    #  match local-preference 8000
    #  match source-vrf Vrf1
    #  match ip next-hop prefix-list ip_pfx_list3
    #  match peer PortChannel 14
    #  match source-protocol bgp
    #  match metric 400
    #  match origin egp
    #  set community 79:150 308:650 45:736 no-export no-peer additive
    #  set extcommunity soo 10.73.14.9:78
    #  set comm-list bgp_comm_list2 delete
    #  set metric +rtt
    #  set ip next-hop 10.48.16.18
    #  set ipv6 next-hop global 30::30
    #  set local-preference 635
    #  set origin egp
    #  set weight 93471
    #  set tag 65
    # !
    # route-map rm1 deny 3047
    #  match as-path bgp_as3
    #  match evpn route-type multicast
    #  match ext-community bgp_ext_comm2
    #  match peer Ethernet6
    #  match source-protocol ospf
    #  match origin igp
    #  set metric -rtt
    #  set origin incomplete
    # !
    # route-map rm2 permit 100
    #  match interface Ethernet16
    #  set as-path prepend 200,300,400
    #  set metric 8000
    #  set ipv6 next-hop prefer-global
    #  set ipv6 next-hop global 37::58
    # !
    # route-map rm3 deny 285
    #  match evpn route-type macip
    #  match local-preference 14783
    #  call rm1
    #  match peer 87:95:15::53
    #  match source-protocol bgp
    #  match origin igp
    #  set community no-advertise
    #  set metric rtt
    #  set origin igp
    # !
    # route-map rm4 permit 480
    #  match evpn route-type prefix
    #  match source-protocol static
    #  set metric -rtt
    # ------------
    - name: Delete a route map subset or a route map
      dellemc.enterprise_sonic.sonic_route_maps:
        config:
          - map_name: rm1
            sequence_num: 3047
          - map_name: rm2
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration route-map
    # !
    # route-map rm1 permit 80
    #  match evpn default-route
    #  match evpn route-type prefix
    #  match ipv6 address prefix-list ipv6_pfx_list1
    #  match interface Vlan7
    #  match ext-community bgp_ext_comm1
    #  match tag 7284
    #  match local-preference 8000
    #  match source-vrf Vrf1
    #  match ip next-hop prefix-list ip_pfx_list3
    #  match peer PortChannel 14
    #  match source-protocol bgp
    #  match metric 400
    #  match origin egp
    #  set community 79:150 308:650 45:736 no-export no-peer additive
    #  set extcommunity soo 10.73.14.9:78
    #  set comm-list bgp_comm_list2 delete
    #  set metric +rtt
    #  set ip next-hop 10.48.16.18
    #  set ipv6 next-hop global 30::30
    #  set local-preference 635
    #  set origin egp
    #  set weight 93471
    #  set tag 65
    # !
    # route-map rm3 deny 285
    #  match evpn route-type macip
    #  match local-preference 14783
    #  call rm1
    #  match peer 87:95:15::53
    #  match source-protocol bgp
    #  match origin igp
    #  set community no-advertise
    #  set metric rtt
    #  set origin igp
    # !
    # route-map rm4 permit 480
    #  match evpn route-type prefix
    #  match source-protocol static
    #  set metric -rtt


    # Using "deleted" state to remove all route map configuration
    #
    # Before state:
    # ------------
    #
    # sonic# show running-configuration route-map
    # !
    # route-map rm1 permit 80
    #  match evpn default-route
    #  match evpn route-type prefix
    #  match ipv6 address prefix-list ipv6_pfx_list1
    #  match interface Vlan7
    #  match ext-community bgp_ext_comm1
    #  match tag 7284
    #  match local-preference 8000
    #  match source-vrf Vrf1
    #  match ip next-hop prefix-list ip_pfx_list3
    #  match peer PortChannel 14
    #  match source-protocol bgp
    #  match metric 400
    #  match origin egp
    #  set community 79:150 308:650 45:736 no-export no-peer additive
    #  set extcommunity soo 10.73.14.9:78
    #  set comm-list bgp_comm_list2 delete
    #  set metric +rtt
    #  set ip next-hop 10.48.16.18
    #  set ipv6 next-hop global 30::30
    #  set local-preference 635
    #  set origin egp
    #  set weight 93471
    #  set tag 65
    # !
    # route-map rm3 deny 285
    #  match evpn route-type macip
    #  match local-preference 14783
    #  call rm1
    #  match peer 87:95:15::53
    #  match source-protocol bgp
    #  match origin igp
    #  set community no-advertise
    #  set metric rtt
    #  set origin igp
    # !
    # route-map rm4 permit 480
    #  match evpn route-type prefix
    #  match source-protocol static
    #  set metric -rtt
    # ------------
    - name: Delete all route map configuration
      dellemc.enterprise_sonic.sonic_route_maps:
        config: []
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration route-map
    # sonic#
    # (no route map configuration present)



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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format
     as the parameters above.</div>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format
     as the parameters above.</div>
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

- Kerry Meyer (@kerry-meyer)
