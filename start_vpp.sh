#!/bin/bash

qemu-system-x86_64 -enable-kvm -daemonize -display none \
-rtc base=utc \
-smp sockets=1,cores=1,threads=1 \
-m 2048 \
-drive file=/opt/images/voltron/ubuntu-18.04.1-server-amd64.iso,media=disk,if=virtio,index=0 \
-serial telnet::30000,server,nowait \
-monitor mon:telnet::30001,server,nowait \
-netdev tap,id=mgmt0,ifname=vpp0,script=no,downscript=no \
-device virtio,netdev=mgmt0,mac=18:54:00:8a:26:d6 \
-netdev tap,id=eth1,ifname=vpp-eth1,script=no,downscript=no \
-device virtio,netdev=eth1,mac=18:54:01:8a:26:d6 \
-netdev tap,id=eth2,ifname=vpp-eth2,script=no,downscript=no \
-device virtio,netdev=eth2,mac=18:54:02:8a:26:d6 \
-name vpp -pidfile vpp.pid
