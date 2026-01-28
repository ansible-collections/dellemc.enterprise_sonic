.. _dellemc.enterprise_sonic.sonic_login_lockout_module:


********************************************
dellemc.enterprise_sonic.sonic_login_lockout
********************************************

**Manage Global Login Lockout configurations on SONiC**


Version added: 2.5.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of login lockout parameters.
- Login Lockout feature is to lock out the user account for user-lockout-period after the max-retry failed attempts. Console exempt option can be enabled to skip the login lockout validations for console users.




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
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The set of login lockout attribute configurations</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>console_exempt</b>
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
                        <div>Exempt console logins from account lockout.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>max_retries</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The number of maximum password retries.</div>
                        <div>The range is from 0 to 16</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>period</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Account lockout period in minutes</div>
                        <div>The range is from 0 to 43200</div>
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
                        <div>Specifies the operation to be performed on the login attributes configured on the device.</div>
                        <div>If the state is &quot;merged&quot;, merge specified attributes with existing configured login attributes.</div>
                        <div>For &quot;deleted&quot;, delete the specified login attributes from existing configuration.</div>
                        <div>For &quot;overridden&quot;, Overrides all on-device login lockout configurations with the provided configuration.</div>
                        <div>For &quot;replaced&quot;, Replaces on-device login lockout configurations with the provided configuration.</div>
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
    # sonic# show running-configuration | grep lockout
    # !
    # login lockout period 12
    # login lockout max-retries 5
    # login lockout console-exempt
    # !

    - name: Delete Login Lockout configurations
      dellemc.enterprise_sonic.sonic_login_lockout:
        config:
          period: 12
          max_retries: 5
        state: deleted

    # After state:
    # ------------
    # sonic# show running-configuration | grep lockout
    # !
    # login lockout console-exempt
    # !
    # sonic#


    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration | grep lockout
    # sonic#

    - name: Modify Login Lockout configurations
      dellemc.enterprise_sonic.sonic_login_lockout:
        config:
          console_exempt: true
          period: 12
          max_retries: 5
        state: merged

    # After state:
    # ------------
    # sonic# show running-configuration | grep lockout
    # !
    # login lockout period 12
    # login lockout max-retries 5
    # login lockout console-exempt
    # !

    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration | grep lockout
    # !
    # login lockout period 10
    # login lockout max-retries 2
    # !
    # sonic#

    - name: Override Login Lockout configurations
      dellemc.enterprise_sonic.sonic_login_lockout:
        config:
          console_exempt: true
          period: 11
          max_retries: 3
        state: overridden

    # After state:
    # ------------
    # sonic# show running-configuration | grep lockout
    # !
    # login lockout period 11
    # login lockout max-retries 3
    # login lockout console-exempt
    # !

    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration | grep lockout
    # !
    # login lockout period 10
    # login lockout max-retries 2
    # !
    # sonic#

    - name: Replace Login Lockout configurations
      dellemc.enterprise_sonic.sonic_login_lockout:
        config:
          period: 15
        state: replaced

    # After state:
    # ------------
    # sonic# show running-configuration | grep lockout
    # !
    # login lockout period 15
    # !



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
                      <span style="color: purple">dictionary</span>
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

- Arul Kumar Shankara Narayanan(@arulkumar9690)
