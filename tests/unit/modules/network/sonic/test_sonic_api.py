from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.dellemc.enterprise_sonic.tests.unit.compat.mock import (
    patch,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.modules import (
    sonic_api,
)
from ansible_collections.dellemc.enterprise_sonic.tests.unit.modules.utils import (
    set_module_args,
)
from .sonic_module import TestSonicModule


class TestSonicApiModule(TestSonicModule):
    module = sonic_api

    @classmethod
    def setUpClass(cls):
        cls.mock_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.modules.sonic_api.edit_config"
        )
        cls.fixture_data = cls.load_fixtures('sonic_api.yaml')

    def setUp(self):
        super(TestSonicApiModule, self).setUp()
        self.edit_config = self.mock_edit_config.start()
        self.edit_config.return_value = [(204, '')]

    def tearDown(self):
        super(TestSonicApiModule, self).tearDown()
        self.mock_edit_config.stop()

    def test_sonic_api_merged_01(self):
        set_module_args(self.fixture_data['merged_01']['module_args'])
        result = self.execute_module(changed=True)
