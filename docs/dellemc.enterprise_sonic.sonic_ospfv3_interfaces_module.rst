.. _dellemc.enterprise_sonic.sonic_ospfv3_interfaces_module:


************************************************
dellemc.enterprise_sonic.sonic_ospfv3_interfaces
************************************************

**Configure OSPFv3 interface mode protocol settings on SONiC.**


Version added: 3.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration management of OSPFv3 interface mode parameters on devices running SONiC.
- Configure VRF instance before configuring OSPFv3 in a VRF.
- Configure global/VRF OSPFv3 instance before configuring OSPFv3 in interfaces.




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
                        <div>Specifies the OSPFv3 interface mode related configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>advertise</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Enable OSPFv3 interface advertise.</div>
                        <div>expects name of a prefix list.</div>
                </td>
            </tr>
            <tr>
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
                        <div>OSPFv3 Area ID of the network (A.B.C.D or 0 to 4294967295).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Configure OSPFv3 interface BFD.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
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
                <td colspan="1">
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
                        <div>Enable BFD support for OSPFv3.</div>
                </td>
            </tr>

            <tr>
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
                        <div>Configure OSPFv3 interface cost (1 to 65535).</div>
                </td>
            </tr>
            <tr>
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
                        <div>Configure OSPFv3 adjacency dead interval (1 to 65535).</div>
                </td>
            </tr>
            <tr>
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
                        <div>Configure OSPFv3 neighbour hello interval (1 to 65535).</div>
                </td>
            </tr>
            <tr>
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
                        <div>Disable OSPFv3 MTU mismatch detection.</div>
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
                        <div>Full name of the interface, i.e. Ethernet1.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Configure OSPFv3 interface network type</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>passive</b>
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
                        <div>Configure ospfv3 interface as passive.</div>
                </td>
            </tr>
            <tr>
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
                        <div>Configure OSPFv3 adjacency router priority (0 to 255).</div>
                </td>
            </tr>
            <tr>
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
                        <div>Configure OSPFv3 retransmit interval (2 to 65535).</div>
                </td>
            </tr>
            <tr>
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
                        <div>Configure OSPFv3 transmit delay (1 to 65535).</div>
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
                        <div>Specifies the operation to be performed on the OSPFv3 interfaces configured on the device.</div>
                        <div>In case of merged, the input configuration will be merged with the existing OSPFv3 interfaces configuration on the device.</div>
                        <div>In case of deleted, the specified existing OSPFv3 interfaces configuration will be removed from the device.</div>
                        <div>In case of overridden, all the existing OSPFv3 interfaces configuration will be deleted and the specified input configuration will be installed.</div>
                        <div>In case of replaced, the existing OSPFv3 interface configuration on the device will be replaced by the configuration in the playbook for each interface group configured by the playbook.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - Supports ``check_mode``.
   - Tested against Enterprise SONiC Distribution by Dell Technologies.



Examples
--------

