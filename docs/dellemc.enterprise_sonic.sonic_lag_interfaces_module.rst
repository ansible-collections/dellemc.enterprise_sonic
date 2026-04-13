.. _dellemc.enterprise_sonic.sonic_lag_interfaces_module:


*********************************************
dellemc.enterprise_sonic.sonic_lag_interfaces
*********************************************

**Manage link aggregation group (LAG) interface parameters**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages attributes of link aggregation group (LAG) interfaces of devices running Enterprise SONiC Distribution by Dell Technologies.




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
                        <div>A list of LAG configurations.</div>
                        <div><em>adv_speed</em> and <em>speed</em> are mutually exclusive.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>adv_speed</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 4.0.0</div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>10</li>
                                    <li>100</li>
                                    <li>1000</li>
                                    <li>2500</li>
                                    <li>5000</li>
                                    <li>10000</li>
                                    <li>20000</li>
                                    <li>25000</li>
                                    <li>40000</li>
                                    <li>50000</li>
                                    <li>100000</li>
                                    <li>200000</li>
                                    <li>400000</li>
                                    <li>800000</li>
                        </ul>
                </td>
                <td>
                        <div>Advertised speed of the LAG interface measured in megabytes.</div>
                        <div>Supported speeds are dependent on the type of switch.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ethernet_segment</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 2.5.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies Ethernet segment.</div>
                        <div><em>esi_type</em> and <em>esi</em> can not be deleted separately.</div>
                        <div>When <em>state=deleted</em> and both <em>esi</em> and <em>df_preference</em> are not specifed, the entire Ethernet segment will be deleted.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>df_preference</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The preference for Designated Forwarder election method.</div>
                        <div>The range of df_preference value is from 1 to 65535.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>esi</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies value of Ethernet Segment Identifier.</div>
                        <div>Only <code>AUTO</code> is supported when <em>esi_type=auto_lacp</em> or <em>esi_type=auto_system_mac</em>.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>esi_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>auto_lacp</li>
                                    <li>auto_system_mac</li>
                                    <li>ethernet_segment_id</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies type of Ethernet Segment Identifier.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>fallback</b>
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
                        <div>Enable fallback mode.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>fast_rate</b>
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
                        <div>Enable LACP fast rate mode.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>graceful_shutdown</b>
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
                        <div>Enable graceful shutdown.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>lacp_individual</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.1.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies LACP individual configuration.</div>
                        <div>Applicable only when <em>mode=lacp</em>.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Enable LACP individual.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies LACP individual timeout in seconds.</div>
                        <div>The range is from 3 to 90.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>members</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The list of interfaces that are part of the group.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interfaces</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The list of interfaces that are part of the group.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>member</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
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
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>min_links</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.1.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies minimum number of links.</div>
                        <div>The range is from 1 to 32.</div>
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
                                    <li>static</li>
                                    <li>lacp</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies mode of the port-channel while creation.</div>
                        <div>Functional default is <code>lacp</code>.</div>
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
                        <div>ID of the LAG.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>speed</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 4.0.0</div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>10</li>
                                    <li>100</li>
                                    <li>1000</li>
                                    <li>2500</li>
                                    <li>5000</li>
                                    <li>10000</li>
                                    <li>20000</li>
                                    <li>25000</li>
                                    <li>40000</li>
                                    <li>50000</li>
                                    <li>100000</li>
                                    <li>200000</li>
                                    <li>400000</li>
                                    <li>800000</li>
                        </ul>
                </td>
                <td>
                        <div>LAG Interface speed measured in megabytes.</div>
                        <div>Supported speeds are dependent on the type of switch.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>system_mac</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.1.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies system MAC address for the portchannel.</div>
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
                        <div>The state that the configuration should be left in.</div>
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
    # interface Eth1/10
    #  mtu 9100
    #  speed 100000
    #  no shutdown
    # !
    # interface PortChannel10
    #  no shutdown
    #

    - name: Merge LAG interfaces configuration
      dellemc.enterprise_sonic.sonic_lag_interfaces:
        config:
          - name: PortChannel10
            fallback: true
            fast_rate: true
            graceful_shutdown: true
            members:
              interfaces:
                - member: Eth1/10
            system_mac: "12:12:12:12:12:12"
            ethernet_segment:
              esi_type: auto_lacp
              df_preference: 2222
          - name: PortChannel12
            min_links: 2
            members:
              interfaces:
                - member: Eth1/15
                - member: Eth1/16
                - member: Eth1/17
            lacp_individual:
              enable: true
              timeout: 30
        state: merged

    # After state:
    # ------------
    #
    # interface Eth1/10
    #  channel-group 10
    #  mtu 9100
    #  speed 100000
    #  no shutdown
    # !
    # interface Eth1/15
    #  channel-group 12
    #  mtu 9100
    #  speed 100000
    #  no shutdown
    # !
    # interface Eth1/16
    #  channel-group 12
    #  mtu 9100
    #  speed 100000
    #  no shutdown
    # !
    # interface Eth1/17
    #  channel-group 12
    #  mtu 9100
    #  speed 100000
    #  no shutdown
    # !
    # interface PortChannel10
    #  fast_rate
    #  fallback
    #  graceful-shutdown
    #  no shutdown
    #  system-mac 12:12:12:12:12:12
    #  !
    #  evpn ethernet-segment auto-lacp
    #   df-preference 2222
    #  !
    # !
    # interface PortChannel12
    #  min-links 2
    #  lacp individual
    #  lacp individual timeout 30
    #  no shutdown
    #

    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # interface Eth1/5
    #  channel-group 10
    #  mtu 9100
    #  speed 100000
    #  no shutdown
    # !
    # interface Eth1/7
    #  no channel-group
    #  mtu 9100
    #  speed 100000
    #  no shutdown
    # !
    # interface PortChannel10
    #  graceful-shutdown
    #  no shutdown
    #  system-mac 12:12:12:12:12:12
    #  !
    #  evpn ethernet-segment auto-lacp
    #   df-preference 2222
    #

    - name: Replace LAG configurations of specified LAG interfaces
      dellemc.enterprise_sonic.sonic_lag_interfaces:
        config:
          - name: PortChannel20
            members:
              interfaces:
                - member: Eth1/6
            system_mac: "14:14:14:14:14:14"
            ethernet_segment:
              esi_type: auto_system_mac
              df_preference: 6666
          - name: PortChannel10
            members:
              interfaces:
                - member: Eth1/7
            system_mac: "14:14:14:14:14:14"
            ethernet_segment:
              esi_type: auto_system_mac
              df_preference: 3333
        state: replaced

    # After state:
    # ------------
    #
    # interface Eth1/5
    #  mtu 9100
    #  speed 100000
    #  no shutdown
    # !
    # interface Eth1/6
    #  channel-group 20
    #  mtu 9100
    #  speed 100000
    #  no shutdown
    # !
    # interface Eth1/7
    #  channel-group 10
    #  mtu 9100
    #  speed 100000
    #  no shutdown
    # !
    # interface PortChannel10
    #  no shutdown
    #  system-mac 14:14:14:14:14:14
    #  !
    #  evpn ethernet-segment auto-system-mac
    #   df-preference 3333
    # !
    # interface PortChanne20
    #  no shutdown
    #  system-mac 14:14:14:14:14:14
    #  !
    #  evpn ethernet-segment auto-system-mac
    #   df-preference 6666
    #

    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # interface Eth1/5
    #  channel-group 10
    #  mtu 9100
    #  speed 100000
    #  no shutdown
    # !
    # interface Eth1/6
    #  no channel-group
    #  mtu 9100
    #  speed 100000
    #  no shutdown
    # !
    # interface PortChannel10
    #  fast_rate
    #  fallback
    #  no shutdown
    #  !
    #  evpn ethernet-segment auto-system-mac
    #   df-preference 2222
    #

    - name: Override all LAG interface configurations
      dellemc.enterprise_sonic.sonic_lag_interfaces:
        config:
          - name: PortChannel20
            min_links: 2
            members:
              interfaces:
                - member: Eth1/6
                - member: Eth1/7
                - member: Eth1/8
            system_mac: "12:12:12:12:12:12"
            ethernet_segment:
              esi_type: auto_lacp
              df_preference: 3333
            lacp_individual:
              enable: true
              timeout: 60
        state: overridden

    # After state:
    # ------------
    #
    # interface Eth1/5
    #  mtu 9100
    #  speed 100000
    #  no shutdown
    # !
    # interface Eth1/6
    #  channel-group 20
    #  mtu 9100
    #  speed 100000
    #  no shutdown
    # !
    # interface Eth1/7
    #  channel-group 20
    #  mtu 9100
    #  speed 100000
    #  no shutdown
    # !
    # interface Eth1/8
    #  channel-group 20
    #  mtu 9100
    #  speed 100000
    #  no shutdown
    # !
    # interface PortChannel20
    #  min-links 2
    #  lacp individual
    #  lacp individual timeout 60
    #  no shutdown
    #  system-mac 12:12:12:12:12:12
    #  !
    #  evpn ethernet-segment auto-lacp
    #   df-preference 3333
    #

    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # interface Eth1/10
    #  channel-group 10
    #  mtu 9100
    #  speed 100000
    #  no shutdown
    # !
    # interface Eth1/15
    #  channel-group 12
    #  mtu 9100
    #  speed 100000
    #  no shutdown
    # !
    # interface Eth1/16
    #  channel-group 12
    #  mtu 9100
    #  speed 100000
    #  no shutdown
    # !
    # interface PortChannel 10
    #  no shutdown
    #  system-mac 12:12:12:12:12:12
    #  !
    #  evpn ethernet-segment auto-lacp
    #   df-preference 2222
    # !
    # interface PortChannel 12
    #  fast_rate
    #  fallback
    #  graceful-shutdown
    #  min-links 2
    #  no shutdown
    #

    - name: Delete all LAG interfaces
      dellemc.enterprise_sonic.sonic_lag_interfaces:
        config:
        state: deleted

    # After state:
    # -------------
    #
    # interface Eth1/10
    #  mtu 9100
    #  speed 100000
    #  no shutdown
    # !
    # interface Eth1/15
    #  mtu 9100
    #  speed 100000
    #  no shutdown
    # !
    # interface Eth1/16
    #  mtu 9100
    #  speed 100000
    #  no shutdown
    #

    # Using "deleted" state
    #
    # Before state:
    # -------------
    # interface Eth1/10
    #  channel-group 10
    #  mtu 9100
    #  speed 100000
    #  no shutdown
    # !
    # interface Eth1/11
    #  channel-group 10
    #  mtu 9100
    #  speed 100000
    #  no shutdown
    # !
    # interface Eth1/20
    #  channel-group 20
    #  mtu 9100
    #  speed 100000
    #  no shutdown
    # !
    # interface PortChannel10
    #  min-links 2
    #  no shutdown
    #  system-mac 12:12:12:12:12:12
    #  !
    #  evpn ethernet-segment auto-lacp
    #   df-preference 2222
    # !
    # interface PortChannel20
    #  no shutdown
    #

    - name: Delete specified LAG configurations and LAG interfaces
      dellemc.enterprise_sonic.sonic_lag_interfaces:
        config:
          - name: PortChannel10
            min_links: 2
            members:
              interfaces:
                - member: Eth1/10
            system_mac: "12:12:12:12:12:12"
            ethernet_segment:
              esi_type: auto_lacp
          - name: PortChannel20
        state: deleted

    # After state:
    # -------------
    #
    # interface Eth1/10
    #  mtu 9100
    #  speed 100000
    #  no shutdown
    # !
    # interface Eth1/11
    #  channel-group 10
    #  mtu 9100
    #  speed 100000
    #  no shutdown
    # !
    # interface Eth1/20
    #  mtu 9100
    #  speed 100000
    #  no shutdown
    # !
    # interface PortChannel10
    #  no shutdown
    #



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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned is always in the same format as the parameters above.</div>
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
                            <div>The configuration expected as a result of module invocation.</div>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration that is returned is always in the same format as the parameters above.</div>
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

- Abirami N (@abirami-n)
