.. _dellemc.enterprise_sonic.sonic_prefix_lists_module:


*******************************************
dellemc.enterprise_sonic.sonic_prefix_lists
*******************************************

**prefix list configuration handling for SONiC**


Version added: 2.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management for prefix list parameters on devices running SONiC.




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
                        <div>Specifies a list of prefix set configuration dictionaries</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>afi</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>ipv4</b>&nbsp;&larr;</div></li>
                                    <li>ipv6</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the Address Family for addresses in the prefix list entries</div>
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
                        <div>Name of a prefix set (a list of prefix entries)</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>prefixes</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A list of prefix entries</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>action</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>permit</li>
                                    <li>deny</li>
                        </ul>
                </td>
                <td>
                        <div>Action to be taken for addresses matching this prefix entry</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ge</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Minimum prefix length to be matched</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>le</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Maximum prefix length to be matched</div>
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
                        <div>IPv4 or IPv6 prefix in A.B.C.D/LEN or A:B::C:D/LEN format</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>sequence</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Precedence for this prefix entry (unique within the prefix list)</div>
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
                        <div>Specifies the type of configuration update to be performed on the device.</div>
                        <div>For &quot;merged&quot;, merge specified attributes with existing configured attributes.</div>
                        <div>For &quot;deleted&quot;, delete the specified attributes from existing configuration.</div>
                        <div>For &quot;replaced&quot;, replace the specified existing configuration with the provided configuration.</div>
                        <div>For &quot;overridden&quot;, override the existing configuration with the provided configuration.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - Supports ``check_mode``.
   - Supports D(diff_mode).



Examples
--------

