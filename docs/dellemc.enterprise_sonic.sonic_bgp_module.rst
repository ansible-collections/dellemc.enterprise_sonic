.. _dellemc.enterprise_sonic.sonic_bgp_module:


**********************************
dellemc.enterprise_sonic.sonic_bgp
**********************************

**Manage global BGP and its parameters**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of global BGP parameters on devices running Enterprise SONiC Distribution by Dell Technologies.




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
                        <div>Specifies the BGP-related configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>as_notation</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>asdot</li>
                                    <li>asdot+</li>
                        </ul>
                </td>
                <td>
                        <div>Specify the AS number notation format</div>
                        <div>Option supported on Enterprise-Sonic releases 4.4.0 and higher.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>bestpath</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configures the BGP best-path.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>as_path</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configures the as-path values.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>confed</b>
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
                        <div>Configures the confed values of as-path.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ignore</b>
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
                        <div>Configures the ignore values of as-path.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>multipath_relax</b>
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
                        <div>Configures the multipath_relax values of as-path.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>multipath_relax_as_set</b>
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
                        <div>Configures the multipath_relax_as_set values of as-path.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>bandwidth</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.1.0</div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>default_weight</li>
                                    <li>ignore_weight</li>
                                    <li>skip_missing</li>
                        </ul>
                </td>
                <td>
                        <div>Link Bandwidth attribute for the bestpath selection process</div>
                        <div>Options are as follows</div>
                        <div>default_weight - Assign a low default weight (value 1) to paths not having link bandwidth</div>
                        <div>ignore_weight - Ignore link bandwidth (i.e., do regular ECMP, not weighted)</div>
                        <div>skip_missing - Ignore paths without link bandwidth for ECMP (if other paths have it)</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>compare_routerid</b>
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
                        <div>Configures the compare_routerid.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>med</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configures the med values.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>always_compare_med</b>
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
                        <div>Allows comparing meds from different neighbors if set to true</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>confed</b>
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
                        <div>Configures the confed values of med.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>missing_as_worst</b>
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
                        <div>Configures the missing_as_worst values of as-path.</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Specifies the BGP autonomous system (AS) number to configure on the device.</div>
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
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.1.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure graceful restart</div>
                </td>
            </tr>
                                <tr>
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
                        <div>Enable graceful restart</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>preserve_fw_state</b>
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
                        <div>Configures preserve-fw-state</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>restart_time</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configures restart-time.</div>
                        <div>The range is from 1 to 3600.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>stale_routes_time</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configures stale-routes-time.</div>
                        <div>The range is from 1 to 3600.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>log_neighbor_changes</b>
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
                        <div>Enables/disables logging neighbor up/down and reset reason.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>max_med</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure max med and its parameters</div>
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
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>On startup time and max-med value</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>med_val</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>on startup med value</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>timer</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configures on startup time</div>
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
                        <div>Configures the BGP routing process router-id value.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>rt_delay</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Time in seconds to wait before processing route-map changes.</div>
                        <div>Range is 0-600. 0 disables the timer and changes to route-map will not be updated.</div>
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
                        <div>Adjust routing timers</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>holdtime</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configures hold-time</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>keepalive_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configures keepalive-interval</div>
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
                        <div>Specifies the VRF name.</div>
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
                        <div>Specifies the operation to be performed on the BGP process that is configured on the device.</div>
                        <div>In case of merged, the input configuration is merged with the existing BGP configuration on the device.</div>
                        <div>In case of deleted, the existing BGP configuration is removed from the device.</div>
                        <div>In case of replaced, the existing configuration of the specified BGP AS will be replaced with provided configuration.</div>
                        <div>In case of overridden, the existing BGP configuration will be overridden with the provided configuration.</div>
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
    # !
    # router bgp 10 vrf VrfCheck1
    #  router-id 10.2.2.32
    #  route-map delay-timer 20
    #  log-neighbor-changes
    # !
    # router bgp 11 vrf VrfCheck2
    #  log-neighbor-changes
    #  bestpath as-path ignore
    #  bestpath med missing-as-worst confed
    #  bestpath compare-routerid
    # !
    # router bgp 4
    #  router-id 10.2.2.4
    #  graceful-restart enable
    #  graceful-restart restart-time 1
    #  graceful-restart stalepath-time 500
    #  route-map delay-timer 10
    #  bestpath as-path ignore
    #  bestpath as-path confed
    #  bestpath med missing-as-worst confed
    #  bestpath compare-routerid
    #  bestpath bandwidth default-weight
    # !
    #
    - name: Delete BGP Global attributes
      dellemc.enterprise_sonic.sonic_bgp:
        config:
          - bgp_as: 4
            router_id: 10.2.2.4
            rt_delay: 10
            log_neighbor_changes: false
            graceful_restart:
              stale_routes_time: 500
              restart_time: 1
            bestpath:
              as_path:
                confed: true
                ignore: true
                multipath_relax: false
                multipath_relax_as_set: true
              bandwidth: default_weight
              compare_routerid: true
              med:
                confed: true
                missing_as_worst: true
          - bgp_as: 10
            router_id: 10.2.2.32
            rt_delay: 20
            log_neighbor_changes: true
            vrf_name: 'VrfCheck1'
          - bgp_as: 11
            log_neighbor_changes: true
            vrf_name: 'VrfCheck2'
            bestpath:
              as_path:
                confed: false
                ignore: true
                multipath_relax_as_set: true
              compare_routerid: true
              med:
                confed: true
                missing_as_worst: true
        state: deleted


    # After state:
    # ------------
    #
    # !
    # router bgp 10 vrf VrfCheck1
    #  log-neighbor-changes
    # !
    # router bgp 11 vrf VrfCheck2
    #  log-neighbor-changes
    #  bestpath compare-routerid
    # !
    # router bgp 4
    #  graceful-restart enable
    #  log-neighbor-changes
    #  bestpath compare-routerid
    # !


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # !
    # router bgp 10 vrf VrfCheck1
    #  router-id 10.2.2.32
    #  route-map delay-timer 20
    #  log-neighbor-changes
    # !
    # router bgp 11 vrf VrfCheck2
    #  graceful-restart enable
    #  log-neighbor-changes
    #  bestpath as-path ignore
    #  bestpath med missing-as-worst confed
    #  bestpath compare-routerid
    #  bestpath bandwidth ignore-weight
    # !
    # router bgp 4
    #  router-id 10.2.2.4
    #  route-map delay-timer 10
    #  bestpath as-path ignore
    #  bestpath as-path confed
    #  bestpath med missing-as-worst confed
    #  bestpath compare-routerid
    # !

    - name: Deletes all the bgp global configurations
      dellemc.enterprise_sonic.sonic_bgp:
        config:
        state: deleted

    # After state:
    # ------------
    #
    # !
    # !


    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # !
    # router bgp 4
    #  router-id 10.1.1.4
    # !
    #
    - name: Merges provided configuration with device configuration
      dellemc.enterprise_sonic.sonic_bgp:
        config:
          - bgp_as: 4
            router_id: 10.2.2.4
            rt_delay: 10
            log_neighbor_changes: false
            graceful_restart:
              enabled: true
              preserve_fw_state: true
            timers:
              holdtime: 20
              keepalive_interval: 30
            bestpath:
              as_path:
                confed: true
                ignore: true
                multipath_relax: false
                multipath_relax_as_set: true
              bandwidth: ignore-weight
              compare_routerid: true
              med:
                confed: true
                missing_as_worst: true
                always_compare_med: true
            max_med:
              on_startup:
                timer: 667
                med_val: 7878
          - bgp_as: 10
            router_id: 10.2.2.32
            rt_delay: 20
            log_neighbor_changes: true
            vrf_name: 'VrfCheck1'
          - bgp_as: 11
            log_neighbor_changes: true
            vrf_name: 'VrfCheck2'
            bestpath:
              as_path:
                confed: false
                ignore: true
                multipath_relax_as_set: true
              compare_routerid: true
              med:
                confed: true
                missing_as_worst: true
        state: merged

    #
    # After state:
    # ------------
    #
    # !
    # router bgp 10 vrf VrfCheck1
    #  router-id 10.2.2.32
    #  route-map delay-timer 20
    #  log-neighbor-changes
    # !
    # router bgp 11 vrf VrfCheck2
    #  log-neighbor-changes
    #  bestpath as-path ignore
    #  bestpath med missing-as-worst confed
    #  bestpath compare-routerid
    # !
    # router bgp 4
    #  router-id 10.2.2.4
    #  graceful-restart enable
    #  graceful-restart preserve-fw-state
    #  route-map delay-timer 10
    #  bestpath as-path ignore
    #  bestpath as-path confed
    #  bestpath med missing-as-worst confed
    #  bestpath compare-routerid
    #  bestpath bandwidth ignore-weight
    #  always-compare-med
    #  max-med on-startup 667 7878
    #  timers 20 30
    #
    # !


    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # !
    # router bgp 10 vrf VrfCheck1
    #  router-id 10.2.2.32
    #  log-neighbor-changes
    #  timers 60 180
    # !
    # router bgp 4
    #  router-id 10.2.2.4
    #  max-med on-startup 667 7878
    #  bestpath as-path ignore
    #  bestpath as-path confed
    #  bestpath med missing-as-worst confed
    #  bestpath compare-routerid
    #  bestpath bandwidth default-weight
    #  timers 20 30
    # !
    #

    - name: Replace device configuration of specified BGP AS with provided
      dellemc.enterprise_sonic.sonic_bgp:
        config:
          - bgp_as: 4
            router_id: 10.2.2.44
            log_neighbor_changes: true
            bestpath:
              as_path:
                confed: true
              bandwidth: skip_missing
              compare_routerid: true
          - bgp_as: 11
            vrf_name: 'VrfCheck2'
            router_id: 10.2.2.33
            log_neighbor_changes: true
            bestpath:
              as_path:
                confed: true
                ignore: true
              compare_routerid: true
              med:
                confed: true
                missing_as_worst: true
        state: replaced

    #
    # After state:
    # ------------
    #
    # !
    # router bgp 10 vrf VrfCheck1
    #  router-id 10.2.2.32
    #  log-neighbor-changes
    #  timers 60 180
    # !
    # router bgp 11 vrf VrfCheck2
    #  router-id 10.2.2.33
    #  log-neighbor-changes
    #  bestpath as-path ignore
    #  bestpath as-path confed
    #  bestpath med missing-as-worst confed
    #  bestpath compare-routerid
    #  timers 60 180
    # !
    # router bgp 4
    #  router-id 10.2.2.44
    #  log-neighbor-changes
    #  bestpath as-path confed
    #  bestpath compare-routerid
    #  bestpath bandwidth skip_missing
    #  timers 60 180
    # !


    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # !
    # router bgp 10 vrf VrfCheck1
    #  router-id 10.2.2.32
    #  log-neighbor-changes
    #  timers 60 180
    # !
    # router bgp 4
    #  router-id 10.2.2.4
    #  max-med on-startup 667 7878
    #  bestpath as-path ignore
    #  bestpath as-path confed
    #  bestpath med missing-as-worst confed
    #  bestpath compare-routerid
    #  bestpath bandwidth default-weight
    #  timers 20 30
    # !
    #

    - name: Override device configuration of global BGP with provided configuration
      dellemc.enterprise_sonic.sonic_bgp:
        config:
          - bgp_as: 4
            router_id: 10.2.2.44
            log_neighbor_changes: true
            bestpath:
              as_path:
                confed: true
              compare_routerid: true
          - bgp_as: 11
            vrf_name: 'VrfCheck2'
            router_id: 10.2.2.33
            log_neighbor_changes: true
            bestpath:
              as_path:
                confed: true
                ignore: true
              compare_routerid: true
            timers:
              holdtime: 90
              keepalive_interval: 30
        state: overridden

    #
    # After state:
    # ------------
    #
    # !
    # router bgp 11 vrf VrfCheck2
    #  router-id 10.2.2.33
    #  log-neighbor-changes
    #  bestpath as-path ignore
    #  bestpath as-path confed
    #  bestpath compare-routerid
    #  timers 30 90
    # !
    # router bgp 4
    #  router-id 10.2.2.44
    #  log-neighbor-changes
    #  bestpath as-path confed
    #  bestpath compare-routerid
    #  timers 60 180
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

- Dhivya P (@dhivayp)
