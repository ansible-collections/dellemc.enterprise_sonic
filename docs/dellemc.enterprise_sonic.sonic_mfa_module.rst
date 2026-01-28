.. _dellemc.enterprise_sonic.sonic_mfa_module:


**********************************
dellemc.enterprise_sonic.sonic_mfa
**********************************

**Manage Multi-factor authentication (MFA) configurations on SONiC.**


Version added: 4.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of MFA parameters for devices running SONiC.
- Pre-configured host cert is required for MFA security profile, and ca-cert for RSA/CAC-PIV security profiles.




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
                        <div>Specifies MFA configurations.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>cac_piv_global</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>CAC-PIV Global configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>cert_username_field</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>common-name</li>
                                    <li>common-name-or-user-principal-name</li>
                                    <li>user-principal-name</li>
                        </ul>
                </td>
                <td>
                        <div>SSH user certificate field for matching with SSH login username.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>cert_username_match</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>10digit-username</li>
                                    <li>first-name</li>
                                    <li>username-as-is</li>
                                    <li>username-without-domain</li>
                        </ul>
                </td>
                <td>
                        <div>Match option to parse the username from respective certificate field.</div>
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
                        <div>Security profile for SSH access with CAC-PIV.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mfa_global</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>MFA Global configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>client_secret</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Password used in basic authorization header for MFA REST API.</div>
                        <div>Minimum 32 characters with atleast one symbol, digit, uppercase, and lowercase.</div>
                        <div>Plain text password i.e. <em>client_secret_encrypted=false</em> will be stored in encrypted format in running-config, so idempotency will not be maintained and hence the task output will always be <em>changed=true</em>.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>client_secret_encrypted</b>
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
                        <div>Indicates whether <em>client_secret</em> is plain text or encrypted.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>key_seed</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Seed for generating secure key in MFA service.</div>
                        <div>Plain text seed i.e. <em>key_seed_encrypted=false</em> will be stored in encrypted format in running-config, so idempotency will not be maintained and hence the task output will always be <em>changed=true</em>.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>key_seed_encrypted</b>
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
                        <div>Indicates whether <em>key_seed</em> is plain text or encrypted.</div>
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
                        <div>Security profile contains the certificate for MFA service.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>rsa_global</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>RSA Global configuration.</div>
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
                        <div>Security profile with CA-cert for validating RSA SecurID server.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>rsa_servers</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>RSA Server configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>client_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Unique identifier of the system as a client of SecurID service, assigned by SecurID service.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>client_key</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Key associated with the client-id, assigned by SecurID service.</div>
                        <div>Plain text key i.e. <em>client_key_encrypted=false</em> will be stored in encrypted format in running-config, so idempotency will not be maintained and hence the task output will always be <em>changed=true</em>.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>client_key_encrypted</b>
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
                        <div>Indicates whether <em>client_key</em> is plain text or encrypted.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>connection_timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Timeout in seconds for connection to the SecurID server.</div>
                        <div>Range 1-30.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>hostname</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>RSA server&#x27;s hostname or IP address.</div>
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
                </td>
                <td>
                        <div>Timeout in seconds to read from the SecurID server.</div>
                        <div>Range 1-150.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>server_port</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Port number of the RSA SecurID server.</div>
                        <div>Range 1025-49151.</div>
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
                        <div>The state of the configuration after module completion.</div>
                        <div><code>merged</code> - Merges provided MFA configuration with on-device configuration.</div>
                        <div><code>replaced</code> - Replaces on-device MFA configuration with provided configuration.</div>
                        <div><code>overridden</code> - Overrides all on-device MFA configurations with the provided configuration.</div>
                        <div><code>deleted</code> - Deletes on-device MFA configuration.</div>
                </td>
            </tr>
    </table>
    <br/>




Examples
--------

