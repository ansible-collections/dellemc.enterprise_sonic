.. _dellemc.enterprise_sonic.sonic_ospf_area_module:


****************************************
dellemc.enterprise_sonic.sonic_ospf_area
****************************************

**configure OSPF area settings on SONiC**


Version added: 2.5.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration for the area settings of OSPF running on SONiC switches




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
                        <div>Specifies configuration for OSPFv2 areas</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>area_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Area ID of the network (A.B.C.D or 0 to 4294967295).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>authentication_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>message_digest</li>
                                    <li>text</li>
                        </ul>
                </td>
                <td>
                        <div>authentication type for area</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>default_cost</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure NSSA or stub area summary default cost</div>
                        <div>range is 0 to 16777215 inclusive</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>filter_list_in</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>inter area prefix filter list.</div>
                        <div>Filter incoming prefixes into the area.</div>
                        <div>expects name of a prefix list.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>filter_list_out</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>inter area prefix filter list.</div>
                        <div>Filter outgoing prefixes from the area.</div>
                        <div>expects name of a prefix list.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>networks</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure networks in an area</div>
                        <div>is a masked ip address</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ranges</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure address range summarization on border routers</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>advertise</b>
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
                        <div>enable address range advertising</div>
                        <div>default of true</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>cost</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>configure cost of address range</div>
                        <div>range is 0 to 16777215 inclusive</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>address range prefix</div>
                        <div>is a masked ip address</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>substitute</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure substitute prefix for the address range</div>
                        <div>is a masked ip address</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>shortcut</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>default</li>
                                    <li>disable</li>
                                    <li>enable</li>
                        </ul>
                </td>
                <td>
                        <div>Configure area&#x27;s shortcut mode</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>stub</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>configuration for stub type area</div>
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
                        <div>configure area as stub type area</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>no_summary</b>
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
                        <div>disable inter-area route injection into the stub</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>virtual_links</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>configuration for virtual links</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>authentication</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>configure authentication settings for virtual link</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>auth_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>message_digest</li>
                                    <li>text</li>
                                    <li>none</li>
                        </ul>
                </td>
                <td>
                        <div>authentication type for virtual link</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>text authentication password for virtual link</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>key_encrypted</b>
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
                        <div>password is in encrypted format</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dead_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>configure adjacency dead interval</div>
                        <div>value is in seconds</div>
                        <div>range is 1 to 65535 inclusive</div>
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
                        <div>enable virtual link</div>
                        <div>virtual link must be enabled for creation</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>hello_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>configure neighbor hello interval</div>
                        <div>value is in seconds</div>
                        <div>range is 1 to 65535 inclusive</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>message_digest_list</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>configure message-digest authentication keys</div>
                        <div>For deletion, only the key_id is used.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>authentication password (ignored for deletion)</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>key_encrypted</b>
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
                        <div>password is in encrypted format (ignored for deletion)</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>key_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>message-digest authentication key id</div>
                        <div>range is 1 to 255 inclusive</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>retransmit_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>configure LSA retransmit interval</div>
                        <div>value is in seconds</div>
                        <div>range is 1 to 65535 inclusive</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>router_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>router id of the remote ABR</div>
                        <div>ip address format</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>transmit_delay</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>configure LSA transmit delay</div>
                        <div>value is in seconds</div>
                        <div>range is 1 to 65535 inclusive</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vrf_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">"default"</div>
                </td>
                <td>
                        <div>name of the vrf this area belongs to</div>
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
                        <div>Specifies the type of configuration update to be performed on the device.</div>
                </td>
            </tr>
    </table>
    <br/>




Examples
--------

