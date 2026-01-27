.. _dellemc.enterprise_sonic.sonic_static_routes_module:


********************************************
dellemc.enterprise_sonic.sonic_static_routes
********************************************

**Manage static routes configuration on SONiC**


Version added: 2.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of static routes for devices running SONiC




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="5">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="5">
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
                        <div>Manages &#x27;static_routes&#x27; configurations</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>static_list</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A list of &#x27;static_routes&#x27; configurations.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>next_hops</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A list of next-hops to be utilised for the static route being specified.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>index</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>An identifier utilised to uniquely reference the next-hop.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>blackhole</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Indicates that packets matching this route should be discarded.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interface</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The reference to a base interface.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>next_hop</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The next-hop that is to be used for the static route.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>nexthop_vrf</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of the next-hop network instance for leaked routes.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>metric</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the preference of the next-hop entry when it is injected into the RIB.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>tag</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The tag value for the static route.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>track</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The IP SLA track ID for static route.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Destination prefix for the static route, either IPv4 or IPv6.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vrf_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of the configured VRF on the device.</div>
                </td>
            </tr>

            <tr>
                <td colspan="5">
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
   - Supports ``check_mode``.



Examples
--------

.. code-block:: yaml

    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration | grep "ip route"
    # (No "ip route" configuration present)

    - name: Merge static routes configurations
      dellemc.enterprise_sonic.sonic_static_routes:
        config:
          - vrf_name: 'default'
            static_list:
              - prefix: '2.0.0.0/8'
                next_hops:
                  - index:
                      interface: 'Ethernet4'
                    metric: 1
                    tag: 2
                    track: 3
                  - index:
                    next_hop: '3.0.0.0'
                    metric: 2
                    tag: 4
                    track: 8
          - vrf_name: 'VrfReg1'
            static_list:
              - prefix: '3.0.0.0/8'
                next_hops:
                  - index:
                      interface: 'eth0'
                      nexthop_vrf: 'VrfReg2'
                      next_hop: '4.0.0.0'
                    metric: 4
                    tag: 5
                    track: 6
                  - index:
                      blackhole: true
                    metric: 10
                    tag: 20
                    track: 30
        state: merged

    # After state:
    # ------------
    #
    # sonic# show running-configuration | grep "ip route"
    # ip route 2.0.0.0/8 3.0.0.0 tag 4 track 8 2
    # ip route 2.0.0.0/8 interface Ethernet4 tag 2 track 3 1
    # ip route vrf VrfReg1 3.0.0.0/8 4.0.0.0 interface Management 0 nexthop-vrf VrfReg2 tag 5 track 6 4
    # ip route vrf VrfReg1 3.0.0.0/8 blackhole tag 20 track 30 10
    #
    #
    # Modifying previous merge

    - name: Modify static routes configurations
      dellemc.enterprise_sonic.sonic_static_routes:
        config:
          - vrf_name: 'VrfReg1'
            static_list:
              - prefix: '3.0.0.0/8'
                next_hops:
                  - index:
                      blackhole: true
                    metric: 11
                    tag: 22
                    track: 33
        state: merged

    # After state:
    # ------------
    #
    # sonic# show running-configuration | grep "ip route"
    # ip route 2.0.0.0/8 3.0.0.0 tag 4 track 8 2
    # ip route 2.0.0.0/8 interface Ethernet4 tag 2 track 3 1
    # ip route vrf VrfReg1 3.0.0.0/8 4.0.0.0 interface Management 0 nexthop-vrf VrfReg2 tag 5 track 6 4
    # ip route vrf VrfReg1 3.0.0.0/8 blackhole tag 22 track 33 11


    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration | grep "ip route"
    # ip route 4.0.0.0/8 2.0.0.0 tag 4 track 8 2

    - name: Override static routes configurations
      dellemc.enterprise_sonic.sonic_static_routes:
        config:
          - vrf_name: 'VrfReg2'
            static_list:
              - prefix: '3.0.0.0/8'
                next_hops:
                  - index:
                      blackhole: true
                    metric: 10
                    tag: 20
                    track: 30
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show running-configuration | grep "ip route"
    # ip route vrf VrfReg2 3.0.0.0/8 blackhole tag 20 track 30 10


    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration | grep "ip route"
    # ip route 4.0.0.0/8 2.0.0.0 tag 4 track 8 2

    - name: Replace static routes configurations
      dellemc.enterprise_sonic.sonic_static_routes:
        config:
          - vrf_name: 'default'
            static_list:
              - prefix: '4.0.0.0/8'
                next_hops:
                  - index:
                      blackhole: true
                    metric: 5
                    tag: 10
                    track: 15
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show running-configuration | grep "ip route"
    # ip route 4.0.0.0/8 blackhole tag 10 track 15 5


    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration | grep "ip route"
    # ip route 2.0.0.0/8 3.0.0.0 tag 4 track 8 2
    # ip route 2.0.0.0/8 interface Ethernet4 tag 2 track 3 1
    # ip route vrf VrfReg1 3.0.0.0/8 4.0.0.0 interface Management 0 nexthop-vrf VrfReg2 tag 5 track 6 4
    # ip route vrf VrfReg1 3.0.0.0/8 blackhole tag 22 track 33 11

    - name: Delete static routes configurations
      dellemc.enterprise_sonic.sonic_static_routes:
        config:
          - vrf_name: 'default'
            static_list:
              - prefix: '2.0.0.0/8'
                next_hops:
                  - index:
                      interface: 'Ethernet4'
          - vrf_name: 'VrfReg1'
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration | grep "ip route"
    # ip route 2.0.0.0/8 3.0.0.0 tag 4 track 8 2



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

- S. Talabi (@stalabi1)
