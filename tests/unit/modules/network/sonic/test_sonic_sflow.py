from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.dellemc.enterprise_sonic.tests.unit.compat.mock import (
    patch,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.modules import (
    sonic_sflow,
)
from ansible_collections.dellemc.enterprise_sonic.tests.unit.modules.utils import (
    set_module_args,
)
from .sonic_module import TestSonicModule


class TestSonicSflowModule(TestSonicModule):
    module = sonic_sflow

    @classmethod
    def setUpClass(cls):
        cls.mock_facts_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.sflow.sflow.edit_config"
        )
        cls.mock_config_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.sflow.sflow.edit_config"
        )
        cls.mock_utils_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils.edit_config"
        )
        cls.mock_get_interface_naming_mode = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils.get_device_interface_naming_mode"
        )
        cls.fixture_data = cls.load_fixtures('sonic_sflow.yaml')

    def setUp(self):
        super(TestSonicSflowModule, self).setUp()
        self.facts_edit_config = self.mock_facts_edit_config.start()
        self.facts_edit_config.side_effect = self.facts_side_effect

        self.config_edit_config = self.mock_config_edit_config.start()
        self.config_edit_config.side_effect = self.config_side_effect

        self.utils_edit_config = self.mock_utils_edit_config.start()
        self.utils_edit_config.side_effect = self.config_side_effect

        self.get_interface_naming_mode = self.mock_get_interface_naming_mode.start()
        self.get_interface_naming_mode.return_value = 'native'

    def tearDown(self):
        super(TestSonicSflowModule, self).tearDown()
        self.mock_facts_edit_config.stop()
        self.mock_config_edit_config.stop()
        self.mock_utils_edit_config.stop()
        self.mock_get_interface_naming_mode.stop()

    def test_sonic_sflow_merged_01_primitives(self):
        test_name = "merged_01_primitives"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_sflow_config'])
        self.initialize_config_requests(self.fixture_data[test_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_sflow_merged_02_merge_lists(self):
        test_name = "merged_02_merge_lists"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_sflow_config'])
        self.initialize_config_requests(self.fixture_data[test_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_sflow_merged_03_just_interface_name(self):
        test_name = "merged_03_just_interface_name"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_sflow_config'])
        self.initialize_config_requests(self.fixture_data[test_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_sflow_merged_04_collectors_not_add(self):
        test_name = "merged_04_collectors_not_add"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_sflow_config'])
        result = self.execute_module(changed=False)
        self.validate_config_requests()

    def test_sonic_sflow_deleted_01_clear_all(self):
        test_name = "deleted_01_clear_all"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_sflow_config'])
        self.initialize_config_requests(self.fixture_data[test_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_sflow_deleted_02_clear_all_but_blank(self):
        test_name = "deleted_02_clear_all_but_blank"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_sflow_config'])
        result = self.execute_module(changed=False)
        self.validate_config_requests()

    def test_sonic_sflow_deleted_03_only_enabled_deletable(self):
        test_name = "deleted_03_only_enabled_deletable"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_sflow_config'])
        self.initialize_config_requests(self.fixture_data[test_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_sflow_deleted_04_matches(self):
        test_name = "deleted_04_matches"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_sflow_config'])
        self.initialize_config_requests(self.fixture_data[test_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_sflow_deleted_05_mismatches(self):
        test_name = "deleted_05_mismatches"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_sflow_config'])
        result = self.execute_module(changed=False)
        self.validate_config_requests()

    def test_sonic_sflow_deleted_06_no_matches(self):
        test_name = "deleted_06_no_matches"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_sflow_config'])
        self.initialize_config_requests(self.fixture_data[test_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_sflow_deleted_07_clear_lists(self):
        test_name = "deleted_07_clear_lists"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_sflow_config'])
        self.initialize_config_requests(self.fixture_data[test_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_sflow_deleted_08_delete_interface_attributes(self):
        test_name = "deleted_08_delete_interface_attributes"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_sflow_config'])
        self.initialize_config_requests(self.fixture_data[test_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_sflow_overridden_01_blank(self):
        test_name = "overridden_01_blank"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_sflow_config'])
        self.initialize_config_requests(self.fixture_data[test_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_sflow_overridden_02_mixed(self):
        test_name = "overridden_02_mixed"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_sflow_config'])
        self.initialize_config_requests(self.fixture_data[test_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_sflow_replaced_01_blank(self):
        test_name = "replaced_01_blank"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_sflow_config'])
        result = self.execute_module(changed=False)
        self.validate_config_requests()

    def test_sonic_sflow_replaced_02_mixed(self):
        test_name = "replaced_02_mixed"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_sflow_config'])
        self.initialize_config_requests(self.fixture_data[test_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_sflow_replaced_03_interfaces(self):
        test_name = "replaced_03_interfaces"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_sflow_config'])
        changed = False
        if 'expected_config_requests' in self.fixture_data[test_name]:
            self.initialize_config_requests(self.fixture_data[test_name]['expected_config_requests'])
            changed = True
        result = self.execute_module(changed=changed)
        self.validate_config_requests()
