#!/usr/bin/env python

# This script starts routers in the Jalapeno demo topology - see .png file.  Interface/vswitch values are hardcoded 
# into this script based on the topology file, however, if the user wishes to modify the topology they may do so by
# changing the ovs-vsctl command values below

from os import getpid
from sys import argv, exit
import sys
import time
import subprocess

# example:  sudo ./start_router_eqnx.py r00

#################################################################################

# R00
#g0/0/0/0 - jlpn_br/tag100 to client VM (if exists)
#g0/0/0/1 - jlpn_br/tag101 to R01 g0/0/0/0
#g0/0/0/2 - jlpn_br/tag102 to R02 g0/0/0/0
#g0/0/0/3 - jlpn_br/tag103 to R03 gi0/0/0/0
#g0/0/0/4 - jlpn_br/tag104 to R04 gi0/0/0/0

if (sys.argv[1]) in ['r00']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r00.img', '00', 'r00'])
    subprocess.call(['ovs-vsctl', 'add-port', 'jlpn_mgt_br', 'rtr00mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'jlpn_br', 'r00ge0', 'tag=100'])
    subprocess.call(['ovs-vsctl', 'add-port', 'jlpn_br', 'rtr00xr1', 'tag=101'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr00xr2', 'tag=102'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr00xr3', 'tag=103'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr00xr4', 'tag=104'])

# R01 
#g0/0/0/0 - jlpn_br/tag103 to R00 g0/0/0/1
#g0/0/0/1 - jlpn_br/tag400 to R03 g0/0/0/3
#g0/0/0/5 - jlpn_br/tag112 to R04 g0/0/0/3

if (sys.argv[1]) in ['r01']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r01.img', '01', 'r01'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr01mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr01xr0', 'tag=101'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr01xr1', 'tag=105'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr01xr5', 'tag=106'])

# R02 
#g0/0/0/0 - jlpn_br/tag104 to R00 gi0/0/0/4
#g0/0/0/2 - vlt_br/tag107 to R03 gi0/0/0/4
#g0/0/0/2 - vlt_br/tag108 to R04 gi0/0/0/4

if (sys.argv[1]) in ['r05']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r05.img', '05', 'r05'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr05mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr05xr0', 'tag=104'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr05xr2', 'tag=107'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr05xr2', 'tag=108'])

# R03
#gi0/0/0/0 -  jlpn_br/tag102 to R00 g0/0/0/2
#gi0/0/0/1 -  jlpn_br/tag109 to R71 g1
#gi0/0/0/2 -  jlpn_br/tag110 to R72 g1
#gi0/0/0/3 -  jlpn_br/tag105 to R01 g0/0/0/1
#gi0/0/0/4 -  jlpn_br/tag107 to R02 g0/0/0/1

if (sys.argv[1]) in ['r03']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r03.img', '03', 'r03'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr04mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr03xr0', 'tag=102'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr03xr1', 'tag=109'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr03xr2', 'tag=110'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr03xr3', 'tag=105'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr03xr4', 'tag=107'])
    
# R04
#gi0/0/0/0 -  jlpn_br/tag103 to R00 g0/0/0/2
#gi0/0/0/1 -  jlpn_br/tag111 to R71 g1
#gi0/0/0/2 -  jlpn_br/tag112 to R72 g1
#gi0/0/0/3 -  jlpn_br/tag106 to R01 g0/0/0/1
#gi0/0/0/4 -  jlpn_br/tag108 to R02 g0/0/0/1

if (sys.argv[1]) in ['r04']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r04.img', '04', 'r04'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_mgt_br', 'rtr04mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr04xr0', 'tag=103'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr04xr1', 'tag=111'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr04xr2', 'tag=112'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr04xr3', 'tag=106'])
    subprocess.call(['ovs-vsctl', 'add-port', 'vlt_br', 'rtr04xr4', 'tag=108'])

# R71 External Peer
#g1 - vlt_br/tag109 to r1 gi0/0/0/1 
#g2 - vlt_br/tag110 to r2 gi0/0/0/1
#g3 - not used
#g4 - vlt_outside_br br to internet_user_vlan

if (sys.argv[1]) in ['r71']:
    subprocess.call(['virsh', 'start', 'r71'])

# R72 External Peer
#g1 - vlt_br/tag111 to r2 gi0/0/0/2 
#g2 - vlt_br/tag112 to r1 gi0/0/0/2
#g3 - not used
#g4 - vlt_outside_br br to internet_user_vlan

if (sys.argv[1]) in ['r72']:
    subprocess.call(['virsh', 'start', 'r72'])

############################
print "node started"


