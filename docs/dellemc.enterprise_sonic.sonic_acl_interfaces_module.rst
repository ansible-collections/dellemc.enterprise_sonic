.. _dellemc.enterprise_sonic.sonic_acl_interfaces_module:


*********************************************
dellemc.enterprise_sonic.sonic_acl_interfaces
*********************************************

**Manage access control list (ACL) to interface binding on SONiC**


Version added: 2.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of applying access control lists (ACL) to interfaces in devices running SONiC.
- ACL needs to be created earlier in the device.




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
                        <div>Specifies interface access-group configurations.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>access_groups</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Access-group configurations to be set for the interface.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>acls</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of ACLs for the given type.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>direction</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>in</li>
                                    <li>out</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the direction of the packets that the ACL will be applied on.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
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
                        <div>Name of the ACL to be applied on the interface.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>mac</li>
                                    <li>ipv4</li>
                                    <li>ipv6</li>
                        </ul>
                </td>
                <td>
                        <div>Type of the ACLs to be applied on the interface.</div>
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
                </td>
                <td>
                        <div>Full name of the interface, i.e. Eth1/1.</div>
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
                                    <li>replaced</li>
                                    <li>overridden</li>
                                    <li>deleted</li>
                        </ul>
                </td>
                <td>
                        <div>The state of the configuration after module completion.</div>
                        <div><em>merged</em> - Merges provided interface access-group configuration with on-device configuration.</div>
                        <div><em>replaced</em> - Replaces on-device access-group configuration of the specified interfaces with provided configuration.</div>
                        <div><em>overridden</em> - Overrides all on-device interface access-group configurations with the provided configuration.</div>
                        <div><em>deleted</em> - Deletes on-device interface access-group configuration.</div>
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

    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show mac access-group
    # sonic#
    # sonic# show ip access-group
    # sonic#
    # sonic# show ipv6 access-group
    # Ingress IPV6 access-list ipv6-acl-1 on Eth1/1
    # sonic#

    - name: Merge provided interface access-group configurations
      dellemc.enterprise_sonic.sonic_acl_interfaces:
        config:
          - name: 'Eth1/1'
            access_groups:
              - type: 'mac'
                acls:
                  - name: 'mac-acl-1'
                    direction: 'in'
                  - name: 'mac-acl-2'
                    direction: 'out'
              - type: 'ipv6'
                acls:
                  - name: 'ipv6-acl-2'
                    direction: 'out'
          - name: 'Eth1/2'
            access_groups:
              - type: 'ipv4'
                acls:
                  - name: 'ip-acl-1'
                    direction: 'in'
        state: merged

    # After state:
    # ------------
    #
    # sonic# show mac access-group
    # Ingress MAC access-list mac-acl-1 on Eth1/1
    # Egress MAC access-list mac-acl-2 on Eth1/1
    # sonic#
    # sonic# show ip access-group
    # Ingress IP access-list ip-acl-1 on Eth1/2
    # sonic#
    # sonic# show ipv6 access-group
    # Ingress IPV6 access-list ipv6-acl-1 on Eth1/1
    # Egress IPV6 access-list ipv6-acl-2 on Eth1/1
    # sonic#


    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show mac access-group
    # Ingress MAC access-list mac-acl-1 on Eth1/1
    # Egress MAC access-list mac-acl-2 on Eth1/1
    # sonic#
    # sonic# show ip access-group
    # Ingress IP access-list ip-acl-1 on Eth1/2
    # sonic#
    # sonic# show ipv6 access-group
    # Ingress IPV6 access-list ipv6-acl-1 on Eth1/1
    # Egress IPV6 access-list ipv6-acl-2 on Eth1/1
    # sonic#

    - name: Replace device access-group configuration of specified interfaces with provided configuration
      dellemc.enterprise_sonic.sonic_acl_interfaces:
        config:
          - name: 'Eth1/2'
            access_groups:
              - type: 'ipv6'
                acls:
                  - name: 'ipv6-acl-2'
                    direction: 'out'
          - name: 'Eth1/3'
            access_groups:
              - type: 'ipv4'
                acls:
                  - name: 'ip-acl-2'
                    direction: 'out'
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show mac access-group
    # Ingress MAC access-list mac-acl-1 on Eth1/1
    # Egress MAC access-list mac-acl-2 on Eth1/1
    # sonic#
    # sonic# show ip access-group
    # Egress IP access-list ip-acl-2 on Eth1/3
    # sonic#
    # sonic# show ipv6 access-group
    # Ingress IPV6 access-list ipv6-acl-1 on Eth1/1
    # Egress IPV6 access-list ipv6-acl-2 on Eth1/1
    # Egress IPV6 access-list ipv6-acl-2 on Eth1/2
    # sonic#


    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show mac access-group
    # Ingress MAC access-list mac-acl-1 on Eth1/1
    # Egress MAC access-list mac-acl-2 on Eth1/1
    # sonic#
    # sonic# show ip access-group
    # Egress IP access-list ip-acl-2 on Eth1/3
    # sonic#
    # sonic# show ipv6 access-group
    # Ingress IPV6 access-list ipv6-acl-1 on Eth1/1
    # Egress IPV6 access-list ipv6-acl-2 on Eth1/1
    # Egress IPV6 access-list ipv6-acl-2 on Eth1/2
    # sonic#

    - name: Override all interfaces access-group device configuration with provided configuration
      dellemc.enterprise_sonic.sonic_acl_interfaces:
        config:
          - name: 'Eth1/1'
            access_groups:
              - type: 'ip'
                acls:
                  - name: 'ip-acl-2'
                    direction: 'out'
          - name: 'Eth1/2'
            access_groups:
              - type: 'ip'
                acls:
                  - name: 'ip-acl-2'
                    direction: 'out'
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show mac access-group
    # sonic#
    # sonic# show ip access-group
    # Egress IP access-list ip-acl-2 on Eth1/1
    # Egress IP access-list ip-acl-2 on Eth1/2
    # sonic#
    # sonic# show ipv6 access-group
    # sonic#


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show mac access-group
    # Ingress MAC access-list mac-acl-1 on Eth1/1
    # Egress MAC access-list mac-acl-2 on Eth1/1
    # sonic#
    # sonic# show ip access-group
    # Egress IP access-list ip-acl-2 on Eth1/3
    # sonic#
    # sonic# show ipv6 access-group
    # Ingress IPV6 access-list ipv6-acl-1 on Eth1/1
    # Egress IPV6 access-list ipv6-acl-2 on Eth1/1
    # Egress IPV6 access-list ipv6-acl-2 on Eth1/2
    # sonic#

    - name: Delete specified interfaces access-group configurations
      dellemc.enterprise_sonic.sonic_l2_acls:
        config:
          - name: 'Eth1/1'
            access_groups:
              - type: 'mac'
                acls:
                  - name: 'mac-acl-1'
                    direction: 'in'
              - type: 'ipv6'
          - name: 'Eth1/2'
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show mac access-group
    # Egress MAC access-list mac-acl-2 on Eth1/1
    # sonic#
    # sonic# show ip access-group
    # Egress IP access-list ip-acl-2 on Eth1/3
    # sonic#
    # sonic# show ipv6 access-group
    # sonic#


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show mac access-group
    # Ingress MAC access-list mac-acl-1 on Eth1/1
    # Egress MAC access-list mac-acl-2 on Eth1/1
    # sonic#
    # sonic# show ip access-group
    # Egress IP access-list ip-acl-2 on Eth1/3
    # sonic#
    # sonic# show ipv6 access-group
    # Ingress IPV6 access-list ipv6-acl-1 on Eth1/1
    # Egress IPV6 access-list ipv6-acl-2 on Eth1/1
    # Egress IPV6 access-list ipv6-acl-2 on Eth1/2
    # sonic#

    - name: Delete all interface access-group configurations
      dellemc.enterprise_sonic.sonic_acl_interfaces:
        config:
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show mac access-group
    # sonic#
    # sonic# show ip access-group
    # sonic#
    # sonic# show ipv6 access-group
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

- Arun Saravanan Balachandran (@ArunSaravananBalachandran)
