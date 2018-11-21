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

# r0 - simulated ToR
#gi0/0/0/0 - vlt_br/tag100 to centos/voltron ens4
#gi0/0/0/1 - vlt_br/tag101 to voltron_api_gw_vlan
#gi0/0/0/2 - vlt_br/tag102 to voltron_client1 & 2_vlan
#gi0/0/0/3 - vlt_br/tag103 to r1 gi0/0/0/0
#gi0/0/0/4 - vtl_br/tag104 to r2 gi0/0/0/0
#gi0/0/0/5 - vlt_br/tag105 to r11 gi0/0/0/5
#gi0/0/0/6 - vtl_br/tag106 to r12 gi0/0/0/4
if (sys.argv[1]) in ['r0']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r0.img', '00', 'r0'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr00mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr00xr0', 'tag=100'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr00xr1', 'tag=101'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr00xr2', 'tag=102'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr00xr3', 'tag=103'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr00xr4', 'tag=104'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr00xr5', 'tag=105'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr00xr6', 'tag=106'])

# r1 CDN Peering Router
#gi0/0/0/0 - vlt_br/tag103 to r0 gi0/0/0/3
#gi0/0/0/1 - vlt_br/tag107 to r71 g1
#gi0/0/0/2 - vlt_br/tag108 to r72 g2
#gi0/0/0/3 - vlt_br/tag125 to r12 gi0/0/0/2
#gi0/0/0/4 - vlt_br/tag119 to r11 gi0/0/0/2
#gi0/0/0/5 - vlt_br/tag112 to r5 RR gi0/0/0/0

if (sys.argv[1]) in ['r1']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r1.img', '01', 'r1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr01mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr01xr0', 'tag=103'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr01xr1', 'tag=107'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr01xr2', 'tag=108'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr01xr3', 'tag=125'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr01xr4', 'tag=119'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr01xr5', 'tag=112'])

# r2 CDN Peering Router
#gi0/0/0/0 - vlt_br/tag104 to r0 gi0/0/0/4
#gi0/0/0/1 - vlt_br/tag109 to r71 g2
#gi0/0/0/2 - vlt_br/tag110 to r72 g1
#gi0/0/0/3 - vlt_br/tag126 to r12 gi0/0/0/3
#gi0/0/0/4 - vlt_br/tag120 to r11 gi0/0/0/3
#gi0/0/0/5 - vlt_br/tag113 to r5 RR gi0/0/0/1

if (sys.argv[1]) in ['r2']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r2.img', '02', 'r2'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr02mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr02xr0', 'tag=104'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr02xr1', 'tag=109'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr02xr2', 'tag=110'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr02xr3', 'tag=126'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr02xr4', 'tag=120'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr02xr5', 'tag=113'])

# r5 Route Reflector
#gi0/0/0/0 - vlt_br/tag112 to r1 gi0/0/0/5
#gi0/0/0/1 - vlt_br/tag113 to r2 gi0/0/0/5

if (sys.argv[1]) in ['r5']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r5.img', '05', 'r5'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr05mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr05xr0', 'tag=112'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr05xr1', 'tag=113'])

# External Peers - to save disk and memory, CSR1kv virtual routers are used for external peers in the topology
# CSR1k OVS plumbing is managed in the virsh xml files found in voltron/config/

# r71 CDN External Peer
#g1 - vlt_br/tag107 to r1 gi0/0/0/1 
#g2 - vlt_br/tag109 to r2 gi0/0/0/1
#g3 - not used
#g4 - vlt_outside_br br to internet_user_vlan

if (sys.argv[1]) in ['r71']:
    subprocess.call(['virsh', 'start', 'r71'])

# r72 CDN External Peer
#g1 - vlt_br/tag110 to r2 gi0/0/0/2 
#g2 - vlt_br/tag108 to r1 gi0/0/0/2
#g3 - not used
#g4 - vlt_outside_br br to internet_user_vlan

if (sys.argv[1]) in ['r72']:
    subprocess.call(['virsh', 'start', 'r72'])


