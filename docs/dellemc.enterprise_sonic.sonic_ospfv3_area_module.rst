.. _dellemc.enterprise_sonic.sonic_ospfv3_area_module:


******************************************
dellemc.enterprise_sonic.sonic_ospfv3_area
******************************************

**Configure OSPFv3 area settings on SONiC.**


Version added: 3.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration for the area settings of OSPFv3 running on SONiC switches.
- Configure global/VRF OSPFv3 instance before configuring OSPFv3 areas.
- Configure OSPFv3 instance before configuring OSPFv3 areas.




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
                        <div>Specifies configuration for OSPFv3 areas.</div>
                        <div><em>stub</em> and <em>nssa</em> are mutually exclusive.</div>
                        <div>If <em>area_id=0 or 0.0.0.0</em>, <em>stub/nssa</em> should not be specified.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>area_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Area ID of the network (A.B.C.D or 0 to 4294967295).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>filter_list_in</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Inter-area prefix filter list.</div>
                        <div>Filter incoming prefixes into the area.</div>
                        <div>Expects name of a prefix list.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>filter_list_out</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Inter-area prefix filter list.</div>
                        <div>Filter outgoing prefixes from the area.</div>
                        <div>Expects name of a prefix list.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>nssa</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configuration for NSSA type area.</div>
                        <div><em>default_originate</em> and <em>no_summary</em> are mutually exclusive.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>default_originate</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Advertise default route for the NSSA area.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>enabled</b>
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
                        <div>Enable to advertise the default route for the NSSA area.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>metric</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure metric for the redistributed route (0 to 16777214).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>metric_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>1</li>
                                    <li>2</li>
                        </ul>
                </td>
                <td>
                        <div>Configure metric type for the redistributed route.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>enabled</b>
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
                        <div>Configure area as NSSA type area.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>no_summary</b>
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
                        <div>Disable inter-area route injection into the NSSA.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ranges</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure address range summarization on border routers.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>advertise</b>
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
                        <div>Enable address range advertising.</div>
                        <div>Default value while creating a new range is True.</div>
                        <div>If the <em>cost</em> is specified, <em>advertise</em> is unconditionally set to True during playbook execution.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
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
                        <div>Configure cost of address range (0 to 16777215).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>Configure address range prefix.</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ranges</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure address range summarization on border routers.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>advertise</b>
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
                        <div>Enable address range advertising.</div>
                        <div>Default value while creating a new range is True.</div>
                        <div>If the <em>cost</em> is specified, <em>advertise</em> is unconditionally set to True during playbook execution.</div>
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
                        <div>Configure cost of address range (0 to 16777215).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Configure address range prefix.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>stub</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configuration for STUB type area.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>enabled</b>
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
                        <div>Configure area as STUB type area.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>no_summary</b>
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
                        <div>Disable inter-area route injection into the STUB.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vrf_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of the VRF this area belongs to.</div>
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
                                    <li>replaced</li>
                                    <li>overridden</li>
                                    <li>deleted</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the type of configuration update to be performed on the device.</div>
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

    # Using "deleted" state
    #
    # Before state:
    # -------------
    # sonic(config-router-ospfv3)# show configuration
    # !
    # router ospfv3 vrf Vrf1
    #  area 0.0.0.1 stub no-summary
    #  area 0.0.0.1 filter-list prefix pf1 in
    #  area 0.0.0.1 filter-list prefix pf2 out
    #  area 0.0.0.2 stub no-summary
    #  area 0.0.0.1 range 1::1/64 not-advertise
    #  area 0.0.0.1 range 1::2/64
    #  area 0.0.0.2 range 1::1/64
    #  area 0.0.0.3 range 1::3/24 cost 14
    # sonic(config-router-ospfv3)#

    - name: "test delete all settings for areas"
      dellemc.enterprise_sonic.sonic_ospfv3_area:
        state: deleted
        config:
          - area_id: 0.0.0.1
            vrf_name: Vrf1
          - area_id: 0.0.0.2
            vrf_name: Vrf1
            ranges:
              - prefix: 1::1/64
                advertise: true
            stub:
              enabled: true
              no_summary: true

    # After state
    # -------------
    # sonic(config-router-ospfv3)# show configuration
    # !
    # router ospfv3 vrf Vrf1
    #  area 0.0.0.3 range 1::3/24 cost 14
    # sonic(config-router-ospfv3)#


    # Using "deleted" state
    # Before state:
    # -------------
    # sonic(config-router-ospfv3)# show configuration
    # !
    # router ospfv3 vrf Vrf1
    #  area 0.0.0.1 nssa no-summary
    #  area 0.0.0.3 filter-list prefix pf1 in
    #  area 0.0.0.1 nssa
    #  area 0.0.0.4 stub no-summary
    #  area 0.0.0.1 nssa range 1::1/64
    #  area 0.0.0.1 nssa range 1::2/64 cost 20
    #  area 0.0.0.2 range 1::1/64 not-advertise
    #  area 0.0.0.2 range 1::2/64 advertise cost 4
    #  area 0.0.0.2 range 1::3/24 not-advertise
    # sonic(config-router-ospfv3)#

    - name: "test clear subsections"
      dellemc.enterprise_sonic.sonic_ospfv3_area:
        state: deleted
        config:
          - area_id: 0.0.0.1
            vrf_name: Vrf1
            nssa:
              enabled: true
              ranges: []
          - area_id: 0.0.0.2
            vrf_name: Vrf1
            ranges: []
          - area_id: 4
            vrf_name: Vrf1

    # After state
    # -------------
    # sonic(config-router-ospfv3)# show configuration
    # !
    # router ospfv3 vrf Vrf1
    #  area 0.0.0.1 nssa no-summary
    #  area 0.0.0.3 filter-list prefix pf1 in
    #  area 0.0.0.1 nssa
    # sonic(config-router-ospfv3)#


    # Using "deleted" state
    # Before state:
    # -------------
    # sonic# show running-configuration ospfv3
    # !
    # router ospfv3 vrf Vrf1
    #  area 0.0.0.1 nssa no-summary
    #  area 0.0.0.1 filter-list prefix pf1 in
    #  area 0.0.0.1 filter-list prefix pf2 out
    #  area 0.0.0.3 filter-list prefix pf1 in
    #  area 0.0.0.1 nssa
    #  area 0.0.0.4 stub no-summary
    #  area 0.0.0.1 nssa range 1::1/64
    #  area 0.0.0.1 nssa range 1::2/64 cost 20
    #  area 0.0.0.2 range 1::1/64 not-advertise
    #  area 0.0.0.2 range 1::2/64 advertise cost 4
    #  area 0.0.0.2 range 1::3/24 not-advertise
    # router ospfv3
    #  area 0.0.0.1 nssa no-summary
    #  area 0.0.0.1 filter-list prefix pf1 in
    #  area 0.0.0.1 filter-list prefix pf2 out
    #  area 0.0.0.3 filter-list prefix pf1 in
    #  area 0.0.0.1 nssa
    #  area 0.0.0.4 stub no-summary
    #  area 0.0.0.1 nssa range 1::1/64
    #  area 0.0.0.1 nssa range 1::2/64 cost 20
    #  area 0.0.0.2 range 1::1/64 not-advertise
    #  area 0.0.0.2 range 1::2/64 advertise cost 4
    #  area 0.0.0.2 range 1::3/24 not-advertise
    # sonic#

    - name: "test clear subsections"
      dellemc.enterprise_sonic.sonic_ospfv3_area:
        state: deleted
        config:
          - area_id: 0.0.0.1
            vrf_name: Vrf1
            filter_list_in: pf1
            filter_list_out: pf2
            nssa:
              enabled: true
              range:
                - prefix: 1::2/64
                  advertise: true
                  cost: 20
          - area_id: 0.0.0.2
            vrf_name: Vrf1
            range:
              - prefix: 1::2/64
          - area_id: 3
            vrf_name: default
          - area_id: 4
            vrf_name: default
            stub:
              enabled: true
              no_summary: true

    # After state
    # -------------
    # sonic# show running-configuration ospfv3
    # !
    # router ospfv3 vrf Vrf1
    #  area 0.0.0.1 nssa no-summary
    #  area 0.0.0.3 filter-list prefix pf1 in
    #  area 0.0.0.1 nssa
    #  area 0.0.0.4 stub no-summary
    #  area 0.0.0.1 nssa range 1::1/64
    #  area 0.0.0.2 range 1::1/64 not-advertise
    #  area 0.0.0.2 range 1::3/24 not-advertise
    # router ospfv3
    #  area 0.0.0.1 nssa no-summary
    #  area 0.0.0.1 filter-list prefix pf1 in
    #  area 0.0.0.1 filter-list prefix pf2 out
    #  area 0.0.0.1 nssa
    #  area 0.0.0.4
    #  area 0.0.0.1 nssa range 1::1/64
    #  area 0.0.0.1 nssa range 1::2/64 cost 20
    #  area 0.0.0.2 range 1::1/64 not-advertise
    #  area 0.0.0.2 range 1::2/64 advertise cost 4
    #  area 0.0.0.2 range 1::3/24 not-advertise
    # sonic#


    # Using "merged" state
    # Before state:
    # -------------
    # sonic# show running-configuration ospfv3
    # !
    # router ospfv3 vrf Vrf2
    # !
    # router ospfv3 vrf Vrf1
    # sonic#

    - name: merge examples of all settings
      dellemc.enterprise_sonic.sonic_ospfv3_area:
        state: merged
        config:
          - area_id: 1
            vrf_name: Vrf1
          - area_id: 2
            vrf_name: Vrf1
            stub:
              enabled: true
              no_summary: true
          - area_id: 3
            vrf_name: Vrf1
            filter_list_in: pf1
            filter_list_out: pf2
            ranges:
              - prefix: 1::1/64
              - prefix: 1::2/64
                advertise: true
                cost: 4
              - prefix: 1::3/24
                advertise: false
              - prefix: 1::4/24
                advertise: true
                cost: 10
          - area_id: 4
            vrf_name: Vrf1
          - area_id: 5
            vrf_name: Vrf2

    # After state
    # -------------
    # sonic# show running-configuration ospfv3
    #
    # outer ospfv3 vrf Vrf1
    # area 0.0.0.1
    # area 0.0.0.2 stub no-summary
    # area 0.0.0.3 filter-list prefix pf1 in
    # area 0.0.0.3 filter-list prefix pf2 out
    # area 0.0.0.4
    # area 0.0.0.3 range 1::1/64
    # area 0.0.0.3 range 1::2/64 advertise cost 4
    # area 0.0.0.3 range 1::3/24 not-advertise
    # area 0.0.0.3 range 1::4/24 advertise cost 10
    # !
    # router ospfv3 vrf Vrf2
    #  area 0.0.0.5
    # sonic#


    # Using "merged" state
    # Before state:
    # -------------
    # sonic(config-router-ospfv3)# show configuration
    # !
    # router ospfv3 vrf Vrf2
    # sonic(config-router-ospfv3)# show configuration
    # !
    # router ospfv3 vrf Vrf1
    # sonic(config-router-ospfv3)#

    - name: merge smallest group of settings
      dellemc.enterprise_sonic.sonic_ospfv3_area:
        state: merged
        config:
          - area_id: 0.0.0.1
            vrf_name: Vrf1
          - area_id: 0.0.0.2
            vrf_name: Vrf1
            nssa:
              enabled: true
              no_summary: true
          - area_id: 0.0.0.3
            vrf_name: Vrf1
            ranges:
              - prefix: 1::1/64
            nssa:
              enabled: true
              default_originate:
                enabled: true
          - area_id: 0.0.0.4
            vrf_name: Vrf2
            stub:
              enabled: true
          - area_id: 0.0.0.5
            vrf_name: Vrf2
            filter_list_in: pf1
            filter_list_out: pf2

    # After state
    # -------------
    # sonic(config-router-ospfv3)# show configuration
    # !
    # router ospfv3 vrf Vrf1
    #  area 0.0.0.1
    #  area 0.0.0.2 nssa no-summary
    #  area 0.0.0.3 range 1::1/64
    #  area 0.0.0.3 nssa default-information-originate
    # sonic(config-router-ospfv3)# router ospfv3 vrf Vrf2
    # sonic(config-router-ospfv3)# show configuration
    # !
    # router ospfv3 vrf Vrf2
    #  area 0.0.0.4 stub
    #  area 0.0.0.5 filter-list prefix pf1 in
    #  area 0.0.0.5 filter-list prefix pf2 out
    # sonic(config-router-ospfv3)#


    # Using "merged" state
    # Before state:
    # -------------
    # sonic(config-router-ospfv3)# show configuration
    # !
    # router ospfv3 vrf Vrf1
    #  area 0.0.0.1 stub no-summary
    #  area 0.0.0.1 filter-list prefix pf1 in
    #  area 0.0.0.1 filter-list prefix pf2 out
    #  area 0.0.0.1 range 1::1/64 not-advertise
    #  area 0.0.0.1 range 1::2/64 advertise
    # sonic(config-router-ospfv3)#

    - name: "test merge all settings"
      dellemc.enterprise_sonic.sonic_ospfv3_area:
        state: merged
        config:
          - area_id: 0.0.0.1
            vrf_name: Vrf1
            filter_list_in: pf2
            filter_list_out: pf1
            ranges:
              - prefix: 1::1/64
                advertise: true
                cost: 12
              - prefix: 1::2/64
                advertise: false
            stub:
              enabled: true
              no_summary: false

    # After state
    # -------------
    # sonic(config-router-ospfv3)# show configuration
    # !
    # router ospfv3 vrf Vrf1
    #  area 0.0.0.1 stub
    #  area 0.0.0.1 filter-list prefix pf2 in
    #  area 0.0.0.1 filter-list prefix pf1 out
    #  area 0.0.0.1 range 1::1/64 advertise cost 12
    #  area 0.0.0.1 range 1::2/64 not-advertise
    # sonic(config-router-ospfv3)#


    # Using "replaced" state
    # Before state:
    # -------------
    # sonic# show running-configuration ospfv3
    # !
    # router ospfv3 vrf Vrf1
    #  area 0.0.0.1 nssa no-summary
    #  area 0.0.0.1 filter-list prefix pf1 in
    #  area 0.0.0.1 filter-list prefix pf2 out
    #  area 0.0.0.3 filter-list prefix pf1 in
    #  area 0.0.0.1 nssa
    #  area 0.0.0.4 stub no-summary
    #  area 0.0.0.1 nssa range 1::1/64
    #  area 0.0.0.1 nssa range 1::2/64 cost 20
    #  area 0.0.0.2 range 1::1/64 not-advertise
    #  area 0.0.0.2 range 1::2/64 advertise cost 4
    #  area 0.0.0.2 range 1::3/24 not-advertise
    # router ospfv3
    #  area 0.0.0.1 nssa no-summary
    #  area 0.0.0.1 filter-list prefix pf1 in
    #  area 0.0.0.1 filter-list prefix pf2 out
    #  area 0.0.0.3 filter-list prefix pf1 in
    #  area 0.0.0.1 nssa
    #  area 0.0.0.4 stub no-summary
    #  area 0.0.0.1 nssa range 1::1/64
    #  area 0.0.0.1 nssa range 1::2/64 cost 20
    #  area 0.0.0.2 range 1::1/64 not-advertise
    #  area 0.0.0.2 range 1::2/64 advertise cost 4
    #  area 0.0.0.2 range 1::3/24 not-advertise
    # sonic#

    - name: "replace areas"
      dellemc.enterprise_sonic.sonic_ospfv3_area:
        state: replaced
        config:
          - area_id: 0.0.0.1
            vrf_name: Vrf1
          - area_id: 0.0.0.5
            vrf_name: Vrf1
            nssa:
              enabled: true
              default_originate:
                enabled: true
                metric: 10
                metric_type: 1
              ranges:
                - prefix: "1::1/64"
                  cost: 15
          - area_id: 0.0.0.4
            vrf_name: Vrf1
            stub:
              no_summary: true
              enabled: true

    # After state
    # -------------
    # sonic# show running-configuration ospfv3
    # !
    # router ospfv3 vrf Vrf1
    #  area 0.0.0.1
    #  area 0.0.0.4 stub no-summary
    #  area 0.0.0.5 nssa nssa default-information-originate metric 10 metric-type 1
    #  area 0.0.0.5 nssa range 1::1/64 cost 15
    # router ospfv3
    #  area 0.0.0.1 nssa no-summary
    #  area 0.0.0.1 filter-list prefix pf1 in
    #  area 0.0.0.1 filter-list prefix pf2 out
    #  area 0.0.0.3 filter-list prefix pf1 in
    #  area 0.0.0.1 nssa
    #  area 0.0.0.4 stub no-summary
    #  area 0.0.0.1 nssa range 1::1/64
    #  area 0.0.0.1 nssa range 1::2/64 cost 20
    #  area 0.0.0.2 range 1::1/64 not-advertise
    #  area 0.0.0.2 range 1::2/64 advertise cost 4
    #  area 0.0.0.2 range 1::3/24 not-advertise
    # sonic#


    # Using "overridden" state
    # Before state:
    # -------------
    # sonic# show running-configuration ospfv3
    # !
    # router ospfv3 vrf Vrf1
    #  area 0.0.0.1 nssa no-summary
    #  area 0.0.0.1 filter-list prefix pf1 in
    #  area 0.0.0.1 filter-list prefix pf2 out
    #  area 0.0.0.3 filter-list prefix pf1 in
    #  area 0.0.0.1 nssa
    #  area 0.0.0.4 stub no-summary
    #  area 0.0.0.1 nssa range 1::1/64
    #  area 0.0.0.1 nssa range 1::2/64 cost 20
    #  area 0.0.0.2 range 1::1/64 not-advertise
    #  area 0.0.0.2 range 1::2/64 advertise cost 4
    #  area 0.0.0.2 range 1::3/24 not-advertise
    # router ospfv3
    #  area 0.0.0.1 nssa no-summary
    #  area 0.0.0.1 filter-list prefix pf1 in
    #  area 0.0.0.1 filter-list prefix pf2 out
    #  area 0.0.0.3 filter-list prefix pf1 in
    #  area 0.0.0.1 nssa
    #  area 0.0.0.4 stub no-summary
    #  area 0.0.0.1 nssa range 1::1/64
    #  area 0.0.0.1 nssa range 1::2/64 cost 20
    #  area 0.0.0.2 range 1::1/64 not-advertise
    #  area 0.0.0.2 range 1::2/64 advertise cost 4
    #  area 0.0.0.2 range 1::3/24 not-advertise
    # sonic#

    - name: "override areas"
      dellemc.enterprise_sonic.sonic_ospfv3_area:
        state: overridden
        config:
          - area_id: 0.0.0.1
            vrf_name: Vrf1
          - area_id: 0.0.0.5
            vrf_name: Vrf1
            nssa:
              enabled: true
              default_originate:
                enabled: true
                metric: 10
                metric_type: 1
              ranges:
                - prefix: "1::1/64"
                  cost: 15
          - area_id: 0.0.0.4
            vrf_name: Vrf1
            stub:
              no_summary: true
              enabled: true

    # After state
    # -------------
    # sonic# show running-configuration ospfv3
    # !
    # router ospfv3 vrf Vrf1
    #  area 0.0.0.1
    #  area 0.0.0.4 stub no-summary
    #  area 0.0.0.5 nssa nssa default-information-originate metric 10 metric-type 1
    #  area 0.0.0.5 nssa range 1::1/64 cost 15
    # router ospfv3
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
                            <div>The configuration resulting from model invocation.</div>
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
                            <div>The generated (calculated) configuration that would be applied by module invocation.</div>
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
                            <div>The configuration prior to the module invocation.</div>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[{&#x27;config&#x27;: &#x27;...&#x27;, &#x27;state&#x27;: &#x27;...&#x27;}, {&#x27;config&#x27;: &#x27;...&#x27;, &#x27;state&#x27;: &#x27;...&#x27;}]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Santhosh kumar T (@santhosh-kt)
