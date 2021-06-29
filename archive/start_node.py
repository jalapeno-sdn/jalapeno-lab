#!/usr/bin/env python

# This script starts routers in the Jalapeno demo topology - see .png file.  Interface/vswitch values are hardcoded 
# into this script based on the topology file, however, if the user wishes to modify the topology they may do so by
# changing the ovs-vsctl command values below

from os import getpid
from sys import argv, exit
import sys
import time
import subprocess

# example:  sudo ./start_node.py r00

#################################################################################

########## Nodes on naja ########

# R00 
if (sys.argv[1]) in ['r00']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r00.img', '00', 'r00'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr00mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr00xr0', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr00xr1', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr00xr2', 'tag=102'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr00xr3', 'tag=103'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr00xr4', 'tag=128'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr00xr5', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr00xr6', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr00xr7'])

# R01 
if (sys.argv[1]) in ['r01']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r01.img', '01', 'r01'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr01mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr01xr0', 'tag=102'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr01xr1', 'tag=104'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr01xr2', 'tag=105'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr01xr3', 'tag=108'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr01xr4', 'tag=110'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr01xr5', 'tag=121'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr01xr6', 'tag=124'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr01xr7', 'tag=1012'])
    subprocess.call(['ovs-vsctl', 'add-port', 'gre-br1', 'rtr01xr8', 'tag=100'])
    subprocess.call(['ovs-vsctl', 'add-port', 'gre-br1', 'rtr01xr9', 'tag=102'])

# R02
if (sys.argv[1]) in ['r02']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r02.img', '02', 'r02'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr02mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr02xr0', 'tag=103'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr02xr1', 'tag=106'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr02xr2', 'tag=107'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr02xr3', 'tag=109'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr02xr4', 'tag=111'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr02xr5', 'tag=125'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr02xr6', 'tag=1012'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr02xr7'])
    subprocess.call(['ovs-vsctl', 'add-port', 'gre-br1', 'rtr02xr8', 'tag=101'])
    subprocess.call(['ovs-vsctl', 'add-port', 'gre-br1', 'rtr02xr9', 'tag=103'])

# R03 
if (sys.argv[1]) in ['r03']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r03.img', '03', 'r03'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr03mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr03xr0', 'tag=111'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr03xr1', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr03xr2', 'tag=112'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr03xr3', 'tag=363'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr03xr4', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr03xr5', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr03xr6', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr03xr7', 'tag=999'])

# R04 
if (sys.argv[1]) in ['r04']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r04.img', '04', 'r04'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr04mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr04xr0', 'tag=112'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr04xr1', 'tag=113'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr04xr2', 'tag=74'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr04xr3', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr04xr4', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr04xr5', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr04xr6', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr04xr7'])
    

# R05
if (sys.argv[1]) in ['r05']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r05.img', '05', 'r05'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr05mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr05xr0', 'tag=113'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr05xr1', 'tag=114'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr05xr2', 'tag=364'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr05xr3', 'tag=365'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr05xr4', 'tag=516'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr05xr5', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr05xr6', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr05xr7'])


# R06
if (sys.argv[1]) in ['r06']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r06.img', '06', 'r06'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr06mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr06xr0', 'tag=104'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr06xr1', 'tag=106'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr06xr2', 'tag=116'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr06xr3', 'tag=117'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr06xr4', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr06xr5', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr06xr6', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr06xr7'])
    

# R07
if (sys.argv[1]) in ['r07']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r07.img', '07', 'r07'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr07mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr07xr0', 'tag=104'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr07xr1', 'tag=107'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr07xr2', 'tag=118'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr07xr3', 'tag=119'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr07xr4', 'tag=366'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr07xr5', 'tag=367'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr07xr6', 'tag=130'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr07xr7'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr07xr8', 'tag=74'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr07xr9', 'tag=999'])    


# R08
if (sys.argv[1]) in ['r08']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r08.img', '08', 'r08'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr08mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr08xr0', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr08xr1', 'tag=108'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr08xr2', 'tag=115'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr08xr3', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr08xr4', 'tag=368'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr08xr5', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr08xr6', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr08xr7'])


