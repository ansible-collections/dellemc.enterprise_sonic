.. _dellemc.enterprise_sonic.sonic_lst_module:


**********************************
dellemc.enterprise_sonic.sonic_lst
**********************************

**Manage link state tracking (LST) configuration on SONiC**


Version added: 3.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of LST for devices running SONiC




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
                        <div>LST configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>LST configuration for interfaces</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>downstream_group</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>LST group name used to track the interface as downstream</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Name of interface</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>upstream_groups</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Upstream groups configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
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
                        <div>LST group name used to track the interface as upstream</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>lst_groups</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>LST groups configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>all_evpn_es_downstream</b>
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
                        <div>Indicates that the LST group tracks all EVPN ethernet segments as downstream interfaces</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>all_mclags_downstream</b>
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
                        <div>Indicates that the LST group tracks all MCLAGs as downstream interfaces</div>
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
                        <div>Description of LST group</div>
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
                                    <li>l3</li>
                        </ul>
                </td>
                <td>
                        <div>LST group type</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Name of LST group</div>
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
                        <div>Downstream ports will shut down if the threshold falls below this value</div>
                        <div>Range 0-100</div>
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
                                    <li>percentage</li>
                        </ul>
                </td>
                <td>
                        <div>Type of threshold calculation scheme to use</div>
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
                        <div>Downstream ports will go online if the threshold is greater than or equal to this value</div>
                        <div>Range 0-100</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Time in seconds to wait to bring up the downstream ports after the first upstream port is online</div>
                        <div>Range 1-1800</div>
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
    # sonic# show running-configuration link state tracking
    # (No link state tracking configuration present)
    # sonic# show running-configuration interface Ethernet 20
    # !
    # interface Ethernet20
    # (No link state tracking configuration present for interface Ethernet20)
    # sonic# show running-configuration interface Ethernet 24
    # !
    # interface Ethernet24
    # (No link state tracking configuration present for interface Ethernet24)

    - name: Merge LST configuration
      dellemc.enterprise_sonic.sonic_lst:
        config:
          lst_groups:
            - name: lst
              all_evpn_es_downstream: true
              group_description: abc
              group_type: l3
              threshold_down: 20
              threshold_type: percentage
              threshold_up: 40
              timeout: 120
          interfaces:
            - name: Ethernet20
              downstream_group: lst
            - name: Ethernet24
              upstream_groups:
                - group_name: lst
        state: merged

    # After state:
    # ------------
    #
    # sonic# show running-configuration link state tracking
    # !
    # link state track lst
    #   timeout 120
    #   description abc
    #   downstream all-evpn-es
    #   threshold type percentage up 40 down 20
    # sonic# show running-configuration interface Ethernet 20
    # !
    # interface Ethernet20
    #  link state track lst downstream
    # sonic# show running-configuration interface Ethernet 24
    # !
    # interface Ethernet24
    #  link state track lst upstream


    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration link state tracking
    # !
    # link state track lst
    #   timeout 120
    #   description abc
    #   downstream all-evpn-es
    #   threshold type percentage up 40 down 20
    # sonic# show running-configuration interface Ethernet 20
    # !
    # interface Ethernet20
    #  link state track lst downstream
    # sonic# show running-configuration interface Ethernet 24
    # !
    # interface Ethernet24
    #  link state track lst upstream

    - name: Replace LST configuration
      dellemc.enterprise_sonic.sonic_lst:
        config:
          lst_groups:
            - name: lst
              all_mclags_downstream: true
              timeout: 75
          interfaces:
            - name: Ethernet20
              upstream_groups:
                - group_name: lst
            - name: Ethernet24
              downstream_group: lst
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show running-configuration link state tracking
    # !
    # link state track lst
    #   timeout 75
    #   downstream all-mclag
    # sonic# show running-configuration interface Ethernet 20
    # !
    # interface Ethernet20
    #  link state track lst upstream
    # sonic# show running-configuration interface Ethernet 24
    # !
    # interface Ethernet24
    #  link state track lst downstream


    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration link state tracking
    # !
    # link state track lst
    #   timeout 75
    #   downstream all-mclag
    # sonic# show running-configuration interface Ethernet 20
    # !
    # interface Ethernet20
    #  link state track lst upstream
    # sonic# show running-configuration interface Ethernet 24
    # !
    # interface Ethernet24
    #  link state track lst downstream

    - name: Override LST configuration
      dellemc.enterprise_sonic.sonic_lst:
        config:
          lst_groups:
            - name: lst2
              all_evpn_es_downstream: true
              group_description: xyz
              group_type: l3
              threshold_down: 30
              threshold_type: percentage
              threshold_up: 50
              timeout: 130
          interfaces:
            - name: Ethernet20
              downstream_group: lst2
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show running-configuration link state tracking
    # !
    # link state track lst2
    #   timeout 130
    #   description xyz
    #   downstream all-evpn-es
    #   threshold type percentage up 50 down 30
    # sonic# show running-configuration interface Ethernet 20
    # !
    # interface Ethernet20
    #  link state track lst2 downstream
    # sonic# show running-configuration interface Ethernet 24
    # !
    # interface Ethernet24
    # (No link state configuration present for interface Ethernet24)


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration link state tracking
    # !
    # link state track lst2
    #   timeout 130
    #   description xyz
    #   downstream all-evpn-es
    #   threshold type percentage up 50 down 30
    # sonic# show running-configuration interface Ethernet 20
    # !
    # interface Ethernet20
    #  link state track lst2 downstream
    # sonic# show running-configuration interface Ethernet 24
    # !
    # interface Ethernet24
    #  link state track lst2 upstream

    - name: Delete LST configuration
      dellemc.enterprise_sonic.sonic_lst:
        config:
          lst_groups:
            - name: lst2
              all_evpn_es_downstream: true
              group_description: xyz
              threshold_down: 30
              threshold_type: percentage
              threshold_up: 50
              timeout: 130
          interfaces:
            - name: Ethernet20
              downstream_group: lst2
            - name: Ethernet24
              upstream_groups:
                - group_name: lst2
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration link state tracking
    # !
    # link state track lst2
    # sonic# show running-configuration interface Ethernet 20
    # !
    # interface Ethernet20
    # (No link state configuration present for interface Ethernet20)
    # sonic# show running-configuration interface Ethernet 24
    # !
    # interface Ethernet24
    # (No link state configuration present for interface Ethernet24)


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration link state tracking
    # !
    # link state track lst
    #   timeout 120
    #   description abc
    #   downstream all-evpn-es
    #   threshold type percentage up 40 down 20
    # sonic# show running-configuration interface Ethernet 20
    # !
    # interface Ethernet20
    #  link state track lst downstream
    # sonic# show running-configuration interface Ethernet 24
    # !
    # interface Ethernet24
    #  link state track lst upstream

    - name: Delete LST configuration
      dellemc.enterprise_sonic.sonic_lst:
        config: {}
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration link state tracking
    # (No link state tracking configuration present)
    # sonic# show running-configuration interface Ethernet 20
    # !
    # interface Ethernet20
    # (No link state tracking configuration present for interface Ethernet20)
    # sonic# show running-configuration interface Ethernet 24
    # !
    # interface Ethernet24
    # (No link state tracking configuration present for interface Ethernet24)



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
                            <div>The resulting configuration from module invocation.</div>
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
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>when <code>check_mode</code></td>
                <td>
                            <div>The generated configuration from module invocation.</div>
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
                      <span style="color: purple">dictionary</span>
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

- S\. Talabi (@stalabi1)
