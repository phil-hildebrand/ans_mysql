# Ansible Based MySQL Deployment Tool

![](https://travis-ci.org/phil-hildebrand/ans_mysql.svg?branch=master)

# Overview

This project installs and configures MySQL via ansible

# Requirements

- pip
- ansible

# Installation

- Clone https://github.com/phil-hildebrand/ans_mysql locally

_if ansible needed_

```
$ sudo pip install ansible
```

## Dev Environment Setup

- Assumes Virtualbox Installed
- Vagrant >= 1.7.2

```
  $ cd <repo_path>/ans_mysql
  $ vagrant box add ubuntu/trusty64
  $ vagrant up
  $ ssh-add .vagrant/machines/ans_mysql/virtualbox/private_key 
  $ ansible -i inventory dev -m ping
  
```

1. Run `$ ansible-playbook -v -b playbooks/main.yml  -l 192.168.2.11`
2. MySQL should be available either directly on localhost with `mysql` or at 192.168.2.11 with `mysql -h 192.168.2.11` 

## Options

- force: \[ true | false \] (`default=false`) - Remove existing mysql instances
- data_dir: ( `default=/data`) - Where to put mysql data & log directories
- backup_dir: ( `/backup` ) - Where to put mysql backups of existing data if `force=true`
- version: \[ 5.5 | 5.6 | 5.7 \] (`default=5.7`) - Major version of MySQL to install
- db\_port: (`default=3306`) - MySQL port to listen on
- db\_extra\_port: (`default=3307`) - MySQL port for administration emergencies
- root\_pass: (`default=test`) - Creds for root user

## Deployment

1. Update inventory file (`./inventory`) with ip/hostname of node being deployed to
2. Run ansible with appropriate variables
```
   $ ansible-playbook -v -b -i inventory playbooks/main.yml  -l hostname or ip --extra-vars "version=5.6" 
```

_Note: Any option can be changed at deploy time by seeting it in the --extra-vars string: --extra-vars "[option=value option=value ...]"_

## Known Issues

- Currently it does configure replication
