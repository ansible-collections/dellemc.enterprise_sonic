#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2025 Dell Inc. or its subsidiaries. All Rights Reserved.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
---
module: sonic
author: S. Talabi (@stalabi1)
short_description: A dummy module for the sonic action plugin
version_added: "4.0.0"
description:
  - "This is the corresponding module for the `sonic` action plugin."
  - "It is responsible for parameter validation and is not executed directly."
options:
  config:
    description:
      - Dummy configuration
    type: str
    required: true
"""

EXAMPLES = """
"""


from ansible.module_utils.basic import AnsibleModule


def main():
    """Defines the module's parameters."""
    module = AnsibleModule(argument_spec=dict(config=dict(type='str', required=True)),
                           supports_check_mode=True)
    # The action plugin will handle the execution.
    # This module code is generally not executed.
    module.exit_json(changed=False, msg="This module was not executed. The action plugin handled the task.")


if __name__ == '__main__':
    main()
