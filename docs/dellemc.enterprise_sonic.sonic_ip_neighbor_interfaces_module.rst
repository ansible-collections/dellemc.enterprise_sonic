.. _dellemc.enterprise_sonic.sonic_ip_neighbor_interfaces_module:


*****************************************************
dellemc.enterprise_sonic.sonic_ip_neighbor_interfaces
*****************************************************

**Manage interface-specific IP neighbor configurations on SONiC**


Version added: 3.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of interface-specific IP neighbor parameters for devices running SONiC.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="3">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="3">
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
                        <div>Specifies interface-specific IP neighbor configurations.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ipv4_neighbors</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the static IPv4 neighbors.</div>
                        <div><em>ip</em> &amp; <em>mac</em> are required for adding a new neighbor.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ip</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IPv4 address of the neighbor.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mac</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>MAC address of the neighbor.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ipv6_neighbors</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the static IPv6 neighbors.</div>
                        <div><em>ip</em> &amp; <em>mac</em> are required for adding a new neighbor.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ip</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IPv6 address of the neighbor.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mac</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>MAC address of the neighbor.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                <td colspan="3">
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
                        <div><code>merged</code> - Merges provided interface-specific IP neighbor configuration with on-device configuration.</div>
                        <div><code>replaced</code> - Replaces on-device IP neighbor configuration of the specified interfaces with provided configuration.</div>
                        <div><code>overridden</code> - Overrides all on-device interface-specific IP neighbor configurations with the provided configuration.</div>
                        <div><code>deleted</code> - Deletes on-device interface-specific IP neighbor configuration.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - Tested against Enterprise SONiC Distribution by Dell Technologies
   - Supports ``check_mode``



Examples
--------

