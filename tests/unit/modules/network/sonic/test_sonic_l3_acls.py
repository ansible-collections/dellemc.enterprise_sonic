from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.dellemc.enterprise_sonic.tests.unit.compat.mock import (
    patch,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.modules import (
    sonic_l3_acls,
)
from ansible_collections.dellemc.enterprise_sonic.tests.unit.modules.utils import (
    set_module_args,
)
from .sonic_module import TestSonicModule


class TestSonicL3AclsModule(TestSonicModule):
    module = sonic_l3_acls

    @classmethod
    def setUpClass(cls):
        cls.mock_facts_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.l3_acls.l3_acls.edit_config"
        )
        cls.mock_config_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.l3_acls.l3_acls.edit_config"
        )
        cls.mock_get_interface_naming_mode = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils.get_device_interface_naming_mode"
        )
        cls.fixture_data = cls.load_fixtures('sonic_l3_acls.yaml')

    def setUp(self):
        super(TestSonicL3AclsModule, self).setUp()
        self.facts_edit_config = self.mock_facts_edit_config.start()
        self.config_edit_config = self.mock_config_edit_config.start()

        self.facts_edit_config.side_effect = self.facts_side_effect
        self.config_edit_config.side_effect = self.config_side_effect

        self.get_interface_naming_mode = self.mock_get_interface_naming_mode.start()
        self.get_interface_naming_mode.return_value = 'standard'

    def tearDown(self):
        super(TestSonicL3AclsModule, self).tearDown()
        self.mock_facts_edit_config.stop()
        self.mock_config_edit_config.stop()
        self.mock_get_interface_naming_mode.stop()

    def validate_config_requests(self):
        # Sort by payload content for requests with same path
        acl_path = 'data/openconfig-acl:acl/acl-sets/acl-set'
        self.config_requests_valid.sort(key=lambda request: (request['path'], request['method'],
                                                             request['data']['acl-set'][0]['name'] if request['path'] == acl_path else ''))
        self.config_requests_sent.sort(key=lambda request: (request['path'], request['method'],
                                                            request['data']['acl-set'][0]['name'] if request['path'] == acl_path else ''))
        super(TestSonicL3AclsModule, self).validate_config_requests(requests_sorted=True)

    def test_sonic_l3_acls_merged_01(self):
        set_module_args(self.fixture_data['merged_01']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['merged_01']['facts_get_requests'])
        self.initialize_config_requests(self.fixture_data['merged_01']['config_requests'])

        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_l3_acls_merged_02(self):
        set_module_args(self.fixture_data['merged_02']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['merged_02']['facts_get_requests'])
        self.initialize_config_requests(self.fixture_data['merged_02']['config_requests'])

        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_l3_acls_replaced_01(self):
        set_module_args(self.fixture_data['replaced_01']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['replaced_01']['facts_get_requests'])
        self.initialize_config_requests(self.fixture_data['replaced_01']['config_requests'])

        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_l3_acls_overridden_01(self):
        set_module_args(self.fixture_data['overridden_01']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['overridden_01']['facts_get_requests'])
        self.initialize_config_requests(self.fixture_data['overridden_01']['config_requests'])

        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_l3_acls_deleted_01(self):
        set_module_args(self.fixture_data['deleted_01']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['deleted_01']['facts_get_requests'])
        self.initialize_config_requests(self.fixture_data['deleted_01']['config_requests'])

        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_l3_acls_deleted_02(self):
        set_module_args(self.fixture_data['deleted_02']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['deleted_02']['facts_get_requests'])
        self.initialize_config_requests(self.fixture_data['deleted_02']['config_requests'])

        result = self.execute_module(changed=True)
        self.validate_config_requests()
