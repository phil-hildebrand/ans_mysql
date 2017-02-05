# -*- mode: ruby -*-
# vi: set ft=ruby :

## Vagrant :: Ubuntu MySQL :: Vagrant File ##

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config| 
    config.ssh.forward_agent = true
    config.ssh.insert_key = false
    config.ssh.private_key_path = [ '~/.vagrant.d/insecure_private_key' ]

    config.vm.box = "ubuntu/trusty64"

    # VM config 5.7
    config.vm.define :mysql57, autostart: true do |mysql57|
        mysql57.vm.network :private_network, ip: "192.168.1.57"
        mysql57.vm.network :forwarded_port, host: 3306, guest: 3306
        mysql57.vm.network :forwarded_port, host: 3307, guest: 3307

        mysql57.vm.hostname = "mysql-57"

        mysql57.vm.provider 'virtualbox' do |v|
            v.customize ['modifyvm', :id, '--name', 'ubuntu-mysql-57']
            v.customize ['modifyvm', :id, '--cpus', '1']
            v.customize ['modifyvm', :id, '--memory', 2048]
            v.customize ['modifyvm', :id, '--ioapic', 'off']
            v.customize ['modifyvm', :id, '--natdnshostresolver1', 'on']
        end

        # Update package list
        mysql57.vm.provision :shell, :path => "bootstrap.sh", :args => "5.7"
    end

    # VM config 5.6
    config.vm.define :mysql56, autostart: false do |mysql56|
        mysql56.vm.network :private_network, ip: "192.168.1.56"
        mysql56.vm.network :forwarded_port, host: 3306, guest: 3306
        mysql56.vm.network :forwarded_port, host: 3307, guest: 3307

        mysql56.vm.hostname = "mysql-56"

        mysql56.vm.provider 'virtualbox' do |v|
            v.customize ['modifyvm', :id, '--name', 'ubuntu-mysql-56']
            v.customize ['modifyvm', :id, '--cpus', '1']
            v.customize ['modifyvm', :id, '--memory', 2048]
            v.customize ['modifyvm', :id, '--ioapic', 'off']
            v.customize ['modifyvm', :id, '--natdnshostresolver1', 'on']
        end

        # Update package list
        mysql56.vm.provision :shell, :path => "bootstrap.sh", :args => "5.6"
    end

    # VM config
    config.vm.define :mysql55, autostart: false do |mysql55|
        mysql55.vm.network :private_network, ip: "192.168.1.55"
        mysql55.vm.network :forwarded_port, host: 3306, guest: 3306
        mysql55.vm.network :forwarded_port, host: 3307, guest: 3307

        mysql55.vm.hostname = "mysql-55"

        mysql55.vm.provider 'virtualbox' do |v|
            v.customize ['modifyvm', :id, '--name', 'ubuntu-mysql-55']
            v.customize ['modifyvm', :id, '--cpus', '1']
            v.customize ['modifyvm', :id, '--memory', 2048]
            v.customize ['modifyvm', :id, '--ioapic', 'off']
            v.customize ['modifyvm', :id, '--natdnshostresolver1', 'on']
        end

        # Update package list
        mysql55.vm.provision :shell, :path => "bootstrap.sh", :args => "5.5"
    end
end
