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


############################
print "node started"


