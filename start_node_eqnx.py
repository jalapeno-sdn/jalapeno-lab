#!/usr/bin/env python

# This script starts routers in the Voltron demo topology - see .png file.  Interface/vswitch values are hardcoded 
# into this script based on the topology file, however, if the user wishes to modify the topology they may do so by
# changing the ovs-vsctl command values below

from os import getpid
from sys import argv, exit
import sys
import time
import subprocess

# example:  sudo ./start_router_eqnx.py r00

#################################################################################

# r00
#gi0/0/0/0 - vlt_br/tag100 to centos/voltron ens4
#gi0/0/0/1 - vlt_br/tag101 to voltron_api_gw_vlan
#gi0/0/0/2 - vlt_br/tag102 to voltron_client1 & 2_vlan
#gi0/0/0/3 - vlt_br/tag103 to r1 gi0/0/0/0
#gi0/0/0/4 - vtl_br/tag104 to r2 gi0/0/0/0
#gi0/0/0/5 - vlt_br/tag105 to r11 gi0/0/0/5
#gi0/0/0/6 - vlt_br/tag106 to r12 gi0/0/0/4
#gi0/0/0/7 - vlt_br/tag111 to r06 gi0/0/0/0
#gi0/0/0/8 - available
#gi0/0/0/9 - vlt_outside_br for scapy
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
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_outside_br', 'rtr00xr9'])

# r01 
#gi0/0/0/0 - vlt_br/tag103 to r0 gi0/0/0/3
#gi0/0/0/1 - vlt_br/tag400 to r7 gi0/0
#gi0/0/0/5 - vlt_br/tag112 to r5 RR gi0/0/0/0
#gi0/0/0/9 - vlt_outside_br for scapy

if (sys.argv[1]) in ['r01']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r01.img', '01', 'r01'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr01mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr01xr0', 'tag=103'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr01xr1', 'tag=400'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr01xr5', 'tag=112'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_outside_br', 'rtr01xr9'])

# r05 
#gi0/0/0/0 - vlt_br/tag112 to r1 gi0/0/0/5
#gi0/0/0/2 - vlt_br/tag401 to r7 gi0/0/0/3

if (sys.argv[1]) in ['r05']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r05.img', '05', 'r05'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr05mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr05xr0', 'tag=112'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr05xr2', 'tag=401'])

# r11
#gi0/0/0/2 -  vlt_br/tag105 to r00
#gi0/0/0/3 -  vlt_br/tag402 to r12
#gi0/0/0/5 -  vlt_br/tag403 to r03

if (sys.argv[1]) in ['r11']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r11.img', '11', 'r11'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr11mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr11xr2', 'tag=105'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr11xr3', 'tag=402'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr11xr5', 'tag=403'])

# r12
#gi0/0/0/0 -  vlt_br/tag402 to r11
#gi0/0/0/5 -  vlt_br/tag139 to r03
#gi0/0/0/6 -  vlt_br/tag130 to r04

if (sys.argv[1]) in ['r12']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r12.img', '12', 'r12'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr12mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr12xr0', 'tag=402'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr12xr5', 'tag=139'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr12xr6', 'tag=130'])

# r03
#gi0/0/0/0 -  vlt_br/tag127 to r11 
#gi0/0/0/3 -  vlt_br/tag139 to r12

if (sys.argv[1]) in ['r03']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r03.img', '03', 'r03'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr03mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr03xr0', 'tag=127'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr03xr3', 'tag=139'])

# r4
#gi0/0/0/0 -  vlt_br/tag404 to r07 
#gi0/0/0/3 -  vlt_br/tag130 to r12

if (sys.argv[1]) in ['r04']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r04.img', '04', 'r04'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr04mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr04xr0', 'tag=404'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr04xr3', 'tag=130'])

# r7 - Dallas LSR
#gi0/0/0/0 -  vlt_br/tag400 to r01 
#gi0/0/0/1 -  vlt_br/tag401 to r05
#gi0/0/0/2 -  vlt_br/tag404 to r04
#gi0/0/0/7 -  vlt_br/tag405 to r01 

if (sys.argv[1]) in ['r07']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r07.img', '07', 'r07'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr07mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr07xr0', 'tag=400'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr07xr1', 'tag=401'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr07xr2', 'tag=404'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr07xr7', 'tag=405'])

##############################
# Amazon DMVPN

# r50 - corp site a R50
#g1 -  vlt_outside_br
#g2 -  vlt_br/tag500 to r51 g2
#g3 -  vlt_br/tag505 to r55 g2
#g4 -  vlt_mgt_br
if (sys.argv[1]) in ['r50']:
    subprocess.call(['virsh', 'start', 'r50'])

# r51 - small pop RR51
#g1 -  vlt_outside_br
#g2 -  vlt_br/tag500 to r50 g2
#g3 -  vlt_br/tag501 to r52 g2
#g4 -  vlt_mgt_br
if (sys.argv[1]) in ['r51']:
    subprocess.call(['virsh', 'start', 'r51'])

# r52 - AWS PE R52
#g1 -  vlt_outside_br
#g2 -  vlt_br/tag501 to r51 g3
#g3 -  vlt_br/tag502 to r53 g2
#g4 -  vlt_mgt_br
if (sys.argv[1]) in ['r52']:
    subprocess.call(['virsh', 'start', 'r52'])

# r53 - AWS PE53
#g1 -  vlt_outside_br
#g2 -  vlt_br/tag502 to r52 g3 
#g3 -  vlt_br/tag503 to r56 g2
#g4 -  vlt_mgt_br
#g5 -  vlt_br/tag509 to r58 g5
if (sys.argv[1]) in ['r53']:
    subprocess.call(['virsh', 'start', 'r53'])

# r56 - lg pop R56
#g1 -  vlt_outside_br
#g2 -  vlt_br/tag503 to r53 g3 
#g3 -  vlt_br/tag504 to r54 g2
#g4 -  vlt_mgt_br
#g5 -  vlt_br/tag510 to r57 g5
if (sys.argv[1]) in ['r56']:
    subprocess.call(['virsh', 'start', 'r56'])

# r54 - DC R54
#g1 -  vlt_outside_br
#g2 -  vlt_br/tag504 to r56 g3
#g3 -  vlt_br/tag508 to r58 g3
#g4 -  vlt_mgt_br
if (sys.argv[1]) in ['r54']:
    subprocess.call(['virsh', 'start', 'r54'])

# r55 - AWS PE55
#g1 -  vlt_outside_br
#g2 -  vlt_br/tag505 to r50 g3
#g3 -  vlt_br/tag506 to r57 g2
#g4 -  vlt_mgt_br
if (sys.argv[1]) in ['r55']:
    subprocess.call(['virsh', 'start', 'r55'])

# r57 - AWS PE57
#g1 -  vlt_outside_br
#g2 -  vlt_br/tag506 to r55 g3 
#g3 -  vlt_br/tag507 to r58 g2
#g4 -  vlt_mgt_br
#g5 -  vlt_br/tag510 to r56 g5
if (sys.argv[1]) in ['r57']:
    subprocess.call(['virsh', 'start', 'r57'])

# r58 - lg pop R58
#g1 -  vlt_outside_br
#g2 -  vlt_br/tag507 to r57 g3 
#g3 -  vlt_br/tag508 to r54 g3
#g4 -  vlt_mgt_br
#g5 -  vlt_br/tag509 to r53 g5
if (sys.argv[1]) in ['r58']:
    subprocess.call(['virsh', 'start', 'r58'])

############################
print "node started"


