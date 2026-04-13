.. _dellemc.enterprise_sonic.sonic_ospfv2_interfaces_module:


************************************************
dellemc.enterprise_sonic.sonic_ospfv2_interfaces
************************************************

**Configure OSPFv2 interface mode protocol settings on SONiC.**


Version added: 2.5.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of OSPFv2 interface mode parameters on devices running SONiC.
- Configure VRF instance before configuring OSPF in a VRF.
- Configure OSPF instance before configuring OSPF in interfaces.




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
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the OSPFv2 interface configurations.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>bfd</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure OSPFv2 interface BFD.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>bfd_profile</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure BFD profile.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>enable</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Enable BFD support for OSPFv2.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Full name of the interface, i.e. Ethernet1.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>network</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>broadcast</li>
                                    <li>point_to_point</li>
                        </ul>
                </td>
                <td>
                        <div>Configure OSPFv2 interface network type</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ospf_attributes</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies OSPFv2 configurations for the interface.</div>
                        <div>If <em>address</em> is not specified, the IPv4 address of the interface is considered.</div>
                        <div><em>dead_interval</em> and <em>hello_multiplier</em> are mutually exclusive.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the interface IPv4 address.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>area_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>OSPFv2 Area ID of the network (A.B.C.D or 0 to 4294967295).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>authentication</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure OSPFv2 plain text authentication type password.</div>
                        <div>Authentication key shall be max 8 charater long.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>encrypted</b>
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
                        <div>Indicates whether the password is in encrypted format.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>password</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the authentication password.</div>
                        <div>Plain text password i.e. password with <em>encrypted=false</em> will be stored in encrypted format in running-config, so idempotency will not be maintained and hence the task output will always be <em>changed=true</em>.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>authentication_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>MD5HMAC</li>
                                    <li>NONE</li>
                                    <li>TEXT</li>
                        </ul>
                </td>
                <td>
                        <div>Enable OSPFv2 authentication and its type.</div>
                        <div><code>MD5HMAC</code> - Enable Message digest authentication type.</div>
                        <div><code>NONE</code> - Enable null authentication.</div>
                        <div><code>TEXT</code> - Enable plain text authentication.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>cost</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure OSPFv2 interface cost (1 to 65535).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dead_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure OSPFv2 adjacency dead interval (1 to 65535).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>hello_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure OSPFv2 neighbour hello interval (1 to 65535).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>hello_multiplier</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Minimal 1s dead-interval with fast sub-second hellos.</div>
                        <div>Number of Hellos to send each second (1 to 10).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>md_authentication</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure OSPFv2 message digest keys and password.</div>
                        <div>Uses MD5 algorithm.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>encrypted</b>
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
                        <div>Indicates whether the password is in encrypted format.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>key_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the OSPFv2 message digest key ID (1 to 255).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>md5key</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the OSPFv2 message digest password.</div>
                        <div>Plain text password i.e. password with <em>encrypted=false</em> will be stored in encrypted format in running-config, so idempotency will not be maintained and hence the task output will always be <em>changed=true</em>.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mtu_ignore</b>
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
                        <div>Disable OSPFv2 MTU mismatch detection.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>priority</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure OSPFv2 adjacency router priority (0 to 255).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>retransmit_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure OSPFv2 retransmit interval (2 to 65535).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>transmit_delay</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure OSPFv2 transmit delay (1 to 65535).</div>
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
                        <div>Specifies the operation to be performed on the OSPFv2 interfaces configured on the device.</div>
                        <div>In case of merged, the input configuration will be merged with the existing OSPFv2 interfaces configuration on the device.</div>
                        <div>In case of deleted, the existing OSPFv2 interfaces configuration will be removed from the device.</div>
                        <div>In case of overridden, all the existing OSPFv2 interfaces configuration will be deleted and the specified input configuration will be installed.</div>
                        <div>In case of replaced, the existing OSPFv2 interface configuration on the device will be replaced by the configuration in the playbook for each interface group configured by the playbook.</div>
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

    # Using "deleted" state

    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    # ip ospf area 2.2.2.2
    # ip ospf bfd
    # ip ospf bfd profile profile2
    # ip ospf cost 30
    # ip ospf dead-interval 40
    # ip ospf hello-interval 10
    # ip ospf mtu-ignore
    # ip ospf network point-to-point
    # ip ospf priority 20
    # ip ospf authentication null 10.10.120.1
    # ip ospf authentication-key U2FsdGVkX1/Ml24vwe6RSjUUqI+54BdDyDL0eKUezJw= encrypted 10.10.120.1
    # ip ospf dead-interval minimal hello-multiplier 5 10.10.120.1
    # ip ospf authentication null 10.19.119.1
    # ip ospf message-digest-key 10 md5 U2FsdGVkX1/Bq/+x8a3fsBo9ZrAX56ynmPKnRM87kfQ= encrypted 10.19.119.1
    # !
    # interface Eth1/2
    # ip ospf bfd
    # ip ospf network point-to-point
    # !
    # interface Eth1/3
    # ip ospf bfd
    # ip ospf network point-to-point
    # ip ospf area 3.3.3.3 10.19.120.2
    # ip ospf authentication message-digest 10.19.120.2
    # ip ospf authentication-key U2FsdGVkX19HqGCcf2pzGur9MDnb0VzLNRvoFij3Os0= encrypted 10.19.120.2
    # ip ospf dead-interval minimal hello-multiplier 5 10.19.120.2
    # !
    # sonic#

    - name: Delete the OSPFv2_interface configurations
      sonic_ospfv2_interfaces:
        config:
          - name: 'Eth1/1'
            ospf_attributes:
              - area_id: '2.2.2.2'
                cost: 30
                priority: 20
                hello_interval: 10
                dead_interval: 40
                mtu_ignore: true
              - address: '10.10.120.1'
                authentication_type: 'NONE'
                authentication:
                  password: 'pass2'
              - address: '10.19.119.1'
            bfd:
              enable: true
              bfd_profile: 'profile2'
            network: point_to_point
          - name: 'Eth1/2'
            bfd:
              enable: true
          - name: 'Eth1/3'
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    # ip ospf dead-interval minimal hello-multiplier 5 10.10.120.1
    # !
    # interface Eth1/2
    # ip ospf network point-to-point
    # !
    # interface Eth1/3
    # !
    # sonic#


    # Using "deleted" state

    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    # ip ospf area 2.2.2.2
    # ip ospf bfd
    # ip ospf bfd profile profile2
    # ip ospf cost 30
    # ip ospf dead-interval 40
    # ip ospf hello-interval 10
    # ip ospf mtu-ignore
    # ip ospf network point-to-point
    # ip ospf priority 20
    # ip ospf authentication null 10.10.120.1
    # ip ospf authentication-key U2FsdGVkX1/Ml24vwe6RSjUUqI+54BdDyDL0eKUezJw= encrypted 10.10.120.1
    # ip ospf dead-interval minimal hello-multiplier 5 10.10.120.1
    # ip ospf authentication null 10.19.119.1
    # ip ospf message-digest-key 10 md5 U2FsdGVkX1/Bq/+x8a3fsBo9ZrAX56ynmPKnRM87kfQ= encrypted 10.19.119.1
    # !
    # interface Eth1/2
    # ip ospf bfd
    # ip ospf network point-to-point
    # !
    # interface Eth1/3
    # ip ospf bfd
    # ip ospf network point-to-point
    # ip ospf area 3.3.3.3 10.19.120.2
    # ip ospf authentication message-digest 10.19.120.2
    # ip ospf authentication-key U2FsdGVkX19HqGCcf2pzGur9MDnb0VzLNRvoFij3Os0= encrypted 10.19.120.2
    # ip ospf dead-interval minimal hello-multiplier 5 10.19.120.2
    # !
    # sonic#

    - name: Delete the OSPFv2_interface configurations
      sonic_ospfv2_interfaces:
        config:
          - name: 'Eth1/1'
          - name: 'Eth1/2'
            bfd:
              enable: true
          - name: 'Eth1/3'
        state: deleted

    # After state:
    # ------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    # !
    # interface Eth1/2
    # ip ospf network point-to-point
    # !
    # interface Eth1/3
    # !
    # sonic#


    # Using "merged" state

    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    # !
    # interface Eth1/2
    # !
    # interface Eth1/3
    # !
    # sonic#

    - name: Add the OSPFv2_interface configurations
      sonic_ospfv2_interfaces:
        config:
          - name: 'Eth1/1'
            ospf_attributes:
              - area_id: '2.2.2.2'
                cost: 20
                priority: 20
                hello_interval: 10
                dead_interval: 40
                mtu_ignore: true
                -address: '10.10.120.1'
                authentication_type: 'MD5HMAC'
                authentication:
                  password: 'password'
                hello_multiplier: 5
            bfd:
              enable: true
              bfd_profile: 'profile1'
            network: broadcast
          - name: 'Eth1/3'
            ospf_attributes:
              - area_id: '3.3.3.3'
                address: '10.19.120.2'
                authentication_type: 'MD5HMAC'
                authentication:
                  password: 'password'
                hello_multiplier: 5
            bfd:
              enable: true
            network: point_to_point
        state: merged

    # After state:
    # ------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    # ip ospf area 2.2.2.2
    # ip ospf bfd
    # ip ospf bfd profile profile1
    # ip ospf cost 20
    # ip ospf dead-interval 40
    # ip ospf hello-interval 10
    # ip ospf mtu-ignore
    # ip ospf network broadcast
    # ip ospf priority 20
    # ip ospf authentication message-digest 10.10.120.1
    # ip ospf authentication-key U2FsdGVkX1+ozJSEI69XJb2KR9Pu1Sa3Ou6ujTRalbQ= encrypted 10.10.120.1
    # ip ospf dead-interval minimal hello-multiplier 5 10.10.120.1
    # !
    # interface Eth1/2
    # !
    # interface Eth1/3
    # ip ospf bfd
    # ip ospf network point-to-point
    # ip ospf area 3.3.3.3 10.19.120.2
    # ip ospf authentication message-digest 10.19.120.2
    # ip ospf authentication-key U2FsdGVkX19HqGCcf2pzGur9MDnb0VzLNRvoFij3Os0= encrypted 10.19.120.2
    # ip ospf dead-interval minimal hello-multiplier 5 10.19.120.2
    # !
    # sonic#


    # Using "merged" state

    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    # ip ospf area 2.2.2.2
    # ip ospf bfd
    # ip ospf bfd profile profile1
    # ip ospf cost 20
    # ip ospf dead-interval 40
    # ip ospf hello-interval 10
    # ip ospf mtu-ignore
    # ip ospf network broadcast
    # ip ospf priority 20
    # ip ospf authentication message-digest 10.10.120.1
    # ip ospf authentication-key U2FsdGVkX1+ozJSEI69XJb2KR9Pu1Sa3Ou6ujTRalbQ= encrypted 10.10.120.1
    # ip ospf dead-interval minimal hello-multiplier 5 10.10.120.1
    # !
    # interface Eth1/2
    # !
    # interface Eth1/3
    # ip ospf bfd
    # ip ospf network point-to-point
    # ip ospf area 3.3.3.3 10.19.120.2
    # ip ospf authentication message-digest 10.19.120.2
    # ip ospf authentication-key U2FsdGVkX19HqGCcf2pzGur9MDnb0VzLNRvoFij3Os0= encrypted 10.19.120.2
    # ip ospf dead-interval minimal hello-multiplier 5 10.19.120.2
    # !
    # sonic#

    - name: Add the OSPFv2_interface configurations
      sonic_ospfv2_interfaces:
        config:
          - name: 'Eth1/1'
            ospf_attributes:
              - area_id: '2.2.2.2'
                cost: 30
                priority: 20
                hello_interval: 10
                dead_interval: 40
                mtu_ignore: true
              - address: '10.10.120.1'
                authentication_type: 'NONE'
                authentication:
                  password: 'pass2'
              - address: '10.19.119.1'
                authentication_type: 'NONE'
                md_authentication:
                  - key_id: 10
                    md5key: 'U2FsdGVkX1/Bq/+x8a3fsBo9ZrAX56ynmPKnRM87kfQ='
                    encrypted: true
            bfd:
              enable: true
              bfd_profile: 'profile2'
            network: point_to_point
          - name: 'Eth1/2'
            bfd:
              enable: true
            network: point_to_point
        state: merged

    # After state:
    # ------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    # ip ospf area 2.2.2.2
    # ip ospf bfd
    # ip ospf bfd profile profile2
    # ip ospf cost 30
    # ip ospf dead-interval 40
    # ip ospf hello-interval 10
    # ip ospf mtu-ignore
    # ip ospf network point-to-point
    # ip ospf priority 20
    # ip ospf authentication null 10.10.120.1
    # ip ospf authentication-key U2FsdGVkX1/Ml24vwe6RSjUUqI+54BdDyDL0eKUezJw= encrypted 10.10.120.1
    # ip ospf dead-interval minimal hello-multiplier 5 10.10.120.1
    # ip ospf authentication null 10.19.119.1
    # ip ospf message-digest-key 10 md5 U2FsdGVkX1/Bq/+x8a3fsBo9ZrAX56ynmPKnRM87kfQ= encrypted 10.19.119.1
    # !
    # interface Eth1/2
    # ip ospf bfd
    # ip ospf network point-to-point
    # !
    # interface Eth1/3
    # ip ospf bfd
    # ip ospf network point-to-point
    # ip ospf area 3.3.3.3 10.19.120.2
    # ip ospf authentication message-digest 10.19.120.2
    # ip ospf authentication-key U2FsdGVkX19HqGCcf2pzGur9MDnb0VzLNRvoFij3Os0= encrypted 10.19.120.2
    # ip ospf dead-interval minimal hello-multiplier 5 10.19.120.2
    # !
    # sonic#


    # Using "replaced" state

    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    # ip ospf area 2.2.2.2
    # ip ospf bfd
    # ip ospf bfd profile profile1
    # ip ospf cost 20
    # ip ospf dead-interval 40
    # ip ospf hello-interval 10
    # ip ospf mtu-ignore
    # ip ospf network broadcast
    # ip ospf priority 20
    # ip ospf authentication message-digest 10.10.120.1
    # ip ospf authentication-key U2FsdGVkX1+ozJSEI69XJb2KR9Pu1Sa3Ou6ujTRalbQ= encrypted 10.10.120.1
    # ip ospf dead-interval minimal hello-multiplier 5 10.10.120.1
    # !
    # interface Eth1/2
    # !
    # interface Eth1/3
    # ip ospf bfd
    # ip ospf network point-to-point
    # ip ospf area 3.3.3.3 10.19.120.2
    # ip ospf authentication message-digest 10.19.120.2
    # ip ospf authentication-key U2FsdGVkX19HqGCcf2pzGur9MDnb0VzLNRvoFij3Os0= encrypted 10.19.120.2
    # ip ospf dead-interval minimal hello-multiplier 5 10.19.120.2
    # !
    # sonic#

    - name: Replace the OSPFv2_interface configurations
      sonic_ospfv2_interfaces:
        config:
          - name: 'Eth1/3'
            ospf_attributes:
              - area_id: '2.2.2.2'
                cost: 30
                priority: 20
                hello_interval: 10
                dead_interval: 40
                mtu_ignore: true
              - address: '10.10.120.1'
                authentication_type: 'NONE'
                authentication:
                  password: 'pass2'
              - address: '10.19.119.1'
                authentication_type: 'NONE'
                md_authentication:
                  - key_id: 10
                    md5key: 'U2FsdGVkX1/Bq/+x8a3fsBo9ZrAX56ynmPKnRM87kfQ='
                    encrypted: true
            bfd:
              enable: true
              bfd_profile: 'profile2'
            network: broadcast
        state: replaced

    # After state:
    # ------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    # ip ospf area 2.2.2.2
    # ip ospf bfd
    # ip ospf bfd profile profile1
    # ip ospf cost 20
    # ip ospf dead-interval 40
    # ip ospf hello-interval 10
    # ip ospf mtu-ignore
    # ip ospf network broadcast
    # ip ospf priority 20
    # ip ospf authentication message-digest 10.10.120.1
    # ip ospf authentication-key U2FsdGVkX1+ozJSEI69XJb2KR9Pu1Sa3Ou6ujTRalbQ= encrypted 10.10.120.1
    # ip ospf dead-interval minimal hello-multiplier 5 10.10.120.1
    # !
    # interface Eth1/2
    # !
    # interface Eth1/3
    # ip ospf area 2.2.2.2
    # ip ospf bfd
    # ip ospf bfd profile profile2
    # ip ospf cost 30
    # ip ospf dead-interval 40
    # ip ospf hello-interval 10
    # ip ospf mtu-ignore
    # ip ospf network broadcast
    # ip ospf priority 20
    # ip ospf authentication null 10.10.120.1
    # ip ospf authentication-key U2FsdGVkX186k2R2hUXaDloW8hfkApn5Zx5hCQy9usc= encrypted 10.10.120.1
    # ip ospf authentication null 10.19.119.1
    # ip ospf message-digest-key 10 md5 U2FsdGVkX1/Bq/+x8a3fsBo9ZrAX56ynmPKnRM87kfQ= encrypted 10.19.119.1
    # !
    # sonic#


    # Using "overridden" state

    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    # ip ospf area 2.2.2.2
    # ip ospf bfd
    # ip ospf bfd profile profile1
    # ip ospf cost 20
    # ip ospf dead-interval 40
    # ip ospf hello-interval 10
    # ip ospf mtu-ignore
    # ip ospf network broadcast
    # ip ospf priority 20
    # ip ospf authentication message-digest 10.10.120.1
    # ip ospf authentication-key U2FsdGVkX1+ozJSEI69XJb2KR9Pu1Sa3Ou6ujTRalbQ= encrypted 10.10.120.1
    # ip ospf dead-interval minimal hello-multiplier 5 10.10.120.1
    # !
    # interface Eth1/2
    # !
    # interface Eth1/3
    # ip ospf bfd
    # ip ospf network point-to-point
    # ip ospf area 3.3.3.3 10.19.120.2
    # ip ospf authentication message-digest 10.19.120.2
    # ip ospf authentication-key U2FsdGVkX19HqGCcf2pzGur9MDnb0VzLNRvoFij3Os0= encrypted 10.19.120.2
    # ip ospf dead-interval minimal hello-multiplier 5 10.19.120.2
    # !
    # sonic#

    - name: Override the OSPFv2_interface configurations
      sonic_ospfv2_interfaces:
        config:
          - name: 'Eth1/3'
            ospf_attributes:
              - area_id: '2.2.2.2'
                cost: 30
                priority: 20
                hello_interval: 10
                dead_interval: 40
                mtu_ignore: true
              - address: '10.10.120.1'
                authentication_type: 'NONE'
                authentication:
                  password: 'pass2'
              - address: '10.19.119.1'
                authentication_type: 'NONE'
                md_authentication:
                  - key_id: 10
                    md5key: 'U2FsdGVkX1/Bq/+x8a3fsBo9ZrAX56ynmPKnRM87kfQ='
                    encrypted: true
            bfd:
              enable: true
              bfd_profile: 'profile2'
            network: broadcast
        state: overridden

    # After state:
    # ------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    # !
    # interface Eth1/2
    # !
    # interface Eth1/3
    # ip ospf area 2.2.2.2
    # ip ospf bfd
    # ip ospf bfd profile profile2
    # ip ospf cost 30
    # ip ospf dead-interval 40
    # ip ospf hello-interval 10
    # ip ospf mtu-ignore
    # ip ospf network broadcast
    # ip ospf priority 20
    # ip ospf authentication null 10.10.120.1
    # ip ospf authentication-key U2FsdGVkX186k2R2hUXaDloW8hfkApn5Zx5hCQy9usc= encrypted 10.10.120.1
    # ip ospf authentication null 10.19.119.1
    # ip ospf message-digest-key 10 md5 U2FsdGVkX1/Bq/+x8a3fsBo9ZrAX56ynmPKnRM87kfQ= encrypted 10.19.119.1
    # !
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
                            <div>The resulting configuration model invocation.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format
     of the parameters above.</div>
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
                            <div>The generated configuration model invocation.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format
     of the parameters above.</div>
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
                            <div>The configuration prior to the model invocation.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format
     of the parameters above.</div>
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

- Santhosh kumar T (@santhosh-kt)
