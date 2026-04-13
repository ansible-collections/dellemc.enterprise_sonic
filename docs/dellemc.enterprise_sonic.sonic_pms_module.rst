.. _dellemc.enterprise_sonic.sonic_pms_module:


**********************************
dellemc.enterprise_sonic.sonic_pms
**********************************

**Configure interface mode port security settings on SONiC.**


Version added: 3.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of port security interface mode parameters on devices running SONiC.
- Configure switchport before configuring port security in interfaces.




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
                        <div>Specifies the port security interface configurations.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>max_allowed_macs</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Maximum no. of secure MACs allowed on the interface. (1 to 4097)</div>
                        <div>If <em>port_security_enable=True</em> and <em>max_allowed_macs</em> not configured, default is <code>1</code>.</div>
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
                        <div>Full name of the interface, i.e. Ethernet1.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>port_security_enable</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Enables port security at interface level.</div>
                        <div>If <em>port_security_enable=False</em>, entire port security configurations will be deleted.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>sticky_mac</b>
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
                        <div>Enable sticky MAC feature on the interface.</div>
                        <div>If <em>port_security_enable=True</em> and <em>sticky_mac</em> not configured, default is <code>False</code>.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>violation</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>SHUTDOWN</li>
                                    <li>PROTECT</li>
                        </ul>
                </td>
                <td>
                        <div>Configure the action to be taken in the event of security violation.</div>
                        <div><code>SHUTDOWN</code> - Shutdown the interface.</div>
                        <div><code>PROTECT</code> - Drop packets received on the interface.</div>
                        <div>If <em>port_security_enable=True</em> and <em>violation</em> not configured, default is <code>PROTECT</code>.</div>
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
                        <div>Specifies the operation to be performed on the port security related interfaces configured on the device.</div>
                        <div>In case of merged, the input configuration will be merged with the existing port security interfaces related configuration on the device.</div>
                        <div>In case of deleted, the existing OSPFv2 interfaces configuration will be removed from the device.</div>
                        <div>In case of overridden, all the existing OSPFv2 interfaces configuration will be deleted and the specified input configuration will be installed.</div>
                        <div>In case of replaced, the existing interface configuration on the device will be replaced by the configuration in the playbook for each interface group configured by the playbook.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - Supports ``check_mode``.
   - Tested against Enterprise SONiC Distribution by Dell Technologies.



Examples
--------

