.. _dellemc.enterprise_sonic.sonic_bgp_af_module:


*************************************
dellemc.enterprise_sonic.sonic_bgp_af
*************************************

**Manage global BGP address-family and its parameters**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of global BGP_AF parameters on devices running Enterprise SONiC.
- bgp_as and vrf_name must be created in advance on the device.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="6">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="6">
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
                        <div>Specifies the BGP_AF related configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address_family</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies BGP address family related configurations.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>afis</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of address families, such as ipv4, ipv6, and l2vpn.</div>
                        <div>afi and safi are required together.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>advertise_all_vni</b>
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
                        <div>Specifies the advertise all vni flag.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>advertise_default_gw</b>
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
                        <div>Specifies the advertise default gateway flag.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>advertise_pip</b>
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
                        <div>Enables advertise PIP</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>advertise_pip_ip</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>PIP IPv4 address</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>advertise_pip_peer_ip</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>PIP peer IPv4 address</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>advertise_svi_ip</b>
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
                        <div>Enables advertise SVI MACIP routes</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Type of address family to configure.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>aggregate_address_config</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 2.5.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>Aggregate address configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>as_set</b>
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
                        <div>Enables/disables generation of AS set path information</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>policy_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Preconfigured routing policy (route map name) to be applied to aggregate network</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>prefix</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Aggregate address prefix</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>summary_only</b>
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
                        <div>Enables/disables restriction of route information included in updates</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dampening</b>
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
                        <div>Enable route flap dampening if set to true</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dup_addr_detection</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.1.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>Duplicate address detection configuration.</div>
                        <div><em>max_moves</em> and <em>time</em> are required together.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>enabled</b>
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
                        <div>Enable duplicate address detection.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>freeze</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies duplicate address detection freeze.</div>
                        <div>Value can be <code>permanent</code> or time in the range 30 to 3600.</div>
                        <div><code>permanent</code> - Enable permanent freeze.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>max_moves</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the max allowed moves before address is detected as duplicate.</div>
                        <div>The range is from 2 to 1000.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>time</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the duplicate address detection time.</div>
                        <div>The range is from 2 to 1800.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>import</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 2.5.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the routes to be imported to this address family.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vrf</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Import routes from other VRFs.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>route_map</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
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
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vrf_list</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the VRFs to import routes from.</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>max_path</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the maximum paths of ibgp and ebgp count.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ebgp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the count of the ebgp multipaths count.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ibgp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the count of the ibgp multipaths count.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>network</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Enable routing on an IP network for each prefix provided in the network</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>rd</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the route distiguisher to be used by the VRF instance.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>redistribute</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the redistribute information from another routing protocol.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>metric</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the metric for redistributed routes.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>protocol</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ospf</li>
                                    <li>static</li>
                                    <li>connected</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the protocol for configuring redistribute information.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>route_map</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the route map reference.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>route_advertise_list</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of advertise routes</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>advertise_afi</b>
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
                        </ul>
                </td>
                <td>
                        <div>Specifies the address family</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>route_map</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the route-map reference</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>rt_in</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Route-targets to be imported.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>rt_out</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Route-targets to be exported.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Specifies the type of communication for the address family.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vnis</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>VNI configuration for the EVPN.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>advertise_default_gw</b>
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
                        <div>Specifies the advertise default gateway flag.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>advertise_svi_ip</b>
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
                        <div>Enables advertise SVI MACIP routes</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>rd</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the route distiguisher to be used by the VRF instance.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>rt_in</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Route-targets to be imported.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>rt_out</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Route-targets to be exported.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vni_number</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the VNI number.</div>
                </td>
            </tr>



            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="5">
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
                <td colspan="5">
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
                <td colspan="6">
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
                                    <li>overridden</li>
                                    <li>replaced</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the operation to be performed on the BGP_AF process configured on the device.</div>
                        <div>In case of merged, the input configuration is merged with the existing BGP_AF configuration on the device.</div>
                        <div>In case of deleted, the existing BGP_AF configuration is removed from the device.</div>
                        <div>In case of replaced, the existing BGP_AF of specified BGP AS will be replaced with provided configuration.</div>
                        <div>In case of overridden, the existing BGP_AF configuration will be overridden with the provided configuration.</div>
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
    # sonic# show running-configuration bgp
    # !
    # router bgp 51 vrf VrfReg1
    #  log-neighbor-changes
    #  timers 60 180
    #  !
    #  address-family ipv4 unicast
    #   maximum-paths 1
    #   maximum-paths ibgp 1
    #   network 3.3.3.3/16
    #   aggregate-address 1.1.1.1/1
    #   aggregate-address 5.5.5.5/5 as-set summary-only route-map rmap-1
    #   dampening
    #   import vrf route-map rmap-1
    #   import vrf default
    # !
    # router bgp 51
    #  router-id 111.2.2.41
    #  timers 60 180
    #  !
    #  address-family ipv4 unicast
    #   maximum-paths 1
    #   maximum-paths ibgp 1
    #   dampening
    #  !
    #  address-family ipv6 unicast
    #   redistribute connected route-map bb metric 21
    #   redistribute ospf route-map aa metric 27
    #   redistribute static route-map bb metric 26
    #   maximum-paths 4
    #   maximum-paths ibgp 5
    #  !
    #  address-family l2vpn evpn
    #   advertise-svi-ip
    #   advertise ipv6 unicast route-map aa
    #   rd 3.3.3.3:33
    #   route-target import 22:22
    #   route-target export 33:33
    #   dup-addr-detection
    #   advertise-pip ip 1.1.1.1 peer-ip 2.2.2.2
    #   !
    #   vni 1
    #    advertise-default-gw
    #    advertise-svi-ip
    #    rd 5.5.5.5:55
    #    route-target import 88:88
    #    route-target export 77:77
    #

    - name: Delete BGP Address family configuration from the device
      dellemc.enterprise_sonic.sonic_bgp_af:
        config:
          - bgp_as: 51
            address_family:
              afis:
                - afi: l2vpn
                  safi: evpn
                  advertise_pip: true
                  advertise_pip_ip: "1.1.1.1"
                  advertise_pip_peer_ip: "2.2.2.2"
                  advertise_svi_ip: true
                  advertise_all_vni: false
                  advertise_default_gw: false
                  route_advertise_list:
                    - advertise_afi: ipv6
                      route_map: aa
                  rd: "3.3.3.3:33"
                  rt_in:
                    - "22:22"
                  rt_out:
                    - "33:33"
                  vnis:
                    - vni_number: 1
                - afi: ipv4
                  safi: unicast
                - afi: ipv6
                  safi: unicast
                  max_path:
                    ebgp: 2
                    ibgp: 5
                  redistribute:
                    - metric: "21"
                      protocol: connected
                      route_map: bb
                    - metric: "27"
                      protocol: ospf
                      route_map: aa
                    - metric: "26"
                      protocol: static
                      route_map: bb
          - bgp_as: 51
            vrf_name: VrfReg1
            address_family:
              afis:
                - afi: ipv4
                  safi: unicast
                  import:
                    vrf:
                      vrf_list:
                        - default
                      route_map: rmap-1
                  aggregate_address_config:
                    - prefix: "1.1.1.1/1"
                    - prefix: "5.5.5.5/5"
                      as_set: true
                      policy_name: rmap-1
                      summary_only: true
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration bgp
    # !
    # router bgp 51 vrf VrfReg1
    #  log-neighbor-changes
    #  timers 60 180
    #  !
    #  address-family ipv4 unicast
    #   maximum-paths 1
    #   maximum-paths ibgp 1
    #   network 3.3.3.3/16
    #   aggregate-address 5.5.5.5/5
    #   dampening
    # !
    # router bgp 51
    #  router-id 111.2.2.41
    #  timers 60 180
    #  !
    #  address-family ipv6 unicast
    #  !
    #  address-family l2vpn evpn
    #   dup-addr-detection
    #

    #  Using "deleted" state
    #
    #  Before state:
    #  -------------
    #
    # sonic# show running-configuration bgp
    # !
    # router bgp 51 vrf VrfReg1
    #  log-neighbor-changes
    #  timers 60 180
    #  !
    #  address-family ipv4 unicast
    #   maximum-paths 1
    #   maximum-paths ibgp 1
    #   network 3.3.3.3/16
    #   aggregate-address 5.5.5.5/5 as-set summary-only route-map rmap-1
    #   dampening
    #   import vrf route-map rmap-1
    #   import vrf default
    # !
    # router bgp 51
    #  router-id 111.2.2.41
    #  timers 60 180
    #  !
    #  address-family ipv6 unicast
    #  !
    #  address-family l2vpn evpn
    #

    - name: Delete All BGP address family configurations
      dellemc.enterprise_sonic.sonic_bgp_af:
        config:
        state: deleted


    # After state:
    # ------------
    #
    # sonic# show running-configuration bgp
    # !
    # router bgp 51 vrf VrfReg1
    #  log-neighbor-changes
    #  timers 60 180
    # !
    # router bgp 51
    #  router-id 111.2.2.41
    #  timers 60 180
    #

    #  Using "merged" state
    #
    #  Before state:
    #  -------------
    #
    # sonic# show running-configuration bgp
    # !
    # router bgp 51 vrf VrfReg1
    #  log-neighbor-changes
    #  timers 60 180
    # !
    # router bgp 51
    #  router-id 111.2.2.41
    #  timers 60 180
    #  !
    #  address-family l2vpn evpn
    #   dup-addr-detection
    #

    - name: Merge provided BGP address family configuration on the device.
      dellemc.enterprise_sonic.sonic_bgp_af:
        config:
          - bgp_as: 51
            address_family:
              afis:
                - afi: l2vpn
                  safi: evpn
                  advertise_pip: true
                  advertise_pip_ip: "3.3.3.3"
                  advertise_pip_peer_ip: "4.4.4.4"
                  advertise_svi_ip: true
                  advertise_all_vni: false
                  advertise_default_gw: false
                  dup_addr_detection:
                    freeze: permanent
                    max_moves: 10
                    time: 600
                  route_advertise_list:
                    - advertise_afi: ipv4
                      route_map: bb
                  rd: "1.1.1.1:11"
                  rt_in:
                    - "12:12"
                  rt_out:
                    - "13:13"
                  vnis:
                    - vni_number: 1
                      advertise_default_gw: true
                      advertise_svi_ip: true
                      rd: "5.5.5.5:55"
                      rt_in:
                        - "88:88"
                      rt_out:
                        - "77:77"
                - afi: ipv4
                  safi: unicast
                  network:
                    - 2.2.2.2/16
                    - 192.168.10.1/32
                  dampening: true
                  aggregate_address_config:
                    - prefix: 1.1.1.1/1
                      as_set: true
                      policy_name: bb
                      summary_only: true
                - afi: ipv6
                  safi: unicast
                  max_path:
                    ebgp: 4
                    ibgp: 5
                  redistribute:
                    - metric: "21"
                      protocol: connected
                      route_map: bb
                    - metric: "27"
                      protocol: ospf
                      route_map: aa
                    - metric: "26"
                      protocol: static
                      route_map: bb
          - bgp_as: 51
            vrf_name: VrfReg1
            address_family:
              afis:
                - afi: ipv4
                  safi: unicast
                  import:
                    vrf:
                      vrf_list:
                        - default
                      route_map: rmap-1
        state: merged

    # After state:
    # ------------
    #
    # sonic# show running-configuration bgp
    # !
    # router bgp 51 vrf VrfReg1
    #  log-neighbor-changes
    #  timers 60 180
    #  !
    #  address-family ipv4 unicast
    #   maximum-paths 1
    #   maximum-paths ibgp 1
    #   import vrf route-map rmap-1
    #   import vrf default
    # !
    # router bgp 51
    #  router-id 111.2.2.41
    #  timers 60 180
    #  !
    #  address-family ipv4 unicast
    #   network 2.2.2.2/16
    #   network 192.168.10.1/32
    #   aggregate-address 1.1.1.1/1 as-set summary-only route-map bb
    #   dampening
    #  !
    #  address-family ipv6 unicast
    #   redistribute connected route-map bb metric 21
    #   redistribute ospf route-map aa metric 27
    #   redistribute static route-map bb metric 26
    #   maximum-paths 4
    #   maximum-paths ibgp 5
    #  !
    #  address-family l2vpn evpn
    #   advertise-svi-ip
    #   advertise ipv4 unicast route-map bb
    #   rd 1.1.1.1:11
    #   route-target import 12:12
    #   route-target import 13:13
    #   dup-addr-detection max-moves 10 time 600
    #   dup-addr-detection freeze permanent
    #   advertise-pip ip 3.3.3.3 peer-ip 4.4.4.4
    #   !
    #   vni 1
    #    advertise-default-gw
    #    advertise-svi-ip
    #    rd 5.5.5.5:55
    #    route-target import 88:88
    #    route-target export 77:77
    #

    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration bgp
    # !
    # router bgp 51 vrf VrfReg1
    #  log-neighbor-changes
    #  timers 60 180
    #  !
    #  address-family ipv4 unicast
    #   maximum-paths 1
    #   maximum-paths ibgp 1
    #   network 3.3.3.3/16
    #   dampening
    # !
    # router bgp 51 vrf VrfReg2
    #  log-neighbor-changes
    #  timers 60 180
    #  !
    #  address-family ipv4 unicast
    #   maximum-paths 1
    #   maximum-paths ibgp 1
    #   import vrf route-map rmap-1
    #   import vrf default
    # !
    # router bgp 51
    #  router-id 111.2.2.41
    #  log-neighbor-changes
    #  timers 60 180
    #  !
    #  address-family ipv4 unicast
    #   redistribute connected route-map bb metric 21
    #   redistribute ospf route-map bb metric 27
    #   maximum-paths 1
    #   maximum-paths ibgp 1
    #   network 2.2.2.2/16
    #   network 192.168.10.1/32
    #   aggregate-address 5.5.5.5/5 as-set summary-only route-map bb
    #   dampening
    #  !
    #  address-family ipv6 unicast
    #   redistribute static route-map aa metric 26
    #   maximum-paths 4
    #   maximum-paths ibgp 5
    #  !
    #  address-family l2vpn evpn
    #   advertise-all-vni
    #   advertise-svi-ip
    #   advertise ipv4 unicast route-map bb
    #   rd 1.1.1.1:11
    #   route-target import 12:12
    #   route-target export 13:13
    #   advertise-pip ip 3.3.3.3 peer-ip 4.4.4.4
    #   no dup-addr-detection
    #   !
    #   vni 1
    #    advertise-default-gw
    #    advertise-svi-ip
    #    rd 5.5.5.5:55
    #    route-target import 88:88
    #    route-target export 77:77
    #

    - name: Replace device configuration of address families of specified BGP AS with provided configuration.
      dellemc.enterprise_sonic.sonic_bgp_af:
        config:
          - bgp_as: 51
            address_family:
              afis:
                - afi: l2vpn
                  safi: evpn
                  advertise_pip: true
                  advertise_pip_ip: "3.3.3.3"
                  advertise_pip_peer_ip: "4.4.4.4"
                  advertise_svi_ip: true
                  advertise_all_vni: true
                  advertise_default_gw: false
                  route_advertise_list:
                    - advertise_afi: ipv4
                      route_map: bb
                  rd: "1.1.1.1:11"
                  rt_in:
                    - "22:22"
                  rt_out:
                    - "13:13"
                  vnis:
                    - vni_number: 5
                      advertise_default_gw: true
                      advertise_svi_ip: true
                      rd: "10.10.10.10:55"
                      rt_in:
                        - "88:88"
                      rt_out:
                        - "77:77"
                - afi: ipv4
                  safi: unicast
                  network:
                    - 2.2.2.2/16
                    - 192.168.10.1/32
                  dampening: true
                  redistribute:
                    - protocol: connected
                    - protocol: ospf
                      metric: 30
                  aggregate-address-config:
                    - prefix: '5.5.5.5/5'
                      as_set: true
          - bgp_as: 51
            vrf_name: VrfReg2
            address_family:
              afis:
                - afi: ipv4
                  safi: unicast
                  import:
                    vrf:
                      vrf_list:
                        - VrfReg1
                      route_map: rmap-reg1
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show running-configuration bgp
    # !
    # router bgp 51 vrf VrfReg1
    #  log-neighbor-changes
    #  timers 60 180
    #  !
    #  address-family ipv4 unicast
    #   maximum-paths 1
    #   maximum-paths ibgp 1
    #   network 3.3.3.3/16
    #   dampening
    # !
    # router bgp 51 vrf VrfReg2
    #  log-neighbor-changes
    #  timers 60 180
    #  !
    #  address-family ipv4 unicast
    #   maximum-paths 1
    #   maximum-paths ibgp 1
    #   import vrf route-map rmap-reg1
    #   import vrf VrfReg1
    # !
    # router bgp 51
    #  router-id 111.2.2.41
    #  log-neighbor-changes
    #  timers 60 180
    #  !
    #  address-family ipv4 unicast
    #   redistribute connected
    #   redistribute ospf metric 30
    #   maximum-paths 1
    #   maximum-paths ibgp 1
    #   network 2.2.2.2/16
    #   network 192.168.10.1/32
    #   aggregate-address 5.5.5.5/5 as-set
    #   dampening
    #  !
    #  address-family ipv6 unicast
    #   redistribute static route-map aa metric 26
    #   maximum-paths 4
    #   maximum-paths ibgp 5
    #  !
    #  address-family l2vpn evpn
    #   advertise-all-vni
    #   advertise-svi-ip
    #   advertise ipv4 unicast route-map bb
    #   rd 1.1.1.1:11
    #   route-target import 22:22
    #   route-target export 13:13
    #   dup-addr-detection
    #   advertise-pip ip 3.3.3.3 peer-ip 4.4.4.4
    #   !
    #   vni 5
    #    advertise-default-gw
    #    advertise-svi-ip
    #    rd 10.10.10.10:55
    #    route-target import 88:88
    #    route-target export 77:77
    #

    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration bgp
    # !
    # router bgp 51 vrf VrfReg1
    #  log-neighbor-changes
    #  timers 60 180
    #  !
    #  address-family ipv4 unicast
    #   maximum-paths 1
    #   maximum-paths ibgp 1
    #   network 3.3.3.3/16
    #   dampening
    #   import vrf route-map rmap-1
    #   import vrf default
    # !
    # router bgp 51
    #  router-id 111.2.2.41
    #  log-neighbor-changes
    #  timers 60 180
    #  !
    #  address-family ipv4 unicast
    #   redistribute connected route-map bb metric 21
    #   redistribute ospf route-map bb metric 27
    #   maximum-paths 1
    #   maximum-paths ibgp 1
    #   network 2.2.2.2/16
    #   network 192.168.10.1/32
    #   dampening
    #  !
    #  address-family ipv6 unicast
    #   redistribute static route-map aa metric 26
    #   maximum-paths 4
    #   maximum-paths ibgp 5
    #  !
    #  address-family l2vpn evpn
    #   advertise-all-vni
    #   advertise-svi-ip
    #   advertise ipv4 unicast route-map bb
    #   rd 1.1.1.1:11
    #   route-target import 12:12
    #   route-target export 13:13
    #   dup-addr-detection max-moves 10 time 600
    #   dup-addr-detection freeze permanent
    #   advertise-pip ip 3.3.3.3 peer-ip 4.4.4.4
    #   !
    #   vni 1
    #    advertise-default-gw
    #    advertise-svi-ip
    #    rd 5.5.5.5:55
    #    route-target import 88:88
    #    route-target export 77:77
    #

    - name: Override device configuration of BGP address families with provided configuration.
      dellemc.enterprise_sonic.sonic_bgp_af:
        config:
          - bgp_as: 51
            address_family:
              afis:
                - afi: l2vpn
                  safi: evpn
                  advertise_pip: true
                  advertise_pip_ip: "3.3.3.3"
                  advertise_pip_peer_ip: "4.4.4.4"
                  advertise_svi_ip: true
                  advertise_all_vni: true
                  advertise_default_gw: false
                  dup_addr_detection:
                    freeze: '600'
                  route_advertise_list:
                    - advertise_afi: ipv4
                      route_map: bb
                  rd: "1.1.1.1:11"
                  rt_in:
                    - "22:22"
                  rt_out:
                    - "13:13"
                  vnis:
                    - vni_number: 5
                      advertise_default_gw: true
                      advertise_svi_ip: true
                      rd: "10.10.10.10:55"
                      rt_in:
                        - "88:88"
                      rt_out:
                        - "77:77"
                - afi: ipv4
                  safi: unicast
                  network:
                    - 2.2.2.2/16
                    - 192.168.10.1/32
                  dampening: true
                  redistribute:
                    - protocol: connected
                    - protocol: ospf
                      metric: 30
                  aggregate_address_config:
                    - prefix: 4.4.4.4/4
                      as_set: true
                      policy_name: bb
                      summary_only: true
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show running-configuration bgp
    # !
    # router bgp 51 vrf VrfReg1
    #  log-neighbor-changes
    #  timers 60 180
    # !
    # router bgp 51
    #  router-id 111.2.2.41
    #  log-neighbor-changes
    #  timers 60 180
    #  !
    #  address-family ipv4 unicast
    #   redistribute connected
    #   redistribute ospf metric 30
    #   maximum-paths 1
    #   maximum-paths ibgp 1
    #   network 2.2.2.2/16
    #   network 192.168.10.1/32
    #   aggregate-address 4.4.4.4/4 as-set summary-only route-map bb
    #   dampening
    #  !
    #  address-family l2vpn evpn
    #   advertise-all-vni
    #   advertise-svi-ip
    #   advertise ipv4 unicast route-map bb
    #   rd 1.1.1.1:11
    #   route-target import 22:22
    #   route-target export 13:13
    #   dup-addr-detection
    #   dup-addr-detection freeze 600
    #   advertise-pip ip 3.3.3.3 peer-ip 4.4.4.4
    #   !
    #   vni 5
    #    advertise-default-gw
    #    advertise-svi-ip
    #    rd 10.10.10.10:55
    #    route-target import 88:88
    #    route-target export 77:77
    #



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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned always in the same format as the parameters above.</div>
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