.. code-block:: yaml

    # NOTE: Configuration of an OSPF network instance (VRF) is required before an OSPF "area" can
    # be configured in association with that network instance (VRF).

    # ============ MERGED ==================

    # Scenario: Using "merged" state to add or change ospf_area settings
    # merging all settings for an area

    # Before state:

    # sonic# show running-configuration ospf
    # router ospf vrf Vrf1
    # !
    # router ospf vrf Vrf2
    # !

    # example:
    - name: merge examples of all settings
      sonic_ospf_area:
        state: merged
        config:
          - area_id: 2
            vrf_name: Vrf1
            authentication_type: message_digest
            default_cost: 3
            stub:
              enabled: true
              no_summary: true
            shortcut: default
          - area_id: 3
            vrf_name: Vrf1
            filter_list_in: pf1
            filter_list_out: pf2
            ranges:
              - prefix: 1.1.1.1/24
              - prefix: 1.1.1.2/24
                advertise: true
                cost: 4
              - prefix: 1.1.1.3/24
                advertise: false
              - prefix: 1.1.1.4/24
                advertise: true
                cost: 10
                substitute: 3.3.3.3/24
          - area_id: 4
            vrf_name: Vrf1
            networks:
              - 1.1.1.1/24
              - 3.5.1.5/23
              - 23.235.75.1/23
          - area_id: 5
            vrf_name: Vrf1
            virtual_links:
              - router_id: 34.7.35.1
                enabled: true
              - router_id: 34.7.35.2
                enabled: true
                dead_interval: 30
                hello_interval: 10
                retransmit_interval: 40
                transmit_delay: 50
                authentication:
                  auth_type: text
                  key: "U2FsdGVkX197YJtZ/3Ac6n5kRIG/ZqeU1/wC0cVFyfU="
                  key_encrypted: true
                message_digest_list:
                  - key_id: 1
                    key: "U2FsdGVkX1/wbqjMB7Lr+Mm3wY8+lCdaqUmG2rr9Adw="
                    key_encrypted: true
                  - key_id: 2
                    key: "U2FsdGVkX18Czj9r8skDrg/wtpwTKKCQ8FXUehpCmHc="
                    key_encrypted: true

    # After state

    # sonic# show running-configuration ospf
    # router ospf vrf Vrf1
    #  area 0.0.0.2 authentication message-digest
    #  area 0.0.0.2 stub no-summary
    #  area 0.0.0.2 default-cost 3
    #  area 0.0.0.2 shortcut default
    #  area 0.0.0.3 filter-list prefix pf1 in
    #  area 0.0.0.3 filter-list prefix pf2 out
    #  area 0.0.0.4
    #  area 0.0.0.5
    #  area 0.0.0.5 virtual-link 34.7.35.1
    #  area 0.0.0.5 virtual-link 34.7.35.2
    #  area 0.0.0.5 virtual-link 34.7.35.2 authentication
    #  area 0.0.0.5 virtual-link 34.7.35.2 authentication-key U2FsdGVkX197YJtZ/3Ac6n5kRIG/ZqeU1/wC0cVFyfU= encrypted
    #  area 0.0.0.5 virtual-link 34.7.35.2 dead-interval 30
    #  area 0.0.0.5 virtual-link 34.7.35.2 hello-interval 10
    #  area 0.0.0.5 virtual-link 34.7.35.2 retransmit-interval 40
    #  area 0.0.0.5 virtual-link 34.7.35.2 transmit-delay 50
    #  area 0.0.0.5 virtual-link 34.7.35.2 message-digest-key 1 md5 U2FsdGVkX1/wbqjMB7Lr+Mm3wY8+lCdaqUmG2rr9Adw= encrypted
    #  area 0.0.0.5 virtual-link 34.7.35.2 message-digest-key 2 md5 U2FsdGVkX18Czj9r8skDrg/wtpwTKKCQ8FXUehpCmHc= encrypted
    #  area 0.0.0.3 range 1.1.1.1/24
    #  area 0.0.0.3 range 1.1.1.2/24 advertise cost 4
    #  area 0.0.0.3 range 1.1.1.3/24 not-advertise
    #  area 0.0.0.3 range 1.1.1.4/24 advertise cost 10
    #  area 0.0.0.3 range 1.1.1.4/24 substitute 3.3.3.3/24
    #  network 1.1.1.1/24 area 0.0.0.4
    #  network 23.235.75.1/23 area 0.0.0.4
    #  network 3.5.1.5/23 area 0.0.0.4
    # !
    # router ospf vrf Vrf2
    # !
    # -----

    # Scenario: minimum data for config subsections

    # Before state:

    # sonic# show running-configuration ospf
    # router ospf vrf Vrf1
    # !
    # router ospf vrf Vrf2
    # !

    # example:
    - name: merge smallest group of settings
      sonic_ospf_area:
        state: merged
        config:
          - area_id: 0.0.0.2
            vrf_name: Vrf1
            networks:
              - 1.1.1.1/24
          - area_id: 0.0.0.3
            vrf_name: Vrf1
            ranges:
              - prefix: 1.1.1.1/24
          - area_id: 0.0.0.4
            vrf_name: Vrf1
            virtual_links:
              - router_id: 34.7.35.1
                enabled: true
          - area_id: 0.0.0.5
            vrf_name: Vrf1
            virtual_links:
              - router_id: 34.7.35.1
                enabled: true
                message_digest_list:
                  - key_id: 1
                    key: grighr
    # NOTE: The existence of an 'area' is only displayed by this Ansible module if configuration options are
    # currently configured for that area. (An "area" that currently has no configured sub-options is not displayed.)

    # After state

    # sonic# show running-configuration ospf
    # router ospf vrf Vrf1
    #  area 0.0.0.2
    #  area 0.0.0.3
    #  area 0.0.0.4
    #  area 0.0.0.5
    #  area 0.0.0.4 virtual-link 34.7.35.1
    #  area 0.0.0.5 virtual-link 34.7.35.1
    #  area 0.0.0.5 virtual-link 34.7.35.1 message-digest-key 1 md5 U2FsdGVkX19oCaX2HsxLR2nWtyK15AfE7ajHVjzgoaY= encrypted
    #  area 0.0.0.3 range 1.1.1.1/24
    #  network 1.1.1.1/24 area 0.0.0.2
    # !
    # router ospf vrf Vrf2
    # !
    # -----

    # Scenario: merging and making changes to attributes

    # Before state:

    # sonic# show running-configuration ospf
    # router ospf vrf Vrf1
    #  area 0.0.0.1 authentication message-digest
    #  area 0.0.0.1 stub no-summary
    #  area 0.0.0.1 default-cost 6
    #  area 0.0.0.1 filter-list prefix pf1 in
    #  area 0.0.0.1 filter-list prefix pf2 out
    #  area 0.0.0.1 shortcut disable
    #  area 0.0.0.1 virtual-link 1.1.1.1
    #  area 0.0.0.1 virtual-link 1.1.1.1 authentication
    #  area 0.0.0.1 virtual-link 1.1.1.1 authentication-key U2FsdGVkX18zN46d3pzk+t7TofEHAZGY+5RvgXMwDiQ= encrypted
    #  area 0.0.0.1 virtual-link 1.1.1.1 dead-interval 20
    #  area 0.0.0.1 virtual-link 1.1.1.1 hello-interval 10
    #  area 0.0.0.1 virtual-link 1.1.1.1 retransmit-interval 10
    #  area 0.0.0.1 virtual-link 1.1.1.1 transmit-delay 10
    #  area 0.0.0.1 virtual-link 1.1.1.2
    #  area 0.0.0.1 virtual-link 1.1.1.2 dead-interval 34
    #  area 0.0.0.1 virtual-link 1.1.1.1 message-digest-key 1 md5 U2FsdGVkX1//fyBCsQYQI4q743L8Rf1Q1qUOEc75lNM= encrypted
    #  area 0.0.0.1 virtual-link 1.1.1.1 message-digest-key 2 md5 U2FsdGVkX18tvS+HyOt1zIbx9P8I9NMguQ17NZGd9ZY= encrypted
    #  area 0.0.0.1 range 1.1.1.1/24 not-advertise
    #  area 0.0.0.1 range 1.1.1.2/24 advertise
    #  network 1.1.1.1/24 area 0.0.0.1
    #  network 1.1.1.2/24 area 0.0.0.1
    # !
    # router ospf vrf Vrf2
    # !

    # example:
    - name: "test merge all settings"
      sonic_ospf_area:
        state: merged
        config:
          - area_id: 0.0.0.1
            vrf_name: Vrf1
            authentication_type: text
            default_cost: 5
            filter_list_in: pf2
            filter_list_out: pf1
            networks:
              - 1.1.1.5/24
            ranges:
              - prefix: 1.1.1.1/24
                advertise: true
                cost: 12
                substitute: 11.11.1.1/24
              - prefix: 1.1.1.2/24
                advertise: false
            shortcut: enable
            stub:
              enabled: true
              no_summary: false
            virtual_links:
              - router_id: 1.1.1.1
                enabled: true
                dead_interval: 45
                hello_interval: 21
                retransmit_interval: 15
                transmit_delay: 23
                authentication:
                  auth_type: text
                  key: "U2FsdGVkX1/lz7KE/onDUAhQU2nftsm/nddLb2ZvYSQ="
                  key_encrypted: true
                message_digest_list:
                  - key_id: 1
                    key: "somepass"
              - router_id: 1.1.1.2
                enabled: true
                dead_interval: 16

    # After state

    # sonic# show running-configuration ospf
    # router ospf vrf Vrf1
    #  area 0.0.0.1 authentication
    #  area 0.0.0.1 stub
    #  area 0.0.0.1 default-cost 5
    #  area 0.0.0.1 filter-list prefix pf2 in
    #  area 0.0.0.1 filter-list prefix pf1 out
    #  area 0.0.0.1 shortcut enable
    #  area 0.0.0.1 virtual-link 1.1.1.1
    #  area 0.0.0.1 virtual-link 1.1.1.1 authentication
    #  area 0.0.0.1 virtual-link 1.1.1.1 authentication-key U2FsdGVkX1/lz7KE/onDUAhQU2nftsm/nddLb2ZvYSQ= encrypted
    #  area 0.0.0.1 virtual-link 1.1.1.1 dead-interval 45
    #  area 0.0.0.1 virtual-link 1.1.1.1 hello-interval 21
    #  area 0.0.0.1 virtual-link 1.1.1.1 retransmit-interval 15
    #  area 0.0.0.1 virtual-link 1.1.1.1 transmit-delay 23
    #  area 0.0.0.1 virtual-link 1.1.1.2
    #  area 0.0.0.1 virtual-link 1.1.1.2 dead-interval 16
    #  area 0.0.0.1 virtual-link 1.1.1.1 message-digest-key 1 md5 U2FsdGVkX18D0swlrl3pVzMGxRZYzY58X06jPq2CrNU= encrypted
    #  area 0.0.0.1 virtual-link 1.1.1.1 message-digest-key 2 md5 U2FsdGVkX18tvS+HyOt1zIbx9P8I9NMguQ17NZGd9ZY= encrypted
    #  area 0.0.0.1 range 1.1.1.1/24 advertise cost 12
    #  area 0.0.0.1 range 1.1.1.1/24 substitute 11.11.1.1/24
    #  area 0.0.0.1 range 1.1.1.2/24 not-advertise
    #  network 1.1.1.1/24 area 0.0.0.1
    #  network 1.1.1.2/24 area 0.0.0.1
    #  network 1.1.1.5/24 area 0.0.0.1
    # !
    # router ospf vrf Vrf2
    # !
    # -----

    # Scenario: merging different keys

    # Before state:

    # sonic# show running-configuration ospf
    # router ospf vrf Vrf1
    # !
    # router ospf vrf Vrf2
    # !

    # example:
    - name: "test merge different keys"
      sonic_ospf_area:
        state: merged
        config:
          - area_id: 0.0.0.1
            vrf_name: Vrf1
            virtual_links:
              - router_id: 1.1.1.1
                enabled: true
                authentication:
                  key: qwerty
                  key_encrypted: false
              - router_id: 1.1.1.3
                enabled: true
                authentication:
                  key: "U2FsdGVkX1/lz7KE/onDUAhQU2nftsm/nddLb2ZvYSQ="
                  key_encrypted: true
              - router_id: 1.1.1.4
                enabled: true
                authentication:
                  key: somepass

    # After state

    # sonic# show running-configuration ospf
    # router ospf vrf Vrf1
    #  area 0.0.0.1
    #  area 0.0.0.1 virtual-link 1.1.1.1
    #  area 0.0.0.1 virtual-link 1.1.1.1 authentication-key U2FsdGVkX180JKbs3Rf5IyLot8UW0/srcXdGaQXEHiw= encrypted
    #  area 0.0.0.1 virtual-link 1.1.1.3
    #  area 0.0.0.1 virtual-link 1.1.1.3 authentication-key U2FsdGVkX1/lz7KE/onDUAhQU2nftsm/nddLb2ZvYSQ= encrypted
    #  area 0.0.0.1 virtual-link 1.1.1.4
    #  area 0.0.0.1 virtual-link 1.1.1.4 authentication-key U2FsdGVkX1+2i/anKXKpEfwZIAkb1Hzkx1nH2IBnlMA= encrypted
    # !
    # router ospf vrf Vrf2
    # !
    # Note: the device automatically converts keys to encrypted format
    # ----------

    # ============ DELETED ==================

    # using deleted to remove ospf settings
    # Scenario: deleting all settings for areas

    # Before state:

    # sonic# show running-configuration ospf
    # router ospf vrf Vrf1
    #  area 0.0.0.1 authentication message-digest
    #  area 0.0.0.1 stub no-summary
    #  area 0.0.0.1 default-cost 6
    #  area 0.0.0.1 filter-list prefix pf1 in
    #  area 0.0.0.1 filter-list prefix pf2 out
    #  area 0.0.0.1 shortcut disable
    #  area 0.0.0.2 stub no-summary
    #  area 0.0.0.2 shortcut disable
    #  area 0.0.0.3 shortcut default
    #  area 0.0.0.1 virtual-link 1.1.1.1
    #  area 0.0.0.1 virtual-link 1.1.1.1 authentication
    #  area 0.0.0.1 virtual-link 1.1.1.1 authentication-key U2FsdGVkX18zN46d3pzk+t7TofEHAZGY+5RvgXMwDiQ= encrypted
    #  area 0.0.0.1 virtual-link 1.1.1.1 dead-interval 20
    #  area 0.0.0.1 virtual-link 1.1.1.1 hello-interval 10
    #  area 0.0.0.1 virtual-link 1.1.1.1 retransmit-interval 10
    #  area 0.0.0.1 virtual-link 1.1.1.1 transmit-delay 10
    #  area 0.0.0.1 virtual-link 1.1.1.2
    #  area 0.0.0.1 virtual-link 1.1.1.2 dead-interval 34
    #  area 0.0.0.1 virtual-link 1.1.1.1 message-digest-key 1 md5 U2FsdGVkX1//fyBCsQYQI4q743L8Rf1Q1qUOEc75lNM= encrypted
    #  area 0.0.0.1 virtual-link 1.1.1.1 message-digest-key 2 md5 U2FsdGVkX18tvS+HyOt1zIbx9P8I9NMguQ17NZGd9ZY= encrypted
    #  area 0.0.0.1 range 1.1.1.1/24 not-advertise
    #  area 0.0.0.1 range 1.1.1.2/24 advertise
    #  area 0.0.0.2 range 1.1.1.1/24 advertise
    #  area 0.0.0.3 range 1.1.4.6/24 cost 14
    #  network 1.1.1.1/24 area 0.0.0.1
    #  network 1.1.1.2/24 area 0.0.0.1
    # !
    # router ospf vrf Vrf2
    # !

    # example:
    - name: "test delete all settings for areas"
      sonic_ospf_area:
        state: deleted
        config:
          - area_id: 0.0.0.1
            vrf_name: Vrf1
          - area_id: 0.0.0.2
            vrf_name: Vrf1
            ranges:
              - prefix: 1.1.1.1/24
            shortcut: disable
            stub:
              enabled: true
              no_summary: true

    # After state

    # sonic# show running-configuration ospf
    # router ospf vrf Vrf1
    #  area 0.0.0.3 shortcut default
    #  area 0.0.0.3 range 1.1.4.6/24 cost 14
    # !
    # router ospf vrf Vrf2
    # !
    # -----


    # Scenario: clearing subsections of config

    # Before state:

    # sonic# show running-configuration ospf
    # router ospf vrf Vrf1
    #  area 0.0.0.1 shortcut default
    #  area 0.0.0.2 authentication message-digest
    #  area 0.0.0.3 filter-list prefix pf1 in
    #  area 0.0.0.4
    #  area 0.0.0.3 virtual-link 34.7.35.1
    #  area 0.0.0.3 virtual-link 34.7.35.1 hello-interval 30
    #  area 0.0.0.3 virtual-link 34.7.35.1 transmit-delay 50
    #  area 0.0.0.3 virtual-link 34.7.35.2
    #  area 0.0.0.3 virtual-link 34.7.35.2 dead-interval 10
    #  area 0.0.0.3 virtual-link 34.7.35.2 retransmit-interval 40
    #  area 0.0.0.4 virtual-link 34.7.35.1
    #  area 0.0.0.4 virtual-link 34.7.35.1 authentication
    #  area 0.0.0.4 virtual-link 34.7.35.1 authentication-key U2FsdGVkX1/lz7KE/onDUAhQU2nftsm/nddLb2ZvYSQ= encrypted
    #  area 0.0.0.4 virtual-link 34.7.35.1 dead-interval 10
    #  area 0.0.0.4 virtual-link 34.7.35.2
    #  area 0.0.0.4 virtual-link 34.7.35.2 dead-interval 10
    #  area 0.0.0.4 virtual-link 34.7.35.2 message-digest-key 1 md5 U2FsdGVkX18mUZjlJL/Q/7vYtx2UyDc+NcLKc/BOJUA= encrypted
    #  area 0.0.0.4 virtual-link 34.7.35.2 message-digest-key 3 md5 U2FsdGVkX19SlRpqsnpeRmjq7WmtctYtveHlYF0Faqo= encrypted
    #  area 0.0.0.1 range 1.1.1.2/24 advertise cost 4
    #  area 0.0.0.1 range 1.1.1.3/24 not-advertise
    #  network 1.1.1.1/24 area 0.0.0.2
    #  network 23.235.75.1/23 area 0.0.0.2
    #  network 3.5.1.5/23 area 0.0.0.2
    # !
    # router ospf vrf Vrf2
    # !

    # example:
    - name: "test clear subsections"
      sonic_ospf_area:
        state: deleted
        config:
          - area_id: 0.0.0.1
            vrf_name: Vrf1
            ranges: []
          - area_id: 0.0.0.2
            vrf_name: Vrf1
            networks: []
          - area_id: 0.0.0.3
            vrf_name: Vrf1
            virtual_links: []
          - area_id: 4
            vrf_name: Vrf1
            virtual_links:
              - router_id: 34.7.35.1
                authentication: {}
              - router_id: 34.7.35.2
                message_digest_list: []

    # After state

    # sonic# show running-configuration ospf
    # router ospf vrf Vrf1
    #  area 0.0.0.1 shortcut default
    #  area 0.0.0.2 authentication message-digest
    #  area 0.0.0.3 filter-list prefix pf1 in
    #  area 0.0.0.4
    #  area 0.0.0.4 virtual-link 34.7.35.1
    #  area 0.0.0.4 virtual-link 34.7.35.1 dead-interval 10
    #  area 0.0.0.4 virtual-link 34.7.35.2
    #  area 0.0.0.4 virtual-link 34.7.35.2 dead-interval 10
    # !
    # router ospf vrf Vrf2
    # !
    # -----

    # Scenario: deleting individual attributes

    # Before state:

    # sonic# show running-configuration ospf
    # router ospf vrf Vrf1
    #  area 0.0.0.1 filter-list prefix pf1 in
    #  area 0.0.0.1 filter-list prefix pf2 out
    #  area 0.0.0.2 authentication message-digest
    #  area 0.0.0.3
    #  area 0.0.0.4 stub no-summary
    #  area 0.0.0.4 default-cost 3
    #  area 0.0.0.4 shortcut default
    #  area 0.0.0.5 stub
    #  area 0.0.0.5 default-cost 5
    #  area 0.0.0.3 virtual-link 34.7.35.1
    #  area 0.0.0.3 virtual-link 34.7.35.1 authentication
    #  area 0.0.0.3 virtual-link 34.7.35.1 authentication-key U2FsdGVkX18zN46d3pzk+t7TofEHAZGY+5RvgXMwDiQ= encrypted
    #  area 0.0.0.3 virtual-link 34.7.35.1 hello-interval 30
    #  area 0.0.0.3 virtual-link 34.7.35.1 transmit-delay 50
    #  area 0.0.0.3 virtual-link 34.7.35.2
    #  area 0.0.0.3 virtual-link 34.7.35.2 authentication message-digest
    #  area 0.0.0.3 virtual-link 34.7.35.2 authentication-key U2FsdGVkX18zN46d3pzk+t7TofEHAZGY+5RvgXMwDiQ= encrypted
    #  area 0.0.0.3 virtual-link 34.7.35.2 dead-interval 10
    #  area 0.0.0.3 virtual-link 34.7.35.2 retransmit-interval 40
    #  area 0.0.0.3 virtual-link 34.7.35.2 transmit-delay 50
    #  area 0.0.0.3 virtual-link 34.7.35.2 message-digest-key 1 md5 U2FsdGVkX18mUZjlJL/Q/7vYtx2UyDc+NcLKc/BOJUA= encrypted
    #  area 0.0.0.3 virtual-link 34.7.35.2 message-digest-key 3 md5 U2FsdGVkX19SlRpqsnpeRmjq7WmtctYtveHlYF0Faqo= encrypted
    #  area 0.0.0.1 range 1.1.1.1/24 advertise cost 13
    #  area 0.0.0.1 range 1.1.1.1/24 substitute 11.2.5.1/24
    #  area 0.0.0.1 range 1.1.1.2/24 advertise cost 4
    #  area 0.0.0.1 range 1.1.1.3/24 advertise
    #  area 0.0.0.1 range 1.1.1.3/24 substitute 2.2.2.2/24
    #  area 0.0.0.1 range 1.1.1.4/24 advertise cost 34
    #  area 0.0.0.1 range 1.1.1.4/24 substitute 3.3.3.3/24
    #  network 1.1.1.1/24 area 0.0.0.2
    #  network 23.235.75.1/23 area 0.0.0.2
    #  network 3.5.1.5/23 area 0.0.0.2
    # !
    # router ospf vrf Vrf2
    # !

    # example:
    - name: "delete individual attributes"
      sonic_ospf_area:
        state: deleted
        config:
          - area_id: 0.0.0.1
            vrf_name: Vrf1
            filter_list_in: pf1
            filter_list_out: pf2
            ranges:
              - prefix: 1.1.1.1/24
              - prefix: 1.1.1.2/24
                cost: 4
              - prefix: 1.1.1.3/24
                substitute: 2.2.2.2/24
          - area_id: 0.0.0.2
            vrf_name: Vrf1
            authentication_type: message_digest
            networks:
              - 1.1.1.1/24
              - 3.5.1.5/23
          - area_id: 3
            vrf_name: Vrf1
            virtual_links:
              - router_id: 34.7.35.1
                transmit_delay: 50
                hello_interval: 30
                authentication:
                  auth_type: text
              - router_id: 34.7.35.2
                enabled: true
                dead_interval: 10
                retransmit_interval: 40
                message_digest_list:
                  - key_id: 1
                authentication:
                  key: "U2FsdGVkX18zN46d3pzk+t7TofEHAZGY+5RvgXMwDiQ="
                  key_encrypted: true
          - area_id: 4
            vrf_name: Vrf1
            shortcut: default
            stub:
              enabled: true
              no_summary: true
          - area_id: 5
            vrf_name: Vrf1
            default_cost: 5
            stub:
              enabled: true

    # After state

    # sonic# show running-configuration ospf
    # router ospf vrf Vrf1
    #  area 0.0.0.1
    #  area 0.0.0.2
    #  area 0.0.0.3
    #  area 0.0.0.4 default-cost 3
    #  area 0.0.0.5
    #  area 0.0.0.3 virtual-link 34.7.35.1
    #  area 0.0.0.3 virtual-link 34.7.35.1 authentication-key U2FsdGVkX18zN46d3pzk+t7TofEHAZGY+5RvgXMwDiQ= encrypted
    #  area 0.0.0.3 virtual-link 34.7.35.2
    #  area 0.0.0.3 virtual-link 34.7.35.2 authentication message-digest
    #  area 0.0.0.3 virtual-link 34.7.35.2 transmit-delay 50
    #  area 0.0.0.3 virtual-link 34.7.35.2 message-digest-key 3 md5 U2FsdGVkX19SlRpqsnpeRmjq7WmtctYtveHlYF0Faqo= encrypted
    #  area 0.0.0.1 range 1.1.1.2/24 advertise
    #  area 0.0.0.1 range 1.1.1.3/24 advertise
    #  area 0.0.0.1 range 1.1.1.4/24 advertise cost 34
    #  area 0.0.0.1 range 1.1.1.4/24 substitute 3.3.3.3/24
    #  network 23.235.75.1/23 area 0.0.0.2
    # !
    # router ospf vrf Vrf2
    # !
    # -----
    # ----------


    # ============ REPLACED ==================

    # Scenario: Replace listed areas

    # Before state:

    # sonic# show running-configuration ospf
    # router ospf vrf Vrf1
    #  area 0.0.0.1 filter-list prefix pf1 in
    #  area 0.0.0.1 filter-list prefix pf2 out
    #  area 0.0.0.2 authentication message-digest
    #  area 0.0.0.3
    #  area 0.0.0.4 stub no-summary
    #  area 0.0.0.4 default-cost 3
    #  area 0.0.0.4 shortcut default
    #  area 0.0.0.5 stub
    #  area 0.0.0.5 default-cost 5
    #  area 0.0.0.3 virtual-link 34.7.35.1
    #  area 0.0.0.3 virtual-link 34.7.35.1 authentication
    #  area 0.0.0.3 virtual-link 34.7.35.1 authentication-key U2FsdGVkX18zN46d3pzk+t7TofEHAZGY+5RvgXMwDiQ= encrypted
    #  area 0.0.0.3 virtual-link 34.7.35.1 hello-interval 30
    #  area 0.0.0.3 virtual-link 34.7.35.1 transmit-delay 50
    #  area 0.0.0.3 virtual-link 34.7.35.2
    #  area 0.0.0.3 virtual-link 34.7.35.2 authentication message-digest
    #  area 0.0.0.3 virtual-link 34.7.35.2 authentication-key U2FsdGVkX18zN46d3pzk+t7TofEHAZGY+5RvgXMwDiQ= encrypted
    #  area 0.0.0.3 virtual-link 34.7.35.2 dead-interval 10
    #  area 0.0.0.3 virtual-link 34.7.35.2 retransmit-interval 40
    #  area 0.0.0.3 virtual-link 34.7.35.2 transmit-delay 50
    #  area 0.0.0.3 virtual-link 34.7.35.2 message-digest-key 1 md5 U2FsdGVkX18mUZjlJL/Q/7vYtx2UyDc+NcLKc/BOJUA= encrypted
    #  area 0.0.0.3 virtual-link 34.7.35.2 message-digest-key 3 md5 U2FsdGVkX19SlRpqsnpeRmjq7WmtctYtveHlYF0Faqo= encrypted
    #  area 0.0.0.1 range 1.1.1.1/24 advertise cost 13
    #  area 0.0.0.1 range 1.1.1.1/24 substitute 11.2.5.1/24
    #  area 0.0.0.1 range 1.1.1.2/24 advertise cost 4
    #  area 0.0.0.1 range 1.1.1.3/24 advertise
    #  area 0.0.0.1 range 1.1.1.3/24 substitute 2.2.2.2/24
    #  area 0.0.0.1 range 1.1.1.4/24 advertise cost 34
    #  area 0.0.0.1 range 1.1.1.4/24 substitute 3.3.3.3/24
    #  network 1.1.1.1/24 area 0.0.0.2
    #  network 23.235.75.1/23 area 0.0.0.2
    #  network 3.5.1.5/23 area 0.0.0.2
    # !
    # router ospf vrf Vrf2
    # !

    # example:
    - name: "replace areas"
      sonic_ospf_area:
        state: replaced
        config:
          - area_id: 0.0.0.1
            vrf_name: Vrf1
            authentication_type: message_digest
            networks:
              - 1.1.1.1/24
              - 3.5.1.5/23
              - 23.235.75.1/23
            default_cost: 5
            stub:
              enabled: true
              no_summary: false
          - area_id: 0.0.0.2
            vrf_name: Vrf1
            filter_list_in: pf1
            filter_list_out: pf2
            shortcut: default
            default_cost: 3
            stub:
              enabled: true
              no_summary: true
            authentication_type: message_digest
            networks:
              - 1.1.1.1/24
              - 3.5.1.5/23
              - 23.235.75.1/23
          - area_id: 3
            vrf_name: Vrf1
            virtual_links:
              - router_id: 34.7.35.1
                enabled: true
                transmit_delay: 50
                hello_interval: 30
                authentication:
                  auth_type: text
                  key: "U2FsdGVkX18zN46d3pzk+t7TofEHAZGY+5RvgXMwDiQ="
                  key_encrypted: true
            ranges:
              - prefix: 1.1.1.1/24
                advertise: true
                substitute: 11.2.5.1/24
              - prefix: 1.1.1.2/24
                advertise: true
                cost: 4
              - prefix: 1.1.1.3/24
                advertise: true
                substitute: 2.5.3.78/24
          - area_id: 4
            vrf_name: Vrf1
            shortcut: default
            virtual_links:
              - router_id: 34.7.35.1
                enabled: true
                transmit_delay: 50
                hello_interval: 30
                authentication:
                  auth_type: text
                  key: "U2FsdGVkX18zN46d3pzk+t7TofEHAZGY+5RvgXMwDiQ="
                  key_encrypted: true
              - router_id: 34.7.35.2
                transmit_delay: 50
                enabled: true
                dead_interval: 10
                retransmit_interval: 40
                message_digest_list:
                  - key_id: 1
                    key: "U2FsdGVkX18mUZjlJL/Q/7vYtx2AUyDc+NcLKc/BOJUA="
                    key_encrypted: true
                  - key_id: 3
                    key: "U2FsdGVkX19SlRpqsnpeRmjq7WmtctYtveHlYF0Faqo="
                    key_encrypted: true
                authentication:
                  auth_type: message_digest
                  key: "U2FsdGVkX18zN46d3pzk+t7TofEHAZGY+5RvgXMwDiQ="
                  key_encrypted: true

    # After state

    # sonic# show running-configuration ospf
    # router ospf vrf Vrf1
    #  area 0.0.0.1 authentication message-digest
    #  area 0.0.0.1 stub
    #  area 0.0.0.1 default-cost 5
    #  area 0.0.0.2 authentication message-digest
    #  area 0.0.0.2 stub no-summary
    #  area 0.0.0.2 default-cost 3
    #  area 0.0.0.2 filter-list prefix pf1 in
    #  area 0.0.0.2 filter-list prefix pf2 out
    #  area 0.0.0.2 shortcut default
    #  area 0.0.0.3
    #  area 0.0.0.4 shortcut default
    #  area 0.0.0.5 stub
    #  area 0.0.0.5 default-cost 5
    #  area 0.0.0.3 virtual-link 34.7.35.1
    #  area 0.0.0.3 virtual-link 34.7.35.1 authentication
    #  area 0.0.0.3 virtual-link 34.7.35.1 authentication-key U2FsdGVkX18zN46d3pzk+t7TofEHAZGY+5RvgXMwDiQ= encrypted
    #  area 0.0.0.3 virtual-link 34.7.35.1 hello-interval 30
    #  area 0.0.0.3 virtual-link 34.7.35.1 transmit-delay 50
    #  area 0.0.0.4 virtual-link 34.7.35.1
    #  area 0.0.0.4 virtual-link 34.7.35.1 authentication
    #  area 0.0.0.4 virtual-link 34.7.35.1 authentication-key U2FsdGVkX18zN46d3pzk+t7TofEHAZGY+5RvgXMwDiQ= encrypted
    #  area 0.0.0.4 virtual-link 34.7.35.1 hello-interval 30
    #  area 0.0.0.4 virtual-link 34.7.35.1 transmit-delay 50
    #  area 0.0.0.4 virtual-link 34.7.35.2
    #  area 0.0.0.4 virtual-link 34.7.35.2 authentication message-digest
    #  area 0.0.0.4 virtual-link 34.7.35.2 authentication-key U2FsdGVkX18zN46d3pzk+t7TofEHAZGY+5RvgXMwDiQ= encrypted
    #  area 0.0.0.4 virtual-link 34.7.35.2 dead-interval 10
    #  area 0.0.0.4 virtual-link 34.7.35.2 retransmit-interval 40
    #  area 0.0.0.4 virtual-link 34.7.35.2 transmit-delay 50
    #  area 0.0.0.4 virtual-link 34.7.35.2 message-digest-key 1 md5 U2FsdGVkX18mUZjlJL/Q/7vYtx2UyDc+NcLKc/BOJUA= encrypted
    #  area 0.0.0.4 virtual-link 34.7.35.2 message-digest-key 3 md5 U2FsdGVkX19SlRpqsnpeRmjq7WmtctYtveHlYF0Faqo= encrypted
    #  area 0.0.0.3 range 1.1.1.1/24 advertise
    #  area 0.0.0.3 range 1.1.1.1/24 substitute 11.2.5.1/24
    #  area 0.0.0.3 range 1.1.1.2/24 advertise cost 4
    #  area 0.0.0.3 range 1.1.1.3/24 advertise
    #  area 0.0.0.3 range 1.1.1.3/24 substitute 2.5.3.78/24
    #  network 1.1.1.1/24 area 0.0.0.1
    #  network 23.235.75.1/23 area 0.0.0.1
    #  network 3.5.1.5/23 area 0.0.0.1
    #  network 1.1.1.1/24 area 0.0.0.2
    #  network 23.235.75.1/23 area 0.0.0.2
    #  network 3.5.1.5/23 area 0.0.0.2
    # !
    # router ospf vrf Vrf2
    # !
    # ----------

    # ============ OVERRIDDEN ==================

    # Scenario: override listed areas

    # Before state:

    # sonic# show running-configuration ospf
    # router ospf vrf Vrf1
    #  area 0.0.0.1 filter-list prefix pf1 in
    #  area 0.0.0.1 filter-list prefix pf2 out
    #  area 0.0.0.2 authentication message-digest
    #  area 0.0.0.3
    #  area 0.0.0.4 stub no-summary
    #  area 0.0.0.4 default-cost 3
    #  area 0.0.0.4 shortcut default
    #  area 0.0.0.5 stub
    #  area 0.0.0.5 default-cost 5
    #  area 0.0.0.3 virtual-link 34.7.35.1
    #  area 0.0.0.3 virtual-link 34.7.35.1 authentication
    #  area 0.0.0.3 virtual-link 34.7.35.1 authentication-key U2FsdGVkX18zN46d3pzk+t7TofEHAZGY+5RvgXMwDiQ= encrypted
    #  area 0.0.0.3 virtual-link 34.7.35.1 hello-interval 30
    #  area 0.0.0.3 virtual-link 34.7.35.1 transmit-delay 50
    #  area 0.0.0.3 virtual-link 34.7.35.2
    #  area 0.0.0.3 virtual-link 34.7.35.2 authentication message-digest
    #  area 0.0.0.3 virtual-link 34.7.35.2 authentication-key U2FsdGVkX18zN46d3pzk+t7TofEHAZGY+5RvgXMwDiQ= encrypted
    #  area 0.0.0.3 virtual-link 34.7.35.2 dead-interval 10
    #  area 0.0.0.3 virtual-link 34.7.35.2 retransmit-interval 40
    #  area 0.0.0.3 virtual-link 34.7.35.2 transmit-delay 50
    #  area 0.0.0.3 virtual-link 34.7.35.2 message-digest-key 1 md5 U2FsdGVkX18mUZjlJL/Q/7vYtx2UyDc+NcLKc/BOJUA= encrypted
    #  area 0.0.0.3 virtual-link 34.7.35.2 message-digest-key 3 md5 U2FsdGVkX19SlRpqsnpeRmjq7WmtctYtveHlYF0Faqo= encrypted
    #  area 0.0.0.1 range 1.1.1.1/24 advertise cost 13
    #  area 0.0.0.1 range 1.1.1.1/24 substitute 11.2.5.1/24
    #  area 0.0.0.1 range 1.1.1.2/24 advertise cost 4
    #  area 0.0.0.1 range 1.1.1.3/24 advertise
    #  area 0.0.0.1 range 1.1.1.3/24 substitute 2.2.2.2/24
    #  area 0.0.0.1 range 1.1.1.4/24 advertise cost 34
    #  area 0.0.0.1 range 1.1.1.4/24 substitute 3.3.3.3/24
    #  network 1.1.1.1/24 area 0.0.0.2
    #  network 23.235.75.1/23 area 0.0.0.2
    #  network 3.5.1.5/23 area 0.0.0.2
    # !
    # router ospf vrf Vrf2
    # !

    # example:
    - name: "override areas"
      sonic_ospf_area:
        state: overridden
        config:
          - area_id: 0.0.0.1
            vrf_name: Vrf1
            authentication_type: message_digest
            networks:
              - 1.1.1.1/24
              - 3.5.1.5/23
              - 23.235.75.1/23
            default_cost: 5
            stub:
              enabled: true
              no_summary: false
          - area_id: 0.0.0.2
            vrf_name: Vrf1
            filter_list_in: pf1
            filter_list_out: pf2
            shortcut: default
            default_cost: 3
            stub:
              enabled: true
              no_summary: true
            authentication_type: message_digest
            networks:
              - 1.1.1.1/24
              - 3.5.1.5/23
              - 23.235.75.1/23
          - area_id: 3
            vrf_name: Vrf1
            virtual_links:
              - router_id: 34.7.35.1
                enabled: true
                transmit_delay: 50
                hello_interval: 30
                authentication:
                  auth_type: text
                  key: "U2FsdGVkX18zN46d3pzk+t7TofEHAZGY+5RvgXMwDiQ="
                  key_encrypted: true
            ranges:
              - prefix: 1.1.1.1/24
                advertise: true
                substitute: 11.2.5.1/24
              - prefix: 1.1.1.2/24
                advertise: true
                cost: 4
              - prefix: 1.1.1.3/24
                advertise: true
                substitute: 2.5.3.78/24
          - area_id: 4
            vrf_name: Vrf1
            shortcut: default
            virtual_links:
              - router_id: 34.7.35.1
                enabled: true
                transmit_delay: 50
                hello_interval: 30
                authentication:
                  auth_type: text
                  key: "U2FsdGVkX18zN46d3pzk+t7TofEHAZGY+5RvgXMwDiQ="
                  key_encrypted: true
              - router_id: 34.7.35.2
                transmit_delay: 50
                enabled: true
                dead_interval: 10
                retransmit_interval: 40
                message_digest_list:
                  - key_id: 1
                    key: "U2FsdGVkX18mUZjlJL/Q/7vYtx2UyDc+NcLKc/BOJUA="
                    key_encrypted: true
                  - key_id: 3
                    key: "U2FsdGVkX19SlRpqsnpeRmjq7WmtctYtveHlYF0Faqo="
                    key_encrypted: true
                authentication:
                  auth_type: message_digest
                  key: "U2FsdGVkX18zN46d3pzk+t7TofEHAZGY+5RvgXMwDiQ="
                  key_encrypted: true

    # After state

    # sonic# show running-configuration ospf
    # router ospf vrf Vrf1
    #  area 0.0.0.1 authentication message-digest
    #  area 0.0.0.1 stub
    #  area 0.0.0.1 default-cost 5
    #  area 0.0.0.2 authentication message-digest
    #  area 0.0.0.2 stub no-summary
    #  area 0.0.0.2 default-cost 3
    #  area 0.0.0.2 filter-list prefix pf1 in
    #  area 0.0.0.2 filter-list prefix pf2 out
    #  area 0.0.0.2 shortcut default
    #  area 0.0.0.3
    #  area 0.0.0.4 shortcut default
    #  area 0.0.0.3 virtual-link 34.7.35.1
    #  area 0.0.0.3 virtual-link 34.7.35.1 authentication
    #  area 0.0.0.3 virtual-link 34.7.35.1 authentication-key U2FsdGVkX18zN46d3pzk+t7TofEHAZGY+5RvgXMwDiQ= encrypted
    #  area 0.0.0.3 virtual-link 34.7.35.1 hello-interval 30
    #  area 0.0.0.3 virtual-link 34.7.35.1 transmit-delay 50
    #  area 0.0.0.4 virtual-link 34.7.35.1
    #  area 0.0.0.4 virtual-link 34.7.35.1 authentication
    #  area 0.0.0.4 virtual-link 34.7.35.1 authentication-key U2FsdGVkX18zN46d3pzk+t7TofEHAZGY+5RvgXMwDiQ= encrypted
    #  area 0.0.0.4 virtual-link 34.7.35.1 hello-interval 30
    #  area 0.0.0.4 virtual-link 34.7.35.1 transmit-delay 50
    #  area 0.0.0.4 virtual-link 34.7.35.2
    #  area 0.0.0.4 virtual-link 34.7.35.2 authentication message-digest
    #  area 0.0.0.4 virtual-link 34.7.35.2 authentication-key U2FsdGVkX18zN46d3pzk+t7TofEHAZGY+5RvgXMwDiQ= encrypted
    #  area 0.0.0.4 virtual-link 34.7.35.2 dead-interval 10
    #  area 0.0.0.4 virtual-link 34.7.35.2 retransmit-interval 40
    #  area 0.0.0.4 virtual-link 34.7.35.2 transmit-delay 50
    #  area 0.0.0.4 virtual-link 34.7.35.2 message-digest-key 1 md5 U2FsdGVkX18mUZjlJL/Q/7vYtx2UyDc+NcLKc/BOJUA= encrypted
    #  area 0.0.0.4 virtual-link 34.7.35.2 message-digest-key 3 md5 U2FsdGVkX19SlRpqsnpeRmjq7WmtctYtveHlYF0Faqo= encrypted
    #  area 0.0.0.3 range 1.1.1.1/24 advertise
    #  area 0.0.0.3 range 1.1.1.1/24 substitute 11.2.5.1/24
    #  area 0.0.0.3 range 1.1.1.2/24 advertise cost 4
    #  area 0.0.0.3 range 1.1.1.3/24 advertise
    #  area 0.0.0.3 range 1.1.1.3/24 substitute 2.5.3.78/24
    #  network 1.1.1.1/24 area 0.0.0.1
    #  network 23.235.75.1/23 area 0.0.0.1
    #  network 3.5.1.5/23 area 0.0.0.1
    #  network 1.1.1.1/24 area 0.0.0.2
    #  network 23.235.75.1/23 area 0.0.0.2
    #  network 3.5.1.5/23 area 0.0.0.2
    # !
    # router ospf vrf Vrf2
    # !
    # ----------



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
     as the parameters above.</div>
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
     as the parameters above.</div>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[{&#x27;config&#x27;: &#x27;...&#x27;, &#x27;state&#x27;: &#x27;...&#x27;}, {&#x27;config&#x27;: &#x27;...&#x27;, &#x27;state&#x27;: &#x27;...&#x27;}]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Xiao Han (@Xiao_Han2)
