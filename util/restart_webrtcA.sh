#/bin/bash

lxc-stop -n webrtcA
ovs-vsctl del-port vlt_br webrtcA-eth0
lxc-start -n webrtcA
brctl delif lxcbr0 webrtcA-eth0
ovs-vsctl add-port vlt_br webrtcA-eth0 tag=300
echo lxc-ls --active
lxc-ls --active
