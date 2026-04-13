.. _dellemc.enterprise_sonic.sonic_pim_interfaces_module:


*********************************************
dellemc.enterprise_sonic.sonic_pim_interfaces
*********************************************

**Manage interface-specific PIM configurations on SONiC**


Version added: 2.5.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of interface-specific PIM parameters for devices running SONiC.
- BFD profiles need to be created earlier in the device.




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
                        <div>Specifies interface-specific PIM configurations.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>bfd_enable</b>
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
                        <div>Enable BFD support for PIM.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>bfd_profile</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the BFD profile to be enabled.</div>
                        <div>BFD support for PIM has to be enabled for configuring BFD profile.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>drpriority</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the Designated Router Priority.</div>
                        <div>The range is from 1 to 4294967295.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>hello_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the Hello interval in seconds.</div>
                        <div>The range is from 1 to 255.</div>
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
                        <div>Full name of the interface.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>sparse_mode</b>
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
                        <div>Enable PIM sparse-mode.</div>
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
                                    <li>replaced</li>
                                    <li>overridden</li>
                        </ul>
                </td>
                <td>
                        <div>The state of the configuration after module completion.</div>
                        <div><code>merged</code> - Merges provided interface-specific PIM configuration with on-device configuration.</div>
                        <div><code>replaced</code> - Replaces on-device PIM configuration of the specified interfaces with provided configuration.</div>
                        <div><code>overridden</code> - Overrides all on-device interface-specific PIM configurations with the provided configuration.</div>
                        <div><code>deleted</code> - Deletes on-device interface-specific PIM configuration.</div>
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
    # sonic# show running-configuration interface Eth 1/1 | grep "ip pim"
    #  ip pim sparse-mode
    #  ip pim drpriority 10
    #  ip pim hello 60
    #  ip pim bfd
    #  ip pim bfd profile profile_1
    # sonic# show running-configuration interface Eth 1/2 | grep "ip pim"
    #  ip pim hello 60
    #  ip pim bfd
    # sonic#

    - name: Delete specified interface PIM configurations
      dellemc.enterprise_sonic.sonic_pim_interfaces:
        config:
          - name: 'Eth1/1'
            hello_interval: 60
            bfd_profile: profile_1
          - name: 'Eth1/2'
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration interface Eth 1/1 | grep "ip pim"
    #  ip pim sparse-mode
    #  ip pim drpriority 10
    #  ip pim bfd
    # sonic# show running-configuration interface Eth 1/2 | grep "ip pim"
    # sonic#


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface Eth 1/1 | grep "ip pim"
    #  ip pim sparse-mode
    #  ip pim drpriority 10
    #  ip pim hello 60
    #  ip pim bfd
    #  ip pim bfd profile profile_1
    # sonic# show running-configuration interface Eth 1/2 | grep "ip pim"
    #  ip pim hello 60
    #  ip pim bfd
    # sonic#

    - name: Delete all interface-specific PIM configurations
      dellemc.enterprise_sonic.sonic_pim_interfaces:
        config:
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration interface Eth 1/1 | grep "ip pim"
    # sonic# show running-configuration interface Eth 1/2 | grep "ip pim"
    # sonic#


    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface Eth 1/1 | grep "ip pim"
    #  ip pim sparse-mode
    #  ip pim hello 45
    # sonic# show running-configuration interface Eth 1/2 | grep "ip pim"
    # sonic#

    - name: Merge provided interface PIM configurations
      dellemc.enterprise_sonic.sonic_pim_interfaces:
        config:
          - name: 'Eth1/1'
            drpriority: 10
            hello_interval: 60
            bfd_enable: true
            bfd_profile: profile_1
          - name: 'Eth1/2'
            hello_interval: 60
            bfd_enable: true
        state: merged

    # After state:
    # ------------
    #
    # sonic# show running-configuration interface Eth 1/1 | grep "ip pim"
    #  ip pim sparse-mode
    #  ip pim drpriority 10
    #  ip pim hello 60
    #  ip pim bfd
    #  ip pim bfd profile profile_1
    # sonic# show running-configuration interface Eth 1/2 | grep "ip pim"
    #  ip pim hello 60
    #  ip pim bfd
    # sonic#


    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface Eth 1/1 | grep "ip pim"
    #  ip pim sparse-mode
    #  ip pim drpriority 10
    #  ip pim hello 45
    #  ip pim bfd
    #  ip pim bfd profile profile_1
    # sonic# show running-configuration interface Eth 1/2 | grep "ip pim"
    #  ip pim hello 60
    #  ip pim bfd
    # sonic#

    - name: Replace PIM configurations for specified interfaces
      dellemc.enterprise_sonic.sonic_pim_interfaces:
        config:
          - name: 'Eth1/1'
            hello_interval: 60
            bfd_enable: true
            bfd_profile: profile_1
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show running-configuration interface Eth 1/1 | grep "ip pim"
    #  ip pim hello 60
    #  ip pim bfd
    #  ip pim bfd profile profile_1
    # sonic# show running-configuration interface Eth 1/2 | grep "ip pim"
    #  ip pim hello 60
    #  ip pim bfd
    # sonic#


    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface Eth 1/1 | grep "ip pim"
    #  ip pim sparse-mode
    #  ip pim drpriority 10
    #  ip pim hello 45
    #  ip pim bfd
    #  ip pim bfd profile profile_1
    # sonic# show running-configuration interface Eth 1/2 | grep "ip pim"
    #  ip pim hello 60
    #  ip pim bfd
    # sonic#

    - name: Override interface-specific PIM configurations
      dellemc.enterprise_sonic.sonic_pim_interfaces:
        config:
          - name: 'Eth1/1'
            hello_interval: 60
            bfd_enable: true
            bfd_profile: profile_1
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show running-configuration interface Eth 1/1 | grep "ip pim"
    #  ip pim hello 60
    #  ip pim bfd
    #  ip pim bfd profile profile_1
    # sonic# show running-configuration interface Eth 1/2 | grep "ip pim"
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
                            <div>The resulting configuration on module invocation.</div>
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
                            <div>The generated configuration on module invocation.</div>
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

- Arun Saravanan Balachandran (@ArunSaravananBalachandran)
