.. _dellemc.enterprise_sonic.sonic_sflow_module:


************************************
dellemc.enterprise_sonic.sonic_sflow
************************************

**configure sflow settings on SONiC**


Version added: 2.5.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration for sflow sampling on devices running SONiC




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
                        <div>Defines configuration and operational state data related to data plane traffic sampling based on sflow.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>agent</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The Agent interface</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>collectors</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configuration data for sflow collectors.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IP address of the sflow collector.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>network_instance</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">"default"</div>
                </td>
                <td>
                        <div>name of the network instance containing the sflow collector</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>port</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">6343</div>
                </td>
                <td>
                        <div>UDP port number for the sflow collector.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Enables or disables sflow sampling for the device.</div>
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
                        <div>Configuration data for sflow data on interfaces.</div>
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
                        <div>If sflow is globally enabled, enables or disables sflow on the interface</div>
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
                    <b>sampling_rate</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Override the global sampling rate for this interface</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>max_header_size</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>sflow maximum header size in bytes.</div>
                        <div>must be in multiple of 128 bytes from 128 to 1024.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>polling_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>sflow polling interval (in seconds).</div>
                        <div>must be 0 or in range 5-300</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>sampling_rate</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Sets global packet sampling rate.</div>
                        <div>Sample 1 packet for every sampling_rate number of packets flowing through the interface</div>
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
                        <div>Specifies the type of configuration update to be performed on the device.</div>
                </td>
            </tr>
    </table>
    <br/>




Examples
--------

