#!/usr/bin/env bash
ver=$1
extras="env=vagrant force=true version=${ver}"

cd /vagrant
apt-get update
apt-get purge -y puppet
apt-get install -y python-setuptools build-essential libssl-dev libffi-dev python-dev git
easy_install pip
pip install --upgrade virtualenv
virtualenv venv
. /vagrant/venv/bin/activate
pip install -r requirements.txt
ansible-playbook -vv -b -i inventory playbooks/main.yml  -l localhost --connection=local --extra-vars "${extras}"
echo ". /vagrant/venv/bin/activate" >> ~vagrant/.bashrc
