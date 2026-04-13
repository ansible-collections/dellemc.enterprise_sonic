.. _dellemc.enterprise_sonic.sonic_system_module:


*************************************
dellemc.enterprise_sonic.sonic_system
*************************************

**Configure system parameters**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module is used for configuration management of global system parameters on devices running Enterprise SONiC.




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
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the system related configurations</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>adjust_txrx_clock_freq</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.1.0</div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Adjust TX/RX clock frequency to platform specific value.</div>
                        <div>Operational default value is <code>false</code>.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>anycast_address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies different types of anycast address that can be configured on the device</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ipv4</b>
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
                        <div>Enable or disable ipv4 anycast-address</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ipv6</b>
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
                        <div>Enable or disable ipv6 anycast-address</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mac_address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the mac anycast-address</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>audit_rules</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 2.5.0</div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>BASIC</li>
                                    <li>DETAIL</li>
                                    <li>CUSTOM</li>
                                    <li>NONE</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies audit rule profile type.</div>
                        <div>Can be used on SONiC release versions 4.4.0 and above.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>auto_breakout</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 2.5.0</div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ENABLE</li>
                                    <li>DISABLE</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies auto-breakout status in the device</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>banner</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 4.0.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>The set of banner attribute configurations</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>login</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Banner message to display before login.</div>
                        <div>Format is &#x27;c\r\n{banner text}\r\nc&#x27;, where &#x27;c&#x27; is a delimiting character</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>login_banner_disable</b>
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
                        <div>Disable login banner.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>motd</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Banner message to display after login.</div>
                        <div>Format is &#x27;c\r\n{banner text}\r\nc&#x27;, where &#x27;c&#x27; is a delimiting character</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>motd_banner_disable</b>
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
                        <div>Disable motd banner.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>concurrent_session_limit</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.1.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies limit on number of concurrent sessions</div>
                        <div>Range 1-12</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>hostname</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the hostname of the SONiC device</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interface_naming</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>standard</li>
                                    <li>standard_extended</li>
                                    <li>native</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the type of interface-naming in device</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>load_share_hash_algo</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 2.5.0</div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>CRC</li>
                                    <li>XOR</li>
                                    <li>CRC_32LO</li>
                                    <li>CRC_32HI</li>
                                    <li>CRC_CCITT</li>
                                    <li>CRC_XOR</li>
                                    <li>JENKINS_HASH_LO</li>
                                    <li>JENKINS_HASH_HI</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies different types of ECMP Load share hash algorithm</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>login_exec_timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 4.0.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>CLI session timeout value.</div>
                        <div>The range is from 0 to 3600</div>
                        <div>Default is 600</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>password_complexity</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The set of login password attribute configurations</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>min_length</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Minimum number of required alphanumeric characters</div>
                        <div>The range is from 6 to 32</div>
                        <div>Default is 8</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>min_lower_case</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Minimum number of lowercase characters required</div>
                        <div>The range is from 0 to 31</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>min_numerals</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Minimum number of numeric characters required</div>
                        <div>The range is from 0 to 31</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>min_spl_char</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Minimum number of special characters required</div>
                        <div>The range is from 0 to 31</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>min_upper_case</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Minimum number of uppercase characters required</div>
                        <div>The range is from 0 to 31</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>switching_mode</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.1.0</div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>CUT_THROUGH</li>
                                    <li>STORE_AND_FORWARD</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies switching mode in the device.</div>
                        <div>Operational default value is STORE_AND_FORWARD.</div>
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
                                    <li>replaced</li>
                                    <li>overridden</li>
                                    <li>deleted</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the operation to be performed on the system parameters configured on the device.</div>
                        <div>In case of merged, the input configuration will be merged with the existing system configuration on the device.</div>
                        <div>In case of deleted the existing system configuration will be removed from the device.</div>
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
    # !
    # SONIC(config)#do show running-configuration
    # !
    # banner login @
    # banner - Welcome to DELL SONiC
    # @
    # banner motd @
    # banner - Enjoy the DELL OS
    # @
    # banner motd disable
    # ip anycast-mac-address aa:bb:cc:dd:ee:ff
    # ip anycast-address enable
    # ipv6 anycast-address enable
    # interface-naming standard
    # ip load-share hash algorithm JENKINS_HASH_HI
    # login concurrent-session limit 4
    # system adjust-txrx-clock-freq
    # login password-attribute character-restriction lower 2

    - name: Delete System configuration
      dellemc.enterprise_sonic.sonic_system:
        config:
          hostname: SONIC
          interface_naming: standard
          anycast_address:
            ipv6: true
          load_share_hash_algo: JENKINS_HASH_HI
          concurrent_session_limit: 4
          adjust_txrx_clock_freq: true
          password_complexity:
            min_lower_case: 2
          banner:
            login: "@
    banner_login_message
    @"
            motd: "@
    banner_motd_message
    @"
        state: deleted

    # After state:
    # ------------
    # !
    # sonic(config)#do show running-configuration
    # !
    # ip anycast-mac-address aa:bb:cc:dd:ee:ff
    # ip anycast-address enable


    # Using "deleted" state
    #
    # Before state:
    # -------------
    # !
    # SONIC(config)#do show running-configuration
    # !
    # ip anycast-mac-address aa:bb:cc:dd:ee:ff
    # ip anycast-address enable
    # ipv6 anycast-address enable
    # interface-naming standard
    # ip load-share hash algorithm JENKINS_HASH_HI
    # login concurrent-session limit 4

    - name: Delete all system related configs in device configuration
      dellemc.enterprise_sonic.sonic_system:
        config:
        state: deleted

    # After state:
    # ------------
    # !
    # sonic(config)#do show running-configuration
    # !


    # Using "merged" state
    #
    # Before state:
    # -------------
    # !
    # sonic(config)#do show running-configuration
    # !

    - name: Merge provided configuration with device configuration
      dellemc.enterprise_sonic.sonic_system:
        config:
          hostname: SONIC
          interface_naming: standard
          anycast_address:
            ipv6: true
            ipv4: true
            mac_address: aa:bb:cc:dd:ee:ff
          load_share_hash_algo: JENKINS_HASH_HI
          concurrent_session_limit: 4
          adjust_txrx_clock_freq: true
          password_complexity:
            min_upper_case: 2
            min_spl_char: 2
          banner:
            login_banner_disable: true
            motd: "@
    motd_banner_message
    @"
        state: merged

    # After state:
    # ------------
    # !
    # SONIC(config)#do show running-configuration
    # !
    # banner motd @
    # motd_banner_message
    # @
    # banner login disable
    # hostname SONIC
    # ip anycast-mac-address aa:bb:cc:dd:ee:ff
    # ip anycast-address enable
    # ipv6 anycast-address enable
    # interface-naming standard
    # ip load-share hash algorithm JENKINS_HASH_HI
    # login concurrent-session limit 4
    # system adjust-txrx-clock-freq
    # login password-attribute character-restriction upper 2
    # login password-attribute character-restriction special-char 2

    # Using "replaced" state
    #
    # Before state:
    # -------------
    # !
    # sonic(config)#do show running-configuration
    # !
    # banner login @
    # banner_login_message
    # @
    # banner motd @
    # @
    # banner_motd_message
    # banner motd disable
    # ip anycast-mac-address aa:bb:cc:dd:ee:ff
    # ip anycast-address enable
    # ipv6 anycast-address enable
    # interface-naming standard
    # login concurrent-session limit 4
    # login password-attribute character-restriction upper 2
    # login password-attribute character-restriction special-char 2

    - name: Replace system configuration.
      sonic_system:
        config:
          hostname: SONIC
          anycast_address:
            ipv6: true
          concurrent_session_limit: 5
          password_complexity:
            min_lower_case: 2
          banner:
            login: "@
    login_banner_message
    @"
        state: replaced

    # After state:
    # ------------
    # !
    # SONIC(config)#do show running-configuration
    # !
    # banner login @
    # login_banner_message
    # @
    # hostname SONIC
    # ipv6 anycast-address enable
    # login concurrent-session limit 5
    # login password-attribute character-restriction lower 2

    # Using "replaced" state
    #
    # Before state:
    # -------------
    # !
    # sonic(config)#do show running-configuration
    # !
    # banner login @
    # login_banner_message
    # @
    # ip anycast-mac-address aa:bb:cc:dd:ee:ff
    # interface-naming standard
    # login concurrent-session limit 5
    # login password-attribute character-restriction lower 2

    - name: Replace system device configuration.
      sonic_system:
        config:
          hostname: sonic
          interface_naming: standard
          anycast_address:
            ipv6: true
            ipv4: true
          load_share_hash_algo: JENKINS_HASH_HI
          password_complexity:
            min_numerals: 2
        state: replaced

    # After state:
    # ------------
    # !
    # sonic(config)#do show running-configuration
    # !
    # ip anycast-address enable
    # ipv6 anycast-address enable
    # interface-naming standard
    # ip load-share hash algorithm JENKINS_HASH_HI
    # login password-attribute character-restriction numeric 2

    # Using "overridden" state
    #
    # Before state:
    # -------------
    # !
    # sonic(config)#do show running-configuration
    # !
    # banner motd @
    # banner - Enjoy the DELL OS
    # @
    # banner login disable
    # ipv6 anycast-address enable
    # ip load-share hash algorithm JENKINS_HASH_HI
    # login concurrent-session limit 5
    # login password-attribute character-restriction numeric 2

    - name: Override system configuration.
      sonic_system:
        config:
          hostname: SONIC
          interface_naming: standard
          anycast_address:
            ipv4: true
            mac_address: bb:aa:cc:dd:ee:ff
          load_share_hash_algo: CRC_XOR
          concurrent_session_limit: 4
          password_complexity:
            min_upper_case: 1
          banner:
            motd_banner_disable: true
            login: "@
    banner_login_message
    @"
            motd: "@
    banner_motd_message
    @"
            login_banner_disable: false
        state: overridden

    # After state:
    # ------------
    # !
    # SONIC(config)#do show running-configuration
    # !
    # banner login @
    # banner_login_message
    # @
    # banner motd @
    # banner_motd_message
    # @
    # banner motd disable
    # hostname SONIC
    # ip anycast-mac-address bb:aa:cc:dd:ee:ff
    # ip anycast-address enable
    # interface-naming standard
    # ip load-share hash algorithm CRC_XOR
    # login concurrent-session limit 4
    # login password-attribute character-restriction upper 1

    # Using "merged" state
    #
    # Before state:
    # -------------
    # !
    # sonic(config)#do show running-configuration
    # !

    - name: Merge provided configuration with device configuration
      dellemc.enterprise_sonic.sonic_system:
        config:
          hostname: SONIC
          interface_naming: standard
          auto_breakout: ENABLE
          load_share_hash_algo: JENKINS_HASH_HI
          audit_rules: BASIC
          exec_timeout: 15
        state: merged

    # After state:
    # ------------
    # !
    # SONIC(config)#do show running-configuration
    # !
    # hostname SONIC
    # interface-naming standard
    # auto-breakout
    # ip load-share hash algorithm JENKINS_HASH_HI
    # auditd-system rules basic
    # login exec-timeout 15

    # Using "deleted" state
    #
    # Before state:
    # -------------
    # !
    # SONIC(config)#do show running-configuration
    # !
    # hostname SONIC
    # interface-naming standard
    # auto-breakout
    # ip load-share hash algorithm JENKINS_HASH_HI
    # auditd-system rules basic
    # login exec-timeout 15

    - name: Delete auto-breakout configuration on the device
      dellemc.enterprise_sonic.sonic_system:
        config:
          hostname: SONIC
          auto_breakout: ENABLE
          load_share_hash_algo: JENKINS_HASH_HI
          audit_rules: BASIC
          login_exec_timeout: 15
        state: deleted

    # After state:
    # ------------
    # !
    # sonic(config)#do show running-configuration
    # !
    # interface-naming standard



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

- Abirami N (@abirami-n)