.. code-block:: yaml

    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface Vlan 10 | grep "arp|neighbor"
    #  ip arp 10.1.1.4 00:01:02:03:44:55
    # sonic# show running-configuration interface Vlan 20 | grep "arp|neighbor"
    # sonic#

    - name: Merge provided interface IP neighbor configurations
      dellemc.enterprise_sonic.sonic_ip_neighbor_interfaces:
        config:
          - name: 'Vlan10'
            ipv6_neighbors:
              - ip: '10::2'
                mac: '00:01:02:03:04:22'
          - name: 'Vlan20'
            ipv4_neighbors:
              - ip: '20.1.1.4'
                mac: '00:01:02:03:22:44'
              - ip: '20.1.1.5'
                mac: '00:01:02:03:22:55'
        state: merged

    # After state:
    # ------------
    #
    # sonic# show running-configuration interface Vlan 10 | grep "arp|neighbor"
    #  ip arp 10.1.1.4 00:01:02:03:44:55
    #  ipv6 neighbor 10::2 00:01:02:03:04:22
    # sonic# show running-configuration interface Vlan 20 | grep "arp|neighbor"
    #  ip arp 20.1.1.4 00:01:02:03:22:44
    #  ip arp 20.1.1.5 00:01:02:03:22:55
    # sonic#


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface Vlan 10 | grep "arp|neighbor"
    #  ip arp 10.1.1.3 00:01:02:03:33:55
    #  ip arp 10.1.1.4 00:01:02:03:44:55
    #  ipv6 neighbor 10::2 00:01:02:03:04:22
    #  ipv6 neighbor 10::3 00:01:02:03:04:33
    # sonic# show running-configuration interface Vlan 20 | grep "arp|neighbor"
    #  ip arp 20.1.1.4 00:01:02:03:22:44
    #  ip arp 20.1.1.5 00:01:02:03:22:55
    #  ipv6 neighbor 20::2 00:01:02:03:22:22
    #  ipv6 neighbor 20::3 00:01:02:03:22:33
    # sonic#

    - name: Delete interface IP neighbor configurations
      dellemc.enterprise_sonic.sonic_ip_neighbor_interfaces:
        config:
          - name: 'Vlan10'
            ipv4_neighbors:
              - ip: '10.1.1.4'
            ipv6_neighbors:
              - ip: '10::2'
          - name: 'Vlan20'
            ipv4_neighbors:
              - ip: '20.1.1.4'
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration interface Vlan 10 | grep "arp|neighbor"
    #  ip arp 10.1.1.3 00:01:02:03:33:55
    #  ipv6 neighbor 10::3 00:01:02:03:04:33
    # sonic# show running-configuration interface Vlan 20 | grep "arp|neighbor"
    #  ip arp 20.1.1.5 00:01:02:03:22:55
    #  ipv6 neighbor 20::2 00:01:02:03:22:22
    #  ipv6 neighbor 20::3 00:01:02:03:22:33
    # sonic#


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface Vlan 10 | grep "arp|neighbor"
    #  ip arp 10.1.1.3 00:01:02:03:33:55
    #  ip arp 10.1.1.4 00:01:02:03:44:55
    #  ipv6 neighbor 10::2 00:01:02:03:04:22
    #  ipv6 neighbor 10::3 00:01:02:03:04:33
    # sonic# show running-configuration interface Vlan 20 | grep "arp|neighbor"
    #  ip arp 20.1.1.4 00:01:02:03:22:44
    #  ip arp 20.1.1.5 00:01:02:03:22:55
    #  ipv6 neighbor 20::2 00:01:02:03:22:22
    #  ipv6 neighbor 20::3 00:01:02:03:22:33
    # sonic#

    - name: Delete all interface IP neighbor configurations for interface Vlan 10
      dellemc.enterprise_sonic.sonic_ip_neighbor_interfaces:
        config:
          - name: 'Vlan10'
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration interface Vlan 10 | grep "arp|neighbor"
    # sonic# show running-configuration interface Vlan 20 | grep "arp|neighbor"
    #  ip arp 20.1.1.4 00:01:02:03:22:44
    #  ip arp 20.1.1.5 00:01:02:03:22:55
    #  ipv6 neighbor 20::2 00:01:02:03:22:22
    #  ipv6 neighbor 20::3 00:01:02:03:22:33
    # sonic#


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface Vlan 10 | grep "arp|neighbor"
    #  ip arp 10.1.1.3 00:01:02:03:33:55
    #  ip arp 10.1.1.4 00:01:02:03:44:55
    #  ipv6 neighbor 10::2 00:01:02:03:04:22
    #  ipv6 neighbor 10::3 00:01:02:03:04:33
    # sonic# show running-configuration interface Vlan 20 | grep "arp|neighbor"
    #  ip arp 20.1.1.4 00:01:02:03:22:44
    #  ip arp 20.1.1.5 00:01:02:03:22:55
    #  ipv6 neighbor 20::2 00:01:02:03:22:22
    # sonic#

    - name: Delete all interface IP neighbor configurations
      dellemc.enterprise_sonic.sonic_ip_neighbor_interfaces:
        config:
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration interface Vlan 10 | grep "arp|neighbor"
    # sonic# show running-configuration interface Vlan 20 | grep "arp|neighbor"
    # sonic#


    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface Vlan 10 | grep "arp|neighbor"
    #  ip arp 10.1.1.3 00:01:02:03:33:55
    #  ip arp 10.1.1.4 00:01:02:03:44:55
    #  ipv6 neighbor 10::2 00:01:02:03:04:22
    #  ipv6 neighbor 10::3 00:01:02:03:04:33
    # sonic# show running-configuration interface Vlan 20 | grep "arp|neighbor"
    #  ip arp 20.1.1.4 00:01:02:03:22:44
    #  ip arp 20.1.1.5 00:01:02:03:22:55
    #  ipv6 neighbor 20::2 00:01:02:03:22:22
    #  ipv6 neighbor 20::3 00:01:02:03:22:33
    # sonic#

    - name: Replace interface IP neighbor configurations for interface Vlan 10
      dellemc.enterprise_sonic.sonic_ip_neighbor_interfaces:
        config:
          - name: 'Vlan10'
            ipv4_neighbors:
              - ip: '10.1.1.11'
                mac: '00:01:02:03:04:11'
              - ip: '10.1.1.12'
                mac: '00:01:02:03:04:12'
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show running-configuration interface Vlan 10 | grep "arp|neighbor"
    #  ip arp 10.1.1.11 00:01:02:03:04:11
    #  ip arp 10.1.1.12 00:01:02:03:04:12
    # sonic# show running-configuration interface Vlan 20 | grep "arp|neighbor"
    #  ip arp 20.1.1.4 00:01:02:03:22:44
    #  ip arp 20.1.1.5 00:01:02:03:22:55
    #  ipv6 neighbor 20::2 00:01:02:03:22:22
    #  ipv6 neighbor 20::3 00:01:02:03:22:33
    # sonic#


    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface Vlan 10 | grep "arp|neighbor"
    #  ip arp 10.1.1.3 00:01:02:03:33:55
    #  ip arp 10.1.1.4 00:01:02:03:44:55
    #  ipv6 neighbor 10::2 00:01:02:03:04:22
    #  ipv6 neighbor 10::3 00:01:02:03:04:33
    # sonic# show running-configuration interface Vlan 20 | grep "arp|neighbor"
    #  ip arp 20.1.1.4 00:01:02:03:22:44
    #  ip arp 20.1.1.5 00:01:02:03:22:55
    #  ipv6 neighbor 20::2 00:01:02:03:22:22
    #  ipv6 neighbor 20::3 00:01:02:03:22:33
    # sonic# show running-configuration interface Vlan 30 | grep "arp|neighbor"
    # sonic#

    - name: Override all interface IP neighbor configurations
      dellemc.enterprise_sonic.sonic_ip_neighbor_interfaces:
        config:
          - name: 'Vlan10'
            ipv4_neighbors:
              - ip: '10.1.1.11'
                mac: '00:01:02:03:04:11'
            ipv6_neighbors:
              - ip: '10::11'
                mac: '00:01:02:03:10:11'
          - name: 'Vlan30'
            ipv4_neighbors:
              - ip: '30.1.1.6'
                mac: '00:01:02:03:30:66'
              - ip: '30.1.1.7'
                mac: '00:01:02:03:30:77'
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show running-configuration interface Vlan 10 | grep "arp|neighbor"
    #  ip arp 10.1.1.11 00:01:02:03:04:11
    #  ipv6 neighbor 10::11 00:01:02:03:10:11
    # sonic# show running-configuration interface Vlan 20 | grep "arp|neighbor"
    # sonic# show running-configuration interface Vlan 30 | grep "arp|neighbor"
    #  ip arp 30.1.1.6 00:01:02:03:30:66
    #  ip arp 30.1.1.7 00:01:02:03:30:77
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
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Arun Saravanan Balachandran (@ArunSaravananBalachandran)
