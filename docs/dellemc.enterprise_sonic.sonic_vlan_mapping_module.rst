.. _dellemc.enterprise_sonic.sonic_vlan_mapping_module:


*******************************************
dellemc.enterprise_sonic.sonic_vlan_mapping
*******************************************

**Configure vlan mappings on SONiC.**


Version added: 2.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management for vlan mappings on devices running SONiC.
- Vlan mappings only available on TD3 and TD4 devices.
- For TD4 devices must enable vlan mapping first (can enable in config-switch-resource).




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="5">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="5">
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
                        <div>Specifies the vlan mapping related configurations.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mapping</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Define vlan mappings.</div>
                        <div>dot1q_tunnel and vlan_translation are mutually exclusive.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dot1q_tunnel</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify a vlan stacking.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>priority</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set priority level of the vlan stacking.</div>
                        <div>Priority range is 0-7.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Configure customer VLAN IDs.</div>
                        <div>It can pass ranges and/or multiple list entries.</div>
                        <div>Individual VLAN ID or (-) separated range of VLAN IDs.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>service_vlan</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure service provider VLAN ID.</div>
                        <div>VLAN ID range is 1-4094.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vlan_translation</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.0.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify a vlan translation.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>match_double_tags</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure double tagged vlan translation.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>inner_vlan</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure inner customer VLAN ID.</div>
                        <div>VLAN ID range is 1-4094.</div>
                        <div>Only available for double tagged translations.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>outer_vlan</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure outer customer VLAN ID.</div>
                        <div>VLAN ID range is 1-4094.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>priority</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set priority level of the vlan translation.</div>
                        <div>Priority range is 0-7.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>match_single_tags</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure single tagged vlan translation.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>outer_vlan</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure outer customer VLAN ID.</div>
                        <div>VLAN ID range is 1-4094.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>priority</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set priority level of the vlan translation.</div>
                        <div>Priority range is 0-7.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>multi_tag</b>
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
                        <div>Indicate if there are multiple tags.</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
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
                        <div>Full name of the interface, i.e. Ethernet8, PortChannel2, Eth1/2.</div>
                </td>
            </tr>

            <tr>
                <td colspan="5">
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
                        <div>Specifies the operation to be performed on the vlan mappings configured on the device.</div>
                        <div>In case of merged, the input configuration will be merged with the existing vlan mappings on the device.</div>
                        <div>In case of deleted, the existing vlan mapping configuration will be removed from the device.</div>
                        <div>In case of overridden, all existing vlan mappings will be deleted and the specified input configuration will be add.</div>
                        <div>In case of replaced, the existing vlan mappings on the device will be replaced by the configuration for each vlan mapping.</div>
                </td>
            </tr>
    </table>
    <br/>




Examples
--------

