#!/usr/bin/env python

def test_if_sudo_package_is_installed(host):
    assert host.package("sudo").is_installed

def test_sudoers_file_properties(host):
    _sudo_file_config = host.file("/etc/sudoers")
    assert not _sudo_file_config.contains("#includedir /etc/sudoers.d")
    assert _sudo_file_config.mode == 0o640
    assert _sudo_file_config.user == 'root'
    assert _sudo_file_config.group == 'root'

def test_if_sudoers_d_is_not_empty_and_contains(host):
    assert host.file("/etc/sudoers.d").listdir() != []


def test_sudo_commands_is_working(host):
    _sudo_cmd = host.run("su - firstusersudo -c 'tail /dev/null'")
    assert _sudo_cmd.rc <= 0
