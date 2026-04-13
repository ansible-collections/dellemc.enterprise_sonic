.. _dellemc.enterprise_sonic.sonic_lldp_global_module:


******************************************
dellemc.enterprise_sonic.sonic_lldp_global
******************************************

**Manage Global LLDP configurations on SONiC**


Version added: 2.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of global LLDP parameters for use on LLDP enabled Layer 2 interfaces of devices running SONiC.
- It is intended for use in conjunction with LLDP Layer 2 interface configuration applied on participating interfaces.




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
                        <div>The set of link layer discovery protocol global attribute configurations</div>
                </td>
            </tr>
                                <tr>
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
                        <div>This argument is a boolean value to enable or disable LLDP.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>hello_time</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Frequency at which LLDP advertisements are sent (in seconds).</div>
                        <div>The range is from 5 to 254 sec</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mode</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>receive</li>
                                    <li>transmit</li>
                        </ul>
                </td>
                <td>
                        <div>By default both transmit and receive of LLDP frames is enabled.</div>
                        <div>This command can be used to configure either in receive only or transmit only mode.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>multiplier</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Multiplier value is used to determine the timeout interval (i.e. hello-time x multiplier value)</div>
                        <div>The range is from 1 to 10</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>system_description</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Description of this system to be sent in LLDP advertisements.</div>
                        <div>When configured, this value is used in the advertisements instead of the default system description.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>system_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifying a descriptive system name using this command, user may find it easier to distinguish the device with LLDP.</div>
                        <div>By default, the host name is used.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>tlv_select</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>By default, management address and system capabilities TLV are advertised in LLDP frames.</div>
                        <div>This configuration option can be used to selectively suppress sending of these TLVs to the Peer.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>management_address</b>
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
                        <div>Enable or disable management address TLV.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>system_capabilities</b>
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
                        <div>Enable or disable system capabilities TLV.</div>
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
                        </ul>
                </td>
                <td>
                        <div>The state specifies the type of configuration update to be performed on the device.</div>
                        <div>If the state is &quot;merged&quot;, merge specified attributes with existing configured attributes.</div>
                        <div>For &quot;deleted&quot;, delete the specified attributes from existing configuration.</div>
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
    # sonic# show running-configuration
    # !
    # lldp receive
    # lldp timer 200
    # lldp multiplier 1
    # lldp system-name 8999_System
    # lldp system-description sonic_system
    # !

    - name: Delete LLDP configurations
      dellemc.enterprise_sonic.sonic_lldp_global:
        config:
          hello_time: 200
          system_description: sonic_system
          mode: receive
          multiplier: 1
        state: deleted

    # After state:
    # ------------
    # sonic# show running-configuration | grep lldp
    # !
    # lldp system-name 8999_System
    # !
    # sonic#


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration | grep lldp
    # sonic#

    - name: Delete default LLDP configurations
      dellemc.enterprise_sonic.sonic_lldp_global:
        config:
          tlv_select:
            system_capabilities: true
        state: deleted

    # After state:
    # ------------
    # sonic# show running-configuration
    # !
    # no lldp tlv-select system-capabilities
    # !


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration | grep lldp
    # !
    # lldp receive
    # lldp timer 200
    # lldp multiplier 1
    # lldp system-name 8999_System
    # lldp system-description sonic_system
    # !

    - name: Delete all LLDP configuration
      dellemc.enterprise_sonic.sonic_lldp_global:
        config:
        state: deleted

    # After state:  (No LLDP global configuration present.)
    # ------------
    # sonic# show running-configuration | grep lldp
    # sonic#


    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration | grep lldp
    # sonic#

    - name: Modify LLDP configurations
      dellemc.enterprise_sonic.sonic_lldp_global:
        config:
          enable: false
          multiplier: 9
          system_name: CR_sonic
          hello_time: 18
          mode: receive
          system_description: Sonic_System
          tlv_select:
            management_address: true
            system_capabilities: false
        state: merged

    # After state:
    # ------------
    # sonic# show running-configuration | grep lldp
    # !
    # no lldp enable
    # no lldp tlv-select system_capabilities
    # lldp receive
    # lldp timer 18
    # lldp multiplier 9
    # lldp system-name CR_sonic
    # lldp system-description Sonic_System
    # !


    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration | grep lldp
    # !
    # lldp receive
    # lldp timer 200
    # lldp multiplier 1
    # lldp system-name 8999_System
    # lldp system-description sonic_system
    # !

    - name: Modify LLDP configurations
      dellemc.enterprise_sonic.sonic_lldp_global:
        config:
          multiplier: 9
          system_name: CR_sonic
        state: merged

    # After state:
    # ------------
    # sonic# show running-configuration | grep lldp
    # !
    # lldp receive
    # lldp timer 200
    # lldp multiplier 9
    # lldp system-name CR_sonic
    # lldp system-description sonic_system
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format as the parameters above.</div>
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

- Divya Balasubramanian(@divya-balasubramania)
