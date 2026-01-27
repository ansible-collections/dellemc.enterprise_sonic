.. _dellemc.enterprise_sonic.sonic_l2_acls_module:


**************************************
dellemc.enterprise_sonic.sonic_l2_acls
**************************************

**Manage Layer 2 access control lists (ACL) configurations on SONiC**


Version added: 2.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of Layer 2 access control lists (ACL) in devices running SONiC.




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
                        <div>Specifies Layer 2 ACL configurations.</div>
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
                        <div>Specifies the ACL name.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>remark</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies remark for the ACL.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>rules</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of rules with the ACL.</div>
                        <div><em>sequence_num</em>, <em>action</em>, <em>source</em> &amp; <em>destination</em> are required for adding a new rule.</div>
                        <div>If <em>state=deleted</em>, options other than <em>sequence_num</em> are not considered.</div>
                        <div><em>ethertype</em> and <em>vlan_tag_format</em> are mutually exclusive.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>action</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>deny</li>
                                    <li>discard</li>
                                    <li>do-not-nat</li>
                                    <li>permit</li>
                                    <li>transit</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the action taken on the matched Ethernet frame.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dei</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>0</li>
                                    <li>1</li>
                        </ul>
                </td>
                <td>
                        <div>Match Ethernet frame with the given Drop Eligible Indicator (DEI) value.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>destination</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the destination of the Ethernet frame.</div>
                        <div><em>address</em> and <em>address_mask</em> are required together.</div>
                        <div><em>any</em>, <em>host</em> and <em>address</em> are mutually exclusive.</div>
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
                        <div>Destination MAC address.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address_mask</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Destination MAC address mask.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>any</b>
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
                        <div>Match any destination MAC address.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>host</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>MAC address of a single destination host.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ethertype</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the EtherType of the Ethernet frame.</div>
                        <div>Only one suboption can be specified for ethertype in a rule.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>arp</b>
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
                        <div>Match Ethernet frame with ARP EtherType (0x806).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ipv4</b>
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
                        <div>Match Ethernet frame with IPv4 EtherType (0x800).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ipv6</b>
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
                        <div>Match Ethernet frame with IPv6 EtherType (0x86DD).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the EtherType value to match as a hexadecimal string.</div>
                        <div>The range is from 0x600 to 0xffff.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>pcp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Match Ethernet frames using Priority Code Point (PCP) value.</div>
                        <div><em>mask</em> is valid only when <em>value</em> is specified.</div>
                        <div><em>value</em> and <em>traffic_type</em> are mutually exclusive.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mask</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Match Ethernet frame with given PCP value and mask.</div>
                        <div>The range is from 0 to 7.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>traffic_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>be</li>
                                    <li>bk</li>
                                    <li>ee</li>
                                    <li>ca</li>
                                    <li>vi</li>
                                    <li>vo</li>
                                    <li>ic</li>
                                    <li>nc</li>
                        </ul>
                </td>
                <td>
                        <div>Match Ethernet frame with PCP value for the given traffic type.</div>
                        <div><code>be</code> - Match Ethernet frame with Best effort PCP (0).</div>
                        <div><code>bk</code> - Match Ethernet frame with Background PCP (1).</div>
                        <div><code>ee</code> - Match Ethernet frame with Excellent effort PCP (2).</div>
                        <div><code>ca</code> - Match Ethernet frame with Critical applications PCP (3).</div>
                        <div><code>vi</code> - Match Ethernet frame with Video, &lt; 100 ms latency and jitter PCP (4).</div>
                        <div><code>vo</code> - Match Ethernet frame with Voice, &lt; 10 ms latency and jitter PCP (5).</div>
                        <div><code>ic</code> - Match Ethernet frame with Internetwork control PCP (6).</div>
                        <div><code>nc</code> - Match Ethernet frame with Network control PCP (7).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Match Ethernet frame with the given PCP value.</div>
                        <div>The range is from 0 to 7</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>remark</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies remark for the ACL rule.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>sequence_num</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the sequence number of the rule.</div>
                        <div>The range is from 1 to 65535.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>source</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the source of the Ethernet frame.</div>
                        <div><em>address</em> and <em>address_mask</em> are required together.</div>
                        <div><em>any</em>, <em>host</em> and <em>address</em> are mutually exclusive.</div>
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
                        <div>Source MAC address.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address_mask</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Source MAC address mask.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>any</b>
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
                        <div>Match any source MAC address.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>host</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>MAC address of a single source host.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Match Ethernet frame with the given VLAN ID.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vlan_tag_format</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Match Ethernet frame with the given VLAN tag format.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>multi_tagged</b>
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
                        <div>Match three of more VLAN tagged Ethernet frame.</div>
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
                        <div><code>merged</code> - Merges provided L2 ACL configuration with on-device configuration.</div>
                        <div><code>replaced</code> - Replaces on-device configuration of the specified L2 ACLs with provided configuration.</div>
                        <div><code>overridden</code> - Overrides all on-device L2 ACL configurations with the provided configuration.</div>
                        <div><code>deleted</code> - Deletes on-device L2 ACL configuration.</div>
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
    # sonic# show running-configuration mac access-list
    # !
    # mac access-list test
    #  seq 1 permit host 22:22:22:22:22:22 any vlan 20
    # sonic#

    - name: Merge provided Layer 2 ACL configurations
      dellemc.enterprise_sonic.sonic_l2_acls:
        config:
          - name: 'test'
            rules:
              - sequence_num: 2
                action: 'permit'
                source:
                  any: true
                destination:
                  any: true
                ethertype:
                  value: '0x88cc'
                remark: 'LLDP'
              - sequence_num: 3
                action: 'permit'
                source:
                  any: true
                destination:
                  address: '00:00:10:00:00:00'
                  address_mask: '00:00:ff:ff:00:00'
                pcp:
                  value: 4
                  mask: 6
              - sequence_num: 4
                action: 'deny'
                source:
                  any: true
                destination:
                  any: true
                vlan_tag_format:
                  multi_tagged: true
          - name: 'test1'
            remark: 'test_mac_acl'
            rules:
              - sequence_num: 1
                action: 'permit'
                source:
                  host: '11:11:11:11:11:11'
                destination:
                  any: true
              - sequence_num: 2
                action: 'permit'
                source:
                  any: true
                destination:
                  any: true
                ethertype:
                  arp: true
                vlan_id: 100
              - sequence_num: 3
                action: 'deny'
                source:
                  any: true
                destination:
                  any: true
                dei: 0
        state: merged

    # After state:
    # ------------
    #
    # sonic# show running-configuration mac access-list
    # !
    # mac access-list test
    #  seq 1 permit host 22:22:22:22:22:22 any vlan 20
    #  seq 2 permit any any 0x88cc remark LLDP
    #  seq 3 permit any 00:00:10:00:00:00 00:00:ff:ff:00:00 pcp vi pcp-mask 6
    #  seq 4 deny any any vlan-tag-format multi-tagged
    # !
    # mac access-list test1
    #  remark test_mac_acl
    #  seq 1 permit host 11:11:11:11:11:11 any
    #  seq 2 permit any any arp vlan 100
    #  seq 3 deny any any dei 0
    # sonic#


    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration mac access-list
    # !
    # mac access-list test
    #  seq 1 permit host 22:22:22:22:22:22 any vlan 20
    #  seq 2 permit any any 0x88cc remark LLDP
    #  seq 3 permit any 00:00:10:00:00:00 00:00:ff:ff:00:00 pcp vi pcp-mask 6
    # !
    # mac access-list test1
    #  remark test_mac_acl
    #  seq 1 permit host 11:11:11:11:11:11 any
    #  seq 2 permit any any arp vlan 100
    #  seq 3 deny any any dei 0
    # sonic#

    - name: Replace device configuration of specified Layer 2 ACLs with provided configuration
      dellemc.enterprise_sonic.sonic_l2_acls:
        config:
          - name: 'test1'
            rules:
              - sequence_num: 1
                action: 'permit'
                source:
                  any: true
                destination:
                  any: true
                ethertype:
                  arp: true
                vlan_id: 200
              - sequence_num: 2
                action: 'discard'
                source:
                  any: true
                destination:
                  any: true
          - name: 'test2'
            rules:
              - sequence_num: 1
                action: 'permit'
                source:
                  host: '33:33:33:33:33:33'
                destination:
                  host: '44:44:44:44:44:44'
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show running-configuration mac access-list
    # !
    # mac access-list test
    #  seq 1 permit host 22:22:22:22:22:22 any vlan 20
    #  seq 2 permit any any 0x88cc remark LLDP
    #  seq 3 permit any 00:00:10:00:00:00 00:00:ff:ff:00:00 pcp vi pcp-mask 6
    # !
    # mac access-list test1
    #  seq 1 permit any any arp vlan 200
    #  seq 2 discard any any
    # !
    # mac access-list test2
    #  seq 1 permit host 33:33:33:33:33:33 host 44:44:44:44:44:44
    # sonic#


    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration mac access-list
    # !
    # mac access-list test
    #  seq 1 permit host 22:22:22:22:22:22 any vlan 20
    #  seq 2 permit any any 0x88cc remark LLDP
    #  seq 3 permit any 00:00:10:00:00:00 00:00:ff:ff:00:00 pcp vi pcp-mask 6
    # !
    # mac access-list test1
    #  seq 1 permit any any arp vlan 200
    #  seq 2 discard any any
    # !
    # mac access-list test2
    #  seq 1 permit host 33:33:33:33:33:33 host 44:44:44:44:44:44
    # sonic#

    - name: Override device configuration of all Layer 2 ACLs with provided configuration
      dellemc.enterprise_sonic.sonic_l2_acls:
        config:
          - name: 'test1'
            remark: 'test_mac_acl'
            rules:
              - sequence_num: 1
                action: 'permit'
                source:
                  host: '11:11:11:11:11:11'
                destination:
                  any: true
                vlan_id: 100
              - sequence_num: 2
                action: 'permit'
                source:
                  any: true
                destination:
                  any: true
                pcp:
                  traffic_type: 'ca'
              - sequence_num: 3
                action: 'deny'
                source:
                  any: true
                destination:
                  any: true
                ethertype:
                  ipv4: true
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show running-configuration mac access-list
    # !
    # mac access-list test1
    #  remark test_mac_acl
    #  seq 1 permit host 11:11:11:11:11:11 any vlan 100
    #  seq 2 permit any any pcp ca
    #  seq 3 deny any any ip
    # sonic#


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration mac access-list
    # !
    # mac access-list test
    #  seq 1 permit host 22:22:22:22:22:22 any vlan 20
    #  seq 2 permit any any 0x88cc remark LLDP
    #  seq 3 permit any 00:00:10:00:00:00 00:00:ff:ff:00:00 pcp vi pcp-mask 6
    # !
    # mac access-list test1
    #  remark test_mac_acl
    #  seq 1 permit host 11:11:11:11:11:11 any vlan 100
    #  seq 2 deny any any ip
    # !
    # mac access-list test2
    #  seq 1 permit host 33:33:33:33:33:33 host 44:44:44:44:44:44
    # sonic#

    - name: Delete specified Layer 2 ACLs, ACL remark and ACL rule entries
      dellemc.enterprise_sonic.sonic_l2_acls:
        config:
          - name: 'test'
            rules:
              - sequence_num: 3
          - name: 'test1'
            remark: 'test_mac_acl'
          - name: 'test2'
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration mac access-list
    # !
    # mac access-list test
    #  seq 1 permit host 22:22:22:22:22:22 any vlan 20
    #  seq 2 permit any any 0x88cc remark LLDP
    # !
    # mac access-list test1
    #  seq 1 permit host 11:11:11:11:11:11 any vlan 100
    #  seq 2 deny any any ip
    # sonic#


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration mac access-list
    # !
    # mac access-list test
    #  seq 1 permit host 22:22:22:22:22:22 any vlan 20
    #  seq 2 permit any any 0x88cc remark LLDP
    #  seq 3 permit any 00:00:10:00:00:00 00:00:ff:ff:00:00 pcp vi pcp-mask 6
    # !
    # mac access-list test1
    #  remark test_mac_acl
    #  seq 1 permit host 11:11:11:11:11:11 any vlan 100
    #  seq 2 deny any any ip
    # !
    # mac access-list test2
    #  seq 1 permit host 33:33:33:33:33:33 host 44:44:44:44:44:44
    # sonic#

    - name: Delete all Layer 2 ACL configurations
      dellemc.enterprise_sonic.sonic_l2_acls:
        config:
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration mac access-list
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
