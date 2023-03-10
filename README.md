# check-vm-migration
The objective is to extract the features of the processors of a virtual machine that are necessary for the proper functioning of the applications that run on it. It will also be necessary to build the dependency graph of the features of the processor specific to the said virtual machine.

# how ?
Our approach is to write scripts that will automate the process of retrieving features (CPUID) from our virtual machine, and launching tests suites.

For this project we used the PostgreSQL application that provides tests. To do this, you need to install PostgreSQL from the source code:

 - follow the first three (03) steps of this tutorial : https://www.tecmint.com/install-postgresql-from-source-code-in-linux/

 - Then follow the instructions here : https://www.postgresql.org/docs/current/install-short.html


- In case of success of the tests we must have at the end of the execution this :

                    =======================
                    All 193 tests passed.
                    =======================
 
 - In the python folder, the script first.py must be launched in dom0. 
It contains the main program for automating the determination of the list of features necessary for the proper functioning of the application on the vm.

 - These features are contained in the file ./python/feautures.txt. 
    At the beginning, this file contains the list of all the features to be tested, these will be eliminated progressively until the necessary minimum of features is obtained.    


# scenario
 - The cpuid file (cpuid.c++), allows us to discover the features of the virtual machine.
We execute this code a first time in the virtual machine in order to recover the global features.

Once obtained, we delete the disabled features because they cannot be modified.  

 - Then we take the active features one by one, we deactivate them and we appreciate the behavior of the virtual machine (#1), then that of PostgreSQL (#2).

        |__(#1)There are some features necessary to start the virtual      
        |    machine, without them the machine will sputter. 
        |
        |
        |
        |__(#2) Other features may be unnecessary for the virtual machine 
            startup, but rather necessary for the application operation: these are the important features.
        |
        |__(#3) We also notice that when we disable some features, others are automatically set to 0 (disabled).
            This is how we were able to establish the dependencies between the features. 