.. code-block:: yaml

    # Using "deleted" state

    # Before state:
    # -------------
    #
    # sonic# show port-security
    #
    # Secure Port         isEnabled    MaxSecureAddr   FdbCount    ViolationCount    SecurityAction  StickyMac
    # ---------------------------------------------------------------------------------------------------------
    #     Ethernet0           Y            1               0           0                 PROTECT         N
    #     Ethernet10          N            1               0           0                 PROTECT         Y
    # sonic#

    - name: Delete the PMS configurations
      sonic_pms:
        config:
          - name: 'Ethernet0'
            port_security_enable: true
          - name: 'Ethernet10'
            port_security_enable: false
            sticky_mac: true
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show port-security
    #
    # Secure Port         isEnabled    MaxSecureAddr   FdbCount    ViolationCount    SecurityAction  StickyMac
    # ---------------------------------------------------------------------------------------------------------
    #     Ethernet10          N            1               0           0                 PROTECT         N
    # sonic#


    # Using "deleted" state

    # Before state:
    # -------------
    #
    # sonic# show port-security
    #
    # Secure Port         isEnabled    MaxSecureAddr   FdbCount    ViolationCount    SecurityAction  StickyMac
    # ---------------------------------------------------------------------------------------------------------
    #     Ethernet0           Y            1               0           0                 PROTECT         N
    #     Ethernet3           Y            10              0           0                 PROTECT         N
    #     Ethernet4           N            15              0           0                 SHUTDOWN        N
    #     Ethernet5           Y            30              0           0                 SHUTDOWN        N
    #     Ethernet10          N            1               0           0                 PROTECT         Y
    # sonic#

    - name: Delete all the PMS configurations
      sonic_pms:
        config: []
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show port-security
    # sonic#


    # Using "merged" state

    # Before state:
    # -------------
    #
    # sonic# show port-security
    # sonic#

    - name: Add the PMS configurations new to interfaces
      sonic_pms:
        config:
          - name: 'Ethernet0'
            sticky_mac: true
            port_security_enable: true
            max_allowed_macs: 10
          - name: 'Ethernet3'
            port_security_enable: false
            max_allowed_macs: 10
          - name: 'Ethernet4'
            port_security_enable: true
            violation: SHUTDOWN
        state: merged

    # After state:
    # ------------
    #
    # sonic# show port-security
    #
    # Secure Port         isEnabled    MaxSecureAddr   FdbCount    ViolationCount    SecurityAction  StickyMac
    # ---------------------------------------------------------------------------------------------------------
    #     Ethernet0           Y            10              0           0                 PROTECT         Y
    #     Ethernet3           N            10              0           0                 PROTECT         N
    #     Ethernet4           Y            1               0           0                 SHUTDOWN        N
    # sonic#


    # Using "merged" state

    # Before state:
    # -------------
    #
    # sonic# show port-security
    #
    # Secure Port         isEnabled    MaxSecureAddr   FdbCount    ViolationCount    SecurityAction  StickyMac
    # ---------------------------------------------------------------------------------------------------------
    #     Ethernet0           Y            10              0           0                 PROTECT         Y
    #     Ethernet3           N            10              0           0                 PROTECT         N
    #     Ethernet4           Y            1               0           0                 SHUTDOWN        N
    # sonic#

    - name: Disable a PMS interface by merge
      sonic_pms:
        config:
          - name: 'Ethernet10'
            port_security_enable: false
            max_allowed_macs: 12
            violation: SHUTDOWN
            sticky_mac: true
          - name: 'Ethernet4'
            port_security_enable: false
        state: merged

    # After state:
    # ------------
    #
    # sonic# show port-security
    #
    # Secure Port         isEnabled    MaxSecureAddr   FdbCount    ViolationCount    SecurityAction  StickyMac
    # ---------------------------------------------------------------------------------------------------------
    #     Ethernet0           Y            10              0           0                 PROTECT         Y
    #     Ethernet3           N            10              0           0                 PROTECT         N
    #     Ethernet10          N            12              0           0                 SHUTDOWN        Y
    # sonic#


    # Using "replaced" state

    # Before state:
    # -------------
    #
    # sonic# show port-security
    #
    # Secure Port         isEnabled    MaxSecureAddr   FdbCount    ViolationCount    SecurityAction  StickyMac
    # ---------------------------------------------------------------------------------------------------------
    #     Ethernet0           Y            1               0           0                 PROTECT         N
    #     Ethernet3           Y            10              0           0                 PROTECT         N
    #     Ethernet4           N            15              0           0                 SHUTDOWN        N
    #     Ethernet5           Y            30              0           0                 SHUTDOWN        N
    #     Ethernet10          N            12              0           0                 SHUTDOWN        Y
    # sonic#

    - name: Replace the PMS configurations by interface level
      sonic_pms:
        config:
          - name: 'Ethernet10'
            port_security_enable: true
          - name: 'Ethernet3'
            port_security_enable: false
            violation: 'PROTECT'
            sticky_mac: true
          - name: 'Ethernet7'
            port_security_enable: true
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show port-security
    #
    # Secure Port         isEnabled    MaxSecureAddr   FdbCount    ViolationCount    SecurityAction  StickyMac
    # ---------------------------------------------------------------------------------------------------------
    #     Ethernet0           Y            1               0           0                 PROTECT         N
    #     Ethernet3           N            10              0           0                 PROTECT         Y
    #     Ethernet4           N            15              0           0                 SHUTDOWN        N
    #     Ethernet5           Y            30              0           0                 SHUTDOWN        N
    #     Ethernet7           Y            1               0           0                 PROTECT         N
    #     Ethernet10          Y            1               0           0                 PROTECT         N
    # sonic#


    # Using "overridden" state

    # Before state:
    # -------------
    #
    # sonic# show port-security
    #
    # Secure Port         isEnabled    MaxSecureAddr   FdbCount    ViolationCount    SecurityAction  StickyMac
    # ---------------------------------------------------------------------------------------------------------
    #     Ethernet0           Y            1               0           0                 PROTECT         N
    #     Ethernet3           Y            10              0           0                 PROTECT         N
    #     Ethernet4           N            15              0           0                 SHUTDOWN        N
    #     Ethernet5           Y            30              0           0                 SHUTDOWN        N
    #     Ethernet10          N            12              0           0                 SHUTDOWN        Y
    # sonic#

    - name: Override the PMS configurations
      sonic_pms:
        config:
          - name: 'Ethernet7'
            port_security_enable: true
          - name: 'Ethernet10'
            port_security_enable: false
            max_allowed_macs: 12
            violation: SHUTDOWN
            sticky_mac: true
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show port-security
    #
    # Secure Port         isEnabled    MaxSecureAddr   FdbCount    ViolationCount    SecurityAction  StickyMac
    # ---------------------------------------------------------------------------------------------------------
    #     Ethernet7           Y            1               0           0                 PROTECT         N
    #     Ethernet10          N            12              0           0                 SHUTDOWN        Y
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
                            <div>The configuration resulting from module invocation.</div>
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
                            <div>The configuration that would be generated by non-check-mode module invocation.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format
     of the parameters above.</div>
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

- Santhosh kumar T (@santhosh-kt)
