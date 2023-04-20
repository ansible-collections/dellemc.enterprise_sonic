#!/usr/bin/python
# -*- coding: utf-8 -*-
# © Copyright 2020 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for sonic_bgp
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
---
module: sonic_bgp
version_added: 1.0.0
notes:
- Tested against Enterprise SONiC Distribution by Dell Technologies.
- Supports C(check_mode).
author: Dhivya P (@dhivayp)
short_description: Manage global BGP and its parameters
description:
  - This module provides configuration management of global BGP parameters on devices running Enterprise SONiC Distribution by Dell Technologies.
options:
  config:
    description:
      - Specifies the BGP-related configuration.
    type: list
    elements: dict
    suboptions:
      bgp_as:
        description:
          - Specifies the BGP autonomous system (AS) number to configure on the device.
        type: str
        required: true
      vrf_name:
        description:
          - Specifies the VRF name.
        type: str
        default: 'default'
      router_id:
        description:
          - Configures the BGP routing process router-id value.
        type: str
      log_neighbor_changes:
        description:
          - Enables/disables logging neighbor up/down and reset reason.
        type: bool
      max_med:
        description:
          - Configure max med and its parameters
        type: dict
        suboptions:
          on_startup:
            description:
              - On startup time and max-med value
            type: dict
            suboptions:
              timer:
                description:
                  - Configures on startup time
                type: int
              med_val:
                description:
                  - on startup med value
                type: int
      timers:
        description:
          - Adjust routing timers
        type: dict
        suboptions:
          holdtime:
            description:
              - Configures hold-time
            type: int
          keepalive_interval:
            description:
              - Configures keepalive-interval
            type: int
      bestpath:
        description:
          - Configures the BGP best-path.
        type: dict
        suboptions:
          as_path:
            description:
              - Configures the as-path values.
            type: dict
            suboptions:
              confed:
                description:
                  - Configures the confed values of as-path.
                type: bool
              ignore:
                description:
                  - Configures the ignore values of as-path.
                type: bool
              multipath_relax:
                description:
                  - Configures the multipath_relax values of as-path.
                type: bool
              multipath_relax_as_set:
                description:
                  - Configures the multipath_relax_as_set values of as-path.
                type: bool
          compare_routerid:
            description:
              - Configures the compare_routerid.
            type: bool
          med:
            description:
              - Configures the med values.
            type: dict
            suboptions:
              confed:
                description:
                  - Configures the confed values of med.
                type: bool
              missing_as_worst:
                description:
                  - Configures the missing_as_worst values of as-path.
                type: bool
              always_compare_med:
                description:
                  - Allows comparing meds from different neighbors if set to true
                type: bool
  state:
    description:
      - Specifies the operation to be performed on the BGP process that is configured on the device.
      - In case of merged, the input configuration is merged with the existing BGP configuration on the device.
      - In case of deleted, the existing BGP configuration is removed from the device.
      - In case of replaced, the existing configuration of the specified BGP AS will be replaced with provided configuration.
      - In case of overridden, the existing BGP configuration will be overridden with the provided configuration.
    default: merged
    choices: ['merged', 'deleted', 'replaced', 'overridden']
    type: str
"""
EXAMPLES = """
# Using deleted
#
# Before state:
# -------------
#
#!
#router bgp 10 vrf VrfCheck1
# router-id 10.2.2.32
# log-neighbor-changes
#!
#router bgp 11 vrf VrfCheck2
# log-neighbor-changes
# bestpath as-path ignore
# bestpath med missing-as-worst confed
# bestpath compare-routerid
#!
#router bgp 4
# router-id 10.2.2.4
# bestpath as-path ignore
# bestpath as-path confed
# bestpath med missing-as-worst confed
# bestpath compare-routerid
#!
#
- name: Delete BGP Global attributes
  dellemc.enterprise_sonic.sonic_bgp:
    config:
       - bgp_as: 4
         router_id: 10.2.2.4
         log_neighbor_changes: False
         bestpath:
           as_path:
             confed: True
             ignore: True
             multipath_relax: False
             multipath_relax_as_set: True
           compare_routerid: True
           med:
             confed: True
             missing_as_worst: True
       - bgp_as: 10
         router_id: 10.2.2.32
         log_neighbor_changes: True
         vrf_name: 'VrfCheck1'
       - bgp_as: 11
         log_neighbor_changes: True
         vrf_name: 'VrfCheck2'
         bestpath:
           as_path:
             confed: False
             ignore: True
             multipath_relax_as_set: True
           compare_routerid: True
           med:
             confed: True
             missing_as_worst: True
    state: deleted


# After state:
# ------------
#
#!
#router bgp 10 vrf VrfCheck1
# log-neighbor-changes
#!
#router bgp 11 vrf VrfCheck2
# log-neighbor-changes
# bestpath compare-routerid
#!
#router bgp 4
# log-neighbor-changes
# bestpath compare-routerid
#!


# Using deleted
#
# Before state:
# -------------
#
#!
#router bgp 10 vrf VrfCheck1
# router-id 10.2.2.32
# log-neighbor-changes
#!
#router bgp 11 vrf VrfCheck2
# log-neighbor-changes
# bestpath as-path ignore
# bestpath med missing-as-worst confed
# bestpath compare-routerid
#!
#router bgp 4
# router-id 10.2.2.4
# bestpath as-path ignore
# bestpath as-path confed
# bestpath med missing-as-worst confed
# bestpath compare-routerid
#!

