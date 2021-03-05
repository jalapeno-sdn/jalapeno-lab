Streaming of specific telemetry data from IOS-XR routers

1.	Install pyang (a handy python-based tool for exploring a YANG data model’s tree structure)

brmcdoug > pip install pyang
/usr/lib/python2.7/dist-packages/OpenSSL/crypto.py:12: CryptographyDeprecationWarning: Python 2 is no longer supported by the Python core team. Support for it is now deprecated in cryptography, and will be removed in a future release.
  from cryptography import x509
Collecting pyang
  Downloading https://files.pythonhosted.org/packages/12/22/16c98564086f4f5901b7e8d886ad928ce6eceb577b3504edc333762df92f/pyang-2.4.0-py2.py3-none-any.whl (591kB)
    100% |████████████████████████████████| 593kB 639kB/s 
Collecting lxml (from pyang)
  Downloading https://files.pythonhosted.org/packages/15/55/ddcb9b3428c94aa2794f248897418178ee812288688f9cc8ec5147a4be47/lxml-4.6.2-cp27-cp27mu-manylinux1_x86_64.whl (5.5MB)
    100% |████████████████████████████████| 5.5MB 122kB/s 
Installing collected packages: lxml, pyang
Successfully installed lxml-4.6.2 pyang-2.4.0


2.	Clone YANG model repository

brmcdoug > git clone https://github.com/YangModels/yang.git
Cloning into 'yang'...
remote: Enumerating objects: 141, done.
remote: Counting objects: 100% (141/141), done.
remote: Compressing objects: 100% (109/109), done.
remote: Total 37061 (delta 49), reused 105 (delta 32), pack-reused 36920
Receiving objects: 100% (37061/37061), 79.09 MiB | 2.94 MiB/s, done.
Resolving deltas: 100% (28351/28351), done.
Checking out files: 100% (41574/41574), done.


3.	CD into XR release directory and list data models (or grep for specifics)

brmcdoug > cd yang/vendor/cisco/xr/721

brmcdoug > ls | grep openconfig-interfaces
cisco-xr-openconfig-interfaces-deviations.yang
openconfig-interfaces.yang


4.	Run pyang against a specific model (go 2 or 3 levels down into the tree to begin with)

brmcdoug > pyang -f tree --tree-depth 3 openconfig-interfaces.yang
module: openconfig-interfaces
  +--rw interfaces
     +--rw interface* [name]
        +--rw name             -> ../config/name
        +--rw config
        |     ...
        +--ro state
        |     ...
        +--rw hold-time
        |     ...
        +--rw subinterfaces
              ...


5.	Explore deeper into the tree

brmcdoug > pyang -f tree --tree-depth 5 openconfig-interfaces.yang
module: openconfig-interfaces
  +--rw interfaces
     +--rw interface* [name]
        +--rw name             -> ../config/name
        +--rw config
        |  +--rw name?            string
        |  +--rw type             identityref
        |  +--rw mtu?             uint16
        |  +--rw loopback-mode?   boolean
        |  +--rw description?     string
        |  +--rw enabled?         boolean
        +--ro state
        |  +--ro name?            string
        |  +--ro type             identityref
        |  +--ro mtu?             uint16
        |  +--ro loopback-mode?   boolean
        |  +--ro description?     string
        |  +--ro enabled?         boolean
        |  +--ro ifindex?         uint32
        |  +--ro admin-status     enumeration
        |  +--ro oper-status      enumeration
        |  +--ro last-change?     oc-types:timeticks64
        |  +--ro logical?         boolean
        |  +--ro counters
        |     +--ro in-octets?             oc-yang:counter64
        |     +--ro in-pkts?               oc-yang:counter64
        |     +--ro in-unicast-pkts?       oc-yang:counter64
        |     +--ro in-broadcast-pkts?     oc-yang:counter64
        |     +--ro in-multicast-pkts?     oc-yang:counter64
        |     +--ro in-discards?           oc-yang:counter64
        |     +--ro in-errors?             oc-yang:counter64
        |     +--ro in-unknown-protos?     oc-yang:counter64
        |     +--ro in-fcs-errors?         oc-yang:counter64
        |     +--ro out-octets?            oc-yang:counter64
        |     +--ro out-pkts?              oc-yang:counter64
        |     +--ro out-unicast-pkts?      oc-yang:counter64
        |     +--ro out-broadcast-pkts?    oc-yang:counter64
        |     +--ro out-multicast-pkts?    oc-yang:counter64
        |     +--ro out-discards?          oc-yang:counter64
        |     +--ro out-errors?            oc-yang:counter64
        |     +--ro carrier-transitions?   oc-yang:counter64
        |     +--ro last-clear?            oc-types:timeticks64
        +--rw hold-time
        |  +--rw config
        |  |  +--rw up?     uint32
        |  |  +--rw down?   uint32
        |  +--ro state
        |     +--ro up?     uint32
        |     +--ro down?   uint32
        +--rw subinterfaces
           +--rw subinterface* [index]
              +--rw index     -> ../config/index
              +--rw config
              |     ...
              +--ro state
                    ...


6.	Derive YANG path for streaming telemetry