# R09
if (sys.argv[1]) in ['r09']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r09.img', '09', 'r09'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr09mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr09xr0', 'tag=115'])
    subprocess.call(['ovs-vsctl', 'add-port', 'gre-br23', 'rtr09xr1', 'tag=103'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr09xr2', 'tag=369'])
    subprocess.call(['ovs-vsctl', 'add-port', 'gre-br23', 'rtr09xr3', 'tag=104'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr09xr4', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr09xr5', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr09xr6', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr09xr7'])

# R10
if (sys.argv[1]) in ['r10']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r10.img', '10', 'r10'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr10mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr10xr0', 'tag=121'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr10xr1', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr10xr2', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr10xr3', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr10xr4', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr10xr5', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr10xr6', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr10xr7'])
    

# R11
if (sys.argv[1]) in ['r11']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r11.img', '11', 'r11'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr11mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr11xr0', 'tag=128'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr11xr1', 'tag=129'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr11xr2', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr11xr3', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr11xr4', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr11xr5', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr11xr6', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr11xr7'])

# R12
if (sys.argv[1]) in ['r12']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r12.img', '12', 'r12'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr12mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr12xr0', 'tag=129'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr12xr1', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr12xr2', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr12xr3', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr12xr4', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr12xr5', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr12xr6', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr12xr7'])

# R13
if (sys.argv[1]) in ['r13']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r13.img', '13', 'r13'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr13mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr13xr0', 'tag=130'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr13xr1', 'tag=131'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr13xr2', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr13xr3', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr13xr4', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr13xr5', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr13xr6', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr13xr7'])

# R14
if (sys.argv[1]) in ['r14']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r14.img', '14', 'r14'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr14mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr14xr0', 'tag=131'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr14xr1', 'tag=132'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr14xr2', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr14xr3', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr14xr4', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr14xr5', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr14xr6', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr14xr7'])

# R15
if (sys.argv[1]) in ['r15']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r15.img', '15', 'r15'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr15mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr15xr0', 'tag=132'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr15xr1', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr15xr2', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr15xr3', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr15xr4', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr15xr5', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr15xr6', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr15xr7'])

# R16
if (sys.argv[1]) in ['r16']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r16.img', '16', 'r16'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr16mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr16xr0', 'tag=516'])
    subprocess.call(['ovs-vsctl', 'add-port', 'gre-br23', 'rtr16xr1', 'tag=100'])
    subprocess.call(['ovs-vsctl', 'add-port', 'gre-br23', 'rtr16xr2', 'tag=101'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr16xr3', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr16xr4', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr16xr5', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr16xr6', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr16xr7'])

########## Nodes on gojira ########

# R17
if (sys.argv[1]) in ['r17']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r17.img', '17', 'r17'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr17mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'gre-br23', 'rtr17xr0', 'tag=100'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr17xr1', 'tag=200'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr17xr2', 'tag=207'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr17xr3', 'tag=208'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr17xr4', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr17xr5', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr17xr6', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr17xr7'])


# R18
if (sys.argv[1]) in ['r18']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r18.img', '18', 'r18'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr18mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr18xr0', 'tag=200'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr18xr1', 'tag=203'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr18xr2', 'tag=202'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr18xr3', 'tag=209'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr18xr4', 'tag=210'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr18xr5', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr18xr6', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr18xr7'])


# R19
if (sys.argv[1]) in ['r19']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r19.img', '19', 'r19'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr19mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr19xr0', 'tag=203'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr19xr1', 'tag=204'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr19xr2', 'tag=205'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr19xr3', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr19xr4', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr19xr5', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr19xr6', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr19xr7'])


# R20
if (sys.argv[1]) in ['r20']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r20.img', '20', 'r20'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr20mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr20xr0', 'tag=204'])
    subprocess.call(['ovs-vsctl', 'add-port', 'gre-br23', 'rtr20xr1', 'tag=103'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr20xr2', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr20xr3', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr20xr4', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr20xr5', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr20xr6', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr20xr7'])


# R21
if (sys.argv[1]) in ['r21']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r21.img', '21', 'r21'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr21mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'gre-br23', 'rtr21xr0', 'tag=101'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr21xr1', 'tag=201'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr21xr2', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr21xr3', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr21xr4', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr21xr5', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr21xr6', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr21xr7'])


# R22
if (sys.argv[1]) in ['r22']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r22.img', '22', 'r22'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr22mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr22xr0', 'tag=201'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr22xr1', 'tag=202'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr22xr2', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr22xr3', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr22xr4', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr22xr5', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr22xr6', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr22xr7'])


# R23
if (sys.argv[1]) in ['r23']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r23.img', '23', 'r23'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr23mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr23xr0', 'tag=206'])
    subprocess.call(['ovs-vsctl', 'add-port', 'gre-br23', 'rtr23xr1', 'tag=104'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr23xr2', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr23xr3', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr23xr4', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr23xr5', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr23xr6', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr23xr7'])


# R24
if (sys.argv[1]) in ['r24']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r24.img', '24', 'r24'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr24mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr24xr0', 'tag=206'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr24xr1', 'tag=205'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr24xr2', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr24xr3', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr24xr4', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr24xr5', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr24xr6', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr24xr7'])


########## Nodes on bruce-dev ########

