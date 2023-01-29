# check-vm-migration
The objective is to extract the features of the processors of a virtual machine that are necessary for the proper functioning of the applications that run on it. It will also be necessary to build the dependency graph of the features of the processor specific to the said virtual machine.

# how ?
Our approach is to write scripts that will automate the process of retrieving features (CPUID) from our virtual machine, and launching tests suites.

For this project we used the PostgreSQL application that provides tests. To do this, you need to install PostgreSQL from the source code:

 --> follow the first three (03) steps of this tutorial : https://www.tecmint.com/install-postgresql-from-source-code-in-linux/

 --> Then follow the instructions here : https://www.postgresql.org/docs/current/install-short.html


--> In case of success of the tests we must have at the end of the execution this :

                        =======================
                        All 193 tests passed.
                        =======================



