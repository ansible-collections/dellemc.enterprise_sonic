.. _dellemc.enterprise_sonic.sonic_config_module:


*************************************
dellemc.enterprise_sonic.sonic_config
*************************************

**Manages configuration sections on devices running Enterprise SONiC**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Manages configuration sections of Enterprise SONiC Distribution by Dell Technologies. SONiC configurations use a simple block indent file syntax for segmenting configuration into sections. This module provides an implementation for working with SONiC configuration sections in a deterministic way.




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
                    <b>after</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The ordered set of commands to append to the end of the command stack if a change needs to be made. Just like with <em>before</em>, this allows the playbook designer to append a set of commands to be executed after the command set.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>backup</b>
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
                        <div>This argument causes the module to create a full backup of the current <code>running-configuration</code> from the remote device before any changes are made. If the <code>backup_options</code> value is not given, the backup file is written to the <code>backup</code> folder in the playbook root directory. If the directory does not exist, it is created.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>backup_options</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>This is a dictionary object containing configurable options related to backup file path. The value of this option is read only when <code>backup</code> is set to <em>yes</em>, if <code>backup</code> is set to <em>no</em> this option is ignored.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dir_path</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">path</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>This option provides the path ending with directory name in which the backup configuration file is stored. If the directory does not exist it is first created, and the filename is either the value of <code>filename</code> or default filename as described in <code>filename</code> options description. If the path value is not given, an <em>backup</em> directory is created in the current working directory and backup configuration is copied in <code>filename</code> within the <em>backup</em> directory.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>filename</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The filename to be used to store the backup configuration. If the filename is not given, it is generated based on the hostname, current time, and date in the format defined by &lt;hostname&gt;_config.&lt;current-date&gt;@&lt;current-time&gt;.</div>
                </td>
            </tr>

            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>before</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The ordered set of commands to push on to the command stack if a change needs to be made. This allows the playbook designer the opportunity to perform configuration commands prior to pushing any changes without affecting how the set of commands are matched against the system.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>config</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The module, by default, connects to the remote device and retrieves the current running-configuration to use as a base for comparing against the contents of source. There are times when it is not desirable to have the task get the current running-configuration for every task in a playbook. The <em>config</em> argument allows the implementer to pass in the configuration to use as the base configuration for comparison.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>lines</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The ordered set of commands that should be configured in the section. The commands must be the exact same commands as found in the device running-configuration. Be sure to note the configuration command syntax as some commands are automatically modified by the device configuration parser. This argument is mutually exclusive with <em>src</em>.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: commands</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>match</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>line</b>&nbsp;&larr;</div></li>
                                    <li>strict</li>
                                    <li>exact</li>
                                    <li>none</li>
                        </ul>
                </td>
                <td>
                        <div>Instructs the module on the way to perform the matching of the set of commands against the current device configuration. If match is set to <em>line</em>, commands are matched line by line. If match is set to <em>strict</em>, command lines are matched with respect to position. If match is set to <em>exact</em>, command lines must be an equal match. If match is set to <em>none</em>, the module does not attempt to compare the source configuration with the running-configuration on the remote device.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>parents</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The ordered set of parents that uniquely identify the section or hierarchy the commands should be checked against. If the parents argument is omitted, the commands are checked against the set of top level or global commands.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>replace</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>line</b>&nbsp;&larr;</div></li>
                                    <li>block</li>
                        </ul>
                </td>
                <td>
                        <div>Instructs the module how to perform a configuration on the device. If the replace argument is set to <em>line</em>, then the modified lines are pushed to the device in configuration mode. If the replace argument is set to <em>block</em>, then the entire command block is pushed to the device in configuration mode if any line is not correct.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>save</b>
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
                        <b>Default:</b><br/><div style="color: blue">"false"</div>
                </td>
                <td>
                        <div>The <code>save</code> argument instructs the module to save the running- configuration to the startup-configuration at the conclusion of the module running. If check mode is specified, this argument is ignored.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>src</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">path</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the source path to the file that contains the configuration or configuration template to load. The path to the source file can either be the full path on the Ansible control host, or a relative path from the playbook or role root directory. This argument is mutually exclusive with <em>lines</em>.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>update</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>merge</b>&nbsp;&larr;</div></li>
                                    <li>check</li>
                        </ul>
                </td>
                <td>
                        <div>The <em>update</em> argument controls how the configuration statements are processed on the remote device. Valid choices for the <em>update</em> argument are <em>merge</em> and <em>check</em>. When you set this argument to <em>merge</em>, the configuration changes merge with the current device running-configuration. When you set this argument to <em>check</em>, the configuration updates are determined but not configured on the remote device.</div>
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

    - dellemc.enterprise_sonic.sonic_config:
        lines: ['username {{ user_name }} password {{ user_password }} role {{ user_role }}']

    - dellemc.enterprise_sonic.sonic_config:
        lines:
          - description 'SONiC'
        parents: ['interface Eth1/10']

    - dellemc.enterprise_sonic.sonic_config:
        lines:
          - seq 2 permit udp any any
          - seq 3 deny icmp any any
        parents: ['ip access-list test']
        before: ['no ip access-list test']



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
                    <b>commands</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The set of commands that is pushed to the remote device.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;username foo password foo role admin&#x27;, &#x27;router bgp 1&#x27;, &#x27;router-id 1.1.1.1&#x27;]</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>saved</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>When not check_mode.</td>
                <td>
                            <div>Returns whether the configuration is saved to the startup configuration or not.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>updates</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The set of commands that is pushed to the remote device.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;username foo password foo role admin&#x27;, &#x27;router bgp 1&#x27;, &#x27;router-id 1.1.1.1&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Abirami N (@abirami-n)
