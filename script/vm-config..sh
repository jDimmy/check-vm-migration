#!/bin/bash

sudo bash

ip link set eth0 up

# apt-get install nano
echo "-----------------vi editor--------------"
echo "Press 'i' to write"
echo "Press 'x' to erase"
echo "Press 'esc' ':' 'x' to save and exit"

sleep 5
vi /etc/netplan/01-netcfg.yaml

netplan applych
sleep 3
