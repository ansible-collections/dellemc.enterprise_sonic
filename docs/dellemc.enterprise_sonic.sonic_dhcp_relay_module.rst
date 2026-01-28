.. _dellemc.enterprise_sonic.sonic_dhcp_relay_module:


*****************************************
dellemc.enterprise_sonic.sonic_dhcp_relay
*****************************************

**Manage DHCP and DHCPv6 relay configurations on SONiC**


Version added: 2.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of DHCP and DHCPv6 relay parameters on Layer 3 interfaces of devices running SONiC.
- Layer 3 interface and VRF name need to be created earlier in the device.




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
                        <div>Specifies the DHCP and DHCPv6 relay configurations.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ipv4</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>DHCP relay configurations to be set for the interface mentioned in name option.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>circuit_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>%h:%p</li>
                                    <li>%i</li>
                                    <li>%p</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the DHCP relay circuit-id format.</div>
                        <div><code>%h:%p</code> - Hostname followed by interface name eg. sonic:Vlan100</div>
                        <div><code>%i</code> - Name of the physical interface eg. Eth1/2</div>
                        <div><code>%p</code> - Name of the interface eg. Vlan100</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>link_select</b>
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
                        <div>Enable link selection suboption.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>max_hop_count</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the maximum hop count for DHCP relay packets.</div>
                        <div>The range is from 1 to 16.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>policy_action</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>append</li>
                                    <li>discard</li>
                                    <li>replace</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the policy for handling of DHCP relay options.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>server_addresses</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of DHCP server IPv4 addresses.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IPv4 address of the DHCP server.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Specifies the DHCP relay source interface.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vrf_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies name of the VRF in which the DHCP server resides.</div>
                        <div>This option is not used with state <em>deleted</em>.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vrf_select</b>
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
                        <div>Enable VRF selection suboption.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ipv6</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>DHCPv6 relay configurations to be set for the interface mentioned in name option.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>max_hop_count</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the maximum hop count for DHCPv6 relay packets.</div>
                        <div>The range is from 1 to 16.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>server_addresses</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of DHCPv6 server IPv6 addresses.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IPv6 address of the DHCPv6 server.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Specifies the DHCPv6 relay source interface.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vrf_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies name of the VRF in which the DHCPv6 server resides.</div>
                        <div>This option is used only with state <em>merged</em>.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vrf_select</b>
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
                        <div>Enable VRF selection suboption.</div>
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
                        <div>Full name of the Layer 3 interface, i.e. Eth1/1.</div>
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
                        <div>The state of the configuration after module completion.</div>
                        <div><code>merged</code> - Merges provided DHCP and DHCPv6 relay configuration with on-device configuration.</div>
                        <div><code>deleted</code> - Deletes on-device DHCP and DHCPv6 relay configuration.</div>
                        <div><code>replaced</code> - Replaces on-device DHCP and DHCPv6 relay configuration of the specified interfaces with provided configuration.</div>
                        <div><code>overridden</code> - Overrides all on-device DHCP and DHCPv6 relay configurations with the provided configuration.</div>
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
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 81.1.1.1/24
    #  ip dhcp-relay 91.1.1.1 92.1.1.1 vrf VrfReg1
    #  ip dhcp-relay max-hop-count 5
    #  ip dhcp-relay vrf-select
    #  ip dhcp-relay policy-action append
    #  ipv6 address 81::1/24
    #  ipv6 dhcp-relay 91::1 92::1
    #  ipv6 dhcp-relay max-hop-count 5
    # !
    # interface Eth1/2
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 61.1.1.1/24
    #  ip dhcp-relay 71.1.1.1 72.1.1.1 73.1.1.1
    #  ip dhcp-relay source-interface Vlan100
    #  ip dhcp-relay link-select
    #  ip dhcp-relay circuit-id %h:%p
    # !

    - name: Delete DHCP and DHCPv6 relay configurations
      dellemc.enterprise_sonic.sonic_dhcp_relay:
        config:
          - name: 'Eth1/1'
            ipv4:
              server_addresses:
                - address: '92.1.1.1'
              vrf_select: true
              max_hop_count: 5
            ipv6:
              server_addresses:
                - address: '91::1'
                - address: '92::1'
          - name: 'Eth1/2'
            ipv4:
              server_addresses:
                - address: '71.1.1.1'
                - address: '72.1.1.1'
              source_interface: 'Vlan100'
              link_select: true
              circuit_id: '%h:%p'
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 81.1.1.1/24
    #  ip dhcp-relay 91.1.1.1 vrf VrfReg1
    #  ip dhcp-relay policy-action append
    #  ipv6 address 81::1/24
    # !
    # interface Eth1/2
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 61.1.1.1/24
    #  ip dhcp-relay 73.1.1.1
    # !


    # Using "deleted" state
    #
    # NOTE: Support is provided in the dhcp_relay resource module for deletion of all attributes for a
    # given address family (IPv4 or IPv6) by using a "special" YAML sequence specifying a server address list
    # containing a single "blank" IP address under the target address family. The following example shows
    # a task using this syntax for deletion of all DHCP (IPv4) configurations for an interface, but the
    # equivalent syntax is supported for DHCPv6 (IPv6) as well.
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 81.1.1.1/24
    #  ip dhcp-relay 91.1.1.1 92.1.1.1 vrf VrfReg1
    #  ip dhcp-relay max-hop-count 5
    #  ip dhcp-relay vrf-select
    #  ip dhcp-relay policy-action append
    #  ipv6 address 81::1/24
    #  ipv6 dhcp-relay 91::1 92::1
    #  ipv6 dhcp-relay max-hop-count 5
    # !
    # interface Eth1/2
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 61.1.1.1/24
    #  ip dhcp-relay 71.1.1.1 72.1.1.1 73.1.1.1
    #  ip dhcp-relay source-interface Vlan100
    #  ip dhcp-relay link-select
    #  ip dhcp-relay circuit-id %h:%p
    # !

    - name: Delete all IPv4 DHCP relay configurations for interface Eth1/1
      dellemc.enterprise_sonic.sonic_dhcp_relay:
        config:
          - name: 'Eth1/1'
            ipv4:
              server_addresses:
                - address:
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 81.1.1.1/24
    #  ipv6 address 81::1/24
    #  ipv6 dhcp-relay 91::1 92::1
    #  ipv6 dhcp-relay max-hop-count 5
    # !
    # interface Eth1/2
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 61.1.1.1/24
    #  ip dhcp-relay 71.1.1.1 72.1.1.1 73.1.1.1
    #  ip dhcp-relay source-interface Vlan100
    #  ip dhcp-relay link-select
    #  ip dhcp-relay circuit-id %h:%p
    # !


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 81.1.1.1/24
    #  ip dhcp-relay 91.1.1.1 92.1.1.1 vrf VrfReg1
    #  ip dhcp-relay max-hop-count 5
    #  ip dhcp-relay vrf-select
    #  ip dhcp-relay policy-action append
    #  ipv6 address 81::1/24
    #  ipv6 dhcp-relay 91::1 92::1
    #  ipv6 dhcp-relay max-hop-count 5
    # !
    # interface Eth1/2
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 61.1.1.1/24
    #  ip dhcp-relay 71.1.1.1 72.1.1.1 73.1.1.1
    #  ip dhcp-relay source-interface Vlan100
    #  ip dhcp-relay link-select
    #  ip dhcp-relay circuit-id %h:%p
    # !

    - name: Delete all DHCP and DHCPv6 relay configurations for interface Eth1/1
      dellemc.enterprise_sonic.sonic_dhcp_relay:
        config:
          - name: 'Eth1/1'
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 81.1.1.1/24
    #  ipv6 address 81::1/24
    # !
    # interface Eth1/2
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 61.1.1.1/24
    #  ip dhcp-relay 71.1.1.1 72.1.1.1 73.1.1.1
    #  ip dhcp-relay source-interface Vlan100
    #  ip dhcp-relay link-select
    #  ip dhcp-relay circuit-id %h:%p
    # !


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 81.1.1.1/24
    #  ip dhcp-relay 91.1.1.1 92.1.1.1 vrf VrfReg1
    #  ip dhcp-relay max-hop-count 5
    #  ip dhcp-relay vrf-select
    #  ip dhcp-relay policy-action append
    #  ipv6 address 81::1/24
    #  ipv6 dhcp-relay 91::1 92::1
    #  ipv6 dhcp-relay max-hop-count 5
    # !
    # interface Eth1/2
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 61.1.1.1/24
    #  ip dhcp-relay 71.1.1.1 72.1.1.1 73.1.1.1
    #  ip dhcp-relay source-interface Vlan100
    #  ip dhcp-relay link-select
    #  ip dhcp-relay circuit-id %h:%p
    # !

    - name: Delete all DHCP and DHCPv6 relay configurations
      dellemc.enterprise_sonic.sonic_dhcp_relay:
        config:
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 81.1.1.1/24
    #  ipv6 address 81::1/24
    # !
    # interface Eth1/2
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 61.1.1.1/24
    # !


    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 81.1.1.1/24
    #  ipv6 address 81::1/24
    # !
    # interface Eth1/2
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 61.1.1.1/24
    #  ip dhcp-relay 71.1.1.1 72.1.1.1
    # !

    - name: Add DHCP and DHCPv6 relay configurations
      dellemc.enterprise_sonic.sonic_dhcp_relay:
        config:
          - name: 'Eth1/1'
            ipv4:
              server_addresses:
                - address: '91.1.1.1'
                - address: '92.1.1.1'
              vrf_name: 'VrfReg1'
              vrf_select: true
              max_hop_count: 5
              policy_action: 'append'
            ipv6:
              server_addresses:
                - address: '91::1'
                - address: '92::1'
              max_hop_count: 5
          - name: 'Eth1/2'
            ipv4:
              server_addresses:
                - address: '73.1.1.1'
              source_interface: 'Vlan100'
              link_select: true
              circuit_id: '%h:%p'
        state: merged

    # After state:
    # ------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 81.1.1.1/24
    #  ip dhcp-relay 91.1.1.1 92.1.1.1 vrf VrfReg1
    #  ip dhcp-relay max-hop-count 5
    #  ip dhcp-relay vrf-select
    #  ip dhcp-relay policy-action append
    #  ipv6 address 81::1/24
    #  ipv6 dhcp-relay 91::1 92::1
    #  ipv6 dhcp-relay max-hop-count 5
    # !
    # interface Eth1/2
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 61.1.1.1/24
    #  ip dhcp-relay 71.1.1.1 72.1.1.1 73.1.1.1
    #  ip dhcp-relay source-interface Vlan100
    #  ip dhcp-relay link-select
    #  ip dhcp-relay circuit-id %h:%p
    # !


    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 81.1.1.1/24
    #  ip dhcp-relay 91.1.1.1 92.1.1.1 vrf VrfReg1
    #  ip dhcp-relay max-hop-count 5
    #  ip dhcp-relay vrf-select
    #  ip dhcp-relay policy-action append
    #  ipv6 address 81::1/24
    #  ipv6 dhcp-relay 91::1 92::1
    #  ipv6 dhcp-relay max-hop-count 5
    # !
    # interface Eth1/2
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 61.1.1.1/24
    #  ip dhcp-relay 71.1.1.1 72.1.1.1 73.1.1.1
    #  ip dhcp-relay source-interface Vlan100
    #  ip dhcp-relay link-select
    #  ip dhcp-relay circuit-id %h:%p
    #  ipv6 address 61::1/24
    #  ipv6 dhcp-relay 71::1 72::1
    # !
    # interface Eth1/3
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  shutdown
    #  ip address 41.1.1.1/24
    #  ip dhcp-relay 51.1.1.1 52.1.1.1
    #  ip dhcp-relay circuit-id %h:%p
    #  ipv6 address 41::1/24
    #  ipv6 dhcp-relay 51::1 52::1
    # !

    - name: Replace DHCP and DHCPv6 relay configurations of specified interfaces
      dellemc.enterprise_sonic.sonic_dhcp_relay:
        config:
          - name: 'Eth1/1'
            ipv4:
              server_addresses:
                - address: '91.1.1.1'
                - address: '93.1.1.1'
                - address: '95.1.1.1'
              vrf_name: 'VrfReg1'
              vrf_select: true
            ipv6:
              server_addresses:
                - address: '93::1'
                - address: '94::1'
              source_interface: 'Vlan100'
          - name: 'Eth1/2'
            ipv4:
              server_addresses:
                - address: '73.1.1.1'
              circuit_id: '%h:%p'
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 81.1.1.1/24
    #  ip dhcp-relay 91.1.1.1 93.1.1.1 95.1.1.1 vrf VrfReg1
    #  ip dhcp-relay vrf-select
    #  ipv6 address 81::1/24
    #  ipv6 dhcp-relay 93::1 94::1
    #  ipv6 dhcp-relay source-interface Vlan100
    # !
    # interface Eth1/2
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 61.1.1.1/24
    #  ip dhcp-relay 73.1.1.1
    #  ip dhcp-relay circuit-id %h:%p
    #  ipv6 address 61::1/24
    # !
    # interface Eth1/3
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  shutdown
    #  ip address 41.1.1.1/24
    #  ip dhcp-relay 51.1.1.1 52.1.1.1
    #  ip dhcp-relay circuit-id %h:%p
    #  ipv6 address 41::1/24
    #  ipv6 dhcp-relay 51::1 52::1
    # !


    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 81.1.1.1/24
    #  ip dhcp-relay 91.1.1.1 92.1.1.1 vrf VrfReg1
    #  ip dhcp-relay max-hop-count 5
    #  ip dhcp-relay vrf-select
    #  ip dhcp-relay policy-action append
    #  ipv6 address 81::1/24
    #  ipv6 dhcp-relay 91::1 92::1
    #  ipv6 dhcp-relay max-hop-count 5
    # !
    # interface Eth1/2
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 61.1.1.1/24
    #  ip dhcp-relay 71.1.1.1 72.1.1.1 73.1.1.1
    #  ip dhcp-relay source-interface Vlan100
    #  ip dhcp-relay link-select
    #  ip dhcp-relay circuit-id %h:%p
    #  ipv6 address 61::1/24
    #  ipv6 dhcp-relay 71::1 72::1
    # !
    # interface Eth1/3
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  shutdown
    #  ip address 41.1.1.1/24
    #  ip dhcp-relay 51.1.1.1 52.1.1.1
    #  ip dhcp-relay circuit-id %h:%p
    #  ipv6 address 41::1/24
    #  ipv6 dhcp-relay 51::1 52::1
    # !

    - name: Override DHCP and DHCPv6 relay configurations
      dellemc.enterprise_sonic.sonic_dhcp_relay:
        config:
          - name: 'Eth1/1'
            ipv4:
              server_addresses:
                - address: '91.1.1.1'
                - address: '93.1.1.1'
                - address: '95.1.1.1'
              vrf_name: 'VrfReg1'
              vrf_select: true
            ipv6:
              server_addresses:
                - address: '93::1'
                - address: '94::1'
              source_interface: 'Vlan100'
          - name: 'Eth1/2'
            ipv4:
              server_addresses:
                - address: '73.1.1.1'
              circuit_id: '%h:%p'
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 81.1.1.1/24
    #  ip dhcp-relay 91.1.1.1 93.1.1.1 95.1.1.1 vrf VrfReg1
    #  ip dhcp-relay vrf-select
    #  ipv6 address 81::1/24
    #  ipv6 dhcp-relay 93::1 94::1
    #  ipv6 dhcp-relay source-interface Vlan100
    # !
    # interface Eth1/2
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 61.1.1.1/24
    #  ip dhcp-relay 73.1.1.1
    #  ip dhcp-relay circuit-id %h:%p
    #  ipv6 address 61::1/24
    # !
    # interface Eth1/3
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  shutdown
    #  ip address 41.1.1.1/24
    #  ipv6 address 41::1/24
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
