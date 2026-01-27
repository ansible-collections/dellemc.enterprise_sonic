.. _dellemc.enterprise_sonic.sonic_mgmt_servers_module:


*******************************************
dellemc.enterprise_sonic.sonic_mgmt_servers
*******************************************

**Manage management servers configuration on SONiC**


Version added: 2.5.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of management servers for devices running SONiC




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
                        <div>Management servers configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>rest</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>REST server configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>api_timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">900</div>
                </td>
                <td>
                        <div>Maximum time in seconds the REST server will wait for a REST API request-response cycle to complete</div>
                        <div>Range 0-4294967295</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>cipher_suite</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.1.0</div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">"ecdhe-ecdsa-with-aes-256-gcm-SHA384,ecdhe-ecdsa-with-chacha20-poly1305-SHA256,ecdhe-ecdsa-with-aes-128-gcm-SHA256"</div>
                </td>
                <td>
                        <div>Cipher suites used for TLS connection with the clients</div>
                        <div>Specify as a comma separated list. Options are ecdhe-ecdsa-with-aes-256-gcm-SHA384, ecdhe-ecdsa-with-chacha20-poly1305-SHA256 and ecdhe-ecdsa-with-aes-128-gcm-SHA256.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>client_auth</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">"password,jwt"</div>
                </td>
                <td>
                        <div>Client authentication methods list</div>
                        <div>Specify as a comma separated list. Options for list are password, jwt, cert, and none.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>log_level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">0</div>
                </td>
                <td>
                        <div>Log level of REST server, range 0-255</div>
                </td>
            </tr>
            <tr>
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
                        <b>Default:</b><br/><div style="color: blue">443</div>
                </td>
                <td>
                        <div>Port that the REST server listens on, range 0-65535</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>read_timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">15</div>
                </td>
                <td>
                        <div>Maximum time in seconds the REST server will wait for an HTTP request-response cycle to complete</div>
                        <div>Range 0-4294967295</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>req_limit</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Maximum number of concurrent requests that the client can make to the REST server</div>
                        <div>Range 0-4294967295</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>security_profile</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of security profile</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>shutdown</b>
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
                        <div>Enables/disables REST server from listening on the port</div>
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
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>mgmt</li>
                        </ul>
                </td>
                <td>
                        <div>Name of VRF</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>telemetry</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Telemetry server configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>api_timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">0</div>
                </td>
                <td>
                        <div>Maximum time in seconds the telemetry server will wait for a gNMI request-response cycle to complete</div>
                        <div>Range 0-4294967295</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>client_auth</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">"password,jwt"</div>
                </td>
                <td>
                        <div>Client authentication methods list</div>
                        <div>Specify as a comma separated list. Options for list are password, jwt, cert, and none.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>jwt_refresh</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">900</div>
                </td>
                <td>
                        <div>Duration of time in seconds before JWT expires and can be refreshed</div>
                        <div>Range 0-4294967295</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>jwt_valid</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">3600</div>
                </td>
                <td>
                        <div>Duration of time in seconds for which JWT is valid on the telemetry server</div>
                        <div>Range 0-4294967295</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>log_level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">0</div>
                </td>
                <td>
                        <div>Log level of telemetry server, range 0-255</div>
                </td>
            </tr>
            <tr>
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
                        <b>Default:</b><br/><div style="color: blue">8080</div>
                </td>
                <td>
                        <div>Port that the telemetry server listens on, range 0-65535</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>security_profile</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of security profile</div>
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
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>mgmt</li>
                        </ul>
                </td>
                <td>
                        <div>Name of VRF</div>
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
    # sonic# show ip rest
    #
    # Log level is 0
    # Port is 443
    # Request limit is not-set
    # Read timeout is 15 seconds
    # Client authentication mode is password,jwt
    # Security profile is not-set
    # API timeout is 900 seconds
    # vrf is not-set
    # Cipher suite is ecdhe-ecdsa-with-aes-256-gcm-SHA384,ecdhe-ecdsa-with-chacha20-poly1305-SHA256,ecdhe-ecdsa-with-aes-128-gcm-SHA256
    #
    # sonic# show ip telemetry
    #
    # Log level is 0
    # JWT valid is 3600 seconds
    # JWT refresh is 900 seconds
    # Port is 8080
    # Client authentication mode is password,jwt
    # Security profile is not-set
    # API timeout is 0 seconds
    # vrf is not-set

    - name: Merge mgmt servers configuration
      dellemc.enterprise_sonic.sonic_mgmt_servers:
        config:
          rest:
            api_timeout: 120
            client_auth: password
            log_level: 6
            port: 443
            read_timeout: 60
            req_limit: 100
            security_profile: profile1
            shutdown: true
            vrf: mgmt
            cipher_suite: ecdhe-ecdsa-with-aes-256-gcm-SHA384
          telemetry:
            api_timeout: 45
            client_auth: cert,jwt
            jwt_refresh: 80
            jwt_valid: 300
            log_level: 10
            port: 1234
            security_profile: profile2
            vrf: mgmt
        state: merged

    # After state:
    # ------------
    #
    # sonic# show ip rest
    #
    # Log level is 6
    # Port is 443, disabled
    # Request limit is 100
    # Read timeout is 60 seconds
    # Client authentication mode is password
    # Security profile is profile1
    # API timeout is 120 seconds
    # vrf is mgmt
    # Cipher suite is ecdhe-ecdsa-with-aes-256-gcm-SHA384
    #
    # sonic# show ip telemetry
    #
    # Log level is 10
    # JWT valid is 300 seconds
    # JWT refresh is 80 seconds
    # Port is 1234
    # Client authentication mode is cert,jwt
    # Security profile is profile2
    # API timeout is 45 seconds
    # vrf is mgmt


    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show ip rest
    #
    # Log level is 6
    # Port is 443, disabled
    # Request limit is 100
    # Read timeout is 60 seconds
    # Client authentication mode is password
    # Security profile is profile1
    # API timeout is 120 seconds
    # vrf is mgmt
    # Cipher suite is ecdhe-ecdsa-with-aes-256-gcm-SHA384
    #
    # sonic# show ip telemetry
    #
    # Log level is 10
    # JWT valid is 300 seconds
    # JWT refresh is 80 seconds
    # Port is 1234
    # Client authentication mode is cert,jwt
    # Security profile is profile2
    # API timeout is 45 seconds
    # vrf is mgmt

    - name: Replace mgmt servers configuration
      dellemc.enterprise_sonic.sonic_mgmt_servers:
        config:
          rest:
            api_timeout: 180
            vrf: mgmt
            cipher_suite: ecdhe-ecdsa-with-aes-256-gcm-SHA384,ecdhe-ecdsa-with-chacha20-poly1305-SHA256
          telemetry:
            log_level: 25
            security_profile: profile2
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show ip rest
    #
    # Log level is 0
    # Port is 443
    # Request limit is not-set
    # Read timeout is 15 seconds
    # Client authentication mode is password,jwt
    # Security profile is not-set
    # API timeout is 180 seconds
    # vrf is mgmt
    # Cipher suite is ecdhe-ecdsa-with-aes-256-gcm-SHA384,ecdhe-ecdsa-with-chacha20-poly1305-SHA256
    #
    # sonic# show ip telemetry
    #
    # Log level is 25
    # JWT valid is 3600 seconds
    # JWT refresh is 900 seconds
    # Port is 8080
    # Client authentication mode is password,jwt
    # Security profile is profile2
    # API timeout is 0 seconds
    # vrf is not-set


    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show ip rest
    #
    # Log level is 6
    # Port is 443, disabled
    # Request limit is 100
    # Read timeout is 60 seconds
    # Client authentication mode is password
    # Security profile is profile1
    # API timeout is 120 seconds
    # vrf is mgmt
    # Cipher suite is ecdhe-ecdsa-with-aes-256-gcm-SHA384,ecdhe-ecdsa-with-chacha20-poly1305-SHA256
    #
    # sonic# show ip telemetry
    #
    # Log level is 10
    # JWT valid is 300 seconds
    # JWT refresh is 80 seconds
    # Port is 1234
    # Client authentication mode is cert,jwt
    # Security profile is profile2
    # API timeout is 45 seconds
    # vrf is mgmt

    - name: Override mgmt servers configuration
      dellemc.enterprise_sonic.sonic_mgmt_servers:
        config:
          rest:
            api_timeout: 120
            client_auth: password
            log_level: 6
            port: 443
            read_timeout: 60
            req_limit: 100
            security_profile: profile1
            shutdown: true
            vrf: mgmt
            cipher_suite: ecdhe-ecdsa-with-aes-128-gcm-SHA256,ecdhe-ecdsa-with-aes-256-gcm-SHA384
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show ip rest
    #
    # Log level is 6
    # Port is 443, disabled
    # Request limit is 100
    # Read timeout is 60 seconds
    # Client authentication mode is password
    # Security profile is profile1
    # API timeout is 120 seconds
    # vrf is mgmt
    # Cipher suite is ecdhe-ecdsa-with-aes-128-gcm-SHA256,ecdhe-ecdsa-with-aes-256-gcm-SHA384
    #
    # sonic# show ip telemetry
    #
    # Log level is 0
    # JWT valid is 3600 seconds
    # JWT refresh is 900 seconds
    # Port is 8080
    # Client authentication mode is password,jwt
    # Security profile is not-set
    # API timeout is 0 seconds
    # vrf is not-set


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show ip rest
    #
    # Log level is 6
    # Port is 443, disabled
    # Request limit is 100
    # Read timeout is 60 seconds
    # Client authentication mode is password
    # Security profile is profile1
    # API timeout is 120 seconds
    # vrf is mgmt
    # Cipher suite is ecdhe-ecdsa-with-aes-128-gcm-SHA256,ecdhe-ecdsa-with-aes-256-gcm-SHA384
    #
    # sonic# show ip telemetry
    #
    # Log level is 10
    # JWT valid is 300 seconds
    # JWT refresh is 80 seconds
    # Port is 1234
    # Client authentication mode is cert,jwt
    # Security profile is profile2
    # API timeout is 45 seconds
    # vrf is mgmt

    - name: Delete mgmt servers configuration
      dellemc.enterprise_sonic.sonic_mgmt_servers:
        config:
          rest:
            api_timeout: 120
            client_auth: password
            log_level: 6
            port: 443
            read_timeout: 60
            req_limit: 100
            security_profile: profile1
            shutdown: true
            vrf: mgmt
            cipher_suite: ecdhe-ecdsa-with-aes-256-gcm-SHA384,ecdhe-ecdsa-with-aes-128-gcm-SHA256
          telemetry:
            api_timeout: 45
            client_auth: cert,jwt
            jwt_refresh: 80
            jwt_valid: 300
            log_level: 10
            port: 1234
            security_profile: profile2
            vrf: mgmt
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show ip rest
    #
    # Log level is 0
    # Port is 443
    # Request limit is not-set
    # Read timeout is 15 seconds
    # Client authentication mode is password,jwt
    # Security profile is not-set
    # API timeout is 900 seconds
    # vrf is not-set
    # Cipher suite is ecdhe-ecdsa-with-aes-256-gcm-SHA384,ecdhe-ecdsa-with-chacha20-poly1305-SHA256,ecdhe-ecdsa-with-aes-128-gcm-SHA256
    #
    # sonic# show ip telemetry
    #
    # Log level is 0
    # JWT valid is 3600 seconds
    # JWT refresh is 900 seconds
    # Port is 8080
    # Client authentication mode is password,jwt
    # Security profile is not-set
    # API timeout is 0 seconds
    # vrf is not-set



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

- S\. Talabi (@stalabi1)
