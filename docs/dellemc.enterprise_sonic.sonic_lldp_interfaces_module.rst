.. _dellemc.enterprise_sonic.sonic_lldp_interfaces_module:


**********************************************
dellemc.enterprise_sonic.sonic_lldp_interfaces
**********************************************

**Manage Inteface LLDP configurations on SONiC**


Version added: 2.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of interface LLDP parameters in devices running SONiC.
- It is intended for use in conjunction with global LLDP.




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
                        <div>The set of link layer discovery protocol interface attribute configurations</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>This argument is a boolean value to enable or disable LLDP.</div>
                        <div>This command is supported only on physical interfaces and not on logical interfaces.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>med_tlv_select</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>This command can be used to select whether to advertise the LLDP-MED TLVs or not. By default the LLDP-MED TLVs are advertised.</div>
                        <div>This command is supported only on physical interfaces and not on logical interfaces.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>network_policy</b>
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
                        <div>This command can be used to select whether to advertise network-policy LLDP-MED TLVs or not. By default network-policy LLDP-MED TLVs are advertised.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>power_management</b>
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
                        <div>This command can be used to select whether to advertise power-management LLDP-MED TLVs or not. By default power-management LLDP-MED TLVs are advertised.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mode</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>receive</li>
                                    <li>transmit</li>
                        </ul>
                </td>
                <td>
                        <div>By default both transmit and receive of LLDP frames is enabled.</div>
                        <div>This command can be used to configure either in receive only or transmit only mode.</div>
                        <div>This command is supported on physical and logical interfaces.</div>
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
                        <div>Interface name in which LLDP needs to be configured on.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>network_policy</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.1.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>Network policy number, range 1-128.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>tlv_select</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>This command can be used to select whether to advertise the LLDP 802.3at or bt power management TLVs or not. By default this TLV is advertised.</div>
                        <div>This command is supported only on physical interfaces and not on logical interfaces.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>link_aggregation</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.1.0</div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>This command can be used to select whether to advertise link-aggregation LLDP TLVs or not. By default link-aggregation LLDP TLVs are advertised.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>max_frame_size</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.1.0</div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>This command can be used to select whether to advertise max-frame-size LLDP TLVs or not. By default max-frame-size LLDP TLVs are advertised.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>port_vlan_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.1.0</div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>This command can be used to select whether to advertise port-vlan-id LLDP TLVs or not. By default port-vlan-id LLDP TLVs are advertised.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>power_management</b>
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
                        <div>This command can be used to select whether to advertise power-management LLDP TLVs or not. By default power-management LLDP TLVs are advertised.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vlan_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.1.0</div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>This command can be used to select whether to advertise vlan-name LLDP TLVs or not. By default vlan-name LLDP TLVs are advertised.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>tlv_set</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>This command can be used to configure an IPv4 or IPv6 management address that will be used to advertise by LLDP on an interface</div>
                        <div>This command is supported only on physical interfaces and not on logical interfaces.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ipv4_management_address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>To configure IPv4 management address for LLDP in A.B.C.D format</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ipv6_management_address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>To configure IPv6 management address for LLDP in A:B::C:D format</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vlan_name_tlv</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.1.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>This command can be used to configure the vlan list for the Vlan name TLV advertisement.</div>
                        <div>This command is supported only on physical interfaces and not on logical interfaces.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>allowed_vlans</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>This command can be used to configure the vlan list for the Vlan name TLV advertisement.</div>
                        <div>Multiple Vlans or Vlan ranges can be configured.</div>
                        <div>Ranges are specified by a start and end Vlan value separated by hyphen.</div>
                        <div>Vlans configured should be in the range 1-4094.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vlan</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configures the specified VLAN or VLAN range.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>max_tlv_count</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>This command can be used to configure the maximum number of Vlan name TLVs that can be advertised on the interface.</div>
                        <div>Range is 1-128 and the default value is 10.</div>
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
                        <div>The state specifies the type of configuration update to be performed on the device.</div>
                        <div>If the state is &quot;merged&quot;, merge specified attributes with existing configured attributes.</div>
                        <div>For &quot;deleted&quot;, delete the specified attributes from existing configuration.</div>
                        <div>For &quot;replaced&quot;, replaces lldp interface configuration of the specified interfaces with provided configuration.</div>
                        <div>For &quot;overridden&quot;, overrides all on-device lldp interface configurations with the provided configuration.</div>
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
    # sonic# show running-configuration interface Ethernet 1
    # !
    # interface Ethernet1
    #  mtu 9100
    #  speed 25000
    #  unreliable-los auto
    #  no shutdown
    #  lldp transmit
    #  network-policy 1
    #  lldp tlv-set management-address ipv4 10.1.1.2
    # sonic#

    - name: Delete LLDP interface configurations
      dellemc.enterprise_sonic.sonic_lldp_interfaces:
        config:
          - name: Ethernet1
            mode: transmit
            network_policy: 1
            tlv_set:
              ipv4_management_address: 10.1.1.2
        state: deleted

    # After state:
    # ------------
    # sonic# show running-configuration interface Ethernet 1
    # !
    # interface Ethernet1
    #  mtu 9100
    #  speed 25000
    #  unreliable-los auto
    #  no shutdown
    # sonic#


    # Using "deleted" state
    #
    # Before state:
    # -------------
    # sonic# show running-configuration interface
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 25000
    #  unreliable-los auto
    #  no shutdown
    # !
    # interface Ethernet1
    #  mtu 9100
    #  speed 25000
    #  unreliable-los auto
    #  no shutdown
    # !
    # sonic#

    - name: Delete default LLDP Interface configurations
      dellemc.enterprise_sonic.sonic_lldp_interfaces:
        config:
          - name: Ethernet1
            tlv_select:
              power-management: true
              port_vlan_id: true
              vlan_name: true
              link_aggregation: true
              max_frame_size: true
            med_tlv_select:
              network_policy: true
        state: deleted

    # After State:
    # ------------
    # sonic# show running-configuration interface
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 25000
    #  unreliable-los auto
    #  no shutdown
    # !
    # interface Ethernet1
    #  mtu 9100
    #  speed 25000
    #  unreliable-los auto
    #  no shutdown
    #  no lldp med-tlv-select network-policy
    #  no lldp tlv-select power-management
    #  no lldp tlv-select port-vlan-id
    #  no lldp tlv-select vlan-name
    #  no lldp tlv-select link-aggregation
    #  no lldp tlv-select max-frame-size
    # sonic#


    # Using "deleted" state
    #
    # Before state:
    # -------------
    # sonic# show running-configuration interface
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 25000
    #  unreliable-los auto
    #  no shutdown
    #  lldp receive
    #  lldp tlv-set management-address ipv4 20.1.1.1
    #  lldp vlan-name-tlv allowed Vlan 10,15-20
    #  lldp vlan-name-tlv max-tlv-count 15
    # !
    # interface Ethernet1
    #  mtu 9100
    #  speed 25000
    #  unreliable-los auto
    #  no shutdown
    #  lldp transmit
    #  lldp tlv-set management-address ipv4 21.1.1.1
    #  lldp vlan-name-tlv allowed Vlan 10,15-20
    #  lldp vlan-name-tlv max-tlv-count 15
    # !
    # sonic#

    - name: Delete default LLDP Interface configurations
      dellemc.enterprise_sonic.sonic_lldp_interfaces:
        config:
          - name: Ethernet0
            vlan_name_tlv:
              allowed_vlans:
                - vlan: 10
                - vlan: 15-20
              max_tlv_count: 15
          - name: Ethernet1
        state: deleted

    # After state:
    # ------------
    # sonic# show running-configuration interface
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 25000
    #  unreliable-los auto
    #  no shutdown
    #  lldp receive
    #  lldp tlv-set management-address ipv4 20.1.1.1
    # !
    # interface Ethernet1
    #  mtu 9100
    #  speed 25000
    #  unreliable-los auto
    #  no shutdown
    # sonic#


    # Using "merged" state
    #
    # Before state:
    # -------------
    # sonic# show running-configuration interface
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 25000
    #  unreliable-los auto
    #  no shutdown
    # !
    # interface Ethernet1
    #  mtu 9100
    #  speed 25000
    #  unreliable-los auto
    #  no shutdown
    #  no lldp enable
    # !
    # sonic#

    - name: Modify LLDP Interface configurations
      dellemc.enterprise_sonic.sonic_lldp_interfaces:
        config:
          - name: Ethernet1
            enable: true
            mode: transmit
            network_policy: 2
            med_tlv_select:
              power_management: true
            tlv_set:
              ipv4_management_address: 10.1.1.2
            vlan_name_tlv:
              allowed_vlans:
                - vlan: 10
                - vlan: 15-20
              max_tlv_count: 15
        state: merged

    # After State:
    # ------------
    # sonic# show running-configuration interface
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 25000
    #  unreliable-los auto
    #  no shutdown
    # !
    # interface Ethernet1
    #  mtu 9100
    #  speed 25000
    #  unreliable-los auto
    #  no shutdown
    #  lldp transmit
    #  network-policy 2
    #  lldp tlv-set management-address ipv4 10.1.1.2
    #  lldp vlan-name-tlv allowed Vlan 10,15-20
    #  lldp vlan-name-tlv max-tlv-count 15
    # sonic#

    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/5
    #  mtu 9100
    #  speed 10000
    #  unreliable-los auto
    #  no shutdown
    #  lldp tlv-set management-address ipv6 10::1
    #  no lldp med-tlv-select network-policy
    #  no lldp med-tlv-select power-management
    #  lldp vlan-name-tlv allowed Vlan 10,15-20
    #  lldp vlan-name-tlv max-tlv-count 15
    #
    # !
    # interface Eth1/6
    #  mtu 9100
    #  speed 10000
    #  unreliable-los auto
    #  no shutdown
    #  no lldp med-tlv-select power-management
    #  no lldp tlv-select power-management

    - name: Replace LLDP interface configurations
      dellemc.enterprise_sonic.sonic_lldp_interfaces:
        config:
          - name: Eth1/5
            mode: receive
            tlv_set:
              ipv6_management_address: '30::1'
            med_tlv_select:
              network_policy: false
            vlan_name_tlv:
              allowed_vlans:
                - vlan: 20-30
              max_tlv_count: 20
        state: replaced

    # After State:

    # ------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/5
    #  mtu 9100
    #  speed 10000
    #  unreliable-los auto
    #  no shutdown
    #  lldp receive
    #  lldp tlv-set management-address ipv6 30::1
    #  no lldp med-tlv-select network-policy
    #  lldp vlan-name-tlv allowed Vlan 20-30
    #  lldp vlan-name-tlv max-tlv-count 20
    # !
    # interface Eth1/6
    #  mtu 9100
    #  speed 10000
    #  unreliable-los auto
    #  no shutdown
    #  no lldp med-tlv-select power-management
    #  no lldp tlv-select power-management

    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface
    # interface Eth1/5
    #  mtu 9100
    #  speed 10000
    #  unreliable-los auto
    #  no shutdown
    #  lldp transmit
    #  lldp tlv-set management-address ipv6 30::2
    # !
    # interface Eth1/6
    #  mtu 9100
    #  speed 10000
    #  unreliable-los auto
    #  no shutdown
    #  lldp transmit
    #  lldp tlv-set management-address ipv4 40.1.1.1

    - name: Override LLDP interface configurations
      dellemc.enterprise_sonic.sonic_lldp_interfaces:
        config:
          - name: Eth1/5
            mode: receive
            tlv_set:
              ipv4_management_address: '10.1.1.2'
            vlan_name_tlv:
              allowed_vlans:
                - vlan: 10
                - vlan: 15-20
              max_tlv_count: 15
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/5
    #  mtu 9100
    #  speed 10000
    #  unreliable-los auto
    #  no shutdown
    #  lldp receive
    #  lldp tlv-set management-address ipv4 10.1.1.2
    #  lldp vlan-name-tlv allowed Vlan 10,15-20
    #  lldp vlan-name-tlv max-tlv-count 15
    # !
    # interface Eth1/6
    #  mtu 9100
    #  speed 10000
    #  unreliable-los auto
    #  no shutdown



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
                            <div>The generated configuration from module invocation.</div>
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

- Divya Balasubramanian(@divya-balasubramania)
