.. _dellemc.enterprise_sonic.sonic_port_breakout_module:


********************************************
dellemc.enterprise_sonic.sonic_port_breakout
********************************************

**Configure port breakout settings on physical interfaces**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of port breakout parameters on devices running Enterprise SONiC.




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
                        <div>Specifies the port breakout related configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mode</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>1x10G</li>
                                    <li>1x25G</li>
                                    <li>1x40G</li>
                                    <li>1x50G</li>
                                    <li>1x100G</li>
                                    <li>1x200G</li>
                                    <li>1x400G</li>
                                    <li>1x800G</li>
                                    <li>2x10G</li>
                                    <li>2x25G</li>
                                    <li>2x40G</li>
                                    <li>2x50G</li>
                                    <li>2x100G</li>
                                    <li>2x200G</li>
                                    <li>2x400G</li>
                                    <li>4x10G</li>
                                    <li>4x25G</li>
                                    <li>4x50G</li>
                                    <li>4x100G</li>
                                    <li>4x200G</li>
                                    <li>8x10G</li>
                                    <li>8x25G</li>
                                    <li>8x50G</li>
                                    <li>8x100G</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the mode of the port breakout.</div>
                </td>
            </tr>
            <tr>
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
                        <div>Specifies the name of the port breakout.</div>
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
                        <div>Specifies the operation to be performed on the port breakout configured on the device.</div>
                        <div>In case of merged, the input mode configuration will be merged with the existing port breakout configuration on the device.</div>
                        <div>In case of deleted, the existing port breakout mode configuration will be removed from the device.</div>
                        <div>In case of replaced, on-device port breakout configuration of the specified interfaces is replaced with provided configuration.</div>
                        <div>In case of overridden, all on-device port breakout configurations are overridden with the provided configuration.</div>
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
    # sonic# show interface breakout
    # -----------------------------------------------
    # Port  Breakout Mode  Status        Interfaces
    # -----------------------------------------------
    # 1/1   4x10G          Completed     Eth1/1/1
    #                                    Eth1/1/2
    #                                    Eth1/1/3
    #                                    Eth1/1/4
    # 1/11  1x100G         Completed     Eth1/11/1
    #

    - name: Delete interface port breakout configuration
      dellemc.enterprise_sonic.sonic_port_breakout:
        config:
          - name: 1/11
            mode: 1x100G
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show interface breakout
    # -----------------------------------------------
    # Port  Breakout Mode  Status        Interfaces
    # -----------------------------------------------
    # 1/1   4x10G          Completed     Eth1/1/1
    #                                    Eth1/1/2
    #                                    Eth1/1/3
    #                                    Eth1/1/4
    # 1/11  Default        Completed     Eth1/11
    #


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show interface breakout
    # -----------------------------------------------
    # Port  Breakout Mode  Status        Interfaces
    # -----------------------------------------------
    # 1/1   4x10G          Completed     Eth1/1/1
    #                                    Eth1/1/2
    #                                    Eth1/1/3
    #                                    Eth1/1/4
    # 1/11  1x100G         Completed     Eth1/11/1
    #

    - name: Delete all port breakout configurations
      dellemc.enterprise_sonic.sonic_port_breakout:
        config:
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show interface breakout
    # -----------------------------------------------
    # Port  Breakout Mode  Status        Interfaces
    # -----------------------------------------------
    # 1/1   Default        Completed     Eth1/1
    # 1/11  Default        Completed     Eth1/11


    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show interface breakout
    # -----------------------------------------------
    # Port  Breakout Mode  Status        Interfaces
    # -----------------------------------------------
    # 1/1   4x10G          Completed     Eth1/1/1
    #                                    Eth1/1/2
    #                                    Eth1/1/3
    #                                    Eth1/1/4
    #

    - name: Merge port breakout configurations
      dellemc.enterprise_sonic.sonic_port_breakout:
        config:
          - name: 1/11
            mode: 1x100G
        state: merged

    # After state:
    # ------------
    #
    # sonic# show interface breakout
    # -----------------------------------------------
    # Port  Breakout Mode  Status        Interfaces
    # -----------------------------------------------
    # 1/1   4x10G          Completed     Eth1/1/1
    #                                    Eth1/1/2
    #                                    Eth1/1/3
    #                                    Eth1/1/4
    # 1/11  1x100G         Completed     Eth1/11/1


    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show interface breakout
    # -----------------------------------------------
    # Port  Breakout Mode  Status        Interfaces
    # -----------------------------------------------
    # 1/49   4x25G         Completed     Eth1/49/1
    #                                    Eth1/49/2
    #                                    Eth1/49/3
    #                                    Eth1/49/4
    #

    - name: Replace port breakout configurations
      dellemc.enterprise_sonic.sonic_port_breakout:
        config:
          - name: 1/49
            mode: 4x10G
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show interface breakout
    # -----------------------------------------------
    # Port  Breakout Mode  Status        Interfaces
    # -----------------------------------------------
    # 1/49   4x10G         Completed     Eth1/49/1
    #                                    Eth1/49/2
    #                                    Eth1/49/3
    #                                    Eth1/49/4


    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show interface breakout
    # ----------------------------------------------
    # Port  Breakout Mode  Status        Interfaces
    # -----------------------------------------------
    # 1/49  4x10G          Completed     Eth1/49/1
    #                                    Eth1/49/2
    #                                    Eth1/49/3
    #                                    Eth1/49/4
    # 1/50  2x50G          Completed     Eth1/50/1
    #                                    Eth1/50/2
    # 1/51  1x100G         Completed     Eth1/51/1
    #

    - name: Override port breakout configurations
      dellemc.enterprise_sonic.sonic_port_breakout:
        config:
          - name: 1/52
            mode: 4x10G
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show interface breakout
    # -----------------------------------------------
    # Port  Breakout Mode  Status        Interfaces
    # -----------------------------------------------
    # 1/49  Default        Completed     Eth1/49
    # 1/50  Default        Completed     Eth1/50
    # 1/51  Default        Completed     Eth1/51
    # 1/52  4x10G          Completed     Eth1/52/1
    #                                    Eth1/52/2
    #                                    Eth1/52/3
    #                                    Eth1/52/4



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

- Niraimadaiselvam M (@niraimadaiselvamm)
