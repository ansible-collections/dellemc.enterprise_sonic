.. _dellemc.enterprise_sonic.sonic_image_management_module:


***********************************************
dellemc.enterprise_sonic.sonic_image_management
***********************************************

**Manage installation of Enterprise SONiC image, software patch and firmware updater**


Version added: 2.4.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Manage installation of Enterprise SONiC image, software patch and firmware updater.




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
                    <b>firmware</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Manage installation of Firmware updater</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>command</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>install</li>
                                    <li>cancel</li>
                                    <li>get-list</li>
                                    <li>get-status</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the firmware updater manangement operation to be performed.</div>
                        <div><code>install</code> - Stage firmware updater specified by <em>path</em>.</div>
                        <div><code>cancel</code> - Cancel a pending firmware updater.</div>
                        <div><code>get-list</code> - Retrieve details of pending firmware updater and result of installed firmware updater.</div>
                        <div><code>get-status</code> - Retrieve firmware updater staging status.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>path</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>When <em>command=install</em>, specifies the path of the firmware updater to be staged.</div>
                        <div>Path can be a file in the device (file://filepath) or URL (http:// or https://).</div>
                </td>
            </tr>

            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>image</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Manage installation of Enterprise SONiC image.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>command</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>install</li>
                                    <li>cancel</li>
                                    <li>remove</li>
                                    <li>set-default</li>
                                    <li>get-list</li>
                                    <li>get-status</li>
                                    <li>gpg-key</li>
                                    <li>verify</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the image manangement operation to be performed.</div>
                        <div><code>install</code> - Install image specified by <em>path</em>.</div>
                        <div><code>cancel</code> - Cancel image installation.</div>
                        <div><code>remove</code> - Remove image specified by <em>name</em>.</div>
                        <div><code>set-default</code> - Set the image specified by <em>name</em> as default boot image.</div>
                        <div><code>get-list</code> - Retrieve list of installed images.</div>
                        <div><code>get-status</code> - Retrieve image installation status.</div>
                        <div><code>gpg-key</code> - Install GPG key.</div>
                        <div><code>verify</code> - Verify the image specified by <em>path</em> using GPG or PKI method.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>keyserver</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.0.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>GPG Key server URL.</div>
                        <div>Required when <em>command=gpg-key</em>.</div>
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
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>When <em>command=remove</em> or <em>command=set-default</em> specifies the name of the image.</div>
                        <div>When <em>command=remove</em>, name can be specified as <code>all</code> to remove all images which are not current or next.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>path</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>When <em>command=install</em> or <em>command=verify</em> specifies the path of the image to be installed.</div>
                        <div>Path can be a file in the device (file://filepath) or URL (http:// or https://).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>pubkeyfilename</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.0.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the certificate for signature file.</div>
                        <div>Required when <em>command=verify</em> and <em>verifymethod=pki</em>.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>pubkeyid</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.0.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>GPG Key ID to be installed.</div>
                        <div>Required when <em>command=gpg-key</em>.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>signaturefile</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.0.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>GPG/PKI file to be verified.</div>
                        <div>Required when <em>command=verify</em>.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>verifymethod</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 3.0.0</div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>gpg</li>
                                    <li>pki</li>
                        </ul>
                </td>
                <td>
                        <div>Image verification GPG or PKI method</div>
                        <div>Required when <em>command=verify</em>.</div>
                </td>
            </tr>

            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>patch</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Manage installation of software patch.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>command</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>install</li>
                                    <li>rollback</li>
                                    <li>get-history</li>
                                    <li>get-list</li>
                                    <li>get-status</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the patch manangement operation to be performed.</div>
                        <div><code>install</code> - Install patch specified by <em>path</em>.</div>
                        <div><code>rollback</code> - Remove an installed patch specified by <em>name</em>.</div>
                        <div><code>get-history</code> - Retrieve history of patches applied/rolled back.</div>
                        <div><code>get-list</code> - Retrieve list of installed patches.</div>
                        <div><code>get-status</code> - Retrieve patch installation/removal status.</div>
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
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>When <em>command=rollback</em>, specifies the name of the patch.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>path</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>When <em>command=install</em>, specifies the path of the patch to be installed.</div>
                        <div>Path can be a file in the device (file://filepath) or URL (http:// or https://).</div>
                </td>
            </tr>

    </table>
    <br/>




Examples
--------

.. code-block:: yaml

    - name: Install Enterprise SONiC image
      dellemc.enterprise_sonic.sonic_image_management:
        image:
          command: install
          path: 'file://home/admin/sonic.bin'

    - name: Get image installation status
      dellemc.enterprise_sonic.sonic_image_management:
        image:
          command: get-status

    - name: Get list of installed images
      dellemc.enterprise_sonic.sonic_image_management:
        image:
          command: get-list

    - name: Stage a firmware updater
      dellemc.enterprise_sonic.sonic_image_management:
        firmware:
          command: install
          path: 'file://home/admin/onie-update-full.bin'

    - name: Install GPG Key for image verification
      dellemc.enterprise_sonic.sonic_image_management:
        image:
          command: gpg-key
          keyserver: 'hkp://keyserver.ubuntu.com:80'
          pubkeyid: 'DAFWQGEW12345678'

    - name: Verify Enterprise SONiC image
      dellemc.enterprise_sonic.sonic_image_management:
        image:
          command: verify
          path: 'home://sonic.bin'
          verifymethod: 'gpg'
          signaturefile: 'sign.gpg'



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
                    <b>info</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>when <em>command=get-status</em> or <em>command=get-list</em> or <em>command=get-history</em></td>
                <td>
                            <div>Details returned by the specified get operation.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{
            &quot;file-download-speed&quot; : &quot;106200&quot;,
            &quot;file-progress&quot; : 100,
            &quot;file-size&quot; : &quot;1304997870&quot;,
            &quot;file-transfer-bytes&quot; : &quot;1304997870&quot;,
            &quot;install-end-time&quot; : &quot;1695714740&quot;,
            &quot;install-start-time&quot; : &quot;1695714698&quot;,
            &quot;install-status&quot; : &quot;INSTALL_STATE_SUCCESS&quot;,
            &quot;install-status-detail&quot; : &quot;Image install success&quot;,
            &quot;operation-status&quot; : &quot;GLOBAL_STATE_SUCCESS&quot;,
            &quot;transfer-end-time&quot; : &quot;1695714669&quot;,
            &quot;transfer-start-time&quot; : &quot;1695714657&quot;,
            &quot;transfer-status&quot; : &quot;TRANSFER_STATE_SUCCESS&quot;,
            &quot;transfer-status-detail&quot; : &quot;DOWNLOADING IMAGE&quot;
    }</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>status</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                    </div>
                </td>
                <td>when <em>command</em> is not <code>get-status</code>, <code>get-list</code> and <code>get-history</code></td>
                <td>
                            <div>Status of the operation performed.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">SUCCESS</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Arun Saravanan Balachandran (@ArunSaravananBalachandran), Aravind Mani (@aravindmani-1)
