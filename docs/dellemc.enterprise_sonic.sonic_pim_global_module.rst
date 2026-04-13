.. _dellemc.enterprise_sonic.sonic_pim_global_module:


*****************************************
dellemc.enterprise_sonic.sonic_pim_global
*****************************************

**Manage global PIM configurations on SONiC**


Version added: 2.5.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of global PIM parameters for devices running SONiC.
- VRF and prefix-list need to be created earlier in the device.




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
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies global PIM configurations.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ecmp_enable</b>
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
                        <div>Enable PIM ECMP.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ecmp_rebalance_enable</b>
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
                        <div>Enable PIM ECMP rebalance.</div>
                        <div>ECMP has to be enabled for configuring ECMP rebalance.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>join_prune_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the PIM Join Prune Interval in seconds.</div>
                        <div>The range is from 60 to 600.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>keepalive_timer</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the PIM Keepalive timer in seconds.</div>
                        <div>The range is from 31 to 60000.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ssm_prefix_list</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the SSM prefix-list.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
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
                        <div>Name of the VRF to which the PIM configurations belong.</div>
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
                                    <li>replaced</li>
                                    <li>overridden</li>
                        </ul>
                </td>
                <td>
                        <div>The state of the configuration after module completion.</div>
                        <div><code>merged</code> - Merges provided global PIM configuration with on-device configuration.</div>
                        <div><code>replaced</code> - Replaces on-device PIM configuration of the specified VRFs with provided configuration.</div>
                        <div><code>overridden</code> - Overrides all on-device global PIM configurations with the provided configuration.</div>
                        <div><code>deleted</code> - Deletes on-device global PIM configuration.</div>
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
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration | grep "ip pim"
    # ip pim vrf VrfReg1 join-prune-interval 60
    # ip pim vrf VrfReg1 keep-alive-timer 180
    # ip pim vrf VrfReg1 ssm prefix-list prefix-list-1
    # ip pim vrf VrfReg2 ecmp
    # ip pim vrf VrfReg2 ssm prefix-list prefix-list-2
    # ip pim vrf default ecmp
    # ip pim vrf default ecmp rebalance
    # sonic#

    - name: Delete specified global PIM configurations
      dellemc.enterprise_sonic.sonic_pim_global:
        config:
          - vrf_name: 'VrfReg1'
            join_prune_interval: 60
            keepalive_timer: 180
          - vrf_name: 'VrfReg2'
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration | grep "ip pim"
    # ip pim vrf VrfReg1 ssm prefix-list prefix-list-1
    # ip pim vrf default ecmp
    # ip pim vrf default ecmp rebalance
    # sonic#


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration | grep "ip pim"
    # ip pim vrf VrfReg1 join-prune-interval 60
    # ip pim vrf VrfReg1 keep-alive-timer 180
    # ip pim vrf VrfReg1 ssm prefix-list prefix-list-1
    # ip pim vrf VrfReg2 ecmp
    # ip pim vrf VrfReg2 ssm prefix-list prefix-list-2
    # ip pim vrf default ecmp
    # ip pim vrf default ecmp rebalance
    # sonic#

    - name: Delete all global PIM configurations
      dellemc.enterprise_sonic.sonic_pim_global:
        config:
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration | grep "ip pim"
    # sonic#


    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration | grep "ip pim"
    # ip pim vrf default join-prune-interval 120
    # ip pim vrf default keep-alive-timer 360
    # ip pim vrf default ssm prefix-list prefix-list-1
    # sonic#

    - name: Merge provided global PIM configurations
      dellemc.enterprise_sonic.sonic_pim_global:
        config:
          - vrf_name: 'default'
            ecmp_enable: true
            ecmp_rebalance_enable: true
            join_prune_interval: 60
            keepalive_timer: 180
            ssm_prefix_list: 'prefix-list-def'
          - vrf_name: 'VrfReg1'
            join_prune_interval: 60
            keepalive_timer: 180
          - vrf_name: 'VrfReg2'
            ssm_prefix_list: 'prefix-list-2'
        state: merged

    # After state:
    # ------------
    #
    # sonic# show running-configuration | grep "ip pim"
    # ip pim vrf VrfReg1 join-prune-interval 60
    # ip pim vrf VrfReg1 keep-alive-timer 180
    # ip pim vrf VrfReg2 ssm prefix-list prefix-list-2
    # ip pim vrf default ecmp
    # ip pim vrf default ecmp rebalance
    # ip pim vrf default join-prune-interval 60
    # ip pim vrf default keep-alive-timer 180
    # ip pim vrf default ssm prefix-list prefix-list-def
    # sonic#


    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration | grep "ip pim"
    # ip pim vrf VrfReg1 join-prune-interval 60
    # ip pim vrf VrfReg1 keep-alive-timer 180
    # ip pim vrf VrfReg1 ssm prefix-list prefix-list-1
    # ip pim vrf VrfReg2 ecmp
    # ip pim vrf VrfReg2 ssm prefix-list prefix-list-2
    # ip pim vrf default ecmp
    # ip pim vrf default ecmp rebalance
    # sonic#

    - name: Replace global PIM configurations of specified VRFs
      dellemc.enterprise_sonic.sonic_pim_global:
        config:
          - vrf_name: 'default'
            ecmp_enable: true
          - vrf_name: 'VrfReg1'
            join_prune_interval: 120
            keepalive_timer: 360
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show running-configuration | grep "ip pim"
    # ip pim vrf VrfReg1 join-prune-interval 120
    # ip pim vrf VrfReg1 keep-alive-timer 360
    # ip pim vrf VrfReg2 ecmp
    # ip pim vrf VrfReg2 ssm prefix-list prefix-list-2
    # ip pim vrf default ecmp
    # sonic#


    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration | grep "ip pim"
    # ip pim vrf VrfReg1 join-prune-interval 60
    # ip pim vrf VrfReg1 keep-alive-timer 180
    # ip pim vrf VrfReg1 ssm prefix-list prefix-list-1
    # ip pim vrf VrfReg2 ecmp
    # ip pim vrf VrfReg2 ssm prefix-list prefix-list-2
    # ip pim vrf default ecmp
    # ip pim vrf default ecmp rebalance
    # sonic#

    - name: Override global PIM configurations
      dellemc.enterprise_sonic.sonic_pim_global:
        config:
          - vrf_name: 'default'
            ecmp_enable: true
          - vrf_name: 'VrfReg1'
            join_prune_interval: 120
            keepalive_timer: 360
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show running-configuration | grep "ip pim"
    # ip pim vrf VrfReg1 join-prune-interval 120
    # ip pim vrf VrfReg1 keep-alive-timer 360
    # ip pim vrf default ecmp
    # sonic#



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
                            <div>The resulting configuration on module invocation.</div>
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
                            <div>The generated configuration on module invocation.</div>
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

- Arun Saravanan Balachandran (@ArunSaravananBalachandran)
