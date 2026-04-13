.. _dellemc.enterprise_sonic.sonic_bgp_as_paths_module:


*******************************************
dellemc.enterprise_sonic.sonic_bgp_as_paths
*******************************************

**Manage BGP autonomous system path (or as-path-list) and its parameters**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of BGP bgp_as_paths for devices running Enterprise SONiC Distribution by Dell Technologies.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="2">
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
                        <div>A list of &#x27;bgp_as_paths&#x27; configurations.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>members</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Members of this BGP as-path; regular expression string can be provided.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
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
                        <div>Name of as-path-list.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
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
                        <div>Permits or denies this as-path.</div>
                        <div>Default value while adding a new as-path-list is <code>False</code>.</div>
                </td>
            </tr>

            <tr>
                <td colspan="2">
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
    # show bgp as-path-access-list
    # AS path list test:
    #   action: permit
    #   members: 808.*,909.*

    - name: Delete BGP as path list
      dellemc.enterprise_sonic.sonic_bgp_as_paths:
        config:
          - name: test
            members:
              - 909.*
            permit: true
        state: deleted

    # After state:
    # ------------
    #
    # show bgp as-path-access-list
    # AS path list test:
    #   action: permit
    #   members: 808.*


    # Using "deleted" state

    # Before state:
    # -------------
    #
    # show bgp as-path-access-list
    # AS path list test:
    #   action: permit
    #   members: 808.*,909.*
    # AS path list test1:
    #   action: deny
    #   members: 608.*,709.*

    - name: Deletes BGP as-path list
      dellemc.enterprise_sonic.sonic_bgp_as_paths:
        config:
          - name: test
            members:
        state: deleted

    # After state:
    # ------------
    #
    # show bgp as-path-access-list
    # AS path list test1:
    #   action: deny
    #   members: 608.*,709.*


    # Using "deleted" state

    # Before state:
    # -------------
    #
    # show bgp as-path-access-list
    # AS path list test:
    #   action: permit
    #   members: 808.*,909.*

    - name: Deletes BGP as-path list
      dellemc.enterprise_sonic.sonic_bgp_as_paths:
        config:
        state: deleted

    # After state:
    # ------------
    #
    # show bgp as-path-access-list
    # (No bgp as-path-access-list configuration present)


    # Using "merged" state

    # Before state:
    # -------------
    #
    # show bgp as-path-access-list
    # (No bgp as-path-access-list configuration present)

    - name: Create a BGP as-path list
      dellemc.enterprise_sonic.sonic_bgp_as_paths:
        config:
          - name: test
            members:
              - 909.*
            permit: true
        state: merged

    # After state:
    # ------------
    #
    # show bgp as-path-access-list
    # AS path list test:
    #   action: permit
    #   members: 909.*


    # Using "replaced" state

    # Before state:
    # -------------
    #
    # show bgp as-path-access-list
    # AS path list test:
    #    action: permit
    #    members: 800.*,808.*
    # AS path list test1:
    #    action: deny
    #    members: 500.*

    - name: Replace device configuration of specified BGP as-path lists with provided configuration
      dellemc.enterprise_sonic.sonic_bgp_as_paths:
        config:
          - name: test
            members:
              - 900.*
              - 901.*
            permit: true
          - name: test1
          - name: test2
            members:
              - 100.*
            permit: true
        state: replaced

    # After state:
    # ------------
    #
    # show bgp as-path-access-list
    # AS path list test:
    #    action: permit
    #    members: 900.*,901.*
    # AS path list test2:
    #    action: permit
    #    members: 100.*


    # Using "overridden" state

    # Before state:
    # -------------
    #
    # show bgp as-path-access-list
    # AS path list test:
    #    action: permit
    #    members: 800.*,808.*
    # AS path list test1:
    #    action: deny
    #    members: 500.*

    - name: Override device configuration of all BGP as-path lists with provided configuration
      dellemc.enterprise_sonic.sonic_bgp_as_paths:
        config:
          - name: test
            members:
              - 900.*
              - 901.*
            permit: true
        state: overridden

    # After state:
    # ------------
    #
    # show bgp as-path-access-list
    # AS path list test:
    #    action: permit
    #    members: 900.*,901.*



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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned is always in the same format as the parameters above.</div>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned is always in the same format as the parameters above.</div>
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
