#! /usr/bin/env python

# Set log level to benefit from Scapy warnings
import logging
logging.getLogger("scapy").setLevel(1)

from scapy.all import *
import subprocess
import sys
import time
from random import getrandbits, randint
from ipaddress import IPv4Network, IPv4Address

class MPLS(Packet):
         name = "MPLS"
         fields_desc =  [
                 BitField("label", 3, 20),
                 BitField("experimental_bits", 0, 3),
                 BitField("bottom_of_label_stack", 1, 1),
                 ByteField("TTL", 255)
                 ]

bind_layers(Ether, MPLS, type = 0x8847)
bind_layers(MPLS, MPLS, bottom_of_label_stack = 0)
bind_layers(MPLS, IP)

def getRandomIP():
    subnet = IPv4Network(u"10.0.130.0/24") 
    bits = getrandbits(subnet.max_prefixlen - subnet.prefixlen)
    addr = IPv4Address(subnet.network_address + bits)
    addr_str = str(addr)
    print(addr_str)
    return addr_str

def getRandomEXP():
    ranInt = randint(0,7)
    #if ranInt == 2:
    #   ranInt = ranInt + 1
    print(ranInt)
    return ranInt

i = 0
while i < 1000000:
    i += 1
    newIP = getRandomIP()
    newExp = getRandomEXP()
    p = Ether(src = "00:16:3e:d6:79:f5", dst = "52:00:00:ff:01:00") \
    / MPLS(label = 100001) / MPLS(label = 100009) / MPLS(label = 100004, experimental_bits = newExp, bottom_of_label_stack=1) \
    / IP(src = newIP, dst = "10.0.0.4") / ICMP()
    sendp(p, iface="eth0", count=100)
