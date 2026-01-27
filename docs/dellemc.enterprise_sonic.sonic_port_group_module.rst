.. _dellemc.enterprise_sonic.sonic_port_group_module:


*****************************************
dellemc.enterprise_sonic.sonic_port_group
*****************************************

**Manages port group configuration on SONiC.**


Version added: 2.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of port group for devices running SONiC.




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
                        <div>A list of port group configurations.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The index of the port group.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>speed</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>SPEED_10MB</li>
                                    <li>SPEED_100MB</li>
                                    <li>SPEED_1GB</li>
                                    <li>SPEED_2500MB</li>
                                    <li>SPEED_5GB</li>
                                    <li>SPEED_10GB</li>
                                    <li>SPEED_20GB</li>
                                    <li>SPEED_25GB</li>
                                    <li>SPEED_40GB</li>
                                    <li>SPEED_50GB</li>
                                    <li>SPEED_100GB</li>
                                    <li>SPEED_200GB</li>
                                    <li>SPEED_400GB</li>
                        </ul>
                </td>
                <td>
                        <div>Speed for the port group.</div>
                        <div>This configures the speed for all the memebr ports of the prot group.</div>
                        <div>Supported speeds are dependent on the type of switch.</div>
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
                        <div>The state of the configuration after module completion.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - Supports ``check_mode``.



Examples
--------

