.. _dellemc.enterprise_sonic.sonic_api_module:


**********************************
dellemc.enterprise_sonic.sonic_api
**********************************

**Manages REST operations on devices running Enterprise SONiC**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Manages REST operations on devices running Enterprise SONiC Distribution by Dell Technologies. This module provides an implementation for working with SONiC REST operations in a deterministic way.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>body</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">raw</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The body of the HTTP request/response to the web service which contains the payload.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>method</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>GET</li>
                                    <li>PUT</li>
                                    <li>POST</li>
                                    <li>PATCH</li>
                                    <li>DELETE</li>
                        </ul>
                </td>
                <td>
                        <div>The HTTP method of the request or response. Must be a valid method accepted by the service that handles the request.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>status_code</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=integer</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A list of valid, numeric, HTTP status codes that signifies the success of a request.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>url</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">path</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The HTTP path of the request after &#x27;restconf/&#x27;.</div>
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

    - name: Checks that you can connect (GET) to a page and it returns a status 200
      dellemc.enterprise_sonic.sonic_api:
        url: data/openconfig-interfaces:interfaces/interface=Ethernet60
        method: "GET"
        status_code: 200

    - name: Appends data to an existing interface using PATCH and verifies if it returns status 204
      dellemc.enterprise_sonic.sonic_api:
        url: data/openconfig-interfaces:interfaces/interface=Ethernet60/config/description
        method: "PATCH"
        body: {"openconfig-interfaces:description": "Eth-60"}
        status_code: 204

    - name: Deletes an associated IP address using DELETE and verifies if it returns status 204
      dellemc.enterprise_sonic.sonic_api:
        url: >
          data/openconfig-interfaces:interfaces/interface=Ethernet64/subinterfaces/subinterface=0/
          openconfig-if-ip:ipv4/addresses/address=1.1.1.1/config/prefix-length
        method: "DELETE"
        status_code: 204

    - name: Adds a VLAN network instance using PUT and verifies if it returns status 204
      dellemc.enterprise_sonic.sonic_api:
        url: data/openconfig-network-instance:network-instances/network-instance=Vlan100/
        method: "PUT"
        body: {"openconfig-network-instance:network-instance": [{"name": "Vlan100", "config": {"name": "Vlan100"}}]}
        status_code: 204

    - name: Adds a prefix-set to a routing policy using POST and verifies if it returns 201
      dellemc.enterprise_sonic.sonic_api:
        url: data/openconfig-routing-policy:routing-policy/defined-sets/prefix-sets/prefix-set=p1
        method: "POST"
        body: {"openconfig-routing-policy:config": {"name": "p1", "mode": "IPV4" }}
        status_code: 201



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
                    <b>msg</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                    </div>
                </td>
                <td>HTTP Error</td>
                <td>
                            <div>The HTTP error message from the request.</div>
                    <br/>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>response</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The response at the network device end for the REST call which contains the status code.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;response&#x27;: [204, {&#x27;&#x27;: None}]}</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Abirami N (@abirami-n)
