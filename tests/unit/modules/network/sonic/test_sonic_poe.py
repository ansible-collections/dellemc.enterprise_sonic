from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.dellemc.enterprise_sonic.tests.unit.compat.mock import (
    patch,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.modules import (
    sonic_poe,
)
from ansible_collections.dellemc.enterprise_sonic.tests.unit.modules.utils import (
    set_module_args,
)
from .sonic_module import TestSonicModule


class TestSonicPoeModule(TestSonicModule):
    module = sonic_poe

    @classmethod
    def setUpClass(cls):
        cls.mock_facts_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.poe.poe.edit_config"
        )
        cls.mock_config_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.poe.poe.edit_config"
        )
        cls.fixture_data = cls.load_fixtures('sonic_poe.yaml')

    def setUp(self):
        super(TestSonicPoeModule, self).setUp()
        self.facts_edit_config = self.mock_facts_edit_config.start()
        self.config_edit_config = self.mock_config_edit_config.start()

        self.facts_edit_config.side_effect = self.facts_side_effect
        self.config_edit_config.side_effect = self.config_side_effect

    def tearDown(self):
        super(TestSonicPoeModule, self).tearDown()
        self.mock_facts_edit_config.stop()
        self.mock_config_edit_config.stop()

    def test_sonic_lag_interfaces_merged_01_merge_all(self):
        test_case_name = "merged_01_merge_all"
        set_module_args(self.fixture_data[test_case_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_case_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_case_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()
    
    def test_sonic_lag_interfaces_merged_02_list_items(self):
        test_case_name = "merged_02_list_items"
        set_module_args(self.fixture_data[test_case_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_case_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_case_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_lag_interfaces_merged_03_test_all_settings(self):
        test_case_name = "merged_03_test_all_settings"
        set_module_args(self.fixture_data[test_case_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_case_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_case_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_lag_interfaces_deleted_01_clear_lists(self):
        test_case_name = "deleted_01_clear_lists"
        set_module_args(self.fixture_data[test_case_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_case_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_case_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_lag_interfaces_deleted_02_delete_some_items(self):
        test_case_name = "deleted_02_delete_some_items"
        set_module_args(self.fixture_data[test_case_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_case_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_case_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_lag_interfaces_deleted_03_mismatches(self):
        test_case_name = "deleted_03_mismatches"
        set_module_args(self.fixture_data[test_case_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_case_name]['existing_config'])
        result = self.execute_module(changed=False)
        self.validate_config_requests()

    def test_sonic_lag_interfaces_overridden_01_lists(self):
        test_case_name = "overridden_01_lists"
        set_module_args(self.fixture_data[test_case_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_case_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_case_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_lag_interfaces_overridden_02_others(self):
        test_case_name = "overridden_02_others"
        set_module_args(self.fixture_data[test_case_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_case_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_case_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_lag_interfaces_overridden_03_clear_lists(self):
        test_case_name = "overridden_03_clear_lists"
        set_module_args(self.fixture_data[test_case_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_case_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_case_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_lag_interfaces_replaced_01_lists(self):
        test_case_name = "replaced_01_lists"
        set_module_args(self.fixture_data[test_case_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_case_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_case_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_lag_interfaces_replaced_02_others(self):
        test_case_name = "replaced_02_others"
        set_module_args(self.fixture_data[test_case_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_case_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_case_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()