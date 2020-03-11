#!/usr/bin/python
#
# (c) 2015 Peter Sprygada, <psprygada@ansible.com>
# Copyright (c) 2020 Dell Inc.
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = """
---
module: sonic_config
version_added: "2.10"
author: "Abirami N (@abirami-n)"
short_description: Manage SONiC configuration sections
description:
  - SONiC configurations use a simple block indent file syntax
    for segmenting configuration into sections.  This module provides
    an implementation for working with SONiC configuration sections in
    a deterministic way.
extends_documentation_fragment: sonic
options:
  lines:
    description:
      - The ordered set of commands that should be configured in the
        section.  The commands must be the exact same commands as found
        in the device running-config. Be sure to note the configuration
        command syntax as some commands are automatically modified by the
        device config parser. This argument is mutually exclusive with I(src).
    aliases: ['commands']
  parents:
    description:
      - The ordered set of parents that uniquely identify the section or hierarchy
        the commands should be checked against.  If the parents argument
        is omitted, the commands are checked against the set of top
        level or global commands.
  src:
    description:
      - Specifies the source path to the file that contains the configuration
        or configuration template to load.  The path to the source file can
        either be the full path on the Ansible control host or a relative
        path from the playbook or role root directory. This argument is
        mutually exclusive with I(lines).
  before:
    description:
      - The ordered set of commands to push on to the command stack if
        a change needs to be made.  This allows the playbook designer
        the opportunity to perform configuration commands prior to pushing
        any changes without affecting how the set of commands are matched
        against the system.
  after:
    description:
      - The ordered set of commands to append to the end of the command
        stack if a change needs to be made.  Just like with I(before) this
        allows the playbook designer to append a set of commands to be
        executed after the command set.
  save:
    description:
      - The C(save) argument instructs the module to save the running-
        config to the startup-config at the conclusion of the module
        running.  If check mode is specified, this argument is ignored.
    type: bool
    default: 'no'
"""

EXAMPLES = """
- sonic_config:
    lines: ['username {{ user_name }} password {{ user_password }} role {{ user_role }}']

- sonic_config:
    lines:
      - description 'SONiC'
    parents: ['interface Ethernet 40']

- sonic_config:
    lines:
      - seq 2 permit udp any any
      - seq 3 deny icmp any any
    parents: ['ip access-list test']
    before: ['no ip access-list test']

"""

RETURN = """
updates:
  description: The set of commands that will be pushed to the remote device.
  returned: always
  type: list
  sample: ['username foo password foo role admin', 'router bgp 1', 'router-id 1.1.1.1']
commands:
  description: The set of commands that will be pushed to the remote device
  returned: always
  type: list
  sample: ['username foo password foo role admin', 'router bgp 1', 'router-id 1.1.1.1']
saved:
  description: Returns whether the configuration is saved to the startup
               configuration or not.
  returned: When not check_mode.
  type: bool
  sample: True
"""
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc_networking.sonic.plugins.module_utils.network.sonic.sonic import run_commands
from ansible_collections.dellemc_networking.sonic.plugins.module_utils.network.sonic.sonic import load_config, check_args
from ansible.module_utils.network.common.config import NetworkConfig, dumps


def get_candidate(module):
    candidate = NetworkConfig(indent=1)
    if module.params['src']:
        candidate.load(module.params['src'])
    elif module.params['lines']:
        parents = module.params['parents'] or list()
        commands = module.params['lines'][0]
        if (isinstance(commands, dict)) and (isinstance((commands['command']), list)):
            candidate.add(commands['command'], parents=parents)
        elif (isinstance(commands, dict)) and (isinstance((commands['command']), str)):
            candidate.add([commands['command']], parents=parents)
        else:
            candidate.add(module.params['lines'], parents=parents)
    return candidate


def main():

    argument_spec = dict(
        lines=dict(aliases=['commands'], type='list'),
        parents=dict(type='list'),

        src=dict(type='path'),

        before=dict(type='list'),
        after=dict(type='list'),
        save=dict(type='bool', default=False),
        config=dict(),
    )

    mutually_exclusive = [('lines', 'src')]

    module = AnsibleModule(argument_spec=argument_spec,
                           mutually_exclusive=mutually_exclusive,
                           supports_check_mode=True)

    parents = module.params['parents'] or list()

    warnings = list()
    check_args(module, warnings)

    result = dict(changed=False, saved=False, warnings=warnings)

    commands = list()
    candidate = get_candidate(module)

    if any((module.params['lines'], module.params['src'])):
        configobjs = candidate.items

        if configobjs:
            commands = dumps(configobjs, 'commands')
            if ((isinstance((module.params['lines']), list)) and
                    (isinstance((module.params['lines'][0]), dict)) and
                    (set(['prompt', 'answer']).issubset(module.params['lines'][0]))):

                cmd = {'command': commands,
                       'prompt': module.params['lines'][0]['prompt'],
                       'answer': module.params['lines'][0]['answer']}
                commands = [module.jsonify(cmd)]
            else:
                commands = commands.split('\n')

            if module.params['before']:
                commands[:0] = module.params['before']

            if module.params['after']:
                commands.extend(module.params['after'])

            if not module.check_mode:
                load_config(module, commands)

            result['changed'] = True
            result['commands'] = commands
            result['updates'] = commands

    if module.params['save']:
        result['changed'] = True
        if not module.check_mode:
            cmd = {r'command': ' write memory'}
            run_commands(module, [cmd])
            result['saved'] = True

    module.exit_json(**result)


if __name__ == '__main__':
    main()
