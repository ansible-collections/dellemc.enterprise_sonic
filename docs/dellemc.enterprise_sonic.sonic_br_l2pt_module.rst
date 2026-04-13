.. _dellemc.enterprise_sonic.sonic_br_l2pt_module:


**************************************
dellemc.enterprise_sonic.sonic_br_l2pt
**************************************

**Manage L2PT configurations on SONiC**


Version added: 3.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of L2PT parameters in devices running SONiC.




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
                        <div>A list of L2PT configurations.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>bridge_l2pt_params</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>VLAN ID list per supported Layer 2 protocol.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
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
                                    <li>LLDP</li>
                                    <li>LACP</li>
                                    <li>STP</li>
                                    <li>CDP</li>
                        </ul>
                </td>
                <td>
                        <div>L2 protocol.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vlan_ids</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of VLAN IDs on which the L2 Protocol packets are to be tunneled.</div>
                        <div>Ranges can be specified in the list of VLAN IDs using the delimiter &#x27;-&#x27;.</div>
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
                        <div>Interface name for L2PT configuration.</div>
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
    # sonic# show running-configuration interface Ethernet 0
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  unreliable-los auto
    #  no shutdown
    #  switchport l2proto-tunnel lldp Vlan 10

    - name: Modify interface L2PT configurations
      dellemc.enterprise_sonic.sonic_br_l2pt:
        config:
          - name: Ethernet0
            bridge_l2pt_params:
              - protocol: 'LACP'
                vlan_ids:
                  - 10-12
              - protocol: 'CDP'
                vlan_ids:
                  - 20
                  - 40-60
              - protocol: 'STP'
                vlan_ids:
                  - 25-26
        state: merged

    # After state:
    # ------------
    # sonic# show running-configuration interface Ethernet0
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  unreliable-los auto
    #  no shutdown
    #  switchport l2proto-tunnel cdp Vlan 20,40-60
    #  switchport l2proto-tunnel lacp Vlan 10-12
    #  switchport l2proto-tunnel lldp Vlan 10
    #  switchport l2proto-tunnel stp Vlan 25-26


    # Using "merged" state
    #
    # Before state:
    # -------------
    # sonic# show running-configuration interface Ethernet 0
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  unreliable-los auto
    #  no shutdown
    #  switchport l2proto-tunnel cdp Vlan 20, 40-50
    #  switchport l2proto-tunnel lacp Vlan 10-11
    #  switchport l2proto-tunnel lldp Vlan 10
    #  switchport l2proto-tunnel stp Vlan 25-26

    - name: Modify interface L2PT configurations
      dellemc.enterprise_sonic.sonic_br_l2pt:
        config:
          - name: Ethernet0
            bridge_l2pt_params:
              - protocol: 'LLDP'
                vlan_ids:
                  - 12
              - protocol: 'LACP'
                vlan_ids:
                  - 12
              - protocol: 'CDP'
                vlan_ids:
                  - 20
                  - 45-60
              - protocol: 'STP'
                vlan_ids:
                  - 20-21
        state: merged

    # After state:
    # ------------
    # sonic# show running-configuration interface Ethernet0
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  unreliable-los auto
    #  no shutdown
    #  switchport l2proto-tunnel cdp Vlan 20,40-60
    #  switchport l2proto-tunnel lacp Vlan 10-12
    #  switchport l2proto-tunnel lldp Vlan 10,12
    #  switchport l2proto-tunnel stp Vlan 20-21,25-26


    # Using "deleted" state
    #
    # Before state:
    # -------------
    # sonic# show running-configuration interface Ethernet 0
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  unreliable-los auto
    #  no shutdown
    #  switchport l2proto-tunnel lacp Vlan 10-12
    #  switchport l2proto-tunnel cdp Vlan 20,40-60
    #  switchport l2proto-tunnel stp Vlan 25-26

    - name: Delete interface L2PT configurations
      dellemc.enterprise_sonic.sonic_br_l2pt:
        config:
          - name: Ethernet0
            bridge_l2pt_params:
              - protocol: 'LACP'
                vlan_ids:
                  - 10-12
        state: deleted

    # After state:
    # ------------
    # sonic# show running-configuration interface Ethernet0
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  unreliable-los auto
    #  no shutdown
    #  switchport l2proto-tunnel cdp Vlan 20,40-60
    #  switchport l2proto-tunnel stp Vlan 25-26


    # Using "deleted" state
    #
    # Before state:
    # -------------
    # sonic# show running-configuration interface Ethernet 0
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  unreliable-los auto
    #  no shutdown
    #  switchport l2proto-tunnel lacp Vlan 10-12
    #  switchport l2proto-tunnel cdp Vlan 20,40-60
    #  switchport l2proto-tunnel stp Vlan 25-26
    # sonic# show running-configuration interface Ethernet 8
    # !
    # interface Ethernet8
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  unreliable-los auto
    #  no shutdown
    #  switchport l2proto-tunnel lldp Vlan 100
    #  switchport l2proto-tunnel stp Vlan 100-150

    - name: Delete all interface L2PT configurations
      dellemc.enterprise_sonic.sonic_br_l2pt:
        config:
        state: deleted

    # After state:
    # ------------
    # sonic# show running-configuration interface Ethernet0
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  unreliable-los auto
    #  no shutdown
    # sonic# show running-configuration interface Ethernet 8
    # !
    # interface Ethernet8
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  unreliable-los auto
    #  no shutdown


    # Using "deleted" state
    #
    # Before state:
    # -------------
    # sonic# show running-configuration interface Ethernet 0
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  unreliable-los auto
    #  no shutdown
    #  switchport l2proto-tunnel lacp Vlan 10-12
    #  switchport l2proto-tunnel cdp Vlan 20,40-60
    #  switchport l2proto-tunnel stp Vlan 25-26

    - name: Delete L2PT configurations for protocol
      dellemc.enterprise_sonic.sonic_br_l2pt:
        config:
          - name: Ethernet0
            bridge_l2pt_params:
              - protocol: 'LACP'
              - protocol: 'CDP'
                vlan_ids: []
        state: deleted

    # After state:
    # ------------
    # sonic# show running-configuration interface Ethernet0
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  unreliable-los auto
    #  no shutdown
    #  switchport l2proto-tunnel stp Vlan 25-26


    # Using "deleted" state
    #
    # Before state:
    # -------------
    # sonic# show running-configuration interface Ethernet 0
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  unreliable-los auto
    #  no shutdown
    #  switchport l2proto-tunnel lacp Vlan 10-12
    #  switchport l2proto-tunnel cdp Vlan 20,40-60
    #  switchport l2proto-tunnel stp Vlan 25-26

    - name: Delete interface L2PT configurations
      dellemc.enterprise_sonic.sonic_br_l2pt:
        config:
          - name: Ethernet0
            bridge_l2pt_params:
              - protocol: 'LACP'
                vlan_ids:
                  - 11
              - protocol: 'CDP'
                vlan_ids:
                  - 40-50
        state: deleted

    # After state:
    # ------------
    # sonic# show running-configuration interface Ethernet0
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  unreliable-los auto
    #  no shutdown
    #  switchport l2proto-tunnel lacp Vlan 10,12
    #  switchport l2proto-tunnel cdp Vlan 20,51-60
    #  switchport l2proto-tunnel stp Vlan 25-26


    # Using "deleted" state
    #
    # Before state:
    # -------------
    # sonic# show running-configuration interface Ethernet 0
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  unreliable-los auto
    #  no shutdown
    #  switchport l2proto-tunnel lacp Vlan 10-12
    #  switchport l2proto-tunnel cdp Vlan 20,40-60
    #  switchport l2proto-tunnel stp Vlan 25-26
    # sonic# show running-configuration interface Ethernet 8
    # !
    # interface Ethernet8
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  unreliable-los auto
    #  no shutdown
    #  switchport l2proto-tunnel lacp Vlan 10-12
    #  switchport l2proto-tunnel cdp Vlan 20,40-60
    #  switchport l2proto-tunnel stp Vlan 25-26

    - name: Delete L2PT configurations for entire interface
      dellemc.enterprise_sonic.sonic_br_l2pt:
        config:
          - name: Ethernet0
            bridge_l2pt_params: []
          - name: Ethernet8
        state: deleted

    # After state:
    # ------------
    # sonic# show running-configuration interface Ethernet 0
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  unreliable-los auto
    #  no shutdown
    # sonic# show running-configuration interface Ethernet 8
    # !
    # interface Ethernet8
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  unreliable-los auto
    #  no shutdown


    # Using "replaced" state
    #
    # Before state:
    # -------------
    # sonic# show running-configuration interface Ethernet 0
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  unreliable-los auto
    #  no shutdown
    #  switchport l2proto-tunnel lacp Vlan 10-12
    #  switchport l2proto-tunnel cdp Vlan 20,40-60
    #  switchport l2proto-tunnel stp Vlan 25-26
    # sonic# show running-configuration interface Ethernet 8
    # !
    # interface Ethernet8
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  unreliable-los auto
    #  no shutdown
    #  switchport l2proto-tunnel lldp Vlan 100
    #  switchport l2proto-tunnel stp Vlan 100-150

    - name: Replace interface L2PT configurations
      dellemc.enterprise_sonic.sonic_br_l2pt:
        config:
          - name: Ethernet0
            bridge_l2pt_params:
              - protocol: 'LLDP'
                vlan_ids:
                  - 10-12
              - protocol: 'LACP'
                vlan_ids:
                  - 8
                  - 12-14
              - protocol: 'CDP'
                vlan_ids:
                  - 20-45
        state: replaced

    # After state:
    # ------------
    # sonic# show running-configuration interface Ethernet 0
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  unreliable-los auto
    #  no shutdown
    #  switchport l2proto-tunnel lldp Vlan 10-12
    #  switchport l2proto-tunnel lacp Vlan 8,12-14
    #  switchport l2proto-tunnel cdp Vlan 20-45
    # sonic# show running-configuration interface Ethernet 8
    # !
    # interface Ethernet8
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  unreliable-los auto
    #  no shutdown
    #  switchport l2proto-tunnel lldp Vlan 100
    #  switchport l2proto-tunnel stp Vlan 100-150


    # Using "overridden" state
    #
    # Before state:
    # -------------
    # sonic# show running-configuration interface Ethernet 0
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  unreliable-los auto
    #  no shutdown
    #  switchport l2proto-tunnel lldp Vlan 10
    #  switchport l2proto-tunnel lacp Vlan 15-50
    #  switchport l2proto-tunnel cdp 20
    #  switchport l2proto-tunnel stp 25-26
    # sonic# show running-configuration interface Ethernet 8
    # !
    # interface Ethernet8
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  unreliable-los auto
    #  no shutdown
    #  switchport l2proto-tunnel lldp Vlan 100
    #  switchport l2proto-tunnel stp Vlan 100-150

    - name: Override interface L2PT configurations
      dellemc.enterprise_sonic.sonic_br_l2pt:
        config:
          - name: Ethernet0
            bridge_l2pt_params:
              - protocol: 'LACP'
                vlan_ids:
                  - 10-12
              - protocol: 'CDP'
                vlan_ids:
                  - 20
                  - 40-60
              - protocol: 'STP'
                vlan_ids:
                  - 25-26
        state: overridden

    # After state:
    # ------------
    # sonic# show running-configuration interface Ethernet0
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  unreliable-los auto
    #  no shutdown
    #  switchport l2proto-tunnel cdp Vlan 20,40-60
    #  switchport l2proto-tunnel lacp Vlan 10-12
    #  switchport l2proto-tunnel stp Vlan 25-26



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
                            <div>The configuration that would result from non-check-mode module invocation.</div>
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
                            <div>The set of commands pushed to the remote device. In <code>check_mode</code> the needed commands are displayed, but not pushed to the device.</div>
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

- Allen Ting (@allenkting)
