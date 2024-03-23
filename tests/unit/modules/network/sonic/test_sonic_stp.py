from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.dellemc.enterprise_sonic.tests.unit.compat.mock import (
    patch,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.modules import (
    sonic_stp,
)
from ansible_collections.dellemc.enterprise_sonic.tests.unit.modules.utils import (
    set_module_args,
)
from .sonic_module import TestSonicModule


class TestSonicStpModule(TestSonicModule):
    module = sonic_stp

    @classmethod
    def setUpClass(cls):
        cls.mock_facts_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.stp.stp.edit_config"
        )
        cls.mock_config_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.stp.stp.edit_config"
        )
        cls.mock_utils_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils.edit_config"
        )
        cls.mock_get_interface_naming_mode = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils.get_device_interface_naming_mode"
        )
        cls.fixture_data = cls.load_fixtures('sonic_stp.yaml')

    def setUp(self):
        super(TestSonicStpModule, self).setUp()
        self.facts_edit_config = self.mock_facts_edit_config.start()
        self.config_edit_config = self.mock_config_edit_config.start()
        self.facts_edit_config.side_effect = self.facts_side_effect
        self.config_edit_config.side_effect = self.config_side_effect
        self.get_interface_naming_mode = self.mock_get_interface_naming_mode.start()
        self.get_interface_naming_mode.return_value = 'native'
        self.utils_edit_config = self.mock_utils_edit_config.start()
        self.utils_edit_config.side_effect = self.config_side_effect

    def tearDown(self):
        super(TestSonicStpModule, self).tearDown()
        self.mock_facts_edit_config.stop()
        self.mock_config_edit_config.stop()
        self.mock_get_interface_naming_mode.stop()
        self.mock_utils_edit_config.stop()

    def test_sonic_stp_merged_01(self):
        set_module_args(self.fixture_data['merged_01']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['merged_01']['existing_stp_config'])
        self.initialize_config_requests(self.fixture_data['merged_01']['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_stp_merged_02(self):
        set_module_args(self.fixture_data['merged_02']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['merged_02']['existing_stp_config'])
        self.initialize_config_requests(self.fixture_data['merged_02']['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_stp_merged_03(self):
        set_module_args(self.fixture_data['merged_03']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['merged_03']['existing_stp_config'])
        self.initialize_config_requests(self.fixture_data['merged_03']['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_stp_replaced_01(self):
        set_module_args(self.fixture_data['replaced_01']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['replaced_01']['existing_stp_config'])
        self.initialize_config_requests(self.fixture_data['replaced_01']['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_stp_replaced_02(self):
        set_module_args(self.fixture_data['replaced_02']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['replaced_02']['existing_stp_config'])
        self.initialize_config_requests(self.fixture_data['replaced_02']['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_stp_replaced_03(self):
        set_module_args(self.fixture_data['replaced_03']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['replaced_03']['existing_stp_config'])
        self.initialize_config_requests(self.fixture_data['replaced_03']['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_stp_replaced_04(self):
        set_module_args(self.fixture_data['replaced_04']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['replaced_04']['existing_stp_config'])
        self.initialize_config_requests(self.fixture_data['replaced_04']['expected_config_requests'])
        result = self.execute_module(changed=True)

    def test_sonic_stp_replaced_05(self):
        set_module_args(self.fixture_data['replaced_05']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['replaced_05']['existing_stp_config'])
        self.initialize_config_requests(self.fixture_data['replaced_05']['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_stp_replaced_06(self):
        set_module_args(self.fixture_data['replaced_06']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['replaced_06']['existing_stp_config'])
        self.initialize_config_requests(self.fixture_data['replaced_06']['expected_config_requests'])
        result = self.execute_module(changed=True)

    def test_sonic_stp_replaced_07(self):
        set_module_args(self.fixture_data['replaced_07']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['replaced_07']['existing_stp_config'])
        self.initialize_config_requests(self.fixture_data['replaced_07']['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_stp_overridden_01(self):
        set_module_args(self.fixture_data['overridden_01']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['overridden_01']['existing_stp_config'])
        self.initialize_config_requests(self.fixture_data['overridden_01']['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_stp_deleted_01(self):
        set_module_args(self.fixture_data['deleted_01']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['deleted_01']['existing_stp_config'])
        self.initialize_config_requests(self.fixture_data['deleted_01']['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_stp_deleted_02(self):
        set_module_args(self.fixture_data['deleted_02']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['deleted_02']['existing_stp_config'])
        self.initialize_config_requests(self.fixture_data['deleted_02']['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_stp_deleted_03(self):
        set_module_args(self.fixture_data['deleted_03']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['deleted_03']['existing_stp_config'])
        self.initialize_config_requests(self.fixture_data['deleted_03']['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_stp_deleted_04(self):
        set_module_args(self.fixture_data['deleted_04']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['deleted_04']['existing_stp_config'])
        self.initialize_config_requests(self.fixture_data['deleted_04']['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()
