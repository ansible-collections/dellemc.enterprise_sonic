#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for sonic_evpn_esi_multihome
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
---
module: sonic_evpn_esi_multihome
version_added: 3.1.0
notes:
  - Tested against Enterprise SONiC Distribution by Dell Technologies.
  - Supports C(check_mode).
short_description: Manage EVPN ESI multihoming configuration on SONiC
description:
  - This module provides configuration management of EVPN ESI multihoming for devices running SONiC
author: Aida Shumburo (@aida-shumburo)
options:
  config:
    description:
      - EVPN ESI multihoming configuration
    type: dict
    suboptions:
      df_election_time:
        description:
          - Election timer value in seconds
          - Has a range of 0 to 86400
          - Default is 3
        type: int
      es_activation_delay:
        description:
          - Activation delay in seconds
          - Has a range of 0 to 1200000
          - Default is 0
        type: int
      mac_holdtime:
        description:
          - MAC hold time in seconds
          - Has a range of 0 to 86400
          - Default is 1080
          - Specify 0 to disable MAC hold time
        type: int
      neigh_holdtime:
        description:
          - Neighbor hold time in seconds
          - Has a range of 0 to 86400
          - Default is 1080
          - Specify 0 to disable neighbor hold time
        type: int
      startup_delay:
        description:
          - Startup delay in seconds
          - Has a range of 0 to 3600
          - Default is 300
          - Specify 0 to disable startup delay
        type: int
  state:
    description:
      - The state of the configuration after module completion
    type: str
    choices: ['merged', 'deleted', 'replaced', 'overridden']
    default: merged
"""

EXAMPLES = """
# Using "deleted" state
#
# Before state:
# ---------------
#
# show running-configuration evpn-mh
#
# evpn esi-multihoming
#  mac-holdtime 1080
#  neigh-holdtime 1080
#  startup-delay 300
#

- name: Delete soecific option from evpn_esi_multihome configuration
  sonic_evpn_esi_multihome:
    config:
      mac-holdtime: 1080
    state: deleted

# After State:
# --------------
#
# show running-configuration evpn-mh
#
# evpn esi-multihoming
#  neigh-holdtime 1080
#  startup-delay 300
#


# Using "deleted" state
#
# Before state:
# ---------------
#
# show running-configuration evpn-mh
#
# evpn esi-multihoming
#  mac-holdtime 1080
#  neigh-holdtime 1080
#  startup-delay 300
#  df-election-time 3

- name: Delete soecific option from evpn_esi_multihome configuration
  sonic_evpn_esi_multihome:
    config: {}
    state: deleted

# After State:
# --------------
#
# show running-configuration evpn-mh
#
#
#


# Using "merged" state
#
# Before state:
# ---------------
#
# show running-configuration evpn-mh
#
#

- name: Merge specific option from evpn_esi_multihome configuration
  sonic_evpn_esi_multihome:
    config:
      startup-delay: 300
      es-activation-delay: 3000
    state: merged

# After State:
# --------------
#
# show running-configuration evpn-mh
#
# evpn esi-multihoming
#  startup-delay 300
#  es-activation-delay 3000


# Using "replaced" state
#
# Before state:
# ----------------
#
# show running-configuration evpn-mh
#
# evpn esi-multihoming
#  mac-holdtime 1080
#  neigh-holdtime 1080
#  startup-delay 300
#  df-election-time: 3

- name: Replace specific option from evpn_esi_multihome configuration
  sonic_evpn_esi_multihome:
    config:
      neigh-holdtime: 200
      df-election-time: 600
    state: replaced

# After State:
# --------------
#
# show running-configuration evpn-mh
#
# evpn esi-multihoming
#  neigh-holdtime 200
#  df-election-time: 600


# Using "overridden" state
#
# Before state:
# ----------------
#
# show running-configuration evpn-mh
#
# evpn esi-multihoming
#  mac-holdtime 1080
#  neigh-holdtime 1080
#  startup-delay 300
#

- name: Override specific option from evpn_esi_multihome configuration
  sonic_evpn_esi_multihome:
    config:
      startup-delay: 200
      mac_holdtime: 500
    state: overridden

# After State:
# --------------
#
# show running-configuration evpn-mh
#
# evpn esi-multihoming
#  startup-delay 200
#  mac_holdtime: 500
"""

RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.evpn_esi_multihome.evpn_esi_multihome import Evpn_esi_multihomeArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.evpn_esi_multihome.evpn_esi_multihome import Evpn_esi_multihome


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=Evpn_esi_multihomeArgs.argument_spec,
                           supports_check_mode=True)

    result = Evpn_esi_multihome(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
