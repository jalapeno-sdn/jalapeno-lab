#!/bin/bash

ovs-vsctl add-br vlt_br
ovs-vsctl add-br vlt_mgt_br
ovs-vsctl add-br vlt_outside_br
ovs-vsctl add-br vlt_scapy
ovs-vsctl add-br vlt_edge
ovs-vsctl add-br vlt_cloud
ovs-vsctl add-br vlt_k8s

ifconfig vlt_br up
ifconfig vlt_mgt_br up
ifconfig vlt_outside_br up
ifconfig vlt_scapy up
ifconfig vlt_edge up
ifconfig vlt_cloud up
ifconfig vlt_k8s up

ip addr add 10.251.251.1/24 dev vlt_mgt_br
ip addr add 10.0.250.2/24 dev vlt_k8s
ip addr add 10.0.251.1/24 dev vlt_scapy
ip addr add 10.0.252.1/24 dev vlt_edge
ip addr add 10.0.253.1/24 dev vlt_cloud
ip addr add 10.0.254.1/24 dev vlt_outside_br

ip -6 addr add 10:0:254::1/120 dev vlt_outside_br
ip -6 addr add 10:0:251::1/120 dev vlt_scapy
ip -6 addr add 10:0:252::1/120 dev vlt_edge
ip -6 addr add 10:0:253::1/120 dev vlt_cloud

#ip route add 10.0.250.0/24 via 10.0.254.71 dev vlt_outside_br
ip route add 10.0.130.0/24 via 10.0.250.1 dev vlt_k8s
ip route add 10.0.0.0/24 via 10.0.250.1 dev vlt_k8s

#ip -6 route add 10:0:250::/120 via 10:0:254::71 dev vlt_outside_br
ip -6 route add 10:0:130::/120 via 10:0:254::72 dev vlt_outside_br

#iptables -t nat -A PREROUTING -p tcp -m tcp --dport 30852 -j DNAT --to-destination 10.251.251.250:30852
#iptables -t nat -A PREROUTING -p tcp -m tcp --dport 30308 -j DNAT --to-destination 10.251.251.250:30308
#iptables -t nat -A PREROUTING -p tcp -m tcp --dport 30300 -j DNAT --to-destination 10.251.251.250:30300
#iptables -t nat -A PREROUTING -p tcp -m tcp --dport 8443 -j DNAT --to-destination 10.251.251.250:8443
#iptables -t nat -A PREROUTING -p tcp -m tcp --dport 25022 -j DNAT --to-destination 10.251.251.250:22
iptables -t nat -A POSTROUTING -s 10.251.251.0/24 -o enp1s0f0 -j MASQUERADE
iptables -t nat -A POSTROUTING -s 10.0.254.0/24 -o enp1s0f0 -j MASQUERADE
iptables -t nat -A POSTROUTING -s 10.0.250.0/24 -o enp1s0f0 -j MASQUERADE
