.. _dellemc.enterprise_sonic.sonic_vxlans_module:


*************************************
dellemc.enterprise_sonic.sonic_vxlans
*************************************

**Manage VXLAN configuration on SONiC**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of VXLAN for devices running SONiC




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
                        <div>A list of VXLAN configurations</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dscp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 4.0.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>DSCP value of the VXLAN tunnel outer IP header, range 0-63</div>
                        <div>Valid only when <em>qos_mode=pipe</em></div>
                        <div>Functional default is 0</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>evpn_nvo</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>EVPN NVO name</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>external_ip</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 2.5.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>The VTEP MCLAG external IP address for this node</div>
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
                        <div>Name of the VXLAN</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>primary_ip</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The VTEP MCLAG primary IP address for this node</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>qos_mode</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 4.0.0</div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>pipe</li>
                                    <li>uniform</li>
                        </ul>
                </td>
                <td>
                        <div>QoS mode to use for prioritizing the network traffic within a VXLAN tunnel</div>
                        <div>Functional default is <code>pipe</code></div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>source_ip</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Source IP address of the VTEP</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>suppress_vlan_neigh</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.1.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of suppress VLAN neighbor configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vlan_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of VLAN</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vlan_map</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of VNI VLAN map configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vlan</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>VLAN ID for VNI VLAN map</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vni</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the VNI ID</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vrf_map</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of VNI VRF map configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vni</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the VNI ID</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vrf</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>VRF name for VNI VRF map</div>
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

    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration vxlan
    #
    # interface vxlan vteptest1
    # source-ip 1.1.1.1
    # primary-ip 2.2.2.2
    # map vni 101 vlan 11
    # map vni 102 vlan 12
    # map vni 101 vrf Vrfcheck1
    # map vni 102 vrf Vrfcheck2
    # suppress vlan-neigh vlan_name Vlan11
    # suppress vlan-neigh vlan_name Vlan12
    # !

    - name: "Test vxlans deleted state 01"
      dellemc.enterprise_sonic.sonic_vxlans:
        config:
          - name: vteptest1
            source_ip: 1.1.1.1
            vlan_map:
              - vni: 101
                vlan: 11
            vrf_map:
              - vni: 101
                vrf: Vrfcheck1
            suppress_vlan_neigh:
              - vlan_name: Vlan11
              - vlan_name: Vlan12
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration vxlan
    #
    # interface vxlan vteptest1
    # source-ip 1.1.1.1
    # map vni 102 vlan 12
    # map vni 102 vrf Vrfcheck2
    # !


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration vxlan
    #
    # interface vxlan vteptest1
    # source-ip 1.1.1.1
    # qos-mode pipe dscp 14
    # map vni 102 vlan 12
    # map vni 102 vrf Vrfcheck2
    # !

    - name: "Test vxlans deleted state 02"
      dellemc.enterprise_sonic.sonic_vxlans:
        config:
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration vxlan
    #
    # !


    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration vxlan
    #
    # !

    - name: "Test vxlans merged state 01"
      dellemc.enterprise_sonic.sonic_vxlans:
        config:
          - name: vteptest1
            source_ip: 1.1.1.1
            primary_ip: 2.2.2.2
            evpn_nvo: nvo1
            qos_mode: pipe
            dscp: 14
            vlan_map:
              - vni: 101
                vlan: 11
              - vni: 102
                vlan: 12
            vrf_map:
              - vni: 101
                vrf: Vrfcheck1
              - vni: 102
                vrf: Vrfcheck2
            suppress_vlan_neigh:
              - vlan_name: Vlan11
              - vlan_name: Vlan12
        state: merged

    # After state:
    # ------------
    #
    # sonic# show running-configuration vxlan
    #
    # interface vxlan vteptest1
    # source-ip 1.1.1.1
    # primary-ip 2.2.2.2
    # qos-mode pipe dscp 14
    # map vni 101 vlan 11
    # map vni 102 vlan 12
    # map vni 101 vrf Vrfcheck1
    # map vni 102 vrf Vrfcheck2
    # suppress vlan-neigh vlan-name Vlan11
    # suppress vlan-neigh vlan-name Vlan12
    # !


    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration vxlan
    #
    # interface vxlan vteptest1
    # source-ip 1.1.1.1
    # primary-ip 2.2.2.2
    # map vni 101 vlan 11
    # map vni 102 vlan 12
    # map vni 101 vrf Vrfcheck1
    # map vni 102 vrf Vrfcheck2
    # !

    - name: "Test vxlans overridden state 01"
      dellemc.enterprise_sonic.sonic_vxlans:
        config:
          - name: vteptest2
            source_ip: 3.3.3.3
            primary_ip: 4.4.4.4
            evpn_nvo: nvo2
            vlan_map:
              - vni: 101
                vlan: 11
            vrf_map:
              - vni: 101
                vrf: Vrfcheck1
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show running-configuration vxlan
    #
    # interface vxlan vteptest2
    # source-ip 3.3.3.3
    # primary-ip 4.4.4.4
    # map vni 101 vlan 11
    # map vni 101 vrf Vrfcheck1
    # !


    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration vxlan
    #
    # interface vxlan vteptest2
    # source-ip 3.3.3.3
    # primary-ip 4.4.4.4
    # map vni 101 vlan 11
    # map vni 101 vrf Vrfcheck
    # !

    - name: "Test vxlans replaced state 01"
      dellemc.enterprise_sonic.sonic_vxlans:
        config:
          - name: vteptest2
            source_ip: 5.5.5.5
            vlan_map:
              - vni: 101
                vlan: 12
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show running-configuration vxlan
    #
    # interface vxlan vteptest2
    # source-ip 5.5.5.5
    # primary-ip 4.4.4.4
    # map vni 101 vlan 12
    # map vni 101 vrf Vrfcheck1
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

- Niraimadaiselvam M (@niraimadaiselvamm)
