#!/usr/bin/env python

# This script starts routers in the Voltron demo topology - see .png file.  Interface/vswitch values are hardcoded 
# into this script based on the topology file, however, if the user wishes to modify the topology they may do so by
# changing the ovs-vsctl command values below

from os import getpid
from sys import argv, exit
import sys
import time
import subprocess

# example:  sudo ./start_router.py r0

#################################################################################
# Base Topology: Chicago


# r0 - Chicago ToR
#gi0/0/0/0 - vlt_br/tag100 to centos/voltron ens4
#gi0/0/0/1 - vlt_br/tag101 to voltron_api_gw_vlan
#gi0/0/0/2 - vlt_br/tag102 to voltron_client1 & 2_vlan
#gi0/0/0/3 - vlt_br/tag103 to r1 gi0/0/0/0
#gi0/0/0/4 - vtl_br/tag104 to r2 gi0/0/0/0
#gi0/0/0/5 - vlt_br/tag105 to r11 gi0/0/0/5
#gi0/0/0/6 - vtl_br/tag106 to r12 gi0/0/0/4
#gi0/0/0/7 - vtl_br/tag111 to r06 gi0/0/0/0
if (sys.argv[1]) in ['r00']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r00.img', '00', 'r00'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr00mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr00xr0', 'tag=100'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr00xr1', 'tag=101'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr00xr2', 'tag=102'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr00xr3', 'tag=103'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr00xr4', 'tag=104'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr00xr5', 'tag=105'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr00xr6', 'tag=106'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr00xr7', 'tag=111'])

# r1 Chicago POP Peering Router
#gi0/0/0/0 - vlt_br/tag103 to r0 gi0/0/0/3
#gi0/0/0/1 - vlt_br/tag107 to r71 g1
#gi0/0/0/2 - vlt_br/tag108 to r72 g2
#gi0/0/0/3 - vlt_br/tag125 to r12 gi0/0/0/2
#gi0/0/0/4 - vlt_br/tag119 to r11 gi0/0/0/2
#gi0/0/0/5 - vlt_br/tag112 to r5 RR gi0/0/0/0
#gi0/0/0/6 - vlt_br/tag114 to r6 LSR gi0/0/0/1

if (sys.argv[1]) in ['r01']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r01.img', '01', 'r01'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr01mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr01xr0', 'tag=103'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr01xr1', 'tag=107'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr01xr2', 'tag=108'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr01xr3', 'tag=125'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr01xr4', 'tag=119'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr01xr5', 'tag=112'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr01xr6', 'tag=114'])

# r2 Chicago POP Peering Router
#gi0/0/0/0 - vlt_br/tag104 to r0 gi0/0/0/4
#gi0/0/0/1 - vlt_br/tag109 to r71 g2
#gi0/0/0/2 - vlt_br/tag110 to r72 g1
#gi0/0/0/3 - vlt_br/tag126 to r12 gi0/0/0/3
#gi0/0/0/4 - vlt_br/tag120 to r11 gi0/0/0/3
#gi0/0/0/5 - vlt_br/tag113 to r5 RR gi0/0/0/1
#gi0/0/0/6 - vlt_br/tag115 to r6 LSR gi0/0/0/2
#gi0/0/0/7 - vlt_br/tag116 to game_svr00

if (sys.argv[1]) in ['r02']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r02.img', '02', 'r02'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr02mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr02xr0', 'tag=104'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr02xr1', 'tag=109'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr02xr2', 'tag=110'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr02xr3', 'tag=126'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr02xr4', 'tag=120'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr02xr5', 'tag=113'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr02xr6', 'tag=115'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr02xr7', 'tag=116'])

# r05 Chicago Route Reflector
#gi0/0/0/0 - vlt_br/tag112 to r1 gi0/0/0/5
#gi0/0/0/1 - vlt_br/tag113 to r2 gi0/0/0/5

if (sys.argv[1]) in ['r05']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r05.img', '05', 'r05'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr05mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr05xr0', 'tag=112'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr05xr1', 'tag=113'])

# r06 Chicago LSR
#gi0/0/0/0 - vlt_br/tag111 to r0 gi0/0/0/7
#gi0/0/0/1 - vlt_br/tag114 to r1 gi0/0/0/6
#gi0/0/0/2 - vlt_br/tag115 to r2 gi0/0/0/6
#gi0/0/0/1 - vlt_br/tag117 to r11 gi0/0/0/8
#gi0/0/0/2 - vlt_br/tag118 to r12 gi0/0/0/8

if (sys.argv[1]) in ['r06']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r06.img', '06', 'r06'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr06mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr06xr0', 'tag=111'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr06xr1', 'tag=114'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr06xr2', 'tag=115'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr06xr3', 'tag=117'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr06xr4', 'tag=118'])

