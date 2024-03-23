from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.dellemc.enterprise_sonic.tests.unit.compat.mock import (
    patch,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.modules import (
    sonic_facts,
)
from ansible_collections.dellemc.enterprise_sonic.tests.unit.modules.utils import (
    set_module_args,
)
from .sonic_module import TestSonicModule


class TestSonicFactsModule(TestSonicModule):
    module = sonic_facts

    @classmethod
    def setUpClass(cls):
        cls.mock_get_network_resources_facts = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.facts.FactsBase.get_network_resources_facts"
        )
        cls.fixture_data = cls.load_fixtures('sonic_facts.yaml')

    def setUp(self):
        super(TestSonicFactsModule, self).setUp()
        self.get_network_resources_facts = self.mock_get_network_resources_facts.start()
        self.get_network_resources_facts.return_value = ({
            'ansible_network_resources': {'bgp': [{'bgp_as': '24', 'router_id': '10.1.1.1', 'log_neighbor_changes': True, 'vrf_name': 'default',
                                          'timers': {'holdtime': 180, 'keepalive_interval': 60},
                                                  'bestpath': {'as_path': {'confed': False, 'ignore': False, 'multipath_relax': True,
                                                                           'multipath_relax_as_set': False},
                                                               'med': {'confed': False, 'missing_as_worst': False, 'always_compare_med': False},
                                                               'compare_routerid': False}, 'max_med': None}]},
            'ansible_net_gather_network_resources': ['bgp'], 'ansible_net_gather_subset': []}, [])

    def tearDown(self):
        super(TestSonicFactsModule, self).tearDown()
        self.mock_get_network_resources_facts.stop()

    def test_sonic_facts_merged_01(self):
        set_module_args(self.fixture_data['merged_01']['module_args'])
        result = self.execute_module(changed=False)
