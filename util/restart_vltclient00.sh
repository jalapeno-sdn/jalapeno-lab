#/bin/bash

lxc-stop -n vltclient00
ovs-vsctl del-port vlt_br vltclient00
lxc-start -n vltclient00
ovs-vsctl del-port vlt_br vltclient00
ovs-vsctl add-port vlt_br vltclient00-eth0 tag=102
echo lxc-ls --active
lxc-ls --active
