.. _dellemc.enterprise_sonic.sonic_ospfv3_module:


*************************************
dellemc.enterprise_sonic.sonic_ospfv3
*************************************

**Configure global OSPFv3 protocol settings on SONiC.**


Version added: 3.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of global OSPFv3 parameters on devices running SONiC.
- Configure VRF instance before configuring OSPFv3 in a VRF.




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
                        <div>Specifies the OSPFv3 related configuration.</div>
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
                        <div>External routes (1 to 255).</div>
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
                        <div>Inter area routes (1 to 255).</div>
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
                        <div>Intra area routes (1 to 255).</div>
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
                        <div>OSPFv3 non stop forwarding (NSF) also known as OSPFv3 Graceful Restart.</div>
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
                        <div>Maximum length of the grace period (1 to 1800).</div>
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
                        <div>OSPFv3 GR Helper.</div>
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
                        <div>Supported grace interval (10 to 1800).</div>
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
                        <div>Enable OSPFv3 adjacency state logs.</div>
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
                        <div>Configure route redistribution into OSPFv3 router.</div>
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
                        <div>Enable default route redistribution into OSPFv3 always.</div>
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
                        <div>Configure the type of protocol to redistribute into OSPFv3.</div>
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
                    <b>router_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure OSPFv3 router identifier (A.B.C.D).</div>
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
                        <div>LSA minimum arrival timer (0 to 600000).</div>
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
                        <div>OSPFv3 SPF timers.</div>
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
                        <div>Configure write multiplier (1 to 100).</div>
                        <div>Maximum number of interfaces serviced per write.</div>
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
                        <div>Specifies the operation to be performed on the OSPFv3 process configured on the device.</div>
                        <div>In case of merged, the input configuration will be merged with the existing OSPFv3 configuration on the device.</div>
                        <div>In case of deleted, the specified existing OSPFv3 configuration will be removed from the device.</div>
                        <div>In case of overridden, all the existing OSPFv3 configuration will be deleted and the specified input configuration will be installed.</div>
                        <div>In case of replaced, the existing OSPFv3 configuration on the device will be replaced by the configuration in the playbook for each VRF group configured by the playbook.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - Supports ``check_mode``.
   - Tested against Enterprise SONiC Distribution by Dell Technologies.



Examples
--------

