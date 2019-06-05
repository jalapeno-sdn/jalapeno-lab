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

if (sys.argv[1]) in ['r20']:
    subprocess.call(['virsh', 'destroy', 'r20'])

if (sys.argv[1]) in ['r21']:
    subprocess.call(['virsh', 'destroy', 'r21'])

if (sys.argv[1]) in ['r22']:
    subprocess.call(['virsh', 'destroy', 'r22'])

if (sys.argv[1]) in ['lxc20']:
    subprocess.call(['lxc-stop', '-n', 'lxc20'])

if (sys.argv[1]) in ['lxc21']:
    subprocess.call(['lxc-stop', '-n', 'lxc21'])

if (sys.argv[1]) in ['lxc22']:
    subprocess.call(['lxc-stop', '-n', 'lxc22'])

with open("util/pid/%s.pid" %(sys.argv[1])) as file:
    pid = file.read()

parent = psutil.Process(int(pid))
parent.kill()

print "router stopped"
time.sleep(1)

