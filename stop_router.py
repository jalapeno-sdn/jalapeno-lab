#!/usr/bin/env python

# Use this script to stop/shutdown a given xrv9k router
# example: sudo ./stop_router.py r00

from os import getpid
from sys import argv, exit
import psutil  ## pip install psutil
import sys
import time
import subprocess

if (sys.argv[1]) in ['r71']:
    subprocess.call(['virsh', 'destroy', 'r71'])

if (sys.argv[1]) in ['r72']:
    subprocess.call(['virsh', 'destroy', 'r72'])

if (sys.argv[1]) in ['r76']:
    subprocess.call(['virsh', 'destroy', 'r76'])

if (sys.argv[1]) in ['r77']:
    subprocess.call(['virsh', 'destroy', 'r77'])

if (sys.argv[1]) in ['r78']:
    subprocess.call(['virsh', 'destroy', 'r78'])

with open("pid/%s.pid" %(sys.argv[1])) as file:
    pid = file.read()

parent = psutil.Process(int(pid))
parent.kill()

print "router stopped"
time.sleep(1)

