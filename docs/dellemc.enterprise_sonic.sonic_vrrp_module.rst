.. _dellemc.enterprise_sonic.sonic_vrrp_module:


***********************************
dellemc.enterprise_sonic.sonic_vrrp
***********************************

**Configure VRRP protocol settings on SONiC.**


Version added: 2.5.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of VRRP protocol settings on devices running SONiC
- Configure interface IP address before configuring VRRP
- Configure interface VRF forwarding before configuring VRRP in a VRF




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
                        <div>Specifies the VRRP related configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>group</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Defining the VRRP/VRRP6 group</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>advertisement_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure advertisement interval (1 to 254)</div>
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
                        <div>VRRP configurations to be set for the interface mentioned in types(VRRP/VRRP6).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>preempt</b>
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
                        <div>Enable preempt</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>preempt_delay</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 4.0.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure preempt delay interval (0 to 1000)</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>priority</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Priority for MASTER election (1 to 254)</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>track_interface</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure track interface for priority change.</div>
                        <div><em>interface</em> and <em>priority_increment</em> are required together.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
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
                        <div>Full name of the Layer 3 interface, i.e. Eth1/1.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>priority_increment</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Weight for changing priority (1 to 254)</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>use_v2_checksum</b>
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
                        <div>Enable checksum compatibility with VRRPv2 (Not supported for IPv6).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>version</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>2</li>
                                    <li>3</li>
                        </ul>
                </td>
                <td>
                        <div>Configure VRRP Version 2 or 3 (Not supported for IPv6).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>virtual_address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure virtual IP Address.</div>
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
                        <div>List of IP addresses to be set.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>virtual_router_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>VRRP ID (1 to 255)</div>
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
                        <div>Specifies the operation to be performed on the VRRP process configured on the device.</div>
                        <div>In case of merged, the input configuration will be merged with the existing VRRP configuration on the device.</div>
                        <div>In case of deleted, the existing VRRP configuration will be removed from the device.</div>
                        <div>In case of overridden, all existing VRRP configuration will be deleted and the specified input configuration will be installed.</div>
                        <div>In case of replaced, the existing VRRP configuration on the device will be replaced by the configuration in the playbook for each VRRP interface/group configured by the playbook.</div>
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
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 81.1.1.1/24
    #  ipv6 address 81::1/24
    #  !
    #  vrrp 1 address-family ipv4
    #  preempt
    #  vip 81.1.1.3
    #  vip 81.1.1.4
    #  !
    #  vrrp 10 address-family ipv6
    #  priority 10
    #  preempt-delay 4
    #  advertisement-interval 4
    #  vip 81::3
    #  vip 81::4
    # !
    # interface Eth1/3
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 61.1.1.1/24
    #  !
    #  vrrp 5 address-family ipv4
    #  priority 20
    #  vip 61.1.1.3
    #  !
    #  vrrp 15 address-family ipv4
    #  priority 20
    #  preempt
    #  vip 61.1.1.4
    # !
    - name: Delete VRRP and VRRP6 relay configurations
      sonic_vrrp:
        config:
          - name: 'Eth1/1'
            group:
              - virtual_router_id: 1
                afi: ipv4
                virtual_address:
                  - address: 81.1.1.4
                preempt: true
              - virtual_router_id: 10
                afi: ipv6
                advertisement_interval: 4
                priority: 10
                preempt_delay: 4
          - name: 'Eth1/3'
            group:
              - virtual_router_id: 5
                afi: ipv4
                virtual_address:
                  - address: 61.1.1.3
                priority: 20
              - virtual_router_id: 15
                afi: ipv4
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
    #  !
    #  vrrp 1 address-family ipv4
    #  vip 81.1.1.3
    #  !
    #  vrrp 10 address-family ipv6
    #  vip 81::3
    #  vip 81::4
    # !
    # interface Eth1/3
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
    # interface Eth1/3
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 61.1.1.1/24
    # !
    - name: Add VRRP and VRRP6 configurations
      sonic_vrrp:
        config:
          - name: 'Eth1/1'
            group:
              - virtual_router_id: 1
                afi: ipv4
                virtual_address:
                  - address: 81.1.1.3
                  - address: 81.1.1.4
                preempt: true
              - virtual_router_id: 10
                afi: ipv6
                virtual_address:
                  - address: 81::3
                  - address: 81::4
                advertisement_interval: 4
                priority: 10
                preempt_delay: 4
          - name: 'Eth1/3'
            group:
              - virtual_router_id: 5
                afi: ipv4
                virtual_address:
                  - address: 61.1.1.3
                priority: 20
              - virtual_router_id: 15
                afi: ipv4
                virtual_address:
                  - address: 61.1.1.4
                preempt: true
                priority: 20
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
    #  ipv6 address 81::1/24
    #  !
    #  vrrp 1 address-family ipv4
    #  preempt
    #  vip 81.1.1.3
    #  vip 81.1.1.4
    #  !
    #  vrrp 10 address-family ipv6
    #  priority 10
    #  preempt-delay 4
    #  advertisement-interval 4
    #  vip 81::3
    #  vip 81::4
    # !
    # interface Eth1/3
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 61.1.1.1/24
    #  !
    #  vrrp 5 address-family ipv4
    #  priority 20
    #  vip 61.1.1.3
    #  !
    #  vrrp 15 address-family ipv4
    #  priority 20
    #  preempt
    #  vip 61.1.1.4
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
    #  ipv6 address 81::1/24
    #  !
    #  vrrp 1 address-family ipv4
    #  preempt
    #  vip 81.1.1.3
    #  vip 81.1.1.4
    #  !
    #  vrrp 10 address-family ipv6
    #  priority 10
    #  preempt-delay 4
    #  advertisement-interval 4
    #  vip 81::3
    #  vip 81::4
    # !
    # interface Eth1/3
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 61.1.1.1/24
    #  !
    #  vrrp 5 address-family ipv4
    #  priority 20
    #  vip 61.1.1.3
    #  !
    #  vrrp 15 address-family ipv4
    #  priority 20
    #  preempt
    #  vip 61.1.1.4
    # !
    - name: Replace VRRP and VRRP6 relay configurations
      sonic_vrrp:
        config:
          - name: 'Eth1/1'
            group:
              - virtual_router_id: 10
                afi: ipv6
                priority: 20
          - name: 'Eth1/3'
            group:
              - virtual_router_id: 5
                afi: ipv4
                virtual_address:
                  - address: 61.1.1.5
                preempt: false
                track_interface:
                  - interface: Eth1/1
                    priority_increment: 10
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
    #  ipv6 address 81::1/24
    #  !
    #  vrrp 1 address-family ipv4
    #  vip 81.1.1.3
    #  vip 81.1.1.4
    #  !
    #  vrrp 10 address-family ipv6
    #  priority 20
    # !
    # interface Eth1/3
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 61.1.1.1/24
    #  !
    #  vrrp 5 address-family ipv4
    #  no preempt
    #  vip 61.1.1.5
    #  track-interface Eth1/1 weight 10
    #  !
    #  vrrp 15 address-family ipv4
    #  priority 20
    #  preempt
    #  vip 61.1.1.4
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
    #  ipv6 address 81::1/24
    #  !
    #  vrrp 1 address-family ipv4
    #  preempt
    #  vip 81.1.1.3
    #  vip 81.1.1.4
    #  !
    #  vrrp 10 address-family ipv6
    #  priority 10
    #  advertisement-interval 4
    #  preempt-delay 4
    #  vip 81::3
    #  vip 81::4
    # !
    # interface Eth1/3
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 61.1.1.1/24
    #  !
    #  vrrp 5 address-family ipv4
    #  priority 20
    #  vip 61.1.1.3
    #  !
    #  vrrp 15 address-family ipv4
    #  priority 20
    #  preempt
    #  vip 61.1.1.4
    # !
    - name: Overwrite the VRRP and VRRP6 relay configurations
      sonic_vrrp:
        config:
          - name: 'Eth1/1'
            group:
              - virtual_router_id: 15
                afi: ipv4
                virtual_address:
                  - address: 81.1.1.15
                preempt: false
          - name: 'Eth1/3'
            group:
              - virtual_router_id: 5
                afi: ipv4
              - virtual_router_id: 15
                afi: ipv4
                virtual_address:
                  - address: 61.1.1.5
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
    #  ipv6 address 81::1/24
    #  !
    #  vrrp 15 address-family ipv4
    #  no preempt
    #  vip 81.1.1.15
    # !
    # interface Eth1/3
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  ip address 61.1.1.1/24
    #  !
    #  vrrp 5 address-family ipv4
    #  !
    #  vrrp 15 address-family ipv4
    #  vip 61.1.1.5
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
                            <div>The generated configuration model invocation.</div>
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

- Santhosh Kumar T(@santhosh-kt)
