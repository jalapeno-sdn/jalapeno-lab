#/bin/bash

lxc-stop -n vlt_client
ovs-vsctl del-port vlt_br client-eth0
lxc-start -n vlt_client
brctl delif lxcbr0 client-eth0
ovs-vsctl add-port vlt_br client-eth0 tag=102
echo lxc-ls --active
lxc-ls --active
