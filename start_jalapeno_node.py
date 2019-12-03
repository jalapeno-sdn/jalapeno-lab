#!/usr/bin/env python

# This script starts routers in the Jalapeno demo topology - see .png file.  Interface/vswitch values are hardcoded 
# into this script based on the topology file, however, if the user wishes to modify the topology they may do so by
# changing the ovs-vsctl command values below

from os import getpid
from sys import argv, exit
import sys
import time
import subprocess

# example:  sudo ./start_jalapeno_node.py r00

#################################################################################

# r00
#gi0/0/0/0 - vlt_k8s to baremetal openshift
#gi0/0/0/1 - vlt_client to voltron client and nsm vlan
#gi0/0/0/2 - vlt_br/tag102 to r1 gi0/0/0/0
#gi0/0/0/3 - vtl_br/tag103 to r2 gi0/0/0/0
#gi0/0/0/9 - vlt_outside_br for scapy
if (sys.argv[1]) in ['r00']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r00.img', '00', 'r00'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr00mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_k8s', 'rtr00xr0'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr00xr1', 'tag=101'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr00xr2', 'tag=102'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr00xr3', 'tag=103'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_scapy', 'rtr00xr9'])

# r01 
#gi0/0/0/0 - vlt_br/tag102 to r00 g2
#gi0/0/0/1 - vlt_br/tag104 to r06 g0
#gi0/0/0/2 - vlt_br/tag105 to r07 g0
#gi0/0/0/3 - vlt_br/tag108 to r08 g1
#gi0/0/0/4 - vlt_br/tag110 to r03 g1
#gi0/0/0/9 - vlt_scapy 

if (sys.argv[1]) in ['r01']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r01.img', '01', 'r01'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr01mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr01xr0', 'tag=102'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr01xr1', 'tag=104'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr01xr2', 'tag=105'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr01xr3', 'tag=108'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr01xr4', 'tag=110'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_scapy', 'rtr01xr9'])

# r02
#gi0/0/0/0 - vlt_br/tag103 to r00 g3
#gi0/0/0/1 - vlt_br/tag106 to r06 g1
#gi0/0/0/2 - vlt_br/tag107 to r07 g1
#gi0/0/0/3 - vlt_br/tag109 to r08 g0
#gi0/0/0/4 - vlt_br/tag111 to r03 g0
#gi0/0/0/9 - vlt_scapy 

if (sys.argv[1]) in ['r02']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r02.img', '02', 'r02'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr02mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr02xr0', 'tag=103'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr02xr1', 'tag=106'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr02xr2', 'tag=107'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr02xr3', 'tag=109'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr02xr4', 'tag=111'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_scapy', 'rtr02xr9'])

# r03
#gi0/0/0/0 -  vlt_br/tag111 to r02 g4
#gi0/0/0/1 -  vlt_br/tag110 to r01 g4
#gi0/0/0/2 -  vlt_br/tag112 to r04 g0

if (sys.argv[1]) in ['r03']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r03.img', '03', 'r03'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr03mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr03xr0', 'tag=111'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr03xr1', 'tag=110'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr03xr2', 'tag=112'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_scapy', 'rtr03xr9'])

# r04
#gi0/0/0/0 -  vlt_br/tag112 to r03 g2
#gi0/0/0/1 -  vlt_br/tag113 to r05 g0

if (sys.argv[1]) in ['r04']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r04.img', '04', 'r04'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr04mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr04xr0', 'tag=112'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr04xr1', 'tag=113'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_scapy', 'rtr04xr9'])

# r05
#gi0/0/0/0 -  vlt_br/tag113 to r04 g1
#gi0/0/0/1 -  vlt_br/tag114 to r09 g1
#gi0/0/0/1 -  vlt_edge

if (sys.argv[1]) in ['r05']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r05.img', '05', 'r05'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr05mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr05xr0', 'tag=113'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr05xr1', 'tag=114'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_edge', 'rtr05xr2'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_scapy', 'rtr05xr9'])

# r06
#gi0/0/0/0 -  vlt_br/tag104 to r01 g1
#gi0/0/0/1 -  vlt_br/tag106 to r02 g1
#gi0/0/0/2 -  vlt_br/tag116 to r71 g1
#gi0/0/0/3 -  vlt_br/tag117 to r72 g1

if (sys.argv[1]) in ['r06']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r06.img', '06', 'r06'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr06mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr06xr0', 'tag=104'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr06xr1', 'tag=106'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr06xr2', 'tag=116'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr06xr3', 'tag=117'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_scapy', 'rtr06xr9'])

# r07
#gi0/0/0/0 -  vlt_br/tag105 to r01 g2
#gi0/0/0/1 -  vlt_br/tag107 to r02 g2
#gi0/0/0/2 -  vlt_br/tag118 to r71 g2
#gi0/0/0/3 -  vlt_br/tag119 to r72 g2

if (sys.argv[1]) in ['r07']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r07.img', '07', 'r07'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr07mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr07xr0', 'tag=105'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr07xr1', 'tag=107'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr07xr2', 'tag=118'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr07xr3', 'tag=119'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_scapy', 'rtr07xr9'])

# r08
#gi0/0/0/0 -  vlt_br/tag109 to r02 g3
#gi0/0/0/1 -  vlt_br/tag108 to r01 g3
#gi0/0/0/2 -  vlt_br/tag115 to r09 g0

if (sys.argv[1]) in ['r08']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r08.img', '08', 'r08'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr08mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr08xr0', 'tag=109'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr08xr1', 'tag=108'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr08xr2', 'tag=115'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_scapy', 'rtr08xr9'])

# r09
#gi0/0/0/0 -  vlt_br/tag115 to r08 g2
#gi0/0/0/1 -  vlt_br/tag114 to r05 g1
#gi0/0/0/2 -  vlt_edge to nsm01

if (sys.argv[1]) in ['r09']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r09.img', '09', 'r09'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr09mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr09xr0', 'tag=115'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr09xr1', 'tag=114'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_edge', 'rtr09xr2'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_scapy', 'rtr09xr9'])



##### R99 test router

# r99

if (sys.argv[1]) in ['r99']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r99.img', '99', 'r99'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr99mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_outside_br', 'rtr99xr0'])








############################
print "node started"

