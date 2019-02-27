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


# TODO add "assert false" in certain configurations
# (ex: no ssh and vddk defined, no manageiq, etc)
def test_host_infra_default(host):
    inventory_vars = host.ansible.get_variables()

    # Check wrapper
    wrapper = host.file("/usr/bin/virt-v2v-wrapper.py")
    assert (wrapper.exists and wrapper.mode == 0o755)

    # Check package virt-v2v
    assert host.package("virt-v2v").is_installed

    # Check packages nbdkit
    assert host.package("nbdkit").is_installed
    assert host.package("nbdkit-plugin-python2").is_installed

    # Check transport vddk
    if "vddk" in inventory_vars.get("v2v_transport_methods"):
        vddk_dir = host.file(inventory_vars.get("v2v_vddk_install_dir") +
                             "/vmware-vix-disklib-distrib")
        assert (vddk_dir.exists and vddk_dir.is_directory)
        assert host.package("nbdkit-plugin-vddk").is_installed

    # Check manageiq / cloudforms
    providers = inventory_vars.get("manageiq_providers")
    host_provider_name = inventory_vars.get("manageiq_provider_name")
    for provider in providers:
        if provider.get("name") == host_provider_name:
            provider_host = provider
            break
    else:
        provider_host = None

    if provider_host is not None:

        # Check CA chain file
        for connection_conf in provider_host.get("connection_configurations"):
            endpoint = connection_conf.get("endpoint")
            if endpoint.get("role") == "default":
                certificate_authority = endpoint.get("certificate_authority")
                break
        else:
            certificate_authority = None

        if certificate_authority is not None:
            ca_chain = host.file("/etc/pki/ca-trust/source/anchors/" +
                                 provider_host.get("hostname") +
                                 "-ca-chain.pem")
            assert (ca_chain.exists and ca_chain.user == "root"
                    and ca_chain.mode == 0o644)


def test_host_infra_openstack(host):
    inventory_vars = host.ansible.get_variables()
    if inventory_vars.get("v2v_host_type") == "openstack":

        # Check repo dir
        repo_data = host.file("/opt/yum/empty/repodata")
        assert (repo_data.exists and repo_data.is_directory)

        # Check transport ssh
        if "ssh" in inventory_vars.get("v2v_transport_methods"):
            id_rsa = host.file("/root/.ssh/id_rsa")
            assert (id_rsa.exists and id_rsa.user == "root"
                    and id_rsa.mode == 0o600)

        # Check specific packages
        assert host.package("python2-openstackclient").is_installed
        assert host.package("virtio-win").is_installed
        assert (host.package("python-six").is_installed or
                host.package("python2-six").is_installed)

        # Check cron job file (log cleanup)
        cron_script = host.file("/etc/cron.daily/virt-v2-logs")
        assert (cron_script.exists and cron_script.user == "root"
                and cron_script.mode == 0o755)


def test_host_infra_rhv(host):
    inventory_vars = host.ansible.get_variables()
    if inventory_vars.get("v2v_host_type") == "rhv":

        # Check transport ssh
        if "ssh" in inventory_vars.get("v2v_transport_methods"):
            id_rsa = host.file("/var/lib/vdsm/.ssh/id_rsa")
            assert (id_rsa.exists and id_rsa.user == "vdsm" and
                    id_rsa.mode == 0o600)

        # Check specific packages
        assert host.package("python-ovirt-engine-sdk4").is_installed
