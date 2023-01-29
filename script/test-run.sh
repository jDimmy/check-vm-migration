#!/bin/bash

su - root
su - postgres
cd postgresql-12.0

make check > check_result.txt
scp check_result.txt $1@$2:~/Documents/xen-virt/code/

su - popo
./test2 > check_cpuid.txt
scp check_cpuid.txt $1@$2:~/Documents/xen-virt/code/test_cpuid_bits.txt


shutdown