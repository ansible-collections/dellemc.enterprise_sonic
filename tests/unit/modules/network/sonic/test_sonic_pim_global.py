from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.dellemc.enterprise_sonic.tests.unit.compat.mock import (
    patch,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.modules import (
    sonic_pim_global,
)
from ansible_collections.dellemc.enterprise_sonic.tests.unit.modules.utils import (
    set_module_args,
)
from .sonic_module import TestSonicModule


class TestSonicPimGlobalModule(TestSonicModule):
    module = sonic_pim_global

    @classmethod
    def setUpClass(cls):
        cls.mock_facts_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.pim_global.pim_global.edit_config"
        )
        cls.mock_config_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.pim_global.pim_global.edit_config"
        )
        cls.mock_bgp_utils_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.bgp_utils.edit_config"
        )
        cls.fixture_data = cls.load_fixtures('sonic_pim_global.yaml')

    def setUp(self):
        super(TestSonicPimGlobalModule, self).setUp()
        self.facts_edit_config = self.mock_facts_edit_config.start()
        self.config_edit_config = self.mock_config_edit_config.start()
        self.utils_edit_config = self.mock_bgp_utils_edit_config.start()

        self.facts_edit_config.side_effect = self.facts_side_effect
        self.config_edit_config.side_effect = self.config_side_effect
        self.utils_edit_config.side_effect = self.facts_side_effect

    def tearDown(self):
        super(TestSonicPimGlobalModule, self).tearDown()
        self.mock_facts_edit_config.stop()
        self.mock_config_edit_config.stop()
        self.mock_bgp_utils_edit_config.stop()

    def test_sonic_pim_global_merged_01(self):
        set_module_args(self.fixture_data['merged_01']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['merged_01']['facts_get_requests'])
        self.initialize_config_requests(self.fixture_data['merged_01']['config_requests'])

        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_pim_global_merged_invalid_ecmp_config(self):
        set_module_args(self.fixture_data['merged_invalid_ecmp_config']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['merged_invalid_ecmp_config']['facts_get_requests'])
        msg = 'ECMP cannot be disabled when ECMP Rebalance is enabled'

        result = self.execute_module(failed=True)
        self.assertEqual(result['msg'], msg)

    def test_sonic_pim_global_merged_invalid_ecmp_rebalance_config(self):
        set_module_args(self.fixture_data['merged_invalid_ecmp_rebalance_config']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['merged_invalid_ecmp_rebalance_config']['facts_get_requests'])
        msg = 'ECMP has to be enabled for configuring ECMP rebalance'

        result = self.execute_module(failed=True)
        self.assertEqual(result['msg'], msg)

    def test_sonic_pim_global_deleted_01(self):
        set_module_args(self.fixture_data['deleted_01']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['deleted_01']['facts_get_requests'])
        self.initialize_config_requests(self.fixture_data['deleted_01']['config_requests'])

        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_pim_global_deleted_02(self):
        set_module_args(self.fixture_data['deleted_02']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['deleted_02']['facts_get_requests'])
        self.initialize_config_requests(self.fixture_data['deleted_02']['config_requests'])

        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_pim_global_replaced_01(self):
        set_module_args(self.fixture_data['replaced_01']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['replaced_01']['facts_get_requests'])
        self.initialize_config_requests(self.fixture_data['replaced_01']['config_requests'])

        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_pim_global_replaced_invalid_ecmp_config(self):
        set_module_args(self.fixture_data['replaced_invalid_ecmp_config']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['replaced_invalid_ecmp_config']['facts_get_requests'])
        msg = 'ECMP cannot be disabled when ECMP Rebalance is enabled'

        result = self.execute_module(failed=True)
        self.assertEqual(result['msg'], msg)

    def test_sonic_pim_global_replaced_invalid_ecmp_rebalance_config(self):
        set_module_args(self.fixture_data['replaced_invalid_ecmp_rebalance_config']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['replaced_invalid_ecmp_rebalance_config']['facts_get_requests'])
        msg = 'ECMP has to be enabled for configuring ECMP rebalance'

        result = self.execute_module(failed=True)
        self.assertEqual(result['msg'], msg)

    def test_sonic_pim_global_overridden_01(self):
        set_module_args(self.fixture_data['overridden_01']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['overridden_01']['facts_get_requests'])
        self.initialize_config_requests(self.fixture_data['overridden_01']['config_requests'])

        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_pim_global_overridden_invalid_ecmp_rebalance_config(self):
        set_module_args(self.fixture_data['overridden_invalid_ecmp_rebalance_config']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['overridden_invalid_ecmp_rebalance_config']['facts_get_requests'])
        msg = 'ECMP has to be enabled for configuring ECMP rebalance'

        result = self.execute_module(failed=True)
        self.assertEqual(result['msg'], msg)
