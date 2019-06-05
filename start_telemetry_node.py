#!/usr/bin/env python

# This script starts nodes in the streaming telemetry demo topology - see .png file.  Interface/vswitch values are hardcoded 
# into this script based on the topology file, however, if the user wishes to modify the topology they may do so by
# changing the ovs-vsctl command values below

from os import getpid
from sys import argv, exit
import sys
import time
import subprocess

# example:  sudo ./start_telemetry.py r20

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
    subprocess.call(['util/r22.sh'])  
    
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

