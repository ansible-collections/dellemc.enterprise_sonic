.. _dellemc.enterprise_sonic.sonic_qos_scheduler_module:


********************************************
dellemc.enterprise_sonic.sonic_qos_scheduler
********************************************

**Manage QoS scheduler configuration on SONiC**


Version added: 2.5.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of QoS scheduler for devices running SONiC




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
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>QoS scheduler configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Name of scheduler policy</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>schedulers</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Schedulers configuration for the scheduler policy</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>cbs</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Committed burst size measured in bytes</div>
                        <div>Range 0-125000000</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>cir</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Committed information rate measured in bps</div>
                        <div>Range 0-400000000000</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>meter_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>packets</li>
                                    <li>bytes</li>
                        </ul>
                </td>
                <td>
                        <div>Metering method used by the scheduler</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>pbs</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Excess burst size measured in bytes</div>
                        <div>Range 0-125000000</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>pir</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Peak information rate measured in bps</div>
                        <div>Range 0-400000000000, must be greater than or equal to cir</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>scheduler_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>dwrr</li>
                                    <li>wrr</li>
                                    <li>strict</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the type of scheduler</div>
                        <div>Strict priority scheduling cannot be configured with weight</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>sequence</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Sequence number of the scheduler</div>
                        <div>Range 0-7 for interface queues</div>
                        <div>Range 0-47 for CPU queues</div>
                        <div>Specify 255 for port queues</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
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
                        <div>Weight of the scheduler</div>
                        <div>Range 1-100</div>
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
    # sonic# show qos scheduler-policy
    # (No qos scheduler-policy configuration present)

    - name: Merge QoS scheduler configurations
      dellemc.enterprise_sonic.sonic_qos_scheduler:
        config:
          - name: policy1
            schedulers:
              - sequence: 0
                scheduler_type: dwrr
                weight: 10
                meter_type: packets
                cir: 32000
                pir: 40000
                cbs: 30000
                pbs: 35000
        state: merged

    # After state:
    # ------------
    #
    # sonic# show qos scheduler-policy
    # Scheduler Policy: policy1
    #   Queue: 0
    #              type: dwrr
    #              weight: 10
    #              meter-type: packets
    #              cir: 32000       Pps
    #              cbs: 30000       Packets
    #              pir: 40000       Pps
    #              pbs: 35000       Packets


    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show qos scheduler-policy
    # Scheduler Policy: policy1
    #   Queue: 0
    #              type: dwrr
    #              weight: 10
    #              meter-type: packets
    #              cir: 32000       Pps
    #              cbs: 30000       Packets
    #              pir: 40000       Pps
    #              pbs: 35000       Packets

    - name: Replace QoS scheduler configurations
      dellemc.enterprise_sonic.sonic_qos_scheduler:
        config:
          - name: policy1
            schedulers:
              - sequence: 0
                weight: 12
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show qos scheduler-policy
    # Scheduler Policy: policy1
    #   Queue: 0
    #              weight: 12


    # Using "overridden" state
    # Before state:
    # -------------
    #
    # sonic# show qos scheduler-policy
    # Scheduler Policy: policy1
    #   Queue: 0
    #              type: dwrr
    #              weight: 10
    #              meter-type: packets
    #              cir: 32000       Pps
    #              cbs: 30000       Packets
    #              pir: 40000       Pps
    #              pbs: 35000       Packets
    #   Queue: 1
    #              type: dwrr
    #              weight: 14
    #              meter-type: packets

    - name: Override QoS scheduler configurations
      dellemc.enterprise_sonic.sonic_qos_scheduler:
        config:
          - name: policy2
            schedulers:
              - sequence: 0
                scheduler_type: wrr
                weight: 5
                meter_type: bytes
                cir: 50000
                pir: 60000
                cbs: 800000
                pbs: 900000
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show qos scheduler-policy
    # Scheduler Policy: policy2
    #   Queue: 0
    #              type: wrr
    #              weight: 5
    #              meter-type: bytes
    #              cir: 50          Kbps
    #              cbs: 800000      Bytes
    #              pir: 60          Kbps
    #              pbs: 900000      Bytes


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show qos scheduler-policy
    # Scheduler Policy: policy1
    #   Queue: 0
    #              type: dwrr
    #              weight: 10
    #              meter-type: packets
    #              cir: 32000       Pps
    #              cbs: 30000       Packets
    #              pir: 40000       Pps
    #              pbs: 35000       Packets
    #   Queue: 1
    #              type: dwrr
    #              weight: 14
    #              meter-type: packets
    # Scheduler Policy: policy2
    #   Queue: 0
    #              type: wrr
    #              weight: 5
    #              meter-type: bytes
    #              cir: 50          Kbps
    #              cbs: 800000      Bytes
    #              pir: 60          Kbps
    #              pbs: 900000      Bytes

    - name: Delete QoS scheduler configurations
      dellemc.enterprise_sonic.sonic_qos_scheduler:
        config:
          - name: policy1
            schedulers:
              - sequence: 0
                cir: 32000
                pir: 40000
                cbs: 30000
                pbs: 35000
              - sequence: 1
          - name: policy2
        state: deleted

    # After state:
    # -------------
    #
    # sonic# show qos scheduler-policy
    # Scheduler Policy: policy1
    #   Queue: 0
    #              type: dwrr
    #              weight: 10
    #              meter-type: packets



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
                            <div>The resulting configuration from module invocation.</div>
                    <br/>
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
                      <span style="color: purple">list</span>
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

- S. Talabi (@stalabi1)
