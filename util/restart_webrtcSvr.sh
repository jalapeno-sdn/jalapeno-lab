#/bin/bash

lxc-stop -n vltwebrtcsvr00
ovs-vsctl del-port vlt_br vltwebrtc00
lxc-start -n vltwebrtcsvr00
ovs-vsctl del-port vlt_br vltwebrtc00
ovs-vsctl add-port vlt_br vltwebrtc00 tag=100
echo lxc-ls --active
lxc-ls --active
