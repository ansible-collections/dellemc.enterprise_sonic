from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.dellemc.enterprise_sonic.tests.unit.compat.mock import (
    patch,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.modules import (
    sonic_pki,
)
from ansible_collections.dellemc.enterprise_sonic.tests.unit.modules.utils import (
    set_module_args,
)
from .sonic_module import TestSonicModule


class TestSonicPkiModule(TestSonicModule):
    module = sonic_pki

    @classmethod
    def setUpClass(cls):
        cls.mock_facts_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.pki.pki.edit_config"
        )
        cls.mock_config_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.pki.pki.edit_config"
        )

        cls.fixture_data = cls.load_fixtures("sonic_pki.yaml")

    def setUp(self):
        super(TestSonicPkiModule, self).setUp()
        self.facts_edit_config = self.mock_facts_edit_config.start()
        self.config_edit_config = self.mock_config_edit_config.start()
        self.facts_edit_config.side_effect = self.facts_side_effect
        self.config_edit_config.side_effect = self.config_side_effect

    def tearDown(self):
        super(TestSonicPkiModule, self).tearDown()
        self.mock_facts_edit_config.stop()
        self.mock_config_edit_config.stop()

    def test_sonic_pki_merged_01(self):
        set_module_args(self.fixture_data["merged_01"]["module_args"])
        self.initialize_facts_get_requests(
            self.fixture_data["merged_01"]["existing_pki_config"]
        )
        self.initialize_config_requests(
            self.fixture_data["merged_01"]["expected_config_requests"]
        )
        self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_pki_deleted_01(self):
        set_module_args(self.fixture_data["deleted_01"]["module_args"])
        self.initialize_facts_get_requests(
            self.fixture_data["deleted_01"]["existing_pki_config"]
        )
        self.initialize_config_requests(
            self.fixture_data["deleted_01"]["expected_config_requests"]
        )
        self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_pki_replaced_01(self):
        set_module_args(self.fixture_data["replaced_01"]["module_args"])
        self.initialize_facts_get_requests(
            self.fixture_data["replaced_01"]["existing_pki_config"]
        )
        self.initialize_config_requests(
            self.fixture_data["replaced_01"]["expected_config_requests"]
        )
        self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_pki_overridden_01(self):
        set_module_args(self.fixture_data["overridden_01"]["module_args"])
        self.initialize_facts_get_requests(
            self.fixture_data["overridden_01"]["existing_pki_config"]
        )
        self.initialize_config_requests(
            self.fixture_data["overridden_01"]["expected_config_requests"]
        )
        self.execute_module(changed=True)
        self.validate_config_requests()
