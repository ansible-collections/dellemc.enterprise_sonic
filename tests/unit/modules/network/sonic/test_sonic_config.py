from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.dellemc.enterprise_sonic.tests.unit.compat.mock import (
    patch,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.modules import (
    sonic_config,
)
from ansible_collections.dellemc.enterprise_sonic.tests.unit.modules.utils import (
    set_module_args,
)
from .sonic_module import TestSonicModule


class TestSonicInterfacesModule(TestSonicModule):
    module = sonic_config

    @classmethod
    def setUpClass(cls):
        cls.mock_get_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.modules.sonic_config.get_config"
        )
        cls.mock_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.modules.sonic_config.edit_config"
        )
        cls.mock_run_commands = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.modules.sonic_config.run_commands"
        )
        cls.fixture_data = cls.load_fixtures('sonic_config.yaml')

    def setUp(self):
        super(TestSonicInterfacesModule, self).setUp()
        self.get_config = self.mock_get_config.start()
        self.get_config.return_value = "show running-configuration\nip load-share hash ipv4 ipv4-dst-ip"
        self.edit_config = self.mock_edit_config.start()
        self.edit_config.return_value = ['no ip access-list test', 'ip access-list test', 'seq 1 permit tcp any any ack', 'no ip access-list test']
        self.run_commands = self.mock_run_commands.start()
        self.run_commands.return_value = ['Software Version  : dell_sonic_4.x_share.770-0beb2c821\n']

    def tearDown(self):
        super(TestSonicInterfacesModule, self).tearDown()
        self.mock_get_config.stop()
        self.mock_edit_config.stop()
        self.mock_run_commands.stop()

    def test_sonic_config_merged_01(self):
        set_module_args(self.fixture_data['merged_01']['module_args'])
        result = self.execute_module(changed=True)

    def test_sonic_config_merged_02(self):
        set_module_args(self.fixture_data['merged_02']['module_args'])
        result = self.execute_module(changed=True)
