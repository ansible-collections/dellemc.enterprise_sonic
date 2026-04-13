.. _dellemc.enterprise_sonic.sonic_dhcp_snooping_module:


********************************************
dellemc.enterprise_sonic.sonic_dhcp_snooping
********************************************

**Manage DHCP Snooping on SONiC**


Version added: 2.3.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of DHCP snooping for devices running SONiC.




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
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The DHCP snooping configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>afis</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of address families to configure.</div>
                        <div>There can be up to two items in this list: one where <em>afi=ipv4</em> and one where <em>afi=ipv6</em> to configure DHCPv4 and DHCPv6, respectively.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>afi</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ipv4</li>
                                    <li>ipv6</li>
                        </ul>
                </td>
                <td>
                        <div>The address family to configure.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>enabled</b>
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
                        <div>Enable DHCP snooping for <em>afi</em>.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>source_bindings</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Create a static entry in the DHCP snooping binding database for <em>afi</em>.</div>
                        <div>When <em>state=deleted</em>, passing an empty list will delete all source bindings.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>intf_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The binding&#x27;s interface name.</div>
                        <div>Can be an Ethernet or a PortChannel interface.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ip_addr</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The bindings&#x27;s IP address.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mac_addr</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The binding&#x27;s MAC address.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vlan_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The binding&#x27;s VLAN ID.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>trusted</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Mark interfaces as trusted for DHCP snooping for <em>afi</em>.</div>
                        <div>When <em>state=deleted</em>, passing an empty list will delete all trusted interfaces.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>intf_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The interface name.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>verify_mac</b>
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
                        <div>Enable DHCP snooping MAC verification for <em>afi</em>.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vlans</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Enable DHCP snooping on a list of VLANs for <em>afi</em>.</div>
                        <div>When <em>state=deleted</em>, passing an empty list will disable DHCP snooping in all VLANs</div>
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
    # sonic# show ip dhcp snooping
    # !
    # DHCP snooping is Disabled
    # DHCP snooping source MAC verification is Disabled
    # DHCP snooping is enabled on the following VLANs:
    # DHCP snooping trusted interfaces:
    # !

    - name: Configure DHCPv4 snooping global settings
      dellemc.enterprise_sonic.sonic_dhcp_snooping:
        config:
          afis:
            - afi: 'ipv4'
              enabled: true
              verify_mac: true
              vlans: ['1', '2', '3', '5']
              trusted:
                - intf_name: 'Ethernet8'
        state: merged

    # After state:
    # ------------
    #
    # sonic# show ip dhcp snooping
    # !
    # DHCP snooping is Enabled
    # DHCP snooping source MAC verification is Enabled
    # DHCP snooping is enabled on the following VLANs: 1 2 3 5
    # DHCP snooping trusted interfaces: Ethernet8
    # !


    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show ipv6 dhcp snooping
    # !
    # DHCPv6 snooping is Disabled
    # DHCPv6 snooping source MAC verification is Disabled
    # DHCPv6 snooping is enabled on the following VLANs:
    # DHCPv6 snooping trusted interfaces:
    # !

    - name: Configure DHCPv6 snooping global settings
      dellemc.enterprise_sonic.sonic_dhcp_snooping:
        config:
          afis:
            - afi: 'ipv6'
              enabled: true
              vlans:
                - '4'
              trusted:
                - intf_name: 'Ethernet2'
                - intf_name: PortChannel1
        state: merged

    # After state:
    # ------------
    #
    # sonic# show ipv6 dhcp snooping
    # !
    # DHCPv6 snooping is Enabled
    # DHCPv6 snooping source MAC verification is Disabled
    # DHCPv6 snooping is enabled on the following VLANs: 4
    # DHCPv6 snooping trusted interfaces: PortChannel1
    # !


    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show ip dhcp snooping binding
    # !
    # Total number of Dynamic bindings: 0
    # Total number of Static bindings: 0
    # Total number of Tentative bindings: 0
    # MAC Address        IP Address       VLAN   Interface    Type     Lease (Secs)
    # -----------------  ---------------  ----   -----------  -------  -----------
    # !

    - name: Add DHCPv4 snooping bindings
      dellemc.enterprise_sonic.sonic_dhcp_snooping:
        config:
          afis:
            - afi: 'ipv4'
              source_bindings:
                - mac_addr: '00:b0:d0:63:c2:26'
                  ip_addr: '192.0.2.146'
                  intf_name: 'Ethernet4'
                  vlan_id: '1'
                - mac_addr: 'aa:f7:67:fc:f4:9a'
                  ip_addr: '156.33.90.167'
                  intf_name: 'PortChannel1'
                  vlan_id: '2'
        state: merged

    # After state:
    # ------------
    #
    # sonic# show ip dhcp snooping binding
    # !
    # Total number of Dynamic bindings: 0
    # Total number of Static bindings: 2
    # Total number of Tentative bindings: 0
    # MAC Address        IP Address       VLAN   Interface    Type     Lease (Secs)
    # -----------------  ---------------  ----   -----------  -------  -----------
    # 00:b0:d0:63:c2:26  192.0.2.146      1      Ethernet4    static   NA
    # aa:f7:67:fc:f4:9a  156.33.90.167    2      PortChannel1  static   NA
    # !


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show ip dhcp snooping
    # !
    # DHCP snooping is Enabled
    # DHCP snooping source MAC verification is Enabled
    # DHCP snooping is enabled on the following VLANs: 1 2 3 5
    # DHCP snooping trusted interfaces: Ethernet8
    # !

    - name: Disable DHCPv4 snooping on some VLANs
      dellemc.enterprise_sonic.sonic_dhcp_snooping:
        config:
          afis:
            - afi: 'ipv4'
              vlans:
                - '3'
                - '5'
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show ip dhcp snooping
    # !
    # DHCP snooping is Enabled
    # DHCP snooping source MAC verification is Enabled
    # DHCP snooping is enabled on the following VLANs: 1 2
    # DHCP snooping trusted interfaces:
    # !


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show ipv6 dhcp snooping
    # !
    # DHCPv6 snooping is Enabled
    # DHCPv6 snooping source MAC verification is Disabled
    # DHCPv6 snooping is enabled on the following VLANs: 4
    # DHCPv6 snooping trusted interfaces: PortChannel1 PortChannel2 PortChannel3 PortChannel4
    # !

    - name: Disable DHCPv6 snooping on all VLANs
      dellemc.enterprise_sonic.sonic_dhcp_snooping:
        config:
          afis:
            - afi: 'ipv6'
              vlans: []
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show ipv6 dhcp snooping
    # !
    # DHCPv6 snooping is Enabled
    # DHCPv6 snooping source MAC verification is Disabled
    # DHCPv6 snooping is enabled on the following VLANs:
    # DHCPv6 snooping trusted interfaces: PortChannel1 PortChannel2 PortChannel3 PortChannel4
    # !


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show ipv6 dhcp snooping
    # !
    # DHCPv6 snooping is Enabled
    # DHCPv6 snooping source MAC verification is Disabled
    # DHCPv6 snooping is enabled on the following VLANs: 4
    # DHCPv6 snooping trusted interfaces: PortChannel1 PortChannel2 PortChannel3 PortChannel4
    # !

    - name: Delete all DHCPv6 configuration
      dellemc.enterprise_sonic.sonic_dhcp_snooping:
        config:
          afis:
            - afi: 'ipv6'
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show ipv6 dhcp snooping
    # !
    # DHCPv6 snooping is Disabled
    # DHCPv6 snooping source MAC verification is Disabled
    # DHCPv6 snooping is enabled on the following VLANs:
    # DHCPv6 snooping trusted interfaces:
    # !


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show ip dhcp snooping binding
    # !
    # Total number of Dynamic bindings: 0
    # Total number of Static bindings: 2
    # Total number of Tentative bindings: 0
    # MAC Address        IP Address       VLAN   Interface    Type     Lease (Secs)
    # -----------------  ---------------  ----   -----------  -------  -----------
    # 00:b0:d0:63:c2:26  192.0.2.146      1      Ethernet4    static   NA
    # aa:f7:67:fc:f4:9a  156.33.90.167    2      PortChannel1  static   NA
    # !

    - name: Delete a DHCPv4 snooping binding
      dellemc.enterprise_sonic.sonic_dhcp_snooping:
        config:
          afis:
            - afi: 'ipv4'
              source_bindings:
                - mac_addr: '00:b0:d0:63:c2:26'
                  ip_addr: '192.0.2.146'
                  intf_name: 'Ethernet4'
                  vlan_id: '1'
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show ip dhcp snooping binding
    # !
    # Total number of Dynamic bindings: 0
    # Total number of Static bindings: 2
    # Total number of Tentative bindings: 0
    # MAC Address        IP Address       VLAN   Interface    Type     Lease (Secs)
    # -----------------  ---------------  ----   -----------  -------  -----------
    # aa:f7:67:fc:f4:9a  156.33.90.167    2      PortChannel1  static   NA
    # !


    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show ipv4 dhcp snooping binding
    # !
    # MAC Address        IP Address       VLAN   Interface    Type     Lease (Secs)
    # -----------------  ---------------  ----   -----------  -------  -----------
    # 00:b0:d0:63:c2:26  192.0.2.146      1      Ethernet4    static   NA
    # 28:21:28:15:c1:1b  141.202.222.118  1      Ethernet2    static   NA
    # aa:f7:67:fc:f4:9a  156.33.90.167    2      PortChannel1  static   NA
    # !

    - name: Override DHCPv4 snooping bindings
      dellemc.enterprise_sonic.sonic_dhcp_snooping:
        config:
          afis:
            - afi: 'ipv4'
              source_bindings:
                - mac_addr: '00:b0:d0:63:c2:26'
                  ip_addr: '192.0.2.146'
                  intf_name: 'Ethernet4'
                  vlan_id: '3'
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show ipv4 dhcp snooping binding
    # !
    # MAC Address        IP Address       VLAN   Interface    Type     Lease (Secs)
    # -----------------  ---------------  ----   -----------  -------  -----------
    # 00:b0:d0:63:c2:26  192.0.2.146      3      Ethernet4    static   NA
    # !


    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show ipv4 dhcp snooping binding
    # !
    # MAC Address        IP Address       VLAN   Interface    Type     Lease (Secs)
    # -----------------  ---------------  ----   -----------  -------  -----------
    # 00:b0:d0:63:c2:26  192.0.2.146      1      Ethernet4    static   NA
    # 28:21:28:15:c1:1b  141.202.222.118  1      Ethernet2    static   NA
    # aa:f7:67:fc:f4:9a  156.33.90.167    2      PortChannel1  static   NA
    # !

    - name: Replace DHCPv4 snooping bindings
      dellemc.enterprise_sonic.sonic_dhcp_snooping:
        config:
          afis:
            - afi: 'ipv4'
              source_bindings:
                - mac_addr: '00:b0:d0:63:c2:26'
                  ip_addr: '192.0.2.146'
                  intf_name: 'Ethernet4'
                  vlan_id: '3'
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show ipv4 dhcp snooping binding
    # !
    # MAC Address        IP Address       VLAN   Interface    Type     Lease (Secs)
    # -----------------  ---------------  ----   -----------  -------  -----------
    # 00:b0:d0:63:c2:26  192.0.2.146      3      Ethernet4    static   NA
    # 28:21:28:15:c1:1b  141.202.222.118  1      Ethernet2    static   NA
    # aa:f7:67:fc:f4:9a  156.33.90.167    2      PortChannel1  static   NA
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

- Simon Nathans (@simon-nathans), Xiao Han (@Xiao_Han2)
