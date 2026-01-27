.. _dellemc.enterprise_sonic.sonic_aaa_module:


**********************************
dellemc.enterprise_sonic.sonic_aaa
**********************************

**Manage AAA configuration on SONiC**


Version added: 1.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of AAA for devices running SONiC.




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
                        <div>AAA configuration</div>
                        <div>For all lists in the module, the list items should be specified in order of desired priority.</div>
                        <div>List items specified first have the highest priority.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>accounting</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 4.0.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>AAA accounting configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>commands_accounting</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>AAA commands accounting configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>accounting_console_exempt</b>
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
                        <div>Exempt accounting of events from console.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>accounting_method</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>tacacs+</li>
                                    <li>logging</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the methods in which to perform accounting.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>accounting_record_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>start-stop</li>
                                    <li>stop-only</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the type of record to be sent to the accounting server.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>session_accounting</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>AAA session accounting configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>accounting_console_exempt</b>
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
                        <div>Exempt accounting of events from console.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>accounting_method</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>tacacs+</li>
                                    <li>logging</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the methods in which to perform accounting.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>accounting_record_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>start-stop</li>
                                    <li>stop-only</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the type of record to be sent to the accounting server.</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>authentication</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.0.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>AAA authentication configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>auth_method</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ldap</li>
                                    <li>local</li>
                                    <li>radius</li>
                                    <li>tacacs+</li>
                                    <li>cac-piv</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the order of the methods in which to authenticate login</div>
                        <div>Any 1 choice may be specified or 2 choices consisting of local and another group may be specified</div>
                        <div><code>cac-piv</code> option is only available in devices running sonic 4.5.0 and above.</div>
                        <div>MFA is not applicable when <code>cac-piv</code> is configured as first factor for authentication.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>console_auth_local</b>
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
                        <div>Enable/disable local authentication on console</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>failthrough</b>
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
                        <div>Enable/disable failthrough</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>login_mfa_console</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.1.0</div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Enable/disable MFA method for console access.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mfa_auth_method</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.1.0</div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>rsa-securid</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies RSA SecurID as multi-factor authentication method.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>authorization</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.0.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>AAA authorization configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>commands_auth_method</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>local</li>
                                    <li>tacacs+</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the order of the methods in which to authorize commands</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>login_auth_method</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ldap</li>
                                    <li>local</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the order of the methods in which to authorize login</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name_service</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.0.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>AAA name-service configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>group</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ldap</li>
                                    <li>local</li>
                                    <li>login</li>
                        </ul>
                </td>
                <td>
                        <div>Name-service source for group method</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>netgroup</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ldap</li>
                                    <li>local</li>
                        </ul>
                </td>
                <td>
                        <div>Name-service source for netgroup method</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>passwd</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ldap</li>
                                    <li>local</li>
                                    <li>login</li>
                        </ul>
                </td>
                <td>
                        <div>Name-service source for passwd method</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>shadow</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ldap</li>
                                    <li>local</li>
                                    <li>login</li>
                        </ul>
                </td>
                <td>
                        <div>Name-service source for shadow method</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>sudoers</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ldap</li>
                                    <li>local</li>
                        </ul>
                </td>
                <td>
                        <div>Name-service source for sudoers method</div>
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
                                    <li>overridden</li>
                                    <li>replaced</li>
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
    # sonic# show aaa
    # (No AAA configuration present)
    #
    # sonic# show mfa
    # ---------------------------------------------------------
    # Multi-factor Authentication Information
    # ---------------------------------------------------------
    # MFA Authentication             : None
    # Console Exempted               : None
    # MFA Service Security Profile   : None
    # RSA SecurID Security Profile   : None

    - name: Merge AAA configuration
      dellemc.enterprise_sonic.sonic_aaa:
        config:
          authentication:
            auth_method:
              - local
              - ldap
            console_auth_local: true
            failthrough: true
            mfa_auth_method: 'rsa-securid'
            login_mfa_console: true
          authorization:
            commands_auth_method:
              - local
              - tacacs+
            login_auth_method:
              - local
              - ldap
          accounting:
            commands_accounting:
              accounting_method:
                - tacacs+
                - logging
              accounting_record_type: 'start-stop'
              accounting_console_exempt: true
            session_accounting:
              accounting_method:
                - logging
              accounting_record_type: 'stop-only'
              accounting_console_exempt: true
          name_service:
            group:
              - ldap
            netgroup:
              - local
            passwd:
              - login
            shadow:
              - ldap
            sudoers:
              - local
        state: merged

    # After state:
    # ------------
    #
    # sonic# show aaa
    # ---------------------------------------------------------
    # AAA Authentication Information
    # ---------------------------------------------------------
    # failthrough  : True
    # login-method : local, ldap
    # login-mfa    : rsa-securid
    # console authentication  : local
    # ---------------------------------------------------------
    # AAA Authorization Information
    # ---------------------------------------------------------
    # login        : local, ldap
    # commands     : local, tacacs+
    # ---------------------------------------------------------
    # AAA Accounting Information
    # ---------------------------------------------------------
    # commands   : tacacs+, logging (start-stop, console-disabled)
    # session    : logging (stop-only, console-disabled)
    # ---------------------------------------------------------
    # AAA Name-Service Information
    # ---------------------------------------------------------
    # group-method    : ldap
    # netgroup-method : local
    # passwd-method   : login
    # shadow-method   : ldap
    # sudoers-method  : local
    #
    # sonic# show mfa
    # ---------------------------------------------------------
    # Multi-factor Authentication Information
    # ---------------------------------------------------------
    # MFA Authentication             : rsa-securid
    # Console Exempted               : No
    # MFA Service Security Profile   : None
    # RSA SecurID Security Profile   : None


    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show aaa
    # ---------------------------------------------------------
    # AAA Authentication Information
    # ---------------------------------------------------------
    # failthrough  : True
    # login-method : local, ldap
    # login-mfa    : rsa-securid
    # console authentication  : local
    # ---------------------------------------------------------
    # AAA Authorization Information
    # ---------------------------------------------------------
    # login        : local, ldap
    # commands     : local, tacacs+
    # ---------------------------------------------------------
    # AAA Accounting Information
    # ---------------------------------------------------------
    # commands   : tacacs+, logging (start-stop, console-disabled)
    # session    : logging (stop-only, console-disabled)
    # ---------------------------------------------------------
    # AAA Name-Service Information
    # ---------------------------------------------------------
    # group-method    : ldap
    # netgroup-method : local
    # passwd-method   : login
    # shadow-method   : ldap
    # sudoers-method  : local
    #
    # sonic# show mfa
    # ---------------------------------------------------------
    # Multi-factor Authentication Information
    # ---------------------------------------------------------
    # MFA Authentication             : rsa-securid
    # Console Exempted               : No
    # MFA Service Security Profile   : None
    # RSA SecurID Security Profile   : None

    - name: Replace AAA configuration
      dellemc.enterprise_sonic.sonic_aaa:
        config:
          authentication:
            auth_method:
              - cac-piv
              - local
            console_auth_local: true
            failthrough: false
          authorization:
            commands_auth_method:
              - local
          accounting:
            commands_accounting:
              accounting_method:
                - tacacs+
            session_accounting:
              accounting_record_type: 'start-stop'
          name_service:
            group:
              - ldap
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show aaa
    # ---------------------------------------------------------
    # AAA Authentication Information
    # ---------------------------------------------------------
    # failthrough  : False
    # login-method : cac-piv, local
    # login-mfa    : None
    # console authentication  : local
    # ---------------------------------------------------------
    # AAA Authorization Information
    # ---------------------------------------------------------
    # login        : local
    # ---------------------------------------------------------
    # AAA Accounting Information
    # ---------------------------------------------------------
    # commands   : tacacs+ (start-stop, console-disabled)
    # session    : logging (start-stop, console-disabled)
    # ---------------------------------------------------------
    # AAA Name-Service Information
    # ---------------------------------------------------------
    # group-method    : ldap
    #
    # sonic# show mfa
    # ---------------------------------------------------------
    # Multi-factor Authentication Information
    # ---------------------------------------------------------
    # MFA Authentication             : None
    # Console Exempted               : None
    # MFA Service Security Profile   : None
    # RSA SecurID Security Profile   : None


    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show aaa
    # ---------------------------------------------------------
    # AAA Authentication Information
    # ---------------------------------------------------------
    # failthrough  : True
    # login-method : local, ldap
    # login-mfa    : rsa-securid
    # console authentication  : local
    # ---------------------------------------------------------
    # AAA Authorization Information
    # ---------------------------------------------------------
    # login        : local, ldap
    # commands     : local, tacacs+
    # ---------------------------------------------------------
    # AAA Accounting Information
    # ---------------------------------------------------------
    # commands   : tacacs+ (start-stop, console-disabled)
    # session    : logging (start-stop, console-disabled)
    # ---------------------------------------------------------
    # AAA Name-Service Information
    # ---------------------------------------------------------
    # group-method    : ldap
    # netgroup-method : local
    # passwd-method   : login
    # shadow-method   : ldap
    # sudoers-method  : local
    #
    # sonic# show mfa
    # ---------------------------------------------------------
    # Multi-factor Authentication Information
    # ---------------------------------------------------------
    # MFA Authentication             : rsa-securid
    # Console Exempted               : Yes
    # MFA Service Security Profile   : None
    # RSA SecurID Security Profile   : None

    - name: Override AAA configuration
      dellemc.enterprise_sonic.sonic_aaa:
        config:
          authentication:
            auth_method:
              - tacacs+
            console_auth_local: true
            failthrough: true
            mfa_auth_method: 'rsa-securid'
            login_mfa_console: true
          accounting:
            commands_accounting:
              accounting_method:
                - tacacs+
                - logging
              accounting_record_type: 'stop-only'
              accounting_console_exempt: true
            session_accounting:
              accounting_method:
                - logging
              accounting_record_type: 'stop-only'
              accounting_console_exempt: true
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show aaa
    # ---------------------------------------------------------
    # AAA Authentication Information
    # ---------------------------------------------------------
    # failthrough  : True
    # login-method : tacacs+
    # login-mfa    : rsa-securid
    # console authentication  : local
    #
    # sonic# show mfa
    # ---------------------------------------------------------
    # Multi-factor Authentication Information
    # ---------------------------------------------------------
    # MFA Authentication             : rsa-securid
    # Console Exempted               : No
    # MFA Service Security Profile   : None
    # RSA SecurID Security Profile   : None
    # ---------------------------------------------------------
    # AAA Accounting Information
    # ---------------------------------------------------------
    # commands   : tacacs+, logging (stop-only, console-disabled)
    # session    : logging (stop-only, console-disabled)

    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show aaa
    # ---------------------------------------------------------
    # AAA Authentication Information
    # ---------------------------------------------------------
    # failthrough  : True
    # login-method : local, ldap
    # login-mfa    : rsa-securid
    # console authentication  : local
    # ---------------------------------------------------------
    # AAA Authorization Information
    # ---------------------------------------------------------
    # login        : local, ldap
    # commands     : local, tacacs+
    # ---------------------------------------------------------
    # AAA Accounting Information
    # ---------------------------------------------------------
    # commands   : tacacs+, logging (stop-only, console-disabled)
    # session    : logging (stop-only, console-disabled)
    # ---------------------------------------------------------
    # AAA Name-Service Information
    # ---------------------------------------------------------
    # group-method    : ldap
    # netgroup-method : local
    # passwd-method   : login
    # shadow-method   : ldap
    # sudoers-method  : local
    #
    # sonic# show mfa
    # ---------------------------------------------------------
    # Multi-factor Authentication Information
    # ---------------------------------------------------------
    # MFA Authentication             : rsa-securid
    # Console Exempted               : No
    # MFA Service Security Profile   : None
    # RSA SecurID Security Profile   : None

    - name: Delete AAA individual attributes
      dellemc.enterprise_sonic.sonic_aaa:
        config:
          authentication:
            auth_method:
              - local
              - ldap
            console_auth_local: true
            failthrough: true
            mfa_auth_method: 'rsa-securid'
            login_mfa_console: true
          authorization:
            commands_auth_method:
              - local
              - tacacs+
            login_auth_method:
              - local
              - ldap
          accounting:
            commands_accounting:
              accounting_method:
                - tacacs+
                - logging
              accounting_record_type: 'stop-only'
              accounting_console_exempt: true
            session_accounting:
              accounting_method:
                - logging
              accounting_record_type: 'stop-only'
              accounting_console_exempt: true
          name_service:
            group:
              - ldap
            netgroup:
              - local
            passwd:
              - login
            shadow:
              - ldap
            sudoers:
              - local
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show aaa
    # (No AAA configuration present)
    #
    # sonic# show mfa
    # ---------------------------------------------------------
    # Multi-factor Authentication Information
    # ---------------------------------------------------------
    # MFA Authentication             : None
    # Console Exempted               : None
    # MFA Service Security Profile   : None
    # RSA SecurID Security Profile   : None


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show aaa
    # ---------------------------------------------------------
    # AAA Authentication Information
    # ---------------------------------------------------------
    # failthrough  : True
    # login-method : local, ldap
    # login-mfa    : rsa-securid
    # console authentication  : local
    # ---------------------------------------------------------
    # AAA Authorization Information
    # ---------------------------------------------------------
    # login        : local, ldap
    # commands     : local, tacacs+
    # ---------------------------------------------------------
    # AAA Accounting Information
    # ---------------------------------------------------------
    # commands   : tacacs+, logging (stop-only, console-disabled)
    # session    : logging (stop-only, console-disabled)
    # ---------------------------------------------------------
    # AAA Name-Service Information
    # ---------------------------------------------------------
    # group-method    : ldap
    # netgroup-method : local
    # passwd-method   : login
    # shadow-method   : ldap
    # sudoers-method  : local
    #
    # sonic# show mfa
    # ---------------------------------------------------------
    # Multi-factor Authentication Information
    # ---------------------------------------------------------
    # MFA Authentication             : rsa-securid
    # Console Exempted               : Yes
    # MFA Service Security Profile   : None
    # RSA SecurID Security Profile   : None

    - name: Delete all AAA configuration
      dellemc.enterprise_sonic.sonic_aaa:
        config: {}
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show aaa
    # (No AAA configuration present)
    #
    # sonic# show mfa
    # ---------------------------------------------------------
    # Multi-factor Authentication Information
    # ---------------------------------------------------------
    # MFA Authentication             : None
    # Console Exempted               : None
    # MFA Service Security Profile   : None
    # RSA SecurID Security Profile   : None



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
                            <div>The generated configuration module invocation.</div>
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

- S\. Talabi (@stalabi1)
