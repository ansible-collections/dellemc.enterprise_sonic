from __future__ import absolute_import, division, print_function
__metaclass__ = type


import unittest
import os
import yaml

import sys
sys.path.append('/root/.ansible/collections')

from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils import (
    get_diff,
)


class TestDiffUtils(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def read_and_compare(self, file_name):
        file_name = os.path.join(os.path.dirname(__file__), file_name)
        file_stream = open(file_name, "r")
        data = yaml.full_load(file_stream)
        file_stream.close()

        want = data.get('want', [])
        have = data.get('have', [])
        diff_exp = data.get('diff', [])
        test_keys = data.get('test_keys', None)
        is_skeleton = data.get('skeleton', None)

        diff_act = get_diff(want, have, test_keys, is_skeleton=is_skeleton)

        self.assertEqual(diff_exp, diff_act)

    def test_01_dict_diff_with_key_name(self):
        self.read_and_compare("test_01_dict_diff_with_key_name.yaml")

    def test_02_dict_diff_with_key_other(self):
        self.read_and_compare("test_02_dict_diff_with_key_other.yaml")

    def test_03_dict_diff_without_key(self):
        self.read_and_compare("test_03_dict_diff_without_key.yaml")

    def test_04_dict_diff_with_similar_dict(self):
        self.read_and_compare("test_04_dict_diff_with_similar_dict.yaml")

    def test_05_dict_diff_left_only(self):
        self.read_and_compare("test_05_dict_diff_left_only.yaml")

    def test_06_dict_diff_left_only_with_none(self):
        self.read_and_compare("test_06_dict_diff_left_only_with_none.yaml")

    def test_07_dict_diff_skeleton_only(self):
        self.read_and_compare("test_07_dict_diff_skeleton_only.yaml")

    def test_08_list_diff_with_key_name(self):
        self.read_and_compare("test_08_list_diff_with_key_name.yaml")

    def test_09_list_diff_with_multi_keys(self):
        self.read_and_compare("test_09_list_diff_with_multi_keys.yaml")

    def test_10_list_diff_with_key_other(self):
        self.read_and_compare("test_10_list_diff_with_key_other.yaml")

    def test_11_list_diff_with_similar_list(self):
        self.read_and_compare("test_11_list_diff_with_similar_list.yaml")

    def test_12_list_diff_with_left_only(self):
        self.read_and_compare("test_12_list_diff_with_left_only.yaml")

    def test_13_list_diff_with_left_only_with_none(self):
        self.read_and_compare("test_13_list_diff_with_left_only_with_none.yaml")

    def test_14_list_diff_skeleton_only(self):
        self.read_and_compare("test_14_list_diff_skeleton_only.yaml")

    def test_15_list_of_list_diff(self):
        self.read_and_compare("test_15_list_of_list_diff.yaml")

    def test_16_complex_list_with_dict_diff(self):
        self.read_and_compare("test_16_complex_list_with_dict_diff.yaml")
