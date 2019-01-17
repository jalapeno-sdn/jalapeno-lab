#/bin/bash

echo stopping routers
/opt/vlt/stop_router.py r4
/opt/vlt/stop_router.py r3
/opt/vlt/stop_router.py r2
/opt/vlt/stop_router.py r1
/opt/vlt/stop_router.py r0
sleep 1

echo stopping vms
virsh destroy os_base1
virsh undefine os_base1
virsh destroy r71
virsh undefine r71
virsh destroy r72
virsh undefine r72
virsh destroy r76
virsh undefine r76
virsh destroy r77
virsh undefine r77
virsh destroy r78
virsh undefine r78

echo deleting routes
ip route del 10.0.250.0/23 via 10.0.254.71 dev vlt_outside_br
ip route del 10.0.252.0/23 via 10.0.254.72 dev vlt_outside_br
ip route del 10.0.130.0/23 via 10.0.254.71 dev vlt_outside_br
ip route del 10.0.131.0/23 via 10.0.254.72 dev vlt_outside_br
ip route

echo removing iptables entries
iptables -t nat -D PREROUTING -p tcp -m tcp --dport 8443 -j DNAT --to-destination 10.0.250.2:8443
iptables -t nat -D PREROUTING -p tcp -m tcp --dport 30300 -j DNAT --to-destination 10.0.250.2:30300
iptables -t nat -D PREROUTING -p tcp -m tcp --dport 30852 -j DNAT --to-destination 10.0.250.2:30852
iptables -t nat -D PREROUTING -p tcp -m tcp --dport 30902 -j DNAT --to-destination 10.0.250.2:30902
iptables -t nat -D PREROUTING -p tcp -m tcp --dport 10022 -j DNAT --to-destination 10.251.251.4:22
iptables -t nat -D PREROUTING -p tcp -m tcp --dport 10122 -j DNAT --to-destination 10.251.251.5:22
iptables --table nat --list

echo cleaning up ovs
ovs-vsctl del-port vlt_mgt_br rtr00mgt1
ovs-vsctl del-port vlt_mgt_br rtr01mgt1
ovs-vsctl del-port vlt_mgt_br rtr02mgt1
ovs-vsctl del-port vlt_mgt_br rtr03mgt1
ovs-vsctl del-port vlt_mgt_br rtr04mgt1
ovs-vsctl del-port vlt_k8s_br rtr00xr0
ovs-vsctl del-port vlt_br rtr00xr1
ovs-vsctl del-port vlt_br rtr00xr2
ovs-vsctl del-port vlt_br rtr00xr3
ovs-vsctl del-port vlt_br rtr00xr4
ovs-vsctl del-port vlt_br rtr00xr5
ovs-vsctl del-port vlt_br rtr01xr0
ovs-vsctl del-port vlt_br rtr01xr1
ovs-vsctl del-port vlt_br rtr01xr2
ovs-vsctl del-port vlt_br rtr02xr0
ovs-vsctl del-port vlt_br rtr02xr1
ovs-vsctl del-port vlt_br rtr02xr2
ovs-vsctl del-port vlt_br rtr03xr0
ovs-vsctl del-port vlt_br rtr03xr1
ovs-vsctl del-port vlt_k8s_br rtr03xr2
ovs-vsctl del-port vlt_br rtr04xr0
ovs-vsctl del-port vlt_br rtr04xr1
ovs-vsctl del-port vlt_k8s_br rtr04xr2
ovs-vsctl del-br vlt_br
ovs-vsctl del-br vlt_mgt_br
ovs-vsctl del-br vlt_k8s_br
ovs-vsctl del-br vlt_outside_br
ovs-vsctl show




