.. _dellemc.enterprise_sonic.sonic_logging_module:


**************************************
dellemc.enterprise_sonic.sonic_logging
**************************************

**Manage logging configuration on SONiC.**


Version added: 2.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of logging for devices running SONiC.




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
                        <div>Specifies logging related configurations.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>remote_servers</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Remote logging sever configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>host</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IPv4/IPv6 address or host name of the remote logging server.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>message_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>log</li>
                                    <li>event</li>
                                    <li>audit</li>
                                    <li>auditd-system</li>
                        </ul>
                </td>
                <td>
                        <div>Type of messages that remote server receives. Defaults to &quot;log&quot; value.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>protocol</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>TCP</li>
                                    <li>TLS</li>
                                    <li>UDP</li>
                        </ul>
                </td>
                <td>
                        <div>Type of the protocol for sending the  messages. Defaults to &quot;UDP&quot; value.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>remote_port</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Destination port number for logging messages sent to the server.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>severity</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.1.0</div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>debug</li>
                                    <li>info</li>
                                    <li>notice</li>
                                    <li>warning</li>
                                    <li>error</li>
                                    <li>critical</li>
                                    <li>alert</li>
                                    <li>emergency</li>
                        </ul>
                </td>
                <td>
                        <div>The log severity filter for remote syslog server. Defaults to &quot;notice&quot; value.</div>
                </td>
            </tr>
            <tr>
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
                        <div>Source interface used as source ip for sending logging packets.</div>
                </td>
            </tr>
            <tr>
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
                        <div>VRF name used by remote logging server.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>security_profile</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.1.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the security profile name for the global syslog settings.</div>
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

    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show logging servers
    # ----------------------------------------------------------------------------------------------------------
    # HOST            PORT      SOURCE-INTERFACE    VRF            MESSAGE-TYPE   SEVERITY            PROTOCOL
    # ----------------------------------------------------------------------------------------------------------
    # 10.11.0.2       5         Ethernet24          -              event          notice              udp
    # 10.11.1.1       616       Ethernet8           -              log            alert               tcp
    # log1.dell.com   6         Ethernet28          -              audit          notice              udp
    # 10.11.1.2       116       Ethernet6           -              log            notice              tls
    #
    # sonic# show running-configuration | grep logging
    # !
    # logging security-profile default
    # !

    - name: Delete logging server configuration
      sonic_logging:
        config:
          remote_servers:
            - host: 10.11.0.2
            - host: log1.dell.com
            - host: 10.11.1.1
              message_type: log
              protocol: tcp
              source_interface: Ethernet8
              severity: alert
          security_profile: "default"
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show logging servers
    # ----------------------------------------------------------------------------------------------------------
    # HOST            PORT      SOURCE-INTERFACE    VRF            MESSAGE-TYPE   SEVERITY            PROTOCOL
    # ----------------------------------------------------------------------------------------------------------
    # 10.11.1.1       616       -                   -              log            notice              udp
    # 10.11.1.2       116       Ethernet6           -              log            notice              tls
    #
    # sonic# show running-configuration | grep logging
    # sonic#
    #
    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show logging servers
    # ----------------------------------------------------------------------------------------------------------
    # HOST            PORT      SOURCE-INTERFACE    VRF            MESSAGE-TYPE   SEVERITY            PROTOCOL
    # ----------------------------------------------------------------------------------------------------------
    # 10.11.1.1       616       Ethernet8           -              log            notice              tcp
    #
    # sonic# show running-configuration | grep logging
    # sonic#
    - name: Merge logging server configuration
      sonic_logging:
        config:
          remote_servers:
            - host: 10.11.0.2
              remote_port: 5
              protocol: TCP
              source_interface: Ethernet24
              message_type: event
            - host: 10.11.0.1
              remote_port: 4
              protocol: TLS
              source_interface: Ethernet2
            - host: 10.11.1.1
              severity: error
            - host: log1.dell.com
              remote_port: 6
              protocol: udp
              source_interface: Ethernet28
              message_type: audit
          security_profile: "default"
        state: merged

    # After state:
    # ------------
    # sonic# show logging servers
    # ----------------------------------------------------------------------------------------------------------
    # HOST            PORT      SOURCE-INTERFACE    VRF            MESSAGE-TYPE   SEVERITY            PROTOCOL
    # ----------------------------------------------------------------------------------------------------------
    # 10.11.0.2       5         Ethernet24          -              event          notice              udp
    # 10.11.0.1       4         Ethernet2           -              log            notice              tls
    # 10.11.1.1       616       Ethernet8           -              log            error               tcp
    # log1.dell.com   6         Ethernet28          -              audit          notice              udp
    # sonic# show running-configuration | grep logging
    # !
    # logging security-profile default
    # !
    #
    #
    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show logging servers
    # ----------------------------------------------------------------------------------------------------------
    # HOST            PORT      SOURCE-INTERFACE    VRF            MESSAGE-TYPE   SEVERITY            PROTOCOL
    # ----------------------------------------------------------------------------------------------------------
    # 10.11.1.1       616       Ethernet8           -              log            notice              tcp
    # 10.11.1.2       626       Ethernet16          -              event          emergency           udp
    # 10.11.1.3       626       Ethernet14          -              log            notice              tls
    #
    # sonic# show running-configuration | grep logging
    # !
    # logging security-profile default
    # !
    - name: Override logging server configuration
      sonic_logging:
        config:
          remote_servers:
            - host: 10.11.1.2
              remote_port: 622
              protocol: TCP
              source_interface: Ethernet24
              message_type: audit
              severity: alert
        state: overridden
    #
    # After state:
    # ------------
    # sonic# show logging servers
    # ----------------------------------------------------------------------------------------------------------
    # HOST            PORT      SOURCE-INTERFACE    VRF            MESSAGE-TYPE   SEVERITY            PROTOCOL
    # ----------------------------------------------------------------------------------------------------------
    # 10.11.1.2       622       Ethernet24          -              audit          alert               tcp
    # sonic# show running-configuration | grep logging
    # sonic#
    #
    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show logging servers
    # ----------------------------------------------------------------------------------------------------------
    # HOST            PORT      SOURCE-INTERFACE    VRF            MESSAGE-TYPE   SEVERITY            PROTOCOL
    # ----------------------------------------------------------------------------------------------------------
    # 10.11.1.1       616       Ethernet8           -              log            notice              tcp
    # 10.11.1.2       626       Ethernet16          -              event          notice              udp
    #
    # sonic# show running-configuration | grep logging
    # sonic#
    - name: Replace logging server configuration
      sonic_logging:
        config:
          remote_servers:
            - host: 10.11.1.2
              remote_port: 622
              protocol: UDP
              message_type: audit
              severity: debug
          security_profile: "default"
        state: replaced
    #
    # After state:
    # ------------
    #
    # "MESSAGE-TYPE" has default value of "log"
    #
    # ----------------------------------------------------------------------------------------------------------
    # HOST            PORT      SOURCE-INTERFACE    VRF            MESSAGE-TYPE   SEVERITY            PROTOCOL
    # ----------------------------------------------------------------------------------------------------------
    # 10.11.1.1       616       Ethernet8           -              log            notice              tcp
    # 10.11.1.2       622       -                   -              audit          debug               udp
    # sonic# show running-configuration | grep logging
    # !
    # logging security-profile default
    # !
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

- M\. Zhang (@mingjunzhang2019)