.. code-block:: yaml

    #
    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show interface vlan-mappings dot1q-tunnel
    # --------------------------------------------------------------------
    # Name            Vlan                     dot1q-tunnel Vlan  Priority
    # --------------------------------------------------------------------
    # Ethernet4       360-366,392              2755               3
    #
    #  - name: Delete dot1q_tunnel configuration
    #    sonic_vlan_mapping:
    #      config:
    #        - name: Ethernet4
    #          mapping:
    #            - service_vlan: 2755
    #              dot1q_tunnel:
    #                vlan_ids:
    #                  - 392
    #                  - 360-362
    #      state: deleted
    #
    # After state:
    # ------------
    #
    # sonic# show interface vlan-mappings dot1q-tunnel
    # --------------------------------------------------------------------
    # Name            Vlan                     dot1q-tunnel Vlan  Priority
    # --------------------------------------------------------------------
    # Ethernet4       363-366                  2755               3
    #
    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show interface vlan-mappings
    # Flags: M - Multi-tag
    # ---------------------------------------------------------
    # Name            Outer  Inner  Mapped Vlan  Priority Flags
    # ---------------------------------------------------------
    # Ethernet8       610    600    2567         -        -
    # Ethernet8       611    601    2567         1        -
    # Ethernet8       612    602    2567         2        -
    #
    #  - name: Delete vlan translation configuration
    #    sonic_vlan_mapping:
    #      config:
    #        - name: Ethernet8
    #          mapping:
    #          - service_vlan: 2567
    #            vlan_translation:
    #              match_double_tags:
    #                - inner_vlan: 602
    #                  outer_vlan: 612
    #                  priority: 2
    #      state: deleted
    #
    # After state:
    # ------------
    #
    # sonic# show interface vlan-mappings
    # Flags: M - Multi-tag
    # ---------------------------------------------------------
    # Name            Outer  Inner  Mapped Vlan  Priority Flags
    # ---------------------------------------------------------
    # Ethernet8       610    600    2567         -        -
    # Ethernet8       611    601    2567         1        -
    #
    #
    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show interface vlan-mappings dot1q-tunnel
    #
    #  - name: Merge dot1q_tunnel configuration
    #    sonic_vlan_mapping:
    #      config:
    #        - name: Ethernet4
    #          mapping:
    #            - service_vlan: 2755
    #              dot1q_tunnel:
    #                vlan_ids:
    #                  - 392
    #                  - 360-366
    #                priority: 3
    #      state: merged
    #
    # After state:
    # ------------
    #
    # sonic# show interface vlan-mappings dot1q-tunnel
    # --------------------------------------------------------------------
    # Name            Vlan                     dot1q-tunnel Vlan  Priority
    # --------------------------------------------------------------------
    # Ethernet4       360-366,392              2755               3
    #
    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show interface vlan-mappings dot1q-tunnel
    # --------------------------------------------------------------------
    # Name            Vlan                     dot1q-tunnel Vlan  Priority
    # --------------------------------------------------------------------
    # Ethernet4       360-366,392              2755               3
    #
    #  - name: Merge vlan translation configuration
    #    sonic_vlan_mapping:
    #      config:
    #        - name: Ethernet8
    #          mapping:
    #          - service_vlan: 2567
    #            vlan_translation:
    #              match_double_tags:
    #                - inner_vlan: 600
    #                  outer_vlan: 610
    #                - inner_vlan: 601
    #                  outer_vlan: 611
    #                  priority: 1
    #                - inner_vlan: 602
    #                  outer_vlan: 612
    #                  priority: 2
    #      state: merged
    #
    # After state:
    # ------------
    #
    # sonic# show interface vlan-mappings
    # Flags: M - Multi-tag
    # ---------------------------------------------------------
    # Name            Outer  Inner  Mapped Vlan  Priority Flags
    # ---------------------------------------------------------
    # Ethernet8       610    600    2567         -        -
    # Ethernet8       611    601    2567         1        -
    # Ethernet8       612    602    2567         2        -
    #
    # sonic# show interface vlan-mappings dot1q-tunnel
    # --------------------------------------------------------------------
    # Name            Vlan                     dot1q-tunnel Vlan  Priority
    # --------------------------------------------------------------------
    # Ethernet4       360-366,392              2755               3
    #
    #
    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show interface vlan-mappings dot1q-tunnel
    # --------------------------------------------------------------------
    # Name            Vlan                     dot1q-tunnel Vlan  Priority
    # --------------------------------------------------------------------
    # Ethernet4       360-366,392              2755               3
    #
    #  - name: Replace dot1q_tunnel configuration
    #    sonic_vlan_mapping:
    #      config:
    #        - name: Ethernet4
    #          mapping:
    #            - service_vlan: 2755
    #              dot1q_tunnel:
    #                vlan_ids:
    #                  - 660-666
    #                priority: 6
    #      state: replaced
    #
    # After state:
    # ------------
    #
    # sonic# show interface vlan-mappings dot1q-tunnel
    # --------------------------------------------------------------------
    # Name            Vlan                     dot1q-tunnel Vlan  Priority
    # --------------------------------------------------------------------
    # Ethernet4       660-666                  2755               6
    #
    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show interface vlan-mappings
    # Flags: M - Multi-tag
    # ---------------------------------------------------------
    # Name            Outer  Inner  Mapped Vlan  Priority Flags
    # ---------------------------------------------------------
    # Ethernet8       610    600    2567         -        -
    # Ethernet8       611    601    2567         1        -
    # Ethernet8       612    602    2567         2        -
    #
    #  - name: Override vlan translation configuration
    #    sonic_vlan_mapping:
    #      config:
    #        - name: Ethernet8
    #          mapping:
    #          - service_vlan: 2567
    #            vlan_translation:
    #              match_double_tags:
    #                - inner_vlan: 701
    #                  outer_vlan: 711
    #                  priority: 5
    #                - inner_vlan: 702
    #                  outer_vlan: 712
    #                  priority: 6
    #      state: overridden
    #
    # After state:
    # ------------
    #
    # sonic# show interface vlan-mappings
    # Flags: M - Multi-tag
    # ---------------------------------------------------------
    # Name            Outer  Inner  Mapped Vlan  Priority Flags
    # ---------------------------------------------------------
    # Ethernet8       711    701    2567         5        -
    # Ethernet8       712    702    2567         6        -
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

- Cypher Miller (@Cypher-Miller)
