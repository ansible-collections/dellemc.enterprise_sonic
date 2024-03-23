from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.dellemc.enterprise_sonic.tests.unit.compat.mock import (
    patch,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.modules import (
    sonic_command,
)
from ansible_collections.dellemc.enterprise_sonic.tests.unit.modules.utils import (
    set_module_args,
)
from .sonic_module import TestSonicModule


class TestSonicCommandModule(TestSonicModule):
    module = sonic_command

    @classmethod
    def setUpClass(cls):
        cls.mock_run_commands = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.modules.sonic_command.run_commands"
        )
        cls.fixture_data = cls.load_fixtures('sonic_command.yaml')

    def run_commands_side_effect(self, module, commands):
        """Side effect function for run commands  mock"""

        for cmd in commands:
            self.config_commands_sent.append(cmd['command'])
        # Purpose of the Unit testing for sonic_command is to check whether the passed command goes to device.
        # Response from device is validated against the expected values.
        # Simulate a dummy return value for the "show version" command that is being unit tested.
        return ['Software Version : dell_sonic_4.x_share.770-0beb2c821\n']

    def validate_config_commands(self):
        """Check if both list of requests sent and expected are same"""

        self.assertEqual(len(self.config_commands_valid), len(self.config_commands_sent))
        for valid_command, sent_command in zip(self.config_commands_valid, self.config_commands_sent):
            self.assertEqual(valid_command, sent_command)

    def setUp(self):
        super(TestSonicCommandModule, self).setUp()
        self.config_commands_sent = []
        self.config_commands_valid = []
        self.run_commands = self.mock_run_commands.start()
        self.run_commands.side_effect = self.run_commands_side_effect

    def tearDown(self):
        super(TestSonicCommandModule, self).tearDown()
        self.mock_run_commands.stop()

    def test_sonic_commands_merged_01(self):
        set_module_args(self.fixture_data['merged_01']['module_args'])
        self.config_commands_valid = self.fixture_data['merged_01']['expected_command_requests']
        result = self.execute_module(changed=False)
        self.validate_config_commands()
