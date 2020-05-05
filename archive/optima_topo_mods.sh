#!/bin/bash

ifconfig rtr01xr7 up
ifconfig rtr11xr7 up
ifconfig rtr11xr8 up
ifconfig rtr03xr8 up
ifconfig rtr03xr5 up
ifconfig rtr07xr3 up

ovs-vsctl add-port vlt_br rtr01xr7 tag=400
ovs-vsctl del-port vlt_br rtr11xr7
ovs-vsctl add-port vlt_br rtr11xr7 tag=400

ovs-vsctl del-port vlt_br rtr11xr8
ovs-vsctl add-port vlt_br rtr11xr8 tag=401
ovs-vsctl add-port vlt_br rtr03xr8 tag=401

ovs-vsctl del-port vlt_br rtr11xr8
ovs-vsctl add-port vlt_br rtr11xr8 tag=401
ovs-vsctl add-port vlt_br rtr03xr8 tag=401

ovs-vsctl add-port vlt_br rtr03xr5 tag=402
ovs-vsctl add-port vlt_br rtr07xr3 tag=402
