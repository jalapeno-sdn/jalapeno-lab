#/bin/bash

echo stopping routers
/opt/voltron/stop_router.py r4
/opt/voltron/stop_router.py r3
/opt/voltron/stop_router.py r2
/opt/voltron/stop_router.py r1
/opt/voltron/stop_router.py r0
sleep 1

echo stopping vms
virsh destroy vlt_client1
virsh destroy vlt_openshift_vm
virsh undefine vlt_client1
virsh undefine vlt_openshift_vm

echo deleting routes
ip route del 10.0.250.0/23 via 10.0.254.2 dev vlt_outside_br
ip route del 10.0.252.0/23 via 10.0.254.2 dev vlt_outside_br
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




