#!/bin/bash


# $1 --> Ethernet interface
# $2 --> An IP address (dans la plage des adresses de la passerelle)
# $3 --> Gateway IP address


brtcl addbr xenbr0
brctl addif xenbr0 $1
ip route
ifconfig $1
ifconfig $1 0.0.0.0
ifconfig xenbr0 $2
ip route add default via $3 dev xenbr0