.. _dellemc.enterprise_sonic.sonic_mac_module:


**********************************
dellemc.enterprise_sonic.sonic_mac
**********************************

**Manage MAC configuration on SONiC**


Version added: 2.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of MAC for devices running SONiC




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
                        <div>A list of MAC configurations.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mac</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configuration attributes for MAC.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>aging_time</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">600</div>
                </td>
                <td>
                        <div>Time in seconds of inactivity before the MAC entry is timed out.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dampening_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">5</div>
                </td>
                <td>
                        <div>Interval for which mac movements are observed before disabling MAC learning on a port.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dampening_threshold</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">5</div>
                </td>
                <td>
                        <div>Number of MAC movements allowed per second before disabling MAC learning on a port.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mac_table_entries</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configuration attributes for MAC table entries.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interface</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the interface for the MAC table entry.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mac_address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>MAC address for the dynamic or static MAC table entry.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vlan_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>ID number of VLAN on which the MAC address is present.</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Specifies the VRF name.</div>
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
    # sonic# show mac dampening
    # MAC Move Dampening Threshold : 5
    # MAC Move Dampening Interval  : 5
    # sonic# show running-configuration | grep mac
    # (No mac configuration pressent)

    - name: Merge MAC configurations
      dellemc.enterprise_sonic.sonic_mac:
      config:
        - vrf_name: 'default'
          mac:
            aging_time: 50
            dampening_interval: 20
            dampening_threshold: 30
            mac_table_entries:
              - mac_address: '00:00:5e:00:53:af'
                vlan_id: 1
                interface: 'Ethernet20'
              - mac_address: '00:33:33:33:33:33'
                vlan_id: 2
                interface: 'Ethernet24'
              - mac_address: '00:00:4e:00:24:af'
                vlan_id: 3
                interface: 'Ethernet28'
      state: merged

    # After state:
    # ------------
    #
    # sonic# show mac dampening
    # MAC Move Dampening Threshold : 30
    # MAC Move Dampening Interval  : 20
    # sonic# show running-configuration | grep mac
    # mac address-table 00:00:5e:00:53:af Vlan1 Ethernet20
    # mac address-table 00:33:33:33:33:33 Vlan2 Ethernet24
    # mac address-table 00:00:4e:00:24:af Vlan3 Ethernet28
    # mac address-table aging-time 50
    #
    #
    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show mac dampening
    # MAC Move Dampening Threshold : 30
    # MAC Move Dampening Interval  : 20
    # sonic# show running-configuration | grep mac
    # mac address-table 00:00:5e:00:53:af Vlan1 Ethernet20
    # mac address-table 00:33:33:33:33:33 Vlan2 Ethernet24
    # mac address-table 00:00:4e:00:24:af Vlan3 Ethernet28
    # mac address-table aging-time 50

    - name: Replace MAC configurations
      dellemc.enterprise_sonic.sonic_mac:
      config:
        - vrf_name: 'default'
          mac:
            aging_time: 45
            dampening_interval: 30
            dampening_threshold: 60
            mac_table_entries:
              - mac_address: '00:00:5e:00:53:af'
                vlan_id: 3
                interface: 'Ethernet24'
              - mac_address: '00:44:44:44:44:44'
                vlan_id: 2
                interface: 'Ethernet20'
      state: replaced

    # sonic# show mac dampening
    # MAC Move Dampening Threshold : 60
    # MAC Move Dampening Interval  : 30
    # sonic# show running-configuration | grep mac
    # mac address-table 00:00:5e:00:53:af Vlan3 Ethernet24
    # mac address-table 00:33:33:33:33:33 Vlan2 Ethernet24
    # mac address-table 00:00:4e:00:24:af Vlan3 Ethernet28
    # mac address-table 00:44:44:44:44:44 Vlan2 Ethernet20
    # mac address-table aging-time 45
    #
    #
    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show mac dampening
    # MAC Move Dampening Threshold : 60
    # MAC Move Dampening Interval  : 30
    # sonic# show running-configuration | grep mac
    # mac address-table 00:00:5e:00:53:af Vlan3 Ethernet24
    # mac address-table 00:33:33:33:33:33 Vlan2 Ethernet24
    # mac address-table 00:00:4e:00:24:af Vlan3 Ethernet28
    # mac address-table 00:44:44:44:44:44 Vlan2 Ethernet20
    # mac address-table aging-time 45

    - name: Override MAC cofigurations
      dellemc.enterprise_sonic.sonic_mac:
      config:
        - vrf_name: 'default'
          mac:
            aging_time: 10
            dampening_interval: 20
            dampening_threshold: 30
            mac_table_entries:
              - mac_address: '00:11:11:11:11:11'
                vlan_id: 1
                interface: 'Ethernet20'
              - mac_address: '00:22:22:22:22:22'
                vlan_id: 2
                interface: 'Ethernet24'
      state: overridden

    # After state:
    # ------------
    #
    # sonic# show mac dampening
    # MAC Move Dampening Threshold : 30
    # MAC Move Dampening Interval  : 20
    # sonic# show running-configuration | grep mac
    # mac address-table 00:11:11:11:11:11 Vlan1 Ethernet20
    # mac address-table 00:22:22:22:22:22 Vlan2 Ethernet24
    # mac address-table aging-time 10
    #
    #
    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show mac dampening
    # MAC Move Dampening Threshold : 30
    # MAC Move Dampening Interval  : 20
    # sonic# show running-configuration | grep mac
    # mac address-table 00:11:11:11:11:11 Vlan1 Ethernet20
    # mac address-table 00:22:22:22:22:22 Vlan2 Ethernet24
    # mac address-table aging-time 10

    - name: Delete MAC cofigurations
      dellemc.enterprise_sonic.sonic_mac:
      config:
        - vrf_name: 'default'
          mac:
            aging_time: 10
            dampening_interval: 20
            dampening_threshold: 30
            mac_table_entries:
              - mac_address: '00:11:11:11:11:11'
                vlan_id: 1
                interface: 'Ethernet20'
              - mac_address: '00:22:22:22:22:22'
                vlan_id: 2
                interface: 'Ethernet24'
      state: deleted

    # After state:
    # ------------
    #
    # sonic# show mac dampening
    # MAC Move Dampening Threshold : 5
    # MAC Move Dampening Interval  : 5
    # sonic# show running-configuration | grep mac
    # (No mac configuration present)



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

- S\. Talabi (@stalabi1)
