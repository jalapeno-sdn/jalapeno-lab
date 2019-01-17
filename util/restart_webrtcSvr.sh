#/bin/bash

lxc-stop -n webrtcSvr
ovs-vsctl del-port vlt_br webrtcSvr-eth0
lxc-start -n webrtcSvr
brctl delif lxcbr0 webrtcSvr-eth0
ovs-vsctl add-port vlt_br webrtcSvr-eth0 tag=100
echo lxc-ls --active
lxc-ls --active
