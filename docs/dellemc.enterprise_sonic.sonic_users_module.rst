.. _dellemc.enterprise_sonic.sonic_users_module:


************************************
dellemc.enterprise_sonic.sonic_users
************************************

**Manage users and its parameters**


Version added: 1.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of users parameters on devices running Enterprise SONiC.




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
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the users related configuration.</div>
                </td>
            </tr>
                                <tr>
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
                        <div>Specifies the name of the user.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>password</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the password of the user.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>role</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
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
                        <div>Specifies the role of the user.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ssh_key</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.1.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the user ssh key for an existing user.</div>
                        <div>The ssh key pair (public and private key) can be created using ssh-keygen command on the server from</div>
                        <div>where the user will connect to the SONiC device.</div>
                        <div>Only the public key is configured in the ssh_key field.</div>
                        <div>The ssh_key option can only be &quot;merged&quot; after initial creation of the affected &quot;user&quot; instance</div>
                        <div>and must be merged without any additional options specified other than &quot;name&quot;.</div>
                        <div>It can only be deleted as an individual option if it is the only option specified.</div>
                        <div>If other options are specified for deletion, the entire user instance is deleted.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>update_password</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>always</b>&nbsp;&larr;</div></li>
                                    <li>on_create</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the update password flag.</div>
                        <div>In case of always, password will be updated every time.</div>
                        <div>In case of on_create, password will be updated only when user is created.</div>
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
                                    <li>overridden</li>
                                    <li>replaced</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the operation to be performed on the users configured on the device.</div>
                        <div>In case of merged, the input configuration will be merged with the existing users configuration on the device.</div>
                        <div>In case of deleted the existing users configuration will be removed from the device.</div>
                        <div>In case of replaced, the existing specified user configuration will be replaced with provided configuration.</div>
                        <div>In case of overridden, the existing users configuration will be overridden with the provided configuration.</div>
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
    # sonic# show users configured
    # ----------------------------------------------------------------------
    # User                              Role(s)
    # ----------------------------------------------------------------------
    # admin                             admin
    # sysadmin                          admin
    # sysoperator                       operator

    - name: Delete user
      dellemc.enterprise_sonic.sonic_users:
        config:
          - name: sysoperator
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show users configured
    # ----------------------------------------------------------------------
    # User                              Role(s)
    # ----------------------------------------------------------------------
    # admin                             admin
    # sysadmin                          admin

    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show users configured
    # ----------------------------------------------------------------------
    # User                              Role(s)
    # ----------------------------------------------------------------------
    # admin                             admin
    # sysadmin                          admin
    # sysoperator                       operator

    - name: Delete all users configurations except admin
      dellemc.enterprise_sonic.sonic_users:
        config:
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show users configured
    # ----------------------------------------------------------------------
    # User                              Role(s)
    # ----------------------------------------------------------------------
    # admin                             admin

    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show users configured
    # ----------------------------------------------------------------------
    # User                              Role(s)
    # ----------------------------------------------------------------------
    # admin                             admin

    - name: Merge users configurations
      dellemc.enterprise_sonic.sonic_users:
        config:
          - name: sysadmin
            role: admin
            password: admin
            update_password: always
          - name: sysoperator
            role: operator
            password: operator
            update_password: always
        state: merged

    # After state:
    # ------------
    #
    # sonic# show users configured
    # ----------------------------------------------------------------------
    # User                              Role(s)
    # ----------------------------------------------------------------------
    # admin                             admin
    # sysadmin                          admin
    # sysoperator                       operator

    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show users configured
    # ----------------------------------------------------------------------
    # User                              Role(s)
    # ----------------------------------------------------------------------
    # admin                             admin
    # sysadmin                          admin
    # sysoperator                       operator

    - name: Override users configurations
      dellemc.enterprise_sonic.sonic_users:
        config:
          - name: user1
            role: secadmin
            password: 123abc
            update_password: always
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show users configured
    # ----------------------------------------------------------------------
    # User                              Role(s)
    # ----------------------------------------------------------------------
    # admin                             admin
    # user1                             secadmin

    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show users configured
    # ----------------------------------------------------------------------
    # User                              Role(s)
    # ----------------------------------------------------------------------
    # admin                             admin
    # user1                             secadmin
    # user2                             operator

    - name: Replace users configurations
      dellemc.enterprise_sonic.sonic_users:
        config:
          - name: user1
            role: operator
            password: 123abc
            update_password: always
          - name: user2
            role: netadmin
            password: 123abc
            update_password: always
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show users configured
    # ----------------------------------------------------------------------
    # User                              Role(s)
    # ----------------------------------------------------------------------
    # admin                             admin
    # user1                             operator
    # user2                             netadmin

    # Using Merged
    #
    # Before state:
    # -------------
    #
    # sonic# show users sshkey
    #
    # sonic# show users configured
    # --------------------------------------------------------------------
    # User                           Role(s)
    # --------------------------------------------------------------------
    # admin                          admin
    # user1                          operator
    # user2                          netadmin

    - name: Configure user sshkey
      dellemc.enterprise_sonic.sonic_users:
        config:
          - name: user1
            ssh_key: >
              ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQCoCc6lPgrSAXZByJAPH6cwn0Mhj9J1zYUfiLc
              /iz/IwHt/7s++bN1tnL6bAan6Ssg4XvOF0mcP5K53AAP+bX5WHy/d1wm7icllBI0JT150qp9nY5y
              bjNdvLH11cxqc+mmNYa7d40fpeoUgMdSBGtSL0jY2PHHRCvVscFYjSm6tQQ== root@sonic
        state: merged

    # After state:
    # ------------
    #
    # sonic# show users configured
    # ----------------------------------------------------------------------
    # sonic# show users sshKey
    # User: user1
    # SSH Key: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQCoCc6lPgrSAXZByJAPH6cwn0Mhj9J1zYUfiLc/iz/IwHt/7s
    #          ++bN1tnL6bAan6Ssg4XvOF0mcP5K53AAP+bX5WHy/d1wm7icllBI0JT150qp9nY5ybjNdvLH11cxqc+mmNYa7d
    #          40fpeoUgMdSBGtSL0jY2PHHRCvVscFYjSm6tQQ== root@sonic
    # ----------------------------------------------------------------------

    # Using Deleted
    #
    # Before state:
    # -------------
    #
    # sonic# show users sshKey
    # User: user1
    # SSH Key: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQDHD2TJqQ/Fve+fG5i6heOJH55wgbEf+7kTtUGBUtNttQ9OXgBRr
    #          A2h2GKSyUNlyfaVijBrcr2MKwhSASvk58WnEqZhfmmhRDsdNVXPlMQuDBheIlCaXyOh+URJZCfmfeERSVO7kjRhqM
    #          mbHlpTbMDHdFgYEvHGcrHMwIZyZ6KbBw== root@sonic
    # ----------------------------------------------------------------------

    - name: Delete sshkey for existing users
      dellemc.enterprise_sonic.sonic_users:
        config:
          - name: user1
            ssh_key:
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show users sshkey
    # ----------------------------------------------------------------------



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

- Niraimadaiselvam M (@niraimadaiselvamm)