brmcdoug > pyang -f tree --tree-depth 5 openconfig-interfaces.yang
module: openconfig-interfaces
  +--rw interfaces
     +--rw interface
        +--rw name             -> ../config/name
        +--rw config
        |  +--rw name?            string
        |  +--rw type             identityref
        |  +--rw mtu?             uint16
        |  +--rw loopback-mode?   boolean
        |  +--rw description?     string
        |  +--rw enabled?         boolean
        +--ro state
        |  +--ro name?            string
        |  +--ro type             identityref
        |  +--ro mtu?             uint16
        |  +--ro loopback-mode?   boolean
        |  +--ro description?     string
        |  +--ro enabled?         boolean
        |  +--ro ifindex?         uint32
        |  +--ro admin-status     enumeration
        |  +--ro oper-status      enumeration
        |  +--ro last-change?     oc-types:timeticks64
        |  +--ro logical?         boolean
        |  +--ro counters

// Our Path = openconfig-interfaces:interfaces/interface/state/counters


7.	Configure streaming of specific YANG path data

RP/0/RP0/CPU0:R12-LSR(config)#telemetry model-driven
RP/0/RP0/CPU0:R12-LSR(config-model-driven)# sensor-group openconfig_interfaces
RP/0/RP0/CPU0:R12-LSR(config-model-driven-snsr-grp)#  sensor-path openconfig-interfaces:interfaces/interface/state/counters
RP/0/RP0/CPU0:R12-LSR(config-model-driven-snsr-grp)#commit

RP/0/RP0/CPU0:R12-LSR#sho run telemetry model-driven 
Fri Mar  5 09:32:19.895 PST
telemetry model-driven
 destination-group jalapeno
  address-family ipv4 10.251.251.1 port 32400
   encoding self-describing-gpb
   protocol grpc no-tls
  !
 !
 sensor-group openconfig_interfaces
  sensor-path openconfig-interfaces:interfaces/interface/state/counters
 !
 subscription base_metrics
  sensor-group-id openconfig_interfaces sample-interval 10000
  destination-id jalapeno
  source-interface Loopback0


8.	Validate XR resolves the YANG path

RP/0/RP0/CPU0:R12-LSR#sho telemetry model-driven sensor-group openconfig_interfaces 
Fri Mar  5 09:29:44.267 PST
  Sensor Group Id:openconfig_interfaces
    Sensor Path:        openconfig-interfaces:interfaces/interface/state/counters
    Sensor Path State:  Resolved

RP/0/RP0/CPU0:R12-LSR#

// XR is now streaming openconfig-interface counters to the collector at 10.251.251.1 on port 32400


9.	Example data (in this case the router sends its streaming telemetry to a Telegraf collector which publishes the data to Kafka.  Output below is raw data on the Kafka telemetry topic)

openconfig-interfaces:interfaces/interface/state/counters,host=telegraf,name=GigabitEthernet0/0/0/0,path=openconfig-interfaces:interfaces/interface/state/counters,source=R12-LSR,subscription=base_metrics in_pkts=13i,in_octets=910i,out_pkts=5762i,out_octets=8018782i,in_multicast_pkts=0i,in_broadcast_pkts=0i,out_multicast_pkts=0i,out_broadcast_pkts=1i,in_unknown_protos=0i,in_errors=0i,in_fcs_errors=0i,out_errors=0i,carrier_transitions=0i,last_clear="2021-03-05T04:04:00Z",in_unicast_pkts=13i,in_discards=0i,out_unicast_pkts=5761i,out_discards=0i 1614964967334000000

openconfig-interfaces:interfaces/interface/state/counters,host=telegraf,name=GigabitEthernet0/0/0/1,path=openconfig-interfaces:interfaces/interface/state/counters,source=R12-LSR,subscription=base_metrics in_pkts=13i,in_octets=910i,out_pkts=5776i,out_octets=8045932i,in_multicast_pkts=0i,in_broadcast_pkts=0i,out_multicast_pkts=0i,out_broadcast_pkts=1i,in_unknown_protos=0i,in_errors=0i,in_fcs_errors=0i,out_errors=0i,carrier_transitions=0i,last_clear="2021-03-05T04:04:00Z",in_unicast_pkts=13i,in_discards=0i,out_unicast_pkts=5775i,out_discards=0i 1614964967334000000

openconfig-interfaces:interfaces/interface/state/counters,host=telegraf,name=GigabitEthernet0/0/0/2,path=openconfig-interfaces:interfaces/interface/state/counters,source=R12-LSR,subscription=base_metrics in_pkts=10006i,in_octets=8663864i,out_pkts=7183i,out_octets=8617482i,in_multicast_pkts=0i,in_broadcast_pkts=0i,out_multicast_pkts=0i,out_broadcast_pkts=2i,in_unknown_protos=0i,in_errors=0i,in_fcs_errors=0i,out_errors=0i,carrier_transitions=0i,last_clear="2021-03-05T04:04:00Z",in_unicast_pkts=10006i,in_discards=0i,out_unicast_pkts=7181i,out_discards=0i 1614964967334000000

openconfig-interfaces:interfaces/interface/state/counters,host=telegraf,name=GigabitEthernet0/0/0/3,path=openconfig-interfaces:interfaces/interface/state/counters,source=R12-LSR,subscription=base_metrics in_pkts=8830i,in_octets=8586154i,out_pkts=8832i,out_octets=8769321i,in_multicast_pkts=0i,in_broadcast_pkts=0i,out_multicast_pkts=0i,out_broadcast_pkts=2i,in_unknown_protos=0i,in_errors=0i,in_fcs_errors=0i,out_errors=0i,carrier_transitions=0i,last_clear="2021-03-05T04:04:00Z",in_unicast_pkts=8830i,in_discards=0i,out_unicast_pkts=8830i,out_discards=0i 1614964967334000000
