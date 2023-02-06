#!/bin/bash


# $1 --> Ethernet interface
# $2 --> An IP address (dans la plage des adresses de la passerelle)
# $3 --> Gateway IP address

xen-create-image --hostname myvm --force --ip 10.0.0.2 --vcpus 10 --pygrub --dist bionic
