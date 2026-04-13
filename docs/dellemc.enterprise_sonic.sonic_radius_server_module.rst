.. _dellemc.enterprise_sonic.sonic_radius_server_module:


********************************************
dellemc.enterprise_sonic.sonic_radius_server
********************************************

**Manage RADIUS server configuration on SONiC**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of radius server for  devices running Enterprise SONiC.




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
                        <div>Specifies the radius server related configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>auth_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>pap</li>
                                    <li>chap</li>
                                    <li>mschapv2</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the authentication type of the radius server.</div>
                        <div>The default is <code>pap</code>.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the key of the radius server.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>nas_ip</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the network access server of the radius server.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>retransmit</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the re-transmit value of the radius server.</div>
                        <div>The range is 0 to 10.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>servers</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the servers list of the radius server.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>host</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the host details of the radius servers list.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>auth_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>pap</li>
                                    <li>chap</li>
                                    <li>mschapv2</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the authentication type of the radius server host.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the key of the radius server host.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>Specifies the IP address or name of the radius server host.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>port</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the port of the radius server host.</div>
                        <div>The range is 1 to 65535.</div>
                        <div>The default is 1812.</div>
                </td>
            </tr>
            <tr>
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
                        <div>Specifies the priority of the radius server host.</div>
                        <div>The range is 1 to 64.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>protocol</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 4.0.0</div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>TLS</li>
                                    <li>UDP</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the protocol of the radius server host.</div>
                        <div>The functional default is <code>UDP</code>.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>retransmit</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the retransmit of the radius server host.</div>
                        <div>The range is 0 to 10.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>security_profile</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 4.0.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the security profile for the radius server host.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>source_interface</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the source interface of the radius server host.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
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
                        <div>Specifies the timeout of the radius server host.</div>
                        <div>The range is 3 to 60.</div>
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
                        <div>Specifies the vrf of the radius server host.</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>statistics</b>
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
                        <div>Specifies the statistics flag of the radius server.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Specifies the timeout of the radius server.</div>
                        <div>The range is 3 to 60.</div>
                        <div>The default is 5.</div>
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
                                    <li>replaced</li>
                                    <li>overridden</li>
                                    <li>deleted</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the operation to be performed on the radius server configured on the device.</div>
                        <div>In case of merged, the input mode configuration will be merged with the existing radius server configuration on the device.</div>
                        <div>In case of deleted the existing radius server mode configuration will be removed from the device.</div>
                        <div>In case of replaced, the existing radius server configuration will be replaced with provided configuration.</div>
                        <div>In case of overridden, the existing radius server configuration will be overridden with the provided configuration.</div>
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
    # sonic# show running-configuration | grep radius-server
    # radius-server nas-ip 10.11.12.13
    # radius-server statistics enable
    # radius-server timeout 12
    # radius-server retransmit 5
    # radius-server auth-type chap
    # radius-server host 10.10.10.10 protocol TLS security-profile rad-sec-prof
    # radius-server host my-host1.dell auth-port 55 timeout 12 retransmit 7 auth-type chap priority 3 vrf VrfAnsibleTest source-interface Ethernet100

    - name: Delete specified radius server configuration
      dellemc.enterprise_sonic.sonic_radius_server:
        config:
          auth_type: chap
          nas_ip: 10.11.12.13
          timeout: 12
          servers:
            host:
              - name: 10.10.10.10
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration | grep radius-server
    # radius-server statistics enable
    # radius-server retransmit 5
    # radius-server host my-host1.dell auth-port 55 timeout 12 retransmit 7 auth-type chap priority 3 vrf VrfAnsibleTest source-interface Ethernet100


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration | grep radius-server
    # radius-server nas-ip 10.11.12.13
    # radius-server statistics enable
    # radius-server timeout 12
    # radius-server retransmit 5
    # radius-server auth-type chap
    # radius-server host 10.10.10.10 protocol TLS security-profile rad-sec-prof
    # radius-server host my-host1.dell auth-port 55 timeout 12 retransmit 7 auth-type chap priority 3 vrf VrfAnsibleTest source-interface Ethernet100

    - name: Delete all radius server configuration
      dellemc.enterprise_sonic.sonic_radius_server:
        config:
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration | grep radius-server
    # (No radius-server configuration present)


    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration | grep radius-server
    # (No radius-server configuration present)

    - name: Merge radius server configuration
      dellemc.enterprise_sonic.sonic_radius_server:
        config:
          auth_type: chap
          timeout: 12
          nas_ip: 10.11.12.13
          retransmit: 5
          statistics: true
          servers:
            host:
              - name: my-host1.dell
                auth_type: chap
                priority: 3
                vrf: VrfAnsibleTest
                timeout: 12
                port: 55
                source_interface: Ethernet100
                retransmit: 7
              - name: "10.10.10.10"
                protocol: "TLS"
                security_profile: "rad-sec-prof"
        state: merged

    # After state:
    # ------------
    #
    # sonic# show running-configuration | grep radius-server
    # radius-server nas-ip 10.11.12.13
    # radius-server statistics enable
    # radius-server timeout 12
    # radius-server retransmit 5
    # radius-server auth-type chap
    # radius-server host 10.10.10.10 protocol TLS security-profile rad-sec-prof
    # radius-server host my-host1.dell auth-port 55 timeout 12 retransmit 7 auth-type chap priority 3 vrf VrfAnsibleTest source-interface Ethernet100


    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration | grep radius-server
    # radius-server nas-ip 10.11.12.13
    # radius-server statistics enable
    # radius-server timeout 12
    # radius-server retransmit 5
    # radius-server auth-type chap
    # radius-server host 10.10.10.10 protocol TLS security-profile rad-sec-prof
    # radius-server host my-host1.dell auth-port 55 timeout 12 retransmit 7 auth-type chap priority 3 vrf VrfAnsibleTest source-interface Ethernet100

    - name: Replace specified radius server host configuration
      sonic_radius_server:
        config:
          servers:
            - host:
                name: my-host1.dell
                auth_type: mschapv2
                source_interface: Ethernet12
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show running-configuration | grep radius-server
    # radius-server nas-ip 10.11.12.13
    # radius-server statistics enable
    # radius-server timeout 12
    # radius-server retransmit 5
    # radius-server auth-type chap
    # radius-server host 10.10.10.10 protocol TLS security-profile rad-sec-prof
    # radius-server host my-host1.dell auth-type mschapv2 source-interface Ethernet12

    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration | grep radius-server
    # radius-server nas-ip 10.11.12.13
    # radius-server statistics enable
    # radius-server timeout 12
    # radius-server retransmit 5
    # radius-server auth-type chap
    # radius-server host 10.10.10.10 protocol TLS security-profile rad-sec-prof
    # radius-server host my-host1.dell auth-type mschapv2 source-interface Ethernet12

    - name: Override radius server configuration
      sonic_radius_server:
        config:
          servers:
            - host:
                name: 20.20.20.20
                protocol: TLS
                security_profile: rad-sec-prof
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show running-configuration | grep radius-server
    # radius-server host 20.20.20.20 protocol TLS security-profile rad-sec-prof



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

- Niraimadaiselvam M (@niraimadaiselvamm)
