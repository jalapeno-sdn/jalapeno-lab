#/bin/bash

lxc-stop -n webrtcB
ovs-vsctl del-port vlt_outside_br webrtcB-eth0
lxc-start -n webrtcB
brctl delif lxcbr0 webrtcB-eth0
ovs-vsctl add-port vlt_outside_br webrtcB-eth0 
echo lxc-ls --active
lxc-ls --active
