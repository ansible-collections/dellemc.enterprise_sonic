.. _dellemc.enterprise_sonic.sonic_ssh_module:


**********************************
dellemc.enterprise_sonic.sonic_ssh
**********************************

**Manage SSH configurations on SONiC**


Version added: 3.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides SSH configuration management to specify the algorithms used for SSH connection in devices running SONiC.




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
                        <div>SSH clients and servers use the following configurations for SSH connections.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>client</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>SSH client configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>cipher</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Cipher algorithm used in SSH connection for encryption. When configured, this value is used by SSH clients which communicate with the server.</div>
                        <div>Specify as a comma separated list.</div>
                        <div>Options are aes128-ctr, aes192-ctr, aes256-ctr</div>
                        <div>chacha20-poly1305@openssh.com, aes128-gcm@openssh.com</div>
                        <div>and aes256-gcm@openssh.com</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>kex</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>KEX algorithm used in SSH connection for key exchange. When configured, this value is used by SSH clients which communicate with the server.</div>
                        <div>Specify as a comma separated list.</div>
                        <div>Options are curve25519-sha256, curve25519-sha256@libssh.org</div>
                        <div>ecdh-sha2-nistp256, ecdh-sha2-nistp384, ecdh-sha2-nistp521,</div>
                        <div>diffie-hellman-group-exchange-sha256,</div>
                        <div>diffie-hellman-group16-sha512,</div>
                        <div>diffie-hellman-group18-sha512 and</div>
                        <div>diffie-hellman-group14-sha256</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mac</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>MAC algorithm used in SSH connection for generating and verifying Message Authentication Codes. When configured, this value is used by SSH clients which communicate with the server.</div>
                        <div>Specify as a comma separated list.</div>
                        <div>Options are umac-128-etm@openssh.com,</div>
                        <div>hmac-sha2-256-etm@openssh.com,</div>
                        <div>hmac-sha2-512-etm@openssh.com, umac-128@openssh.com,</div>
                        <div>hmac-sha2-256 and hmac-sha2-512</div>
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
                        <div>The state specifies the type of configuration update to be performed on the device.</div>
                        <div>If the state is &quot;merged&quot;, merge specified attributes with existing configured attributes.</div>
                        <div>For &quot;deleted&quot;, delete the specified attributes from existing configuration.</div>
                        <div>For &quot;replaced&quot;, replace on-device SSH configuration with the specified configuration.</div>
                        <div>For &quot;overridden&quot;, override on-device SSH configurations with the specified configuration.</div>
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
    # sonic# show running-configuration | grep "ip ssh client"
    # ip ssh client ciphers aes192-ctr,chacha20-poly1305@openssh.com
    # ip ssh client macs umac-128-etm@openssh.com,hmac-sha2-256-etm@openssh.com
    # ip ssh client kexalgorithms curve25519-sha256,diffie-hellman-group16-sha512
    # sonic#

    - name: Delete specified SSH configurations
      dellemc.enterprise_sonic.sonic_ssh:
        config:
          client:
            cipher: 'aes192-ctr,chacha20-poly1305@openssh.com'
            mac: 'umac-128-etm@openssh.com,hmac-sha2-256-etm@openssh.com'
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration | grep "ip ssh client"
    # ip ssh client kexalgorithms curve25519-sha256,diffie-hellman-group16-sha512
    # sonic#


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration | grep "ip ssh client"
    # ip ssh client ciphers aes192-ctr,chacha20-poly1305@openssh.com
    # ip ssh client kexalgorithms curve25519-sha256,diffie-hellman-group16-sha512
    # ip ssh client macs umac-128-etm@openssh.com,hmac-sha2-256-etm@openssh.com
    # sonic#

    - name: Delete all SSH configurations
      dellemc.enterprise_sonic.sonic_ssh:
        config:
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration | grep "ip ssh client"
    # (No "ip ssh client" configuration present)
    # sonic#


    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration | grep "ip ssh client"
    # sonic
    # (No "ip ssh client" configuration present)

    - name: Modify SSH configurations
      dellemc.enterprise_sonic.sonic_ssh:
        config:
          client:
            cipher: 'aes192-ctr,chacha20-poly1305@openssh.com'
            mac: 'umac-128-etm@openssh.com,hmac-sha2-256-etm@openssh.com'
            kex: 'curve25519-sha256,diffie-hellman-group16-sha512'
        state: merged

    # After state:
    # ------------
    #
    # sonic# show running-configuration | grep "ip ssh client"
    # ip ssh client ciphers aes192-ctr,chacha20-poly1305@openssh.com
    # ip ssh client kexalgorithms curve25519-sha256,diffie-hellman-group16-sha512
    # ip ssh client macs umac-128-etm@openssh.com,hmac-sha2-256-etm@openssh.com
    # sonic#


    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration | grep "ip ssh client"
    # ip ssh client ciphers aes192-ctr,chacha20-poly1305@openssh.com
    # ip ssh client kexalgorithms curve25519-sha256,diffie-hellman-group16-sha512
    # ip ssh client macs umac-128-etm@openssh.com,hmac-sha2-256-etm@openssh.com
    # sonic#

    - name: Modify SSH configurations
      dellemc.enterprise_sonic.sonic_ssh:
        config:
          client:
            cipher: 'aes256-ctr'
            kex: 'curve25519-sha256,diffie-hellman-group16-sha512'
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show running-configuration | grep "ip ssh client"
    # ip ssh client ciphers aes256-ctr
    # ip ssh client kexalgorithms curve25519-sha256,diffie-hellman-group16-sha512
    # sonic#


    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration | grep "ip ssh client"
    # ip ssh client ciphers aes192-ctr,chacha20-poly1305@openssh.com
    # ip ssh client kexalgorithms curve25519-sha256,diffie-hellman-group16-sha512
    # ip ssh client macs umac-128-etm@openssh.com,hmac-sha2-256-etm@openssh.com
    # sonic#

    - name: Modify SSH configurations
      dellemc.enterprise_sonic.sonic_ssh:
        config:
          client:
            cipher: 'aes256-ctr'
            mac: 'umac-128-etm@openssh.com,hmac-sha2-256-etm@openssh.com'
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show running-configuration | grep "ip ssh client"
    # ip ssh client ciphers aes256-ctr
    # ip ssh client macs umac-128-etm@openssh.com,hmac-sha2-256-etm@openssh.com
    # sonic#



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
                            <div>The resulting configuration model invocation.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format
     as the parameters above.</div>
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
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The configuration prior to the model invocation.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format
     as the parameters above.</div>
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

- Balasubramaniam Koundappa(@balasubramaniam-k)
