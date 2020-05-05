### Jalapeno XRv topology builder

1. Requirements: 
    * ubuntu 18.04, minimum 16 vCPU, 96GB memory, 200GB disk

2. Required packages:
    * apt-get install openssh-server lxc lxd-client qemu qemu-kvm libvirt-bin openvswitch-switch python-pip git
    * optional: apt-get install virt-manager kafkacat

3. Clone this archive

4. Construct router images
```
# May require sudo:

mkdir /opt/images/jalapeno
mv <image_name.qcow2> /opt/images/jalapeno/
cd /opt/images/jalapeno/

# Create .img files from qcow2

qemu-img create -b  xrv9k-fullk9-x-7.2.1.32I.qcow2 -f qcow2 r00.img
qemu-img create -b  xrv9k-fullk9-x-7.2.1.32I.qcow2 -f qcow2 r01.img
qemu-img create -b  xrv9k-fullk9-x-7.2.1.32I.qcow2 -f qcow2 r02.img
qemu-img create -b  xrv9k-fullk9-x-7.2.1.32I.qcow2 -f qcow2 r03.img

```

5. 


