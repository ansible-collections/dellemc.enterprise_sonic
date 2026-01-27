.. _dellemc.enterprise_sonic.sonic_copp_module:


***********************************
dellemc.enterprise_sonic.sonic_copp
***********************************

**Manage CoPP configuration on SONiC**


Version added: 2.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of CoPP for devices running SONiC




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
                        <div>Specifies CoPP configurations</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>copp_groups</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of CoPP entries that comprise a CoPP group</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>cbs</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Committed bucket size in packets or bytes</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>cir</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Committed information rate in bps or pps (packets per second)</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>copp_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of CoPP classifier</div>
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
                        <div>CoPP queue ID</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>trap_action</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>copy</li>
                                    <li>copy_cancel</li>
                                    <li>deny</li>
                                    <li>drop</li>
                                    <li>forward</li>
                                    <li>log</li>
                                    <li>transit</li>
                                    <li>trap</li>
                        </ul>
                </td>
                <td>
                        <div>CoPP trap action</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>trap_priority</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>CoPP trap priority</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>copp_traps</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.1.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of CoPP entries that comprise a CoPP trap</div>
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
                        <div>Name of CoPP trap</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>trap_group</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of CoPP group</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>trap_protocol_ids</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Comma separated string of trap protocol IDs</div>
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
    # sonic# show copp actions
    # (No "copp actions" configuration present)
    # sonic# show copp classifiers
    # (No "copp classifiers" configuration present)

    - name: Merge CoPP configuration
      dellemc.enterprise_sonic.sonic_copp:
        config:
          copp_groups:
            - copp_name: 'copp-1'
              trap_priority: 1
              trap_action: 'drop'
              queue: 1
              cir: '45'
              cbs: '45'
            - copp_name: 'copp-2'
              trap_priority: 2
              trap_action: 'forward'
              queue: 2
              cir: '90'
              cbs: '90'
          copp_traps:
            - name: 'trap-1'
              trap_protocol_ids: 'id1,id2,id3'
              trap_group: 'copp-1'
        state: merged

    # After state:
    # ------------
    #
    # sonic# show copp actions
    # CoPP action group copp-1
    #    trap-action drop
    #    trap-priority 1
    #    trap-queue 1
    #    police cir 45 cbs 45
    # CoPP action group copp-2
    #    trap-action forward
    #    trap-priority 2
    #    trap-queue 2
    #    police cir 90 cbs 90
    # sonic# show copp classifiers
    # Class-map trap-1 match-type copp
    #   protocol id1
    #   protocol id2
    #   protocol id3


    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show copp actions
    # CoPP action group copp-1
    #    trap-action drop
    #    trap-priority 1
    #    trap-queue 1
    #    police cir 45 cbs 45
    # CoPP action group copp-2
    #    trap-action forward
    #    trap-priority 2
    #    trap-queue 2
    #    police cir 55 cbs 55
    # sonic# show copp classifiers
    # Class-map trap-1 match-type copp
    #   protocol id1
    #   protocol id2
    #   protocol id3

    - name: Replace CoPP configuration
      dellemc.enterprise_sonic.sonic_copp:
        config:
          copp_groups:
            - copp_name: 'copp-1'
              trap_priority: 2
              trap_action: 'forward'
              queue: 2
            - copp_name: 'copp-3'
              trap_priority: 3
              trap_action: 'drop'
              queue: 3
              cir: '1000'
              cbs: '1000'
          copp_traps:
            - name: 'trap-1'
              trap_protocol_ids: 'id1'
              trap_group: 'copp-2'
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show copp actions
    # CoPP action group copp-1
    #    trap-action forward
    #    trap-priority 2
    #    trap-queue 2
    # CoPP action group copp-2
    #    trap-action forward
    #    trap-priority 2
    #    trap-queue 2
    #    police cir 55 cbs 55
    # CoPP action group copp-3
    #    trap-action drop
    #    trap-priority 3
    #    trap-queue 3
    #    police cir 1000 cbs 1000
    # sonic# show copp classifiers
    # Class-map trap-1 match-type copp
    #   protocol id1


    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show copp actions
    # CoPP action group copp-1
    #    trap-action forward
    #    trap-priority 2
    #    trap-queue 2
    # CoPP action group copp-3
    #    trap-action drop
    #    trap-priority 3
    #    trap-queue 3
    #    police cir 1000 cbs 1000
    # Class-map trap-1 match-type copp
    #   protocol id1

    - name: Override CoPP configuration
      dellemc.enterprise_sonic.sonic_copp:
        config:
          copp_groups:
            - copp_name: 'copp-4'
              trap_priority: 4
              trap_action: 'forward'
              queue: 4
              cir: 200
              cbs: 200
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show copp actions
    # CoPP action group copp-4
    #    trap-action forward
    #    trap-priority 4
    #    trap-queue 4
    #    police cir 200 cbs 200


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show copp actions
    # CoPP action group copp-1
    #    trap-action drop
    #    trap-priority 1
    #    trap-queue 1
    #    police cir 45 cbs 45
    # CoPP action group copp-2
    #    trap-action forward
    #    trap-priority 2
    #    trap-queue 2
    #    police cir 90 cbs 90
    # Class-map trap-1 match-type copp

    - name: Delete CoPP configuration
      dellemc.enterprise_sonic.sonic_copp:
        config:
          copp_groups:
            - copp_name: 'copp-1'
              cir: '45'
              cbs: '45'
            - copp_name: 'copp-2'
          copp_traps:
            - name: 'trap-1'
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show copp actions
    # CoPP action group copp-1
    #    trap-action drop
    #    trap-priority 1
    #    trap-queue 1



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
                            <div>The configuration that would be generated by non-check mode module invocation.</div>
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
