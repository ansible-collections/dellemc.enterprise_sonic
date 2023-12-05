from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible_collections.dellemc.enterprise_sonic.tests.unit.compat.mock import (
    patch,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.modules import (
    sonic_dhcp_snooping,
)
from ansible_collections.dellemc.enterprise_sonic.tests.unit.modules.utils import (
    set_module_args,
)
from .sonic_module import TestSonicModule


class TestSonicDhcpSnoopingModule(TestSonicModule):
    module = sonic_dhcp_snooping

    @classmethod
    def setUpClass(cls):
        cls.mock_facts_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.dhcp_snooping.dhcp_snooping.edit_config"
        )
        cls.mock_config_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.dhcp_snooping.dhcp_snooping.edit_config"
        )
        cls.mock_utils_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils.edit_config"
        )
        cls.fixture_data = cls.load_fixtures('sonic_dhcp_snooping.yaml')

    def setUp(self):
        super(TestSonicDhcpSnoopingModule, self).setUp()
        self.facts_edit_config = self.mock_facts_edit_config.start()
        self.config_edit_config = self.mock_config_edit_config.start()
        self.facts_edit_config.side_effect = self.facts_side_effect
        self.config_edit_config.side_effect = self.config_side_effect
        self.utils_edit_config = self.mock_utils_edit_config.start()
        self.utils_edit_config.side_effect = self.facts_side_effect

    def tearDown(self):
        super(TestSonicDhcpSnoopingModule, self).tearDown()
        self.mock_facts_edit_config.stop()
        self.mock_config_edit_config.stop()
        self.mock_utils_edit_config.stop()

    def test_sonic_dhcp_snooping_merged_01(self):
        test_name = "merged_01"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_dhcp_snooping_merged_02(self):
        test_name = "merged_02"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_dhcp_snooping_merged_03(self):
        test_name = "merged_03"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_dhcp_snooping_merged_04(self):
        test_name = "merged_04_blank"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_name]['expected_config_requests'])
        result = self.execute_module(changed=False)
        self.validate_config_requests()

    def test_sonic_dhcp_snooping_deleted_01(self):
        test_name = "deleted_01"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_dhcp_snooping_deleted_02(self):
        test_name = "deleted_02_clear_vlans"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_dhcp_snooping_deleted_02_2(self):
        test_name = "deleted_02_2_select_vlans"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_dhcp_snooping_deleted_03(self):
        test_name = "deleted_03"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_dhcp_snooping_deleted_04(self):
        test_name = "deleted_04_clear_bindings"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_dhcp_snooping_deleted_05(self):
        test_name = "deleted_05_select_bindings"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_dhcp_snooping_deleted_06(self):
        test_name = "deleted_06_clear_trusted"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_dhcp_snooping_deleted_07(self):
        test_name = "deleted_07_select_trusted"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_dhcp_snooping_deleted_08(self):
        test_name = "deleted_08_booleans"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_dhcp_snooping_deleted_09(self):
        test_name = "deleted_09_empty"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_dhcp_snooping_overridden_01(self):
        test_name = "overridden_01"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_dhcp_snooping_replaced_01(self):
        test_name = "replaced_01"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_dhcp_snooping_replaced_02(self):
        test_name = "replaced_02"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_dhcp_snooping_replaced_03(self):
        test_name = "replaced_03_vlan_replace"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_dhcp_snooping_replaced_04(self):
        test_name = "replaced_04_trusted"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_dhcp_snooping_replaced_05(self):
        test_name = "replaced_05_verify"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_dhcp_snooping_replaced_06(self):
        test_name = "replaced_06_empty_bindings"
        set_module_args(self.fixture_data[test_name]['module_args'])
        self.initialize_facts_get_requests(self.fixture_data[test_name]['existing_config'])
        self.initialize_config_requests(self.fixture_data[test_name]['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()
