.. _dellemc.enterprise_sonic.sonic_dcbx_module:


***********************************
dellemc.enterprise_sonic.sonic_dcbx
***********************************

**Manage DCBx configurations on SONiC**


Version added: 3.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of DCBx parameters in devices running SONiC.




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
                        <div>The set of DCBx attribute configurations</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>global</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Global DCBx configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
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
                        <div>This argument is a boolean value to enable or disable DCBx.</div>
                        <div>It has a default value of False in SONiC and has an operational</div>
                        <div>default value of False for the enterproise_sonic Ansible collection</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interfaces</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Interfaces DCBx configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
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
                        <div>This argument is a boolean value to enable or disable DCBx.</div>
                        <div>It has a default value of True in SONiC and has an operational</div>
                        <div>default value of True for the enterprise_sonic Ansible collection</div>
                        <div>This command is supported only on physical interfaces and not on logical interfaces.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ets_configuration_tlv_enabled</b>
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
                        <div>This command can be used to select whether to advertise and receive ETS configuration TLV.</div>
                        <div>It has a default value of True in SONiC and has an operational</div>
                        <div>default value of True for the enterproise_sonic Ansible collection</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ets_recommendation_tlv_enabled</b>
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
                        <div>This command can be used to select whether to advertise and receive ETS recommendation TLV.</div>
                        <div>It has a default value of True in SONiC and has an operational</div>
                        <div>default value of True for the enterproise_sonic Ansible collection</div>
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
                        <div>Interface name for which DCBx needs to be configured.</div>
                        <div>This must be a physical (Ethernet) interface.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>pfc_tlv_enabled</b>
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
                        <div>This command can be used to select whether to advertise and receive PFC TLV.</div>
                        <div>It has a default value of True in SONiC and has an operational</div>
                        <div>default value of True for the enterproise_sonic Ansible collection</div>
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
                        <div>The state specifies the type of configuration update to be performed on the device.</div>
                        <div>If the state is &quot;merged&quot;, merge specified attributes with existing configured attributes.</div>
                        <div>For &quot;deleted&quot;, delete the specified attributes from existing configuration.</div>
                </td>
            </tr>
    </table>
    <br/>




Examples
--------

