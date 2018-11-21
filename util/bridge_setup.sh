#!/bin/bash

# this script creates Voltron's OVS bridge instances

ovs-vsctl add-br vlt_br
ovs-vsctl add-br vlt_k8s_br
ovs-vsctl add-br vlt_mgt_br
ovs-vsctl add-br vlt_outside_br

ovs-vsctl show | grep vlt_br
ovs-vsctl show | grep vlt_os
ovs-vsctl show | grep vlt_mgt_br

ifconfig vlt_br up
ifconfig vlt_k8s_br up
ifconfig vlt_mgt_br up
ifconfig vlt_outside_br up

ip addr add 10.251.251.1/24 dev vlt_mgt_br
ip addr add 10.0.254.1/24 dev vlt_outside_br

ip route add 10.0.250.0/24 via 10.0.254.2 dev vlt_outside_br

