.. _dellemc.enterprise_sonic.sonic_evpn_esi_multihome_module:


*************************************************
dellemc.enterprise_sonic.sonic_evpn_esi_multihome
*************************************************

**Manage EVPN ESI multihoming configuration on SONiC**


Version added: 3.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of EVPN ESI multihoming for devices running SONiC




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
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>EVPN ESI multihoming configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>df_election_time</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Election timer value in seconds</div>
                        <div>Has a range of 0 to 86400</div>
                        <div>Default is 3</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>es_activation_delay</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Activation delay in seconds</div>
                        <div>Has a range of 0 to 1200000</div>
                        <div>Default is 0</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mac_holdtime</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>MAC hold time in seconds</div>
                        <div>Has a range of 0 to 86400</div>
                        <div>Default is 1080</div>
                        <div>Specify 0 to disable MAC hold time</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>neigh_holdtime</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Neighbor hold time in seconds</div>
                        <div>Has a range of 0 to 86400</div>
                        <div>Default is 1080</div>
                        <div>Specify 0 to disable neighbor hold time</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>startup_delay</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Startup delay in seconds</div>
                        <div>Has a range of 0 to 3600</div>
                        <div>Default is 300</div>
                        <div>Specify 0 to disable startup delay</div>
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
   - Tested against Enterprise SONiC Distribution by Dell Technologies.
   - Supports ``check_mode``.



Examples
--------

.. code-block:: yaml

    # Using "deleted" state
    #
    # Before state:
    # ---------------
    #
    # sonic# show running-configuration evpn-mh
    # !
    # evpn esi-multihoming
    #  mac-holdtime 1080
    #  neigh-holdtime 1080
    #  startup-delay 300

    - name: Delete specific option from evpn_esi_multihome configuration
      sonic_evpn_esi_multihome:
        config:
          mac-holdtime: 1080
        state: deleted

    # After State:
    # --------------
    #
    # sonic# show running-configuration evpn-mh
    # !
    # evpn esi-multihoming
    #  neigh-holdtime 1080
    #  startup-delay 300


    # Using "deleted" state
    #
    # Before state:
    # ---------------
    #
    # sonic# show running-configuration evpn-mh
    # !
    # evpn esi-multihoming
    #  mac-holdtime 1080
    #  neigh-holdtime 1080
    #  startup-delay 300
    #  df-election-time 3

    - name: Delete all evpn_esi_multihome configuration
      sonic_evpn_esi_multihome:
        config: {}
        state: deleted

    # After State:
    # --------------
    #
    # sonic# show running-configuration evpn-mh
    # (No "evpn-mh" configuration present)


    # Using "merged" state
    #
    # Before state:
    # ---------------
    #
    # sonic# show running-configuration evpn-mh
    # (No "evpn-mh" configuration present)

    - name: Merge specific option from evpn_esi_multihome configuration
      sonic_evpn_esi_multihome:
        config:
          startup-delay: 300
          es-activation-delay: 3000
        state: merged

    # After State:
    # --------------
    #
    # sonic# show running-configuration evpn-mh
    # !
    # evpn esi-multihoming
    #  startup-delay 300
    #  es-activation-delay 3000


    # Using "replaced" state
    #
    # Before state:
    # ----------------
    #
    # sonic# show running-configuration evpn-mh
    # !
    # evpn esi-multihoming
    #  mac-holdtime 1080
    #  neigh-holdtime 1080
    #  startup-delay 300
    #  df-election-time: 3

    - name: Replace evpn_esi_multihome configuration
      sonic_evpn_esi_multihome:
        config:
          neigh-holdtime: 200
          df-election-time: 600
        state: replaced

    # After State:
    # --------------
    #
    # sonic# show running-configuration evpn-mh
    # !
    # evpn esi-multihoming
    #  neigh-holdtime 200
    #  df-election-time: 600


    # Using "overridden" state
    #
    # Before state:
    # ----------------
    #
    # sonic# show running-configuration evpn-mh
    # !
    # evpn esi-multihoming
    #  mac-holdtime 1080
    #  neigh-holdtime 1080
    #  startup-delay 300

    - name: Override evpn_esi_multihome configuration
      sonic_evpn_esi_multihome:
        config:
          startup-delay: 200
          mac_holdtime: 500
        state: overridden

    # After State:
    # --------------
    #
    # sonic# show running-configuration evpn-mh
    # !
    # evpn esi-multihoming
    #  startup-delay 200
    #  mac_holdtime: 500



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

- Aida Shumburo (@aida-shumburo)
