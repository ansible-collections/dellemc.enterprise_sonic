.. _dellemc.enterprise_sonic.sonic_l2_interfaces_module:


********************************************
dellemc.enterprise_sonic.sonic_l2_interfaces
********************************************

**Configure interface-to-VLAN association that is based on access or trunk mode**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Manages Layer 2 interface attributes of Enterprise SONiC Distribution by Dell Technologies.




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
                        <div>A list of Layer 2 interface configurations.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>access</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configures access mode characteristics of the interface.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Configures the specified VLAN in access mode.</div>
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
                        <div>Full name of the interface, for example, &#x27;Eth1/26&#x27;.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>trunk</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configures trunking parameters on an interface.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>allowed_vlans</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies a list of allowed trunk mode VLANs and VLAN ranges for the interface.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vlan</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configures the specified trunk mode VLAN or VLAN range.</div>
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
                        <div>The state that the configuration should be left in.</div>
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
    # do show Vlan
    # Q: A - Access (Untagged), T - Tagged
    # NUM        Status      Q Ports
    # 10         Inactive    A  Eth1/3
    # 11         Inactive    T  Eth1/3
    # 12         Inactive    A  Eth1/4
    # 13         Inactive    T  Eth1/4
    # 14         Inactive    A  Eth1/5
    # 15         Inactive    T  Eth1/5
    #
    - name: Configures switch port of interfaces
      dellemc.enterprise_sonic.sonic_l2_interfaces:
        config:
          - name: Eth1/3
          - name: Eth1/4
        state: deleted
    #
    # After state:
    # ------------
    #
    # do show Vlan
    # Q: A - Access (Untagged), T - Tagged
    # NUM        Status      Q Ports
    # 10         Inactive
    # 11         Inactive
    # 12         Inactive
    # 13         Inactive
    # 14         Inactive    A  Eth1/5
    # 15         Inactive    T  Eth1/5
    #
    #
    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # do show Vlan
    # Q: A - Access (Untagged), T - Tagged
    # NUM        Status      Q Ports
    # 10         Inactive    A  Eth1/3
    # 11         Inactive    T  Eth1/3
    # 12         Inactive    A  Eth1/4
    # 13         Inactive    T  Eth1/4
    # 14         Inactive    A  Eth1/5
    # 15         Inactive    T  Eth1/5
    #
    - name: Configures switch port of interfaces
      dellemc.enterprise_sonic.sonic_l2_interfaces:
        config:
        state: deleted
    #
    # After state:
    # do show Vlan
    # Q: A - Access (Untagged), T - Tagged
    # NUM        Status      Q Ports
    # 10         Inactive
    # 11         Inactive
    # 12         Inactive
    # 13         Inactive
    # 14         Inactive
    # 15         Inactive
    #
    #
    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # do show Vlan
    # Q: A - Access (Untagged), T - Tagged
    # NUM        Status      Q Ports
    # 11         Inactive    T  Ethernet12
    # 12         Inactive    A  Ethernet12
    # 13         Inactive    T  Ethernet12
    # 14         Inactive    T  Ethernet12
    # 15         Inactive    T  Ethernet12
    # 16         Inactive    T  Ethernet12

    - name: Delete the access vlan and a range of trunk vlans for an interface
      sonic_l2_interfaces:
        config:
          - name: Ethernet12
            access:
              vlan: 12
            trunk:
              allowed_vlans:
                - vlan: 13-16
        state: deleted

    # After state:
    # ------------
    #
    # do show Vlan
    # Q: A - Access (Untagged), T - Tagged
    # NUM        Status      Q Ports
    # 11         Inactive    T  Ethernet12
    # 12         Inactive
    # 13         Inactive
    # 14         Inactive
    # 15         Inactive
    # 16         Inactive
    #
    #
    #
    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # do show Vlan
    # Q: A - Access (Untagged), T - Tagged
    # NUM        Status      Q Ports
    # 10         Inactive
    # 11         Inactive    T  Eth1/7
    # 12         Inactive    T  Eth1/7
    #
    - name: Configures an access vlan for an interface
      dellemc.enterprise_sonic.sonic_l2_interfaces:
        config:
          - name: Eth1/3
            access:
              vlan: 10
        state: merged
    #
    # After state:
    # ------------
    #
    # do show Vlan
    # Q: A - Access (Untagged), T - Tagged
    # NUM        Status      Q Ports
    # 10         Inactive    A  Eth1/3
    # 11         Inactive    T  Eth1/7
    # 12         Inactive    T  Eth1/7
    #
    #
    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # do show Vlan
    # Q: A - Access (Untagged), T - Tagged
    # NUM        Status      Q Ports
    # 10         Inactive    A  Eth1/3
    # 12         Inactive
    # 13         Inactive
    # 14         Inactive
    # 15         Inactive
    # 16         Inactive
    # 18         Inactive
    #
    - name: Modify the access vlan, add a range of trunk vlans and a single trunk vlan for an interface
      dellemc.enterprise_sonic.sonic_l2_interfaces:
        config:
          - name: Eth1/3
            access:
              vlan: 12
            trunk:
              allowed_vlans:
                - vlan: 13-16
                - vlan: 18
        state: merged
    #
    # After state:
    # ------------
    #
    # do show Vlan
    # Q: A - Access (Untagged), T - Tagged
    # NUM        Status      Q Ports
    # 10         Inactive
    # 12         Inactive    A  Eth1/3
    # 13         Inactive    T  Eth1/3
    # 14         Inactive    T  Eth1/3
    # 15         Inactive    T  Eth1/3
    # 16         Inactive    T  Eth1/3
    # 18         Inactive    T  Eth1/3
    #
    #
    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # do show Vlan
    # Q: A - Access (Untagged), T - Tagged
    # NUM        Status      Q Ports
    # 10         Inactive
    # 11         Inactive
    # 12         Inactive    A  Eth1/4
    # 13         Inactive    T  Eth1/4
    # 14         Inactive    A  Eth1/5
    # 15         Inactive    T  Eth1/5
    #
    - name: Configures switch port of interfaces
      dellemc.enterprise_sonic.sonic_l2_interfaces:
        config:
          - name: Eth1/3
            access:
              vlan: 12
            trunk:
              allowed_vlans:
                - vlan: 13
                - vlan: 14
        state: merged
    #
    # After state:
    # ------------
    #
    # do show Vlan
    # Q: A - Access (Untagged), T - Tagged
    # NUM        Status      Q Ports
    # 10         Inactive
    # 11         Inactive
    # 12         Inactive    A  Eth1/3
    #                        A  Eth1/4
    # 13         Inactive    T  Eth1/3
    #                        T  Eth1/4
    # 14         Inactive    A  Eth1/3
    #                        A  Eth1/5
    # 15         Inactive    T  Eth1/5
    #
    #
    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # do show Vlan
    # Q: A - Access (Untagged), T - Tagged
    # NUM        Status      Q Ports
    # 10         Inactive    A  Ethernet12
    #                        A  Ethernet13
    # 11         Inactive    T  Ethernet12
    #                        T  Ethernet13

    - name: Replace access vlan and trunk vlans for specified interfaces
      sonic_l2_interfaces:
        config:
          - name: Ethernet12
            access:
              vlan: 12
            trunk:
              allowed_vlans:
                - vlan: 13-14
          - name: Ethernet14
            access:
              vlan: 10
            trunk:
              allowed_vlans:
                - vlan: 11
                - vlan: 13-14
        state: replaced

    # After state:
    # ------------
    #
    # do show Vlan
    # Q: A - Access (Untagged), T - Tagged
    # NUM        Status      Q Ports
    # 10         Inactive    A  Ethernet13
    #                        A  Ethernet14
    # 11         Inactive    T  Ethernet13
    #                        T  Ethernet14
    # 12         Inactive    A  Ethernet12
    # 13         Inactive    T  Ethernet12
    #                        T  Ethernet14
    # 14         Inactive    T  Ethernet12
    #                        T  Ethernet14
    #
    #
    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # do show Vlan
    # Q: A - Access (Untagged), T - Tagged
    # NUM        Status      Q Ports
    # 10         Inactive    A  Ethernet11
    # 11         Inactive    T  Ethernet11
    # 12         Inactive    A  Ethernet12
    # 13         Inactive    T  Ethernet12

    - name: Override L2 interfaces configuration in device with provided configuration
      sonic_l2_interfaces:
        config:
          - name: Ethernet13
            access:
              vlan: 12
            trunk:
              allowed_vlans:
                - vlan: 13-14
        state: overridden

    # After state:
    # ------------
    #
    # do show Vlan
    # Q: A - Access (Untagged), T - Tagged
    # NUM        Status      Q Ports
    # 12         Inactive    A  Ethernet13
    # 13         Inactive    T  Ethernet13
    # 14         Inactive    T  Ethernet13
    #
    #



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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned is always in the same format as the parameters above.</div>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned always in the same format as the parameters above.</div>
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

- Niraimadaiselvam M(@niraimadaiselvamm)