.. code-block:: yaml

    #
    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show port-group
    # -------------------------------------------------------------------------------------
    # Port-group  Interface range            Valid speeds      Default Speed Current Speed
    # -------------------------------------------------------------------------------------
    # 1           Ethernet0 - Ethernet3      10G, 25G          25G           10G
    # 2           Ethernet4 - Ethernet7      10G, 25G          25G           25G
    # 3           Ethernet8 - Ethernet11     10G, 25G          25G           25G
    # 4           Ethernet12 - Ethernet15    10G, 25G          25G           25G
    # 5           Ethernet16 - Ethernet19    10G, 25G          25G           25G
    # 6           Ethernet20 - Ethernet23    10G, 25G          25G           25G
    # 7           Ethernet24 - Ethernet27    10G, 25G          25G           25G
    # 8           Ethernet28 - Ethernet31    10G, 25G          25G           25G
    # 9           Ethernet32 - Ethernet35    10G, 25G          25G           10G
    # 10          Ethernet36 - Ethernet39    10G, 25G          25G           25G
    #
    - name: Configure port group speed
      sonic_port_group:
        config:
          - id: 1
          - id: 10
        state: deleted
    #
    #
    # After state:
    # ------------
    #
    # sonic# show port-group
    # -------------------------------------------------------------------------------------
    # Port-group  Interface range            Valid speeds      Default Speed Current Speed
    # -------------------------------------------------------------------------------------
    # 1           Ethernet0 - Ethernet3      10G, 25G          25G           25G
    # 2           Ethernet4 - Ethernet7      10G, 25G          25G           25G
    # 3           Ethernet8 - Ethernet11     10G, 25G          25G           25G
    # 4           Ethernet12 - Ethernet15    10G, 25G          25G           25G
    # 5           Ethernet16 - Ethernet19    10G, 25G          25G           25G
    # 6           Ethernet20 - Ethernet23    10G, 25G          25G           25G
    # 7           Ethernet24 - Ethernet27    10G, 25G          25G           25G
    # 8           Ethernet28 - Ethernet31    10G, 25G          25G           25G
    # 9           Ethernet32 - Ethernet35    10G, 25G          25G           10G
    # 10          Ethernet36 - Ethernet39    10G, 25G          25G           25G
    #
    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show port-group
    # -------------------------------------------------------------------------------------
    # Port-group  Interface range            Valid speeds      Default Speed Current Speed
    # -------------------------------------------------------------------------------------
    # 1           Ethernet0 - Ethernet3      10G, 25G          25G           10G
    # 2           Ethernet4 - Ethernet7      10G, 25G          25G           25G
    # 3           Ethernet8 - Ethernet11     10G, 25G          25G           25G
    # 4           Ethernet12 - Ethernet15    10G, 25G          25G           25G
    # 5           Ethernet16 - Ethernet19    10G, 25G          25G           25G
    # 6           Ethernet20 - Ethernet23    10G, 25G          25G           25G
    # 7           Ethernet24 - Ethernet27    10G, 25G          25G           25G
    # 8           Ethernet28 - Ethernet31    10G, 25G          25G           25G
    # 9           Ethernet32 - Ethernet35    10G, 25G          25G           10G
    # 10          Ethernet36 - Ethernet39    10G, 25G          25G           25G
    #
    - name: Configure port group speed
      sonic_port_group:
        config:
          - id:
        state: deleted
    #
    #
    # After state:
    # ------------
    #
    # sonic# show port-group
    # -------------------------------------------------------------------------------------
    # Port-group  Interface range            Valid speeds      Default Speed Current Speed
    # -------------------------------------------------------------------------------------
    # 1           Ethernet0 - Ethernet3      10G, 25G          25G           25G
    # 2           Ethernet4 - Ethernet7      10G, 25G          25G           25G
    # 3           Ethernet8 - Ethernet11     10G, 25G          25G           25G
    # 4           Ethernet12 - Ethernet15    10G, 25G          25G           25G
    # 5           Ethernet16 - Ethernet19    10G, 25G          25G           25G
    # 6           Ethernet20 - Ethernet23    10G, 25G          25G           25G
    # 7           Ethernet24 - Ethernet27    10G, 25G          25G           25G
    # 8           Ethernet28 - Ethernet31    10G, 25G          25G           25G
    # 9           Ethernet32 - Ethernet35    10G, 25G          25G           25G
    # 10          Ethernet36 - Ethernet39    10G, 25G          25G           25G
    #
    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show port-group
    # -------------------------------------------------------------------------------------
    # Port-group  Interface range            Valid speeds      Default Speed Current Speed
    # -------------------------------------------------------------------------------------
    # 1           Ethernet0 - Ethernet3      10G, 25G          25G           25G
    # 2           Ethernet4 - Ethernet7      10G, 25G          25G           25G
    # 3           Ethernet8 - Ethernet11     10G, 25G          25G           25G
    # 4           Ethernet12 - Ethernet15    10G, 25G          25G           25G
    # 5           Ethernet16 - Ethernet19    10G, 25G          25G           25G
    # 6           Ethernet20 - Ethernet23    10G, 25G          25G           25G
    # 7           Ethernet24 - Ethernet27    10G, 25G          25G           25G
    # 8           Ethernet28 - Ethernet31    10G, 25G          25G           25G
    # 9           Ethernet32 - Ethernet35    10G, 25G          25G           25G
    # 10          Ethernet36 - Ethernet39    10G, 25G          25G           25G
    #
    - name: Configure port group speed
      sonic_port_group:
        config:
          - id: 1
            speed: SPEED_10GB
          - id: 9
            speed: SPEED_10GB
        state: merged
    #
    #
    # After state:
    # ------------
    #
    # sonic# show port-group
    # -------------------------------------------------------------------------------------
    # Port-group  Interface range            Valid speeds      Default Speed Current Speed
    # -------------------------------------------------------------------------------------
    # 1           Ethernet0 - Ethernet3      10G, 25G          25G           10G
    # 2           Ethernet4 - Ethernet7      10G, 25G          25G           25G
    # 3           Ethernet8 - Ethernet11     10G, 25G          25G           25G
    # 4           Ethernet12 - Ethernet15    10G, 25G          25G           25G
    # 5           Ethernet16 - Ethernet19    10G, 25G          25G           25G
    # 6           Ethernet20 - Ethernet23    10G, 25G          25G           25G
    # 7           Ethernet24 - Ethernet27    10G, 25G          25G           25G
    # 8           Ethernet28 - Ethernet31    10G, 25G          25G           25G
    # 9           Ethernet32 - Ethernet35    10G, 25G          25G           10G
    # 10          Ethernet36 - Ethernet39    10G, 25G          25G           25G
    #
    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show port-group
    # -------------------------------------------------------------------------------------
    # Port-group  Interface range            Valid speeds      Default Speed Current Speed
    # -------------------------------------------------------------------------------------
    # 1           Ethernet0 - Ethernet3      10G, 25G          25G           25G
    # 2           Ethernet4 - Ethernet7      10G, 25G          25G           25G
    # 3           Ethernet8 - Ethernet11     10G, 25G          25G           25G
    # 4           Ethernet12 - Ethernet15    10G, 25G          25G           10G
    # 5           Ethernet16 - Ethernet19    10G, 25G          25G           25G
    # 6           Ethernet20 - Ethernet23    10G, 25G          25G           25G
    # 7           Ethernet24 - Ethernet27    10G, 25G          25G           25G
    # 8           Ethernet28 - Ethernet31    10G, 25G          25G           25G
    # 9           Ethernet32 - Ethernet35    10G, 25G          25G           25G
    # 10          Ethernet36 - Ethernet39    10G, 25G          25G           25G
    #
    - name: Replace port group speed
      sonic_port_group:
        config:
          - id: 1
            speed: SPEED_10GB
          - id: 9
            speed: SPEED_10GB
        state: replaced
    #
    # After state:
    # ------------
    #
    # sonic# show port-group
    # -------------------------------------------------------------------------------------
    # Port-group  Interface range            Valid speeds      Default Speed Current Speed
    # -------------------------------------------------------------------------------------
    # 1           Ethernet0 - Ethernet3      10G, 25G          25G           10G
    # 2           Ethernet4 - Ethernet7      10G, 25G          25G           25G
    # 3           Ethernet8 - Ethernet11     10G, 25G          25G           25G
    # 4           Ethernet12 - Ethernet15    10G, 25G          25G           10G
    # 5           Ethernet16 - Ethernet19    10G, 25G          25G           25G
    # 6           Ethernet20 - Ethernet23    10G, 25G          25G           25G
    # 7           Ethernet24 - Ethernet27    10G, 25G          25G           25G
    # 8           Ethernet28 - Ethernet31    10G, 25G          25G           25G
    # 9           Ethernet32 - Ethernet35    10G, 25G          25G           10G
    # 10          Ethernet36 - Ethernet39    10G, 25G          25G           25G
    #
    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show port-group
    # -------------------------------------------------------------------------------------
    # Port-group  Interface range            Valid speeds      Default Speed Current Speed
    # -------------------------------------------------------------------------------------
    # 1           Ethernet0 - Ethernet3      10G, 25G          25G           25G
    # 2           Ethernet4 - Ethernet7      10G, 25G          25G           10G
    # 3           Ethernet8 - Ethernet11     10G, 25G          25G           10G
    # 4           Ethernet12 - Ethernet15    10G, 25G          25G           25G
    # 5           Ethernet16 - Ethernet19    10G, 25G          25G           10G
    # 6           Ethernet20 - Ethernet23    10G, 25G          25G           25G
    # 7           Ethernet24 - Ethernet27    10G, 25G          25G           10G
    # 8           Ethernet28 - Ethernet31    10G, 25G          25G           10G
    # 9           Ethernet32 - Ethernet35    10G, 25G          25G           10G
    # 10          Ethernet36 - Ethernet39    10G, 25G          25G           10G
    #
    - name: Override port group speed
      sonic_port_group:
        config:
          - id: 1
            speed: SPEED_10GB
          - id: 9
            speed: SPEED_10GB
        state: overridden
    #
    # After state:
    # ------------
    #
    # sonic# show port-group
    # -------------------------------------------------------------------------------------
    # Port-group  Interface range            Valid speeds      Default Speed Current Speed
    # -------------------------------------------------------------------------------------
    # 1           Ethernet0 - Ethernet3      10G, 25G          25G           10G
    # 2           Ethernet4 - Ethernet7      10G, 25G          25G           25G
    # 3           Ethernet8 - Ethernet11     10G, 25G          25G           25G
    # 4           Ethernet12 - Ethernet15    10G, 25G          25G           25G
    # 5           Ethernet16 - Ethernet19    10G, 25G          25G           25G
    # 6           Ethernet20 - Ethernet23    10G, 25G          25G           25G
    # 7           Ethernet24 - Ethernet27    10G, 25G          25G           25G
    # 8           Ethernet28 - Ethernet31    10G, 25G          25G           25G
    # 9           Ethernet32 - Ethernet35    10G, 25G          25G           10G
    # 10          Ethernet36 - Ethernet39    10G, 25G          25G           25G
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

- M. Zhang (@mingjunzhang2019)
