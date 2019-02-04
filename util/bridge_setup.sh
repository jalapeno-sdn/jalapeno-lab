#!/bin/bash

# this script creates Voltron's OVS bridge instances

ovs-vsctl add-br vlt_br
ovs-vsctl add-br vlt_mgt_br
ovs-vsctl add-br vlt_outside_br

ifconfig vlt_br up
ifconfig vlt_mgt_br up
ifconfig vlt_outside_br up

ip addr add 10.251.251.1/24 dev vlt_mgt_br
ip addr add 10.0.254.1/24 dev vlt_outside_br

ip route add 10.0.250.0/24 via 10.0.254.71 dev vlt_outside_br
ip route add 10.0.129.0/24 via 10.0.254.72 dev vlt_outside_br
ip route add 10.0.130.0/24 via 10.0.254.71 dev vlt_outside_br
ip route add 10.0.201.0/24 via 10.0.254.76 dev vlt_outside_br
