from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.dellemc.enterprise_sonic.tests.unit.compat.mock import (
    patch,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.modules import (
    sonic_pim_interfaces,
)
from ansible_collections.dellemc.enterprise_sonic.tests.unit.modules.utils import (
    set_module_args,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.sonic import (
    update_url
)
from .sonic_module import TestSonicModule


class TestSonicPimInterfacesModule(TestSonicModule):
    module = sonic_pim_interfaces

    @classmethod
    def setUpClass(cls):
        cls.mock_facts_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.pim_interfaces.pim_interfaces.edit_config"
        )
        cls.mock_config_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.pim_interfaces.pim_interfaces.edit_config"
        )
        cls.mock_bgp_utils_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.bgp_utils.edit_config"
        )
        cls.mock_get_interface_naming_mode = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils.get_device_interface_naming_mode"
        )
        cls.fixture_data = cls.load_fixtures('sonic_pim_interfaces.yaml')

    def setUp(self):
        super(TestSonicPimInterfacesModule, self).setUp()
        self.facts_edit_config = self.mock_facts_edit_config.start()
        self.config_edit_config = self.mock_config_edit_config.start()
        self.utils_edit_config = self.mock_bgp_utils_edit_config.start()

        self.facts_edit_config.side_effect = self.facts_side_effect
        self.config_edit_config.side_effect = self.config_side_effect
        self.utils_edit_config.side_effect = self.facts_side_effect

        self.get_interface_naming_mode = self.mock_get_interface_naming_mode.start()
        self.get_interface_naming_mode.return_value = 'standard'

    def tearDown(self):
        super(TestSonicPimInterfacesModule, self).tearDown()
        self.mock_facts_edit_config.stop()
        self.mock_config_edit_config.stop()
        self.mock_bgp_utils_edit_config.stop()
        self.mock_get_interface_naming_mode.stop()

    # In pim_interfaces config, GET requests are sent to retrieve VRF interfaces data
    # to create PATCH/DELETE requests for modifying PIM interface configurations
    def config_side_effect(self, module, commands):
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

    def test_sonic_pim_interfaces_merged_01(self):
        set_module_args(self.fixture_data['merged_01']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['merged_01']['facts_get_requests'])
        self.initialize_config_requests(self.fixture_data['merged_01']['config_requests'])

        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_pim_interfaces_deleted_01(self):
        set_module_args(self.fixture_data['deleted_01']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['deleted_01']['facts_get_requests'])
        self.initialize_config_requests(self.fixture_data['deleted_01']['config_requests'])

        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_pim_interfaces_deleted_02(self):
        set_module_args(self.fixture_data['deleted_02']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['deleted_02']['facts_get_requests'])
        self.initialize_config_requests(self.fixture_data['deleted_02']['config_requests'])

        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_pim_interfaces_replaced_01(self):
        set_module_args(self.fixture_data['replaced_01']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['replaced_01']['facts_get_requests'])
        self.initialize_config_requests(self.fixture_data['replaced_01']['config_requests'])

        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_pim_interfaces_overridden_01(self):
        set_module_args(self.fixture_data['overridden_01']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['overridden_01']['facts_get_requests'])
        self.initialize_config_requests(self.fixture_data['overridden_01']['config_requests'])

        result = self.execute_module(changed=True)
        self.validate_config_requests()
