#/bin/bash

ovs-vsctl del-port vlt_mgt_br rtr00mgt1
ovs-vsctl del-port vlt_mgt_br rtr01mgt1
ovs-vsctl del-port vlt_mgt_br rtr02mgt1
ovs-vsctl del-port vlt_mgt_br rtr03mgt1
ovs-vsctl del-port vlt_mgt_br rtr04mgt1
ovs-vsctl del-port vlt_br rtr00xr1
ovs-vsctl del-port vlt_br rtr00xr2
ovs-vsctl del-port vlt_br rtr00xr3
ovs-vsctl del-port vlt_br rtr00xr4
ovs-vsctl del-port vlt_br rtr00xr5
ovs-vsctl del-port vlt_br rtr00xr6
ovs-vsctl del-port vlt_br rtr00xr7
ovs-vsctl del-port vlt_br rtr01xr0
ovs-vsctl del-port vlt_br rtr01xr1
ovs-vsctl del-port vlt_br rtr01xr2
ovs-vsctl del-port vlt_br rtr01xr3
ovs-vsctl del-port vlt_br rtr01xr4
ovs-vsctl del-port vlt_br rtr01xr5
ovs-vsctl del-port vlt_br rtr01xr6
ovs-vsctl del-port vlt_br rtr01xr7
ovs-vsctl del-port vlt_br rtr02xr0
ovs-vsctl del-port vlt_br rtr02xr1
ovs-vsctl del-port vlt_br rtr02xr2
ovs-vsctl del-port vlt_br rtr02xr3
ovs-vsctl del-port vlt_br rtr02xr4
ovs-vsctl del-port vlt_br rtr02xr5
ovs-vsctl del-port vlt_br rtr02xr6
ovs-vsctl del-port vlt_br rtr02xr7
ovs-vsctl del-port vlt_br rtr03xr0
ovs-vsctl del-port vlt_br rtr03xr1
ovs-vsctl del-port vlt_br rtr03xr2
ovs-vsctl del-port vlt_br rtr03xr3
ovs-vsctl del-port vlt_br rtr03xr4
ovs-vsctl del-port vlt_br rtr03xr5
ovs-vsctl del-port vlt_br rtr03xr6
ovs-vsctl del-port vlt_br rtr03xr7
ovs-vsctl del-port vlt_br rtr03xr0
ovs-vsctl del-port vlt_br rtr03xr1
ovs-vsctl del-port vlt_br rtr03xr2
ovs-vsctl del-port vlt_br rtr03xr3
ovs-vsctl del-port vlt_br rtr03xr4
ovs-vsctl del-port vlt_br rtr03xr5
ovs-vsctl del-port vlt_br rtr03xr6
ovs-vsctl del-port vlt_br rtr03xr7
ovs-vsctl del-br vlt_br
ovs-vsctl del-br vlt_mgt_br
ovs-vsctl del-br vlt_k8s_br
ovs-vsctl del-br vlt_outside_br
ovs-vsctl show