.. code-block:: yaml

    # Using "merged" state to create initial configuration
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration ip prefix-list
    # sonic#
    # (No configuration present)
    #
    # -------------
    #
    - name: Merge initial prefix-list configuration
      dellemc.enterprise_sonic.sonic_prefix_lists:
        config:
          - name: pfx1
            afi: "ipv4"
            prefixes:
              - sequence: 10
                prefix: "1.2.3.4/24"
                action: "permit"
                ge: 26
                le: 30
        state: merged

    # After state:
    # ------------
    #
    # sonic# show running-configuration ip prefix-list
    # !
    # ip prefix-list pfx1 seq 10 permit 1.2.3.4/24 ge 26 le 30
    # ------------
    #
    # ***************************************************************
    # Using "merged" state to update and add configuration
    #
    # Before state:
    # ------------
    #
    # sonic# show running-configuration ip prefix-list
    # !
    # ip prefix-list pfx1 seq 10 permit 1.2.3.4/24 ge 26 le 30
    #
    # sonic# show running-configuration ipv6 prefix-list
    # sonic#
    # (no IPv6 prefix-list configuration present)
    #
    # ------------
    #
    - name: Merge additional prefix-list configuration
      dellemc.enterprise_sonic.sonic_prefix_lists:
        config:
          - name: pfx1
            afi: "ipv4"
            prefixes:
              - sequence: 20
                action: "deny"
                prefix: "1.2.3.12/26"
              - sequence: 30
                action: "permit"
                prefix: "7.8.9.0/24"
          - name: pfx6
            afi: "ipv6"
            prefixes:
              - sequence: 25
                action: "permit"
                prefix: "40::300/124"
        state: merged

    # After state:
    # ------------
    #
    # sonic# show running-configuration ip prefix-list
    # !
    # ip prefix-list pfx1 seq 10 permit 1.2.3.4/24 ge 26 le 30
    # ip prefix-list pfx1 seq 20 deny 1.2.3.12/26
    # ip prefix-list pfx1 seq 30 permit 7.8.9.0/24
    #
    # sonic# show running-configuration ipv6 prefix-list
    # !
    # ipv6 prefix-list pfx6 seq 25 permit 40::300/124
    #
    # ***************************************************************
    # Using "deleted" state to remove configuration
    #
    # Before state:
    # ------------
    #
    # sonic# show running-configuration ip prefix-list
    # !
    # ip prefix-list pfx1 seq 10 permit 1.2.3.4/24 ge 26 le 30
    # ip prefix-list pfx1 seq 20 deny 1.2.3.12/26
    # ip prefix-list pfx1 seq 30 permit 7.8.9.0/24
    #
    # sonic# show running-configuration ipv6 prefix-list
    # !
    # ipv6 prefix-list pfx6 seq 25 permit 40::300/124
    #
    # ------------
    #
    - name: Delete selected prefix-list configuration
      dellemc.enterprise_sonic.sonic_prefix_lists:
        config:
          - name: pfx1
            afi: "ipv4"
            prefixes:
              - sequence: 10
                prefix: "1.2.3.4/24"
                action: "permit"
                ge: 26
                le: 30
              - sequence: 20
                action: "deny"
                prefix: "1.2.3.12/26"
          - name: pfx6
            afi: "ipv6"
            prefixes:
              - sequence: 25
                action: "permit"
                prefix: "40::300/124"
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration ip prefix-list
    # !
    # ip prefix-list pfx1 seq 30 permit 7.8.9.0/24
    #
    # sonic# show running-configuration ipv6 prefix-list
    # sonic#
    # (no IPv6 prefix-list configuration present)
    #
    # ***************************************************************
    # Using "overriden" state to override configuration
    #
    # Before state:
    # ------------
    #
    # sonic# show running-configuration ip prefix-list
    # !
    # ip prefix-list pfx1 seq 10 permit 1.2.3.4/24 ge 26 le 30
    # ip prefix-list pfx3 seq 20 deny 1.2.3.12/26
    # ip prefix-list pfx4 seq 30 permit 7.8.9.0/24
    #
    # sonic# show running-configuration ipv6 prefix-list
    # !
    # ipv6 prefix-list pfx6 seq 25 permit 40::300/124
    #
    # ------------
    #
    - name: Override prefix-list configuration
      dellemc.enterprise_sonic.sonic_prefix_lists:
        config:
          - name: pfx2
            afi: "ipv4"
            prefixes:
              - sequence: 10
                prefix: "10.20.30.128/24"
                action: "deny"
                ge: 25
                le: 30
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show running-configuration ip prefix-list
    # !
    # ip prefix-list pfx2 seq 10 deny 10.20.30.128/24 ge 25 le 30
    #
    # sonic# show running-configuration ipv6 prefix-list
    # sonic#
    # (no IPv6 prefix-list configuration present)
    #
    # ***************************************************************
    # Using "replaced" state to replace configuration
    #
    # Before state:
    # ------------
    #
    # sonic# show running-configuration ip prefix-list
    # !
    # ip prefix-list pfx2 seq 10 deny 10.20.30.128/24 ge 25 le 30
    #
    # sonic# show running-configuration ipv6 prefix-list
    # sonic#
    # (no IPv6 prefix-list configuration present)
    #
    # ------------
    #
    - name: Replace prefix-list configuration
      dellemc.enterprise_sonic.sonic_prefix_lists:
        config:
          - name: pfx2
            afi: "ipv4"
            prefixes:
              - sequence: 10
                prefix: "10.20.30.128/24"
                action: "permit"
                ge: 25
                le: 30
          - name: pfx3
            afi: "ipv6"
            prefixes:
              - sequence: 20
                action: "deny"
                prefix: "60::70/124"
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show running-configuration ip prefix-list
    # !
    # ip prefix-list pfx2 seq 10 permit 10.20.30.128/24 ge 25 le 30
    #
    # sonic# show running-configuration ipv6 prefix-list
    # sonic#
    # !
    # ipv6 prefix-list pfx3 seq 20 deny 60::70/124
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
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>diff</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>when D(diff_mode)</td>
                <td>
                            <div>The difference between &#x27;before&#x27; and &#x27;after&#x27; (or &#x27;after_generated&#x27;).</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The difference shows several lines of context around the lines that differ.</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Kerry Meyer (@kerry-meyer)