# R32 
if (sys.argv[1]) in ['r32']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r32.img', '32', 'r32'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr32mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'gre-br1', 'rtr32xr0', 'tag=100'])
    subprocess.call(['ovs-vsctl', 'add-port', 'gre-br1', 'rtr32xr1', 'tag=101'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr32xr2', 'tag=100'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr32xr3', 'tag=101'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr32xr4', 'tag=102'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr32xr5', 'tag=103'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr32xr6', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr32xr7', 'tag=999'])

# R33 
if (sys.argv[1]) in ['r33']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r33.img', '33', 'r33'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr33mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'gre-br1', 'rtr33xr0', 'tag=102'])
    subprocess.call(['ovs-vsctl', 'add-port', 'gre-br1', 'rtr33xr1', 'tag=103'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr33xr2', 'tag=104'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr33xr3', 'tag=105'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr33xr4', 'tag=106'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr33xr5', 'tag=107'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr33xr6', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr33xr7', 'tag=999'])

# R34
if (sys.argv[1]) in ['r34']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r34.img', '34', 'r34'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr34mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr34xr0', 'tag=100'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr34xr1', 'tag=104'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr34xr2', 'tag=108'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr34xr3', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr34xr4', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr34xr5', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr34xr6', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr34xr7', 'tag=999'])

# R35 
if (sys.argv[1]) in ['r35']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r35.img', '35', 'r35'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr35mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr35xr0', 'tag=101'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr35xr1', 'tag=105'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr35xr2', 'tag=109'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr35xr3', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr35xr4', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr35xr5', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr35xr6', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr35xr7', 'tag=999'])

# R36 
if (sys.argv[1]) in ['r36']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r36.img', '36', 'r36'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr36mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr36xr0', 'tag=112'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr36xr1', 'tag=113'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr36xr2', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr36xr3', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr36xr4', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr36xr5', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr36xr6', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr36xr7'])
    

# R38
if (sys.argv[1]) in ['r38']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r38.img', '38', 'r38'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr38mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr38xr0', 'tag=108'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr38xr1', 'tag=109'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr38xr2', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr38xr3', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr38xr4', 'tag=111'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr38xr5', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr38xr6', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr38xr7'])

# R39
if (sys.argv[1]) in ['r39']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r39.img', '39', 'r39'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr39mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr39xr0', 'tag=111'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr39xr1', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr39xr2', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr39xr3', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr39xr4', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr39xr5', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr39xr6', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'scapy', 'rtr39xr7'])


########## Nodes on Gojira ########

# R40
if (sys.argv[1]) in ['r40']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r40.img', '40', 'r40'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr40mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr40xr0', 'tag=215'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr40xr1', 'tag=216'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr40xr2', 'tag=224'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr40xr3', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr40xr4', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr40xr5', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr40xr6', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr40xr7', 'tag=999'])

# R41
if (sys.argv[1]) in ['r41']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r41.img', '41', 'r41'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr41mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'gre-br1', 'rtr41xr0', 'tag=207'])
    subprocess.call(['ovs-vsctl', 'add-port', 'gre-br1', 'rtr41xr1', 'tag=209'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr41xr2', 'tag=211'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr41xr3', 'tag=212'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr41xr4', 'tag=215'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr41xr5', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr41xr6', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr41xr7', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr41xr8', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr41xr9', 'tag=999'])

# R42
if (sys.argv[1]) in ['r42']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r42.img', '42', 'r42'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr42mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'gre-br1', 'rtr42xr0', 'tag=208'])
    subprocess.call(['ovs-vsctl', 'add-port', 'gre-br1', 'rtr42xr1', 'tag=210'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr42xr2', 'tag=213'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr42xr3', 'tag=214'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr42xr4', 'tag=216'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr42xr5', 'tag=217'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr42xr6', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr42xr7', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr42xr8', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr42xr9', 'tag=999'])

# R43
if (sys.argv[1]) in ['r43']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r43.img', '43', 'r43'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr43mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr43xr0', 'tag=211'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr43xr1', 'tag=213'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr43xr2', 'tag=218'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr43xr3', 'tag=219'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr43xr4', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr43xr5', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr43xr6', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr43xr7', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr43xr8', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr43xr9', 'tag=999'])

# R44
if (sys.argv[1]) in ['r44']:
    subprocess.call(['python', 'util/qemu-xrv9k.py', 'r44.img', '44', 'r44'])
    subprocess.call(['ovs-vsctl', 'add-port', 'mgt_br', 'rtr44mgt1'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr44xr0', 'tag=212'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr44xr1', 'tag=214'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr44xr2', 'tag=220'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr44xr3', 'tag=221'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr44xr4', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr44xr5', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr44xr6', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr44xr7', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr44xr8', 'tag=999'])
    subprocess.call(['ovs-vsctl', 'add-port', 'rtr_br', 'rtr44xr9', 'tag=999'])


############################
print "node started"