.. code-block:: yaml

    # Using "deleted" state to clear all configuration
    # Before state:
    # config:
    #   enabled: false
    #   polling_interval: 40
    #   max_header_size: 256
    #   collectors:
    #     - address: 1.1.1.1
    #       port: 6343
    #       network_instance: default
    #   interfaces:
    #     - name: Ethernet0
    #       sampling_rate: 400000

    # Example
    - name: "clear all sflow config and disable"
      sonic_sflow:
        config: {}
        state: deleted

    # After state:
    # Note, "enabled" can't be deleted. It's just set to default. All values that can be cleared are deleted.
    # config:
    #   enabled: false
    #   (no other recorded config)
    # ------

    # Using "deleted" state to clear just the interfaces and collectors
    # Before state:
    # config:
    #   enabled: True
    #   polling_interval: 40
    #   max_header_size: 256
    #   collectors:
    #     - address: 1.1.1.1
    #       port: 6343
    #       network_instance: default
    #   interfaces:
    #     - name: Ethernet0
    #       sampling_rate: 400000

    # Example
    - name: "clear all sflow interfaces and collectors"
      sonic_sflow:
        config:
          interfaces: []
          collectors: []
        state: deleted

    # After state:
    # config:
    #   enabled: true
    #   polling_interval: 40
    #   max_header_size: 256
    # Note: deletes list of items if empty list is provided. Otherwise must specify key and have values match to delete, see other Example
    # ------

    # Using "deleted" state to delete individual interfaces
    # Before state:
    # config:
    #   enabled: false
    #   polling_interval: 40
    #   max_header_size: 256
    #   collectors:
    #     - address: 1.1.1.1
    #       port: 6343
    #       network_instance: default
    #   interfaces:
    #     - name: Ethernet0
    #       sampling_rate: 400000
    #     - name: Ethernet8
    #       enabled: false
    #     - name: Ethernet16
    #       sampling_rate: 400000

    # Example
    # note: to delete the whole interface, just the name needs to specify the name, nothing else
    - name: "delete individual interfaces"
      sonic_sflow:
        config:
          interfaces:
            - name: Ethernet8
            - name: Ethernet16
      state: deleted

    # After state:
    # All configuration deleted for the listed interfaces
    # config:
    #   enabled: false
    #   polling_interval: 40
    #   max_header_size: 256
    #   collectors:
    #     - address: 1.1.1.1
    #       port: 6343
    #       network_instance: default
    #   interfaces:
    #     - name: Ethernet0
    #       sampling_rate: 400000
    # ------

    # Using "deleted" state to delete collectors
    # Before state:
    # config:
    #   enabled: false
    #   polling_interval: 40
    #   max_header_size: 256
    #   collectors:
    #     - address: 1.1.1.1
    #       port: 6343
    #       network_instance: default
    #     - address: 1.1.1.2
    #       port: 6000
    #       network_instance: "vrf_1"
    #   interfaces:
    #     - name: Ethernet0
    #       sampling_rate: 400000

    # Example:
    # Note: The values of all three fields must be known to identify a collector, but
    # the "port" and "network instance" attributes have default values. These default
    # values do not need to be explicitly specified in a playbook for deletion of a
    # collector having default values configured for these attributes.
    - name: "delete individual collectors"
      sonic_sflow:
        config:
          collectors:
            - address: 1.1.1.2
              port: 6000
              network_instance: "vrf_1"
            - address: 1.1.1.1
        state: deleted

    # After state:
    # config:
    #   enabled: false
    #   polling_interval: 40
    #   max_header_size: 256
    #   interfaces:
    #     - name: Ethernet0
    #       sampling_rate: 400000
    # ------

    # Using "deleted" state to clear individual values
    # Before state:
    # config:
    #   enabled: true
    #   polling_interval: 30
    #   max_header_size: 128
    #   sampling_rate: 400000
    #   collectors:
    #     - address: 1.1.1.1
    #       port: 6343
    #       network_instance: default
    #   interfaces:
    #     - name: Ethernet0
    #       enabled: true
    #       sampling_rate: 400000
    #     - name: Ethernet4
    #       enabled: true
    #       sampling_rate: 400002

    # Example
    - name: "clear specific config attributes if values match"
      sonic_sflow:
        config:
          enabled: false
          polling_interval: 30
          max_header_size: 128
          sampling_rate: 400000
          interfaces:
            - name: Ethernet0
              sampling_rate: 400000
        state: deleted

    # After state:
    # config:
    #   enabled: true
    #   collectors:
    #     - address: 1.1.1.1
    #       port: 6343
    #       network_instance: default
    #   interfaces:
    #     - name: Ethernet0
    #       enabled: true
    #     - name: Ethernet4
    #       enabled: true
    #       sampling_rate: 400002

    # ------------


    # Using "merged" state to add sflow collector
    # Before state:
    # config:
    #   enabled: false

    # Example:
    - name: "Add an sflow collector with default values for 'port' and 'network_instance"
      sonic_sflow:
        config:
          collectors:
            - address: 1.1.1.2
        state: merged
    # note: There can only be two collectors configured at a time.
    # note: Only "port" and and "network_instance" have default values.

    # After state:
    # config:
    #   enabled: false
    #   collectors:
    #     - address: 1.1.1.2
    #       port: 6343
    #       network_instance: default
    # ------

    # Using "merged" state to add and modify interface configuration
    # Before state:
    # config:
    #   enabled: false
    #   interfaces:
    #     - name: Ethernet0
    #       sampling_rate: 400002
    #     - name: Ethernet8
    #       enabled: true
    #       sampling_rate: 400001

    # Example
    - name: "Add/modify interface settings"
      sonic_sflow:
        config:
          interfaces:
            - name: Ethernet0
              enabled: true
            - name: Ethernet8
              enabled: false
              sampling_rate: 400003
            - name: Ethernet16
            - name: Ethernet32
              sampling_rate: 400001
        state: merged
    # Note: must set at least one of enabled or sampling_rate for interface to be added

    # After state
    # config:
    #   enabled: false
    #   interfaces:
    #     - name: Ethernet0
    #       sampling_rate: 400002
    #       enabled: true
    #     - name: Ethernet8
    #       enabled: false
    #       sampling_rate: 400003
    #     - name: Ethernet32
    #       sampling_rate: 400001
    # ------

    # Using "merged" state to add/modify global settings
    # Before state:
    # config:
    #   enabled: false
    #   polling_interval: 40
    #   max_header_size: 256

    # Example
    - name: "Adding/modifying other settings using 'merged'"
      sonic_sflow:
        config:
          polling_interval: 50
          enabled: true
          agent: Ethernet0
          max_header_size: 128
        state: merged

    # After state
    # config:
    #   enabled: true
    #   polling_interval: 50
    #   max_header_size: 128
    #   agent: Ethernet0

    # -----------


    # using overridden to override all existing sflow config with the given settings
    # Before state:
    # config:
    #   enabled: false
    #   polling_interval: 50
    #   max_header_size: 128
    #   collectors:
    #     - address: 1.1.1.1
    #       port: 6343
    #       network_instance: default
    #   interfaces:
    #     - name: Ethernet0
    #       enabled: false
    #     - name: Ethernet8
    #       enabled: false
    #     - name: Ethernet16
    #       enabled: false
    #     - name: Ethernet24
    #       enabled: false

    # Example:
    - name: "override all existing sflow config with input config from a playbook task"
      sonic_sflow:
        config:
          enabled: true
          agent: Ethernet0
          interfaces:
            - name: Ethernet0
              enabled: true
        state: overridden

    # After state:
    # config:
    #   enabled: true
    #   agent: Ethernet0
    #   interfaces:
    #     - name: Ethernet0
    #       enabled: true
    # ------------


    # Using "replaced" state to replace specific interface settings
    # Before state:
    # config:
    #   enabled: false
    #   polling_interval: 50
    #   max_header_size: 128
    #   collectors:
    #     - address: 1.1.1.1
    #       port: 6343
    #       network_instance: default
    #   interfaces:
    #     - name: Ethernet0
    #       enabled: true
    #       sampling_rate: 400002
    #     - name: Ethernet4
    #       enabled: false
    #     - name: Ethernet8
    #       enabled: false
    #       sampling_rate: 400010
    #     - name: Ethernet24
    #       enabled: false

    # Example:
    - name: "only add or substitute certain interfaces"
      sonic_sflow:
        config:
          enabled: false
          polling_interval: 50
          max_header_size: 128
          interfaces:
            - name: Ethernet0
              sampling_rate: 400010
            - name: Ethernet4
              sampling_rate: 400010
            - name: Ethernet16
              enabled: false
        state: replaced

    # After state:
    # config:
    #   enabled: false
    #   polling_interval: 50
    #   max_header_size: 128
    #   collectors:
    #     - address: 1.1.1.1
    #       port: 6343
    #       network_instance: default
    #   interfaces:
    #     - name: Ethernet0
    #       sampling_rate: 400010
    #     - name: Ethernet4
    #       sampling_rate: 400010
    #     - name: Ethernet8
    #       enabled: false
    #       sampling_rate: 400010
    #     - name: Ethernet16
    #       enabled: false
    #     - name: Ethernet24
    #       enabled: false
    # ------

    # Using "replaced" state with different top level values replaces nested components.
    # Before state:
    # config:
    #   enabled: false
    #   polling_interval: 50
    #   max_header_size: 128
    #   collectors:
    #     - address: 1.1.1.1
    #       port: 6343
    #       network_instance: default
    #   interfaces:
    #     - name: Ethernet0
    #       enabled: false
    #     - name: Ethernet8
    #       enabled: false
    #     - name: Ethernet16
    #       enabled: false
    #     - name: Ethernet24
    #       enabled: false

    # Example:
    - name: "replaces everything"
      sonic_sflow:
        config:
          enabled: false
          polling_interval: 30
          max_header_size: 128
        state: replaced

    # After state:
    # config:
    #   enabled: false
    #   polling_interval: 30
    #   max_header_size: 128
    # -----------



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
                            <div>The resulting configuration module invocation.</div>
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

- Xiao Han (@Xiao_Han2)