# External Peers - to save disk and memory, CSR1kv virtual routers are used for external peers in the topology
# CSR1k OVS plumbing is managed in the virsh xml files found in voltron/config/

# r71 Chicago External Peer
#g1 - vlt_br/tag107 to r1 gi0/0/0/1 
#g2 - vlt_br/tag109 to r2 gi0/0/0/1
#g3 - not used
#g4 - vlt_outside_br br to internet_user_vlan

if (sys.argv[1]) in ['r71']:
    subprocess.call(['virsh', 'start', 'r71'])

# r72 Chicago External Peer
#g1 - vlt_br/tag110 to r2 gi0/0/0/2 
#g2 - vlt_br/tag108 to r1 gi0/0/0/2
#g3 - not used
#g4 - vlt_outside_br br to internet_user_vlan

if (sys.argv[1]) in ['r72']:
    subprocess.call(['virsh', 'start', 'r72'])


#########################################################################################################
##########
# If using the larger data center + backbone topology, additional router start scripts are found  beyond this point 
#########################################################################################################
##########

## Herndon Data Center ##

# r32 - Herndon DC Leaf
#gi0/0/0/0 -  vlt_br/tag200 to Istio LXC00
#gi0/0/0/1 -  vlt_br/tag201 to IAD_Spine_33 gi0/0/0/0 
#gi0/0/0/2 -  vlt_br/tag202 to IAD_Spine_34 gi0/0/0/0
if (sys.argv[1]) in ['r32']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r32.img', '32', 'r32'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr32mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr32xr0', 'tag=200'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr32xr1', 'tag=201'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr32xr2', 'tag=202'])

# r33 - Herndon DC Spine
#gi0/0/0/0 -  vlt_br/tag201 to IAD_Leaf_32 gi0/0/0/1
#gi0/0/0/1 -  vlt_br/tag204 to IAD_Leaf_35 gi0/0/0/2 
#gi0/0/0/2 -  vlt_br/tag121 to IAD_LER_R11 gi0/0/0/0
#gi0/0/0/3 -  vlt_br/tag123 to IAD_LER_R12 gi0/0/0/7
if (sys.argv[1]) in ['r33']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r33.img', '33', 'r33'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr33mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr33xr0', 'tag=201'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr33xr1', 'tag=204'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr33xr2', 'tag=121'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr33xr3', 'tag=123'])

# r34 - Herndon DC Spine
#gi0/0/0/0 -  vlt_br/tag202 to IAD_Leaf_32 gi0/0/0/2
#gi0/0/0/1 -  vlt_br/tag203 to IAD_Leaf_35 gi0/0/0/1 
#gi0/0/0/2 -  vlt_br/tag124 to IAD_LER_R12 gi0/0/0/0
#gi0/0/0/3 -  vlt_br/tag122 to IAD_LER_R11 gi0/0/0/7
if (sys.argv[1]) in ['r34']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r34.img', '34', 'r34'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr34mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr34xr0', 'tag=202'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr34xr1', 'tag=203'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr34xr2', 'tag=124'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr34xr3', 'tag=122'])

# r35 - Herndon DC Leaf
#gi0/0/0/0 -  vlt_br/tag205 to Istio LXC01
#gi0/0/0/1 -  vlt_br/tag203 to IAD_Spine_33 gi0/0/0/1 
#gi0/0/0/2 -  vlt_br/tag204 to IAD_Spine_34 gi0/0/0/1
if (sys.argv[1]) in ['r35']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r35.img', '35', 'r35'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr35mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr35xr0', 'tag=205'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr35xr1', 'tag=203'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr35xr2', 'tag=204'])

################################################################################

## Herndon POP ##

# r11 - Herndon LER
#gi0/0/0/0 -  vlt_br/tag122 to IAD_SP34
#gi0/0/0/1 -  vlt_br/tag121 to IAD_SP33
#gi0/0/0/2 -  vlt_br/tag105 to ORD_TOR00
#gi0/0/0/3 -  vlt_br/tag119 to ORD_BR01
#gi0/0/0/4 -  vlt_br/tag120 to ORD_BR02
#gi0/0/0/5 -  vlt_br/tag127 to IAD_BR03
#gi0/0/0/6 -  vlt_br/tag128 to IAD_BR04
#gi0/0/0/7 -  vlt_br/tag133 to ATL_BR22
#gi0/0/0/8 -  vlt_br/tag117 to ORD_LSR06

if (sys.argv[1]) in ['r11']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r11.img', '11', 'r11'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr11mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr11xr0', 'tag=122'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr11xr1', 'tag=121'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr11xr2', 'tag=105'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr11xr3', 'tag=119'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr11xr4', 'tag=120'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr11xr5', 'tag=127'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr11xr6', 'tag=128'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr11xr7', 'tag=133'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr11xr8', 'tag=117'])

