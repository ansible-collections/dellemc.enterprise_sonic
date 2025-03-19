from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os
import yaml

from ansible_collections.dellemc.enterprise_sonic.tests.unit.compat.mock import (
    patch,
)
from ansible_collections.dellemc.enterprise_sonic.tests.unit.modules.utils import (
    AnsibleExitJson,
    AnsibleFailJson,
    ModuleTestCase,
)

from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    update_url
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    get_diff
)


class TestSonicModule(ModuleTestCase):
    """Enterprise SONiC ansible module base unit test class"""

    def setUp(self):
        super(TestSonicModule, self).setUp()
        self.mock_utils_intf_naming_mode = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils.intf_naming_mode", ""
        )
        self.mock_utils_intf_naming_mode.start()

        self.config_requests_valid = []
        self.config_requests_sent = []

        self._config_requests_dict = {}
        self._facts_requests_dict = {}

    def tearDown(self):
        super(TestSonicModule, self).tearDown()
        self.mock_utils_intf_naming_mode.stop()

    @staticmethod
    def load_fixtures(file_name, content="yaml"):
        """Load data from specified fixture file and format"""
        fixture_path = os.path.join(os.path.dirname(__file__), "fixtures")
        file_path = os.path.join(fixture_path, file_name)

        file_stream = open(file_path, "r")
        if content == "yaml":
            data = yaml.full_load(file_stream)
        else:
            data = file_stream.read()
        file_stream.close()

        return data

    def initialize_facts_get_requests(self, facts_get_requests):
        for request in facts_get_requests:
            self._facts_requests_dict[request['path']] = request['response']

    def initialize_config_requests(self, config_requests):
        for request in config_requests:
            valid_request = request.copy()
            path = valid_request['path']
            method = valid_request['method'].lower()
            data = valid_request.get('data', {})
            if valid_request.get('response'):
                response = valid_request.pop('response')
            else:
                response = {}

            self.config_requests_valid.append(valid_request)
            if self._config_requests_dict.get(path) is None:
                self._config_requests_dict[path] = {}

            config_request_dict = self._config_requests_dict[path]
            if config_request_dict.get(method) is None:
                config_request_dict[method] = []

            config_request_dict[method].append([
                data,
                {'code': response.get('code', 200), 'value': response.get('value', {})}
            ])

    def facts_side_effect(self, module, commands):
        """Side effect function for 'facts' GET requests mock"""
        responses = []
        for command in commands:
            response = []
            path = update_url(command['path'])
            method = command['method'].lower()

            if method == 'get':
                if self._facts_requests_dict.get(path):
                    response.append(self._facts_requests_dict[path]['code'])
                    response.append(self._facts_requests_dict[path].get('value', {}))
            else:
                self.module.fail_json(msg="Non GET REST API request made in get facts {0}".format(command))

            responses.append(response)

        return responses

    def config_side_effect(self, module, commands):
        """Side effect function for 'config' requests mock"""
        responses = []
        for command in commands:
            response = []
            path = update_url(command['path'])
            method = command['method'].lower()
            data = command['data']

            self.config_requests_sent.append({'path': path, 'method': method, 'data': data})
            entries = self._config_requests_dict.get(path, {}).get(method, [])
            for entry in entries:
                if data == entry[0]:
                    response.append(entry[1]['code'])
                    response.append(entry[1]['value'])
                    break

            responses.append(response)

        return responses

    def execute_module(self, failed=False, changed=False):
        if failed:
            result = self.failed()
        else:
            result = self.changed(changed)

        return result

    def failed(self):
        with self.assertRaises(AnsibleFailJson) as exc:
            self.module.main()

        result = exc.exception.args[0]
        self.assertTrue(result["failed"], result)
        return result

    def changed(self, changed=False):
        with self.assertRaises(AnsibleExitJson) as exc:
            self.module.main()

        result = exc.exception.args[0]
        self.assertEqual(result["changed"], changed, result)
        return result

    def validate_config_requests(self, requests_sorted=False):
        """Check if both list of requests sent and expected are same"""
        if not requests_sorted:
            # Sort by 'path' (primary) followed by 'method' (secondary)
            self.config_requests_valid.sort(key=lambda request: (request['path'], request['method']))
            self.config_requests_sent.sort(key=lambda request: (request['path'], request['method']))

        self.assertEqual(len(self.config_requests_valid), len(self.config_requests_sent))
        for valid_request, sent_request in zip(self.config_requests_valid, self.config_requests_sent):
            self.assertEqual(get_diff(valid_request, sent_request, [{'path': "", 'method': "", 'data': {}}]), {})
            self.assertEqual(get_diff(sent_request, valid_request, [{'path': "", 'method': "", 'data': {}}]), {})