- name: Deletes all the bgp global configurations
  dellemc.enterprise_sonic.sonic_bgp:
     config:
     state: deleted

# After state:
# ------------
#
#!
#!


# Using merged
#
# Before state:
# -------------
#
#!
#router bgp 4
# router-id 10.1.1.4
#!
#
- name: Merges provided configuration with device configuration
  dellemc.enterprise_sonic.sonic_bgp:
     config:
       - bgp_as: 4
         router_id: 10.2.2.4
         log_neighbor_changes: False
         timers:
           holdtime: 20
           keepalive_interval: 30
         bestpath:
           as_path:
             confed: True
             ignore: True
             multipath_relax: False
             multipath_relax_as_set: True
           compare_routerid: True
           med:
             confed: True
             missing_as_worst: True
             always_compare_med: True
         max_med:
           on_startup:
             timer: 667
             med_val: 7878
       - bgp_as: 10
         router_id: 10.2.2.32
         log_neighbor_changes: True
         vrf_name: 'VrfCheck1'
       - bgp_as: 11
         log_neighbor_changes: True
         vrf_name: 'VrfCheck2'
         bestpath:
           as_path:
             confed: False
             ignore: True
             multipath_relax_as_set: True
           compare_routerid: True
           med:
             confed: True
             missing_as_worst: True
     state: merged
#
# After state:
# ------------
#
#!
#router bgp 10 vrf VrfCheck1
# router-id 10.2.2.32
# log-neighbor-changes
#!
#router bgp 11 vrf VrfCheck2
# log-neighbor-changes
# bestpath as-path ignore
# bestpath med missing-as-worst confed
# bestpath compare-routerid
#!
#router bgp 4
# router-id 10.2.2.4
# bestpath as-path ignore
# bestpath as-path confed
# bestpath med missing-as-worst confed
# bestpath compare-routerid
# always-compare-med
# max-med on-startup 667 7878
# timers 20 30
#
#!


# Using replaced
#
# Before state:
# -------------
#
#!
#router bgp 10 vrf VrfCheck1
# router-id 10.2.2.32
# log-neighbor-changes
# timers 60 180
#!
#router bgp 4
# router-id 10.2.2.4
# max-med on-startup 667 7878
# bestpath as-path ignore
# bestpath as-path confed
# bestpath med missing-as-worst confed
# bestpath compare-routerid
# timers 20 30
#!
#

  - name: Replace device configuration of specified BGP AS with provided
    dellemc.enterprise_sonic.sonic_bgp:
      config:
        - bgp_as: 4
          router_id: 10.2.2.44
          log_neighbor_changes: True
          bestpath:
            as_path:
              confed: True
            compare_routerid: True
        - bgp_as: 11
          vrf_name: 'VrfCheck2'
          router_id: 10.2.2.33
          log_neighbor_changes: True
          bestpath:
            as_path:
              confed: True
              ignore: True
            compare_routerid: True
            med:
              confed: True
              missing_as_worst: True
      state: replaced

#
# After state:
# ------------
#
#!
#router bgp 10 vrf VrfCheck1
# router-id 10.2.2.32
# log-neighbor-changes
# timers 60 180
#!
#router bgp 11 vrf VrfCheck2
# router-id 10.2.2.33
# log-neighbor-changes
# bestpath as-path ignore
# bestpath as-path confed
# bestpath med missing-as-worst confed
# bestpath compare-routerid
# timers 60 180
#!
#router bgp 4
# router-id 10.2.2.44
# log-neighbor-changes
# bestpath as-path confed
# bestpath compare-routerid
# timers 60 180
#!


# Using overridden
#
# Before state:
# -------------
#
#!
#router bgp 10 vrf VrfCheck1
# router-id 10.2.2.32
# log-neighbor-changes
# timers 60 180
#!
#router bgp 4
# router-id 10.2.2.4
# max-med on-startup 667 7878
# bestpath as-path ignore
# bestpath as-path confed
# bestpath med missing-as-worst confed
# bestpath compare-routerid
# timers 20 30
#!
#

  - name: Override device configuration of global BGP with provided configuration
    dellemc.enterprise_sonic.sonic_bgp:
      config:
        - bgp_as: 4
          router_id: 10.2.2.44
          log_neighbor_changes: True
          bestpath:
            as_path:
              confed: True
            compare_routerid: True
        - bgp_as: 11
          vrf_name: 'VrfCheck2'
          router_id: 10.2.2.33
          log_neighbor_changes: True
          bestpath:
            as_path:
              confed: True
              ignore: True
            compare_routerid: True
          timers:
            holdtime: 90
            keepalive_interval: 30
      state: overridden

#
# After state:
# ------------
#
#!
#router bgp 11 vrf VrfCheck2
# router-id 10.2.2.33
# log-neighbor-changes
# bestpath as-path ignore
# bestpath as-path confed
# bestpath compare-routerid
# timers 30 90
#!
#router bgp 4
# router-id 10.2.2.44
# log-neighbor-changes
# bestpath as-path confed
# bestpath compare-routerid
# timers 60 180
#!


"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: list
  sample: >
    The configuration returned is always in the same format
    of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: list
  sample: >
    The configuration returned is always in the same format
    of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.bgp.bgp import BgpArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.bgp.bgp import Bgp


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=BgpArgs.argument_spec,
                           supports_check_mode=True)

    result = Bgp(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
