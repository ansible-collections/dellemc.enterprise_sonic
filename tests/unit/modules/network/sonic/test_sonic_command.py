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


class TestSonicInterfacesModule(TestSonicModule):
    module = sonic_command

    @classmethod
    def setUpClass(cls):
        cls.mock_run_commands = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.modules.sonic_command.run_commands"
        )
        cls.fixture_data = cls.load_fixtures('sonic_command.yaml')

    def setUp(self):
        super(TestSonicInterfacesModule, self).setUp()
        self.run_commands = self.mock_run_commands.start()
        self.run_commands.return_value = ['Software Version  : dell_sonic_4.x_share.770-0beb2c821\n']

    def tearDown(self):
        super(TestSonicInterfacesModule, self).tearDown()
        self.mock_run_commands.stop()

    def test_sonic_commands_merged_01(self):
        set_module_args(self.fixture_data['merged_01']['module_args'])
        result = self.execute_module(changed=False)