# r12 - Herndon LER
#gi0/0/0/0 -  vlt_br/tag124 to IAD_SP34
#gi0/0/0/1 -  vlt_br/tag123 to IAD_SP33
#gi0/0/0/2 -  vlt_br/tag106 to ORD_TOR00
#gi0/0/0/3 -  vlt_br/tag125 to ORD_BR01
#gi0/0/0/4 -  vlt_br/tag126 to ORD_BR02
#gi0/0/0/5 -  vlt_br/tag139 to IAD_BR03
#gi0/0/0/6 -  vlt_br/tag130 to IAD_BR04
#gi0/0/0/7 -  vlt_br/tag131 to DFW_LSR13
#gi0/0/0/8 -  vlt_br/tag118 to ORD_LSR06

if (sys.argv[1]) in ['r12']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r12.img', '12', 'r12'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr12mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr12xr0', 'tag=124'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr12xr1', 'tag=123'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr12xr2', 'tag=106'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr12xr3', 'tag=125'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr12xr4', 'tag=126'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr12xr5', 'tag=139'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr12xr6', 'tag=130'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr12xr7', 'tag=131'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr12xr8', 'tag=118'])

# r3 - Herndon Border Router
#gi0/0/0/0 -  vlt_br/tag127 to IAD_LER11 
#gi0/0/0/1 -  vlt_br/tag134 to Ext72
#gi0/0/0/2 -  vlt_br/tag135 to Ext78
#gi0/0/0/3 -  vlt_br/tag139 to IAD_LER12

if (sys.argv[1]) in ['r03']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r03.img', '03', 'r03'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr03mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr03xr0', 'tag=127'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr03xr1', 'tag=134'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr03xr2', 'tag=135'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr03xr3', 'tag=139'])


# r4 - Herndon Border Router
#gi0/0/0/0 -  vlt_br/tag128 to IAD_LER11 
#gi0/0/0/1 -  vlt_br/tag136 to Ext78
#gi0/0/0/2 -  vlt_br/tag138 to Ext77
#gi0/0/0/3 -  vlt_br/tag130 to IAD_LER12

if (sys.argv[1]) in ['r04']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r04.img', '04', 'r04'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr04mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr04xr0', 'tag=128'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr04xr1', 'tag=136'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr04xr2', 'tag=138'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr04xr3', 'tag=130'])

# r13 - Dallas CSR1kv LSR
#g1 -  vlt_br/tag131 to r12 g7
#g2 -  vlt_br/tag129 to r22 g0
#g4 -  vlt_outside_br
if (sys.argv[1]) in ['r13']:
    subprocess.call(['virsh', 'start', 'r13'])


################################################################################
## Atlanta POP ##

# r22 - Atlanta Peering Router
#gi0/0/0/0 -  vlt_br/tag129 to r13 gi2
#gi0/0/0/1 -  vlt_br/tag133 to r11 gi0/0/0/6
#gi0/0/0/2 -  vlt_br/tag137 to r78 g3
#gi0/0/0/3 -  vlt_br/tag153 to r77 g1
#gi0/0/0/4 -  vlt_br/tag154 to r76 g2
#gi0/0/0/5 -  vlt_br/tag141 to r78 g5
#gi0/0/0/6 -  vlt_br/tag304 to r41 g2
#gi0/0/0/7 -  vlt_br/tag306 to r42 g2

if (sys.argv[1]) in ['r22']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r22.img', '22', 'r22'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr22mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr22xr0', 'tag=132'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr22xr1', 'tag=133'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr22xr2', 'tag=137'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr22xr3', 'tag=153'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr22xr4', 'tag=154'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr22xr5', 'tag=141'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr22xr6', 'tag=304'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr22xr7', 'tag=306'])

# r23 - Atlanta Peering Router
#gi0/0/0/0 -  vlt_br/tag142 to r13 g3
#gi0/0/0/2 -  vlt_br/tag155 to r77 g3
#gi0/0/0/3 -  vlt_br/tag156 to r76 g1
#gi0/0/0/4 -  vlt_br/tag140 to client6 eth1
#gi0/0/0/5 -  vlt_br/tag305 to r41 g3
#gi0/0/0/6 -  vlt_br/tag307 to r42 g3
if (sys.argv[1]) in ['r23']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r23.img', '23', 'r23'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr23mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr23xr0', 'tag=131'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr23xr2', 'tag=155'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr23xr3', 'tag=156'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr23xr4', 'tag=140'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr23xr5', 'tag=305'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr23xr6', 'tag=307'])

################################################################################
## External Routers ##

# r78 - Herndon CSR1kv External Peer
#g1 -  vlt_br/tag135 to r3 g3
#g2 -  vlt_br/tag136 to r4 g2
#g3 -  vlt_br/tag137 to r22 gi0/0/0/2
#g4 -  vlt_outside_br
#g5 -  vlt_br/tag141 to r22 gi0/0/0/5
if (sys.argv[1]) in ['r78']:
    subprocess.call(['virsh', 'start', 'r78'])

