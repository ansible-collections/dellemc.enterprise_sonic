.. _dellemc.enterprise_sonic.sonic_drop_counter_module:


*******************************************
dellemc.enterprise_sonic.sonic_drop_counter
*******************************************

**Manage drop counter configuration on SONiC**


Version added: 3.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of drop counter for devices running SONiC




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
                        <div>List of drop counter configurations</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>alias</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Alias of drop counter</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>counter_description</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Description of drop counter</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>counter_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>PORT_INGRESS_DROPS</li>
                        </ul>
                </td>
                <td>
                        <div>Type of drop counter</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>enable</b>
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
                        <div>Enable drop counter</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>group</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Group of drop counter</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mirror</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Mirror session to mirror the drop counter</div>
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
                        <div>Name of drop counter</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>reasons</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ACL_ANY</li>
                                    <li>ANY</li>
                                    <li>DIP_LINK_LOCAL</li>
                                    <li>EXCEEDS_L3_MTU</li>
                                    <li>FDB_AND_BLACKHOLE_DISCARDS</li>
                                    <li>IP_HEADER_ERROR</li>
                                    <li>L3_EGRESS_LINK_DOWN</li>
                                    <li>MPLS_MISS</li>
                                    <li>SIP_LINK_LOCAL</li>
                                    <li>SMAC_EQUALS_DMAC</li>
                        </ul>
                </td>
                <td>
                        <div>List of drop counter reasons</div>
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
                        <div>The state of the configuration after module completion</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - Tested against Enterprise SONiC Distribution by Dell Technologies
   - Supports ``check_mode``



Examples
--------

.. code-block:: yaml

    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration dropcounters
    # (No 'dropcounters' configuration present)

    - name: Merge drop counter configuration
      dellemc.enterprise_sonic.sonic_drop_counter:
        config:
          - name: counter1
            alias: c1
            counter_description: abc
            counter_type: PORT_INGRESS_DROPS
            enable: true
            group: group1
            mirror: session1
            reasons:
              - ANY
        state: merged

    # After state:
    # ------------
    #
    # sonic# show running-configuration dropcounters
    # !
    # dropcounters counter1
    #  enable
    #  type PORT_INGRESS_DROPS
    #  alias c1
    #  group group1
    #  description "abc"
    #  mirror session1
    #  add-reason ANY


    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration dropcounters
    # !
    # dropcounters counter1
    #  enable
    #  type PORT_INGRESS_DROPS
    #  alias c1
    #  group group1
    #  description "abc"
    #  mirror session1
    #  add-reason ANY
    # !
    # dropcounters counter2
    #  no enable
    #  type PORT_INGRESS_DROPS
    #  alias drop2
    #  group group2
    #  description "xyz789"
    #  add-reason IP_HEADER_ERROR,L3_EGRESS_LINK_DOWN,SMAC_EQUALS_DMAC

    - name: Replace drop counter configuration
      dellemc.enterprise_sonic.sonic_drop_counter:
        config:
          - name: counter1
            counter_description: abc123
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show running-configuration dropcounters
    # !
    # dropcounters counter1
    #  description "abc123"
    # !
    # dropcounters counter2
    #  no enable
    #  type PORT_INGRESS_DROPS
    #  alias drop2
    #  group group2
    #  description "xyz789"
    #  add-reason IP_HEADER_ERROR,L3_EGRESS_LINK_DOWN,SMAC_EQUALS_DMAC


    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration dropcounters
    # !
    # dropcounters counter1
    #  enable
    #  type PORT_INGRESS_DROPS
    #  alias c1
    #  group group1
    #  description "abc"
    #  mirror session1
    #  add-reason ANY
    # !
    # dropcounters counter2
    #  no enable
    #  type PORT_INGRESS_DROPS
    #  alias drop2
    #  group group2
    #  description "xyz789"
    #  add-reason IP_HEADER_ERROR,L3_EGRESS_LINK_DOWN,SMAC_EQUALS_DMAC

    - name: Override drop counter configuration
      dellemc.enterprise_sonic.sonic_drop_counter:
        config:
          - name: counter3
            alias: c3
            counter_description: qwerty
            counter_type: PORT_INGRESS_DROPS
            enable: true
            group: group3
            mirror: session2
            reasons:
              - ACL_ANY
              - FDB_AND_BLACKHOLE_DISCARDS
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show running-configuration dropcounters
    # !
    # dropcounters counter3
    #  enable
    #  type PORT_INGRESS_DROPS
    #  alias c3
    #  group group3
    #  description "qwerty"
    #  mirror session2
    #  add-reason ACL_ANY,FDB_AND_BLACKHOLE_DISCARDS


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration dropcounters
    # !
    # dropcounters counter1
    #  enable
    #  type PORT_INGRESS_DROPS
    #  alias c1
    #  group group1
    #  description "abc"
    #  mirror session1
    #  add-reason ANY
    # !
    # dropcounters counter2
    #  no enable
    #  type PORT_INGRESS_DROPS
    #  alias drop2
    #  group group2
    #  description "xyz789"
    #  add-reason IP_HEADER_ERROR,L3_EGRESS_LINK_DOWN,SMAC_EQUALS_DMAC

    - name: Delete drop counter configuration
      dellemc.enterprise_sonic.sonic_drop_counter:
        config:
          - name: counter1
            alias: c1
            counter_description: abc
          - name: counter2
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration dropcounters
    # !
    # dropcounters counter1
    #  enable
    #  type PORT_INGRESS_DROPS
    #  group group1
    #  mirror session1
    #  add-reason ANY


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration dropcounters
    # !
    # dropcounters counter1
    #  enable
    #  type PORT_INGRESS_DROPS
    #  group group1
    #  mirror session1
    #  add-reason ANY

    - name: Delete all drop counter configuration
      dellemc.enterprise_sonic.sonic_drop_counter:
        config:
        state: deleted

    # After state:
    # ------------
    #
    # (No 'dropcounters' configuration present)



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

- S. Talabi (@stalabi1)
