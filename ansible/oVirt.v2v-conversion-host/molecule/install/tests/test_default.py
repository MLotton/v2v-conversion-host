import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_host_infra_default(host):
    inventory_vars = host.ansible.get_variables()

    # Check wrapper
    assert host.package("v2v-conversion-host-wrapper").is_installed

    # Check package virt-v2v
    assert host.package("virt-v2v").is_installed

    # Check packages nbdkit
    assert host.package("nbdkit").is_installed
    assert host.package("nbdkit-plugin-python2").is_installed

    # Check transport vddk
    if "vddk" == inventory_vars.get("v2v_transport_method"):
        vddk_dir = host.file(inventory_vars.get("v2v_vddk_install_dir") +
                             "/vmware-vix-disklib-distrib")
        assert (vddk_dir.exists and vddk_dir.is_directory)
        assert host.package("nbdkit-plugin-vddk").is_installed

    # Check ca-bundle
    ca_bundle = inventory_vars.get("v2v_ca_bundle")
    if ca_bundle is not None:
        ca_bundle_file = host.file("/etc/pki/ca-trust/source/anchors/"
                                   "v2v-conversion-host-ca-bundle.pem")
        assert (ca_bundle_file.exists and
                ca_bundle_file.user == "root" and
                ca_bundle_file.group == "root" and
                ca_bundle_file.mode == 0o644)


def test_host_infra_openstack(host):
    inventory_vars = host.ansible.get_variables()
    if inventory_vars.get("v2v_host_type") == "openstack":

        # Check transport ssh
        if "ssh" == inventory_vars.get("v2v_transport_method"):
            id_rsa = host.file("/root/.ssh/id_rsa")
            assert (id_rsa.exists and id_rsa.user == "root"
                    and id_rsa.mode == 0o600)

        # Check specific packages
        assert host.package("python2-openstackclient").is_installed
        assert host.package("virtio-win").is_installed
        assert (host.package("python-six").is_installed or
                host.package("python2-six").is_installed)

        # Check cron job file (log cleanup)
        cron_script = host.file("/etc/cron.daily/virt-v2v-logs")
        assert (cron_script.exists and cron_script.user == "root"
                and cron_script.mode == 0o755)


def test_host_infra_rhv(host):
    inventory_vars = host.ansible.get_variables()
    if inventory_vars.get("v2v_host_type") == "rhv":

        # Check transport ssh
        if "ssh" == inventory_vars.get("v2v_transport_method"):
            id_rsa = host.file("/var/lib/vdsm/.ssh/id_rsa")
            assert (id_rsa.exists and id_rsa.user == "vdsm" and
                    id_rsa.mode == 0o600)

        # Check specific packages
        assert host.package("python-ovirt-engine-sdk4").is_installed
