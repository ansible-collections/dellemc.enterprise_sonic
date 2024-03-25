from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.dellemc.enterprise_sonic.tests.unit.compat.mock import (
    patch,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.modules import (
    sonic_fips,
)
from ansible_collections.dellemc.enterprise_sonic.tests.unit.modules.utils import (
    set_module_args,
)
from .sonic_module import TestSonicModule


class TestSonicFipsModule(TestSonicModule):
    module = sonic_fips

    @classmethod
    def setUpClass(cls):
        cls.mock_facts_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.fips.fips.edit_config"
        )
        cls.mock_config_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.fips.fips.edit_config"
        )
        cls.fixture_data = cls.load_fixtures('sonic_fips.yaml')

    def setUp(self):
        super(TestSonicFipsModule, self).setUp()
        self.facts_edit_config = self.mock_facts_edit_config.start()
        self.config_edit_config = self.mock_config_edit_config.start()

        self.facts_edit_config.side_effect = self.facts_side_effect
        self.config_edit_config.side_effect = self.config_side_effect

    def tearDown(self):
        super(TestSonicFipsModule, self).tearDown()
        self.mock_facts_edit_config.stop()
        self.mock_config_edit_config.stop()

    def test_sonic_fips_merged_01(self):
        set_module_args(self.fixture_data['merged_01']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['merged_01']['facts_get_requests'])
        self.initialize_config_requests(self.fixture_data['merged_01']['config_requests'])

        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_fips_merged_02(self):
        set_module_args(self.fixture_data['merged_02']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['merged_02']['facts_get_requests'])
        self.initialize_config_requests(self.fixture_data['merged_02']['config_requests'])

        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_fips_deleted_01(self):
        set_module_args(self.fixture_data['deleted_01']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['deleted_01']['facts_get_requests'])
        self.initialize_config_requests(self.fixture_data['deleted_01']['config_requests'])

        result = self.execute_module(changed=True)
        self.validate_config_requests()
