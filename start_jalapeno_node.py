#!/usr/bin/env python

# This script starts routers in the Voltron demo topology - see .png file.  Interface/vswitch values are hardcoded 
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
#gi0/0/0/0 - vlt_br/tag100 to centos/voltron ens4
#gi0/0/0/1 - vlt_br/tag101 to voltron client and nsm vlan
#gi0/0/0/2 - vlt_br/tag102 to r1 gi0/0/0/0
#gi0/0/0/3 - vtl_br/tag103 to r2 gi0/0/0/0
#gi0/0/0/4 - vlt_br/tag104 to r3 gi0/0/0/0
#gi0/0/0/5 - vlt_br/tag105 to r4 gi0/0/0/0
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
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_scapy', 'rtr00xr9'])

# r01 
#gi0/0/0/0 - vlt_br/tag102 to r0 gi0/0/0/2
#gi0/0/0/1 - vlt_br/tag106 to r71 g1
#gi0/0/0/2 - vlt_br/tag107 to r72 g1
#gi0/0/0/3 - vlt_br/tag110 to r5 gi0/0/0/0
#gi0/0/0/9 - vlt_scapy 

if (sys.argv[1]) in ['r01']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r01.img', '01', 'r01'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr01mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr01xr0', 'tag=102'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr01xr1', 'tag=106'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr01xr2', 'tag=107'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr01xr3', 'tag=110'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_scapy', 'rtr01xr9'])

# r02
#gi0/0/0/0 - vlt_br/tag103 to r0 gi0/0/0/3
#gi0/0/0/1 - vlt_br/tag107 to r71 g2
#gi0/0/0/2 - vlt_br/tag108 to r72 g2
#gi0/0/0/3 - vlt_br/tag111 to r5 gi0/0/0/1
#gi0/0/0/9 - vlt_scapy 

if (sys.argv[1]) in ['r02']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r02.img', '02', 'r02'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr02mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr02xr0', 'tag=103'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr02xr1', 'tag=107'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr02xr2', 'tag=108'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr02xr3', 'tag=111'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_scapy', 'rtr02xr9'])

# r03
#gi0/0/0/0 -  vlt_br/tag104 to r00 
#gi0/0/0/1 -  vlt_br/tag112 to r05

if (sys.argv[1]) in ['r03']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r03.img', '03', 'r03'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr03mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr03xr0', 'tag=104'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr03xr1', 'tag=112'])

# r4
#gi0/0/0/0 -  vlt_br/tag105 to r00 
#gi0/0/0/1 -  vlt_br/tag113 to r05

if (sys.argv[1]) in ['r04']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r04.img', '04', 'r04'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr04mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr04xr0', 'tag=105'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr04xr1', 'tag=113'])

# r5
#gi0/0/0/0 -  vlt_br/tag110 to r01 
#gi0/0/0/1 -  vlt_br/tag111 to r02
#gi0/0/0/0 -  vlt_br/tag112 to r03
#gi0/0/0/1 -  vlt_br/tag113 to r04

if (sys.argv[1]) in ['r05']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r05.img', '05', 'r05'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr05mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr05xr0', 'tag=110'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr05xr1', 'tag=111'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr05xr2', 'tag=112'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr05xr3', 'tag=113'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_scapy', 'rtr05xr9'])

############################
print "node started"


