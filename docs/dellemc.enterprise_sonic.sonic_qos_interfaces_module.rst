.. _dellemc.enterprise_sonic.sonic_qos_interfaces_module:


*********************************************
dellemc.enterprise_sonic.sonic_qos_interfaces
*********************************************

**Manage QoS interfaces configuration on SONiC**


Version added: 2.5.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of QoS interfaces for devices running SONiC




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
                        <div>QoS interfaces configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>cable_length</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.1.0</div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>5m</li>
                                    <li><div style="color: blue"><b>40m</b>&nbsp;&larr;</div></li>
                                    <li>300m</li>
                        </ul>
                </td>
                <td>
                        <div>Cable length of the interface</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Name of the interface</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>pfc</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>PFC configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>asymmetric</b>
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
                        <div>Enable or disable asymmetric PFC on the interface</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>priorities</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>PFC priorities configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dot1p</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>DOT1P value, range 0-7</div>
                        <div>Maxium of 2 priorities supported</div>
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
                                    <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Enable or disable the priority</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>watchdog_action</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>drop</b>&nbsp;&larr;</div></li>
                                    <li>forward</li>
                                    <li>alert</li>
                        </ul>
                </td>
                <td>
                        <div>PFC watchdog storm action</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>watchdog_detect_time</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>PFC watchdog detection time in milliseconds, range 100-5000</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>watchdog_restore_time</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>PFC watchdog restoration time milliseconds, range 100-60000</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>qos_maps</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>QoS maps interface configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dot1p_fwd_group</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>DOT1P to forwarding group map associated with the interface</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dscp_fwd_group</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>DSCP to forwarding group map associated with the interface</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>fwd_group_dot1p</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Forwarding group to DOT1P map associated with the interface</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>fwd_group_dscp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Forwarding group to DSCP map associated with the interface</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>fwd_group_pg</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Forwading group to priority group map associated with the interface</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>fwd_group_queue</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Forwarding group to queue map associated with the interface</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>pfc_priority_pg</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>PFC priority to priority group map associated with the interface</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>pfc_priority_queue</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>PFC priority to queue map associated with the interface</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>queues</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Queue configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Queue identification</div>
                        <div>Range 0-7 for interface queues, range 0-47 for CPU queues</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>wred_profile</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of the WRED profile</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>scheduler_policy</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of scheduler policy to be applied to traffic on the interface</div>
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
                        </ul>
                </td>
                <td>
                        <div>The state of the configuration after module completion</div>
                        <div>Replaced and overridden states are not supported for this module due to configuration constraints</div>
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
    # sonic# show running-configuration interface Eth 1/5
    # !
    # interface Eth1/5
    # (No QoS configuration present for the interface)

    - name: Merge QoS interfaces configuration
      dellemc.enterprise_sonic.sonic_qos_interfaces:
        config:
          - name: Eth1/5
            queues:
              - id: 0
                wred_profile: profile1
            scheduler_policy: policy1
            cable_length: 40m
            qos_maps:
              dscp_fwd_group: dscp_map1
              dot1p_fwd_group: dot1p_map1
              fwd_group_dscp: fwd_dscp_map1
              fwd_group_dot1p: fwd_dot1p_map1
              fwd_group_queue: fwd_queue_map1
              fwd_group_pg: fwd_pg_map1
              pfc_priority_queue: pfc_queue_map1
              pfc_priority_pg: pfc_pg_map1
            pfc:
              asymmetric: true
              watchdog_action: alert
              watchdog_detect_time: 100
              watchdog_restore_time: 200
              priorities:
                - dot1p: 0
                  enable: true
                - dot1p: 1
                  enable: true
        state: merged

    # After state:
    # ------------
    #
    # sonic# show running-configuration interface Eth 1/5
    # !
    # interface Eth1/5
    #  queue 0 wred-policy profile1
    #  scheduler-policy policy1
    #  cable-length 40m
    #  qos-map dscp-tc dscp_map1
    #  qos-map dot1p-tc dot1p_map1
    #  qos-map tc-queue fwd_queue_map1
    #  qos-map tc-pg fwd_pg_map1
    #  qos-map tc-dscp fwd_dscp_map1
    #  qos-map tc-dot1p fwd_dot1p_map1
    #  qos-map pfc-priority-queue pfc_queue_map1
    #  qos-map pfc-priority-pg pfc_pg_map1
    #  priority-flow-control priority 0
    #  priority-flow-control priority 1
    #  priority-flow-control asymmetric
    #  priority-flow-control watchdog action alert
    #  priority-flow-control watchdog on detect-time 100
    #  priority-flow-control watchdog restore-time 200
    #
    #
    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface Eth 1/5
    # !
    # interface Eth1/5
    #  queue 0 wred-policy profile2
    #  queue 1 wred-policy profile1
    #  scheduler-policy policy2
    #  cable-length 5m
    #  qos-map dscp-tc dscp_map2
    #  qos-map dot1p-tc dot1p_map2
    #  qos-map tc-queue fwd_queue_map2
    #  qos-map tc-pg fwd_pg_map2
    #  qos-map tc-dscp fwd_dscp_map2
    #  qos-map tc-dot1p fwd_dot1p_map2
    #  qos-map pfc-priority-queue pfc_queue_map1
    #  qos-map pfc-priority-pg pfc_pg_map1
    #  priority-flow-control priority 1
    #  priority-flow-control watchdog action drop
    #  priority-flow-control watchdog on detect-time 150
    #  priority-flow-control watchdog restore-time 250
    # sonic# show running-configuration interface Eth 1/6
    # !
    # interface Eth1/6
    #  queue 0 wred-policy profile1
    #  scheduler-policy policy1
    #  cable-length 40m
    #  qos-map dscp-tc dscp_map1
    #  qos-map dot1p-tc dot1p_map1
    #  qos-map tc-queue fwd_queue_map1
    #  qos-map tc-pg fwd_pg_map1
    #  qos-map tc-dscp fwd_dscp_map1
    #  qos-map tc-dot1p fwd_dot1p_map1
    #  qos-map pfc-priority-queue pfc_queue_map1
    #  qos-map pfc-priority-pg pfc_pg_map1
    #  priority-flow-control priority 0
    #  priority-flow-control asymmetric
    #  priority-flow-control watchdog on detect-time 100
    #  priority-flow-control watchdog restore-time 200

    - name: Delete QoS interfaces attributes
      dellemc.enterprise_sonic.sonic_interfaces:
        config:
          - name: Eth1/5
            queues:
              - id: 0
                wred_profile: profile2
              - id: 1
            scheduler_policy: policy2
            cable_length: 5m
            qos_maps:
              dscp_fwd_group: dscp_map2
              dot1p_fwd_group: dot1p_map2
              fwd_group_dscp: fwd_dscp_map2
              fwd_group_dot1p: fwd_dot1p_map2
              fwd_group_queue: fwd_queue_map2
              fwd_group_pg: fwd_pg_map2
          - name: Eth1/6
            pfc:
              asymmetric: true
              watchdog_action: drop
              watchdog_detect_time: 100
              watchdog_restore_time: 200
              priorities:
                - dot1p: 0
                  enable: true
                - dot1p: 1
                  enable: true
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration interface Eth 1/5
    # !
    # interface Eth1/5
    #  cable-length 40m
    #  qos-map pfc-priority-queue pfc_queue_map1
    #  qos-map pfc-priority-pg pfc_pg_map1
    #  priority-flow-control priority 1
    #  priority-flow-control watchdog action drop
    #  priority-flow-control watchdog on detect-time 150
    #  priority-flow-control watchdog restore-time 250
    # sonic# show running-configuration interface Eth 1/6
    # !
    # interface Eth1/6
    #  queue 0 wred-policy profile1
    #  scheduler-policy policy1
    #  cable-length 40m
    #  qos-map dscp-tc dscp_map1
    #  qos-map dot1p-tc dot1p_map1
    #  qos-map tc-queue fwd_queue_map1
    #  qos-map tc-pg fwd_pg_map1
    #  qos-map tc-dscp fwd_dscp_map1
    #  qos-map tc-dot1p fwd_dot1p_map1
    #  qos-map pfc-priority-queue pfc_queue_map1
    #  qos-map pfc-priority-pg pfc_pg_map1



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
                <td>when changed, if <code>check_mode</code> is not set</td>
                <td>
                            <div>The resulting configuration from module invocation.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format as the parameters above.</div>
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
                            <div>The generated (simulated) configuration from module invocation.</div>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format as the parameters above.</div>
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
