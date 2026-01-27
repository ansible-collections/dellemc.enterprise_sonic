.. _dellemc.enterprise_sonic.sonic_ip_neighbor_module:


******************************************
dellemc.enterprise_sonic.sonic_ip_neighbor
******************************************

**Manage IP neighbor global configuration on SONiC.**


Version added: 2.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of IP neighbor global for devices running SONiC.




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
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies IP neighbor global configurations.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ipv4_arp_timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IPv4 ARP timeout.</div>
                        <div>The range is from 60 to 14400.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ipv4_drop_neighbor_aging_time</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IPv4 drop neighbor aging time.</div>
                        <div>The range is from 60 to 14400.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ipv6_drop_neighbor_aging_time</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IPv6 drop neighbor aging time.</div>
                        <div>The range is from 60 to 14400.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ipv6_nd_cache_expiry</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IPv6 ND cache expiry.</div>
                        <div>The range is from 60 to 14400.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>num_local_neigh</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The number of reserved local neighbors.</div>
                        <div>The range is from 0 to 32000.</div>
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
                                    <li>replaced</li>
                                    <li>overridden</li>
                                    <li>deleted</li>
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

    #
    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration
    # !
    # ip arp timeout 180
    # ip drop-neighbor aging-time 300
    # ipv6 drop-neighbor aging-time 300
    # ip reserve local-neigh 0
    # ipv6 nd cache expire 180
    # !
    - name: Configure IP neighbor global
      sonic_ip_neighbor:
        config:
          ipv4_arp_timeout: 1200
          ipv4_drop_neighbor_aging_time: 600
          ipv6_drop_neighbor_aging_time: 600
          ipv6_nd_cache_expiry: 1200
          num_local_neigh: 1000
        state: merged

    # After state:
    # ------------
    #
    # sonic# show running-configuration
    # !
    # ip arp timeout 1200
    # ip drop-neighbor aging-time 600
    # ipv6 drop-neighbor aging-time 600
    # ip reserve local-neigh 1000
    # ipv6 nd cache expire 1200
    # !
    #
    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration
    # !
    # ip arp timeout 1200
    # ip drop-neighbor aging-time 600
    # ipv6 drop-neighbor aging-time 600
    # ip reserve local-neigh 1000
    # ipv6 nd cache expire 1200
    # !
    - name: Delete some IP neighbor configuration
      sonic_ip_neighbor:
        config:
          ipv4_arp_timeout: 0
          ipv4_drop_neighbor_aging_time: 0
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration
    # !
    # ip arp timeout 180
    # ip drop-neighbor aging-time 300
    # ipv6 drop-neighbor aging-time 600
    # ip reserve local-neigh 1000
    # ipv6 nd cache expire 1200
    # !
    #
    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration
    # !
    # ip arp timeout 1200
    # ip drop-neighbor aging-time 600
    # ipv6 drop-neighbor aging-time 600
    # ip reserve local-neigh 1000
    # ipv6 nd cache expire 1200
    # !
    - name: Delete all IP neighbor configuration
      sonic_ip_neighbor:
        config: {}
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration
    # !
    # ip arp timeout 180
    # ip drop-neighbor aging-time 300
    # ipv6 drop-neighbor aging-time 300
    # ip reserve local-neigh 0
    # ipv6 nd cache expire 180
    # !
    #
    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration
    # !
    # ip arp timeout 1200
    # ip drop-neighbor aging-time 600
    # ipv6 drop-neighbor aging-time 300
    # ip reserve local-neigh 0
    # ipv6 nd cache expire 180
    # !
    - name: Change some IP neighbor configuration
      sonic_ip_neighbor:
        config:
          ipv6_drop_neighbor_aging_time: 600
          ipv6_nd_cache_expiry: 1200
          num_local_neigh: 1000
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show running-configuration
    # !
    # ip arp timeout 1200
    # ip drop-neighbor aging-time 600
    # ipv6 drop-neighbor aging-time 600
    # ip reserve local-neigh 1000
    # ipv6 nd cache expire 1200
    # !
    #
    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show running-configuration
    # !
    # ip arp timeout 1200
    # ip drop-neighbor aging-time 600
    # ipv6 drop-neighbor aging-time 300
    # ip reserve local-neigh 0
    # ipv6 nd cache expire 180
    # !
    - name: Reset IP neighbor configuration, then configure some
      sonic_ip_neighbor:
        config:
          ipv6_drop_neighbor_aging_time: 600
          ipv6_nd_cache_expiry: 1200
          num_local_neigh: 1000
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show running-configuration
    # !
    # ip arp timeout 180
    # ip drop-neighbor aging-time 300
    # ipv6 drop-neighbor aging-time 600
    # ip reserve local-neigh 1000
    # ipv6 nd cache expire 1200
    # !
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
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- M. Zhang (@mingjunzhang2019)
