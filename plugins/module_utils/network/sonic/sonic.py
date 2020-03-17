#
# (c) 2015 Peter Sprygada, <psprygada@ansible.com>
# (c) 2017 Red Hat, Inc
#
# Copyright (c) 2016 Dell Inc.
#
# This code is part of Ansible, but is an independent component.
# This particular file snippet, and this file snippet only, is BSD licensed.
# Modules you write using this snippet, which is embedded dynamically by Ansible
# still belong to the author of the module, and may assign their own license
# to the complete work.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
# USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
import json

from ansible.module_utils._text import to_text
from ansible.module_utils.network.common.utils import to_list, ComplexList
from ansible.module_utils.connection import Connection, ConnectionError, exec_command

_DEVICE_CONFIGS = {}
_DEVICE_CONNECTION = None


WARNING_PROMPTS_RE = [
    r"[\r\n]?\[confirm yes/no\]:\s?$",
    r"[\r\n]?\[y/n\]:\s?$",
    r"[\r\n]?\[yes/no\]:\s?$"
]


class Cli:
    def __init__(self, module):
        self._module = module
        self._device_configs = {}
        self._connection = None

    def get_capabilities(self):
        """Returns platform info of the remove device
        """
        connection = self._get_connection()
        return json.loads(connection.get_capabilities())

    def _get_connection(self):
        if not self._connection:
            self._connection = Connection(self._module._socket_path)
        return self._connection

    def load_config(self, commands):
        rc, out, err = exec_command(self._module, 'configure terminal')
        if rc != 0:
            self._module.fail_json(msg='unable to enter configuration mode', err=to_text(err, errors='surrogate_or_strict'))
        for command in to_list(commands):
            if command == 'end':
                continue
            rc, out, err = exec_command(self._module, command)
            if rc != 0:
                self._module.fail_json(msg=to_text(err, errors='surrogate_or_strict'), command=command, rc=rc)
        exec_command(self._module, 'exit')

    def run_commands(self, commands, check_rc=True):
        connection = self._get_connection()
        try:
            return connection.run_commands(commands=commands, check_rc=check_rc)
        except ConnectionError as exc:
            self._module.fail_json(msg=to_text(exc))


class HttpApi:
    def __init__(self, module):
        self._module = module
        self._device_configs = {}
        self._connection_obj = None

    def get_capabilities(self):
        """Returns platform info of the remove device
        """
        try:
            capabilities = self._connection.get_capabilities()
        except ConnectionError as exc:
            self._module.fail_json(msg=to_text(exc, errors='surrogate_then_replace'))

        return json.loads(capabilities)

    @property
    def _connection(self):
        if not self._connection_obj:
            self._connection_obj = Connection(self._module._socket_path)
        return self._connection_obj

    def send_requests(self, requests):
        """Send a list of http requests to remote device and return results
        """
        if requests is None:
            raise ValueError("'requests' value is required")

        responses = list()
        for req in to_list(requests):
            try:
                response = self._connection.send_request(**req)
            except ConnectionError as exc:
                self._module.fail_json(msg=to_text(exc, errors='surrogate_then_replace'))
            responses.append(response)
        return responses


def get_capabilities(module):
    conn = get_connection(module)
    return conn.get_capabilities()


def get_connection(module):
    global _DEVICE_CONNECTION
    if not _DEVICE_CONNECTION:
        connection_proxy = Connection(module._socket_path)
        cap = json.loads(connection_proxy.get_capabilities())
        if cap['network_api'] == 'cliconf':
            conn = Cli(module)
        elif cap['network_api'] == 'sonic_rest':
            conn = HttpApi(module)
        else:
            module.fail_json(msg='Invalid connection type %s' % cap['network_api'])
        _DEVICE_CONNECTION = conn
    return _DEVICE_CONNECTION


def check_args(module, warnings):
    pass


def load_config(module, commands):
    conn = get_connection(module)
    return conn.load_config(commands)


def run_commands(module, commands, check_rc=True):
    conn = get_connection(module)
    return conn.run_commands(commands, check_rc)


def send_requests(module, requests):
    conn = get_connection(module)
    return conn.send_requests(to_request(module, requests))


def to_request(module, requests):
    transform = ComplexList(dict(
        path=dict(key=True),
        method=dict(),
        data=dict(type='dict'),
    ), module)
    return transform(to_list(requests))
