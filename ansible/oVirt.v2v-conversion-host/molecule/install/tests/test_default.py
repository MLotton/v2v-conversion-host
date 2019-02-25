import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_file_example(host):
    f = host.file('/root/.ssh/id_rsa')

    assert f.exists


def test_package_example(host):
    pkg = host.package('virt-v2v')

    assert pkg.is_installed


def test_ansible_variable_get_example(host):
    var = host.ansible.get_variables()

    assert var.get("v2v_host_type") == "openstack"
