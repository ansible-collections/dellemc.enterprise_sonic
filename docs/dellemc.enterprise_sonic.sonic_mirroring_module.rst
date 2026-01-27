.. _dellemc.enterprise_sonic.sonic_mirroring_module:


****************************************
dellemc.enterprise_sonic.sonic_mirroring
****************************************

**Manage port mirroring configuration on SONiC.**


Version added: 3.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management for port mirroring on devices running SONiC.




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
                        <div>Specifies port mirroring configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>erspan</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>ERSPAN mirroring sessions.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>direction</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>rx</li>
                                    <li>tx</li>
                                    <li>both</li>
                        </ul>
                </td>
                <td>
                        <div>Mirror session direction.</div>
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
                        <div>ERSPAN destination DSCP.</div>
                        <div>The range of values is from 0 to 63.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dst_ip</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>ERSPAN destination IP address.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>gre</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>ERSPAN destination GRE type.</div>
                        <div>A hexadecimal string of the form 0xabcd.</div>
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
                        <div>ERSPAN mirroring session name.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>queue</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>ERSPAN destination queue number.</div>
                        <div>The range of values is from 0 to 63.</div>
                        <div>Only queue 0 is supported.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>source</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Mirror session source interface.</div>
                        <div>It may be an Ethernet interface or a PortChannel interface.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>src_ip</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>ERSPAN source IP address.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ttl</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>ERSPAN destination TTL</div>
                        <div>The range of values is from 0 to 63.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>span</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>SPAN mirroring sessions.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>direction</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>rx</li>
                                    <li>tx</li>
                                    <li>both</li>
                        </ul>
                </td>
                <td>
                        <div>Mirror session direction.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dst_port</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Mirror session destination interface.</div>
                        <div>It may be CPU or an Ethernet interface.</div>
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
                        <div>SPAN mirroring session name.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>source</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Mirror session source interface.</div>
                        <div>It may be an Ethernet interface or a PortChannel interface.</div>
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
                        <div>Specifies the operation to be performed on the mirroring configured on the device.</div>
                        <div>In case of merged, the input configuration will be merged with the existing configuration on the device.</div>
                        <div>In case of deleted, the input configuration will be removed from the device.</div>
                        <div>In case of overridden, all existing mirroring configuration will be deleted and the specified input configuration will be added.</div>
                        <div>In case of replaced, the existing mirroring configuration on the device will be replaced by the new specified configuration for each affected mirroring session.</div>
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
    # sonic# show mirror-session
    # ERSPAN Sessions
    # -----------------------------------------------------------------------------------------------------------------------------------------
    # Name                     Status     SRC-IP           DST-IP           GRE    DSCP   TTL    Queue    Policer    SRC-Port         Direction
    # -----------------------------------------------------------------------------------------------------------------------------------------
    # dell-2                   inactive   200.22.22.22     100.11.11.11                          0                   Ethernet28       both
    # SPAN Sessions
    # -------------------------------------------------------------------------------
    # Name                     Status     DST-Port         SRC-Port         Direction
    # -------------------------------------------------------------------------------
    # dell-1                   active     CPU              Ethernet24       both
    # dell-3                   active     CPU

    - name: Delete mirroring configuration
      dellemc.enterprise_sonic.sonic_mirroring:
        config:
          span:
            - name: dell-3
          erspan:
            - name: dell-2
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show mirror-session
    # SPAN Sessions
    # -------------------------------------------------------------------------------
    # Name                     Status     DST-Port         SRC-Port         Direction
    # -------------------------------------------------------------------------------
    # dell-1                   active     CPU              Ethernet24       both


    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show mirror-session
    # No sessions configured

    - name: Merge mirroring configuration
      dellemc.enterprise_sonic.sonic_mirroring:
        config:
          span:
            - name: dell-1
              dst_port: CPU
              source: Ethernet24
              direction: both
          erspan:
            - name: dell-2
              dst_ip: 100.11.11.11
              src_ip: 200.22.22.22
              source: Ethernet28
              direction: both
              queue: 0
        state: merged

    # After state:
    # ------------
    #
    # sonic# show mirror-session
    # ERSPAN Sessions
    # -----------------------------------------------------------------------------------------------------------------------------------------
    # Name                     Status     SRC-IP           DST-IP           GRE    DSCP   TTL    Queue    Policer    SRC-Port         Direction
    # -----------------------------------------------------------------------------------------------------------------------------------------
    # dell-2                   inactive   200.22.22.22     100.11.11.11                          0                   Ethernet28       both
    # SPAN Sessions
    # -------------------------------------------------------------------------------
    # Name                     Status     DST-Port         SRC-Port         Direction
    # -------------------------------------------------------------------------------
    # dell-1                   active     CPU              Ethernet24       both


    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show mirror-session
    # SPAN Sessions
    # -------------------------------------------------------------------------------
    # Name                     Status     DST-Port         SRC-Port         Direction
    # -------------------------------------------------------------------------------
    # dell-1                   active     CPU              Ethernet24       both

    - name: Modify existing mirroring configuration
      dellemc.enterprise_sonic.sonic_mirroring:
        config:
          span:
            - name: dell-1
              dst_port: Ethernet32
              source: Ethernet4
              direction: rx

    # After state:
    # ------------
    #
    # sonic# show mirror-session
    # SPAN Sessions
    # -------------------------------------------------------------------------------
    # Name                     Status     DST-Port         SRC-Port         Direction
    # -------------------------------------------------------------------------------
    # dell-1                   active     Ethernet32       Ethernet4        rx


    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show mirror-session
    # ERSPAN Sessions
    # -----------------------------------------------------------------------------------------------------------------------------------------
    # Name                     Status     SRC-IP           DST-IP           GRE    DSCP   TTL    Queue    Policer    SRC-Port         Direction
    # -----------------------------------------------------------------------------------------------------------------------------------------
    # dell-2                   inactive   200.22.22.22     100.11.11.11                          0                   Ethernet28       both
    # SPAN Sessions
    # -------------------------------------------------------------------------------
    # Name                     Status     DST-Port         SRC-Port         Direction
    # -------------------------------------------------------------------------------
    # dell-1                   active     CPU              Ethernet24       both
    # dell-3                   active     CPU

    - name: Replace mirroring configuration
      dellemc.enterprise_sonic.sonic_mirroring:
        config:
          erspan:
            - name: dell-2
              dst_ip: 32.22.22.12
              src_ip: 31.21.21.12
              source: Ethernet28
              dscp: 6
              gre: "0x6689"
              ttl: 9
              queue: 0
              direction: rx
            - name: dell-3
              dst_ip: 22.22.22.12
              src_ip: 21.21.21.12
              source: Ethernet28
              direction: rx
          span:
            - name: dell-1
              dst_port: Ethernet4
              source: Ethernet24
              direction: tx
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show mirror-session
    # ERSPAN Sessions
    # -----------------------------------------------------------------------------------------------------------------------------------------
    # Name                     Status     SRC-IP           DST-IP           GRE    DSCP   TTL    Queue    Policer    SRC-Port         Direction
    # -----------------------------------------------------------------------------------------------------------------------------------------
    # dell-2                   inactive   32.22.22.22      31.11.11.11      0x6689 6      9      0                   Ethernet28       rx
    # dell-3                   inactive   21.21.21.12      22.22.22.12                                               Ethernet28       rx
    # SPAN Sessions
    # -------------------------------------------------------------------------------
    # Name                     Status     DST-Port         SRC-Port         Direction
    # -------------------------------------------------------------------------------
    # dell-1                   active     Ethertnet4       Ethernet24       tx


    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show mirror-session
    # ERSPAN Sessions
    # -----------------------------------------------------------------------------------------------------------------------------------------
    # Name                     Status     SRC-IP           DST-IP           GRE    DSCP   TTL    Queue    Policer    SRC-Port         Direction
    # -----------------------------------------------------------------------------------------------------------------------------------------
    # dell-2                   inactive   200.22.22.22     100.11.11.11                          0                   Ethernet28       both
    # SPAN Sessions
    # -------------------------------------------------------------------------------
    # Name                     Status     DST-Port         SRC-Port         Direction
    # -------------------------------------------------------------------------------
    # dell-1                   active     CPU              Ethernet24       both
    # dell-3                   active     CPU

    - name: Override mirroring configuration
      dellemc.enterprise_sonic.sonic_mirroring:
        config:
          erspan:
            - name: dell-2
              dst_ip: 32.22.22.12
              src_ip: 31.21.21.12
              source: Ethernet28
              gre: "0x6689"
              dscp: 6
              ttl: 9
              queue: 0
              direction: rx
            - name: dell-1
              dst_ip: 22.22.22.12
              src_ip: 21.21.21.12
              source: Ethernet28
              direction: rx
          span:
            - name: dell-6
              dst_port: CPU
              source: Ethernet24
              direction: tx
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show mirror-session
    # ERSPAN Sessions
    # -----------------------------------------------------------------------------------------------------------------------------------------
    # Name                     Status     SRC-IP           DST-IP           GRE    DSCP   TTL    Queue    Policer    SRC-Port         Direction
    # -----------------------------------------------------------------------------------------------------------------------------------------
    # dell-1                   inactive   21.21.21.12      22.22.22.12                                               Ethernet28       rx
    # dell-2                   inactive   31.21.21.12      32.22.22.12      0x6689 6      9      0                   Ethernet28       rx
    # SPAN Sessions
    # -------------------------------------------------------------------------------
    # Name                     Status     DST-Port         SRC-Port         Direction
    # -------------------------------------------------------------------------------
    # dell-6                   active     Ethertnet4       Ethernet24       tx



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
                      <span style="color: purple">dictionary</span>
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
                      <span style="color: purple">dictionary</span>
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
                      <span style="color: purple">dictionary</span>
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

- M. Zhang (@mingjunzhang2019)
