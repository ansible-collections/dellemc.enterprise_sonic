.. _dellemc.enterprise_sonic.sonic_ptp_default_ds_module:


*********************************************
dellemc.enterprise_sonic.sonic_ptp_default_ds
*********************************************

**Manage global PTP configurations on SONiC**


Version added: 3.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of global PTP parameters for devices running SONiC.
- The device should have timing chip support.




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
                        <div>Specifies global PTP clock configurations.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>announce_receipt_timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The number of announceIntervals that have to pass without receipt of an Announce message before the occurrence of the event ANNOUNCE_RECEIPT_TIMEOUT_EXPIRES.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>clock_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>BC</li>
                                    <li>E2E_TC</li>
                                    <li>P2P_TC</li>
                                    <li>disable</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the type of clock configured in the PTP domain.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>domain_number</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The domain number of the current syntonization domain.</div>
                        <div>The range is from 0 to 127.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>domain_profile</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ieee1588</li>
                                    <li>G.8275.1</li>
                                    <li>G.8275.2</li>
                        </ul>
                </td>
                <td>
                        <div>The method to be used when comparing data sets during the Best Master Clock Algorithm.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>log_announce_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The base-2 logarithm of the mean announceInterval (mean time interval between successive Announce messages).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>log_min_delay_req_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The base-2 logarithm of the minDelayReqInterval.</div>
                        <div>The minimum permitted mean time interval between successive Delay_Req messages.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>log_sync_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The base-2 logarithm of the mean SyncInterval for multicast messages.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>network_transport</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>L2</li>
                                    <li>UDPv4</li>
                                    <li>UDPv6</li>
                        </ul>
                </td>
                <td>
                        <div>The network transport used for communication.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>priority1</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The priority1 attribute of the local clock.</div>
                        <div>The range is from 0 to 255.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>priority2</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The priority2 attribute of the local clock.</div>
                        <div>The range is from 0 to 255.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>source_interface</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Source interface whose IP to use as source ip for PTP IPv4 and IPv6 multicast transport mode.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>two_step_flag</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The clockAccuracy indicates the expected accuracy of the clock.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>unicast_multicast</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>unicast</li>
                                    <li>multicast</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies whether the network transport uses unicast or multicast communication.</div>
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
                        <div><code>merged</code> - Merges provided PTP configuration with on-device configuration.</div>
                        <div><code>replaced</code> - Replaces on-device PTP configuration with provided configuration.</div>
                        <div><code>overridden</code> - Overrides all on-device PTP configurations with the provided configuration.</div>
                        <div><code>deleted</code> - Deletes on-device PTP configuration.</div>
                </td>
            </tr>
    </table>
    <br/>




Examples
--------

.. code-block:: yaml

    # Using deleted
    #
    # Before State:
    # -------------
    #
    # sonic# show running-configuration ptp
    # ptp network-transport l2 multicast
    # ptp domain 25
    # ptp domain-profile default
    # ptp priority1 101
    # ptp priority2 91
    # ptp log-announce-interval 1
    # ptp log-sync-interval -3
    # sonic#

    - name: Delete specified PTP configurations
      dellemc.enterprise_sonic.sonic_ptp:
        config:
          log-sync-interval: -3
          log-announce-interval: 1
          network-transport: 'L2'
          unicast-multicast: 'multicast'
          priority1: 101
          priority2: 91
          domain-number: 25
        state: deleted

    # After State:
    # ------------
    #
    # sonic# show running-configuration ptp
    # ptp domain-profile default
    # sonic#


    # Using deleted
    #
    # Before State:
    # -------------
    #
    # sonic# show running-configuration ptp
    # ptp mode boundary-clock
    # ptp network-transport ipv6 unicast
    # ptp domain 45
    # ptp domain-profile g8275.2
    # ptp announce-timeout 3
    # sonic#

    - name: Delete all PTP configurations
      dellemc.enterprise_sonic.sonic_ptp:
        config:
        state: deleted

    # After State:
    # ------------
    #
    # sonic# show running-configuration ptp
    # sonic#


    # Using merged
    #
    # Before State:
    # -------------
    #
    # sonic# show running-configuration ptp
    # ptp domain 35
    # ptp domain-profile default
    # ptp priority2 100
    # sonic#

    - name: Merge provided global PTP configurations
      dellemc.enterprise_sonic.sonic_ptp:
        config:
          domain-profile: 'G.8275.1'
          log-sync-interval: -4
          log-announce-interval: -3
          announce-receipt-timeout: 5
          log-min-delay-req-interval: -4
          clock-type: 'BC'
          network-transport: 'L2'
          unicast-multicast: 'multicast'
        state: merged

    # After State:
    # ------------
    #
    # sonic# show running-configuration ptp
    # ptp mode boundary-clock
    # ptp network-transport l2 multicast
    # ptp domain 35
    # ptp domain-profile g8275.1
    # ptp priority2 100
    # ptp log-announce-interval -3
    # ptp announce-timeout 5
    # ptp log-sync-interval -4
    # ptp log-min-delay-req-interval -4
    # sonic#


    # Using replaced
    #
    # Before State:
    # -------------
    #
    # sonic# show running-configuration ptp
    # ptp network-transport ipv4 unicast
    # ptp domain 44
    # ptp domain-profile default
    # ptp priority1 100
    # ptp priority2 90
    # ptp log-announce-interval -2
    # ptp log-sync-interval -4
    # sonic#

    - name: Replace global PTP configurations
      dellemc.enterprise_sonic.sonic_ptp:
        config:
          log-sync-interval: -3
          log-announce-interval: 1
          network-transport: 'L2'
          unicast-multicast: 'multicast'
          priority1: 101
          priority2: 91
          domain-number: 25
        state: replaced

    # After State:
    # ------------
    #
    # sonic# show running-configuration ptp
    # ptp network-transport l2 multicast
    # ptp domain 25
    # ptp domain-profile default
    # ptp priority1 101
    # ptp priority2 91
    # ptp log-announce-interval 1
    # ptp log-sync-interval -3
    # sonic#


    # Using overridden
    #
    # Before State:
    # -------------
    #
    # sonic# show running-configuration ptp
    # ptp mode boundary-clock
    # ptp network-transport l2 multicast
    # ptp domain 35
    # ptp domain-profile g8275.1
    # ptp priority2 100
    # ptp log-announce-interval -3
    # ptp announce-timeout 5
    # ptp log-sync-interval -4
    # ptp log-min-delay-req-interval -4
    # sonic#

    - name: Override device configuration of ptp with provided configuration
      dellemc.enterprise_sonic.sonic_ptp:
        config:
          domain-number: 44
          domain-profile: 'G.8275.2'
          network-transport: 'ipv4'
          unicast-multicast: 'unicast'
        state: overridden

    # After State:
    # ------------
    #
    # sonic# show running-configuration ptp
    # ptp network-transport ipv4 unicast
    # ptp domain 44
    # ptp domain-profile g8275.2
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
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>when changed</td>
                <td>
                            <div>The configuration resulting from module invocation.</div>
                    <br/>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>after_generated</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>when <code>check_mode</code></td>
                <td>
                            <div>The configuration that would be generated by module invocation in non-check mode.</div>
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
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The configuration prior to the model invocation.</div>
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
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Pranesh Raagav S (@PraneshRaagavS)
