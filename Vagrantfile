# -*- mode: ruby -*-
# vi: set ft=ruby :

## Vagrant :: Ubuntu MySQL :: Vagrant File ##

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config| 

    config.vm.box = "ubuntu/trusty64"

    # VM config
    config.vm.define :ans_mysql do |ansmysql|
        ansmysql.vm.network :private_network, ip: "192.168.2.11"
        ansmysql.vm.network :forwarded_port, host: 3306, guest: 3306
        ansmysql.vm.network :forwarded_port, host: 3307, guest: 3307

        ansmysql.vm.hostname = "mysql-ans"

        ansmysql.vm.provider 'virtualbox' do |v|
            v.customize ['modifyvm', :id, '--name', 'ubuntu-mysql-ans']
            v.customize ['modifyvm', :id, '--cpus', '1']
            v.customize ['modifyvm', :id, '--memory', 2048]
            v.customize ['modifyvm', :id, '--ioapic', 'off']
            v.customize ['modifyvm', :id, '--natdnshostresolver1', 'on']
        end

        # Update package list
        ansmysql.vm.provision :shell, :inline => 'sudo apt-get update'
    end
end
