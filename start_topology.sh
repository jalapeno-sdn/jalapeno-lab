#/bin/sh

echo 'define routers with virsh'

echo 'virsh define r00.xml'
virsh define r00.xml

echo 'virsh define r01.xml'
virsh define r01.xml

echo 'virsh define r02.xml'
virsh define r02.xml

echo 'virsh define r03.xml'
virsh define r03.xml

sleep 1
echo 'adding briges'
brctl addbr br0
ifconfig br0 up
echo 'brctl addbr br0'
brctl addbr br1
ifconfig br1 up
echo 'brctl addbr br1'
brctl addbr br2
ifconfig br2 up
echo 'brctl addbr br2'
brctl addbr br3
ifconfig br3 up
echo 'brctl addbr br3'
brctl addbr br4
ifconfig br4 up
echo 'brctl addbr br4'
brctl addbr br5
ifconfig br5 up
echo 'brctl addbr br5'
brctl addbr br6
ifconfig br6 up
echo 'brctl addbr br6'
brctl addbr br7
ifconfig br7 up
echo 'brctl addbr br7'
brctl addbr br99

sleep 1
echo 'starting routers'
echo 'virsh start r00'
virsh start r00

echo 'virsh start r01'
virsh start r01

echo 'virsh start r02'
virsh start r02

echo 'virsh start r03'
virsh start r03

