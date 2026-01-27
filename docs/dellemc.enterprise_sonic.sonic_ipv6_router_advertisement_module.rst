.. _dellemc.enterprise_sonic.sonic_ipv6_router_advertisement_module:


********************************************************
dellemc.enterprise_sonic.sonic_ipv6_router_advertisement
********************************************************

**Manage interface-specific IPv6 Router Advertisement configurations on SONiC**


Version added: 3.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of interface-specific IPv6 Router Advertisement parameters for devices running SONiC.
- This functionality is referred to as 'ipv6 nd' in Enterprise SONiC CLI.




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
                        <div>Specifies interface-specific IPv6 Router Advertisement configurations.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>adv_interval_option</b>
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
                        <div>Include Advertisement Interval option in Router Advertisement.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dnssl</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the DNS search list to advertise.</div>
                        <div>If <em>state=deleted</em>, options other than <em>dnssl_name</em> are not considered.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dnssl_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Domain Name suffix to be advertised.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>valid_lifetime</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the valid lifetime in seconds.</div>
                        <div>The range if from 0 to 4294967295.</div>
                        <div>Value of 4294967295 represents infinite valid lifetime.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>home_agent_config</b>
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
                        <div>Set &#x27;Home Agent&#x27; flag in Router Advertisement.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>home_agent_lifetime</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the Home Agent lifetime in seconds when <em>home_agent_config=True</em>.</div>
                        <div>The range is from 0 to 65520.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>home_agent_preference</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the Home Agent preference when <em>home_agent_config=True</em>.</div>
                        <div>The range is from 0 to 65535.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>managed_config</b>
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
                        <div>Set &#x27;Managed Address Configuration&#x27; flag in Router Advertisement.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>min_ra_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the minimum Router Advertisement interval in seconds.</div>
                        <div>The range is from 1 to 1350.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>min_ra_interval_msec</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the minimum Router Advertisement interval in milliseconds.</div>
                        <div>The range is from 30 to 1350000.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mtu</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the MTU (in bytes) to be advertised.</div>
                        <div>The range is from 0 to 65535.</div>
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
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>other_config</b>
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
                        <div>Set &#x27;Other Configuration&#x27; flag in Router Advertisement.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ra_fast_retrans</b>
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
                        <div>Enable faster transmissions of RA packets.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ra_hop_limit</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the Hop limit to be advertised.</div>
                        <div>The range is from 0 to 255.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ra_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the maximum Router Advertisement interval in seconds.</div>
                        <div>The range is from 1 to 1800.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ra_interval_msec</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the maximum Router Advertisement interval in milliseconds.</div>
                        <div>The range is from 70 to 1800000.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ra_lifetime</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the Router Lifetime in seconds.</div>
                        <div>The range is from 0 to 9000.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ra_prefixes</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the IPv6 prefixes to be included in Router Advertisement.</div>
                        <div>If <em>state=deleted</em>, options other than <em>prefix</em> are not considered.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>no_autoconfig</b>
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
                        <div>Indicate the prefix cannot be used for IPv6 autoconfiguration.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>off_link</b>
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
                        <div>Indicate the prefix cannot be used for on-link determination.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>preferred_lifetime</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the preferred lifetime in seconds.</div>
                        <div>The range if from 0 to 4294967295.</div>
                        <div>Value of 4294967295 represents infinite preferred lifetime.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>prefix</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IPv6 prefix to be advertised.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>router_address</b>
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
                        <div>Set &#x27;Router Address&#x27; flag.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>valid_lifetime</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the valid lifetime in seconds.</div>
                        <div>The range if from 0 to 4294967295.</div>
                        <div>Value of 4294967295 represents infinite valid lifetime.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ra_retrans_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the Retransmission Interval in milliseconds.</div>
                        <div>The range is from 0 to 4294967295.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>rdnss</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the Recursive DNS server addresses to advertise.</div>
                        <div>If <em>state=deleted</em>, options other than <em>address</em> are not considered.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Recursive DNS server address to be advertised.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>valid_lifetime</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the valid lifetime in seconds.</div>
                        <div>The range if from 0 to 4294967295.</div>
                        <div>Value of 4294967295 represents infinite valid lifetime.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>reachable_time</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the Reachable Time in milliseconds.</div>
                        <div>The range is from 0 to 3600000.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>router_preference</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>low</li>
                                    <li>medium</li>
                                    <li>high</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the default router preference.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>suppress</b>
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
                        <div>Enable suppression of Router Advertisement.</div>
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
                        <div><code>merged</code> - Merges provided interface-specific IPv6 router advertisement configuration with on-device configuration.</div>
                        <div><code>replaced</code> - Replaces on-device IPv6 router advertisement configuration of the specified interfaces with provided configuration.</div>
                        <div><code>overridden</code> - Overrides all on-device interface-specific IPv6 router advertisement configurations with the provided configuration.</div>
                        <div><code>deleted</code> - Deletes on-device interface-specific IPv6 router advertisement configuration.</div>
                </td>
            </tr>
    </table>
    <br/>




