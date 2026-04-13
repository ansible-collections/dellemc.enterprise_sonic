.. _dellemc.enterprise_sonic.sonic_vrfs_module:


***********************************
dellemc.enterprise_sonic.sonic_vrfs
***********************************

**Manage VRFs and associate VRFs to interfaces such as, Eth, LAG, VLAN, and loopback**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Manages VRF and VRF interface attributes in Enterprise SONiC Distribution by Dell Technologies.




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
                        <div>A list of VRF configurations.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>members</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Holds a dictionary mapping of list of interfaces linked to a VRF interface.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>List of interface names that are linked to a specific VRF interface.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The name of the physical interface.</div>
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
                        <div>The name of the VRF interface.</div>
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
                                    <li>replaced</li>
                                    <li>overridden</li>
                                    <li>deleted</li>
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
   - This module does not support the deletion of mgmt VRF. Deletion of mgmt VRF can be done using the "sonic_config" resource module as shown in "playbooks/common_examples/mgmt_vrf_off.yaml". It can also be done using the SONiC CLI or by using a standalone REST API.



Examples
--------

.. code-block:: yaml

    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # show ip vrf
    # VRF-NAME            INTERFACES
    # ----------------------------------------------------------------
    # Vrfcheck1
    # Vrfcheck2
    # Vrfcheck3           Eth1/3
    #                    Eth1/14
    #                    Eth1/16
    #                    Eth1/17
    # Vrfcheck4           Eth1/5
    #                    Eth1/6
    #
    - name: Configuring vrf deleted state
      dellemc.enterprise_sonic.sonic_vrfs:
        config:
          - name: Vrfcheck4
            members:
              interfaces:
                - name: Eth1/6
          - name: Vrfcheck3
            members:
              interfaces:
                - name: Eth1/3
                - name: Eth1/14
        state: deleted
    #
    # After state:
    # ------------
    #
    # show ip vrf
    # VRF-NAME            INTERFACES
    # ----------------------------------------------------------------
    # Vrfcheck1
    # Vrfcheck2
    # Vrfcheck3           Eth1/16
    #                    Eth1/17
    # Vrfcheck4           Eth1/5
    #
    #
    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # show ip vrf
    # VRF-NAME            INTERFACES
    # ----------------------------------------------------------------
    # Vrfcheck1
    # Vrfcheck2
    # Vrfcheck3           Eth1/16
    #                    Eth1/17
    # Vrfcheck4
    #
    - name: Configuring vrf merged state
      dellemc.enterprise_sonic.sonic_vrfs:
        config:
          - name: Vrfcheck4
            members:
              interfaces:
                - name: Eth1/5
                - name: Eth1/6
          - name: Vrfcheck3
            members:
              interfaces:
                - name: Eth1/3
                - name: Eth1/14
        state: merged
    #
    # After state:
    # ------------
    #
    # show ip vrf
    # VRF-NAME            INTERFACES
    # ----------------------------------------------------------------
    # Vrfcheck1
    # Vrfcheck2
    # Vrfcheck3           Eth1/3
    #                    Eth1/14
    #                    Eth1/16
    #                    Eth1/17
    # Vrfcheck4           Eth1/5
    #                    Eth1/6
    #
    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # show ip vrf
    # VRF-NAME            INTERFACES
    # ----------------------------------------------------------------
    # Vrfcheck1
    # Vrfcheck2
    # Vrfcheck3           Eth1/7
    #                    Eth1/8
    #
    - name: Overridden VRF configuration
      dellemc.enterprise_sonic.sonic_vrfs:
      sonic_vrfs:
        config:
          - name: Vrfcheck1
            members:
              interfaces:
                - name: Eth1/3
                - name: Eth1/14
          - name: Vrfcheck3
            members:
              interfaces:
                - name: Eth1/5
                - name: Eth1/6
        state: overridden
    #
    # After state:
    # ------------
    #
    # show ip vrf
    # VRF-NAME            INTERFACES
    # ----------------------------------------------------------------
    # Vrfcheck1           Eth1/3
    #                    Eth1/14
    # Vrfcheck2
    # Vrfcheck3           Eth1/5
    #                    Eth1/6
    #
    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # show ip vrf
    # VRF-NAME            INTERFACES
    # ----------------------------------------------------------------
    # Vrfcheck1           Eth1/3
    # Vrfcheck2
    # Vrfcheck3           Eth1/5
    #                    Eth1/6
    #
    - name: Replace VRF configuration
      dellemc.enterprise_sonic.sonic_vrfs:
      sonic_vrfs:
        config:
          - name: Vrfcheck1
            members:
              interfaces:
                - name: Eth1/3
                - name: Eth1/14
          - name: Vrfcheck3
            members:
              interfaces:
                - name: Eth1/5
                - name: Eth1/6
        state: replaced
    #
    # After state:
    # ------------
    #
    # show ip vrf
    # VRF-NAME            INTERFACES
    # ----------------------------------------------------------------
    # Vrfcheck1           Eth1/3
    #                     Eth1/14
    # Vrfcheck2
    # Vrfcheck3           Eth1/5
    #                    Eth1/6
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned is always in the same format as the parameters above.</div>
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

- Abirami N (@abirami-n)
