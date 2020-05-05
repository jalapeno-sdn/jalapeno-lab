### voltron-testbed

1. Requirements: 
    * ubuntu 18.04, minimum 16 vCPU, 96GB memory, 200GB disk

2. Required packages:
    * apt-get install openssh-server lxc lxd-client qemu qemu-kvm libvirt-bin openvswitch-switch python-pip git
    * optional: apt-get install virt-manager kafkacat

3. Clone this archive into /opt

4. Get your server's outside eth interface name.  Edit vlt_build_testbed_from_scratch.sh and replace <server outside interface> with the interface name. Uncomment the iptables masquerade line

5. cd into util/ and run build_testbed_from_scratch.sh
...or...
5a.  It may be better to manually execute the steps outlined in build_testbed_from_scratch.sh one-by-one

6. Once the script is complete, check the status of routers/vms, verify routes, etc:
    Example XR router console access:
    R00 -> telnet localhost 20000
    R05 -> telnet localhost 20050
    Example CSR router console access:
    sudo virsh console r71

Optional:

7. Add latencies to the topology. Examples:
sudo tc qdisc add dev r71ge1 root netem delay 120000 <br>
sudo tc qdisc add dev r71ge2 root netem delay 150000 <br>
sudo tc qdisc add dev r72ge1 root netem delay 180000 <br>
sudo tc qdisc add dev r72ge2 root netem delay 210000 <br>
