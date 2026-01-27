.. _dellemc.enterprise_sonic.sonic_fbs_groups_module:


*****************************************
dellemc.enterprise_sonic.sonic_fbs_groups
*****************************************

**Manage flow based services (FBS) groups configuration on SONiC**


Version added: 3.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of FBS groups for devices running SONiC




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
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>FBS groups configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>next_hop_groups</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Next-hop groups configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>group_description</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Description of next-hop group</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>group_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of next-hop group</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>group_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ipv4</li>
                                    <li>ipv6</li>
                        </ul>
                </td>
                <td>
                        <div>Type of next-hop group</div>
                        <div>The group type is required for merged, replaced, and overridden states.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>next_hops</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Next-hops configuration for forwarding</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>entry_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Entry ID, range 1-65535</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ip_address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Forwarding IP address</div>
                        <div>The IP address is required for merged, replaced, and overridden states.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>next_hop_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>non_recursive</li>
                                    <li>overlay</li>
                                    <li>recursive</li>
                        </ul>
                </td>
                <td>
                        <div>Type of next-hop</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>Forwarding network instance</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>threshold_down</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the threshold value equal to or below for a next-hop to not be considered forwardable</div>
                        <div>Range 0-127</div>
                        <div><em>threshold_type</em> must be configured.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>threshold_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>count</li>
                                    <li>percentage</li>
                        </ul>
                </td>
                <td>
                        <div>Type of threshold</div>
                        <div>Deletion of <em>threshold_type</em> will delete <em>threshold_up</em> and <em>threshold_down</em>.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>threshold_up</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the minimum threshold value for a next-hop group to be considered forwardable</div>
                        <div>Range 1-128</div>
                        <div><em>threshold_type</em> must be configured.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>replication_groups</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Replication groups configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>group_description</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Description of replication group</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>group_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of replication group</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>group_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ipv4</li>
                                    <li>ipv6</li>
                        </ul>
                </td>
                <td>
                        <div>Type of replication group</div>
                        <div>The group type is required for merged, replaced, and overridden states.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>next_hops</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Next-hops configuration for forwarding</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>entry_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Entry ID, range 1-65535</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ip_address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Forwarding IP address</div>
                        <div>The IP address is required for merged, replaced, and overridden states.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>next_hop_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>non_recursive</li>
                                    <li>overlay</li>
                                    <li>recursive</li>
                        </ul>
                </td>
                <td>
                        <div>Type of next-hop</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>single_copy</b>
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
                        <div>Enable/disable single path to create copy</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>Forwarding network instance</div>
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
    # sonic# show running-configuration pbf next-hop-group
    # (No 'pbf next-hop-group' configuration present)
    # sonic# show running-configuration pbf replication-group
    # (No 'pbf replication-group' configuration present)

    - name: Merge FBS groups configuration
      dellemc.enterprise_sonic.sonic_fbs_groups:
        config:
          next_hop_groups:
            - group_name: hop1
              group_description: abc
              group_type: ipv4
              threshold_type: count
              threshold_up: 15
              threshold_down: 5
              next_hops:
                - entry_id: 1
                  ip_address: 1.1.1.1
                  vrf: VrfReg1
                  next_hop_type: non_recursive
          replication_groups:
            - group_name: rep1
              group_description: xyz
              group_type: ipv6
              next_hops:
                - entry_id: 2
                  ip_address: 1::1
                  vrf: VrfReg2
                  next_hop_type: overlay
                  single_copy: true
        state: merged

    # After state:
    # ------------
    #
    # sonic# show running-configuration pbf next-hop-group
    # !
    # pbf next-hop-group hop1 type ip
    #   description abc
    #   threshold type count up 15 down 5
    #   entry 1 next-hop 1.1.1.1 vrf VrfReg1 non-recursive
    # !
    # sonic# show running-configuration pbf replication-group
    # !
    # pbf replication-group rep1 type ipv6
    #   description xyz
    #   entry 2 next-hop 1::1 vrf VrfReg2 overlay single-copy
    # !


    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration pbf next-hop-group
    # !
    # pbf next-hop-group hop1 type ip
    #   description abc
    #   threshold type count up 15 down 5
    #   entry 1 next-hop 1.1.1.1 vrf VrfReg1 non-recursive
    # !
    # pbf next-hop-group hop2 type ipv6
    #   description abc
    #   entry 5 next-hop 3::3 vrf default non-recursive
    # !
    # sonic# show running-configuration pbf replication-group
    # !
    # pbf replication-group rep1 type ipv6
    #   description xyz
    #   entry 2 next-hop 1::1 vrf VrfReg2 overlay single-copy
    # !

    - name: Replace FBS groups configuration
      dellemc.enterprise_sonic.sonic_fbs_groups:
        config:
          next_hop_groups:
            - group_name: hop2
              group_description: xyz
              group_type: ipv4
              next_hops:
                - entry_id: 1
                  ip_address: 1.1.1.1
                  vrf: VrfReg1
                  next_hop_type: recursive
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show running-configuration pbf next-hop-group
    # !
    # pbf next-hop-group hop1 type ip
    #   description abc
    #   threshold type count up 15 down 5
    #   entry 1 next-hop 1.1.1.1 vrf VrfReg1 non-recursive
    # !
    # pbf next-hop-group hop2 type ipv4
    #   description xyz
    #   entry 1 next-hop 1.1.1.1 vrf VrfReg1 recursive
    # !
    # sonic# show running-configuration pbf replication-group
    # !
    # pbf replication-group rep1 type ipv6
    #   description xyz
    #   entry 2 next-hop 1::1 vrf VrfReg2 overlay single-copy
    # !


    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration pbf next-hop-group
    # !
    # pbf next-hop-group hop1 type ip
    #   description abc
    #   entry 1 next-hop 1.1.1.1 vrf VrfReg1 non-recursive
    # !
    # sonic# show running-configuration pbf replication-group
    # !
    # pbf replication-group rep1 type ipv6
    #   description xyz
    #   entry 2 next-hop 1::1 vrf VrfReg2 overlay single-copy
    # !

    - name: Override FBS groups configuration
      dellemc.enterprise_sonic.sonic_fbs_groups:
        config:
          next_hop_groups:
            - group_name: hop1
              group_description: abc
              group_type: ipv4
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show running-configuration pbf next-hop-group
    # !
    # pbf next-hop-group hop1 type ip
    #   description abc
    # !
    # sonic# show running-configuration pbf replication-group
    # (No 'pbf replication-group' configuration present)


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration pbf next-hop-group
    # !
    # pbf next-hop-group hop1 type ip
    #   description abc
    #   entry 1 next-hop 1.1.1.1 vrf VrfReg1 non-recursive
    # !
    # sonic# show running-configuration pbf replication-group
    # !
    # pbf replication-group rep1 type ipv6
    #   description xyz
    #   entry 2 next-hop 1::1 vrf VrfReg2 overlay single-copy
    # !

    - name: Delete FBS groups configuration
      dellemc.enterprise_sonic.sonic_fbs_groups:
        config:
          next_hop_groups:
            - group_name: hop1
              group_description: abc
          replication_groups:
            - group_name: rep1
              next_hops:
                - entry_id: 2
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration pbf next-hop-group
    # !
    # pbf next-hop-group hop1 type ip
    #   entry 1 next-hop 1.1.1.1 vrf VrfReg1 non-recursive
    # !
    # sonic# show running-configuration pbf replication-group
    # !
    # pbf replication-group rep1 type ipv6
    #   description xyz
    # !


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration pbf next-hop-group
    # !
    # pbf next-hop-group hop1 type ip
    #   entry 1 next-hop 1.1.1.1 vrf VrfReg1 non-recursive
    # !
    # sonic# show running-configuration pbf replication-group
    # !
    # pbf replication-group rep1 type ipv6
    #   description xyz
    # !

    - name: Delete FBS groups configuration
      dellemc.enterprise_sonic.sonic_fbs_groups:
        config:
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration pbf next-hop-group
    # (No 'pbf next-hop-group' configuration present)
    # sonic# show running-configuration pbf replication-group
    # (No 'pbf replication-group' configuration present)



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
                            <div>The resulting configuration module invocation.</div>
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

- S. Talabi (@stalabi1)
