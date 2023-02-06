#!/bin/bash

su - postgres

# test suites
cd postgresql-12.0
make check > check_result.txt
scp check_result.txt ubuntu@192.168.42.101:~/etc/xen/

# cpuid command
./cpuid
./cpuid
scp cpuid_bits.txt ubuntu@192.168.42.101:~/etc/xen/cpuid_bits.txt
scp test_cpuid_bits.txt ubuntu@192.168.42.101:~/etc/xen/test_cpuid_bits.txt


sudo shutdown -h now