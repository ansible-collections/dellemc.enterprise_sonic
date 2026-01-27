.. _dellemc.enterprise_sonic.sonic_poe_module:


**********************************
dellemc.enterprise_sonic.sonic_poe
**********************************

**Manage PoE configuration on SONiC**


Version added: 2.5.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of PoE at global and card level for devices running SONiC




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
                        <div>Specifies PoE configurations</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>cards</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>PoE card (power controller hardware) configuration.</div>
                        <div>currently not supported on platforms.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>auto_reset</b>
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
                        <div>enable PoE auto reset mode for this card</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>card_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Identifier for the card.</div>
                        <div>must be number in range of 0-7.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>power_mgmt_model</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>dynamic</li>
                                    <li>dynamic-priority</li>
                                    <li>static</li>
                                    <li>static-priority</li>
                                    <li>class</li>
                        </ul>
                </td>
                <td>
                        <div>the power management algorithm.</div>
                        <div>dynamic means that power consumption of each port is measured and calculated in real-time.</div>
                        <div>static means that power allocated for each port depends on the type of power threshold configured on the port</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>usage_threshold</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Inline power usage threshold.</div>
                        <div>Range is 0-99 inclusive</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>global</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>configuration for global PoE card</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>auto_reset</b>
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
                        <div>enable PoE auto reset mode for global.</div>
                        <div>currently not supported on platforms.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>power_mgmt_model</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>dynamic</li>
                                    <li>dynamic-priority</li>
                                    <li>static</li>
                                    <li>static-priority</li>
                                    <li>class</li>
                        </ul>
                </td>
                <td>
                        <div>the power management algorithm to use.</div>
                        <div>dynamic means that power consumption of each port is measured and calculated in real-time.</div>
                        <div>static means that power allocated for each port depends on the type of power threshold configured on the port.</div>
                        <div>currently only &#x27;dynamic&#x27; and &#x27;class&#x27; values are supported</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>usage_threshold</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Inline power usage threshold.</div>
                        <div>Range is 0-99 inclusive.</div>
                        <div>currently not supported on platforms.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interfaces</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>PoE configuration for ethernet interfaces</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>detection</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>2pt-dot3af</li>
                                    <li>2pt-dot3af+legacy</li>
                                    <li>4pt-dot3af</li>
                                    <li>4pt-dot3af+legacy</li>
                                    <li>dot3bt</li>
                                    <li>dot3bt+legacy</li>
                                    <li>legacy</li>
                        </ul>
                </td>
                <td>
                        <div>Device detection mechanism performed by this PSE port.</div>
                        <div>Legacy is capacitive detection scheme, which can be used alone or as a backup if other detection schemes fail.</div>
                        <div>Those schemes are IEEE 802 standard schemes.</div>
                        <div>None cannot be forcibly set by adminstrator.</div>
                        <div>currently only &#x27;dot3bt&#x27; and &#x27;dot3bt+legacy&#x27; values are supported</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>disconnect_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ac</li>
                                    <li>dc</li>
                        </ul>
                </td>
                <td>
                        <div>PoE port disconnect type.</div>
                        <div>currently not supported on platforms.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>enable PoE per port</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>four_pair</b>
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
                        <div>Enables four pair mode for port.</div>
                        <div>currently not supported on platforms.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>high_power</b>
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
                        <div>Enables high power mode on a PSE port.</div>
                        <div>currently not supported on platforms.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>Name of the interface</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>power_classification</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>normal</li>
                                    <li>bypass</li>
                        </ul>
                </td>
                <td>
                        <div>PoE power-classification mode for port.</div>
                        <div>currently not supported on platforms.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>power_limit</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The configured maximum power this port can provide to an attached device measured in Milliwatts.</div>
                        <div>Range is 0-99900 inclusive.</div>
                        <div>currently not supported on platforms.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>power_limit_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>class-based</li>
                                    <li>user-defined</li>
                        </ul>
                </td>
                <td>
                        <div>Controls the maximum power that a port can deliver.</div>
                        <div>class-based means that the port power limit is as per the dot3af class of the powered device attached.</div>
                        <div>user-defined means limit is specified by config.</div>
                        <div>currently not supported on platforms.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>power_pairs</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>signal</li>
                                    <li>spare</li>
                        </ul>
                </td>
                <td>
                        <div>PoE port power-pairs settings.</div>
                        <div>currently not supported on platforms.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>power_up_mode</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>dot3af</li>
                                    <li>dot3at</li>
                                    <li>dot3bt</li>
                                    <li>dot3bt-type3</li>
                                    <li>dot3bt-type4</li>
                                    <li>high-inrush</li>
                                    <li>pre-dot3at</li>
                                    <li>pre-dot3bt</li>
                        </ul>
                </td>
                <td>
                        <div>The mode configured for a PSE port to deliver high power.</div>
                        <div>pre-dot3at means that a port is powered in the IEEE 802.3af mode initially, switched to the high-power IEEE 802.3at mode.</div>
                        <div>dot3at means that a port is powered in the IEEE 802.3at mode.</div>
                        <div>dot3bt, type3 and pre-dot3bt are to support 802.3bt interfaces.</div>
                        <div>currently not supported on platforms.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>priority</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>low</li>
                                    <li>medium</li>
                                    <li>high</li>
                                    <li>critical</li>
                        </ul>
                </td>
                <td>
                        <div>PoE port priority in power management algorithm.</div>
                        <div>Priority could be used by a control mechanism that prevents over current situations by disconnecting ports with lower power priority first.</div>
                        <div>currently only &#x27;low&#x27;, &#x27;high&#x27; and &#x27;critical&#x27; values are supported</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>use_spare_pair</b>
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
                        <div>Enables spare pair power for port.</div>
                        <div>currently not supported on platforms.</div>
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
                        <div>The state of the configuration after module completion</div>
                </td>
            </tr>
    </table>
    <br/>




