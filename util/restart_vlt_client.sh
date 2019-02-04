#/bin/bash

lxc-stop -n vltclient00
ovs-vsctl del-port vlt_br vltclient00-eth0
lxc-start -n vlt_client
brctl delif lxcbr0 client-eth0
ovs-vsctl add-port vlt_br vltclient00-eth0 tag=102
echo lxc-ls --active
lxc-ls --active
