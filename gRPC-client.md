### Steps to use gRPC client:

1. Configure routers with gRPC, TPA, and the interface which gRPC sessions will connect to:

```
grpc
 vrf MANAGEMENT
 port 57400
 address-family ipv4
 service-layer
!
tpa
 vrf MANAGEMENT
  address-family ipv4
   default-route mgmt
   update-source dataports MgmtEth0/RP0/CPU0/0
  !
 !
interface MgmtEth0/RP0/CPU0/0
 vrf MANAGEMENT
 ipv4 address 10.200.99.51 255.255.255.0
 ipv6 address 2010:10:200:99::51/128

```

2.  Configure and apply IPv6 ACL:

```
ipv6 access-list LOCATORS
 10 permit ipv6 any 2001:1:1:f001::/64
 20 permit ipv6 any 2001:1:1:f002::/64
 30 permit ipv6 any 2001:1:1:f003::/64
 40 permit ipv6 any 2001:1:1:f004::/64
 50 permit ipv6 any 2001:1:1:f005::/64
 60 permit ipv6 any 2001:1:1:f006::/64
!
interface HundredGigE0/0/0/2
 description to 5011-4 0/0
 mtu 9216
 ipv4 address 172.31.101.20 255.255.255.254
 ipv6 address 172:31:101:101::2e/126
 ipv6 access-group LOCATORS egress
```

3.  Download and unzip the client on a node with IP reachability to your router(s) gRPC server

4.  Add your router(s) IP/user/pw info to the client's 'routers' folder:

Example routers/IE-5508-2.json

```
{
 "host":"10.200.99.51:57400",
 "username":"admin",
 "password":"IELab123!",
 "tlshost":"ems.cisco.com",
 "tlspem":"/misc/config/grpc/ems.pem"
}
```

5.  Run the client:

```
./client -device routers/IE-5508-2.json -oper show-cmd-text -cli snips/get-ipv6-acl-counters.txt 
```

Output:

```
Not compression
EOF

---- show access-lists ipv6 LOCATORS hardware egress interface hundredGigE ----
-------------------------- 0/0/0/2 location 0/0/CPU0 --------------------------
ipv6 access-list LOCATORS
 10 permit ipv6 any 2001:1:1:f001::/64
 20 permit ipv6 any 2001:1:1:f002::/64
 30 permit ipv6 any 2001:1:1:f003::/64
 40 permit ipv6 any 2001:1:1:f004::/64
 50 permit ipv6 any 2001:1:1:f005::/64
 60 permit ipv6 any 2001:1:1:f006::/64
```

6. Another client example (get all BGP paths):

```
./client -device routers/IE-5508-2.json -oper get-oper -json snips/get-oper-bgp-paths.json 
```

