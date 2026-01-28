.. _dellemc.enterprise_sonic.sonic_ospfv2_module:


*************************************
dellemc.enterprise_sonic.sonic_ospfv2
*************************************

**Configure global OSPFv2 protocol settings on SONiC.**


Version added: 2.5.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of global OSPFv2 parameters on devices running SONiC.
- Configure VRF instance before configuring OSPF in a VRF.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="4">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="4">
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
                        <div>Specifies the OSPFv2 related configuration.</div>
                        <div><em>non_passive_interfaces</em> and <em>passive_interfaces</em> are mutually exclusive.</div>
                        <div>When <em>default_passive=True</em>, <em>passive_interfaces</em> cannot be configured.</div>
                        <div>When <em>default_passive=False</em>, <em>non_passive_interfaces</em> cannot be configured.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>abr_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>cisco</li>
                                    <li>ibm</li>
                                    <li>shortcut</li>
                                    <li>standard</li>
                        </ul>
                </td>
                <td>
                        <div>Configure router ABR type.</div>
                        <div><code>cisco</code> - Cisco implementation type ABR.</div>
                        <div><code>ibm</code> - IBM implementation type ABR.</div>
                        <div><code>shortcut</code> - Shortcut ABR.</div>
                        <div><code>standard</code> - RFC2328 Standard implementation ABR.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>auto_cost_reference_bandwidth</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure interface auto cost reference bandwidth (1 to 4294967).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>default_metric</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure metric for redistributed routes (0 to 16777214).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>default_passive</b>
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
                        <div>Suppresses OSPFv2 routing updates on all interfaces.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>distance</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure route administrative distance.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>all</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Distance value for all type of routes (1 to 255).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>external</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Distance value for external routes (1 to 255).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>inter_area</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Distance value for inter-area routes (1 to 255).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>intra_area</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Distance value for intra-area routes (1 to 255).</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>graceful_restart</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>OSPF non stop forwarding (NSF) also known as OSPF Graceful Restart.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>enable</b>
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
                        <div>Enable graceful restart.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>grace_period</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Maximum length of the grace period in seconds (1 to 1800).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>helper</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>OSPF GR Helper.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>advertise_router_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Advertising Router ID.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>enable</b>
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
                        <div>Enable Helper support.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>planned_only</b>
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
                        <div>Supported only planned restart.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>strict_lsa_checking</b>
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
                        <div>Enable strict LSA check.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>supported_grace_time</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Supported grace interval in seconds (10 to 1800).</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>log_adjacency_changes</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>brief</li>
                                    <li>detail</li>
                        </ul>
                </td>
                <td>
                        <div>Enable OSPFv2 adjacency state logs.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>max_metric</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Enables infinite metric advertising in OSPFv2 LSAs.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>administrative</b>
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
                        <div>Enables administrative type infinite metric advertising.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>external_lsa_all</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure external LSA all prefix max metric advertising.</div>
                        <div>Configure the maximum metric value (1 to 16777215).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>external_lsa_connected</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure external LSA connected prefix max metric advertising.</div>
                        <div>Configure the maximum metric value (1 to 16777215).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>on_startup</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Enables infinite metric advertising at OSPFv2 router startup (5 to 86400).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>router_lsa_all</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure router LSA all link max metric advertising.</div>
                        <div>Configure the maximum metric value (1 to 16777215).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>router_lsa_stub</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure router LSA stub link max metric advertising.</div>
                        <div>Configure the maximum metric value (1 to 16777215).</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>maximum_paths</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure maximum number of multiple paths for ECMP support (1 to 256).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>non_passive_interfaces</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure non passive interface types.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>addresses</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure Interface IPv4 addresses.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interface</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Full name of the Layer 3 interface, i.e. Eth1/1.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>opaque_lsa_capability</b>
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
                        <div>Enables opaque LSA capability.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>passive_interfaces</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure passive interface types.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>addresses</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure Interface IPv4 addresses.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interface</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Full name of the Layer 3 interface, i.e. Eth1/1.</div>
                </td>
            </tr>

            <tr>
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
                        <div>Configure route redistribution into OSPFv2 router.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>always</b>
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
                        <div>Enable default route redistribution into OSPF always.</div>
                        <div>Only available for <em>protocol=default_route</em>.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Metric value for redistributed routes (0 to 16777214).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>metric_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>1</li>
                                    <li>2</li>
                        </ul>
                </td>
                <td>
                        <div>Metric type for redistributed routes.</div>
                </td>
            </tr>
            <tr>
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
                                    <li>bgp</li>
                                    <li>connected</li>
                                    <li>default_route</li>
                                    <li>kernel</li>
                                    <li>static</li>
                        </ul>
                </td>
                <td>
                        <div>Configure the type of protocol to redistribute into OSPF.</div>
                        <div>Deleting <em>protocol</em> alone will also delete all the other configuration under <em>redistribute</em>.</div>
                        <div><code>bgp</code> - Border Gateway Protocol.</div>
                        <div><code>connected</code> - Directly connected or attached subnets and hosts.</div>
                        <div><code>default_route</code> - Default routes.</div>
                        <div><code>kernel</code> - Kernel routes other than FRR installed routes.</div>
                        <div><code>static</code> - Statically configured routes.</div>
                </td>
            </tr>
            <tr>
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
                        <div>Route map to filter redistributed routes.</div>
                        <div>Configure route map before.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>refresh_timer</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configures LSA refresh interval in seconds (10 to 1800).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>rfc1583_compatible</b>
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
                        <div>Enable OSPFv2 RFC compatibility.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>router_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure OSPFv2 router identifier (A.B.C.D).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>timers</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configures router timers.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>lsa_min_arrival</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>LSA minimum arrival timer in milliseconds (0 to 600000).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>throttle_lsa_all</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>LSA delay between transmissions in milliseconds (0 to 5000).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>throttle_spf</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>OSPFv2 SPF timers.</div>
                        <div><em>delay_time</em>, <em>initial_hold_time</em> and <em>maximum_hold_time</em> are required together.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>delay_time</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>SPF delay time in milliseconds (0 to 600000).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>initial_hold_time</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>SPF initial hold time in milliseconds (0 to 600000).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>maximum_hold_time</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>SPF maximum hold time in milliseconds (0 to 600000).</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Specifies the vrf name.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>write_multiplier</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the maximum number of interfaces serviced per write (1 to 100)</div>
                </td>
            </tr>

            <tr>
                <td colspan="4">
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
                        <div>Specifies the operation to be performed on the OSPFv2 process configured on the device.</div>
                        <div>In case of merged, the input configuration will be merged with the existing OSPFv2 configuration on the device.</div>
                        <div>In case of deleted, the existing OSPFv2 configuration will be removed from the device.</div>
                        <div>In case of overridden, all the existing OSPFv2 configuration will be deleted and the specified input configuration will be installed.</div>
                        <div>In case of replaced, the existing OSPFv2 configuration on the device will be replaced by the configuration in the playbook for each VRF group configured by the playbook.</div>
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

    # Using "deleted" state

    # Before state:
    # -------------
    #
    # sonic# show running-configuration ospf
    # router ospf vrf Vrf_1
    # default-metric 100
    # max-metric router-lsa external-lsa all 2
    # passive-interface default
    # timers throttle spf 50 20 10
    # timers throttle lsa all 300
    # redistribute bgp metric 15 metric-type 2 route-map RMAP
    # no passive-interface Eth1/1 2.2.2.2
    # no passive-interface Eth1/2 2.2.2.2
    # !
    # router ospf
    # ospf router-id 20.20.20.20
    # distance 30
    # distance ospf external 20
    # refresh timer 300
    # write-multiplier 20
    # maximum-paths 200
    # passive-interface Eth1/2 3.3.3.3
    # passive-interface Eth1/3
    # !
    # sonic#
    # sonic# show running-configuration vrf Vrf_1
    # !
    # ip vrf Vrf_1
    # sonic# show running-configuration ip prefix-list
    # !
    # ip prefix-list PRF_LIST seq 1 permit 1.1.1.1/24
    # ip prefix-list PRF_LIST2 seq 1 permit 1.1.1.1/24
    # sonic# show running-configuration route-map
    # !
    # route-map RMAP permit 1
    # sonic#

    - name: Delete the OSPFv2 configurations
      sonic_ospf:
        config:
          - vrf_name: 'default'
            router_id: "20.20.20.20"
            distance:
              external: 20
            default_passive: false
            maximum_paths: 200
            passive_interfaces:
              interfaces:
                - interface: 'Eth1/3'
            redistribute:
              - protocol: "bgp"
                metric: 15
                metric_type: 2
                route_map: "RMAP"
            refresh_timer: 300
          - vrf_name: "Vrf_1"
            timers:
              throttle_spf:
                delay_time: 50
                initial_hold_time: 20
                maximum_hold_time: 10
            default_metric: 100
            max_metric:
              external_lsa_all: 2
            non_passive_interfaces:
              interfaces:
                - interface: "Eth1/2"
                  addresses:
                    - "2.2.2.2"
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration ospf
    # router ospf vrf Vrf_1
    # passive-interface default
    # timers throttle lsa all 300
    # no passive-interface Eth1/1 2.2.2.2
    # no passive-interface Eth1/2 2.2.2.2
    # !
    # router ospf
    # distance 30
    # write-multiplier 20
    # passive-interface Eth1/2 3.3.3.3
    # !
    # sonic#


    # Using "deleted" state

    # Before state:
    # -------------
    #
    # sonic# show running-configuration ospf
    # router ospf vrf Vrf_1
    # passive-interface default
    # timers throttle lsa all 300
    # no passive-interface Eth1/1 2.2.2.2
    # no passive-interface Eth1/2 2.2.2.2
    # !
    # router ospf
    # distance 30
    # write-multiplier 20
    # passive-interface Eth1/2 3.3.3.3
    # !
    # sonic#
    # sonic# show running-configuration vrf Vrf_1
    # !
    # ip vrf Vrf_1
    # sonic# show running-configuration ip prefix-list
    # !
    # ip prefix-list PRF_LIST seq 1 permit 1.1.1.1/24
    # ip prefix-list PRF_LIST2 seq 1 permit 1.1.1.1/24
    # sonic# show running-configuration route-map
    # !
    # route-map RMAP permit 1
    # sonic#

    - name: Delete the OSPFv2 configurations
      sonic_ospf:
        config:
          - vrf_name: "Vrf_1"
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration ospf
    # router ospf
    # distance 30
    # write-multiplier 20
    # passive-interface Eth1/2 3.3.3.3
    # !
    # sonic#


    # Using "merged" state

    # Before state:
    # -------------
    #
    # sonic# show running-configuration ospf
    # (No ospf configuration present)
    # sonic# show running-configuration vrf Vrf_1
    # !
    # ip vrf Vrf_1
    # sonic# show running-configuration ip prefix-list
    # !
    # ip prefix-list PRF_LIST seq 1 permit 1.1.1.1/24
    # ip prefix-list PRF_LIST2 seq 1 permit 1.1.1.1/24
    # sonic# show running-configuration route-map
    # !
    # route-map RMAP permit 1
    # sonic#

    - name: Add the OSPFv2 configurations
      sonic_ospf:
        config:
          - vrf_name: 'default'
            router_id: "10.10.10.10"
            distance:
              external: 20
            auto_cost_reference_bandwidth: 100
          - vrf_name: "Vrf_1"
            timers:
              throttle_lsa_all: 300
              throttle_spf:
                delay_time: 10
                initial_hold_time: 20
                maximum_hold_time: 50
            redistribute:
              - protocol: "bgp"
                metric: 15
                metric_type: 2
                route_map: "RMAP"
            default_passive: true
            non_passive_interfaces:
              interfaces:
                - interface: "Eth1/1"
                  addresses:
                    - "2.2.2.2"
        state: merged

    # After state:
    # ------------
    #
    # sonic# show running-configuration ospf
    # router ospf vrf Vrf_1
    # passive-interface default
    # timers throttle spf 10 20 50
    # timers throttle lsa all 300
    # redistribute bgp metric 15 metric-type 2 route-map RMAP
    # no passive-interface Eth1/1 2.2.2.2
    # !
    # router ospf
    # auto-cost reference-bandwidth 100
    # ospf router-id 10.10.10.10
    # distance ospf external 20
    # !
    # sonic#


    # Using "merged" state

    # Before state:
    # -------------
    #
    # sonic# show running-configuration ospf
    # router ospf vrf Vrf_1
    # passive-interface default
    # timers throttle spf 10 20 50
    # timers throttle lsa all 300
    # redistribute bgp metric 15 metric-type 2 route-map RMAP
    # no passive-interface Eth1/1 2.2.2.2
    # !
    # router ospf
    # ospf router-id 10.10.10.10
    # distance ospf external 20
    # !
    # sonic#
    # sonic# show running-configuration vrf Vrf_1
    # !
    # ip vrf Vrf_1
    # sonic# show running-configuration ip prefix-list
    # !
    # ip prefix-list PRF_LIST seq 1 permit 1.1.1.1/24
    # ip prefix-list PRF_LIST2 seq 1 permit 1.1.1.1/24
    # sonic# show running-configuration route-map
    # !
    # route-map RMAP permit 1
    # sonic#

    - name: Add the OSPFv2 configurations
      sonic_ospf:
        config:
          - vrf_name: 'default'
            write_multiplier: 20
            router_id: "20.20.20.20"
            distance:
              all: 30
            default_passive: false
            graceful_restart:
              enable: true
              grace_period: 100
              helper:
                enable: true
                planned_only: true
                advertise_router_id:
                  - '1.1.1.1'
                  - '2.2.2.2'
            passive_interfaces:
              interfaces:
                - interface: 'Eth1/2'
                  addresses:
                    - '3.3.3.3'
                - interface: 'Eth1/3'
            log_adjacency_changes: 'detail'
          - vrf_name: "Vrf_1"
            timers:
              throttle_spf:
                delay_time: 50
                initial_hold_time: 20
                maximum_hold_time: 10
            max_metric:
              external_lsa_all: 30
            log_adjacency_changes: 'brief'
            default_passive: true
            non_passive_interfaces:
              interfaces:
                - interface: "Eth1/2"
                  addresses:
                    - "2.2.2.2"
        state: merged

    # After state:
    # ------------
    #
    # sonic# show running-configuration ospf
    # router ospf vrf Vrf_1
    # log-adjacency-changes
    # max-metric router-lsa external-lsa all 30
    # passive-interface default
    # timers throttle spf 50 20 10
    # timers throttle lsa all 300
    # redistribute bgp metric 15 metric-type 2 route-map RMAP
    # no passive-interface Eth1/1 2.2.2.2
    # no passive-interface Eth1/2 2.2.2.2
    # !
    # router ospf
    # ospf router-id 20.20.20.20
    # distance 30
    # distance ospf external 20
    # log-adjacency-changes detail
    # graceful-restart grace-period 100
    # graceful-restart helper enable
    # graceful-restart helper planned-only
    # graceful-restart helper enable 1.1.1.1
    # graceful-restart helper enable 2.2.2.2
    # write-multiplier 20
    # passive-interface Eth1/2 3.3.3.3
    # passive-interface Eth1/3
    # !
    # sonic#


    # Using "replaced" state

    # Before state:
    # -------------
    #
    # sonic# show running-configuration ospf
    # router ospf vrf Vrf_1
    # max-metric router-lsa external-lsa all 2
    # passive-interface default
    # timers throttle spf 50 20 10
    # timers throttle lsa all 300
    # redistribute bgp metric 15 metric-type 2 route-map RMAP
    # no passive-interface Eth1/1 2.2.2.2
    # no passive-interface Eth1/2 2.2.2.2
    # !
    # router ospf
    # ospf router-id 20.20.20.20
    # distance 30
    # distance ospf external 20
    # write-multiplier 20
    # passive-interface Eth1/2 3.3.3.3
    # passive-interface Eth1/3
    # !
    # sonic#
    # sonic# show running-configuration vrf Vrf_1
    # !
    # ip vrf Vrf_1
    # sonic# show running-configuration ip prefix-list
    # !
    # ip prefix-list PRF_LIST seq 1 permit 1.1.1.1/24
    # ip prefix-list PRF_LIST2 seq 1 permit 1.1.1.1/24
    # sonic# show running-configuration route-map
    # !
    # route-map RMAP permit 1
    # route-map RMAP2 permit 2
    # sonic#

    - name: Replace the OSPFv2 vrf default configurations
      sonic_ospf:
        config:
          - vrf_name: 'default'
            router_id: "20.20.20.20"
            redistribute:
              - protocol: "connected"
                metric: 15
                metric_type: 2
                route_map: "RMAP2"
              - protocol: "default_route"
                always: true
                route_map: "RMAP"
            distance:
              all: 20
            abr_type: cisco
            opaque_lsa_capability: true
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show running-configuration ospf
    # router ospf vrf Vrf_1
    # max-metric router-lsa external-lsa all 2
    # passive-interface default
    # timers throttle spf 50 20 10
    # timers throttle lsa all 300
    # redistribute bgp metric 15 metric-type 2 route-map RMAP
    # no passive-interface Eth1/1 2.2.2.2
    # no passive-interface Eth1/2 2.2.2.2
    # !
    # router ospf
    # capability opaque
    # ospf router-id 20.20.20.20
    # default-information originate always route-map RMAP
    # distance 20
    # ospf abr-type cisco
    # redistribute connected metric 15 metric-type 2 route-map RMAP2
    # !


    # Using "overridden" state

    # Before state:
    # -------------
    #
    # sonic# show running-configuration ospf
    # router ospf vrf Vrf_1
    # max-metric router-lsa external-lsa all 2
    # passive-interface default
    # timers throttle spf 50 20 10
    # timers throttle lsa all 300
    # redistribute bgp metric 15 metric-type 2 route-map RMAP
    # no passive-interface Eth1/1 2.2.2.2
    # no passive-interface Eth1/2 2.2.2.2
    # !
    # router ospf
    # ospf router-id 20.20.20.20
    # distance 30
    # distance ospf external 20
    # write-multiplier 20
    # passive-interface Eth1/2 3.3.3.3
    # passive-interface Eth1/3
    # !
    # sonic#
    # sonic# show running-configuration vrf Vrf_1
    # !
    # ip vrf Vrf_1
    # sonic# show running-configuration ip prefix-list
    # !
    # ip prefix-list PRF_LIST seq 1 permit 1.1.1.1/24
    # ip prefix-list PRF_LIST2 seq 1 permit 1.1.1.1/24
    # sonic# show running-configuration route-map
    # !
    # route-map RMAP permit 1
    # route-map RMAP2 permit 2
    # sonic#

    - name: Override the OSPFv2 configurations
      sonic_ospf:
        config:
          - vrf_name: 'default'
            router_id: "20.20.20.20"
            redistribute:
              - protocol: "connected"
                metric: 15
                metric_type: 2
                route_map: "RMAP2"
            distance:
              all: 20
            rfc1583_compatible: true
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show running-configuration ospf
    # router ospf
    # compatible rfc1583
    # ospf router-id 20.20.20.20
    # distance 20
    # redistribute connected metric 15 metric-type 2 route-map RMAP2
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format
     as the parameters above.</div>
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

- Santhosh kumar T (@santhosh-kt)
