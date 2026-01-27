.. _dellemc.enterprise_sonic.sonic_ntp_module:


**********************************
dellemc.enterprise_sonic.sonic_ntp
**********************************

**Manage NTP configuration on SONiC.**


Version added: 2.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of NTP for devices running SONiC.




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
                        <div>Specifies NTP related configurations.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>enable_ntp_auth</b>
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
                        <div>Enable or disable NTP authentication.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ntp_keys</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of NTP authentication keys.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>encrypted</b>
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
                        <div>NTP authentication key_value is encrypted.</div>
                        <div>encrypted can not be deleted.</div>
                        <div>When &quot;state&quot; is &quot;merged&quot;, &quot;encrypted&quot; is required.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>key_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>NTP authentication key identifier.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>key_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>NTP_AUTH_SHA1</li>
                                    <li>NTP_AUTH_MD5</li>
                                    <li>NTP_AUTH_SHA2_256</li>
                        </ul>
                </td>
                <td>
                        <div>NTP authentication key type.</div>
                        <div>key_type can not be deleted.</div>
                        <div>When &quot;state&quot; is &quot;merged&quot;, &quot;key_type&quot; is required.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>key_value</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>NTP authentication key value.</div>
                        <div>key_value can not be deleted.</div>
                        <div>When &quot;state&quot; is &quot;merged&quot;, &quot;key_value&quot; is required.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>servers</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of NTP servers.</div>
                        <div>minpoll and maxpoll are required to be configured together.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IPv4/IPv6 address or host name of NTP server.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>key_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>NTP authentication key used by server.</div>
                        <div>Key_id can not be deleted.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>maxpoll</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Maximum poll interval to poll NTP server.</div>
                        <div>maxpoll can not be deleted.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>minpoll</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Minimum poll interval to poll NTP server.</div>
                        <div>minpoll can not be deleted.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>prefer</b>
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
                        <div>Indicates whether this server should be preferred.</div>
                        <div>prefer can not be deleted.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>source_interfaces</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of names of NTP source interfaces.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>trusted_keys</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of trusted NTP authentication keys.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>VRF name on which NTP is enabled.</div>
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
    # sonic# show ntp server
    # ----------------------------------------------------------------------------
    # NTP Servers                     minpoll maxpoll Prefer Authentication key ID
    # ----------------------------------------------------------------------------
    # 10.11.0.1                       6       10      False
    # 10.11.0.2                       5       9       False
    # dell.com                        6       9       False
    # dell.org                        7       10      True
    #
    - name: Delete NTP server configuration
      sonic_ntp:
        config:
          servers:
            - address: 10.11.0.2
            - address: dell.org
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show ntp server
    # ----------------------------------------------------------------------------
    # NTP Servers                     minpoll maxpoll Prefer Authentication key ID
    # ----------------------------------------------------------------------------
    # 10.11.0.1                       6       10      False
    # dell.com                        6       9       False
    #
    #
    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show ntp global
    # ----------------------------------------------
    # NTP Global Configuration
    # ----------------------------------------------
    # NTP source-interfaces:  Ethernet0, Ethernet4, Ethernet8, Ethernet16
    #
    - name: Delete NTP source-interface configuration
      sonic_ntp:
        config:
          source_interfaces:
            - Ethernet8
            - Ethernet16
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show ntp global
    # ----------------------------------------------
    # NTP Global Configuration
    # ----------------------------------------------
    # NTP source-interfaces:  Ethernet0, Ethernet4
    #
    #
    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration | grep ntp
    # ntp authentication-key 8 sha1 U2FsdGVkX1/NpJrdOeyMeUHEkSohY6azY9VwbAqXRTY= encrypted
    # ntp authentication-key 10 md5 U2FsdGVkX1/Gxds/5pscCvIKbVngGaKka4SQineS51Y= encrypted
    # ntp authentication-key 20 sha2-256 U2FsdGVkX1/eAzKj1teKhYWD7tnzOsYOijGeFAT0rKM= encrypted
    #
    - name: Delete NTP key configuration
      sonic_ntp:
        config:
          ntp_keys:
            - key_id: 10
            - key_id: 20
        state: deleted
    #
    # After state:
    # ------------
    #
    # sonic# show running-configuration | grep ntp
    # ntp authentication-key 8 sha1 U2FsdGVkX1/NpJrdOeyMeUHEkSohY6azY9VwbAqXRTY= encrypted
    #
    #
    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show ntp server
    # ----------------------------------------------------------------------------
    # NTP Servers                     minpoll maxpoll Prefer Authentication key ID
    # ----------------------------------------------------------------------------
    # 10.11.0.1                       6       10      False
    # dell.com                        6       9       False
    #
    - name: Merge NTP server configuration
      sonic_ntp:
        config:
          servers:
            - address: 10.11.0.2
              minpoll: 5
            - address: dell.org
              minpoll: 7
              maxpoll: 10
              prefer: true
        state: merged

    # After state:
    # ------------
    #
    # sonic# show ntp server
    # ----------------------------------------------------------------------------
    # NTP Servers                     minpoll maxpoll Prefer Authentication key ID
    # ----------------------------------------------------------------------------
    # 10.11.0.1                       6       10      Flase
    # 10.11.0.2                       5       10      Flase
    # dell.com                        6       9       Flase
    # dell.org                        7       10      True
    #
    #
    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show ntp global
    # ----------------------------------------------
    # NTP Global Configuration
    # ----------------------------------------------
    # NTP source-interfaces:  Ethernet0, Ethernet4
    #
    - name: Merge NTP source-interface configuration
      sonic_ntp:
        config:
          source_interfaces:
            - Ethernet8
            - Ethernet16
        state: merged

    # After state:
    # ------------
    #
    # sonic# show ntp global
    # ----------------------------------------------
    # NTP Global Configuration
    # ----------------------------------------------
    # NTP source-interfaces:  Ethernet0, Ethernet4, Ethernet8, Ethernet16
    #
    #
    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration | grep ntp
    # ntp authentication-key 8 sha1 U2FsdGVkX1/NpJrdOeyMeUHEkSohY6azY9VwbAqXRTY= encrypted
    #
    - name: Merge NTP key configuration
      sonic_ntp:
        config:
          ntp_keys:
            - key_id: 10
              key_type: NTP_AUTH_MD5
              key_value: dellemc10
              encrypted: false
            - key_id: 20
              key_type: NTP_AUTH_SHA2_256
              key_value: dellemc20
              encrypted: false
        state: merged
    #
    # After state:
    # ------------
    #
    # sonic# show running-configuration | grep ntp
    # ntp authentication-key 8 sha1 U2FsdGVkX1/NpJrdOeyMeUHEkSohY6azY9VwbAqXRTY= encrypted
    # ntp authentication-key 10 md5 U2FsdGVkX1/Gxds/5pscCvIKbVngGaKka4SQineS51Y= encrypted
    # ntp authentication-key 20 sha2-256 U2FsdGVkX1/eAzKj1teKhYWD7tnzOsYOijGeFAT0rKM= encrypted
    #
    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show ntp server
    # ----------------------------------------------------------------------------
    # NTP Servers                     minpoll maxpoll Prefer Authentication key ID
    # ----------------------------------------------------------------------------
    # 10.11.0.1                       6       10      False
    # dell.com                        6       9       False
    #
    - name: Replace NTP server configuration
      sonic_ntp:
        config:
          servers:
            - address: 10.11.0.2
              minpoll: 5
              maxpoll: 9
            - address: dell.com
              minpoll: 7
              maxpoll: 10
              prefer: true
        state: replaced
    #
    # After state:
    # ------------
    #
    # sonic# show ntp server
    # ----------------------------------------------------------------------------
    # NTP Servers                     minpoll maxpoll Prefer Authentication key ID
    # ----------------------------------------------------------------------------
    # 10.11.0.1                       6       10      False
    # 10.11.0.2                       5       9       False
    # dell.com                        7       10      True
    #
    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show ntp server
    # ----------------------------------------------------------------------------
    # NTP Servers                     minpoll maxpoll Prefer Authentication key ID
    # ----------------------------------------------------------------------------
    # 10.11.0.1                       6       10      False
    # dell.com                        6       9       False
    #
    # sonic# show ntp global
    # ----------------------------------------------
    # NTP Global Configuration
    # ----------------------------------------------
    # NTP source-interfaces:  Ethernet0, Ethernet4
    #
    - name: Overridden NTP configuration
      sonic_ntp:
        config:
          servers:
            - address: 10.11.0.2
              minpoll: 5
            - address: dell.com
              minpoll: 7
              maxpoll: 10
              prefer: true
        state: overridden
    #
    # After state:
    # ------------
    #
    # After state:
    # ------------
    #
    # sonic# show ntp server
    # ----------------------------------------------------------------------------
    # NTP Servers                     minpoll maxpoll Prefer Authentication key ID
    # ----------------------------------------------------------------------------
    # 10.11.0.2                       5       10      False
    # dell.com                        7       10      True
    #
    # sonic# show ntp global
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

- M. Zhang (@mingjunzhang2019)
