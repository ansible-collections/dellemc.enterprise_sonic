.. _dellemc.enterprise_sonic.sonic_ptp_port_ds_module:


******************************************
dellemc.enterprise_sonic.sonic_ptp_port_ds
******************************************

**Manage port specific PTP configurations on SONiC**


Version added: 3.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of port-specific PTP parameters for devices running SONiC.




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
                        <div>Specifies port-specific PTP configurations.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interface</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the name of the interface.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>local_priority</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">null</div>
                </td>
                <td>
                        <div>Specifies the local-priority attribute used for the profile G8275-1 and G8275-2.</div>
                        <div>The range is from 1 to 255.</div>
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
                                    <li>dynamic</li>
                                    <li>master</li>
                                    <li>slave</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the role of interface.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>unicast_table</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of ip addresses to use for PTP master.</div>
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
                        <div><code>merged</code> - Merges provided interface-specific PTP configuration with on-device configuration.</div>
                        <div><code>replaced</code> - Replaces on-device PTP configuration of the specified interfaces with provided configuration.</div>
                        <div><code>overridden</code> - Overrides all on-device interface-specific PTP configurations with the provided configuration.</div>
                        <div><code>deleted</code> - Deletes on-device interface-specific PTP configuration.</div>
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

    # Using deleted
    #
    # Before State:
    # -------------
    #
    # sonic# show running-configuration ptp | grep "ptp port"
    # ptp port add Ethernet0 role slave local-priority 100
    # ptp port add Ethernet4 role master local-priority 90
    # ptp port master-table Ethernet0 add 1.1.1.1
    # ptp port master-table Ethernet0 add 1.1.1.2
    # sonic#

    - name: Delete specified PTP port configurations
      dellemc.enterprise_sonic.sonic_ptp_port_ds:
        config:
          - interface: 'Ethernet4'
            role: 'master'
            local_priority: 90
          - interface: 'Ethernet0'
            role: 'slave'
            local_priority: 100
            unicast_table:
              - '1.1.1.1'
              - '1.1.1.2'
        state: deleted

    # After State:
    # ------------
    #
    # sonic# show running-configuration ptp
    # ptp port add Ethernet4 role master local-priority 90
    # sonic#


    # Using deleted
    #
    # Before State:
    # -------------
    #
    # sonic# show running-configuration ptp | grep "ptp port"
    # ptp port add Ethernet0 role slave local-priority 100
    # ptp port add Ethernet4 role master local-priority 90
    # ptp port master-table Ethernet0 add 1.1.1.1
    # ptp port master-table Ethernet0 add 1.1.1.2
    # sonic#

    - name: Delete all PTP configurations in the specified port
      dellemc.enterprise_sonic.sonic_ptp_port_ds:
        config:
          - interface: 'Ethernet0'
        state: deleted

    # After State:
    # ------------
    #
    # sonic# show running-configuration ptp
    # ptp port add Ethernet4 role master local-priority 90
    # sonic#


    # Using deleted
    #
    # Before State:
    # -------------
    #
    # sonic# show running-configuration ptp | grep "ptp port"
    # ptp port add Ethernet0 role slave local-priority 100
    # ptp port add Ethernet4 role master local-priority 90
    # ptp port master-table Ethernet0 add 1.1.1.1
    # ptp port master-table Ethernet0 add 1.1.1.2
    # sonic#

    - name: Delete all PTP port configurations
      dellemc.enterprise_sonic.sonic_ptp_port_ds:
        config:
        state: deleted

    # After State:
    # ------------
    #
    # sonic# show running-configuration ptp
    # sonic#

    # Using merged
    #
    # Before State:
    # -------------
    #
    # sonic# show running-configuration ptp | grep "ptp port"
    # ptp port add Ethernet0
    # sonic#

    - name: Merge provided PTP port configurations
      dellemc.enterprise_sonic.sonic_ptp_port_ds:
        config:
          - interface: 'Ethernet0'
            role: 'slave'
            local_priority: 100
        state: merged

    # After State:
    # ------------
    #
    # sonic# show running-configuration ptp | grep "ptp port"
    # ptp port add Ethernet0 role slave local-priority 100
    # sonic#


    # Using replaced
    #
    # Before State:
    # -------------
    #
    # sonic# do show running-configuration | grep "ptp port"
    # ptp port add Ethernet0 role master local-priority 10
    # ptp port add Ethernet1 local-priority 100
    # ptp port add Ethernet2 role slave
    # ptp port master-table Ethernet1 add 1.1.1.1
    # sonic#

    - name: Replace PTP configurations for specified port
      dellemc.enterprise_sonic.sonic_ptp_port_ds:
        config:
          - interface: 'Ethernet0'
            role: 'slave'
            unicast_table:
              - '2.2.2.2'
        state: replaced

    # After State:
    # ------------
    #
    # sonic# do show running-configuration | grep "ptp port"
    # ptp port add Ethernet0 role slave
    # ptp port add Ethernet1 local-priority 100
    # ptp port add Ethernet2 role slave
    # ptp port master-table Ethernet0 add 2.2.2.2
    # ptp port master-table Ethernet1 add 1.1.1.1
    # sonic#


    # Using overridden
    #
    # Before State:
    # -------------
    #
    # sonic# show running-configuration ptp | grep "ptp port"
    # ptp port add Ethernet0 role slave local-priority 100
    # ptp port master-table Ethernet0 add 1.1.1.1
    # sonic#

    - name: Override device PTP port configuration with provided configuration
      dellemc.enterprise_sonic.sonic_ptp_port_ds:
        config:
          - interface: 'Ethernet4'
            role: 'master'
            local_priority: 90
        state: overridden

    # After State:
    # ------------
    #
    # sonic# show running-configuration ptp | grep "ptp port"
    # ptp port add Ethernet4 role master local-priority 90
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
     of the parameters above.</div>
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
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The configuration prior to the model invocation.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format
     of the parameters above.</div>
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

- Vidya Chidambaram (@vidyac86)
