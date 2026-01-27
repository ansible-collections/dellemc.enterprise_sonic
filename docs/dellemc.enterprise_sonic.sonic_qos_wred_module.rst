.. _dellemc.enterprise_sonic.sonic_qos_wred_module:


***************************************
dellemc.enterprise_sonic.sonic_qos_wred
***************************************

**Manage QoS WRED profiles configuration on SONiC**


Version added: 2.5.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of QoS WRED profiles for devices running SONiC




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
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>QoS WRED profile configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ecn</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>all</li>
                                    <li>none</li>
                        </ul>
                </td>
                <td>
                        <div>ECN setting for colored packets</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>green</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>WRED configuration for green packets</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>drop_probability</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Drop probablity percentage rate for green packets</div>
                        <div>Range 0-100</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>Enable or disable WRED for green packets</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>max_threshold</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Maximum threshold set for green packets in bytes</div>
                        <div>Range 1000-12480000</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>min_threshold</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Minimum threshold set for green packets in bytes</div>
                        <div>Range 1000-12480000</div>
                </td>
            </tr>

            <tr>
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
                        <div>Name of the WRED profile</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>red</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 4.0.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>WRED configuration for red packets</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>drop_probability</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Drop probablity percentage rate for red packets</div>
                        <div>Range 0-100</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>Enable or disable WRED for red packets</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>max_threshold</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Maximum threshold set for red packets in bytes</div>
                        <div>Range 1000-12480000</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>min_threshold</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Minimum threshold set for red packets in bytes</div>
                        <div>Range 1000-12480000</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>yellow</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 4.0.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>WRED configuration for yellow packets</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>drop_probability</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Drop probablity percentage rate for yellow packets</div>
                        <div>Range 0-100</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>Enable or disable WRED for yellow packets</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>max_threshold</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Maximum threshold set for yellow packets in bytes</div>
                        <div>Range 1000-12480000</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>min_threshold</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Minimum threshold set for yellow packets in bytes</div>
                        <div>Range 1000-12480000</div>
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
                                    <li>overridden</li>
                                    <li>replaced</li>
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



Examples
--------

.. code-block:: yaml

    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show qos wred-policy
    # (No qos wred-policy configuration present)

    - name: Merge QoS WRED policy configuration
      dellemc.enterprise_sonic.sonic_qos_wred:
        config:
          - name: profile1
            ecn: green
            green:
              enable: true
              min_threshold: 1000
              max_threshold: 5000
              drop_probability: 25
            red:
              enable: true
              min_threshold: 1000
              max_threshold: 5000
              drop_probability: 25
            yellow:
              enable: true
              min_threshold: 1000
              max_threshold: 5000
              drop_probability: 25
        state: merged

    # After state:
    # ------------
    #
    # sonic# show qos wred-policy
    # ---------------------------------------------------
    # Policy                 : profile1
    # ---------------------------------------------------
    # ecn                    : ecn_all
    # green-min-threshold    : 1           KBytes
    # green-max-threshold    : 5           KBytes
    # green-drop-probability : 25
    # red-min-threshold    : 1           KBytes
    # red-max-threshold    : 5           KBytes
    # red-drop-probability : 25
    # yellow-min-threshold    : 1           KBytes
    # yellow-max-threshold    : 5           KBytes
    # yellow-drop-probability : 25
    #
    #
    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show qos wred-policy
    # ---------------------------------------------------
    # Policy                 : profile1
    # ---------------------------------------------------
    # ecn                    : ecn_all
    # green-min-threshold    : 1           KBytes
    # green-max-threshold    : 5           KBytes
    # green-drop-probability : 25
    # red-min-threshold    : 1           KBytes
    # red-max-threshold    : 5           KBytes
    # red-drop-probability : 25
    # yellow-min-threshold    : 1           KBytes
    # yellow-max-threshold    : 5           KBytes
    # yellow-drop-probability : 25


    - name: Replace QoS WRED policy configuration
      dellemc.enterprise_sonic.sonic_qos_wred:
        config:
          - name: profile1
            green:
              drop_probability: 75
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show qos wred-policy
    # ---------------------------------------------------
    # Policy                 : profile1
    # ---------------------------------------------------
    # green-drop-probability : 75

    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show qos wred-policy
    # ---------------------------------------------------
    # Policy                 : profile1
    # ---------------------------------------------------
    # ecn                    : ecn_all
    # green-min-threshold    : 1           KBytes
    # green-max-threshold    : 5           KBytes
    # green-drop-probability : 25
    # red-min-threshold    : 1           KBytes
    # red-max-threshold    : 5           KBytes
    # red-drop-probability : 25
    # yellow-min-threshold    : 1           KBytes
    # yellow-max-threshold    : 5           KBytes
    # yellow-drop-probability : 25

    - name: Override QoS WRED policy configuration
      dellemc.enterprise_sonic.sonic_qos_wred:
        config:
          - name: profile2
            ecn: green
            green:
              enable: false
              min_threshold: 3000
              max_threshold: 9000
              drop_probability: 75
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show qos wred-policy
    # ---------------------------------------------------
    # Policy                 : profile2
    # ---------------------------------------------------
    # ecn                    : ecn_all
    # green-min-threshold    : 3           KBytes
    # green-max-threshold    : 9           KBytes
    # green-drop-probability : 75
    # red-min-threshold    : 1           KBytes
    # red-max-threshold    : 5           KBytes
    # red-drop-probability : 25
    # yellow-min-threshold    : 1           KBytes
    # yellow-max-threshold    : 5           KBytes
    # yellow-drop-probability : 25
    #
    #
    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show qos wred-policy
    # ---------------------------------------------------
    # Policy                 : profile1
    # ---------------------------------------------------
    # ecn                    : ecn_all
    # green-min-threshold    : 1           KBytes
    # green-max-threshold    : 5           KBytes
    # green-drop-probability : 25
    # red-min-threshold    : 1           KBytes
    # red-max-threshold    : 5           KBytes
    # red-drop-probability : 25
    # yellow-min-threshold    : 1           KBytes
    # yellow-max-threshold    : 5           KBytes
    # yellow-drop-probability : 25
    # ---------------------------------------------------
    # Policy                 : profile2
    # ---------------------------------------------------
    # ecn                    : ecn_all
    # green-min-threshold    : 3           KBytes
    # green-max-threshold    : 9           KBytes
    # green-drop-probability : 75
    # red-min-threshold    : 1           KBytes
    # red-max-threshold    : 5           KBytes
    # red-drop-probability : 25
    # yellow-min-threshold    : 1           KBytes
    # yellow-max-threshold    : 5           KBytes
    # yellow-drop-probability : 25

    - name: Delete QoS WRED policy configuration
      dellemc.enterprise_sonic.sonic_qos_wred:
        config:
          - name: profile1
          - name: profile2
            green:
              enable: false
              min_threshold: 3000
              max_threshold: 9000
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show qos wred-policy
    # ---------------------------------------------------
    # Policy                 : profile2
    # ---------------------------------------------------
    # ecn                    : ecn_all
    # green-drop-probability : 75
    # red-min-threshold    : 1           KBytes
    # red-max-threshold    : 5           KBytes
    # red-drop-probability : 25
    # yellow-min-threshold    : 1           KBytes
    # yellow-max-threshold    : 5           KBytes
    # yellow-drop-probability : 25



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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format
     as the parameters above.</div>
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

- S. Talabi (@stalabi1)
