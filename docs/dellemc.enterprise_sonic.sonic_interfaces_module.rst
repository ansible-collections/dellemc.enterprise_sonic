.. _dellemc.enterprise_sonic.sonic_interfaces_module:


*****************************************
dellemc.enterprise_sonic.sonic_interfaces
*****************************************

**Configure Interface attributes on interfaces such as, Eth, LAG, VLAN, and loopback. (create a loopback interface if it does not exist.)**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Configure Interface attributes such as, MTU, admin statu, and so on, on interfaces such as, Eth, LAG, VLAN, and loopback. (create a loopback interface if it does not exist.)




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
                        <div>A list of interface configurations.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>advertised_speed</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Advertised speeds of the interface.</div>
                        <div>Applicable only for Ethernet interfaces.</div>
                        <div>Supported speeds are dependent on the type of switch.</div>
                        <div>Speeds may be 10, 100, 1000, 2500, 5000, 10000, 20000, 25000, 40000, 50000, 100000, 400000 or 800000.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>auto_negotiate</b>
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
                        <div>auto-negotiate transmission parameters with peer interface.</div>
                        <div>Applicable only for Ethernet interfaces.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>autoneg_mode</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 4.0.0</div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>AUTONEG_MODE_BAM</li>
                                    <li>AUTONEG_MODE_MSA</li>
                        </ul>
                </td>
                <td>
                        <div>BAM/MSA configuration for autonegotiation</div>
                        <div>Applicable only for Ethernet interfaces.</div>
                        <div>auto_negotiate should be set to true to configure autoneg_mode</div>
                        <div>with auto_negotiate set to true , autoneg_mode defaults to BAM</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Description about the interface.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
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
                        <div>Administrative state of the interface.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>fec</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>FEC_RS</li>
                                    <li>FEC_FC</li>
                                    <li>FEC_DISABLED</li>
                                    <li>FEC_DEFAULT</li>
                                    <li>FEC_AUTO</li>
                        </ul>
                </td>
                <td>
                        <div>Interface FEC (Forward Error Correction).</div>
                        <div>Applicable only for Ethernet interfaces.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
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
                        <div>MTU of the interface.</div>
                        <div>Not applicable for Loopback interfaces.</div>
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
                        <div>The name of the interface, for example, &#x27;Eth1/15&#x27;.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>speed</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>SPEED_10MB</li>
                                    <li>SPEED_100MB</li>
                                    <li>SPEED_1GB</li>
                                    <li>SPEED_2500MB</li>
                                    <li>SPEED_5GB</li>
                                    <li>SPEED_10GB</li>
                                    <li>SPEED_20GB</li>
                                    <li>SPEED_25GB</li>
                                    <li>SPEED_40GB</li>
                                    <li>SPEED_50GB</li>
                                    <li>SPEED_100GB</li>
                                    <li>SPEED_200GB</li>
                                    <li>SPEED_400GB</li>
                                    <li>SPEED_800GB</li>
                        </ul>
                </td>
                <td>
                        <div>Interface speed.</div>
                        <div>Applicable only for Ethernet interfaces.</div>
                        <div>Supported speeds are dependent on the type of switch.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>unreliable_los</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>UNRELIABLE_LOS_MODE_ON</li>
                                    <li>UNRELIABLE_LOS_MODE_OFF</li>
                                    <li>UNRELIABLE_LOS_MODE_AUTO</li>
                        </ul>
                </td>
                <td>
                        <div>Monitoring type to be used for generating a loss of service alarm.</div>
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
                        <div>The state the configuration should be left in.</div>
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
    #
    # Before state:
    # -------------
    #
    # show interface status | no-more
    # ------------------------------------------------------------------------------------------
    # Name                Description         Admin     Oper      AutoNeg     Speed        MTU
    # ------------------------------------------------------------------------------------------
    # Ethernet0           -                   up                              100000       9100
    # Ethernet4           -                   up                              100000       9100
    # Ethernet8           Ethernet-8          down                            100000       9100
    # Ethernet12          Ethernet-12         down                on          -            5000
    # Ethernet16          -                   down                            40000        9100
    #
    # show running-configuration interface Ethernet 8
    # !
    # interface Ethernet8
    #  mtu 9100
    #  speed 100000
    #  fec AUTO
    #  shutdown
    #
    - name: Configure interfaces
      sonic_interfaces:
        config:
          - name: Ethernet8
          - name: Ethernet12
          - name: Ethernet16
        state: deleted
    #
    # After state:
    # -------------
    #
    # show interface status | no-more
    # ------------------------------------------------------------------------------------------
    # Name                Description         Admin     Oper      AutoNeg     Speed        MTU
    # ------------------------------------------------------------------------------------------
    # Ethernet0           -                   up                              100000       9100
    # Ethernet4           -                   up                              100000       9100
    # Ethernet8           -                   up                              100000       9100
    # Ethernet12          -                   up                              100000       9100
    # Ethernet16          -                   up                              100000       9100
    #
    # show running-configuration interface Ethernet 8
    # !
    # interface Ethernet8
    #  mtu 9100
    #  speed 100000
    #  shutdown
    #
    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # show interface status | no-more
    # ------------------------------------------------------------------------------------------
    # Name                Description         Admin     Oper      AutoNeg     Speed        MTU
    # ------------------------------------------------------------------------------------------
    # Ethernet0           -                   up                              100000       9100
    # Ethernet4           -                   up                              100000       9100
    # Ethernet8           -                   down                            100000       9100
    # Ethernet12          -                   down                            1000         9100
    # Ethernet16          -                   down                            100000       9100
    #
    - name: Configure interfaces
      sonic_interfaces:
        config:

        state: deleted
    #
    # After state:
    # -------------
    #
    # show interface status | no-more
    # ------------------------------------------------------------------------------------------
    # Name                Description         Admin     Oper      AutoNeg     Speed        MTU
    # ------------------------------------------------------------------------------------------
    # Ethernet0           -                   up                              100000       9100
    # Ethernet4           -                   up                              100000       9100
    # Ethernet8           -                   up                              100000       9100
    # Ethernet12          -                   up                              100000       9100
    # Ethernet16          -                   up                              100000       9100
    #
    #
    #
    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # show interface status | no-more
    # ------------------------------------------------------------------------------------------
    # Name                Description         Admin     Oper      AutoNeg     Speed        MTU
    # ------------------------------------------------------------------------------------------
    # Ethernet0           -                   up                              100000       9100
    # Ethernet4           -                   up                              100000       9100
    # Ethernet8           -                   down                            100000       9100
    # Ethernet12          -                   down                            100000       9100
    # Ethernet16          -                   down                            100000       9100
    #
    # show running-configuration interface Ethernet 8
    # !
    # interface Ethernet8
    #  mtu 9100
    #  speed 100000
    #  shutdown
    #
    - name: Configure interfaces
      sonic_interfaces:
        config:
          - name: Ethernet8
            fec: FEC_AUTO
          - name: Ethernet12
            description: 'Ethernet Twelve'
            auto_negotiate: true
          - name: Ethernet16
            description: 'Ethernet Sixteen'
            enabled: true
            mtu: 3500
            speed: SPEED_40GB
        state: merged
    #
    # After state:
    # ------------
    #
    # show interface status | no-more
    # ------------------------------------------------------------------------------------------
    # Name                Description         Admin     Oper      AutoNeg     Speed        MTU
    # ------------------------------------------------------------------------------------------
    # Ethernet0           -                   up                              100000       9100
    # Ethernet4           -                   up                              100000       9100
    # Ethernet8           -                   down                            100000       9100
    # Ethernet12          Ethernet Twelve     down                on          100000       9100
    # Ethernet16          Ethernet Sixteen    up                              40000        3500
    #
    # show running-configuration interface Ethernet 8
    # !
    # interface Ethernet8
    #  mtu 9100
    #  speed 100000
    #  fec AUTO
    #  shutdown
    #
    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # show interface status | no-more
    # ------------------------------------------------------------------------------------------
    # Name                Description         Admin     Oper      AutoNeg     Speed        MTU
    # ------------------------------------------------------------------------------------------
    # Ethernet0           E0                  up                              100000       9100
    # Ethernet4           E4                  up                              100000       9100
    # Ethernet8           E8                  down                            100000       9100
    # Ethernet12          -                   down                            1000         9100
    # Ethernet16          -                   down                            100000       9100
    #
    # show running-configuration interface Ethernet 8
    # !
    # interface Ethernet8
    #  mtu 9100
    #  speed 100000
    #  shutdown
    #
    - name: Configure interfaces
      sonic_interfaces:
        config:
          - name: Ethernet8
            fec: FEC_AUTO
          - name: Ethernet12
            description: 'Ethernet Twelve'
            mtu: 3500
            enabled: true
            auto_negotiate: true
          - name: Ethernet16
            description: 'Ethernet Sixteen'
            mtu: 3000
            enabled: false
            speed: SPEED_40GB
        state: overridden
    #
    # After state:
    # ------------
    #
    # show interface status | no-more
    # ------------------------------------------------------------------------------------------
    # Name                Description         Admin     Oper      AutoNeg     Speed        MTU
    # ------------------------------------------------------------------------------------------
    # Ethernet0           -                   down                            100000       9100
    # Ethernet4           -                   down                            100000       9100
    # Ethernet8           -                   down                            100000       9100
    # Ethernet12          Ethernet Twelve     up                  on          100000       3500
    # Ethernet16          Ethernet Sixteen    down                            40000        3000
    #
    # show running-configuration interface Ethernet 8
    # !
    # interface Ethernet8
    #  mtu 9100
    #  speed 100000
    #  fec AUTO
    #  no shutdown
    #
    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # show interface status | no-more
    # ------------------------------------------------------------------------------------------
    # Name                Description         Admin     Oper      AutoNeg     Speed        MTU
    # ------------------------------------------------------------------------------------------
    # Ethernet0           -                   up                              100000       9100
    # Ethernet4           -                   up                              100000       9100
    # Ethernet8           -                   down               on           100000       9100
    # Ethernet12          -                   down                            1000         9100
    # Ethernet16          -                   down                            100000       9100
    #
    # show running-configuration interface Ethernet 8
    # !
    # interface Ethernet8
    #  mtu 9100
    #  speed auto 40000
    #  shutdown
    #
    - name: Configure interfaces
      sonic_interfaces:
        config:
          - name: Ethernet8
            auto_negotiate: true
            advertised_speed:
              - "100000"
          - name: Ethernet12
            description: 'Ethernet Twelve'
            mtu: 3500
            enabled: true
            auto_negotiate: true
          - name: Ethernet16
            description: 'Ethernet Sixteen'
            mtu: 3000
            enabled: false
            speed: SPEED_40GB
        state: replaced
    #
    # After state:
    # ------------
    #
    # show interface status | no-more
    # ------------------------------------------------------------------------------------------
    # Name                Description         Admin     Oper      AutoNeg     Speed        MTU
    # ------------------------------------------------------------------------------------------
    # Ethernet0           -                   up                              100000       9100
    # Ethernet4           -                   up                              100000       9100
    # Ethernet8           -                   down                on          100000       9100
    # Ethernet12          Ethernet Twelve     up                  on          100000       3500
    # Ethernet16          Ethernet Sixteen    down                            40000        3000
    #
    # show running-configuration interface Ethernet 8
    # !
    # interface Ethernet8
    #  mtu 9100
    #  speed auto 100000
    #  fec AUTO
    #  shutdown
    #
    # Using "deleted" state for MSA/BAM config
    #
    # Before state:
    # -------------
    # show interface status
    # --------------------------------------------------------------------------------------------------------------------------------------
    # Name                Description                   Oper        Reason         AutoNeg   Speed          MTU            Alternate Name
    # --------------------------------------------------------------------------------------------------------------------------------------
    # Ethernet0           Ethernet0                     down        no-transceiver   off       800000         9100           Eth1/1
    # Ethernet8           Ethernet8                     down        no-transceiver   on        -              9100           Eth1/2
    # Ethernet16          -                             down        no-transceiver   off       800000         9100           Eth1/3
    #
    # show running-configuration interface Ethernet 8
    # !
    # interface Ethernet8
    #  description Ethernet8
    #  mtu 9100
    #  speed auto MSA
    #  fec RS
    #  unreliable-los auto
    #  no shutdown
    #
    - name: Configure interfaces
      sonic_interfaces:
        config:
          - name: Ethernet32
            autoneg_mode: AUTONEG_MODE_MSA
        state: deleted
    #
    # After State :
    # -------------
    # show interface status
    # --------------------------------------------------------------------------------------------------------------------------------------
    # Name                Description                   Oper        Reason         AutoNeg   Speed          MTU            Alternate Name
    # --------------------------------------------------------------------------------------------------------------------------------------
    # Ethernet0           Ethernet0                     down        no-transceiver   off       800000         9100           Eth1/1
    # Ethernet8           Ethernet8                     down        no-transceiver   on        -              9100           Eth1/2
    # Ethernet16          -                             down        no-transceiver   off       800000         9100           Eth1/3
    #
    # show running-configuration interface Ethernet 8
    # !
    # interface Ethernet8
    #  description Ethernet8
    #  mtu 9100
    #  speed auto
    #  fec RS
    #  unreliable-los auto
    #  no shutdown
    #
    # Using "merged" state for MSA/BAM config
    #
    # Before state:
    # -------------
    # show interface status
    # --------------------------------------------------------------------------------------------------------------------------------------
    # Name                Description                   Oper        Reason         AutoNeg   Speed          MTU            Alternate Name
    # --------------------------------------------------------------------------------------------------------------------------------------
    # Ethernet0           Ethernet0                     down        no-transceiver   off       800000         9100           Eth1/1
    # Ethernet8           Ethernet8                     down        no-transceiver   on        -              9100           Eth1/2
    # Ethernet16          -                             down        no-transceiver   off       800000         9100           Eth1/3
    #
    # show running-configuration interface Ethernet 8
    # !
    # interface Ethernet8
    #  description Ethernet8
    #  mtu 9100
    #  speed auto
    #  fec RS
    #  unreliable-los auto
    #  no shutdown
    #
    - name: Configure interfaces
      sonic_interfaces:
        config:
          - name: Ethernet32
            autoneg_mode: AUTONEG_MODE_MSA
        state: merged
    #
    # After state:
    # -------------
    #
    # show interface status
    # --------------------------------------------------------------------------------------------------------------------------------------
    # Name                Description                   Oper        Reason         AutoNeg   Speed          MTU            Alternate Name
    # --------------------------------------------------------------------------------------------------------------------------------------
    # Ethernet0           Ethernet0                     down        no-transceiver   off       800000         9100           Eth1/1
    # Ethernet8           Ethernet8                     down        no-transceiver   on        -              9100           Eth1/2
    # Ethernet16          -                             down        no-transceiver   off       800000         9100           Eth1/3
    #
    # show running-configuration interface Ethernet 8
    # !
    # interface Ethernet8
    #  description Ethernet8
    #  mtu 9100
    #  speed auto MSA
    #  fec RS
    #  unreliable-los auto
    #  no shutdown
    #
    # Using "replaced" state for MSA/BAM config
    #
    # Before state:
    # -------------
    #
    # show interface status
    # --------------------------------------------------------------------------------------------------------------------------------------
    # Name                Description                   Oper        Reason         AutoNeg   Speed          MTU            Alternate Name
    # --------------------------------------------------------------------------------------------------------------------------------------
    # Ethernet0           Ethernet0                     down        no-transceiver   off       800000         9100           Eth1/1
    # Ethernet8           Ethernet8                     down        admin-down       on        -              9100           Eth1/2
    # Ethernet16          -                             down        no-transceiver   off       800000         9100           Eth1/3
    #
    # show running-configuration interface Ethernet 8
    # !
    # interface Ethernet8
    #  description Ethernet8
    #  mtu 9100
    #  speed auto MSA
    #  fec RS
    #  unreliable-los auto
    #  shutdown
    #
    - name: configure interface
      sonic_interfaces:
        config:
          - name: Ethernet8
            description: 'Ethernet eight'
        state: replaced
    #
    # After state:
    # -------------
    #
    # show interface status
    # --------------------------------------------------------------------------------------------------------------------------------------
    # Name                Description                   Oper        Reason         AutoNeg   Speed          MTU            Alternate Name
    # --------------------------------------------------------------------------------------------------------------------------------------
    # Ethernet0           Ethernet0                     down        no-transceiver   off       800000         9100           Eth1/1
    # Ethernet8           Ethernet eight                down        admin-down       off       800000         9100           Eth1/2
    # Ethernet16          -                             down        no-transceiver   off       800000         9100           Eth1/3
    #
    # show running-configuration interface Ethernet 8
    # !
    # interface Ethernet8
    #  description "Ethernet eight"
    #  mtu 9100
    #  speed 800000
    #  fec RS
    #  unreliable-los auto
    #  shutdown
    #
    # Using "replaced" state for MSA/BAM config
    #
    # Before state:
    # -------------
    #
    # show interface status
    # --------------------------------------------------------------------------------------------------------------------------------------
    # Name                Description                   Oper        Reason         AutoNeg   Speed          MTU            Alternate Name
    # --------------------------------------------------------------------------------------------------------------------------------------
    # Ethernet0           Ethernet0                     down        no-transceiver   off       800000         9100           Eth1/1
    # Ethernet8           Ethernet8                     down        admin-down       off       800000         9100           Eth1/2
    #
    # show running-configuration interface Ethernet 8
    # !
    # interface Ethernet8
    #  description Ethernet8
    #  mtu 9100
    #  speed 800000
    #  fec AUTO
    #  unreliable-los auto
    #  shutdown
    #
    - name: configure interface
      sonic_interfaces:
        config:
          - name: Ethernet8
            auto_negotiate: true
            autoneg_mode: AUTONEG_MODE_MSA
        state: replaced
    #
    # After state:
    # -------------
    # show interface status
    # --------------------------------------------------------------------------------------------------------------------------------------
    # Name                Description                   Oper        Reason         AutoNeg   Speed          MTU            Alternate Name
    # --------------------------------------------------------------------------------------------------------------------------------------
    # Ethernet0           Ethernet0                     down        no-transceiver   off       800000         9100           Eth1/1
    # Ethernet8           -                             down        admin-down       on        -              9100           Eth1/2
    # Ethernet16          -                             down        no-transceiver   off       800000         9100           Eth1/3
    #
    # show running-configuration interface Ethernet 8
    # !
    # interface Ethernet8
    #  mtu 9100
    #  speed auto MSA
    #  fec RS
    #  unreliable-los auto
    #  shutdown
    #
    # Using "overridden" state for MSA/BAM config
    #
    # Before state:
    # -------------
    # show interface status
    # --------------------------------------------------------------------------------------------------------------------------------------
    # Name                Description                   Oper        Reason         AutoNeg   Speed          MTU            Alternate Name
    # --------------------------------------------------------------------------------------------------------------------------------------
    # Ethernet0           Ethernet0                     down        admin-down       on        -              5432           Eth1/1
    # Ethernet8           Ethernet8                     down        no-transceiver   on        -              4532           Eth1/2
    # Ethernet16          -                             down        admin-down       off       800000         9100           Eth1/3
    #
    # show running-configuration interface Ethernet 0
    # !
    # interface Ethernet0
    #  description Ethernet0
    #  mtu 5432
    #  speed auto MSA
    #  fec RS
    #  unreliable-los auto
    #  shutdown
    #
    # show running-configuration interface Ethernet 8
    # !
    # interface Ethernet8
    #  description Ethernet8
    #  mtu 4532
    #  speed auto MSA
    #  fec RS
    #  unreliable-los auto
    #  no shutdown
    #
    - name: configure interface
      dellemc.enterprise_sonic.sonic_interfaces:
        config:
          - name: Ethernet8
            description: 'Ethernet eight'
        state: overridden
    #
    # After state:
    # -------------
    # show interface status
    # --------------------------------------------------------------------------------------------------------------------------------------
    # Name                Description                   Oper        Reason         AutoNeg   Speed          MTU            Alternate Name
    # --------------------------------------------------------------------------------------------------------------------------------------
    # Ethernet0           -                             down        admin-down       off       800000         9100           Eth1/1
    # Ethernet8           Ethernet eight                down        admin-down       off       800000         9100           Eth1/2
    # Ethernet16          -                             down        admin-down       off       800000         9100           Eth1/3
    #
    # show running-configuration interface Ethernet 0
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 800000
    #  fec RS
    #  unreliable-los auto
    #  shutdown
    # show running-configuration interface Ethernet 8
    # !
    # interface Ethernet8
    #  description "Ethernet eight"
    #  mtu 9100
    #  speed 800000
    #  fec RS
    #  unreliable-los auto
    #  shutdown
    # sonic#
    #
    # Using "overridden" state for MSA/BAM config
    #
    # Before state:
    # -------------
    # show interface status
    # --------------------------------------------------------------------------------------------------------------------------------------
    # Name                Description                   Oper        Reason         AutoNeg   Speed          MTU            Alternate Name
    # --------------------------------------------------------------------------------------------------------------------------------------
    # Ethernet0           Ethernet0                     down        admin-down       off       400000         5432           Eth1/1
    # Ethernet8           Ethernet eight                down        no-transceiver   off       800000         4352           Eth1/2
    # Ethernet16          -                             down        admin-down       off       800000         9100           Eth1/3
    #
    # show running-configuration interface Ethernet 0
    # !
    # interface Ethernet0
    #  description Ethernet0
    #  mtu 5432
    #  speed 400000
    #  fec RS
    #  unreliable-los auto
    #  shutdown
    #
    # show running-configuration interface Ethernet 8
    # !
    # interface Ethernet8
    #  description "Ethernet eight"
    #  mtu 4352
    #  speed 800000
    #  fec RS
    #  unreliable-los auto
    #  no shutdown
    - name: configure interface
      sonic_interfaces:
        config:
          - name: Ethernet8
            auto_negotiate: true
            autoneg_mode: AUTONEG_MODE_MSA
        state: overridden
    #
    # After state:
    # -------------
    # show interface status
    # --------------------------------------------------------------------------------------------------------------------------------------
    # Name                Description                   Oper        Reason         AutoNeg   Speed          MTU            Alternate Name
    # --------------------------------------------------------------------------------------------------------------------------------------
    # Ethernet0           -                             down        admin-down       off       800000         9100           Eth1/1
    # Ethernet8           -                             down        admin-down       on        -              9100           Eth1/2
    # Ethernet16          -                             down        admin-down       off       800000         9100           Eth1/3
    #
    # show running-configuration interface Ethernet 0
    # !
    # interface Ethernet0
    #  mtu 9100
    #  speed 800000
    #  fec RS
    #  unreliable-los auto
    #  shutdown
    #
    # show running-configuration interface Ethernet 8
    # !
    # interface Ethernet8
    #  mtu 9100
    #  speed auto MSA
    #  fec RS
    #  unreliable-los auto
    #  shutdown



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

- Niraimadaiselvam M(@niraimadaiselvamm)
