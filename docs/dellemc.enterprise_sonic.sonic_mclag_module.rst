.. _dellemc.enterprise_sonic.sonic_mclag_module:


************************************
dellemc.enterprise_sonic.sonic_mclag
************************************

**Manage multi chassis link aggregation groups domain (MCLAG) and its parameters**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Manage multi chassis link aggregation groups domain (MCLAG) and its parameters.




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
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Dict of mclag domain configurations.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>backup_keepalive_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.1.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>MCLAG backup keepalive session interval in secs. Supported interval range is 1-60.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>backup_keepalive_peer_address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.1.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>The IPV4 backup-keepalive-peer-ip to establish MCLAG backup keepalive session</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>backup_keepalive_session_vrf</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.1.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>MCLAG backup keepalive session VRF</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>backup_keepalive_source_address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.1.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>The IPV4 backup-keepalive-source-ip to establish MCLAG backup keepalive session</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>delay_restore</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>MCLAG delay restore time in secs.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>domain_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>ID of the mclag domain (MCLAG domain).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>gateway_mac</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Gateway MAC address for router ports over MCLAG.</div>
                        <div>Configured gateway MAC address can be modified only when <em>state=replaced</em> or <em>state=overridden</em>.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>keepalive</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>MCLAG session keepalive-interval in secs.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Holds portchannels dictionary for an MCLAG domain.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>portchannels</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Holds a list of portchannels for configuring as an MCLAG interface.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>lag</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Holds a PortChannel ID.</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>peer_address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The IPV4 peer-ip for corresponding MCLAG.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>peer_gateway</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Holds Vlan dictionary for MCLAG peer gateway.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vlans</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Holds a list of VLANs and VLAN ranges for which MCLAG peer gateway functionality is enabled.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vlan</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Holds a VLAN name or VLAN range.</div>
                        <div>Specify a single VLAN eg. Vlan10.</div>
                        <div>Specify a range of VLANs eg. Vlan10-20.</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>peer_link</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Peer-link for corresponding MCLAG.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>session_timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>MCLAG session timeout value in secs.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>session_vrf</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 2.5.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>MCLAG session VRF.</div>
                        <div>Session VRF value can be either mgmt or a non-default VRF.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>The IPV4 source-ip for corresponding MCLAG.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>system_mac</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>MAC address of MCLAG.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>unique_ip</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Holds Vlan dictionary for MCLAG unique IP.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vlans</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Holds a list of VLANs and VLAN ranges for which a separate IP address is enabled for Layer 3 protocol support over MCLAG.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vlan</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Holds a VLAN name or VLAN range.</div>
                        <div>Specify a single VLAN eg. Vlan10.</div>
                        <div>Specify a range of VLANs eg. Vlan10-20.</div>
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
                        <div>The state that the configuration should be left in.</div>
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
    # sonic# show mclag brief
    # MCLAG Not Configured

    - name: Merge provided configuration with device configuration
      dellemc.enterprise_sonic.sonic_mclag:
        config:
          domain_id: 1
          peer_address: 1.1.1.1
          source_address: 2.2.2.2
          peer_link: 'Portchannel1'
          session_vrf: 'mgmt'
          keepalive: 1
          session_timeout: 3
          delay_restore: 240
          system_mac: '00:00:00:11:11:11'
          gateway_mac: '00:00:00:12:12:12'
          unique_ip:
            vlans:
              - vlan: Vlan4
              - vlan: Vlan21-25
          peer_gateway:
            vlans:
              - vlan: Vlan4
              - vlan: Vlan21-25
          members:
            portchannels:
              - lag: PortChannel10
          backup_keepalive_source_address: 3.3.3.3
          backup_keepalive_peer_address: 4.4.4.4
          backup_keepalive_interval: 5
          backup_keepalive_session_vrf: mgmt
        state: merged

    # After state:
    # ------------
    #
    # sonic# show mclag brief
    #
    # Domain ID            : 1
    # Role                 : standby
    # Session Status       : down
    # Peer Link Status     : down
    # Source Address       : 2.2.2.2
    # Peer Address         : 1.1.1.1
    # Session Vrf          : mgmt
    # Peer Link            : PortChannel1
    # Keepalive Interval   : 1 secs
    # Session Timeout      : 3 secs
    # Delay Restore        : 240 secs
    # System Mac           : 20:04:0f:37:bd:c9
    # Mclag System Mac     : 00:00:00:11:11:11
    # Gateway Mac          : 00:00:00:12:12:12
    #
    # Backup Keepalive Session Information:
    # -----------------------------------
    # Session Vrf          : mgmt
    # Session Status       : down
    # Source Address       : 3.3.3.3
    # Peer Address         : 4.4.4.4
    # Keepalive Interval   : 5 secs
    # -----------------------------------
    #
    # Number of MLAG Interfaces:1
    # -----------------------------------------------------------
    #  MLAG Interface       Local/Remote Status
    # -----------------------------------------------------------
    # PortChannel10            down/down
    #
    # sonic# show mclag separate-ip-interfaces
    # Interface Name
    # ==============
    # Vlan4
    # Vlan21
    # Vlan22
    # Vlan23
    # Vlan24
    # Vlan25
    # ==============
    # Total count :    6
    # ==============
    # sonic#
    # sonic# show mclag peer-gateway-interfaces
    # Interface Name
    # ==============
    # Vlan4
    # Vlan21
    # Vlan22
    # Vlan23
    # Vlan24
    # Vlan25
    # ==============
    # Total count :    6
    # ==============
    # sonic#


    # Using "merged" state
    #
    # Before state:
    # ------------
    #
    # sonic# show mclag brief
    #
    # Domain ID            : 1
    # Role                 : standby
    # Session Status       : down
    # Peer Link Status     : down
    # Source Address       : 2.2.2.2
    # Peer Address         : 1.1.1.1
    # Session Vrf          : mgmt
    # Peer Link            : PortChannel1
    # Keepalive Interval   : 1 secs
    # Session Timeout      : 3 secs
    # Delay Restore        : 240 secs
    # System Mac           : 20:04:0f:37:bd:c9
    # Mclag System Mac     : 00:00:00:11:11:11
    # Gateway Mac          : 00:00:00:12:12:12
    #
    # Backup Keepalive Session Information:
    # -----------------------------------
    # Session Vrf          : mgmt
    # Session Status       : down
    # Source Address       : 3.3.3.3
    # Peer Address         : 4.4.4.4
    # Keepalive Interval   : 5 secs
    # -----------------------------------
    #
    # Number of MLAG Interfaces:1
    # -----------------------------------------------------------
    #  MLAG Interface       Local/Remote Status
    # -----------------------------------------------------------
    # PortChannel10            down/down
    #
    # sonic# show mclag separate-ip-interfaces
    # Interface Name
    # ==============
    # Vlan4
    # Vlan21
    # Vlan22
    # Vlan23
    # Vlan24
    # Vlan25
    # ==============
    # Total count :    6
    # ==============
    # sonic#
    # sonic# show mclag peer-gateway-interfaces
    # Interface Name
    # ==============
    # Vlan4
    # Vlan21
    # Vlan22
    # Vlan23
    # Vlan24
    # Vlan25
    # ==============
    # Total count :    6
    # ==============
    # sonic#

    - name: Merge device configuration with the provided configuration
      dellemc.enterprise_sonic.sonic_mclag:
        config:
          domain_id: 1
          source_address: 3.3.3.3
          keepalive: 10
          session_timeout: 30
          session_vrf: VrfRed
          delay_restore: 360
          unique_ip:
            vlans:
              - vlan: Vlan5
              - vlan: Vlan26-28
          peer_gateway:
            vlans:
              - vlan: Vlan5
              - vlan: Vlan26-28
          members:
            portchannels:
              - lag: PortChannel12
          backup_keepalive_source_address: 31.31.31.31
          backup_keepalive_peer_address: 44.44.44.44
          backup_keepalive_interval: 59
          backup_keepalive_session_vrf: VrfRed
        state: merged

    # After state:
    # ------------
    #
    # sonic# show mclag brief
    #
    # Domain ID            : 1
    # Role                 : standby
    # Session Status       : down
    # Peer Link Status     : down
    # Source Address       : 3.3.3.3
    # Peer Address         : 1.1.1.1
    # Session Vrf          : VrfRed
    # Peer Link            : PortChannel1
    # Keepalive Interval   : 10 secs
    # Session Timeout      : 30 secs
    # Delay Restore        : 360 secs
    # System Mac           : 20:04:0f:37:bd:c9
    # Mclag System Mac     : 00:00:00:11:11:11
    # Gateway Mac          : 00:00:00:12:12:12
    #
    # Backup Keepalive Session Information:
    # -----------------------------------
    # Session Vrf          : VrfRed
    # Session Status       : down
    # Source Address       : 31.31.31.31
    # Peer Address         : 44.44.44.44
    # Keepalive Interval   : 59 secs
    # -----------------------------------
    #
    # Number of MLAG Interfaces:2
    # -----------------------------------------------------------
    #  MLAG Interface       Local/Remote Status
    # -----------------------------------------------------------
    # PortChannel10            down/down
    # PortChannel12            down/down
    #
    # sonic# show mclag separate-ip-interfaces
    # Interface Name
    # ==============
    # Vlan4
    # Vlan5
    # Vlan21
    # Vlan22
    # Vlan23
    # Vlan24
    # Vlan25
    # Vlan26
    # Vlan27
    # Vlan28
    # ==============
    # Total count :   10
    # ==============
    # sonic# show mclag peer-gateway-interfaces
    # Interface Name
    # ==============
    # Vlan4
    # Vlan5
    # Vlan21
    # Vlan22
    # Vlan23
    # Vlan24
    # Vlan25
    # Vlan26
    # Vlan27
    # Vlan28
    # ==============
    # Total count :   10
    # ==============
    # sonic#


    # Using "deleted" state
    #
    # Before state:
    # ------------
    #
    # sonic# show mclag brief
    #
    # Domain ID            : 1
    # Role                 : standby
    # Session Status       : down
    # Peer Link Status     : down
    # Source Address       : 3.3.3.3
    # Peer Address         : 1.1.1.1
    # Session Vrf          : VrfRed
    # Peer Link            : PortChannel1
    # Keepalive Interval   : 10 secs
    # Session Timeout      : 30 secs
    # Delay Restore        : 360 secs
    # System Mac           : 20:04:0f:37:bd:c9
    # Mclag System Mac     : 00:00:00:11:11:11
    # Gateway Mac          : 00:00:00:12:12:12
    #
    # Backup Keepalive Session Information:
    # -----------------------------------
    # Session Vrf          : VrfRed
    # Session Status       : down
    # Source Address       : 31.31.31.31
    # Peer Address         : 44.44.44.44
    # Keepalive Interval   : 59 secs
    # -----------------------------------
    #
    # Number of MLAG Interfaces:1
    # -----------------------------------------------------------
    #  MLAG Interface       Local/Remote Status
    # -----------------------------------------------------------
    # PortChannel10            down/down
    #
    # sonic# show mclag separate-ip-interfaces
    # Interface Name
    # ==============
    # Vlan4
    # Vlan21
    # Vlan22
    # Vlan23
    # Vlan24
    # Vlan25
    # ==============
    # Total count :    6
    # ==============
    # sonic#
    # sonic# show mclag peer-gateway-interfaces
    # Interface Name
    # ==============
    # Vlan4
    # Vlan21
    # Vlan22
    # Vlan23
    # Vlan24
    # Vlan25
    # ==============
    # Total count :    6
    # ==============
    # sonic#

    - name: Delete device configuration based on the provided configuration
      dellemc.enterprise_sonic.sonic_mclag:
        config:
          domain_id: 1
          source_address: 3.3.3.3
          keepalive: 10
          session_vrf: VrfRed
          unique_ip:
            vlans:
              - vlan: Vlan22
              - vlan: Vlan24-25
          peer_gateway:
            vlans:
              - vlan: Vlan22
              - vlan: Vlan24-25
          members:
            portchannels:
              - lag: PortChannel10
          backup_keepalive_source_address: 31.31.31.31
          backup_keepalive_peer_address: 44.44.44.44
          backup_keepalive_interval: 59
          backup_keepalive_session_vrf: VrfRed
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show mclag brief
    #
    # Domain ID            : 1
    # Role                 : standby
    # Session Status       : down
    # Peer Link Status     : down
    # Source Address       :
    # Peer Address         : 1.1.1.1
    # Session Vrf          : default
    # Peer Link            : PortChannel1
    # Keepalive Interval   : 1 secs
    # Session Timeout      : 30 secs
    # Delay Restore        : 360 secs
    # System Mac           : 20:04:0f:37:bd:c9
    # Mclag System Mac     : 00:00:00:11:11:11
    # Gateway Mac          : 00:00:00:12:12:12
    #
    # Backup Keepalive Session Information:
    # -----------------------------------
    # Session Vrf          : default
    # Session Status       : down
    # Source Address       :
    # Peer Address         :
    # Keepalive Interval   : 30 secs
    # -----------------------------------
    #
    # Number of MLAG Interfaces:0
    #
    # sonic# show mclag separate-ip-interfaces
    # Interface Name
    # ==============
    # Vlan4
    # Vlan21
    # Vlan23
    # ==============
    # Total count :    3
    # ==============
    # sonic#
    # sonic# show mclag peer-gateway-interfaces
    # Interface Name
    # ==============
    # Vlan4
    # Vlan21
    # Vlan23
    # ==============
    # Total count :    3
    # ==============
    # sonic#


    # Using "deleted" state
    #
    # Before state:
    # ------------
    #
    # sonic# show mclag brief
    #
    # Domain ID            : 1
    # Role                 : standby
    # Session Status       : down
    # Peer Link Status     : down
    # Source Address       : 3.3.3.3
    # Peer Address         : 1.1.1.1
    # Session Vrf          : default
    # Peer Link            : PortChannel1
    # Keepalive Interval   : 10 secs
    # Session Timeout      : 30 secs
    # Delay Restore        : 360 secs
    # System Mac           : 20:04:0f:37:bd:c9
    # Mclag System Mac     : 00:00:00:11:11:11
    # Gateway Mac          : 00:00:00:12:12:12
    #
    # Backup Keepalive Session Information:
    # -----------------------------------
    # Session Vrf          : default
    # Session Status       : down
    # Source Address       :
    # Peer Address         :
    # Keepalive Interval   : 30 secs
    # -----------------------------------
    #
    # Number of MLAG Interfaces:1
    # -----------------------------------------------------------
    #  MLAG Interface       Local/Remote Status
    # -----------------------------------------------------------
    # PortChannel10            down/down
    #
    # sonic# show mclag separate-ip-interfaces
    # Interface Name
    # ==============
    # Vlan4
    # ==============
    # Total count :    1
    # ==============
    # sonic#
    # sonic# show mclag peer-gateway-interfaces
    # Interface Name
    # ==============
    # Vlan4
    # ==============
    # Total count :    1
    # ==============
    # sonic#

    - name: Delete all device configuration
      dellemc.enterprise_sonic.sonic_mclag:
        config:
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show mclag brief
    # MCLAG Not Configured
    # sonic# show mclag separate-ip-interfaces
    # MCLAG separate IP interface not configured
    # sonic# show mclag peer-gateway-interfaces
    # MCLAG Peer Gateway interface not configured
    # sonic#


    # Using "deleted" state
    #
    # Before state:
    # ------------
    #
    # sonic# show mclag brief
    #
    # Domain ID            : 1
    # Role                 : standby
    # Session Status       : down
    # Peer Link Status     : down
    # Source Address       : 3.3.3.3
    # Peer Address         : 1.1.1.1
    # Session Vrf          : default
    # Peer Link            : PortChannel1
    # Keepalive Interval   : 10 secs
    # Session Timeout      : 30 secs
    # Delay Restore        : 360 secs
    # System Mac           : 20:04:0f:37:bd:c9
    # Mclag System Mac     : 00:00:00:11:11:11
    # Gateway Mac          : 00:00:00:12:12:12
    #
    # Backup Keepalive Session Information:
    # -----------------------------------
    # Session Vrf          : VrfRed
    # Session Status       : down
    # Source Address       : 31.31.31.31
    # Peer Address         : 44.44.44.44
    # Keepalive Interval   : 59 secs
    # -----------------------------------
    #
    # Number of MLAG Interfaces:2
    # -----------------------------------------------------------
    #  MLAG Interface       Local/Remote Status
    # -----------------------------------------------------------
    # PortChannel10            down/down
    # PortChannel12            down/down
    #
    # sonic# show mclag separate-ip-interfaces
    # Interface Name
    # ==============
    # Vlan4
    # ==============
    # Total count :    1
    # ==============
    # sonic#
    # sonic# show mclag peer-gateway-interfaces
    # Interface Name
    # ==============
    # Vlan4
    # ==============
    # Total count :    1
    # ==============
    # sonic#

    - name: Delete device configuration based on the provided configuration
      dellemc.enterprise_sonic.sonic_mclag:
        config:
          domain_id: 1
          source_address: 3.3.3.3
          keepalive: 10
          peer_gateway:
            vlans:
          members:
            portchannels:
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show mclag brief
    #
    # Domain ID            : 1
    # Role                 : standby
    # Session Status       : down
    # Peer Link Status     : down
    # Source Address       :
    # Peer Address         : 1.1.1.1
    # Session Vrf          : default
    # Peer Link            : PortChannel1
    # Keepalive Interval   : 1 secs
    # Session Timeout      : 30 secs
    # Delay Restore        : 360 secs
    # System Mac           : 20:04:0f:37:bd:c9
    # Mclag System Mac     : 00:00:00:11:11:11
    # Gateway Mac          : 00:00:00:12:12:12
    #
    # Backup Keepalive Session Information:
    # -----------------------------------
    # Session Vrf          : VrfRed
    # Session Status       : down
    # Source Address       : 31.31.31.31
    # Peer Address         : 44.44.44.44
    # Keepalive Interval   : 59 secs
    # -----------------------------------
    #
    # Number of MLAG Interfaces:0
    #
    # sonic# show mclag separate-ip-interfaces
    # Interface Name
    # ==============
    # Vlan4
    # ==============
    # Total count :    1
    # ==============
    # sonic#
    # sonic# show mclag peer-gateway-interfaces
    # MCLAG Peer Gateway interface not configured
    # sonic#


    # Using "replaced" state
    #
    # Before state:
    # ------------
    #
    # sonic# show mclag brief
    #
    # Domain ID            : 1
    # Role                 : standby
    # Session Status       : down
    # Peer Link Status     : down
    # Source Address       : 2.2.2.2
    # Peer Address         : 1.1.1.1
    # Session Vrf          : VrfRed
    # Peer Link            : PortChannel1
    # Keepalive Interval   : 1 secs
    # Session Timeout      : 3 secs
    # Delay Restore        : 240 secs
    # System Mac           : 20:04:0f:37:bd:c9
    # Mclag System Mac     : 00:00:00:11:11:11
    # Gateway Mac          : 00:00:00:12:12:12
    #
    #
    # Backup Keepalive Session Information:
    # -----------------------------------
    # Session Vrf          : VrfRed
    # Session Status       : down
    # Source Address       : 31.31.31.31
    # Peer Address         : 44.44.44.44
    # Keepalive Interval   : 59 secs
    # -----------------------------------
    #
    # Number of MLAG Interfaces:2
    # -----------------------------------------------------------
    #  MLAG Interface       Local/Remote Status
    # -----------------------------------------------------------
    # PortChannel10            down/down
    # PortChannel11            down/down
    #
    # sonic# show mclag separate-ip-interfaces
    # Interface Name
    # ==============
    # Vlan4
    # Vlan21
    # Vlan22
    # Vlan23
    # Vlan24
    # Vlan25
    # ==============
    # Total count :    6
    # ==============
    # sonic#
    # sonic# show mclag peer-gateway-interfaces
    # Interface Name
    # ==============
    # Vlan4
    # Vlan21
    # Vlan22
    # Vlan23
    # Vlan24
    # Vlan25
    # ==============
    # Total count :    6
    # ==============
    # sonic#

    - name: Replace device configuration with the provided configuration
      dellemc.enterprise_sonic.sonic_mclag:
        config:
          domain_id: 1
          unique_ip:
            vlans:
              - vlan: Vlan5
              - vlan: Vlan24-28
          session_vrf: VrfBlue
          peer_gateway:
            vlans:
              - vlan: Vlan5
              - vlan: Vlan24-28
          members:
            portchannels:
              - lag: PortChannel10
              - lag: PortChannel12
          backup_keepalive_source_address: 131.131.131.131
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show mclag brief
    #
    # Domain ID            : 1
    # Role                 : standby
    # Session Status       : down
    # Peer Link Status     : down
    # Source Address       : 2.2.2.2
    # Peer Address         : 1.1.1.1
    # Session Vrf          : VrfBlue
    # Peer Link            : PortChannel1
    # Keepalive Interval   : 1 secs
    # Session Timeout      : 3 secs
    # Delay Restore        : 240 secs
    # System Mac           : 20:04:0f:37:bd:c9
    # Mclag System Mac     : 00:00:00:11:11:11
    # Gateway Mac          : 00:00:00:12:12:12
    #
    # Backup Keepalive Session Information:
    # -----------------------------------
    # Session Vrf          : Default
    # Session Status       : down
    # Source Address       : 131.131.131.131
    # Peer Address         :
    # Keepalive Interval   : 30 secs
    # -----------------------------------
    #
    # Number of MLAG Interfaces:2
    # -----------------------------------------------------------
    #  MLAG Interface       Local/Remote Status
    # -----------------------------------------------------------
    # PortChannel10            down/down
    # PortChannel12            down/down
    #
    # sonic# show mclag separate-ip-interfaces
    # Interface Name
    # ==============
    # Vlan5
    # Vlan24
    # Vlan25
    # Vlan26
    # Vlan27
    # Vlan28
    # ==============
    # Total count :   6
    # ==============
    # sonic# show mclag peer-gateway-interfaces
    # Interface Name
    # ==============
    # Vlan5
    # Vlan24
    # Vlan25
    # Vlan26
    # Vlan27
    # Vlan28
    # ==============
    # Total count :   6
    # ==============
    # sonic#


    # Using "overridden" state
    #
    # Before state:
    # ------------
    #
    # sonic# show mclag brief
    #
    # Domain ID            : 1
    # Role                 : standby
    # Session Status       : down
    # Peer Link Status     : down
    # Source Address       : 2.2.2.2
    # Peer Address         : 1.1.1.1
    # Session Vrf          : VrfBlue
    # Peer Link            : PortChannel1
    # Keepalive Interval   : 1 secs
    # Session Timeout      : 3 secs
    # Delay Restore        : 240 secs
    # System Mac           : 20:04:0f:37:bd:c9
    # Mclag System Mac     : 00:00:00:11:11:11
    # Gateway Mac          : 00:00:00:12:12:12
    #
    # Backup Keepalive Session Information:
    # -----------------------------------
    # Session Vrf          : Vrf_Red
    # Session Status       : down
    # Source Address       : 19.19.19.19
    # Peer Address         : 20.20.20.20
    # Keepalive Interval   : 3 secs
    # -----------------------------------
    #
    # Number of MLAG Interfaces:2
    # -----------------------------------------------------------
    #  MLAG Interface       Local/Remote Status
    # -----------------------------------------------------------
    # PortChannel10            down/down
    # PortChannel11            down/down
    #
    # sonic# show mclag separate-ip-interfaces
    # Interface Name
    # ==============
    # Vlan4
    # Vlan21
    # Vlan22
    # Vlan23
    # Vlan24
    # Vlan25
    # ==============
    # Total count :    6
    # ==============
    # sonic#
    # sonic# show mclag peer-gateway-interfaces
    # Interface Name
    # ==============
    # Vlan4
    # Vlan21
    # Vlan22
    # Vlan23
    # Vlan24
    # Vlan25
    # ==============
    # Total count :    6
    # ==============
    # sonic#

    - name: Override device configuration with the provided configuration
      dellemc.enterprise_sonic.sonic_mclag:
        config:
          domain_id: 1
          peer_address: 1.1.1.1
          source_address: 3.3.3.3
          peer_link: 'Portchannel1'
          session_vrf: VrfRed
          system_mac: '00:00:00:11:11:11'
          gateway_mac: '00:00:00:12:12:12'
          unique_ip:
            vlans:
              - vlan: Vlan24-28
          peer_gateway:
            vlans:
              - vlan: Vlan24-28
          members:
            portchannels:
              - lag: PortChannel10
              - lag: PortChannel12
          backup_keepalive_source_address: 131.131.131.131
          backup_keepalive_peer_address: 144.144.144.144
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show mclag brief
    #
    # Domain ID            : 1
    # Role                 : standby
    # Session Status       : down
    # Peer Link Status     : down
    # Source Address       : 3.3.3.3
    # Peer Address         : 1.1.1.1
    # Session Vrf          : VrfRed
    # Peer Link            : PortChannel1
    # Keepalive Interval   : 1 secs
    # Session Timeout      : 30 secs
    # Delay Restore        : 300 secs
    # System Mac           : 20:04:0f:37:bd:c9
    # Mclag System Mac     : 00:00:00:11:11:11
    # Gateway Mac          : 00:00:00:12:12:12
    #
    # Backup Keepalive Session Information:
    # -----------------------------------
    # Session Vrf          : Default
    # Session Status       : down
    # Source Address       : 131.131.131.131
    # Peer Address         : 141.141.141.141
    # Keepalive Interval   : 30 secs
    # -----------------------------------
    #
    #
    # Number of MLAG Interfaces:2
    # -----------------------------------------------------------
    #  MLAG Interface       Local/Remote Status
    # -----------------------------------------------------------
    # PortChannel10            down/down
    # PortChannel12            down/down
    #
    # sonic# show mclag separate-ip-interfaces
    # Interface Name
    # ==============
    # Vlan24
    # Vlan25
    # Vlan26
    # Vlan27
    # Vlan28
    # ==============
    # Total count :   5
    # ==============
    # sonic# show mclag peer-gateway-interfaces
    # Interface Name
    # ==============
    # Vlan24
    # Vlan25
    # Vlan26
    # Vlan27
    # Vlan28
    # ==============
    # Total count :   5
    # ==============
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
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>when changed</td>
                <td>
                            <div>The resulting configuration module invocation.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned always in the same format as the parameters above.</div>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned always in the same format as the parameters above.</div>
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

- Abirami N (@abirami-n)
