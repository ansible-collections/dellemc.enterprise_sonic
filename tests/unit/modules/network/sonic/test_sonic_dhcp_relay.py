from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.dellemc.enterprise_sonic.tests.unit.compat.mock import (
    patch,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.modules import (
    sonic_dhcp_relay,
)
from ansible_collections.dellemc.enterprise_sonic.tests.unit.modules.utils import (
    set_module_args,
)
from .sonic_module import TestSonicModule


class TestSonicDhcpRelayModule(TestSonicModule):
    module = sonic_dhcp_relay

    @classmethod
    def setUpClass(cls):
        cls.mock_facts_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.dhcp_relay.dhcp_relay.edit_config"
        )
        cls.mock_config_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.dhcp_relay.dhcp_relay.edit_config"
        )
        cls.mock_get_interface_naming_mode = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils.get_device_interface_naming_mode"
        )
        cls.fixture_data = cls.load_fixtures('sonic_dhcp_relay.yaml')

    def setUp(self):
        super(TestSonicDhcpRelayModule, self).setUp()
        self.facts_edit_config = self.mock_facts_edit_config.start()
        self.config_edit_config = self.mock_config_edit_config.start()

        self.facts_edit_config.side_effect = self.facts_side_effect
        self.config_edit_config.side_effect = self.config_side_effect

        self.get_interface_naming_mode = self.mock_get_interface_naming_mode.start()
        self.get_interface_naming_mode.return_value = 'standard'

    def tearDown(self):
        super(TestSonicDhcpRelayModule, self).tearDown()
        self.mock_facts_edit_config.stop()
        self.mock_config_edit_config.stop()
        self.mock_get_interface_naming_mode.stop()

    def test_sonic_dhcp_relay_merged_01(self):
        set_module_args(self.fixture_data['merged_01']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['merged_01']['facts_get_requests'])
        self.initialize_config_requests(self.fixture_data['merged_01']['config_requests'])

        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_dhcp_relay_merged_02(self):
        set_module_args(self.fixture_data['merged_02']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['merged_02']['facts_get_requests'])
        self.initialize_config_requests(self.fixture_data['merged_02']['config_requests'])

        result = self.execute_module(changed=False)
        self.validate_config_requests()

    def test_sonic_dhcp_relay_deleted_01(self):
        set_module_args(self.fixture_data['deleted_01']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['deleted_01']['facts_get_requests'])
        self.initialize_config_requests(self.fixture_data['deleted_01']['config_requests'])

        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_dhcp_relay_deleted_02(self):
        set_module_args(self.fixture_data['deleted_02']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['deleted_02']['facts_get_requests'])
        self.initialize_config_requests(self.fixture_data['deleted_02']['config_requests'])

        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_dhcp_relay_deleted_03(self):
        set_module_args(self.fixture_data['deleted_03']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['deleted_03']['facts_get_requests'])
        self.initialize_config_requests(self.fixture_data['deleted_03']['config_requests'])

        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_dhcp_relay_deleted_04(self):
        set_module_args(self.fixture_data['deleted_04']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['deleted_04']['facts_get_requests'])
        self.initialize_config_requests(self.fixture_data['deleted_04']['config_requests'])

        result = self.execute_module(changed=False)
        self.validate_config_requests()

    def test_sonic_dhcp_relay_replaced_01(self):
        set_module_args(self.fixture_data['replaced_01']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['replaced_01']['facts_get_requests'])
        self.initialize_config_requests(self.fixture_data['replaced_01']['config_requests'])

        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_dhcp_relay_replaced_02(self):
        set_module_args(self.fixture_data['replaced_02']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['replaced_02']['facts_get_requests'])
        self.initialize_config_requests(self.fixture_data['replaced_02']['config_requests'])

        result = self.execute_module(changed=False)
        self.validate_config_requests()

    def test_sonic_dhcp_relay_overridden_01(self):
        set_module_args(self.fixture_data['overridden_01']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['overridden_01']['facts_get_requests'])
        self.initialize_config_requests(self.fixture_data['overridden_01']['config_requests'])

        result = self.execute_module(changed=True)
        self.validate_config_requests()
