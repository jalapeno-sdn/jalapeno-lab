#/bin/bash

echo adding ovs bridges
ovs-vsctl add-br vlt_br
ovs-vsctl add-br vlt_mgt_br
ovs-vsctl add-br vlt_outside_br
ovs-vsctl show
sleep 1

echo bringing up vlt interfaces
ifconfig vlt_br up
ifconfig vlt_mgt_br up
ifconfig vlt_outside_br up

ip addr add 10.251.251.1/24 dev vlt_mgt_br
ip addr add 10.0.254.1/24 dev vlt_outside_br
ifconfig

echo adding static routes
ip route add 10.0.250.0/23 via 10.0.254.71 dev vlt_outside_br
ip route add 10.0.129.0/23 via 10.0.254.72 dev vlt_outside_br
ip route add 10.0.130.0/23 via 10.0.254.71 dev vlt_outside_br
ip route add 10.0.131.0/23 via 10.0.254.72 dev vlt_outside_br
ip route add 10.0.132.0/23 via 10.0.254.71 dev vlt_outside_br
ip route add 10.0.201.0/24 via 10.0.254.77 dev vlt_outside_br

ip route

#print 'adding iptables nat rules'
#iptables -t nat -A POSTROUTING -o <server outside interface> -j MASQUERADE
#iptables --table nat --list

cd /opt/voltron-testbed/
sleep 1

echo define and launch openshift vm
virsh define config/os_base1.xml
virsh start os_base1

sleep 1

echo define and launch XE routers
virsh define config/r13.xml
virsh start r13
virsh define config/r40.xml
virsh start r40
virsh define config/r41.xml
virsh start r41
virsh define config/r42.xml
virsh start r42
virsh define config/r71.xml
virsh start r71
virsh define config/r72.xml
virsh start r72
virsh define config/r76.xml
virsh start r76
virsh define config/r77.xml
virsh start r77
virsh define config/r78.xml
virsh start r78
sleep 1

echo adding openshift iptables nat rules
iptables -t nat -A PREROUTING -p tcp -m tcp --dport 8443 -j DNAT --to-destination 10.0.250.2:8443
iptables -t nat -A PREROUTING -p tcp -m tcp --dport 30300 -j DNAT --to-destination 10.0.250.2:30300
iptables -t nat -A PREROUTING -p tcp -m tcp --dport 30852 -j DNAT --to-destination 10.0.250.2:30852
iptables -t nat -A PREROUTING -p tcp -m tcp --dport 30902 -j DNAT --to-destination 10.0.250.2:30902
iptables -t nat -A PREROUTING -p tcp -m tcp --dport 30308 -j DNAT --to-destination 10.0.250.2:30308
iptables -t nat -A PREROUTING -p tcp -m tcp --dport 30880 -j DNAT --to-destination 10.0.250.2:30880
iptables -t nat -A PREROUTING -p tcp -m tcp --dport 30881 -j DNAT --to-destination 10.0.250.2:30881
iptables --table nat --list

echo adding xrv9k pidfiles
touch pid/r00.pid
touch pid/r01.pid
touch pid/r02.pid
touch pid/r03.pid
touch pid/r04.pid
touch pid/r05.pid
touch pid/r11.pid
touch pid/r12.pid
touch pid/r22.pid
touch pid/r23.pid
touch pid/r32.pid
touch pid/r33.pid
touch pid/r34.pid
touch pid/r35.pid

echo starting routers
./start_router.py r00
sleep 2
./start_router.py r01
sleep 2
./start_router.py r02
sleep 2
./start_router.py r03
sleep 2
./start_router.py r04
sleep 2
./start_router.py r05
sleep 2
./start_router.py r11
sleep 2
./start_router.py r12
sleep 2
./start_router.py r22
sleep 2
./start_router.py r23
sleep 2
./start_router.py r32
sleep 2
./start_router.py r33
sleep 2
./start_router.py r34
sleep 2
./start_router.py r35
sleep 1

echo creating vltclient00 lxc
lxc-create -t ubuntu -n vltclient00

echo applying vlt_client lxc config file
cp config/vltclient00_lxc_config /var/lib/lxc/vltclient00/config

echo start vltclient00
lxc-start -n vltclient00


echo done
