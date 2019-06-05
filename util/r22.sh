#!/bin/bash

qemu-system-x86_64 -name r22 -pidfile r22.pid -enable-kvm -daemonize -display none -machine smm=off,accel=kvm -realtime mlock=off -rtc base=utc -smp 2 -m 8096 -bios /opt/images/voltron/bios2.bin -device ahci,id=ahci0,bus=pci.0 -drive file=/opt/images/voltron/nxosv.9.2.3.qcow2,if=none,id=drive-sata-disk0,format=qcow2 -device ide-drive,bus=ahci0.0,drive=drive-sata-disk0,id=drive-sata-disk0 -serial telnet::20220,server,nowait -monitor mon:telnet::20221,server,nowait -netdev tap,id=ge1,script=no,downscript=no,ifname=r22ge1 -device e1000,netdev=ge1,mac=52:00:00:ff:01:22 -netdev tap,id=ge2,script=no,downscript=no,ifname=r22ge2 -device e1000,netdev=ge2,mac=52:00:00:ff:02:22 -netdev tap,id=ge3,script=no,downscript=no,ifname=r22ge3 -device e1000,netdev=ge3,mac=52:00:00:ff:03:22

