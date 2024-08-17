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


class TestSonicConfigModule(TestSonicModule):
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

    def edit_config_side_effect(self, module, commands):
        """Side effect function for 'config' requests mock"""

        self.config_commands_sent.extend(commands)

    def run_commands_side_effect(self, module, commands):
        """Side effect function for run_commands mock"""

        for cmd in commands:
            self.config_commands_sent.append(cmd['command'])

    def validate_config_commands(self):
        """Check if both list of requests sent and expected are same"""

        self.assertEqual(len(self.config_commands_valid), len(self.config_commands_sent))
        for valid_command, sent_command in zip(self.config_commands_valid, self.config_commands_sent):
            self.assertEqual(valid_command, sent_command)

    def setUp(self):
        super(TestSonicConfigModule, self).setUp()
        self.config_commands_sent = []
        self.config_commands_valid = []
        self.get_config = self.mock_get_config.start()
        self.get_config.return_value = "show running-configuration\nip load-share hash ipv4 ipv4-dst-ip"
        self.edit_config = self.mock_edit_config.start()
        self.edit_config.side_effect = self.edit_config_side_effect
        self.run_commands = self.mock_run_commands.start()
        self.run_commands.side_effect = self.run_commands_side_effect

    def tearDown(self):
        super(TestSonicConfigModule, self).tearDown()
        self.mock_get_config.stop()
        self.mock_edit_config.stop()
        self.mock_run_commands.stop()

    def test_sonic_config_merged_01(self):
        set_module_args(self.fixture_data['merged_01']['module_args'])
        self.config_commands_valid = self.fixture_data['merged_01']['expected_commands_to_device']
        result = self.execute_module(changed=True)
        self.validate_config_commands()

    def test_sonic_config_merged_02(self):
        set_module_args(self.fixture_data['merged_02']['module_args'])
        self.config_commands_valid = self.fixture_data['merged_02']['expected_commands_to_device']
        result = self.execute_module(changed=True)
        self.validate_config_commands()
