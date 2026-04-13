.. _dellemc.enterprise_sonic.sonic_vlans_module:


************************************
dellemc.enterprise_sonic.sonic_vlans
************************************

**Manage VLAN and its parameters**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of VLANs parameters on devices running Enterprise SONiC Distribution by Dell Technologies.




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
                        <div>A dictionary of VLAN options.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>autostate</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.1.0</div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Enable or disable autostate functionality for the VLAN interface.</div>
                        <div>Default value for this field if not configured yet will be &quot;enable&quot; which is equivalent to true.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Description about the VLAN.</div>
                </td>
            </tr>
            <tr>
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
                        <div>ID of the VLAN</div>
                        <div>Range is 1 to 4094</div>
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
                                    <li>replaced</li>
                                    <li>overridden</li>
                                    <li>deleted</li>
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

    # Using "merged" state

    # Before state:
    # -------------
    #
    # sonic# show Vlan
    # Q: A - Access (Untagged), T - Tagged
    # NUM        Status      Q Ports
    # 10         Inactive
    # 30         Inactive
    #
    # sonic#
    #


    - name: Merges given VLAN attributes with the device configuration
      dellemc.enterprise_sonic.sonic_vlans:
        config:
          - vlan_id: 10
            description: "Internal"
        state: merged

    # After state:
    # ------------
    #
    # sonic# show Vlan
    # Q: A - Access (Untagged), T - Tagged
    # NUM        Status      Q Ports
    # 10         Inactive
    # 30         Inactive
    #
    # sonic#
    #
    # sonic# show interface Vlan 10
    # Description: Internal
    # Vlan10 is up
    # Mode of IPV4 address assignment: not-set
    # Mode of IPV6 address assignment: not-set
    # IP MTU 6000 bytes
    # sonic#
    #

    # Using "replaced" state

    # Before state:
    # -------------
    #
    # sonic# show Vlan
    # Q: A - Access (Untagged), T - Tagged
    # NUM        Status      Q Ports
    # 10         Inactive
    # 30         Inactive
    #
    # sonic#

    - name: Replace all attributes of specified VLANs with provided configuration
      dellemc.enterprise_sonic.sonic_vlans:
        config:
          - vlan_id: 10
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show Vlan
    # Q: A - Access (Untagged), T - Tagged
    # NUM        Status      Q Ports
    # 10         Inactive
    # 30         Inactive
    #
    # sonic#

    # Using "overridden" state

    # Before state:
    # -------------
    #
    # sonic# show Vlan
    # Q: A - Access (Untagged), T - Tagged
    # NUM        Status      Q Ports
    # 10         Inactive
    # 30         Inactive
    #
    # sonic#

    - name: Override device configuration of all VLANs with provided configuration
      dellemc.enterprise_sonic.sonic_vlans:
        config:
          - vlan_id: 10
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show Vlan
    # Q: A - Access (Untagged), T - Tagged
    # NUM        Status      Q Ports
    # 10         Inactive
    #
    # sonic#

    # Using "deleted" state

    # Before state:
    # -------------
    #
    # sonic# show interface Vlan 70
    # Description: Internal
    # Vlan70 is up
    # Mode of IPV4 address assignment: not-set
    # Mode of IPV6 address assignment: not-set
    # IP MTU 6000 bytes

    - name: Deletes attributes of the given VLANs
      dellemc.enterprise_sonic.sonic_vlans:
        config:
          - vlan_id: 70
            description: "Internal"
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show interface Vlan 70
    # Vlan70 is up
    # Mode of IPV4 address assignment: not-set
    # Mode of IPV6 address assignment: not-set
    # IP MTU 6000 bytes

    # Before state:
    # -------------
    #
    # sonic# show Vlan
    # Q: A - Access (Untagged), T - Tagged
    # NUM        Status      Q Ports
    # 10         Inactive
    # 20         Inactive
    #
    # sonic#

    - name: Deletes attributes of the given VLANs
      dellemc.enterprise_sonic.sonic_vlans:
        config:
          - vlan_id: 20
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show Vlan
    # Q: A - Access (Untagged), T - Tagged
    # NUM        Status      Q Ports
    # 10         Inactive
    #
    # sonic#


    # Using "deleted" state

    # Before state:
    # -------------
    #
    # sonic# show Vlan
    # Q: A - Access (Untagged), T - Tagged
    # NUM        Status      Q Ports
    # 10         Inactive
    # 20         Inactive
    # 30         Inactive
    #
    # sonic#

    - name: Deletes all the VLANs on the switch
      dellemc.enterprise_sonic.sonic_vlans:
        config:
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show Vlan
    # Q: A - Access (Untagged), T - Tagged
    # NUM        Status      Q Ports
    #
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration that is returned is always in the same format as the parameters above.</div>
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

- Mohamed Javeed (@javeedf)
