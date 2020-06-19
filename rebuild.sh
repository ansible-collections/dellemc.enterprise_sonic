#!/bin/sh

rm -f /root/ansible_log.log
rm -rf /root/.ansible/collections/ansible_collections/dellemc/*
rm dellemc-sonic-0.0.5.tar.gz
ansible-galaxy collection build
ansible-galaxy collection install dellemc-sonic-0.0.5.tar.gz
# ansible-playbook -i playbooks/common_examples/hosts playbooks/common_examples/sonic_l3_interfaces.yaml -vvvv
# ansible-playbook -i playbooks/common_examples/hosts playbooks/common_examples/sonic_l3_interfaces_config.yaml -vvvv
ansible-playbook -i playbooks/common_examples/hosts playbooks/common_examples/sonic_l3_interfaces_test.yaml -vvvv