.. code-block:: yaml

    # Using deleted

    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    # ipv6 ospfv3 advertise prefix-list test1
    # ipv6 ospfv3 area 2.2.2.2
    # ipv6 ospfv3 bfd
    # ipv6 ospfv3 bfd profile profile2
    # ipv6 ospfv3 cost 30
    # ipv6 ospfv3 dead-interval 40
    # ipv6 ospfv3 hello-interval 10
    # ipv6 ospfv3 mtu-ignore
    # ipv6 ospfv3 network point-to-point
    # ipv6 ospfv3 priority 20
    # ipv6 ospfv3 passive
    # !
    # interface Eth1/2
    # ipv6 ospfv3 bfd
    # ipv6 ospfv3 network point-to-point
    # !
    # interface Eth1/3
    # ipv6 ospfv3 bfd
    # ipv6 ospfv3 network point-to-point
    # ipv6 ospfv3 area 3.3.3.3
    # !
    # sonic#

    - name: Delete the specified OSPFv3_interface configurations
      sonic_ospfv3_interfaces:
        config:
          - name: 'Eth1/1'
            area_id: '2.2.2.2'
            cost: 30
            priority: 20
            hello_interval: 10
            dead_interval: 40
            mtu_ignore: true
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
    # ipv6 ospfv3 advertise prefix-list test1
    # ipv6 ospfv3 passive
    # !
    # interface Eth1/2
    # ipv6 ospfv3 network point-to-point
    # !
    # interface Eth1/3
    # !
    # sonic#


    # Using deleted

    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    # ipv6 ospfv3 advertise prefix-list test1
    # ipv6 ospfv3 area 2.2.2.2
    # ipv6 ospfv3 bfd
    # ipv6 ospfv3 bfd profile profile2
    # ipv6 ospfv3 cost 30
    # ipv6 ospfv3 dead-interval 40
    # ipv6 ospfv3 hello-interval 10
    # ipv6 ospfv3 mtu-ignore
    # ipv6 ospfv3 network point-to-point
    # ipv6 ospfv3 priority 20
    # ipv6 ospfv3 passive
    # !
    # interface Eth1/2
    # ipv6 ospfv3 bfd
    # ipv6 ospfv3 network point-to-point
    # !
    # interface Eth1/3
    # ipv6 ospfv3 bfd
    # ipv6 ospfv3 network point-to-point
    # ipv6 ospfv3 area 3.3.3.3
    # !
    # sonic#

    - name: Delete the specified OSPFv3_interface configurations
      sonic_ospfv3_interfaces:
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
    # ipv6 ospfv3 network point-to-point
    # !
    # interface Eth1/3
    # !
    # sonic#


    # Using merged

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

    - name: Add the OSPFv3_interface configurations
      sonic_ospfv3_interfaces:
        config:
          - name: 'Eth1/1'
            advertise: 'test1'
            area_id: '2.2.2.2'
            cost: 20
            passive: true
            priority: 20
            hello_interval: 10
            dead_interval: 40
            mtu_ignore: true
            hello_multiplier: 5
            bfd:
              enable: true
              bfd_profile: 'profile1'
            network: broadcast
          - name: 'Eth1/3'
            area_id: '3.3.3.3'
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
    # ipv6 ospfv3 advertise prefix-list test1
    # ipv6 ospfv3 area 2.2.2.2
    # ipv6 ospfv3 bfd
    # ipv6 ospfv3 bfd profile profile1
    # ipv6 ospfv3 cost 20
    # ipv6 ospfv3 dead-interval 40
    # ipv6 ospfv3 hello-interval 10
    # ipv6 ospfv3 mtu-ignore
    # ipv6 ospfv3 network broadcast
    # ipv6 ospfv3 passive
    # ipv6 ospfv3 priority 20
    # !
    # interface Eth1/2
    # !
    # interface Eth1/3
    # ipv6 ospfv3 bfd
    # ipv6 ospfv3 network point-to-point
    # ipv6 ospfv3 area 3.3.3.3
    # !
    # sonic#

    # Using merged

    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    # ipv6 ospfv3 advertise prefix-list test1
    # ipv6 ospfv3 area 2.2.2.2
    # ipv6 ospfv3 bfd
    # ipv6 ospfv3 bfd profile profile1
    # ipv6 ospfv3 cost 20
    # ipv6 ospfv3 dead-interval 40
    # ipv6 ospfv3 hello-interval 10
    # ipv6 ospfv3 mtu-ignore
    # ipv6 ospfv3 network broadcast
    # ipv6 ospfv3 priority 20
    # !
    # interface Eth1/2
    # !
    # interface Eth1/3
    # ipv6 ospfv3 bfd
    # ipv6 ospfv3 network point-to-point
    # ipv6 ospfv3 area 3.3.3.3
    # !
    # sonic#

    - name: Add the OSPFv3_interface configurations
      sonic_ospfv3_interfaces:
        config:
          - name: 'Eth1/1'
            area_id: '2.2.2.2'
            cost: 30
            passive: true
            priority: 20
            hello_interval: 10
            dead_interval: 40
            mtu_ignore: true
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
    # ipv6 ospfv3 advertise prefix-list test1
    # ipv6 ospfv3 area 2.2.2.2
    # ipv6 ospfv3 bfd
    # ipv6 ospfv3 bfd profile profile2
    # ipv6 ospfv3 cost 30
    # ipv6 ospfv3 dead-interval 40
    # ipv6 ospfv3 hello-interval 10
    # ipv6 ospfv3 mtu-ignore
    # ipv6 ospfv3 network point-to-point
    # ipv6 ospfv3 passive
    # ipv6 ospfv3 priority 20
    # !
    # interface Eth1/2
    # ipv6 ospfv3 bfd
    # ipv6 ospfv3 network point-to-point
    # !
    # interface Eth1/3
    # ipv6 ospfv3 bfd
    # ipv6 ospfv3 network point-to-point
    # ipv6 ospfv3 area 3.3.3.3
    # !
    # sonic#


    # Using replaced

    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    # ipv6 ospfv3 advertise prefix-list test1
    # ipv6 ospfv3 area 2.2.2.2
    # ipv6 ospfv3 bfd
    # ipv6 ospfv3 bfd profile profile1
    # ipv6 ospfv3 cost 20
    # ipv6 ospfv3 dead-interval 40
    # ipv6 ospfv3 hello-interval 10
    # ipv6 ospfv3 mtu-ignore
    # ipv6 ospfv3 network broadcast
    # ipv6 ospfv3 passive
    # ipv6 ospfv3 priority 20
    # !
    # interface Eth1/2
    # !
    # interface Eth1/3
    # ipv6 ospfv3 bfd
    # ipv6 ospfv3 network point-to-point
    # ipv6 ospfv3 area 3.3.3.3
    # !
    # sonic#


    - name: Replace the OSPFv3_interface configurations
      sonic_ospfv3_interfaces:
        config:
          - name: 'Eth1/3'
            area_id: '2.2.2.2'
            cost: 30
            passive: true
            priority: 20
            hello_interval: 10
            dead_interval: 40
            mtu_ignore: true
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
    # ipv6 ospfv3 advertise prefix-list test1
    # ipv6 ospfv3 area 2.2.2.2
    # ipv6 ospfv3 bfd
    # ipv6 ospfv3 bfd profile profile1
    # ipv6 ospfv3 cost 20
    # ipv6 ospfv3 dead-interval 40
    # ipv6 ospfv3 hello-interval 10
    # ipv6 ospfv3 mtu-ignore
    # ipv6 ospfv3 network broadcast
    # ipv6 ospfv3 passive
    # ipv6 ospfv3 priority 20
    # !
    # interface Eth1/2
    # !
    # interface Eth1/3
    # ipv6 ospfv3 area 2.2.2.2
    # ipv6 ospfv3 bfd
    # ipv6 ospfv3 bfd profile profile2
    # ipv6 ospfv3 cost 30
    # ipv6 ospfv3 dead-interval 40
    # ipv6 ospfv3 hello-interval 10
    # ipv6 ospfv3 mtu-ignore
    # ipv6 ospfv3 network broadcast
    # ipv6 ospfv3 passive
    # ipv6 ospfv3 priority 20
    # !
    # sonic#


    # Using overridden

    # Before state:
    # -------------
    #
    # sonic# show running-configuration interface
    # !
    # interface Eth1/1
    # ipv6 ospfv3 area 2.2.2.2
    # ipv6 ospfv3 bfd
    # ipv6 ospfv3 bfd profile profile1
    # ipv6 ospfv3 cost 20
    # ipv6 ospfv3 dead-interval 40
    # ipv6 ospfv3 hello-interval 10
    # ipv6 ospfv3 mtu-ignore
    # ipv6 ospfv3 network broadcast
    # ipv6 ospfv3 priority 20
    # !
    # interface Eth1/2
    # !
    # interface Eth1/3
    # ipv6 ospfv3 bfd
    # ipv6 ospfv3 network point-to-point
    # ipv6 ospfv3 area 3.3.3.3
    # !
    # sonic#

    - name: Override the OSPFv3_interface configurations
      sonic_ospfv3_interfaces:
        config:
          - name: 'Eth1/3'
            advertise: 'test1'
            area_id: '2.2.2.2'
            cost: 30
            passive: true
            priority: 20
            hello_interval: 10
            dead_interval: 40
            mtu_ignore: true
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
    # ipv6 ospfv3 advertise prefix-list test1
    # ipv6 ospfv3 area 2.2.2.2
    # ipv6 ospfv3 bfd
    # ipv6 ospfv3 bfd profile profile2
    # ipv6 ospfv3 cost 30
    # ipv6 ospfv3 dead-interval 40
    # ipv6 ospfv3 hello-interval 10
    # ipv6 ospfv3 mtu-ignore
    # ipv6 ospfv3 network broadcast
    # ipv6 ospfv3 passive
    # ipv6 ospfv3 priority 20
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
                            <div>The configuration resulting from  module invocation.</div>
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
                            <div>The generated(calculated) configuration that would be applied by module invocation.</div>
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

- Mansi Jharia (@Mansi062001)
