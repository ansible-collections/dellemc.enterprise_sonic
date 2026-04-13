.. _dellemc.enterprise_sonic.sonic_l3_interfaces_module:


********************************************
dellemc.enterprise_sonic.sonic_l3_interfaces
********************************************

**Configure the IPv4 and IPv6 parameters on Interfaces such as, Eth, LAG, VLAN, and loopback**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Configures Layer 3 interface settings on devices running Enterprise SONiC Distribution by Dell Technologies. This module provides configuration management of IPv4 and IPv6 parameters on Ethernet interfaces of devices running Enterprise SONiC.




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
                        <div>A list of l3_interfaces configurations.</div>
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
                        <div>ipv4 configurations to be set for the Layer 3 interface mentioned in name option.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>addresses</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of IPv4 addresses to be set.</div>
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
                        <div>IPv4 address to be set in the format &lt;ipv4 address&gt;/&lt;mask&gt; for example, 192.0.2.1/24.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>secondary</b>
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
                        <div>secondary flag of the ip address.</div>
                        <div>Functional default is &#x27;false&#x27;</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>anycast_addresses</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of IPv4 addresses to be set for anycast.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>proxy_arp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.1.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configurations parameters for ipv4 proxy ARP</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mode</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>DISABLE</li>
                                    <li>REMOTE_ONLY</li>
                                    <li>ALL</li>
                        </ul>
                </td>
                <td>
                        <div>Modes for proxy_arp</div>
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
                        <div>ipv6 configurations to be set for the Layer 3 interface mentioned in name option.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>addresses</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of IPv6 addresses to be set.</div>
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
                        <div>IPv6 address to be set in the address format is &lt;ipv6 address&gt;/&lt;mask&gt; for example, 2001:db8:2201:1::1/64.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>eui64</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 2.5.0</div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Flag to indicate whether it is eui64 address</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>anycast_addresses</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.1.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of IPv6 anycast addresses.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>autoconf</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 2.5.0</div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>autoconfiguration flag</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dad</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 2.5.0</div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ENABLE</li>
                                    <li>DISABLE</li>
                                    <li>DISABLE_IPV6_ON_FAILURE</li>
                        </ul>
                </td>
                <td>
                        <div>IPv6 nd dad related configs.</div>
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
                        <div>enabled flag of the ipv6.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>nd_proxy</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.1.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configurations parameters for ipv6 ND-proxy</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mode</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>DISABLE</li>
                                    <li>REMOTE_ONLY</li>
                                    <li>ALL</li>
                        </ul>
                </td>
                <td>
                        <div>Modes for nd_proxy</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>nd_proxy_rules</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of ipv6 prefixes (subnets) for which this interface is to serve as an nd proxy</div>
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
                        <div>Full name of the interface, for example, Eth1/3.</div>
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
    # interface Ethernet20
    #  mtu 9100
    #  speed 100000
    #  shutdown
    #  ip address 83.1.1.1/16
    #  ip address 84.1.1.1/16 secondary
    #  ipv6 address 83::1/16
    #  ipv6 address 84::1/16
    #  ipv6 address 85::/64 eui-64
    #  ipv6 enable
    #  ipv6 address autoconfig
    #  ipv6 nd dad enable
    #  ip proxy-arp enable remote-only
    #  ipv6 nd-proxy enable all
    # !
    # interface Ethernet24
    #  mtu 9100
    #  speed 100000
    #  shutdown
    #  ip address 91.1.1.1/16
    #  ip address 92.1.1.1/16 secondary
    #  ipv6 address 90::1/16
    #  ipv6 address 91::1/16
    #  ipv6 address 92::1/16
    #  ipv6 address 93::1/16
    # !
    # interface Vlan501
    #  ip anycast-address 11.12.13.14/12
    #  ip anycast-address 1.2.3.4/22
    #  ipv6 anycast-address 101::101/64
    #  ipv6 anycast-address 102::102/64
    # !

    - name: delete l3 interface attributes
      dellemc.enterprise_sonic.sonic_l3_interfaces:
        config:
          - name: Ethernet20
            ipv4:
              proxy_arp:
                mode: REMOTE_ONLY
              addresses:
                - address: 83.1.1.1/16
                - address: 84.1.1.1/16
            ipv6:
              addresses:
                - address: 85::/64
          - name: Ethernet24
            ipv6:
              enabled: true
              addresses:
                - address: 91::1/16
          - name: Vlan501
            ipv4:
              anycast_addresses:
                - 11.12.13.14/12
            ipv6:
              anycast_addresses:
                - 101::101/64
        state: deleted

    #
    # After state:
    # ------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Ethernet20
    #  mtu 9100
    #  speed 100000
    #  shutdown
    #  ipv6 address 83::1/16
    #  ipv6 address 84::1/16
    #  ipv6 enable
    #  ipv6 address autoconfig
    #  ipv6 nd dad enable
    #  ipv6 nd-proxy enable all
    # !
    # interface Ethernet24
    #  mtu 9100
    #  speed 100000
    #  shutdown
    #  ip address 91.1.1.1/16
    #  ip address 92.1.1.1/16 secondary
    #  ipv6 address 90::1/16
    #  ipv6 address 92::1/16
    #  ipv6 address 93::1/16
    # !
    # interface Vlan501
    #  ip anycast-address 1.2.3.4/22
    #  ipv6 anycast-address 102::102/64
    # !

    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Ethernet20
    #  mtu 9100
    #  speed 100000
    #  shutdown
    #  ip address 83.1.1.1/16
    #  ip address 84.1.1.1/16 secondary
    #  ipv6 address 83::1/16
    #  ipv6 address 84::1/16
    #  ipv6 address 85::/64 eui-64
    #  ipv6 enable
    #  ipv6 address autoconfig
    #  ipv6 nd dad enable
    #  ip proxy-arp enable remote-only
    #  ipv6 nd-proxy enable all
    #  ipv6 nd-proxy rule prefix 5001::/24
    # !
    # interface Ethernet24
    #  mtu 9100
    #  speed 100000
    #  shutdown
    #  ip address 91.1.1.1/16
    #  ipv6 address 90::1/16
    #  ipv6 address 91::1/16
    #  ipv6 address 92::1/16
    #  ipv6 address 93::1/16
    #  ip proxy-arp enable all
    #  ipv6 nd-proxy enable remote-only
    #  ipv6 nd-proxy rule prefix 6001::/24
    # !
    # interface Vlan501
    #  ip anycast-address 11.12.13.14/12
    #  ip anycast-address 1.2.3.4/22
    #  ipv6 anycast-address 101::101/64
    #  ipv6 anycast-address 102::102/64
    # !

    - name: delete all l3 interface
      dellemc.enterprise_sonic.sonic_l3_interfaces:
        config:
        state: deleted

    #
    # After state:
    # ------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Ethernet20
    #  mtu 9100
    #  speed 100000
    #  shutdown
    # !
    # interface Ethernet24
    #  mtu 9100
    #  speed 100000
    #  shutdown
    # !
    # interface Vlan501
    # !

    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Ethernet20
    #  mtu 9100
    #  speed 100000
    #  shutdown
    # !
    # interface Ethernet24
    #  mtu 9100
    #  speed 100000
    #  shutdown
    # !
    # interface Vlan501
    #  ip anycast-address 1.2.3.4/22
    #  ipv6 anycast-address 101::101/64
    # !

    - name: Add l3 interface configurations
      dellemc.enterprise_sonic.sonic_l3_interfaces:
        config:
          - name: Ethernet20
            ipv4:
              addresses:
                - address: 83.1.1.1/16
                - address: 84.1.1.1/16
                  secondary: true
              proxy_arp:
                mode: REMOTE_ONLY
            ipv6:
              enabled: true
              dad: ENABLE
              autoconf: true
              addresses:
                - address: 83::1/16
                - address: 84::1/16
                - address: 85::/64
                  eui64: true
          - name: Ethernet24
            ipv4:
              addresses:
                - address: 91.1.1.1/16
            ipv6:
              addresses:
                - address: 90::1/16
                - address: 91::1/16
                - address: 92::1/16
                - address: 93::1/16
              nd_proxy:
                mode: REMOTE_ONLY
                nd_proxy_rules:
                  - 6001::/24
          - name: Vlan501
            ipv4:
              anycast_addresses:
                - 11.12.13.14/12
            ipv6:
              anycast_addresses:
                - 102::102/64
        state: merged

    # After state:
    # ------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Ethernet20
    #  mtu 9100
    #  speed 100000
    #  shutdown
    #  ip address 83.1.1.1/16
    #  ip address 84.1.1.1/16 secondary
    #  ip proxy-arp enable remote-only
    #  ipv6 address 83::1/16
    #  ipv6 address 84::1/16
    #  ipv6 address 85::/64 eui-64
    #  ipv6 enable
    #  ipv6 address autoconfig
    #  ipv6 nd dad enable
    # !
    # interface Ethernet24
    #  mtu 9100
    #  speed 100000
    #  shutdown
    #  ip address 91.1.1.1/16
    #  ipv6 address 90::1/16
    #  ipv6 address 91::1/16
    #  ipv6 address 92::1/16
    #  ipv6 address 93::1/16
    #  ipv6 nd-proxy enable remote-only
    #  ipv6 nd-proxy rule prefix 6001::/24
    # !
    # interface Vlan501
    #  ip anycast-address 1.2.3.4/22
    #  ip anycast-address 11.12.13.14/12
    #  ipv6 anycast-address 101::101/64
    #  ipv6 anycast-address 102::102/64
    # !

    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Ethernet20
    #  mtu 9100
    #  speed 100000
    #  shutdown
    #  ip address 83.1.1.1/16
    #  ip address 84.1.1.1/16 secondary
    #  ipv6 address 83::1/16
    #  ipv6 address 84::1/16
    #  ipv6 enable
    # !
    # interface Ethernet24
    #  mtu 9100
    #  speed 100000
    #  shutdown
    #  ip address 91.1.1.1/16
    #  ipv6 address 90::1/16
    #  ipv6 address 91::1/16
    #  ipv6 address 92::1/16
    #  ipv6 address 93::1/16
    # !

    - name: Replace l3 interface
      dellemc.enterprise_sonic.sonic_l3_interfaces:
        config:
          - name: Ethernet20
            ipv4:
              - address: 81.1.1.1/16
            proxy_arp:
              mode: ALL
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Ethernet20
    #  mtu 9100
    #  speed 100000
    #  shutdown
    #  ip address 81.1.1.1/16
    #  ip proxy-arp enable all
    # !
    # interface Ethernet24
    #  mtu 9100
    #  speed 100000
    #  shutdown
    #  ip address 91.1.1.1/16
    #  ipv6 address 90::1/16
    #  ipv6 address 91::1/16
    #  ipv6 address 92::1/16
    #  ipv6 address 93::1/16
    # !

    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Ethernet20
    #  mtu 9100
    #  speed 100000
    #  shutdown
    #  ip address 83.1.1.1/16
    #  ip address 84.1.1.1/16 secondary
    #  ip proxy-arp enable all
    #  ipv6 address 83::1/16
    #  ipv6 address 84::1/16
    #  ipv6 enable
    #  ipv6 nd-proxy enable remote-only
    #  ipv6 nd-proxy rule prefix 6001::/24
    # !
    # interface Ethernet24
    #  mtu 9100
    #  speed 100000
    #  shutdown
    #  ip address 91.1.1.1/16
    #  ipv6 address 90::1/16
    #  ipv6 address 91::1/16
    #  ipv6 address 92::1/16
    #  ipv6 address 93::1/16
    # !

    - name: Replace l3 interface
      dellemc.enterprise_sonic.sonic_l3_interfaces:
        config:
          - name: Ethernet20
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Ethernet20
    #  mtu 9100
    #  speed 100000
    #  shutdown
    # !
    # interface Ethernet24
    #  mtu 9100
    #  speed 100000
    #  shutdown
    #  ip address 91.1.1.1/16
    #  ipv6 address 90::1/16
    #  ipv6 address 91::1/16
    #  ipv6 address 92::1/16
    #  ipv6 address 93::1/16
    # !

    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Ethernet20
    #  mtu 9100
    #  speed 100000
    #  shutdown
    #  ip address 83.1.1.1/16
    #  ip address 84.1.1.1/16 secondary
    #  ipv6 address 83::1/16
    #  ipv6 address 84::1/16
    #  ipv6 address 85::/64 eui-64
    #  ipv6 enable
    #  ipv6 address autoconfig
    #  ipv6 nd dad enable
    #  ipv6 nd-proxy enable remote-only
    #  ipv6 nd-proxy rule prefix 6001::/24
    # !
    # interface Ethernet24
    #  mtu 9100
    #  speed 100000
    #  shutdown
    #  ip address 91.1.1.1/16
    #  ipv6 address 90::1/16
    #  ipv6 address 91::1/16
    #  ipv6 address 92::1/16
    #  ipv6 address 93::1/16
    # !

    - name: Override l3 interface
      dellemc.enterprise_sonic.sonic_l3_interfaces:
        config:
          - name: Ethernet24
            ipv4:
              - address: 81.1.1.1/16
            proxy_arp:
              mode: ALL
          - name: Vlan100
            ipv4:
              anycast_addresses:
                - 83.1.1.1/24
                - 85.1.1.12/24
            ipv6:
              anycast_addresses:
                - 83::1/24
                - 85::1/24
              nd_proxy:
                mode: REMOTE_ONLY
                nd_proxy_rules:
                  - 6001::/24
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Ethernet20
    #  mtu 9100
    #  speed 100000
    #  shutdown
    # !
    # interface Ethernet24
    #  mtu 9100
    #  speed 100000
    #  shutdown
    #  ip address 81.1.1.1/16
    #  ip proxy-arp enable all
    # !
    # interface Vlan100
    #  ip anycast-address 83.1.1.1/24
    #  ip anycast-address 85.1.1.12/24
    #  ipv6 anycast-address 83::1/24
    #  ipv6 anycast-address 85::1/24
    #  ipv6 nd-proxy enable remote-only
    #  ipv6 nd-proxy rule prefix 6001::/24

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

- Kumaraguru Narayanan (@nkumaraguru)