########
# If using the larger CDN + WAN topology, additional router start scripts are found  beyond this point 

# r10 - ToR
#gi0/0/0/0 -  vlt_br2/tag100 to Centos/Voltron - shutdown this interface when using combined topology
#gi0/0/0/1 -  vlt_br2/tag101 to API-GW vlan 101 - shutdown this interface when using combined topology
#gi0/0/0/2 -  vlt_br2/tag102 to client 1 & 2 vlan 102 - shutdown this interface when using combined topology
#gi0/0/0/3 -  vlt_br2/tag116 to client 3 & 4 vlan 116
#gi0/0/0/4 -  vlt_br2/tag117 to r13 gi0/0/0/0
#gi0/0/0/5 -  vlt_br2/tag118 to r14 gi0/0/0/0
if (sys.argv[1]) in ['r10']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r10.img', '10', 'r10'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr10mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr10xr0', 'tag=100'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr10xr1', 'tag=101'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr10xr2', 'tag=102'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr10xr3', 'tag=116'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr10xr4', 'tag=117'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr10xr5', 'tag=118'])

# r13 - DC Edge LER
#gi0/0/0/0 -  vlt_br2/tag117 to r10 gi0/0/0/4
#gi0/0/0/1 -  vlt_br2/tag130 to r11 gi0/0/0/0
#gi0/0/0/2 -  vlt_br2/tag131 to r12 gi0/0/0/7
if (sys.argv[1]) in ['r13']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r13.img', '13', 'r13'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr13mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr13xr0', 'tag=117'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr13xr1', 'tag=130'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr13xr2', 'tag=131'])

# r14 - DC Edge LER
#gi0/0/0/0 -  vlt_br2/tag118 to r10 gi0/0/0/5
#gi0/0/0/1 -  vlt_br2/tag132 to r12 gi0/0/0/0
if (sys.argv[1]) in ['r14']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r14.img', '14', 'r14'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr14mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr14xr0', 'tag=118'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr14xr1', 'tag=132'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr14xr2', 'tag=124'])

# r11 - WAN LSR
#gi0/0/0/0 -  vlt_br2/tag130 to r13 gi0/0/0/1
#gi0/0/0/1 -  vlt_br2/tag105 to r0 gi0/0/0/0
#gi0/0/0/2 -  vlt_br2/tag119 to r1 gi0/0/0/4
#gi0/0/0/3 -  vlt_br2/tag120 to r2 gi0/0/0/4
#gi0/0/0/4 -  vlt_br2/tag121 to r21 gi0/0/0/0
#gi0/0/0/5 -  vlt_br2/tag122 to r21 gi0/0/0/4
#gi0/0/0/6 -  vlt_br2/tag123 to r22 gi0/0/0/1
#gi0/0/0/7 -  vlt_br2/tag124 to r23 gi0/0/0/1

if (sys.argv[1]) in ['r11']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r11.img', '11', 'r11'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr11mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr11xr0', 'tag=130'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr11xr1', 'tag=105'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr11xr2', 'tag=119'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr11xr3', 'tag=120'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr11xr4', 'tag=121'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr11xr5', 'tag=122'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr11xr6', 'tag=123'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr11xr7', 'tag=124'])

# r12 - WAN LSR
#gi0/0/0/0 -  vlt_br/tag132 to r14 gi0/0/0/1
#gi0/0/0/1 -  vlt_br/tag106 to r0  gi0/0/0/1
#gi0/0/0/2 -  vlt_br/tag125 to r1  gi0/0/0/3
#gi0/0/0/3 -  vlt_br/tag126 to r2  gi0/0/0/3
#gi0/0/0/4 -  vlt_br/tag127 to r21 gi0/0/0/1
#gi0/0/0/5 -  vlt_br/tag128 to r22 gi0/0/0/0
#gi0/0/0/6 -  vlt_br/tag129 to r23 gi0/0/0/0
#gi0/0/0/6 -  vlt_br/tag131 to r13 gi0/0/0/2
if (sys.argv[1]) in ['r12']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r12.img', '12', 'r12'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr12mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr12xr0', 'tag=132'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr12xr1', 'tag=106'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr12xr2', 'tag=125'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr12xr3', 'tag=126'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr12xr4', 'tag=127'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr12xr5', 'tag=128'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr12xr6', 'tag=129'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr12xr7', 'tag=131'])

