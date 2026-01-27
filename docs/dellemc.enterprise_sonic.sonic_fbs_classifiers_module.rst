.. _dellemc.enterprise_sonic.sonic_fbs_classifiers_module:


**********************************************
dellemc.enterprise_sonic.sonic_fbs_classifiers
**********************************************

**Manage flow based services (FBS) classifiers configuration on SONiC**


Version added: 3.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of FBS classifiers for devices running SONiC




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
                        <div>FBS classifiers configuration</div>
                        <div><em>match_acl</em> and <em>match_hdr_fields</em> are mutually exclusive.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>class_description</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Description of classifier</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>class_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of classifier</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>match_acl</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Match ACL configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>acl_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of ACL to be used as match criteria</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>acl_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ip</li>
                                    <li>ipv6</li>
                                    <li>mac</li>
                        </ul>
                </td>
                <td>
                        <div>Type of ACL to be used as match criteria</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>match_hdr_fields</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Match header fields configuration</div>
                        <div><em>ipv4</em> and <em>ipv6</em> are mutually exclusive.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ip</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IP field configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dscp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Value of diffserv code point, range 0-63</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>protocol</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>auth</li>
                                    <li>gre</li>
                                    <li>icmp</li>
                                    <li>icmpv6</li>
                                    <li>igmp</li>
                                    <li>l2tp</li>
                                    <li>pim</li>
                                    <li>rsvp</li>
                                    <li>tcp</li>
                                    <li>udp</li>
                        </ul>
                </td>
                <td>
                        <div>IP protocol</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>IPv4 field configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>destination_address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Destination IPv4 address prefix</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>source_address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Source IPv4 address prefix</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>IPv6 field configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>destination_address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Destination IPv6 address prefix</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>source_address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Source IPv6 address prefix</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>l2</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Ethernet field configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dei</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Drop eligible indicator, range 0-1</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>destination_mac</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Destination MAC address</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>destination_mac_mask</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Destination MAC address mask</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ethertype</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>arp</li>
                                    <li>ipv4</li>
                                    <li>ipv6</li>
                                    <li>lldp</li>
                                    <li>mpls</li>
                                    <li>roce</li>
                                    <li>vlan</li>
                        </ul>
                </td>
                <td>
                        <div>Ethertype field to match in ethernet packets</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>pcp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Priority code point, range 0-7</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>source_mac</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Source MAC address</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>source_mac_mask</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Source MAC address mask</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vlanid</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>VLAN ID, range 1-4094</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>transport</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Transport field configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>destination_port</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Destination port or range</div>
                        <div>For specifying a range use &#x27;..&#x27; as a delimeter, e.g. &#x27;1..3&#x27;.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>icmp_code</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>ICMP or ICMPv6 code, range 0-255</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>icmp_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>ICMP or ICMPv6 type, range 0-255</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>source_port</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Source port or range</div>
                        <div>For specifying a range use &#x27;..&#x27; as a delimeter, e.g. &#x27;1..3&#x27;.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>tcp_flags</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ack</li>
                                    <li>fin</li>
                                    <li>psh</li>
                                    <li>rst</li>
                                    <li>syn</li>
                                    <li>urg</li>
                        </ul>
                </td>
                <td>
                        <div>List of TCP flags to match</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>match_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>acl</li>
                                    <li>fields</li>
                        </ul>
                </td>
                <td>
                        <div>Classifier match type</div>
                        <div>The classifier match type is required for classifier creation and corresponds to either &#x27;match_acl&#x27; or &#x27;match_hdr_fields&#x27; configuration.</div>
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
                        <div>The state of the configuration after module completion</div>
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
    # sonic# show class-map
    # (No 'class-map' configuration present)

    - name: Merge FBS classifiers configuration
      dellemc.enterprise_sonic.sonic_fbs_classifiers:
        config:
          - class_name: class1
            class_description: xyz
            match_type: fields
            match_hdr_fields:
              ip:
                dscp: 0
                protocol: tcp
              ipv4:
                source_address: 1.1.1.1/1
                destination_address: 2.2.2.2/2
              l2:
                source_mac: 1a:2b:3c:4d:5e:6f
                source_mac_mask: 6a:5b:4c:3d:2e:1f
                destination_mac: 2a:4b:6c:8d:10:20
                destination_mac_mask: 20:10:8d:6c:4b:2a
                dei: 0
                ethertype: ipv4
                pcp: 0
                vlanid: 1
              transport:
                source_port: 1..3
                destination_port: 4..6
                tcp_flags:
                  - ack
                  - fin
                  - psh
        state: merged

    # After state:
    # ------------
    #
    # sonic# show class-map
    # Class-map class1 match-type fields
    #   Description: xyz
    #   Match:
    #     ethertype ip
    #     src-mac 1a:2b:3c:4d:5e:6f/6a:5b:4c:3d:2e:1f
    #     dst-mac 2a:4b:6c:8d:10:20/20:10:8d:6c:4b:2a
    #     vlan 1
    #     pcp be
    #     dei 0
    #     ip protocol tcp
    #     src-ip 1.1.1.1/1
    #     dst-ip 2.2.2.2/2
    #     dscp default
    #     src-port 1-3
    #     dst-port 4-6
    #     tcp-flags fin psh ack
    #   Referenced in flows:


    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show class-map
    # Class-map class1 match-type fields
    #   Description: xyz
    #   Match:
    #     ethertype ip
    #     src-mac 1a:2b:3c:4d:5e:6f/6a:5b:4c:3d:2e:1f
    #     dst-mac 2a:4b:6c:8d:10:20/20:10:8d:6c:4b:2a
    #     vlan 1
    #     pcp be
    #     dei 0
    #     ip protocol tcp
    #     src-ip 1.1.1.1/1
    #     dst-ip 2.2.2.2/2
    #     dscp default
    #     src-port 1-3
    #     dst-port 4-6
    #     tcp-flags fin psh ack
    #   Referenced in flows:
    #
    # Class-map class2 match-type acl
    #   Description: abc
    #   Match:
    #     ip access-group acl1
    #   Referenced in flows:

    - name: Replace FBS classifiers configuration
      dellemc.enterprise_sonic.sonic_fbs_classifiers:
        config:
          - class_name: class1
            match_hdr_fields:
              l2:
                source_mac: 9a:8b:7c:6d:5e:4f
                source_mac_mask: 2a:4b:1c:9b:1e:0f
                destination_mac: 1a:6c:3c:4f:40:22
                destination_mac_mask: 26:44:8c:9d:4b:6f
                ethertype: vlan
                pcp: 6
                vlanid: 2
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show class-map
    # Class-map class1 match-type fields
    #   Description: xyz
    #   Match:
    #     ethertype 0x8100
    #     src-mac 9a:8b:7c:6d:5e:4f/2a:4b:1c:9b:1e:0f
    #     dst-mac 1a:6c:3c:4f:40:22/26:44:8c:9d:4b:6f
    #     vlan 2
    #     pcp ic
    #   Referenced in flows:
    #
    # Class-map class2 match-type acl
    #   Description: abc
    #   Match:
    #     ip access-group acl1
    #   Referenced in flows:


    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show class-map
    # Class-map class1 match-type fields
    #   Description: xyz
    #   Match:
    #     ethertype 0x8100
    #     src-mac 9a:8b:7c:6d:5e:4f/2a:4b:1c:9b:1e:0f
    #     dst-mac 1a:6c:3c:4f:40:22/26:44:8c:9d:4b:6f
    #     vlan 2
    #     pcp ic
    #   Referenced in flows:

    - name: Override FBS classifiers configuration
      dellemc.enterprise_sonic.sonic_fbs_classifiers:
        config:
          - class_name: class2
            class_description: abc
            match_type: acl
            match_acl:
              acl_name: acl1
              acl_type: ip

    # After state:
    # ------------
    #
    # sonic# show class-map
    # Class-map class2 match-type acl
    #   Description: abc
    #   Match:
    #     ip access-group acl1
    #   Referenced in flows:


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show class-map
    # Class-map class1 match-type fields
    #   Description: xyz
    #   Match:
    #     ethertype 0x8100
    #     src-mac 9a:8b:7c:6d:5e:4f/2a:4b:1c:9b:1e:0f
    #     dst-mac 1a:6c:3c:4f:40:22/26:44:8c:9d:4b:6f
    #     vlan 2
    #     pcp ic
    #   Referenced in flows:
    #
    # Class-map class2 match-type acl
    #   Description: abc
    #   Match:
    #     ip access-group acl1
    #   Referenced in flows:

    - name: Delete FBS classifiers configuration
      dellemc.enterprise_sonic.sonic_fbs_classifiers:
        config:
          - class_name: class1
            class_description: xyz
            match_hdr_fields:
              l2:
                source_mac: 9a:8b:7c:6d:5e:4f
                source_mac_mask: 2a:4b:1c:9b:1e:0f
                destination_mac: 1a:6c:3c:4f:40:22
                destination_mac_mask: 26:44:8c:9d:4b:6f
                ethertype: vlan
                pcp: 6
                vlanid: 2
          - class_name: class2
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show class-map
    # Class-map class1 match-type fields
    #   Description:
    #   Match:
    #   Referenced in flows:


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show class-map
    # Class-map class1 match-type fields
    #   Description: xyz
    #   Match:
    #     ethertype 0x8100
    #     src-mac 9a:8b:7c:6d:5e:4f/2a:4b:1c:9b:1e:0f
    #     dst-mac 1a:6c:3c:4f:40:22/26:44:8c:9d:4b:6f
    #     vlan 2
    #     pcp ic
    #   Referenced in flows:
    #
    # Class-map class2 match-type acl
    #   Description: abc
    #   Match:
    #     ip access-group acl1
    #   Referenced in flows:

    - name: Delete all FBS classifiers configuration
      dellemc.enterprise_sonic.sonic_fbs_classifiers:
        config:
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show class-map
    # (No 'class-map' configuration present)



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

- S\. Talabi (@stalabi1)
