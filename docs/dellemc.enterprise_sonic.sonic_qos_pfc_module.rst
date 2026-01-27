.. _dellemc.enterprise_sonic.sonic_qos_pfc_module:


**************************************
dellemc.enterprise_sonic.sonic_qos_pfc
**************************************

**Manage QoS PFC configuration on SONiC**


Version added: 2.5.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of QoS PFC for devices running SONiC




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="2">
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
                        <div>QoS PFC configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>counter_poll</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                        </ul>
                </td>
                <td>
                        <div>Enable or disable use of flex-counters for PFC watchdog</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>poll_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Polling interval for PFC watchdog</div>
                        <div>Range 100-3000</div>
                </td>
            </tr>

            <tr>
                <td colspan="2">
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
                        <div>The state of the configuration after module completion.</div>
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
    # sonic# show priority-flow-control watchdog
    #
    # Watchdog Summary
    # ----------------
    # Polling Interval:   : Not Available
    # Flex Counters:      : enabled

    - name: Merge QoS PFC configurations
      dellemc.enterprise_sonic.sonic_qos_pfc:
        config:
          counter_poll: true
          poll_interval: 150
        state: merged

    # After state:
    # ------------
    #
    # sonic# show priority-flow-control watchdog
    #
    # Watchdog Summary
    # ----------------
    # Polling Interval:   : 150
    # Flex Counters:      : enabled
    #
    #
    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show priority-flow-control watchdog
    #
    # Watchdog Summary
    # ----------------
    # Polling Interval:   : 150
    # Flex Counters:      : enabled

    - name: Replace QoS PFC configurations
      dellemc.enterprise_sonic.sonic_qos_pfc:
        config:
          poll_interval: 365
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show priority-flow-control watchdog
    #
    # Watchdog Summary
    # ----------------
    # Polling Interval:   : 365
    # Flex Counters:      : enabled
    #
    #
    # Using "overridden" state
    # Before state:
    # -------------
    #
    # sonic# show priority-flow-control watchdog
    #
    # Watchdog Summary
    # ----------------
    # Polling Interval:   : 365
    # Flex Counters:      : enabled

    - name: Override QoS PFC configurations
      dellemc.enterprise_sonic.sonic_qos_pfc:
        config:
          counter_poll: false
          poll_interval: 400
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show priority-flow-control watchdog
    #
    # Watchdog Summary
    # ----------------
    # Polling Interval:   : 400
    # Flex Counters:      : disabled
    #
    #
    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show priority-flow-control watchdog
    #
    # Watchdog Summary
    # ----------------
    # Polling Interval:   : 400
    # Flex Counters:      : disabled

    - name: Delete QoS PFC configurations
      dellemc.enterprise_sonic.sonic_qos_pfc:
        config:
          counter_poll: false
          poll_interval: 400
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show priority-flow-control watchdog
    #
    # Watchdog Summary
    # ----------------
    # Polling Interval:   : Not Available
    # Flex Counters:      : enabled



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

- S. Talabi (@stalabi1)
