.. _dellemc.enterprise_sonic.sonic_fips_module:


***********************************
dellemc.enterprise_sonic.sonic_fips
***********************************

**Manage FIPS configurations on SONiC**


Version added: 2.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides FIPS configuration management to specify the security requirements for cryptographic modules in devices running SONiC.




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
                        <div>The mode of FIPS configuration with specifications of security requirements for cryptographic modules.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>enable</b>
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
                        <div>This argument is a boolean value to enable or disable FIPS mode.</div>
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
                        </ul>
                </td>
                <td>
                        <div>The state specifies the type of configuration update to be performed on the device. If the state is &quot;merged&quot;, merge specified attributes with existing configured attributes. For &quot;deleted&quot;, delete the specified attributes from existing configuration.</div>
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
    # sonic# show running-configuration | grep fips
    # !
    # crypto fips enable
    # !

    - name: Delete FIPS mode configuration
      dellemc.enterprise_sonic.sonic_fips:
        config:
          enable: false
        state: deleted

    # After state:
    # ------------
    # sonic# show running-configuration | grep fips
    # sonic#


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show fips status
    # !
    # FIPS Mode           : Enabled
    # Crypto Library      : OpenSSL 1.1.1n-fips  15 Mar 2022
    # FIPS Object Module  : DELL OpenSSL FIPS Crypto Module v2.6 July 2021
    # !

    - name: Disable FIPS mode
      dellemc.enterprise_sonic.sonic_fips:
        config:
          enable: false
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show fips status
    # !
    # FIPS Mode           : Disabled
    # Crypto Library      : OpenSSL 1.1.1n-fips  15 Mar 2022
    # FIPS Object Module  : DELL OpenSSL FIPS Crypto Module v2.6 July 2021
    # !


    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration | grep fips
    # sonic#

    - name: Modify FIPS configurations
      dellemc.enterprise_sonic.sonic_fips:
        config:
          enable: true
        state: merged

    # After state:
    # ------------
    # sonic# show running-configuration | grep fips
    # !
    # crypto fips enable
    # !


    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show fips status
    # !
    # FIPS Mode           : Disabled
    # Crypto Library      : OpenSSL 1.1.1n-fips  15 Mar 2022
    # FIPS Object Module  : DELL OpenSSL FIPS Crypto Module v2.6 July 2021
    # !

    - name: Enable FIPS mode
      dellemc.enterprise_sonic.sonic_fips:
        config:
          enable: true
        state: merged

    # After state:
    # ------------
    #
    # sonic# show fips status
    # !
    # FIPS Mode           : Enabled
    # Crypto Library      : OpenSSL 1.1.1n-fips  15 Mar 2022
    # FIPS Object Module  : DELL OpenSSL FIPS Crypto Module v2.6 July 2021
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

- Balasubramaniam Koundappa(@balasubramaniam-k)