.. code-block:: yaml

    # Using "merged" state for DCBx interface configuration
    #
    # Before State:
    # -------------
    #
    # sonic# show running-configuration interface Ethernet0
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 25000
    #  unreliable-los auto
    #  no shutdown

    - name: Modify DCBx Interface configurations
      dellemc.enterprise_sonic.sonic_dcbx:
        config:
          -interfaces:
            - name: Ethernet0
              enabled: false
              pfc_tlv_enabled: false
              ets_configuration_tlv_enabled: false
              ets_recommendation_tlv_enabled: false
        state: merged

    # After State:
    # ------------
    #
    # sonic# show running-configuration interface Ethernet0
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 25000
    #  unreliable-los auto
    #  no shutdown
    #  no dcbx enable
    #  no dcbx tlv-select pfc
    #  no dcbx tlv-select ets-conf
    #  no dcbx tlv-select ets-reco

    # Using "merged" state for DCBx global configuration
    #
    # Before State:
    # -------------
    #
    # sonic# show running-configuration | grep dcbx
    # sonic#

    - name: Modify DCBX configurations
      dellemc.enterprise_sonic.sonic_dcbx:
        config:
          global:
            enabled: true
        state: merged

    # After State:
    # ------------
    #
    # sonic# show running-configuration | grep dcbx
    # !
    # dcbx enable
    # !

    # Using "merged" state for DCBx interface configuration
    #
    # Before State:
    # -------------
    # sonic# show running-configuration interface Ethernet 0
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 25000
    #  unreliable-los auto
    #  no shutdown
    #  no dcbx enable
    #  no dcbx tlv-select pfc
    #  no dcbx tlv-select ets-conf
    #  no dcbx tlv-select ets-reco


    - name: Modify DCBx Interface configurations
      dellemc.enterprise_sonic.sonic_dcbx:
        config:
          interfaces:
            - name: Ethernet0
              enabled: true
              pfc_tlv_enabled: true
              ets_configuration_tlv_enabled: true
              ets_recommendation_tlv_enabled: true
        state: merged

    # After State:
    # ------------
    #
    # sonic# show running-configuration interface Ethernet0
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 25000
    #  unreliable-los auto
    #  no shutdown

    # Using "deleted" state for DCBx interface configuration
    #
    # Before State:
    # -------------
    #
    # sonic# show running-configuration interface Ethernet 0
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 25000
    #  unreliable-los auto
    #  no shutdown
    #  no dcbx enable
    #  no dcbx tlv-select pfc
    #  no dcbx tlv-select ets-conf
    #  no dcbx tlv-select ets-reco


    - name: Delete and set default DCBx Interface configurations
      dellemc.enterprise_sonic.sonic_dcbx:
        config:
          interfaces:
            - name: Ethernet0
              enabled: false
              pfc_tlv_enabled: false
              ets_configuration_tlv_enabled: false
              ets_recommendation_tlv_enabled: false
        state: deleted

    # After State:
    # ------------
    #
    # sonic# show running-configuration interface Ethernet0
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 25000
    #  unreliable-los auto
    #  no shutdown

    # Using "replaced" state for DCBx interface configuration
    #
    # Before State:
    # -------------
    #
    # sonic# show running-configuration interface Ethernet0
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 25000
    #  unreliable-los auto
    #  no shutdown
    #  no dcbx tlv-select pfc
    #  no dcbx tlv-select ets-conf
    #  no dcbx tlv-select ets-reco
    #
    # sonic# show running-configuration interface Ethernet4
    # !
    # interface Ethernet4
    #  mtu 9100
    #  speed 25000
    #  unreliable-los auto
    #  no shutdown
    #  no dcbx enable
    #  no dcbx tlv-select pfc

    - name: Modify DCBx Interface configurations
      dellemc.enterprise_sonic.sonic_dcbx:
        config:
          -interfaces:
            - name: Ethernet0
              enabled: false
        state: replaced

    # After State:
    # ------------
    #
    # sonic# show running-configuration interface Ethernet0
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 25000
    #  unreliable-los auto
    #  no shutdown
    #  no dcbx enable
    #
    # sonic# show running-configuration interface Ethernet4
    # !
    # interface Ethernet4
    #  mtu 9100
    #  speed 25000
    #  unreliable-los auto
    #  no shutdown
    #  no dcbx enable
    #  no dcbx tlv-select pfc

    # Using "overridden" state for DCBx interface configuration
    #
    # Before State:
    # -------------
    # sonic# show running-configuration interface Ethernet0
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 25000
    #  unreliable-los auto
    #  no shutdown
    #  no dcbx tlv-select pfc
    #  no dcbx tlv-select ets-conf
    #  no dcbx tlv-select ets-reco
    #
    # sonic# show running-configuration interface Ethernet4
    # !
    # interface Ethernet4
    #  mtu 9100
    #  speed 25000
    #  unreliable-los auto
    #  no shutdown
    #  no dcbx enable
    #  no dcbx tlv-select pfc
    #
    # sonic# show running-configuration interface Ethernet8
    # !
    # interface Ethernet8
    #  mtu 9100
    #  speed 25000
    #  unreliable-los auto
    #  no shutdown
    #  no dcbx enable
    #  no dcbx tlv-select pfc
    #  no dcbx tlv-select ets-conf
    #  no dcbx tlv-select ets-reco
    #
    # sonic# show running-configuration interface Ethernet12
    # !
    # interface Ethernet12
    #  mtu 9100
    #  speed 25000
    #  unreliable-los auto
    #  no shutdown

    - name: Modify DCBx Interface configurations
      dellemc.enterprise_sonic.sonic_dcbx:
        config:
          -interfaces:
            - name: Ethernet0
              enabled: false
        state: overridden

    # After State:
    # ------------
    # sonic# show running-configuration interface Ethernet0
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 25000
    #  unreliable-los auto
    #  no shutdown
    #  no dcbx enable
    #
    # sonic# show running-configuration interface Ethernet4
    # !
    # interface Ethernet4
    #  mtu 9100
    #  speed 25000
    #  unreliable-los auto
    #  no shutdown
    #
    # sonic# show running-configuration interface Ethernet8
    # !
    # interface Ethernet8
    #  mtu 9100
    #  speed 25000
    #  unreliable-los auto
    #  no shutdown
    #
    # sonic# show running-configuration interface Ethernet12
    # !
    # interface Ethernet12
    #  mtu 9100
    #  speed 25000
    #  unreliable-los auto
    #  no shutdown

    # Using "deleted" state for DCBx global configuration
    #
    # Before State:
    # -------------
    #
    # sonic# show running-configuration | grep dcbx
    # !
    # dcbx enable
    # !

    - name: Delete DCBX mode configuration
      dellemc.enterprise_sonic.sonic_dcbx:
        config:
          global:
            enabled: true
        state: deleted

    # After State:
    # ------------
    #
    # sonic# show running-configuration | grep dcbx
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

- Bing Sun(@bsun-sudo), Haemanthi Sree KR (@haemanthisree)