.. code-block:: yaml

    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration mfa
    # mfa key-seed U2FsdGVkX1/caD7u0ZGRnb981G2DKyML/Gvyfexsurg= encrypted
    # mfa client-secret U2FsdGVkX1+WlquxtZRbsgQhfS1lQBFbJKflxGAp6S3u+Ox5Hi+O16NmprjMVb3HQn1pNSgaaa0Cz1MHeTfDWhFR0WqdENbLU2PqkiRDHv0iVfl72xNPzhnGeO01kAu0 encrypted
    # mfa security-profile mSecurityProfile
    # mfa rsa-server security-profile rSecProfile
    # mfa rsa-server host rsaserver.che-lab.it port 1030 client-id sonicdevtest.che-lab.it client-key
    # U2FsdGVkX18QFJoB9dp8GJN92eP79FGOZDLgQakBmAasGYX77p6PtiiAfS/nGoOb2uEocUkryc+BLLYsg+Wz0gO+c1QsIbIhXk5Pt+aECoVgoFQ9QpxO9od9cTik+3Ot encrypted
    # connection-timeout 29 read-timeout 149
    #
    # sonic# show running-configuration | grep "cac-piv"
    # aaa cac-piv cert-user common-name
    # aaa cac-piv cert-user-match 10digit-username
    # aaa cac-piv security-profile cSecurityProfile
    # sonic#


    - name: Delete specified mfa configuration
      dellemc.enterprise_sonic.sonic_mfa:
        config:
          mfa_global:
            key_seed: 'U2FsdGVkX1/caD7u0ZGRnb981G2DKyML/Gvyfexsurg='
            key_seed_encrypted: true
            client_secret: 'U2FsdGVkX1+WlquxtZRbsgQhfS1lQBFbJKflxGAp6S3u+Ox5Hi+O16NmprjMVb3HQn1pNSgaaa0Cz1MHeTfDWhFR0WqdENbLU2PqkiRDHv0iVfl72xNPzhnGeO01kAu0'
            client_secret_encrypted: true
          rsa_global:
            security_profile: 'rSecProfile'
          rsa_servers:
            hostname: 'rsaserver.che-lab.it'
            server_port: 1030
            client_id: 'sonicdevtest.che-lab.it'
            client_key: 'U2FsdGVkX18QFJoB9dp8GJN92eP79FGOZDLgQakBmAasGYX77p6PtiiAfS/nGoOb2uEocUkryc+BLLYsg+Wz0gO+c1QsIbIhXk5Pt+aECoVgoFQ9QpxO9od9cTik+3Ot'
            client_key_encrypted: true
            connection_timeout: 29
            read_timeout: 149
          cac_piv_global:
            security_profile: 'cSecurityProfile'
            cert_username_field: 'common-name'
        state: deleted


    # After state:
    # ------------
    #
    # sonic# show running-configuration mfa
    # mfa security-profile mSecurityProfile
    #
    # sonic# show running-configuration | grep "cac-piv"
    # aaa cac-piv cert-user-match 10digit-username
    # sonic#


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration mfa
    # mfa key-seed U2FsdGVkX1/caD7u0ZGRnb981G2DKyML/Gvyfexsurg= encrypted
    # mfa client-secret U2FsdGVkX1+WlquxtZRbsgQhfS1lQBFbJKflxGAp6S3u+Ox5Hi+O16NmprjMVb3HQn1pNSgaaa0Cz1MHeTfDWhFR0WqdENbLU2PqkiRDHv0iVfl72xNPzhnGeO01kAu0 encrypted
    # mfa security-profile mSecurityProfile
    # mfa rsa-server security-profile rSecProfile
    # mfa rsa-server host rsaserver.che-lab.it port 1030 client-id sonicdevtest.che-lab.it client-key
    # U2FsdGVkX18QFJoB9dp8GJN92eP79FGOZDLgQakBmAasGYX77p6PtiiAfS/nGoOb2uEocUkryc+BLLYsg+Wz0gO+c1QsIbIhXk5Pt+aECoVgoFQ9QpxO9od9cTik+3Ot encrypted
    # connection-timeout 29 read-timeout 149
    #
    # sonic# show running-configuration | grep "cac-piv"
    # aaa cac-piv cert-user common-name
    # aaa cac-piv cert-user-match 10digit-username
    # aaa cac-piv security-profile cSecurityProfile
    # sonic#


    - name: Delete all mfa configurations
      dellemc.enterprise_sonic.sonic_mfa:
        config:
        state: deleted


    # After state:
    # ------------
    #
    # sonic# show running-configuration mfa
    # sonic#
    #
    # sonic# show running-configuration | grep "cac-piv"
    # sonic#


    # Using "merged" state
    #
    # Before State:
    # -------------
    #
    # sonic# show running-configuration mfa
    # sonic#
    #
    # sonic# show running-configuration | grep "cac-piv"
    # sonic#


    - name: Merge provided MFA configurations
      dellemc.enterprise_sonic.sonic_mfa:
        config:
          mfa_global:
            security_profile: 'mSecurityProfile'
            key_seed: 'sonic'
            key_seed_encrypted: true
            client_secret: 'U2FsdGVkX18mPdwkM1z24i7lxMtqNZR9p2q3aa6YXR16OfDxQXCR9z9I0lQZpVjE!'
            client_secret_encrypted: true
          rsa_global:
            security_profile: 'rSecProfile'
          rsa_servers:
            hostname: 'rsaserver.che-lab.it'
            server_port: 1030
            client_id: 'sonicdevtest.che-lab.it'
            client_key: 'aplr05825jshusp80699scuv62u5l3lu63wxf66b0y883w92677ac0c9m0lwv6o8'
            client_key_encrypted: true
            connection_timeout: 29
            read_timeout: 149
          cac_piv_global:
            security_profile: 'cSecurityProfile'
            cert_username_field: 'user-principal-name'
            cert_username_match: '10digit-username'
        state: merged


    # After State:
    # ------------
    #
    # sonic# show running-configuration mfa
    # mfa key-seed U2FsdGVkX1/caD7u0ZGRnb981G2DKyML/Gvyfexsurg= encrypted
    # mfa client-secret U2FsdGVkX1+WlquxtZRbsgQhfS1lQBFbJKflxGAp6S3u+Ox5Hi+O16NmprjMVb3HQn1pNSgaaa0Cz1MHeTfDWhFR0WqdENbLU2PqkiRDHv0iVfl72xNPzhnGeO01kAu0 encrypted
    # mfa security-profile mSecurityProfile
    # mfa rsa-server security-profile rSecProfile
    # mfa rsa-server host rsaserver.che-lab.it port 1030 client-id sonicdevtest.che-lab.it client-key
    # U2FsdGVkX18QFJoB9dp8GJN92eP79FGOZDLgQakBmAasGYX77p6PtiiAfS/nGoOb2uEocUkryc+BLLYsg+Wz0gO+c1QsIbIhXk5Pt+aECoVgoFQ9QpxO9od9cTik+3Ot encrypted
    # connection-timeout 29 read-timeout 149
    #
    # sonic# show running-configuration | grep "cac-piv"
    # aaa cac-piv cert-user user-principal-name
    # aaa cac-piv cert-user-match 10digit-username
    # aaa cac-piv security-profile cSecurityProfile


    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration mfa
    # mfa key-seed U2FsdGVkX1/caD7u0ZGRnb981G2DKyML/Gvyfexsurg= encrypted
    # mfa rsa-server host rsaserver.che-lab.it port 1030 client-id sonicdevtest.che-lab.it client-key
    # U2FsdGVkX1+xnsxfUrqCvBQg0KkPUm11R8Vpn2cXLHCWzL59k3Jm4/OrRiMOemPJccnEa8sMuynOAaySpHkaMOePtpedW0aApp+qicIF2Hz32LR4vB07b7OSx7OaEZBj encrypted
    # connection-timeout 16 read-timeout 129


    - name: Replace specified mfa rsa-server configuration
      dellemc.enterprise_sonic.sonic_mfa:
        config:
          rsa_servers:
            - hostname: 'rsaserver.che-lab.it'
              server_port: 1050
              client_id: 'sonicdevtest.che-lab.it'
              client_key: 'aplr05825jshusp80699scuv62u5l3lu63wxf66b0y883w92677ac0c9m0lwv6o8'
              client_key_encrypted: true
              connection_timeout: 29
              read_timeout: 149
        state: replaced


    # After state:
    # ------------
    #
    # sonic# show running-configuration mfa
    # mfa key-seed U2FsdGVkX1/caD7u0ZGRnb981G2DKyML/Gvyfexsurg= encrypted
    # mfa rsa-server host rsaserver.che-lab.it port 1050 client-id sonicdevtest.che-lab.it client-key
    # U2FsdGVkX1/b1Tjka6pWv1BjwGd1I8cfjXxBIIJ6ZK/JaZpGgPbNAnw6WmdstRWJz49A+bymj6gJfkGjbzlWQhGCGi4VofPStOdNktqDcIyk33AaDkO+awkzyi7HRxcB encrypted
    # connection-timeout 29 read-timeout 149


    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration mfa
    # mfa key-seed U2FsdGVkX1/caD7u0ZGRnb981G2DKyML/Gvyfexsurg= encrypted
    # mfa client-secret U2FsdGVkX1+WlquxtZRbsgQhfS1lQBFbJKflxGAp6S3u+Ox5Hi+O16NmprjMVb3HQn1pNSgaaa0Cz1MHeTfDWhFR0WqdENbLU2PqkiRDHv0iVfl72xNPzhnGeO01kAu0 encrypted
    # mfa security-profile mSecurityProfile
    # mfa rsa-server security-profile rSecProfile
    # mfa rsa-server host sonicrsaserver.che-lab.it port 1030 client-id sonic.che-lab.it client-key
    # U2FsdGVkX18QFJoB9dp8GJN92eP79FGOZDLgQakBmAasGYX77p6PtiiAfS/nGoOb2uEocUkryc+BLLYsg+Wz0gO+c1QsIbIhXk5Pt+aECoVgoFQ9QpxO9od9cTik+3Ot encrypted
    # connection-timeout 29 read-timeout 149
    #
    # sonic# show running-configuration | grep "cac-piv"
    # aaa cac-piv cert-user user-principal-name
    # aaa cac-piv cert-user-match 10digit-username
    # aaa cac-piv security-profile cSecurityProfile


    - name: Override device configuration of mfa with provided configuration
      dellemc.enterprise_sonic.sonic_mfa:
        config:
          cac_piv_global:
            cert_username_match: 'first-name'
        state: overridden


    # After state:
    # ------------
    #
    # sonic# show running-configuration | grep "cac-piv"
    # aaa cac-piv cert-user-match first-name



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
                    <b>before</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The configuration prior to module invocation.</div>
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
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>generated_after</b>
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
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Divya Narendran (@Divya-N3)
