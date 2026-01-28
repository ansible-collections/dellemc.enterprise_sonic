.. _dellemc.enterprise_sonic.sonic_bgp_communities_module:


**********************************************
dellemc.enterprise_sonic.sonic_bgp_communities
**********************************************

**Manage BGP community and its parameters**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of BGP bgp_communities for device running Enterprise SONiC Distribution by Dell Technologies.




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
                        <div>A list of &#x27;bgp_communities&#x27; configurations.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>local_as</b>
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
                        <div>Do not send outside local AS (well-known community); applicable for standard BGP community type.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>match</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ALL</li>
                                    <li>ANY</li>
                        </ul>
                </td>
                <td>
                        <div>Matches any/all of the members.</div>
                        <div>If unspecified, operational default value is <code>ANY</code>.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Members of this BGP community list.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>aann</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.0.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>Community number aa:nn format 0..65535:0..65535; applicable for standard BGP community type.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>regex</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Members of this BGP community list. Regular expression string can be given here. Applicable for expanded BGP community type.</div>
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
                        <div>Name of the BGP community-list.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>no_advertise</b>
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
                        <div>Do not advertise to any peer (well-known community); applicable for standard BGP community type.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>no_export</b>
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
                        <div>Do not export to next AS (well-known community); applicable for standard BGP community type.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>no_peer</b>
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
                        <div>Do not export to next AS (well-known community); applicable for standard BGP community type.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>permit</b>
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
                        <div>Permits or denies this community.</div>
                        <div>If unspecified, operational default value is <code>False</code>.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>standard</li>
                                    <li>expanded</li>
                        </ul>
                </td>
                <td>
                        <div>Whether it is a standard or expanded community-list entry.</div>
                        <div>If unspecified, operational default value is <code>standard</code>.</div>
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

    # Before state:
    # -------------
    #
    # show bgp community-list
    # Standard community list test:  match: ANY
    #     permit local-as
    #     permit no-peer
    # Expanded community list test1:   match: ANY
    #     deny 101
    #     deny 302

    - name: Delete a BGP community-list member
      dellemc.enterprise_sonic.sonic_bgp_communities:
        config:
          - name: test1
            type: expanded
            permit: false
            members:
              regex:
                - 302
        state: deleted

    # After state:
    # ------------
    #
    # show bgp community-list
    # Standard community list test:  match: ANY
    #     permit local-as
    #     permit no-peer
    # Expanded community list test1:   match: ANY
    #     deny 101


    # Using "deleted" state

    # Before state:
    # -------------
    #
    # show bgp community-list
    # Standard community list test:  match: ANY
    #     permit local-as
    #     permit no-peer
    # Expanded community list test1:   match: ANY
    #     deny 101
    #     deny 302

    - name: Delete a single BGP community-list
      dellemc.enterprise_sonic.sonic_bgp_communities:
        config:
          - name: test
            type: standard
        state: deleted

    # After state:
    # ------------
    #
    # show bgp community-list
    # Expanded community list test1:   match: ANY
    #     deny 101
    #     deny 302


    # Using "deleted" state

    # Before state:
    # -------------
    #
    # show bgp community-list
    # Standard community list test:  match: ANY
    #     permit local-as
    #     permit no-peer
    # Expanded community list test1:   match: ANY
    #     deny 101
    #     deny 302

    - name: Delete All BGP community-lists
      dellemc.enterprise_sonic.sonic_bgp_communities:
        config:
        state: deleted

    # After state:
    # ------------
    #
    # show bgp community-list
    #


    # Using "deleted" state

    # Before state:
    # -------------
    #
    # show bgp community-list
    # Standard community list test:  match: ANY
    #     permit local-as
    #     permit no-peer
    # Expanded community list test1:   match: ANY
    #     deny 101
    #     deny 302

    - name: Delete all members in a single BGP community-list
      dellemc.enterprise_sonic.sonic_bgp_communities:
        config:
          - name: test1
            type: expanded
            members:
              regex:
        state: deleted

    # After state:
    # ------------
    #
    # show bgp community-list
    # Standard community list test:  match: ANY
    #     permit local-as
    #     permit no-peer


    # Using "merged" state

    # Before state:
    # -------------
    #
    # show bgp community-list
    # Expanded community list test1:   match: ANY
    #     permit 101
    #     permit 302

    - name: Add new BGP community-lists
      dellemc.enterprise_sonic.sonic_bgp_communities:
        config:
          - name: test2
            type: expanded
            permit: true
            members:
              regex:
                - 909
          - name: test3
            type: standard
            permit: true
            no_peer: true
            members:
              aann:
                - 1000:10
        state: merged

    # After state:
    # ------------
    #
    # show bgp community-list
    # Expanded community list test1:   match: ANY
    #     permit 101
    #     permit 302
    # Expanded community list test2:   match: ANY
    #     permit 909
    # Standard community list test3:  match: ANY
    #     permit 1000:10
    #     permit no-peer


    # Using "replaced" state

    # Before state:
    # -------------
    #
    # show bgp community-list
    # Standard community list test:  match: ANY
    #     permit local-as
    #     permit no-peer
    # Expanded community list test1:   match: ANY
    #     deny 101
    #     deny 302

    - name: Replacing a single BGP community-list
      dellemc.enterprise_sonic.sonic_bgp_communities:
        config:
          - name: test
            type: expanded
            members:
              regex:
                - 301
          - name: test2
            type: standard
            members:
              aann:
                - 1000:10
                - 2000:20
          - name: test3
            type: standard
            no_advertise: true
            no_peer: true
            permit: false
            match: ALL
        state: replaced

    # After state:
    # ------------
    #
    # show bgp community-list
    # Expanded community list test:   match: ANY
    #     deny 301
    # Expanded community list test1:   match: ANY
    #     deny 101
    #     deny 302
    # Standard community list test2:  match: ANY
    #     deny 1000:10
    #     deny 2000:10
    # Standard community list test3:  match: ALL
    #     deny no-advertise
    #     deny no-peer


    # Using "overridden" state

    # Before state:
    # -------------
    #
    # show bgp community-list
    # Standard community list test:  match: ANY
    #     permit local-as
    #     permit no-peer
    # Expanded community list test1:   match: ANY
    #     deny 101
    #     deny 302

    - name: Override entire BGP community-lists
      dellemc.enterprise_sonic.sonic_bgp_communities:
        config:
          - name: test3
            type: expanded
            members:
              regex:
                - 301
        state: overridden

    # After state:
    # ------------
    #
    # show bgp community-list
    # Expanded community list test3:   match: ANY
    #     deny 301
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
                            <div>The resulting configuration module invocation.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration that is returned is always in the same format as the parameters above.</div>
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
                            <div>The set of commands that are pushed to the remote device.</div>
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
