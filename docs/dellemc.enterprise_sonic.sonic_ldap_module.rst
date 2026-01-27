.. _dellemc.enterprise_sonic.sonic_ldap_module:


***********************************
dellemc.enterprise_sonic.sonic_ldap
***********************************

**Configure global LDAP server settings on SONiC.**


Version added: 2.5.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of global LDAP server parameters on devices running SONiC.
- Configure VRF instance before configuring VRF to be used for LDAP server connection.




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
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the LDAP server related configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>base</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure base distinguished name.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>bind_timelimit</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure connect time limit (0 to 65535).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>binddn</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure distinguished name to bind.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>bindpw</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure credentials to bind</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Indicates whether the password is encrypted text.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>pwd</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Authentication password for the bind.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>idle_timelimit</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure NSS idle time limit (0 to 65535).</div>
                        <div>Applicable only for global and nss.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>map</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure LDAP server for map.</div>
                        <div>Applicable only for global.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>attribute</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure attribute map.</div>
                        <div><em>from</em> and <em>to</em> are required together.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>from</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure attribute map key.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>to</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure attribute map value.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>default_attribute</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure default attribute map.</div>
                        <div><em>from</em> and <em>to</em> are required together.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>from</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure default attribute map key.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>to</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure default attribute map value.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>map_remote_groups_to_sonic_roles</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure mapping for remote groups to sonic roles.</div>
                        <div><em>remote_group</em> and <em>sonic_roles</em> are required together.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>remote_group</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Map remote groups to SONiC roles.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>sonic_roles</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>admin</li>
                                    <li>operator</li>
                                    <li>netadmin</li>
                                    <li>secadmin</li>
                        </ul>
                </td>
                <td>
                        <div>Configure SONiC roles.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>objectclass</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure Objectclass map.</div>
                        <div><em>from</em> and <em>to</em> are required together.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>from</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure Objectclass map key.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>to</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure Objectclass map value.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>override_attribute</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure override attribute map.</div>
                        <div><em>from</em> and <em>to</em> are required together.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>from</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure override attribute map key.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>to</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure override attribute map value.</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>global</li>
                                    <li>nss</li>
                                    <li>pam</li>
                                    <li>sudo</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the LDAP type.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>nss_base_group</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure NSS search base for group map.</div>
                        <div>Applicable only for global and nss.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>nss_base_netgroup</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure NSS search base for netgroup map.</div>
                        <div>Applicable only for global and nss.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>nss_base_passwd</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure NSS search base for passwd map.</div>
                        <div>Applicable only for global, nss and pam.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>nss_base_shadow</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure NSS search base for shadow map.</div>
                        <div>Applicable only for global and nss.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>nss_base_sudoers</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure NSS search base for sudoers map.</div>
                        <div>Applicable only for global and nss.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>nss_initgroups_ignoreusers</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure NSS init groups ignore users.</div>
                        <div>Applicable only for global and nss.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>nss_skipmembers</b>
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
                        <div>Configure NSS skipmembers</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>pam_filter</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure PAM filter.</div>
                        <div>Applicable only for global and pam.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>pam_group_dn</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure PAM Group Distinguished name.</div>
                        <div>Applicable only for global and pam.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>pam_login_attribute</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure PAM Login attribute.</div>
                        <div>Applicable only for global and pam.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>pam_member_attribute</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure PAM Member attribute.</div>
                        <div>Applicable only for global and pam.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Configure server port (1 to 65535).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>retry</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure retransmit attempt (0 to 10).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>scope</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>sub</li>
                                    <li>one</li>
                                    <li>base</li>
                        </ul>
                </td>
                <td>
                        <div>Configure the search scope.</div>
                        <div>Applicable only for global, nss and pam.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Configure security profile for LDAP.</div>
                        <div>Applicable only for global.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Configure host name or IP address for a LDAP server.</div>
                        <div>Applicable only for global.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Hostname or IP address of LDAP server.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Configure server port number (1 to 65535).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Configure priority (1 to 99).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>retry</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure retransmit attempt (0 to 10).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>server_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>all</li>
                                    <li>nss</li>
                                    <li>sudo</li>
                                    <li>pam</li>
                                    <li>nss_sudo</li>
                                    <li>nss_pam</li>
                                    <li>sudo_pam</li>
                        </ul>
                </td>
                <td>
                        <div>Configure server type.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ssl</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>on</li>
                                    <li>off</li>
                                    <li>start_tls</li>
                        </ul>
                </td>
                <td>
                        <div>Configure TLS configuration.</div>
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
                        <div>Configure source interface to be used as source IP for the LDAP packets.</div>
                        <div>Applicable only for global.</div>
                        <div>Full name of the Layer 3 interface, i.e. Eth1/1.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ssl</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>on</li>
                                    <li>off</li>
                                    <li>start_tls</li>
                        </ul>
                </td>
                <td>
                        <div>Configure TLS configuration.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>sudoers_base</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure sudo base distinguished name for queries.</div>
                        <div>Applicable only for global and sudo.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>sudoers_search_filter</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure sudo search filter for queries.</div>
                        <div>Applicable only for global and sudo.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>timelimit</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure search time limit (1 to 65535).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>version</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>2</li>
                                    <li>3</li>
                        </ul>
                </td>
                <td>
                        <div>Configure LDAP version 2 or 3.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Configure VRF to be used for LDAP server connection.</div>
                        <div>Applicable only for global.</div>
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
                                    <li>replaced</li>
                                    <li>overridden</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the operation to be performed on the LDAP server configured on the device.</div>
                        <div>In case of merged, the input configuration will be merged with the existing LDAP server configuration on the device.</div>
                        <div>In case of deleted, the existing LDAP server configuration will be removed from the device.</div>
                        <div>In case of overridden, all the existing LDAP server configuration will be deleted and the specified input configuration will be installed.</div>
                        <div>In case of replaced, the existing LDAP server configuration on the device will be replaced by the configuration in the playbook for each LDAP server group configured by the playbook.</div>
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
    # sonic# show running-configuration vrf Vrf_1
    # !
    # ip vrf Vrf_1
    # sonic# show running-configuration | grep ldap
    # ldap-server port 389
    # ldap-server version 2
    # ldap-server nss-base-passwd password
    # ldap-server nss-initgroups-ignoreusers username1
    # ldap-server nss scope sub
    # ldap-server nss timelimit 15
    # ldap-server nss idle-timelimit 25
    # ldap-server nss nss-base-group group1
    # ldap-server nss nss-base-sudoers sudo1
    # ldap-server pam base admin
    # ldap-server pam binddn CN=example.com
    # ldap-server pam pam-login-attribute loginattrstring
    # ldap-server sudo retry 10
    # ldap-server sudo ssl start_tls
    # ldap-server sudo bind-timelimit 15
    # ldap-server vrf Vrf_1
    # ldap-server host 10.10.10.1 port 1550 priority 5
    # ldap-server host 20.20.20.10 retry 1
    # ldap-server host example.com priority 10 ssl off
    # ldap-server map default-attribute-value attr1 to attr2
    # ldap-server map default-attribute-value attr3 to attr4
    # ldap-server map objectclass attr1 to attr3
    # sonic#

    - name: Delete the LDAP server configurations
      sonic_ldap:
        config:
          - name: "global"
            servers:
              - address: "example.com"
            vrf: "Vrf_1"
          - name: "nss"
            idle_timelimit: 25
            scope: "sub"
          - name: "sudo"
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration | grep ldap
    # ldap-server port 389
    # ldap-server version 2
    # ldap-server nss-base-passwd password
    # ldap-server nss-initgroups-ignoreusers username1
    # ldap-server nss timelimit 15
    # ldap-server nss nss-base-group group1
    # ldap-server nss nss-base-sudoers sudo1
    # ldap-server pam base admin
    # ldap-server pam binddn CN=example.com
    # ldap-server pam pam-login-attribute loginattrstring
    # ldap-server host 10.10.10.1 port 1550 priority 5
    # ldap-server host 20.20.20.10 retry 1
    # ldap-server map default-attribute-value attr1 to attr2
    # ldap-server map default-attribute-value attr3 to attr4
    # ldap-server map objectclass attr1 to attr3
    # sonic#


    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration vrf Vrf_1
    # !
    # ip vrf Vrf_1
    # !
    # sonic# show running-configuration | grep ldap
    # sonic#

    - name: Add the LDAP server configurations
      sonic_ldap:
        config:
          - name: "global"
            servers:
              - address: "example.com"
                priority: 10
                ssl: "on"
              - address: "10.10.10.1"
                priority: 5
                port: 1550
            port: 389
            version: 2
            nss_base_passwd: password
          - name: "pam"
            base: "admin"
            binddn: "CN=example.com"
            pam_login_attribute: "loginattrstring"
          - name: "sudo"
            bind_timelimit: 20
            retry: 10
        state: merged

    # After state:
    # ------------
    #
    # sonic# show running-configuration | grep ldap
    # ldap-server port 389
    # ldap-server version 2
    # ldap-server nss-base-passwd password
    # ldap-server pam base admin
    # ldap-server pam binddn CN=example.com
    # ldap-server pam pam-login-attribute loginattrstring
    # ldap-server sudo retry 10
    # ldap-server sudo bind-timelimit 20
    # ldap-server host 10.10.10.1 port 1550 priority 5
    # ldap-server host example.com priority 10 ssl on
    # sonic#


    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration vrf Vrf_1
    # !
    # ip vrf Vrf_1
    # !
    # sonic# show running-configuration | grep ldap
    # ldap-server port 389
    # ldap-server version 2
    # ldap-server nss-base-passwd password
    # ldap-server pam base admin
    # ldap-server pam binddn CN=example.com
    # ldap-server pam pam-login-attribute loginattrstring
    # ldap-server sudo retry 10
    # ldap-server sudo bind-timelimit 20
    # ldap-server host 10.10.10.1 port 1550 priority 5
    # ldap-server host example.com priority 10 ssl on
    # sonic#

    - name: Add the LDAP server configurations
      sonic_ldap:
        config:
          - name: "global"
            servers:
              - address: "example.com"
                ssl: "off"
              - address: "20.20.20.10"
                retry: 1
            nss_base_passwd: password
            pam_login_attribute: "globallogin"
            nss_initgroups_ignoreusers: "username1"
            vrf: "Vrf_1"
            map:
              default_attribute:
                - from: "attr1"
                  to: "attr2"
                - from: "attr3"
                  to: "attr4"
              objectclass:
                - from: "attr1"
                  to: "attr3"
              map_remote_groups_to_sonic_roles:
                - remote_group: "group1"
                  sonic_roles:
                    - admin
                    - operator
          - name: "nss"
            nss_base_netgroup: "group1"
            idle_timelimit: 25
            timelimit: 15
            scope: "sub"
            nss_base_sudoers: "sudo1"
          - name: "sudo"
            bind_timelimit: 15
            ssl: "start_tls"
        state: merged

    # After state:
    # ------------
    #
    # sonic# show running-configuration | grep ldap
    # ldap-server port 389
    # ldap-server version 2
    # ldap-server nss-base-passwd password
    # ldap-server pam-login-attribute globallogin
    # ldap-server nss-initgroups-ignoreusers username1
    # ldap-server nss scope sub
    # ldap-server nss timelimit 15
    # ldap-server nss idle-timelimit 25
    # ldap-server nss nss-base-group group1
    # ldap-server nss nss-base-sudoers sudo1
    # ldap-server pam base admin
    # ldap-server pam binddn CN=example.com
    # ldap-server pam pam-login-attribute loginattrstring
    # ldap-server sudo retry 10
    # ldap-server sudo ssl start_tls
    # ldap-server sudo bind-timelimit 15
    # ldap-server vrf Vrf_1
    # ldap-server host 10.10.10.1 port 1550 priority 5
    # ldap-server host 20.20.20.10 retry 1
    # ldap-server host example.com priority 10 ssl off
    # ldap-server map default-attribute-value attr1 to attr2
    # ldap-server map default-attribute-value attr3 to attr4
    # ldap-server map objectclass attr1 to attr3
    # ldap-server map remote-groups-override-to-sonic-roles group1 to admin,operator
    # sonic#


    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration vrf Vrf_1
    # !
    # ip vrf Vrf_1
    # sonic# show running-configuration | grep ldap
    # ldap-server port 389
    # ldap-server version 2
    # ldap-server nss-base-passwd password
    # ldap-server nss-initgroups-ignoreusers username1
    # ldap-server nss idle-timelimit 25
    # ldap-server nss nss-base-group group1
    # ldap-server nss nss-base-sudoers sudo1
    # ldap-server pam base admin
    # ldap-server pam binddn CN=example.com
    # ldap-server pam pam-login-attribute loginattrstring
    # ldap-server host 10.10.10.1 port 1550 priority 5
    # ldap-server host 20.20.20.10 retry 1
    # ldap-server map default-attribute-value attr1 to attr2
    # ldap-server map default-attribute-value attr3 to attr4
    # ldap-server map objectclass attr1 to attr3
    # sonic#

    - name: Replace the LDAP server configurations
      sonic_ldap:
        config:
          - name: "nss"
            scope: "one"
            bindpw:
              pwd: "password"
          - name: "pam"
            version: 3
            port: 2000
            timelimit: 20
            pam_group_dn: "DNAME"
          - name: "sudo"
            sudoers_search_filter: "filter1"
            base: "base_name"
            version: 3
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show running-configuration | grep ldap
    # ldap-server port 389
    # ldap-server version 2
    # ldap-server nss scope one
    # ldap-server nss bindpw U2FsdGVkX1+t8PR9IIi+qjZpYoNwjmd78D1WDBdkLxs= encrypted
    # ldap-server pam version 3
    # ldap-server pam port 2000
    # ldap-server pam timelimit 20
    # ldap-server pam pam-group-dn DNAME
    # ldap-server sudo version 3
    # ldap-server sudo base base_name
    # ldap-server sudo sudoers-search-filter filter1
    # ldap-server host 10.10.10.1 port 1550 priority 5
    # ldap-server host 20.20.20.10 retry 1
    # ldap-server map default-attribute-value attr1 to attr2
    # ldap-server map default-attribute-value attr3 to attr4
    # ldap-server map objectclass attr1 to attr3
    # sonic#


    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration vrf Vrf_1
    # !
    # ip vrf Vrf_1
    # sonic# show running-configuration | grep ldap
    # ldap-server port 389
    # ldap-server version 2
    # ldap-server nss scope one
    # ldap-server nss bindpw U2FsdGVkX1+t8PR9IIi+qjZpYoNwjmd78D1WDBdkLxs= encrypted
    # ldap-server pam version 3
    # ldap-server pam port 2000
    # ldap-server pam timelimit 20
    # ldap-server pam pam-group-dn DNAME
    # ldap-server sudo version 3
    # ldap-server sudo base base_name
    # ldap-server sudo sudoers-search-filter filter1
    # ldap-server host 10.10.10.1 port 1550 priority 5
    # ldap-server host 20.20.20.10 retry 1
    # ldap-server map default-attribute-value attr1 to attr2
    # ldap-server map default-attribute-value attr3 to attr4
    # ldap-server map objectclass attr1 to attr3
    # sonic#

    - name: Override the LDAP server configurations
      sonic_ldap:
        config:
          - name: "global"
            source_interface: "Eth1/1"
            security_profile: "default"
            vrf: "Vrf_1"
            servers:
              - address: "client.com"
              - address: "host.com"
                server_type: "sudo_pam"
            map:
              override_attribute:
                - from: "attr1"
                  to: "attr2"
              map_remote_groups_to_sonic_roles:
                - remote_group: "group1"
                  sonic_roles:
                    - admin
                    - operator
            idle_timelimit: 20
          - name: "pam"
            ssl: "off"
            scope: "base"
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show running-configuration | grep ldap
    # ldap-server idle-timelimit 20
    # ldap-server pam ssl off
    # ldap-server pam scope base
    # ldap-server source-interface Eth1/1
    # ldap-server security-profile default
    # ldap-server vrf Vrf_1
    # ldap-server host client.com
    # ldap-server host host.com use-type sudo_pam
    # ldap-server map override-attribute-value attr1 to attr2
    # ldap-server map remote-groups-override-to-sonic-roles group1 to admin,operator
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
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>when changed</td>
                <td>
                            <div>The resulting configuration module invocation.</div>
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

- Santhosh Kumar T(@santhosh-kt)
