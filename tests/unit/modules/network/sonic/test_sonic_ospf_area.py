from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.dellemc.enterprise_sonic.tests.unit.compat.mock import (
    patch,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.modules import (
    sonic_ospf_area
)
from ansible_collections.dellemc.enterprise_sonic.tests.unit.modules.utils import (
    set_module_args,
)
from .sonic_module import TestSonicModule


class TestSonicOspfAreaModule(TestSonicModule):
    module = sonic_ospf_area

    @classmethod
    def setUpClass(cls):
        cls.mock_facts_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.ospf_area.ospf_area.edit_config"
        )
        cls.mock_config_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.ospf_area.ospf_area.edit_config"
        )
        cls.mock_get_interface_naming_mode = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils.get_device_interface_naming_mode"
        )
        cls.mock_bgp_utils_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.bgp_utils.edit_config"
        )

        cls.fixture_data = cls.load_fixtures('sonic_ospf_area.yaml')

    def setUp(self):
        super(TestSonicOspfAreaModule, self).setUp()
        self.facts_edit_config = self.mock_facts_edit_config.start()
        self.facts_edit_config.side_effect = self.facts_side_effect

        self.config_edit_config = self.mock_config_edit_config.start()
        self.config_edit_config.side_effect = self.config_side_effect

        self.get_interface_naming_mode = self.mock_get_interface_naming_mode.start()
        self.get_interface_naming_mode.return_value = 'native'

        self.utils_edit_config = self.mock_bgp_utils_edit_config.start()
        self.utils_edit_config.side_effect = self.facts_side_effect

    def tearDown(self):
        super(TestSonicOspfAreaModule, self).tearDown()
        self.mock_facts_edit_config.stop()
        self.mock_config_edit_config.stop()
        self.mock_get_interface_naming_mode.stop()
        self.mock_bgp_utils_edit_config.stop()

    def test_sonic_ospf_area_merged_keys(self):
        test_case_name = "merged_keys"
        set_module_args(self.fixture_data[test_case_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_case_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_case_name]['expected_config_requests'])
        result = self.execute_module(changed=self.fixture_data[test_case_name]['makes_changes'])
        self.validate_config_requests()

    def test_sonic_ospf_area_merged_01_all_settings(self):
        test_case_name = "merged_01_all_settings"
        set_module_args(self.fixture_data[test_case_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_case_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_case_name]['expected_config_requests'])
        result = self.execute_module(changed=self.fixture_data[test_case_name]['makes_changes'])
        self.validate_config_requests()

    def test_sonic_ospf_area_merged_add_minimum(self):
        test_case_name = "merged_add_minimum"
        set_module_args(self.fixture_data[test_case_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_case_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_case_name]['expected_config_requests'])
        result = self.execute_module(changed=self.fixture_data[test_case_name]['makes_changes'])
        self.validate_config_requests()

    def test_sonic_ospf_area_merge_changes(self):
        test_case_name = "merge_changes"
        set_module_args(self.fixture_data[test_case_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_case_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_case_name]['expected_config_requests'])
        result = self.execute_module(changed=self.fixture_data[test_case_name]['makes_changes'])
        self.validate_config_requests()

    def test_sonic_ospf_area_merge_no_changes(self):
        test_case_name = "merge_no_changes"
        set_module_args(self.fixture_data[test_case_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_case_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_case_name]['expected_config_requests'])
        result = self.execute_module(changed=self.fixture_data[test_case_name]['makes_changes'])
        self.validate_config_requests()

    def test_sonic_ospf_area_delete_areas(self):
        test_case_name = "delete_areas"
        set_module_args(self.fixture_data[test_case_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_case_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_case_name]['expected_config_requests'])
        result = self.execute_module(changed=self.fixture_data[test_case_name]['makes_changes'])
        self.validate_config_requests()

    def test_sonic_ospf_area_clear_subsections(self):
        test_case_name = "clear_subsections"
        set_module_args(self.fixture_data[test_case_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_case_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_case_name]['expected_config_requests'])
        result = self.execute_module(changed=self.fixture_data[test_case_name]['makes_changes'])
        self.validate_config_requests()

    def test_sonic_ospf_area_clear_everything(self):
        test_case_name = "clear_everything"
        set_module_args(self.fixture_data[test_case_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_case_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_case_name]['expected_config_requests'])
        result = self.execute_module(changed=self.fixture_data[test_case_name]['makes_changes'])
        self.validate_config_requests()

    def test_sonic_ospf_area_delete_attributes(self):
        test_case_name = "delete_attributes"
        set_module_args(self.fixture_data[test_case_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_case_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_case_name]['expected_config_requests'])
        result = self.execute_module(changed=self.fixture_data[test_case_name]['makes_changes'])
        self.validate_config_requests()

    def test_sonic_ospf_area_no_deletes(self):
        test_case_name = "no_deletes"
        set_module_args(self.fixture_data[test_case_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_case_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_case_name]['expected_config_requests'])
        result = self.execute_module(changed=self.fixture_data[test_case_name]['makes_changes'])
        self.validate_config_requests()

    def test_sonic_ospf_area_replaced(self):
        test_case_name = "replaced"
        set_module_args(self.fixture_data[test_case_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_case_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_case_name]['expected_config_requests'])
        result = self.execute_module(changed=self.fixture_data[test_case_name]['makes_changes'])
        self.validate_config_requests()

    def test_sonic_ospf_area_overridden(self):
        test_case_name = "overridden"
        set_module_args(self.fixture_data[test_case_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_case_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_case_name]['expected_config_requests'])
        result = self.execute_module(changed=self.fixture_data[test_case_name]['makes_changes'])
        self.validate_config_requests()