Examples
--------

.. code-block:: yaml

    # Using merged
    #
    # Before State:
    # -------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    # !
    # interface Eth1/2
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  no ipv6 nd suppress-ra
    #  ipv6 nd prefix 1000:0:0:1000::/64 86400 86400 off-link no-autoconfig
    # !

    - name: Add IPv6 Router Advertisement configurations
      dellemc.enterprise_sonic.sonic_ipv6_router_advertisement:
        config:
          - name: 'Eth1/1'
            suppress: false
            router_preference: high
            ra_interval: 180
            min_ra_interval: 60
            ra_lifetime: 360
            ra_retrans_interval: 30000
            ra_hop_limit: 10
            dnssl:
              - dnssl_name: 'test.com'
                valid_lifetime: 3600
            rdnss:
              - address: 100::100
              - address: 100::200
          - name: 'Eth1/2'
            adv_interval_option: true
            ra_fast_retrans: false
            reachable_time: 7200000
            ra_prefixes:
              - prefix: 1000:0:0:2000::/64
                valid_lifetime: 86400
                preferred_lifetime: 86400
                off_link: true
                no_autoconfig: true
        state: merged

    # After State:
    # ------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  no ipv6 nd suppress-ra
    #  ipv6 nd ra-hop-limit 10
    #  ipv6 nd ra-interval 180
    #  ipv6 nd min-ra-interval 60
    #  ipv6 nd ra-lifetime 360
    #  ipv6 nd ra-retrans-interval 30000
    #  ipv6 nd router-preference high
    #  ipv6 nd dnssl test.com 3600
    #  ipv6 nd rdnss 100::100
    #  ipv6 nd rdnss 100::200
    # !
    # interface Eth1/2
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  no ipv6 nd suppress-ra
    #  no ipv6 nd ra-fast-retrans
    #  ipv6 nd adv-interval-option
    #  ipv6 nd reachable-time 1200000
    #  ipv6 nd prefix 1000:0:0:1000::/64 86400 86400 off-link no-autoconfig
    #  ipv6 nd prefix 1000:0:0:2000::/64 86400 86400 off-link no-autoconfig
    # !


    # Using deleted
    #
    # Before State:
    # -------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  no ipv6 nd suppress-ra
    #  ipv6 nd ra-hop-limit 10
    #  ipv6 nd ra-interval 180
    #  ipv6 nd min-ra-interval 60
    #  ipv6 nd ra-lifetime 360
    #  ipv6 nd ra-retrans-interval 30000
    #  ipv6 nd router-preference high
    #  ipv6 nd dnssl test.com 3600
    #  ipv6 nd dnssl test2.com 7200
    #  ipv6 nd rdnss 100::100 3600
    #  ipv6 nd rdnss 100::200 7200
    # !
    # interface Eth1/2
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  no ipv6 nd suppress-ra
    #  no ipv6 nd ra-fast-retrans
    #  ipv6 nd adv-interval-option
    #  ipv6 nd min-ra-interval msec 45500
    #  ipv6 nd reachable-time 1200000
    #  ipv6 nd prefix 1000:0:0:1000::/64 86400 86400 off-link no-autoconfig
    #  ipv6 nd prefix 1000:0:0:2000::/64 86400 86400 off-link no-autoconfig
    # !

    - name: Delete IPv6 Router Advertisement configurations
      dellemc.enterprise_sonic.sonic_ipv6_router_advertisement:
        config:
          - name: 'Eth1/1'
            ra_hop_limit: 10
            router_preference: high
            dnssl:
              - dnssl_name: test2.com
            rdnss:
              - address: 100::200
          - name: 'Eth1/2'
            adv_interval_option: true
            ra_fast_retrans: false
            ra_prefixes:
              - prefix: 1000:0:0:2000::/64
        state: deleted

    # After State:
    # ------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  shutdown
    #  no ipv6 nd suppress-ra
    #  ipv6 nd ra-interval 180
    #  ipv6 nd min-ra-interval 60
    #  ipv6 nd ra-lifetime 360
    #  ipv6 nd ra-retrans-interval 30000
    #  ipv6 nd dnssl test.com 3600
    #  ipv6 nd rdnss 100::100 3600
    # !
    # interface Eth1/2
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  shutdown
    #  no ipv6 nd suppress-ra
    #  ipv6 nd min ra-interval msec 45500
    #  ipv6 nd reachable-time 1200000
    #  ipv6 nd prefix 1000:0:0:1000::/64 86400 86400 off-link no-autoconfig
    # !


    # Using deleted
    #
    # Before State:
    # -------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  no ipv6 nd suppress-ra
    #  ipv6 nd ra-hop-limit 10
    #  ipv6 nd ra-interval 180
    #  ipv6 nd min-ra-interval 60
    #  ipv6 nd ra-lifetime 360
    #  ipv6 nd ra-retrans-interval 30000
    #  ipv6 nd dnssl test.com 3600
    #  ipv6 nd rdnss 100::100 3600
    #  ipv6 nd rdnss 100::200 7200
    # !
    # interface Eth1/2
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  no ipv6 nd suppress-ra
    #  ipv6 nd adv-interval-option
    #  ipv6 nd router-preference low
    #  ipv6 nd prefix 1000:0:0:1000::/64 86400 86400 off-link no-autoconfig
    # !

    - name: Delete all IPv6 Router Advertisement configurations for interface Eth1/1
      dellemc.enterprise_sonic.sonic_ipv6_router_advertisement:
        config:
          - name: 'Eth1/1'
        state: deleted

    # After State:
    # ------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    # !
    # interface Eth1/2
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  no ipv6 nd suppress-ra
    #  ipv6 nd adv-interval-option
    #  ipv6 nd router-preference low
    #  ipv6 nd prefix 1000:0:0:1000::/64 86400 86400 off-link no-autoconfig
    # !


    # Using deleted
    #
    # Before State:
    # -------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  no ipv6 nd suppress-ra
    #  ipv6 nd ra-hop-limit 10
    #  ipv6 nd ra-interval 180
    #  ipv6 nd min-ra-interval 60
    #  ipv6 nd ra-lifetime 360
    #  ipv6 nd ra-retrans-interval 30000
    #  ipv6 nd dnssl test.com 3600
    #  ipv6 nd rdnss 100::100 3600
    #  ipv6 nd rdnss 100::200 7200
    # !
    # interface Eth1/2
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  no ipv6 nd suppress-ra
    #  ipv6 nd adv-interval-option
    #  ipv6 nd router-preference low
    #  ipv6 nd prefix 1000:0:0:1000::/64 86400 86400 off-link no-autoconfig
    # !

    - name: Delete all IPv6 Router Advertisement configurations
      dellemc.enterprise_sonic.sonic_ipv6_router_advertisement:
        config:
        state: deleted

    # After State:
    # ------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    # !
    # interface Eth1/2
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    # !


    # Using replaced
    #
    # Before State:
    # -------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  no ipv6 nd suppress-ra
    #  ipv6 nd ra-hop-limit 10
    #  ipv6 nd ra-interval 180
    #  ipv6 nd min-ra-interval 60
    #  ipv6 nd ra-lifetime 360
    #  ipv6 nd router-preference high
    # !
    # interface Eth1/2
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  no ipv6 nd suppress-ra
    #  no ipv6 nd ra-fast-retrans
    #  ipv6 nd adv-interval-option
    #  ipv6 nd min-ra-interval msec 45500
    #  ipv6 nd ra-hop-limit 10
    #  ipv6 nd reachable-time 1200000
    #  ipv6 nd prefix 1000:0:0:1000::/64 86400 86400 off-link no-autoconfig
    #  ipv6 nd prefix 1000:0:0:2000::/64 86400 86400 off-link no-autoconfig
    # !

    - name: Replace IPv6 Router Advertisement configurations for interface Eth1/2
      dellemc.enterprise_sonic.sonic_ipv6_router_advertisement:
        config:
          - name: 'Eth1/2'
            suppress: false
            ra_interval: 300
            router_preference: high
            ra_prefixes:
              - prefix: 2000:0:0:1000::/64
                valid_lifetime: 3600
                preferred_lifetime: 3600
                router_address: true
        state: replaced

    # After State:
    # ------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  no ipv6 nd suppress-ra
    #  ipv6 nd ra-hop-limit 10
    #  ipv6 nd ra-interval 180
    #  ipv6 nd min-ra-interval 60
    #  ipv6 nd ra-lifetime 360
    #  ipv6 nd router-preference high
    # !
    # interface Eth1/2
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  no ipv6 nd suppress-ra
    #  ipv6 nd ra-interval 300
    #  ipv6 nd router-preference high
    #  ipv6 nd prefix 2000:0:0:1000::/64 3600 3600 router-address
    # !


    # Using overridden
    #
    # Before State:
    # -------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  no ipv6 nd suppress-ra
    #  ipv6 nd ra-hop-limit 10
    #  ipv6 nd ra-interval 180
    #  ipv6 nd min-ra-interval 60
    #  ipv6 nd ra-lifetime 360
    #  ipv6 nd router-preference high
    # !
    # interface Eth1/2
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  no ipv6 nd suppress-ra
    #  ipv6 nd ra-interval 300
    #  ipv6 nd router-preference high
    #  ipv6 nd prefix 2000:0:0:1000::/64 3600 3600 router-address
    # !
    # interface Eth1/3
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    # !

    - name: Override all IPv6 Router Advertisement configurations
      dellemc.enterprise_sonic.sonic_ipv6_router_advertisement:
        config:
          - name: 'Eth1/1'
            suppress: false
            home_agent_config: true
            home_agent_lifetime: 7200
            home_agent_preference: 100
          - name: 'Eth1/3'
            suppress: false
            managed_config: true
            other_config: true
            ra_retrans_interval: 30000
        state: overridden

    # After State:
    # ------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  no ipv6 nd suppress-ra
    #  ipv6 nd home-agent-config-flag
    #  ipv6 nd home-agent-lifetime 7200
    #  ipv6 nd home-agent-preference 100
    # !
    # interface Eth1/2
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    # !
    # interface Eth1/3
    #  mtu 9100
    #  speed 400000
    #  fec RS
    #  no shutdown
    #  no ipv6 nd suppress-ra
    #  ipv6 nd managed-config-flag
    #  ipv6 nd other-config-flag
    #  ipv6 nd ra-retrans-interval 30000
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
                            <div>The configuration resulting from module invocation.</div>
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
                            <div>The configuration that would be generated by module invocation.</div>
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

- Arun Saravanan Balachandran (@ArunSaravananBalachandran)
