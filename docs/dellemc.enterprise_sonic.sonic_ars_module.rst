.. _dellemc.enterprise_sonic.sonic_ars_module:


**********************************
dellemc.enterprise_sonic.sonic_ars
**********************************

**Manage adaptive routing and switching (ARS) configuration on SONiC**


Version added: 3.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of ARS for devices running SONiC




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="3">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>config</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>ARS configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ars_objects</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of ARS next-hop group objects configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>idle_time</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Idle time in microseconds</div>
                        <div>Range 16-32767</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>max_flows</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>256</li>
                                    <li>512</li>
                                    <li>1024</li>
                                    <li>2048</li>
                                    <li>4096</li>
                                    <li>8192</li>
                                    <li>16384</li>
                                    <li>32768</li>
                        </ul>
                </td>
                <td>
                        <div>Maximum number of flows that can be maintained by the ARS object</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mode</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>fixed</li>
                                    <li>flowlet-quality</li>
                                    <li>flowlet-random</li>
                                    <li>packet-quality</li>
                                    <li>packet-random</li>
                        </ul>
                </td>
                <td>
                        <div>ARS path reassignment mode</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of next-hop group object</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>port_bindings</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of ARS port bindings configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of port</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>profile</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>ARS port profile to bind to port</div>
                        <div>Required for modifcation</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>port_profiles</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of ARS port profiles configuration</div>
                </td>
            </tr>
                                <tr>
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
                        <div>Enable/disable ARS for the port</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>load_future_weight</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Weight of future port load used in EWMA calculations</div>
                        <div>Range 1-16</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>load_past_weight</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Weight as a percentage of the past port load</div>
                        <div>Range 0-100</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>load_scaling_factor</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>0</li>
                                    <li>1</li>
                                    <li>2.5</li>
                                    <li>4</li>
                                    <li>5</li>
                                    <li>10</li>
                                    <li>20</li>
                                    <li>40</li>
                                    <li>80</li>
                        </ul>
                </td>
                <td>
                        <div>Port load scaling factor</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of port profile</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>profiles</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of ARS profiles configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>algorithm</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>EWMA</li>
                        </ul>
                </td>
                <td>
                        <div>ARS algorithm used for quality computation</div>
                        <div><code>EWMA</code> - Exponential Weighted Moving Average</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>load_current_max_val</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Maximum current load threshold value for the quantization process</div>
                        <div>Range 0-133169151</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>load_current_min_val</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Minimum current load threshold value for the quantization process</div>
                        <div>Range 0-133169151</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>load_future_max_val</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Maximum future load threshold value for the quantization process</div>
                        <div>Range 0-266338303</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>load_future_min_val</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Minimum future load threshold value for the quantization process</div>
                        <div>Range 0-266338303</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>load_past_max_val</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Maximum past load threshold value for the quantization process</div>
                        <div>Range 0-10000</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>load_past_min_val</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Minimum past load threshold value for the quantization process</div>
                        <div>Range 0-10000</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of profile</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>port_load_current</b>
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
                        <div>Set port load to current sampled value when sampled value is less than the average</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>port_load_exponent</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>EWMA exponent used in port loading computation</div>
                        <div>Range 1-16</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>port_load_future</b>
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
                        <div>Enable/disable future port load, the average queued bytes measured on a port</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>port_load_future_weight</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Weight of future port load used in EWMA calculations</div>
                        <div>Range 1-16</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>port_load_past</b>
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
                        <div>Enable/disable past port load, the average egress bytes measured on a port</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>port_load_past_weight</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Weight of past port load used in EWMA calculations</div>
                        <div>Range 1-16</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>random_seed</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Random seed value</div>
                        <div>Range 0-16777214</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>sampling_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Sampling interval in microseconds</div>
                        <div>Range 1-255</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>switch_binding</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>ARS switch binding configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>profile</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>ARS profile to bind to switch</div>
                </td>
            </tr>


            <tr>
                <td colspan="3">
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
                        <div>The state of the configuration after module completion</div>
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

    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration ars
    # (No ARS configuration present)

    - name: Merge ARS configuration
      dellemc.enterprise_sonic.sonic_ars:
        config:
          ars_objects:
            - name: obj1
              idle_time: 100
              max_flows: 1024
              mode: flowlet-quality
          port_profiles:
            - name: pp1
              enable: true
              load_future_weight: 9
              load_past_weight: 20
              load_scaling_factor: 0
          profiles:
            - name: p1
              algorithm: EWMA
              load_current_max_val: 10000
              load_current_min_val: 100
              load_future_max_val: 20000
              load_future_min_val: 200
              load_past_max_val: 500
              load_past_min_val: 50
              port_load_current: true
              port_load_exponent: 7
              port_load_future: true
              port_load_future_weight: 9
              port_load_past: true
              port_load_past_weight: 11
              random_seed: 800000
              sampling_interval: 140
          port_bindings:
            - name: Ethernet20
              profile: pp1
          switch_binding:
            profile: p1
        state: merged

    # After state:
    # ------------
    #
    # sonic# show running-configuration ars
    # ars profile p1
    #  sampling-interval 140
    #  random-seed 800000
    #  port-load-past-weight 11
    #  port-load-future-weight 9
    #  port-load-current
    #  port-load-exponent 7
    #  load-past-min-val 50
    #  load-past-max-val 500
    #  load-future-min-val 200
    #  load-future-max-val 20000
    #  load-current-min-val 100
    #  load-current-max-val 10000
    # !
    # ars port-profile pp1
    #  enable
    #  load-past-weight 20
    #  load-future-weight 9
    # !
    # ars object obj1
    #  idle-time 100
    #  max-flows 1024
    # !
    # interface Ethernet20
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  unreliable-los auto
    #  shutdown
    #  ars bind pp1
    # !
    # ars bind profile p1


    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration ars
    # ars profile p1
    #  sampling-interval 140
    #  random-seed 800000
    #  port-load-past-weight 11
    #  port-load-future-weight 9
    #  port-load-current
    #  port-load-exponent 7
    #  load-past-min-val 50
    #  load-past-max-val 500
    #  load-future-min-val 200
    #  load-future-max-val 20000
    #  load-current-min-val 100
    #  load-current-max-val 10000
    # !
    # ars port-profile pp1
    #  enable
    #  load-past-weight 20
    #  load-future-weight 9
    # !
    # ars object obj1
    #  idle-time 100
    #  max-flows 1024
    # !
    # interface Ethernet20
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  unreliable-los auto
    #  shutdown
    #  ars bind pp1
    # !
    # ars bind profile p1

    - name: Replace ARS configuration
      dellemc.enterprise_sonic.sonic_ars:
        config:
          port_profiles:
            - name: pp2
              enable: true
              load_future_weight: 8
              load_past_weight: 15
          port_bindings:
            - name: Ethernet20
              profile: pp2
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show running-configuration ars
    # ars profile p1
    #  sampling-interval 140
    #  random-seed 800000
    #  port-load-past-weight 11
    #  port-load-future-weight 9
    #  port-load-current
    #  port-load-exponent 7
    #  load-past-min-val 50
    #  load-past-max-val 500
    #  load-future-min-val 200
    #  load-future-max-val 20000
    #  load-current-min-val 100
    #  load-current-max-val 10000
    # !
    # ars port-profile pp2
    #  enable
    #  load-past-weight 15
    #  load-future-weight 8
    # !
    # ars object obj1
    #  idle-time 100
    #  max-flows 1024
    # !
    # interface Ethernet20
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  unreliable-los auto
    #  shutdown
    #  ars bind pp2
    # !
    # ars bind profile p1


    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration ars
    # ars profile p1
    #  sampling-interval 140
    #  random-seed 800000
    #  port-load-past-weight 11
    #  port-load-future-weight 9
    #  port-load-current
    #  port-load-exponent 7
    #  load-past-min-val 50
    #  load-past-max-val 500
    #  load-future-min-val 200
    #  load-future-max-val 20000
    #  load-current-min-val 100
    #  load-current-max-val 10000
    # !
    # ars port-profile pp2
    #  enable
    #  load-past-weight 15
    #  load-future-weight 8
    # !
    # ars object obj1
    #  idle-time 100
    #  max-flows 1024
    # !
    # interface Ethernet20
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  unreliable-los auto
    #  shutdown
    #  ars bind pp1
    # !
    # ars bind profile p1

    - name: Override ARS configuration
      dellemc.enterprise_sonic.sonic_ars:
        config:
          ars_objects:
            - name: obj4
              idle_time: 65
              max_flows: 4096
              mode: flowlet-quality
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show running-configuration ars
    # ars object obj4
    #  idle-time 65
    #  max-flows 4096


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration ars
    # ars profile p1
    #  sampling-interval 140
    #  random-seed 800000
    #  port-load-past-weight 11
    #  port-load-future-weight 9
    #  port-load-current
    #  port-load-exponent 7
    #  load-past-min-val 50
    #  load-past-max-val 500
    #  load-future-min-val 200
    #  load-future-max-val 20000
    #  load-current-min-val 100
    #  load-current-max-val 10000
    # !
    # ars port-profile pp2
    #  enable
    #  load-past-weight 15
    #  load-future-weight 8

    - name: Delete specified ARS configuration
      dellemc.enterprise_sonic.sonic_ars:
        config:
          port_profiles:
            - name: pp2
          profiles:
            - name: p1
              load_current_max_val: 10000
              load_future_max_val: 20000
              load_past_max_val: 500
              random_seed: 800000
              sampling_interval: 140
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration ars
    # ars profile p1
    #  port-load-past-weight 11
    #  port-load-future-weight 9
    #  port-load-current
    #  port-load-exponent 7
    #  load-past-min-val 50
    #  load-future-min-val 200
    #  load-current-min-val 100


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration ars
    # ars profile p1
    #  sampling-interval 140
    #  random-seed 800000
    #  port-load-past-weight 11
    #  port-load-future-weight 9
    #  port-load-current
    #  port-load-exponent 7
    #  load-past-min-val 50
    #  load-past-max-val 500
    #  load-future-min-val 200
    #  load-future-max-val 20000
    #  load-current-min-val 100
    #  load-current-max-val 10000
    # !
    # ars port-profile pp1
    #  enable
    #  load-past-weight 20
    #  load-future-weight 9
    # !
    # ars object obj1
    #  idle-time 100
    #  max-flows 1024
    # !
    # interface Ethernet20
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  unreliable-los auto
    #  shutdown
    #  ars bind pp1
    # !
    # ars bind profile p1

    - name: Delete all ARS configuration
      dellemc.enterprise_sonic.sonic_ars:
        config:
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration ars
    # (No ARS configuration present)



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
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>when changed</td>
                <td>
                            <div>The configuration resulting from module invocation.</div>
                    <br/>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>after_generated</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>when <code>check_mode</code></td>
                <td>
                            <div>The generated configuration from module invocation.</div>
                    <br/>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>before</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The configuration prior to the module invocation.</div>
                    <br/>
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

- S\. Talabi (@stalabi1)
