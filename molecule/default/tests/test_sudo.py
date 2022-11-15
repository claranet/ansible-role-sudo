#!/usr/bin/env python

def test_if_sudo_package_is_installed(host):
    assert host.package("sudo").is_installed

def test_sudoers_file_properties(host):
    _sudo_file_config = host.file("/etc/sudoers")
    assert _sudo_file_config.mode == 0o440
    assert _sudo_file_config.user == 'root'
    assert _sudo_file_config.group == 'root'
    assert host.run('visudo -c').rc <= 0

def test_syntax_of_sudoers_files(host):
    _sudo_config_dir = "/etc/sudoers.d"
    for file in  host.file(_sudo_config_dir).listdir():
        assert host.run("visudo -cf {}/{}".format(_sudo_config_dir,file)).rc <= 0

def test_if_sudo_commands_is_working(host):
    _sudo_cmd = host.run("su - firstusersudo -c 'sudo tail /dev/null'")
    assert _sudo_cmd.rc <= 0
