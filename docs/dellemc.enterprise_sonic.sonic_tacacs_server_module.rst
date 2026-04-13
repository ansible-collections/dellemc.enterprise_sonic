.. _dellemc.enterprise_sonic.sonic_tacacs_server_module:


********************************************
dellemc.enterprise_sonic.sonic_tacacs_server
********************************************

**Manage TACACS server and its parameters**


Version added: 1.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of tacacs server parameters on devices running Enterprise SONiC.




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
                        <div>Specifies the tacacs server related configuration.</div>
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
                                    <li><div style="color: blue"><b>pap</b>&nbsp;&larr;</div></li>
                                    <li>chap</li>
                                    <li>mschap</li>
                                    <li>login</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the authentication type of the tacacs server.</div>
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
                        <div>Specifies the key of the tacacs server.</div>
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
                        <div>Specifies the servers list of the tacacs server.</div>
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
                        <div>Specifies the host details of the tacacs servers list.</div>
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
                                    <li><div style="color: blue"><b>pap</b>&nbsp;&larr;</div></li>
                                    <li>chap</li>
                                    <li>mschap</li>
                                    <li>login</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the authentication type of the tacacs server host.</div>
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
                        <div>Specifies the key of the tacacs server host.</div>
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
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the name of the tacacs server host.</div>
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
                        <b>Default:</b><br/><div style="color: blue">49</div>
                </td>
                <td>
                        <div>Specifies the port of the tacacs server host.</div>
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
                        <b>Default:</b><br/><div style="color: blue">1</div>
                </td>
                <td>
                        <div>Specifies the priority of the tacacs server host.</div>
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
                        <b>Default:</b><br/><div style="color: blue">5</div>
                </td>
                <td>
                        <div>Specifies the timeout of the tacacs server host.</div>
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
                        <b>Default:</b><br/><div style="color: blue">"default"</div>
                </td>
                <td>
                        <div>Specifies the vrf of the tacacs server host.</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Specifies the source interface of the tacacs server.</div>
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
                        <b>Default:</b><br/><div style="color: blue">5</div>
                </td>
                <td>
                        <div>Specifies the timeout of the tacacs server.</div>
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
                        <div>Specifies the operation to be performed on the tacacs server configured on the device.</div>
                        <div>In case of merged, the input mode configuration will be merged with the existing tacacs server configuration on the device.</div>
                        <div>In case of deleted the existing tacacs server mode configuration will be removed from the device.</div>
                        <div>In case of replaced, the existing tacacs server configuration will be replaced with provided configuration.</div>
                        <div>In case of overridden, the existing tacacs server configuration will be overridden with the provided configuration.</div>
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
    # do show tacacs-server
    # ---------------------------------------------------------
    # TACACS Global Configuration
    # ---------------------------------------------------------
    # source-interface  : Ethernet12
    # timeout    : 10
    # auth-type  : login
    # key        : login
    # ------------------------------------------------------------------------------------------------
    # HOST                 AUTH-TYPE       KEY        PORT       PRIORITY   TIMEOUT    VRF
    # ------------------------------------------------------------------------------------------------
    # 1.2.3.4              pap             *****      50         2          10         mgmt
    # localhost            pap                        49         1          5          default
    #

    - name: Merge tacacs configurations
      dellemc.enterprise_sonic.sonic_tacacs_server:
        config:
          auth_type: login
          key: login
          source_interface: Ethernet 12
          timeout: 10
          servers:
            host:
              - name: 1.2.3.4
        state: deleted

    # After state:
    # ------------
    #
    # do show tacacs-server
    # ---------------------------------------------------------
    # TACACS Global Configuration
    # ---------------------------------------------------------
    # timeout    : 5
    # auth-type  : pap
    # ------------------------------------------------------------------------------------------------
    # HOST                 AUTH-TYPE       KEY        PORT       PRIORITY   TIMEOUT    VRF
    # ------------------------------------------------------------------------------------------------
    # localhost            pap                        49         1          5          default


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # do show tacacs-server
    # ---------------------------------------------------------
    # TACACS Global Configuration
    # ---------------------------------------------------------
    # source-interface  : Ethernet12
    # timeout    : 10
    # auth-type  : login
    # key        : login
    # ------------------------------------------------------------------------------------------------
    # HOST                 AUTH-TYPE       KEY        PORT       PRIORITY   TIMEOUT    VRF
    # ------------------------------------------------------------------------------------------------
    # 1.2.3.4              pap             *****      50         2          10         mgmt
    # localhost            pap                        49         1          5          default
    #

    - name: Merge tacacs configurations
      dellemc.enterprise_sonic.sonic_tacacs_server:
        config:
        state: deleted

    # After state:
    # ------------
    #
    # do show tacacs-server
    # ---------------------------------------------------------
    # TACACS Global Configuration
    # ---------------------------------------------------------
    # timeout    : 5
    # auth-type  : pap


    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic(config)# do show tacacs-server
    # ---------------------------------------------------------
    # TACACS Global Configuration
    # ---------------------------------------------------------
    #
    - name: Merge tacacs configurations
      dellemc.enterprise_sonic.sonic_tacacs_server:
        config:
          auth_type: pap
          key: pap
          source_interface: Ethernet 12
          timeout: 10
          servers:
            host:
              - name: 1.2.3.4
                auth_type: pap
                key: 1234
        state: merged

    # After state:
    # ------------
    #
    # sonic(config)# do show tacacs-server
    # ---------------------------------------------------------
    # TACACS Global Configuration
    # ---------------------------------------------------------
    # source-interface  : Ethernet12
    # timeout    : 10
    # auth-type  : pap
    # key        : pap
    # ------------------------------------------------------------------------------------------------
    # HOST                 AUTH-TYPE       KEY        PORT       PRIORITY   TIMEOUT    VRF
    # ------------------------------------------------------------------------------------------------
    # 1.2.3.4              pap             1234       49         1          5          default
    #
    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic(config)# do show tacacs-server
    # ---------------------------------------------------------
    # TACACS Global Configuration
    # ---------------------------------------------------------
    # source-interface  : Ethernet12
    # timeout           : 10
    # auth-type         : pap
    # key configured    : Yes
    # --------------------------------------------------------------------------------------
    # HOST                 AUTH-TYPE    KEY-CONFIG PORT       PRIORITY   TIMEOUT    VRF
    # --------------------------------------------------------------------------------------
    # 1.2.3.4              pap          No         49         1          5          default
    #
    - name: Replace tacacs configurations
      sonic_tacacs_server:
        config:
          auth_type: pap
          key: pap
          source_interface: Ethernet12
          timeout: 10
          servers:
            - host:
                name: 1.2.3.4
                auth_type: mschap
                key: 1234
        state: replaced
    #
    # After state:
    # ------------
    #
    # sonic(config)# do show tacacs-server
    # ---------------------------------------------------------
    # TACACS Global Configuration
    # ---------------------------------------------------------
    # source-interface  : Ethernet12
    # timeout           : 10
    # auth-type         : pap
    # key configured    : Yes
    # --------------------------------------------------------------------------------------
    # HOST                 AUTH-TYPE    KEY-CONFIG PORT       PRIORITY   TIMEOUT    VRF
    # --------------------------------------------------------------------------------------
    # 1.2.3.4              mschap       Yes        49         1          5          default
    #
    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic(config)# do show tacacs-server
    # ---------------------------------------------------------
    # TACACS Global Configuration
    # ---------------------------------------------------------
    # source-interface  : Ethernet12
    # timeout           : 10
    # auth-type         : pap
    # key configured    : Yes
    # --------------------------------------------------------------------------------------
    # HOST                 AUTH-TYPE    KEY-CONFIG PORT       PRIORITY   TIMEOUT    VRF
    # --------------------------------------------------------------------------------------
    # 1.2.3.4              pap          No         49         1          5          default
    # 11.12.13.14          chap         Yes        49         10         5          default
    #
    - name: Override tacacs configurations
      sonic_tacacs_server:
        config:
          auth_type: mschap
          key: mschap
          source_interface: Ethernet12
          timeout: 20
          servers:
            - host:
                name: 1.2.3.4
                auth_type: mschap
                key: mschap
            - host:
                name: 10.10.11.12
                auth_type: chap
                timeout: 30
                priority: 2
        state: overridden
    #
    # After state:
    # ------------
    #
    # sonic(config)# do show tacacs-server
    # ---------------------------------------------------------
    # TACACS Global Configuration
    # ---------------------------------------------------------
    # source-interface  : Ethernet12
    # timeout           : 20
    # auth-type         : mschap
    # key configured    : Yes
    # --------------------------------------------------------------------------------------
    # HOST                 AUTH-TYPE    KEY-CONFIG PORT       PRIORITY   TIMEOUT    VRF
    # --------------------------------------------------------------------------------------
    # 1.2.3.4              mschap       Yes        49         1          5          default
    # 10.10.11.12          chap         No         49         2          30         default
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

- Niraimadaiselvam M (@niraimadaiselvamm)