# r77 - Atlanta CSR1kv External Peer (Transit Provider)
#g1 -  vlt_br/tag153 to r22 gi0/0/0/3 
#g2 -  vlt_br/tag138 to r4 gi0/0/0/3
#g3 -  vlt_br/tag155 to r23 gi0/0/0/2
#g4 -  vlt_br/tag158 to r76 g3
#g5 -  vlt_outside_br
if (sys.argv[1]) in ['r77']:
    subprocess.call(['virsh', 'start', 'r77'])

# r76 - Atlanta CSR1kv External Peer (Transit Provider)
#g1 -  vlt_br/tag156 to r23 gi0/0/0/3 
#g2 -  vlt_br/tag154 to r22 gi0/0/0/4
#g3 -  vlt_br/tag158 to r77 g4
#g4 -  vlt_outside_br
if (sys.argv[1]) in ['r76']:
    subprocess.call(['virsh', 'start', 'r76'])

##################################################################################
## ATL Metro Topology ##

# r40 - ATL CSR1k metro access device 

#g1 -  vlt_br/tag300 to client subnet 10.0.201.0/24
#g2 -  vlt_br/tag301 to atl_r41 gi1
#g3 -  vlt_br/tag302 to atl_r42 gi1
#g4 -  vlt_outside_br
if (sys.argv[1]) in ['r40']:
    subprocess.call(['virsh', 'start', 'r40'])

# r41 - ATL CSR1k metro agg device 

#g1 -  vlt_br/tag301 to atl_r40 gi2
#g2 -  vlt_br/tag304 to atl_br22 gi0/0/0/6
#g3 -  vlt_br/tag305 to atl_br23 gi0/0/0/5
#g4 -  vlt_outside_br
#g5 -  vlt_br/tag308 to atl_r43 gi2
#g6 -  vlt_br/tag310 to atl_r44 gi2
if (sys.argv[1]) in ['r41']:
    subprocess.call(['virsh', 'start', 'r41'])

# r42 - ATL CSR1k metro agg device 

#g1 -  vlt_br/tag301 to atl_r40 gi3
#g2 -  vlt_br/tag306 to atl_br22 gi0/0/0/7
#g3 -  vlt_br/tag307 to atl_br23 gi0/0/0/6
#g4 -  vlt_outside_br
#g5 -  vlt_br/tag309 to atl_r43 gi1
#g6 -  vlt_br/tag311 to atl_r44 gi1
if (sys.argv[1]) in ['r42']:
    subprocess.call(['virsh', 'start', 'r42'])
    
# r43 - ATL CSR1k metro border device 

#g1 -  vlt_br/tag309 to atl_r42 gi5
#g2 -  vlt_br/tag308 to atl_r41 gi5
#g3 -  vlt_br/tag312 to ext_peer r76 gi6
#g4 -  vlt_outside_br
if (sys.argv[1]) in ['r43']:
    subprocess.call(['virsh', 'start', 'r43'])
    
# r44 - ATL CSR1k metro border device 

#g1 -  vlt_br/tag311 to atl_r42 gi6
#g2 -  vlt_br/tag310 to atl_r41 gi6
#g3 -  vlt_br/tag313 to ext_peer r76 gi5
#g4 -  vlt_outside_br
if (sys.argv[1]) in ['r44']:
    subprocess.call(['virsh', 'start', 'r44'])
    

##################################################################################
## CLUS Telemetry Demo topology ##

# r20 - CSR1k metro access device 

#g1 -  br320 to client subnet 10.0.20.0/24
#g2 -  br321 to XR r21
#g4 -  virbr0
if (sys.argv[1]) in ['r20']:
    subprocess.call(['virsh', 'start', 'r20'])

# r21 - XRv9k device 

#g1 -  br321 to CSR1k r20
#g2 -  br322 to collection stack
#g3 -  br323 to vNX device

if (sys.argv[1]) in ['r21']:
    subprocess.call(['virsh', 'start', 'r21'])    
    
# r22 - vNX device 

#g1 -  br323 to XR r21
#g2 -  br324 to client subnet 10.0.21.0/24
#g3 -  virbr0

if (sys.argv[1]) in ['r22']:
    subprocess.call(['virsh', 'start', 'r22'])  
    
# client 20
if (sys.argv[1]) in ['lxc20']:
    subprocess.call(['lxc-start', '-n', 'lxc20'])  
    
# client 21
if (sys.argv[1]) in ['lxc21']:
    subprocess.call(['lxc-start', '-n', 'lxc21'])

# client 21
if (sys.argv[1]) in ['lxc22']:
    subprocess.call(['lxc-start', '-n', 'lxc22']) 

############################
print "node started"






