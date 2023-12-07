from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.dellemc.enterprise_sonic.tests.unit.compat.mock import (
    patch,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.modules import (
    sonic_image_management,
)
from ansible_collections.dellemc.enterprise_sonic.tests.unit.modules.utils import (
    set_module_args,
)
from .sonic_module import TestSonicModule


class TestSonicImageManagementModule(TestSonicModule):
    module = sonic_image_management

    @classmethod
    def setUpClass(cls):
        cls.mock_module_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.modules.sonic_image_management.edit_config"
        )
        cls.fixture_data = cls.load_fixtures('sonic_image_management.yaml')

    def setUp(self):
        super(TestSonicImageManagementModule, self).setUp()
        self.module_edit_config = self.mock_module_edit_config.start()

    def tearDown(self):
        super(TestSonicImageManagementModule, self).tearDown()
        self.mock_module_edit_config.stop()

    def test_sonic_image_management_image_install(self):
        set_module_args(self.fixture_data['image_install']['module_args'])
        self.initialize_config_requests(self.fixture_data['image_install']['requests'])
        self.module_edit_config.side_effect = self.config_side_effect
        status = 'Check image -> command = get-status for image install progress'

        result = self.execute_module()
        self.validate_config_requests()
        self.assertNotIn('info', result)
        self.assertIn('status', result)
        self.assertEqual(status, result['status'])

    def test_sonic_image_management_image_install_ignore_name(self):
        module_args = self.fixture_data['image_install']['module_args'].copy()
        module_args['image']['name'] = 'test.bin'
        set_module_args(module_args)

        self.initialize_config_requests(self.fixture_data['image_install']['requests'])
        self.module_edit_config.side_effect = self.config_side_effect
        status = 'Check image -> command = get-status for image install progress'
        warnings = ['image -> name is ignored when image -> command = install']

        result = self.execute_module()
        self.validate_config_requests()
        self.assertNotIn('info', result)
        self.assertIn('status', result)
        self.assertEqual(status, result['status'])
        self.assertEqual(warnings, result['warnings'])

    def test_sonic_image_management_image_cancel(self):
        set_module_args(self.fixture_data['image_cancel']['module_args'])
        self.initialize_config_requests(self.fixture_data['image_cancel']['requests'])
        self.module_edit_config.side_effect = self.config_side_effect
        status = 'SUCCESS'

        result = self.execute_module()
        self.validate_config_requests()
        self.assertNotIn('info', result)
        self.assertIn('status', result)
        self.assertEqual(status, result['status'])

    def test_sonic_image_management_image_remove(self):
        set_module_args(self.fixture_data['image_remove']['module_args'])
        self.initialize_config_requests(self.fixture_data['image_remove']['requests'])
        self.module_edit_config.side_effect = self.config_side_effect
        status = 'SUCCESS'

        result = self.execute_module()
        self.validate_config_requests()
        self.assertNotIn('info', result)
        self.assertIn('status', result)
        self.assertEqual(status, result['status'])

    def test_sonic_image_management_image_remove_ignore_path(self):
        module_args = self.fixture_data['image_remove']['module_args'].copy()
        module_args['image']['path'] = 'file://home/admin/test.bin'
        set_module_args(module_args)

        self.initialize_config_requests(self.fixture_data['image_remove']['requests'])
        self.module_edit_config.side_effect = self.config_side_effect
        status = 'SUCCESS'
        warnings = ['image -> path is ignored when image -> command = remove']

        result = self.execute_module()
        self.validate_config_requests()
        self.assertNotIn('info', result)
        self.assertIn('status', result)
        self.assertEqual(status, result['status'])
        self.assertEqual(warnings, result['warnings'])

    def test_sonic_image_management_image_set_default(self):
        set_module_args(self.fixture_data['image_set_default']['module_args'])
        self.initialize_config_requests(self.fixture_data['image_set_default']['requests'])
        self.module_edit_config.side_effect = self.config_side_effect
        status = 'SUCCESS'

        result = self.execute_module()
        self.validate_config_requests()
        self.assertNotIn('info', result)
        self.assertIn('status', result)
        self.assertEqual(status, result['status'])

    def test_sonic_image_management_image_get_list(self):
        set_module_args(self.fixture_data['image_get_list']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['image_get_list']['requests'])
        self.module_edit_config.side_effect = self.facts_side_effect
        info = self.fixture_data['image_get_list']['info_output']

        result = self.execute_module()
        self.validate_config_requests()
        self.assertNotIn('status', result)
        self.assertIn('info', result)
        self.assertEqual(info, result['info'])

    def test_sonic_image_management_image_get_status_01(self):
        set_module_args(self.fixture_data['image_get_status_01']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['image_get_status_01']['requests'])
        self.module_edit_config.side_effect = self.facts_side_effect
        info = self.fixture_data['image_get_status_01']['info_output']

        result = self.execute_module()
        self.validate_config_requests()
        self.assertNotIn('status', result)
        self.assertIn('info', result)
        self.assertEqual(info, result['info'])

    def test_sonic_image_management_image_get_status_02(self):
        set_module_args(self.fixture_data['image_get_status_02']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['image_get_status_02']['requests'])
        self.module_edit_config.side_effect = self.facts_side_effect
        info = self.fixture_data['image_get_status_02']['info_output']

        result = self.execute_module()
        self.validate_config_requests()
        self.assertNotIn('status', result)
        self.assertIn('info', result)
        self.assertEqual(info, result['info'])

    def test_sonic_image_management_patch_install(self):
        set_module_args(self.fixture_data['patch_install']['module_args'])
        self.initialize_config_requests(self.fixture_data['patch_install']['requests'])
        self.module_edit_config.side_effect = self.config_side_effect
        status = 'Check patch -> command = get-status for patch install progress'

        result = self.execute_module()
        self.validate_config_requests()
        self.assertNotIn('info', result)
        self.assertIn('status', result)
        self.assertEqual(status, result['status'])

    def test_sonic_image_management_patch_rollback(self):
        set_module_args(self.fixture_data['patch_rollback']['module_args'])
        self.initialize_config_requests(self.fixture_data['patch_rollback']['requests'])
        self.module_edit_config.side_effect = self.config_side_effect
        status = 'Check patch -> command = get-status for patch rollback progress'

        result = self.execute_module()
        self.validate_config_requests()
        self.assertNotIn('info', result)
        self.assertIn('status', result)
        self.assertEqual(status, result['status'])

    def test_sonic_image_management_patch_get_list(self):
        set_module_args(self.fixture_data['patch_get_list']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['patch_get_list']['requests'])
        self.module_edit_config.side_effect = self.facts_side_effect
        info = self.fixture_data['patch_get_list']['info_output']

        result = self.execute_module()
        self.validate_config_requests()
        self.assertNotIn('status', result)
        self.assertIn('info', result)
        self.assertEqual(info, result['info'])

    def test_sonic_image_management_patch_get_history(self):
        set_module_args(self.fixture_data['patch_get_history']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['patch_get_history']['requests'])
        self.module_edit_config.side_effect = self.facts_side_effect
        info = self.fixture_data['patch_get_history']['info_output']

        result = self.execute_module()
        self.validate_config_requests()
        self.assertNotIn('status', result)
        self.assertIn('info', result)
        self.assertEqual(info, result['info'])

    def test_sonic_image_management_patch_get_status(self):
        set_module_args(self.fixture_data['patch_get_status']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['patch_get_status']['requests'])
        self.module_edit_config.side_effect = self.facts_side_effect
        info = self.fixture_data['patch_get_status']['info_output']

        result = self.execute_module()
        self.validate_config_requests()
        self.assertNotIn('status', result)
        self.assertIn('info', result)
        self.assertEqual(info, result['info'])

    def test_sonic_image_management_firmware_install(self):
        set_module_args(self.fixture_data['firmware_install']['module_args'])
        self.initialize_config_requests(self.fixture_data['firmware_install']['requests'])
        self.module_edit_config.side_effect = self.config_side_effect
        status = 'Check firmware -> command = get-status for firmware package staging progress'

        result = self.execute_module()
        self.validate_config_requests()
        self.assertNotIn('info', result)
        self.assertIn('status', result)
        self.assertEqual(status, result['status'])

    def test_sonic_image_management_firmware_get_list(self):
        set_module_args(self.fixture_data['firmware_get_list']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['firmware_get_list']['requests'])
        self.module_edit_config.side_effect = self.facts_side_effect
        info = self.fixture_data['firmware_get_list']['info_output']

        result = self.execute_module()
        self.validate_config_requests()
        self.assertNotIn('status', result)
        self.assertIn('info', result)
        self.assertEqual(info, result['info'])

    def test_sonic_image_management_firmware_get_status(self):
        set_module_args(self.fixture_data['firmware_get_status']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['firmware_get_status']['requests'])
        self.module_edit_config.side_effect = self.facts_side_effect
        info = self.fixture_data['firmware_get_status']['info_output']

        result = self.execute_module()
        self.validate_config_requests()
        self.assertNotIn('status', result)
        self.assertIn('info', result)
        self.assertEqual(info, result['info'])

    def test_sonic_image_management_invalid_args_01(self):
        set_module_args({
            'image': {'command': 'install', 'path': 'file://home/admin/sonic.bin'},
            'firmware': {'command': 'install', 'path': 'file://home/admin/firmware.bin'},
        })
        msg = 'Only one image management operation can be performed at a time'

        result = self.execute_module(failed=True)
        self.assertEqual(msg, result['msg'])

    def test_sonic_image_management_invalid_args_02(self):
        set_module_args({
            'image': {'command': 'remove', 'path': 'file://home/admin/sonic.bin'}
        })
        msg = 'image -> name is required when image -> command = remove'

        result = self.execute_module(failed=True)
        self.assertEqual(msg, result['msg'])

    def test_sonic_image_management_invalid_args_03(self):
        set_module_args({
            'image': {'command': 'install', 'name': 'sonic.bin'}
        })
        msg = 'image -> path is required when image -> command = install'

        result = self.execute_module(failed=True)
        self.assertEqual(msg, result['msg'])
