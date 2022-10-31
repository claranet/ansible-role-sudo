# Ansible role - sudo
[![Maintainer](https://img.shields.io/badge/maintained%20by-claranet-e00000?style=flat-square)](https://www.claranet.fr/)
[![License](https://img.shields.io/github/license/claranet/ansible-role-sudo?style=flat-square)](LICENSE)
[![Release](https://img.shields.io/github/v/release/claranet/ansible-role-sudo?style=flat-square)](https://github.com/claranet/ansible-role-sudo/releases)
[![Status](https://img.shields.io/github/workflow/status/claranet/ansible-role-sudo/Ansible%20Molecule?style=flat-square&label=tests)](https://github.com/claranet/ansible-role-sudo/actions?query=workflow%3A%22Ansible+Molecule%22)
[![Ansible version](https://img.shields.io/badge/ansible-%3E%3D2.10-black.svg?style=flat-square&logo=ansible)](https://github.com/ansible/ansible)
[![Ansible Galaxy](https://img.shields.io/badge/ansible-galaxy-black.svg?style=flat-square&logo=ansible)](https://galaxy.ansible.com/claranet/sudo)


> :star: Star us on GitHub — it motivates us a lot!

Install and Configure sudo

## :warning: Requirements

Ansible >= 2.10

## :zap: Installation

```bash
ansible-galaxy install claranet.sudo
```

## :gear: Role variables

Variable | Default value | Description
---------|---------------|------------
sudo_sudoers_dir | /etc/sudoers.d | directory which contains sudo rigths files
sudo_install_package | true | install sudo package before set rigths
sudo_rigths    | **null**      | contains all sudo rigths to set
sudo_purge_others_sudoers_files | false | purge others file which aren't in our sudo rights configuration
sudo_sudoers_cmnd_aliases | {} | set command alias: name of command alias as key and list of commands as value
sudo_sudoers_user_aliases | {} | set user alias: name of user alias as key and list of users as value
sudo_sudoers_host_aliases | {} | set host alias: name of host alias as key and list of host as values
sudo_sudoers_runas_aliases | {} | set sudoers run as


## :arrows_counterclockwise: Dependencies

N/A

## :pencil2: Example Playbook

```yaml
---
- hosts: all
  vars:
      sudo_purge_others_sudoers_files: true

      sudo_sudoers_user_aliases: {
        test: ["secondusersudo", "firstusersudo"]
      }

      sudo_sudoers_cmnd_aliases : {
        SHUTDOWN: ["/usr/sbin/reboot","/usr/sbin/poweroff"]
      }

      sudo_rights:
        allowrebootsudo:
          - name: "TEST"
            no_passwd: true
            from_hosts: ALL
            as_user: ALL
            as_group: ALL
            commands: SHUTDOWN
            state: present

        allowtailsudo:
          - name: "firstusersudo"
            no_passwd: true
            from_hosts: ALL
            as_user: ALL
            as_group: ALL
            commands:
              - /usr/bin/tail -f /dev/null
            state: present
    roles:
      - role: claranet.sudo
```

## :closed_lock_with_key: [Hardening](HARDENING.md)

## :heart_eyes_cat: [Contributing](CONTRIBUTING.md)

## :copyright: [License](LICENSE)

[Mozilla Public License Version 2.0](https://www.mozilla.org/en-US/MPL/2.0/)
