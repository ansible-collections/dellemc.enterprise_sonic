.. _dellemc.enterprise_sonic.sonic_network_policy_module:


*********************************************
dellemc.enterprise_sonic.sonic_network_policy
*********************************************

**Manage network policy configuration on SONiC**


Version added: 3.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of network policy for devices running SONiC




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
                        <div>List of network policy configurations</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>applications</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of network policy application configurations</div>
                        <div><em>dot1p</em> and <em>vlan_id</em> are mutually exclusive</div>
                        <div><em>dot1p</em> cannot be configured when <em>untagged=True</em></div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>app_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>voice</li>
                                    <li>voice-signaling</li>
                        </ul>
                </td>
                <td>
                        <div>Media type of the application</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dot1p</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>enabled</li>
                        </ul>
                </td>
                <td>
                        <div>Enable dot1p priority tagging</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dscp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>DSCP value of VLAN, range 0-63</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>priority</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Priority of VLAN, range 0-7</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>untagged</b>
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
                        <div>Indicates that the application is using an untagged VLAN</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vlan_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>VLAN identifier, range 1-4094</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>number</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Network policy number, range 1-128</div>
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
    # sonic# show running-configuration
    # (No network policy configuration present)

    - name: Merge network policy configuration
      dellemc.enterprise_sonic.sonic_network_policy:
        config:
          - number: 1
            applications:
              - app_type: voice
                vlan_id: 2
                priority: 1
                dscp: 1
              - app_type: voice-signaling
                dot1p: enabled
                dscp: 50
        state: merged

    # After state:
    # ------------
    #
    # sonic# show running-configuration
    # !
    # network-policy profile 1
    #  voice vlan 2 cos 1 dscp 1
    #  voice-signaling vlan dot1p dscp 50
    # !


    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration
    # !
    # network-policy profile 1
    #  voice vlan 2 cos 1 dscp 1
    #  voice-signaling vlan 3 untagged dscp 50
    # !
    # network-policy profile 2
    #  voice vlan 100 cos 7 dscp 12
    #  voice-signaling vlan 400 cos 7 dscp 45
    # !

    - name: Replace network policy configuration
      dellemc.enterprise_sonic.sonic_network_policy:
        config:
          - number: 1
            applications:
              - app_type: voice
                vlan_id: 1
                untagged: false
                priority: 0
                dscp: 0
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show running-configuration
    # !
    # network-policy profile 1
    #  voice vlan 1 cos 0 dscp 0
    # !
    # network-policy profile 2
    #  voice vlan 100 cos 7 dscp 12
    #  voice-signaling vlan 400 cos 7 dscp 45
    # !


    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration
    # !
    # network-policy profile 1
    #  voice vlan 2 cos 1 dscp 1
    #  voice-signaling vlan 3 untagged dscp 50
    # !
    # network-policy profile 2
    #  voice vlan 100 cos 7 dscp 12
    #  voice-signaling vlan 400 cos 7 dscp 45
    # !

    - name: Override network policy configuration
      dellemc.enterprise_sonic.sonic_network_policy:
        config:
          - number: 1
            applications:
              - app_type: voice
                vlan_id: 1
                untagged: false
                priority: 0
                dscp: 0
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show running-configuration
    # !
    # network-policy profile 1
    #  voice vlan 1 cos 0 dscp 0
    # !


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration
    # !
    # network-policy profile 1
    #  voice vlan 2 cos 1 dscp 1
    #  voice-signaling vlan 3 untagged dscp 50
    # !
    # network-policy profile 2
    #  voice vlan 100 cos 7 dscp 12
    #  voice-signaling vlan 400 cos 7 dscp 45
    # !
    # network-policy profile 3
    #  voice-signaling vlan 80 cos 6 dscp 32
    # !

    - name: Delete network policy configuration
      dellemc.enterprise_sonic.sonic_network_policy:
        config:
          - number: 1
            applications:
              - app_type: voice
                dscp: 1
          - number: 2
            applications:
              - app_type: voice
          - number: 3
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration
    # !
    # network-policy profile 1
    #  voice vlan 2 cos 1
    #  voice-signaling vlan 3 untagged dscp 50
    # !
    # network-policy profile 2
    #  voice-signaling vlan 400 cos 7 dscp 45
    # !


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration
    # !
    # network-policy profile 1
    #  voice vlan 2 cos 1 dscp 1
    #  voice-signaling vlan 3 untagged dscp 50
    # !
    # network-policy profile 2
    #  voice vlan 100 cos 7 dscp 12
    #  voice-signaling vlan 400 cos 7 dscp 45
    # !
    # network-policy profile 3
    #  voice-signaling vlan 80 cos 6 dscp 32
    # !

    - name: Delete all network policy configuration
      dellemc.enterprise_sonic.sonic_network_policy:
        config:
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration
    # (No network policy configuration present)



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
