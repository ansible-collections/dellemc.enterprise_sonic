.. _dellemc.enterprise_sonic.sonic_bfd_module:


**********************************
dellemc.enterprise_sonic.sonic_bfd
**********************************

**Manage BFD configuration on SONiC**


Version added: 2.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of BFD for devices running SONiC




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
                        <div>Specifies BFD configurations</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>multi_hops</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of multi-hop sessions</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>detect_multiplier</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">3</div>
                </td>
                <td>
                        <div>Number of missed packets to bring down a BFD session</div>
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
                                    <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                        </ul>
                </td>
                <td>
                        <div>Enables BFD session when set to true</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>local_address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Source IP address to be used for BFD sessions over the interface</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>min_ttl</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">254</div>
                </td>
                <td>
                        <div>Minimum expected TTL on received packets</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>passive_mode</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies BFD peer as passive when set to true</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>profile_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BFD profile name</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>receive_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">300</div>
                </td>
                <td>
                        <div>Specifies peer receive interval</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>remote_address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IP address used by the remote system for the BFD session</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>transmit_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">300</div>
                </td>
                <td>
                        <div>Specifies peer transmit interval</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vrf</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of the configured VRF on the device</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>profiles</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of preconfiguration profiles</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>detect_multiplier</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">3</div>
                </td>
                <td>
                        <div>Number of missed packets to bring down a BFD session</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>echo_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">300</div>
                </td>
                <td>
                        <div>Specifies echo interval</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>echo_mode</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Echo mode is enabled when set to true</div>
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
                                    <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                        </ul>
                </td>
                <td>
                        <div>Enables BFD session when set to true</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>min_ttl</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">254</div>
                </td>
                <td>
                        <div>Minimum expected TTL on received packets</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>passive_mode</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies BFD peer as passive when set to true</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>profile_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BFD profile name</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>receive_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">300</div>
                </td>
                <td>
                        <div>Specifies peer receive interval</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>transmit_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">300</div>
                </td>
                <td>
                        <div>Specifies peer transmit interval</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>single_hops</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of single-hop sessions</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>detect_multiplier</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">3</div>
                </td>
                <td>
                        <div>Number of missed packets to bring down a BFD session</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>echo_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">300</div>
                </td>
                <td>
                        <div>Specifies echo interval</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>echo_mode</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Echo mode is enabled when set to true</div>
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
                                    <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                        </ul>
                </td>
                <td>
                        <div>Enables BFD session when set to true</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interface</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Interface to use to contact peer</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>local_address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Source IP address to be used for BFD sessions over the interface</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>passive_mode</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies BFD peer as passive when set to true</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>profile_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BFD profile name</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>receive_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">300</div>
                </td>
                <td>
                        <div>Specifies peer receive interval</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>remote_address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IP address used by the remote system for the BFD session</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>transmit_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">300</div>
                </td>
                <td>
                        <div>Specifies peer transmit interval</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vrf</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of the configured VRF on the device</div>
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

    # Using "merged" state
    #
    # Before state:
    # -------------
    #
    # sonic# show bfd profile
    # (No "bfd profile" configuration present)
    # sonic# show bfd peers
    # (No "bfd peers" configuration present)

    - name: Merge BFD configuration
      dellemc.enterprise_sonic.sonic_bfd:
      config:
        profiles:
          - profile_name: 'p1'
            enabled: true
            transmit_interval: 120
            receive_interval: 200
            detect_multiplier: 2
            passive_mode: true
            min_ttl: 140
            echo_interval: 150
            echo_mode: true
        single_hops:
          - remote_address: '196.88.6.1'
            vrf: 'default'
            interface: 'Ethernet20'
            local_address: '1.1.1.1'
            enabled: true
            transmit_interval: 50
            receive_interval: 80
            detect_multiplier: 4
            passive_mode: true
            echo_interval: 110
            echo_mode: true
            profile_name: 'p1'
        multi_hops:
          - remote_address: '192.40.1.3'
            vrf: 'default'
            local_address: '3.3.3.3'
            enabled: true
            transmit_interval: 75
            receive_interval: 100
            detect_multiplier: 3
            passive_mode: true
            min_ttl: 125
            profile_name: 'p1'
      state: merged

    # After state:
    # ------------
    #
    # sonic# show bfd profile
    # BFD Profile:
    #     Profile-name: p1
    #         Enabled: True
    #         Echo-mode: Enabled
    #         Passive-mode: Enabled
    #         Minimum-Ttl: 140
    #         Detect-multiplier: 2
    #         Receive interval: 200ms
    #         Transmission interval: 120ms
    #         Echo transmission interval: 150ms
    # sonic# show bfd peers
    # BFD Peers:
    #
    #     peer 192.40.1.3 multihop local-address 3.3.3.3 vrf default
    #         ID: 989720421
    #         Remote ID: 0
    #         Passive mode: Enabled
    #         Profile: p1
    #         Minimum TTL: 125
    #         Status: down
    #         Downtime: 0 day(s), 0 hour(s), 1 min(s), 46 sec(s)
    #         Diagnostics: ok
    #         Remote diagnostics: ok
    #         Peer Type: configured
    #         Local timers:
    #             Detect-multiplier: 2
    #             Receive interval: 100ms
    #             Transmission interval: 75ms
    #             Echo transmission interval: ms
    #         Remote timers:
    #             Detect-multiplier: 3
    #             Receive interval: 1000ms
    #             Transmission interval: 1000ms
    #             Echo transmission interval: 0ms
    #
    #     peer 196.88.6.1 local-address 1.1.1.1 vrf default interface Ethernet20
    #         ID: 1134635660
    #         Remote ID: 0
    #         Passive mode: Enabled
    #         Profile: p1
    #         Status: down
    #         Downtime: 0 day(s), 1 hour(s), 50 min(s), 48 sec(s)
    #         Diagnostics: ok
    #         Remote diagnostics: ok
    #         Peer Type: configured
    #         Local timers:
    #             Detect-multiplier: 4
    #             Receive interval: 80ms
    #             Transmission interval: 50ms
    #             Echo transmission interval: 110ms
    #         Remote timers:
    #             Detect-multiplier: 3
    #             Receive interval: 1000ms
    #             Transmission interval: 1000ms
    #             Echo transmission interval: 0ms
    #
    #
    # Using "replaced" state
    #
    # Before state:
    # -------------
    #
    # sonic# show bfd profile
    # BFD Profile:
    #     Profile-name: p1
    #         Enabled: True
    #         Echo-mode: Enabled
    #         Passive-mode: Enabled
    #         Minimum-Ttl: 140
    #         Detect-multiplier: 2
    #         Receive interval: 200ms
    #         Transmission interval: 120ms
    #         Echo transmission interval: 150ms
    #     Profile-name: p2
    #         Enabled: True
    #         Echo-mode: Disabled
    #         Passive-mode: Disabled
    #         Minimum-Ttl: 254
    #         Detect-multiplier: 3
    #         Receive interval: 300ms
    #         Transmission interval: 300ms
    #         Echo transmission interval: 300ms

    - name: Replace BFD configuration
      dellemc.enterprise_sonic.sonic_bfd:
      config:
        profiles:
          - profile_name: 'p1'
            transmit_interval: 144
          - profile_name: 'p2'
            enabled: false
            transmit_interval: 110
            receive_interval: 235
            detect_multiplier: 5
            passive_mode: true
            min_ttl: 155
            echo_interval: 163
            echo_mode: true
      state: replaced

    # After state:
    # ------------
    #
    # sonic# show bfd profile
    # BFD Profile:
    #     Profile-name: p1
    #         Enabled: True
    #         Echo-mode: Enabled
    #         Passive-mode: Enabled
    #         Minimum-Ttl: 140
    #         Detect-multiplier: 2
    #         Receive interval: 200ms
    #         Transmission interval: 144ms
    #         Echo transmission interval: 150ms
    #     Profile-name: p2
    #         Enabled: False
    #         Echo-mode: Enabled
    #         Passive-mode: Enabled
    #         Minimum-Ttl: 155
    #         Detect-multiplier: 5
    #         Receive interval: 235ms
    #         Transmission interval: 110ms
    #         Echo transmission interval: 163ms
    #
    #
    # Using "overridden" state
    #
    # Before state:
    # -------------
    #
    # sonic# show bfd peers
    # BFD Peers:
    #
    #     peer 192.40.1.3 multihop local-address 3.3.3.3 vrf default
    #         ID: 989720421
    #         Remote ID: 0
    #         Passive mode: Enabled
    #         Profile: p1
    #         Minimum TTL: 125
    #         Status: down
    #         Downtime: 0 day(s), 0 hour(s), 1 min(s), 46 sec(s)
    #         Diagnostics: ok
    #         Remote diagnostics: ok
    #         Peer Type: configured
    #         Local timers:
    #             Detect-multiplier: 2
    #             Receive interval: 100ms
    #             Transmission interval: 75ms
    #             Echo transmission interval: ms
    #         Remote timers:
    #             Detect-multiplier: 3
    #             Receive interval: 1000ms
    #             Transmission interval: 1000ms
    #             Echo transmission interval: 0ms
    #
    #     peer 196.88.6.1 local-address 1.1.1.1 vrf default interface Ethernet20
    #         ID: 1134635660
    #         Remote ID: 0
    #         Passive mode: Enabled
    #         Profile: p1
    #         Status: down
    #         Downtime: 0 day(s), 1 hour(s), 50 min(s), 48 sec(s)
    #         Diagnostics: ok
    #         Remote diagnostics: ok
    #         Peer Type: configured
    #         Local timers:
    #             Detect-multiplier: 4
    #             Receive interval: 80ms
    #             Transmission interval: 50ms
    #             Echo transmission interval: 110ms
    #         Remote timers:
    #             Detect-multiplier: 3
    #             Receive interval: 1000ms
    #             Transmission interval: 1000ms
    #             Echo transmission interval: 0ms

    - name: Override BFD configuration
      dellemc.enterprise_sonic.sonic_bfd:
      config:
        single_hops:
          - remote_address: '172.68.2.1'
            vrf: 'default'
            interface: 'Ethernet16'
            local_address: '2.2.2.2'
            enabled: true
            transmit_interval: 60
            receive_interval: 88
            detect_multiplier: 6
            passive_mode: true
            echo_interval: 112
            echo_mode: true
            profile_name: 'p3'
        multi_hops:
          - remote_address: '186.42.1.2'
            vrf: 'default'
            local_address: '1.1.1.1'
            enabled: false
            transmit_interval: 85
            receive_interval: 122
            detect_multiplier: 4
            passive_mode: false
            min_ttl: 120
            profile_name: 'p3'
      state: overridden

    # After state:
    # ------------
    #
    # sonic# show bfd peers
    # BFD Peers:
    #
    #     peer 186.42.1.2 multihop local-address 1.1.1.1 vrf default
    #         ID: 989720421
    #         Remote ID: 0
    #         Passive mode: Disabled
    #         Profile: p3
    #         Minimum TTL: 120
    #         Status: down
    #         Downtime: 0 day(s), 0 hour(s), 1 min(s), 46 sec(s)
    #         Diagnostics: ok
    #         Remote diagnostics: ok
    #         Peer Type: configured
    #         Local timers:
    #             Detect-multiplier: 4
    #             Receive interval: 122ms
    #             Transmission interval: 85ms
    #             Echo transmission interval: ms
    #         Remote timers:
    #             Detect-multiplier: 3
    #             Receive interval: 1000ms
    #             Transmission interval: 1000ms
    #             Echo transmission interval: 0ms
    #
    #     peer 172.68.2.1 local-address 2.2.2.2 vrf default interface Ethernet16
    #         ID: 1134635660
    #         Remote ID: 0
    #         Passive mode: Enabled
    #         Profile: p3
    #         Status: down
    #         Downtime: 0 day(s), 1 hour(s), 50 min(s), 48 sec(s)
    #         Diagnostics: ok
    #         Remote diagnostics: ok
    #         Peer Type: configured
    #         Local timers:
    #             Detect-multiplier: 6
    #             Receive interval: 88ms
    #             Transmission interval: 60ms
    #             Echo transmission interval: 112ms
    #         Remote timers:
    #             Detect-multiplier: 3
    #             Receive interval: 1000ms
    #             Transmission interval: 1000ms
    #             Echo transmission interval: 0ms
    #
    #
    # Using "deleted" state
    #
    # Before state:
    # -------------
    #
    # sonic# show bfd profile
    # BFD Profile:
    #     Profile-name: p1
    #         Enabled: True
    #         Echo-mode: Enabled
    #         Passive-mode: Enabled
    #         Minimum-Ttl: 140
    #         Detect-multiplier: 2
    #         Receive interval: 200ms
    #         Transmission interval: 120ms
    #         Echo transmission interval: 150ms
    # sonic# show bfd peers
    # BFD Peers:
    #
    #     peer 192.40.1.3 multihop local-address 3.3.3.3 vrf default
    #         ID: 989720421
    #         Remote ID: 0
    #         Passive mode: Enabled
    #         Profile: p1
    #         Minimum TTL: 125
    #         Status: down
    #         Downtime: 0 day(s), 0 hour(s), 1 min(s), 46 sec(s)
    #         Diagnostics: ok
    #         Remote diagnostics: ok
    #         Peer Type: configured
    #         Local timers:
    #             Detect-multiplier: 2
    #             Receive interval: 100ms
    #             Transmission interval: 75ms
    #             Echo transmission interval: ms
    #         Remote timers:
    #             Detect-multiplier: 3
    #             Receive interval: 1000ms
    #             Transmission interval: 1000ms
    #             Echo transmission interval: 0ms
    #
    #     peer 196.88.6.1 local-address 1.1.1.1 vrf default interface Ethernet20
    #         ID: 1134635660
    #         Remote ID: 0
    #         Passive mode: Enabled
    #         Profile: p1
    #         Status: down
    #         Downtime: 0 day(s), 1 hour(s), 50 min(s), 48 sec(s)
    #         Diagnostics: ok
    #         Remote diagnostics: ok
    #         Peer Type: configured
    #         Local timers:
    #             Detect-multiplier: 4
    #             Receive interval: 80ms
    #             Transmission interval: 50ms
    #             Echo transmission interval: 110ms
    #         Remote timers:
    #             Detect-multiplier: 3
    #             Receive interval: 1000ms
    #             Transmission interval: 1000ms
    #             Echo transmission interval: 0ms

    - name: Delete BFD configuration
      dellemc.enterprise_sonic.sonic_bfd:
      config:
        profiles:
          - profile_name: 'p1'
            enabled: true
            transmit_interval: 120
            receive_interval: 200
            detect_multiplier: 2
            passive_mode: true
            min_ttl: 140
            echo_interval: 150
            echo_mode: true
        single_hops:
          - remote_address: '196.88.6.1'
            vrf: 'default'
            interface: 'Ethernet20'
            local_address: '1.1.1.1'
        multi_hops:
          - remote_address: '192.40.1.3'
            vrf: 'default'
            local_address: '3.3.3.3'
      state: deleted

    # After state
    # -----------
    #
    # sonic# show bfd profile
    # BFD Profile:
    #     Profile-name: p1
    #         Enabled: True
    #         Echo-mode: Disabled
    #         Passive-mode: Disabled
    #         Minimum-Ttl: 254
    #         Detect-multiplier: 3
    #         Receive interval: 300ms
    #         Transmission interval: 300ms
    #         Echo transmission interval: 300ms
    # sonic# show bfd peers
    # (No "bfd peers" configuration present)



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

- S. Talabi (@stalabi1)