# r21 - WAN Peering Router
#gi0/0/0/0 -  vlt_br2/tag121 to r11 gi0/0/0/4
#gi0/0/0/1 -  vlt_br2/tag127 to r12 gi0/0/0/4
#gi0/0/0/2 -  vlt_br2/tag150 to r78 g1
#gi0/0/0/3 -  vlt_br2/tag151 to r77 g2
#gi0/0/0/4 -  vlt_br2/tag122 to r11 gi0/0/0/5
if (sys.argv[1]) in ['r21']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r21.img', '21', 'r21'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr21mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr21xr0', 'tag=121'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr21xr1', 'tag=127'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr21xr2', 'tag=150'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr21xr3', 'tag=151'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr21xr4', 'tag=122'])

# r22 - WAN Peering Router
#gi0/0/0/0 -  vlt_br2/tag128 to r12 gi0/0/0/5
#gi0/0/0/1 -  vlt_br2/tag123 to r11 gi0/0/0/6
#gi0/0/0/2 -  vlt_br2/tag152 to r78 g2
#gi0/0/0/3 -  vlt_br2/tag153 to r77 g1
#gi0/0/0/4 -  vlt_br2/tag154 to r76 g2
#gi0/0/0/5 -  vlt_br2/tag130 to client 5 eth1
if (sys.argv[1]) in ['r22']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r22.img', '22', 'r22'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr22mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr22xr0', 'tag=128'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr22xr1', 'tag=123'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr22xr2', 'tag=152'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr22xr3', 'tag=153'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr22xr4', 'tag=154'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr22xr5', 'tag=130'])

# r23 - WAN Peering Router
#gi0/0/0/0 -  vlt_br2/tag129 to r12 gi0/0/0/6
#gi0/0/0/1 -  vlt_br2/tag124 to r11 gi0/0/0/7
#gi0/0/0/2 -  vlt_br2/tag155 to r77 g3
#gi0/0/0/3 -  vlt_br2/tag156 to r76 g1
#gi0/0/0/5 -  vlt_br2/tag131 to client6 eth1
if (sys.argv[1]) in ['r23']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r23.img', '23', 'r23'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr23mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr23xr0', 'tag=129'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr23xr2', 'tag=155'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr23xr3', 'tag=156'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr23xr4', 'tag=131'])

# r78 - CSR1kv External Peer (Transit Provider)
#g1 -  vlt_br2/tag150 to r21 gi0/0/0/2 
#g2 -  vlt_br2/tag152 to r22 gi0/0/0/2
#g3 -  not used
#g4 -  vlt_outside_br
if (sys.argv[1]) in ['r78']:
    subprocess.call(['virsh', 'start', 'r78'])

# r78 - CSR1kv External Peer (Transit Provider)
#g1 -  vlt_br/tag153 to r21 gi0/0/0/2 
#g2 -  vlt_br/tag151 to r22 gi0/0/0/2
#g3 -  vlt_br/tag155 to r23 gi0/0/0/2
#g4 -  vlt_br/tag158 to r76 g3
#g5 -  vlt_outside_br
if (sys.argv[1]) in ['r77']:
    subprocess.call(['virsh', 'start', 'r77'])

# r77 - CSR1kv External Peer (Transit Provider)
#g1 -  vlt_br/tag156 to r23 gi0/0/0/3 
#g2 -  vlt_br/tag154 to r22 gi0/0/0/4
#g3 -  vlt_br/tag158 to r77 g4
#g4 -  vlt_outside_br
if (sys.argv[1]) in ['r76']:
    subprocess.call(['virsh', 'start', 'r76'])

print "router started"
