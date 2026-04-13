.. _dellemc.enterprise_sonic.sonic_bgp_ext_communities_module:


**************************************************
dellemc.enterprise_sonic.sonic_bgp_ext_communities
**************************************************

**Manage BGP extended community-list and its parameters**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of BGP extcommunity-list for devices running Enterprise SONiC Distribution by Dell Technologies.




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
                        <div>A list of &#x27;bgp_extcommunity_list&#x27; configurations.</div>
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
                                    <li>all</li>
                                    <li><div style="color: blue"><b>any</b>&nbsp;&larr;</div></li>
                        </ul>
                </td>
                <td>
                        <div>Matches any/all of the the members.</div>
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
                        <div>Members of this BGP ext community list.</div>
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
                        <div>Members of this BGP ext community list. Regular expression string can be given here. Applicable for expanded ext BGP community type.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>route_origin</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Members of this BGP ext community list. The format of route_origin is in either 0..65535:0..65535 or A.B.C.D:[1..65535] format.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>route_target</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Members of this BGP ext community list. The format of route_target is in either 0..65535:0..65535 or A.B.C.D:[1..65535] format.</div>
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
                        <div>Name of the BGP ext communitylist.</div>
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
                        <div>Default value while adding a new ext-community-list is False.</div>
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
                                    <li><div style="color: blue"><b>standard</b>&nbsp;&larr;</div></li>
                                    <li>expanded</li>
                        </ul>
                </td>
                <td>
                        <div>Whether it is a standard or expanded ext community_list entry.</div>
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
    # show bgp ext-community-list
    # Standard extended community list test:  match: ANY
    #     permit rt:101:101
    #     permit rt:201:201

    - name: Deletes a BGP ext community member
      dellemc.enterprise_sonic.sonic_bgp_ext_communities:
        config:
          - name: test
            type: standard
            members:
              route_target:
                - 201:201
        state: deleted

    # After state:
    # ------------
    #
    # show bgp ext-community-list
    # Standard extended community list test:  match: ANY
    #     permit rt:101:101
    #


    # Using "deleted" state

    # Before state:
    # -------------
    #
    # show bgp ext-community-list
    # Standard extended community list test:  match: ANY
    #     permit rt:101:101
    #     permit rt:201:201
    # Expanded extended community list test1:   match: ALL
    #     deny 101:102

    - name: Deletes a single BGP extended community
      dellemc.enterprise_sonic.sonic_bgp_ext_communities:
        config:
          - name: test1
            members:
        state: deleted

    # After state:
    # ------------
    #
    # show bgp ext-community-list
    # Standard extended community list test:  match: ANY
    #     permit rt:101:101
    #     permit rt:201:201
    #


    # Using "deleted" state

    # Before state:
    # -------------
    #
    # show bgp ext-community-list
    # Standard extended community list test:  match: ANY
    #     permit rt:101:101
    #     permit rt:201:201
    # Expanded extended community list test1:   match: ALL
    #     deny 101:102

    - name: Deletes all BGP extended communities
      dellemc.enterprise_sonic.sonic_bgp_ext_communities:
        config:
        state: deleted

    # After state:
    # ------------
    #
    # show bgp ext-community-list
    #


    # Using "deleted" state

    # Before state:
    # -------------
    #
    # show bgp ext-community-list
    # Standard extended community list test:  match: ANY
    #     permit rt:101:101
    #     permit rt:201:201
    # Expanded extended community list test1:   match: ALL
    #     deny 101:102

    - name: Deletes all members in a single BGP extended community
      dellemc.enterprise_sonic.sonic_bgp_ext_communities:
        config:
          - name: test1
            members:
              regex:
        state: deleted

    # After state:
    # ------------
    #
    # show bgp ext-community-list
    # Standard extended community list test:  match: ANY
    #     permit rt:101:101
    #     permit rt:201:201
    #


    # Using "merged" state

    # Before state:
    # -------------
    #
    # show bgp ext-community-list
    # Standard extended community list test:  match: ANY
    #     permit rt:101:101
    #     permit rt:201:201
    # Expanded extended community list test1:   match: ALL
    #     deny 101:102

    - name: Adds new community list
      dellemc.enterprise_sonic.sonic_bgp_ext_communities:
        config:
          - name: test3
            type: standard
            match: any
            permit: true
            members:
              route_origin:
                - "301:301"
                - "401:401"
        state: merged

    # After state:
    # ------------
    #
    # show bgp ext-community-list
    # Standard extended community list test:  match: ANY
    #     permit rt:101:101
    #     permit rt:201:201
    # Expanded extended community list test1:   match: ALL
    #     deny 101:102
    # Standard extended community list test3:  match: ANY
    #     permit soo:301:301
    #     permit soo:401:401


    # Using "replaced" state

    # Before state:
    # -------------
    #
    # show bgp ext-community-list
    # Standard extended community list test:  match: ANY
    #     permit rt:101:101
    #     permit rt:201:201
    # Expanded extended community list test1:   match: ALL
    #     deny 101:102

    - name: Replacing a single BGP extended community
      dellemc.enterprise_sonic.sonic_bgp_ext_communities:
        config:
          - name: test
            type: expanded
            permit: true
            match: all
            members:
              regex:
                - 301:302
        state: replaced

    # After state:
    # ------------
    #
    # show bgp ext-community-list
    # Expanded extended community list test:  match: ALL
    #     permit 301:302
    # Expanded extended community list test1:   match: ALL
    #     deny 101:102
    #


    # Using "overridden" state

    # Before state:
    # -------------
    #
    # show bgp ext-community-list
    # Standard extended community list test:  match: ANY
    #     permit rt:101:101
    #     permit rt:201:201
    # Expanded extended community list test1:   match: ALL
    #     deny 101:102


    - name: Override the entire list of BGP extended community
      dellemc.enterprise_sonic.sonic_bgp_ext_communities:
        config:
          - name: test3
            type: expanded
            permit: true
            match: all
            members:
              regex:
                - 301:302
        state: overridden

    # After state:
    # ------------
    #
    # show bgp ext-community-list
    # Expanded extended community list test3:  match: ALL
    #     permit 301:302
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