Examples
--------

.. code-block:: yaml

    # Using "merged" state to add or change poe global settings
    # Before state:
    # config:
    #   global:
    #     auto_reset: false

    # Example:
    - name: "add poe global settings"
      sonic_poe:
        config:
          global:
            auto_reset: true
            power_mgmt_model: 'class'
            usage_threshold: 300
        state: merged

    # After state:
    # config:
    #   global:
    #     auto_reset: true
    #     power_mgmt_model: 'class'
    #     usage_threshold: 300
    # ------

    # Using "merged" state to add cards
    # Note that platform must support adding multiple cards to do this
    # Before state:
    # config:
    #   global:
    #     auto_reset: true

    # Example:
    - name: "add poe cards"
      sonic_poe:
        config:
          cards:
            - card_id: 0
              usage_threshold: 39
        state: merged

    # After state:
    # config:
    #   global:
    #     auto_reset: true
    #   cards:
    #     - card_id: 0
    #       usage_threshold: 39
    # ------

    # Using "merged" state to add or change card settings
    # Before state:
    # config:
    #   cards:
    #     - card_id: 0
    #       usage_threshold: 39

    # Example:
    - name: "add poe cards settings"
      sonic_poe:
        config:
          cards:
            - card_id: 0
              usage_threshold: 60
              power_mgmt_model: dymanic
        state: merged

    # After state:
    # config:
    #   cards:
    #     - card_id: 0
    #       usage_threshold: 60
    #       power_mgmt_model: dymanic
    # ------

    # Using "merged" state to add interfaces
    # Before state:
    # config: {}

    # Example:
    - name: "add poe interfaces"
      sonic_poe:
        config:
          interfaces:
            - name: Ethernet0
              enabled: true
        state: merged

    # After state:
    # config:
    #   interfaces:
    #     - name: Ethernet0
    #       enabled: true
    # ------

    # Using "merged" state to add or change interface settings
    # Before state:
    # config:
    #   interfaces:
    #     - name: Ethernet0
    #       enabled: true
    #       disconnect_type: dc

    # Example:
    - name: "add poe interface settings"
      sonic_poe:
        config:
          interfaces:
            - name: Ethernet0
              four_pair: true
              high_power: true
              detection: dot3bt
              power_classification: normal
              power_limit: 5000
              power_limit_type: class-based
              power_pairs: signal
              power_up_mode: dot3bt
              priority: medium
              use_spare_pair: false
              disconnect_type: ac
        state: merged

    # After state:
    # config:
    #   interfaces:
    #     - name: Ethernet0
    #       four_pair: true
    #       high_power: true
    #       detection: dot3bt
    #       power_classification: normal
    #       power_limit: 5000
    #       power_limit_type: class-based
    #       power_pairs: signal
    #       power_up_mode: dot3bt
    #       priority: medium
    #       use_spare_pair: false
    #       disconnect_type: ac
    #       enabled: true
    # ------


    # Using "deleted" state to remove poe global settings
    # Before state:
    # config:
    #   global:
    #     auto_reset: true
    #     power_mgmt_model: 'class'
    #     usage_threshold: 300

    # Example:
    - name: "delete matching poe global settings"
      sonic_poe:
        config:
          global:
            auto_reset: false
            usage_threshold: 300
        state: deleted

    # After state:
    # config:
    #   global:
    #     power_mgmt_model: 'class'
    #     auto_reset: true
    # ------

    # Using "deleted" state to delete cards or card settings
    # Note: to delete whole card, either need just the name or specify all current settings and values
    # Before state:
    # config:
    #   global:
    #     auto_reset: true
    #   cards:
    #     - card_id: 0
    #       usage_threshold: 39
    #     - card_id: 1
    #       auto_reset: true
    #       usage_threshold: 60
    #       power_mgmt_model: class
    #     - card_id: 2
    #       usage_threshold: 39
    #       power_mgmt_model: dymanic

    # Example:
    - name: "delete poe cards"
      sonic_poe:
        config:
          cards:
            - card_id: 0
            - card_id: 1
              auto_reset: true
              usage_threshold: 60
              power_mgmt_model: class
            - card_id: 2
              usage_threshold: 39
              power_mgmt_model: static
        state: deleted

    # After state:
    # config:
    #   global:
    #     auto_reset: true
    #   cards:
    #     - card_id: 2
    #       power_mgmt_model: dymanic
    # ------

    # Using "deleted" state to delete interfaces or interface settings
    # Note: to delete whole interface, either need just the name or specify all current settings and values
    # Before state:
    # config:
    #   interfaces:
    #     - name: Ethernet0
    #       enabled: true
    #     - name: Ethernet1
    #       enabled: false
    #       four_pair: true
    #     - name: Ethernet2
    #       detection: 4pt-dot3af+legacy
    #       power_up_mode: dot3bt
    #       use_spare_pair: true

    # Example:
    - name: "delete poe interfaces"
      sonic_poe:
        config:
          interfaces:
            - name: Ethernet0
            - name: Ethernet1
              enabled: false
              four_pair: true
            - name: Ethernet2
              detection: 4pt-dot3af+legacy
              power_up_mode: pre-dot3at
        state: deleted

    # After state:
    # config:
    #   interfaces:
    #     - name: Ethernet2
    #       power_up_mode: dot3bt
    #       use_spare_pair: true
    # ------

    # Using "deleted" state to clear all interfaces or cards
    # Before state:
    # config:
    #   cards:
    #     - card_id: 0
    #       usage_threshold: 39
    #   interfaces:
    #     - name: Ethernet0
    #       enabled: true

    # Example:
    - name: "clear poe interfaces and cards"
      sonic_poe:
        config:
          interfaces: []
          cards: []
        state: deleted

    # After state:
    # config: {}
    # ------

    # Using "deleted" state to delete attributes of interfaces or cards
    # Before state:
    # config:
    #   cards:
    #     - card_id: 1
    #       auto_reset: true
    #       usage_threshold: 60
    #   interfaces:
    #     - name: Ethernet1
    #       enabled: false
    #       four_pair: true
    #       power_classification: normal

    # Example:
    - name: "clear poe interfaces and cards"
      sonic_poe:
        config:
          interfaces:
            - name: Ethernet1
              four_pair: true
              cards:
                - card_id: 1
                  usage_threshold: 60
        state: deleted

    # After state:
    # config:
    #   interfaces:
    #     - name: Ethernet1
    #       enabled: false
    #       power_classification: normal
    #   cards:
    #     - card_id: 1
    #       auto_reset: true
    # ------


    # Using "overridden" state to set poe config
    # Before state:
    # config:
    #   global:
    #     auto_reset: true
    #     power_mgmt_model: 'class'
    #     usage_threshold: 300
    #   interfaces:
    #     - name: Ethernet1
    #       power_classification: normal
    #       enabled: true
    #   cards:
    #     - card_id: 0
    #       usage_threshold: 60
    #       power_mgmt_model: dymanic

    # Example:
    - name: "overridden to exactly specified"
      sonic_poe:
        config:
          global:
            auto_reset: false
          interfaces:
            - name: Ethernet0
              enabled: true
              disconnect_type: ac
            - name: Ethernet1
              power_pairs: signal
        state: overridden

    # After state:
    # config:
    #   global:
    #     auto_reset: false
    #   interfaces:
    #     - name: Ethernet0
    #       disconnect_type: ac
    #       enabled: true
    #     - name: Ethernet1
    #       power_pairs: signal
    # ------


    # Using "replaced" state to replace sections of poe config
    # Before state:
    # config:
    #   global:
    #     auto_reset: true
    #     power_mgmt_model: 'class'
    #     usage_threshold: 300
    #   interfaces:
    #     - name: Ethernet1
    #       power_classification: normal
    #       enabled: true
    #     - name: Ethernet0
    #       enabled: true
    #       power_limit_type: class-based
    #   cards:
    #     - card_id: 0
    #       usage_threshold: 60
    #       power_mgmt_model: dymanic

    # Example:
    - name: "replace sections of config to exactly specified"
      sonic_poe:
        config:
          global:
            auto_reset: false
          interfaces:
            - name: Ethernet0
              enabled: true
              disconnect_type: ac
        state: repalced

    # After state:
    # config:
    #   global:
    #     auto_reset: false
    #   interfaces:
    #     - name: Ethernet0
    #       disconnect_type: ac
    #       enabled: true
    #   cards:
    #     - card_id: 0
    #       usage_threshold: 60
    #       power_mgmt_model: dymanic
    # ------



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
                            <div>The resulting configuration after module invocation.</div>
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
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The configuration prior to the module invocation.</div>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;command 1&#x27;, &#x27;command 2&#x27;, &#x27;command 3&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- S. Talabi (@stalabi1), Xiao Han (@Xiao_Han2)