.. code-block:: yaml

    # Using deleted

    # Before state:
    # -------------
    #
    # sonic# show running-configuration ospfv3
    # router ospfv3 vrf Vrf_1
    # timers throttle spf 50 20 1000
    # redistribute bgp metric 15 metric-type 2 route-map RMAP
    # !
    # router ospfv3
    # ospfv3 router-id 20.20.20.20
    # distance 30
    # distance ospfv3 external 20
    # write-multiplier 20
    # !
    # sonic#
    # sonic# show running-configuration vrf Vrf_1
    # !
    # ip vrf Vrf_1
    # sonic# show running-configuration ipv6 prefix-list
    # !
    # ipv6 prefix-list PRF_LIST seq 1 permit 1::1/64
    # ipv6 prefix-list PRF_LIST2 seq 1 permit 2::1/64
    # sonic# show running-configuration route-map
    # !
    # route-map RMAP permit 1
    # sonic#

    - name: Delete the OSPFv3 configurations
      sonic_ospfv3:
        config:
          - vrf_name: 'default'
            router_id: "20.20.20.20"
            distance:
              external: 20
          - vrf_name: "Vrf_1"
            timers:
              throttle_spf:
              delay_time: 50
              initial_hold_time: 20
              maximum_hold_time: 1000
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration ospfv3
    # router ospfv3 vrf Vrf_1
    # redistribute bgp metric 15 metric-type 2 route-map RMAP
    # !
    # router ospfv3
    # distance 30
    # write-multiplier 20
    # !
    # sonic#


    # Using deleted

    # Before state:
    # -------------
    #
    # sonic# show running-configuration ospfv3
    # router ospfv3 vrf Vrf_1
    # timers throttle spf 50 20 1000
    # redistribute bgp metric 15 metric-type 2 route-map RMAP
    # !
    # router ospfv3
    # distance 30
    # write-multiplier 20
    # !
    # sonic#
    # sonic# show running-configuration vrf Vrf_1
    # !
    # ip vrf Vrf_1
    # sonic# show running-configuration ipv6 prefix-list
    # !
    # ipv6 prefix-list PRF_LIST seq 1 permit 1::1/24
    # ipv6 prefix-list PRF_LIST2 seq 1 permit 2::1/24
    # sonic# show running-configuration route-map
    # !
    # route-map RMAP permit 1
    # sonic#

    - name: Delete the OSPFv3 configurations
      sonic_ospfv3:
        config:
          - vrf_name: "Vrf_1"
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration ospfv3
    # router ospfv3
    # distance 30
    # write-multiplier 20
    # !
    # sonic#


    # Using merged

    # Before state:
    # -------------
    #
    # sonic# show running-configuration ospfv3
    # (No ospfv3 configuration present)
    # sonic# show running-configuration vrf Vrf_1
    # !
    # ip vrf Vrf_1
    # sonic# show running-configuration ipv6 prefix-list
    # !
    # ipv6 prefix-list PRF_LIST seq 1 permit 1::1/24
    # ipv6 prefix-list PRF_LIST2 seq 1 permit 2::1/24
    # sonic# show running-configuration route-map
    # !
    # route-map RMAP permit 1
    # sonic#

    - name: Add the OSPFv3 configurations
      sonic_ospfv3:
        config:
          - vrf_name: 'default'
            router_id: "10.10.10.10"
            distance:
              external: 20
          - vrf_name: "Vrf_1"
            timers:
              throttle_spf:
              delay_time: 10
              initial_hold_time: 20
              maximum_hold_time: 50
            redistribute:
              - protocol: "bgp"
                metric: 15
                metric_type: 2
                route_map: "RMAP"
        state: merged

    # After state:
    # ------------
    #
    # sonic# show running-configuration ospfv3
    # router ospfv3 vrf Vrf_1
    # timers throttle spf 10 20 50
    # redistribute bgp metric 15 metric-type 2 route-map RMAP
    # !
    # router ospfv3
    # ospfv3 router-id 10.10.10.10
    # distance ospfv3 external 20
    # !
    # sonic#


    # Using merged

    # Before state:
    # -------------
    #
    # sonic# show running-configuration ospfv3
    # router ospfv3 vrf Vrf_1
    # timers throttle spf 10 20 50
    # redistribute bgp metric 15 metric-type 2 route-map RMAP
    # !
    # router ospfv3
    # ospfv3 router-id 10.10.10.10
    # distance ospfv3 external 20
    # !
    # sonic#
    # sonic# show running-configuration vrf Vrf_1
    # !
    # ip vrf Vrf_1
    # sonic# show running-configuration ipv6 prefix-list
    # !
    # ipv6 prefix-list PRF_LIST seq 1 permit 1::1/24
    # ipv6 prefix-list PRF_LIST2 seq 1 permit 2::1/24
    # sonic# show running-configuration route-map
    # !
    # route-map RMAP permit 1
    # sonic#

    - name: Add the OSPFv3 configurations
      sonic_ospfv3:
        config:
          - vrf_name: 'default'
            write_multiplier: 20
            router_id: "20.20.20.20"
            distance:
              all: 30
          - vrf_name: "Vrf_1"
            timers:
              throttle_spf:
                delay_time: 50
                initial_hold_time: 20
                maximum_hold_time: 100
        state: merged

    # After state:
    # ------------
    #
    # sonic# show running-configuration ospfv3
    # router ospfv3 vrf Vrf_1
    # timers throttle spf 50 20 100
    # redistribute bgp metric 15 metric-type 2 route-map RMAP
    # !
    # router ospfv3
    # ospfv3 router-id 20.20.20.20
    # distance 30
    # distance ospfv3 external 20
    # write-multiplier 20
    # !
    # sonic#


    # Using replaced

    # Before state:
    # -------------
    #
    # sonic# show running-configuration ospfv3
    # router ospfv3 vrf Vrf_1
    # timers throttle spf 50 20 10
    # redistribute bgp metric 15 metric-type 2 route-map RMAP
    # !
    # router ospfv3
    # ospfv3 router-id 20.20.20.20
    # distance 30
    # distance ospfv3 external 20
    # write-multiplier 20
    # !
    # sonic#
    # sonic# show running-configuration vrf Vrf_1
    # !
    # ip vrf Vrf_1
    # sonic# show running-configuration ipv6 prefix-list
    # !
    # ipv6 prefix-list PRF_LIST seq 1 permit 1::1/24
    # ipv6 prefix-list PRF_LIST2 seq 1 permit 2::1/24
    # sonic# show running-configuration route-map
    # !
    # route-map RMAP permit 1
    # route-map RMAP2 permit 2
    # sonic#

    - name: Replace the OSPFv3 vrf default configurations
      sonic_ospfv3:
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
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show running-configuration ospfv3
    # router ospfv3 vrf Vrf_1
    # timers throttle spf 50 20 10
    # redistribute bgp metric 15 metric-type 2 route-map RMAP
    # !
    # router ospfv3
    # ospfv3 router-id 20.20.20.20
    # distance 20
    # redistribute connected metric 15 metric-type 2 route-map RMAP2
    # !


    # Using overridden

    # Before state:
    # -------------
    #
    # sonic# show running-configuration ospfv3
    # router ospfv3 vrf Vrf_1
    # timers throttle spf 50 20 10
    # redistribute bgp metric 15 metric-type 2 route-map RMAP
    # !
    # router ospfv3
    # ospfv3 router-id 20.20.20.20
    # distance 30
    # distance ospfv3 external 20
    # write-multiplier 20
    # !
    # sonic#
    # sonic# show running-configuration vrf Vrf_1
    # !
    # ip vrf Vrf_1
    # sonic# show running-configuration ipv6 prefix-list
    # !
    # ipv6 prefix-list PRF_LIST seq 1 permit 1::1/24
    # ipv6 prefix-list PRF_LIST2 seq 1 permit 2::1/24
    # sonic# show running-configuration route-map
    # !
    # route-map RMAP permit 1
    # route-map RMAP2 permit 2
    # sonic#

    - name: Override the OSPFv3 configurations
      sonic_ospfv3:
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
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show running-configuration ospfv3
    # router ospfv3
    # ospfv3 router-id 20.20.20.20
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
                            <div>The configuration resulting from module invocation.</div>
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
                            <div>The generated (calculated) configuration that would be applied by module invocation.</div>
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

- Thenmozhi Gopal (@thenmozhi-gopal), Naresh Sasivarnan (@NareshSasivarnan)
