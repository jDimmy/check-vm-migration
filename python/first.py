def modification_dict(reg : str, feats : dict) -> dict:
    
    """"
        Dictionnaire 
    """
    mod_dict = {}
    i = 0
    for j in feats.keys():
        mod_dict[j] = feats[j] == reg[i]
        i += 1

    return mod_dict


def feature_dep(feature : str, feat_dep : dict, mod_dict = dict) -> dict:

    for i in mod_dict.keys():
        if not mod_dict[i] and i is not feature :
            if feature in feat_dep:
                feat_dep[feature].append(i)
            else:
                feat_dep[feature] = [i]

    return feat_dep


def no_dep(feat_dep : dict) -> dict:

    for i in feat_dep.keys():
        if not feat_dep[i] :
            feat_dep.pop(i, None)

    return feat_dep


def zero_features(feats : dict, feat_dict : dict) -> dict:

    feats["zero_features"] = []
    for i in feat_dict.keys():
        if feat_dict[i] == '0':
            feats["zero_features"].append(i)

    return feats



def cpuid_update(cpuid : str, new_feat : str, prev_test : bool) -> str:
    
    if(prev_test) :
        cpuid = cpuid[:-1] + "," + new_feat + cpuid[-1]
    else:
        cpuid = cpuid.split(',')
        #print(cpuid)
        if len(cpuid) > 1:
            cpuid.pop()
            cpuid.append("\"")
        str = ""
        cpuid = str.join(cpuid)
        cpuid = cpuid[:-1] + "," + new_feat + cpuid[-1]

    return cpuid



def get_cpuid_param(file : str) -> str :

    with open(file, 'r') as f:
        return f.readlines()[-1]



def features_test(vm_conf_file : str, cpuid : str, new_feat : str, prev_test : bool):

    with open(vm_conf_file, 'r+') as f: 
        content = f.read()
        f.seek(2) 
        content = content.replace(cpuid, cpuid_update(cpuid, new_feat, prev_test))
        f.write(content)
        f.truncate()



def remove_tested_feature(feature_file : str, feature : str) :

    with open(feature_file, 'r+') as f: 
        content = f.read()
        f.seek(0) 
        content = content.replace(feature, "")
        f.write(content)
        f.truncate()



def check_success(res_file : str) -> bool:

    with open(res_file, 'r') as f: 
        return f.readlines()[-2] == ' All 192 tests passed.\n'



def check_launch(launch_log : str) -> bool:
    with open(launch_log, 'r') as f:
        return f.readlines()[-1] == 'Ubuntu 18.04 LTS myvm hvc0\n' or f.readlines()[-1] == 'Ubuntu 18.04 LTS myvm hvc0'




if __name__ == "__main__" :

    import os

    file = open("../cpuid_bits.txt", "r")
    file.readline()
    ECX = file.readline()
    EDX = file.readline()
    file.close()


    edx_feats = {
        "fpu" : 1, 
        "vme" : 1,
        "de" : 1,
        "pse" : 1,
        "tsc" : 1,
        "msr" : 1,
        "pae" : 1,
        "mce" : 1,
        "cmpxchg8" : 1,
        "apic" : 1,
        "reserved10" : 1,
        "sysenter" : 1,
        "mtrr" : 1,
        "pge" : 1,
        "mca" : 1,
        "cmov" : 1,
        "pat" : 1,
        "pse36" : 1,
        "psn" : 1,
        "clfsh" : 1,
        "reserved20" : 1,
        "ds" : 1,
        "acpi" : 1,
        "mmx" : 1,
        "fxsr" : 1,
        "sse" : 1,
        "sse2" : 1,
        "ss" : 1,
        "htt" : 1,
        "tm" : 1,
        "ia64" : 1,
        "pbe" : 1,
    }


    ecx_feats = {
        "sse3" : 1,
        "pclmulqdq" : 1,
        "dtes64" : 1,
        "monitor" : 1,
        "dscpl" : 1,
        "vmx" : 1,
        "smx" : 1,
        "est" : 1,
        "tm2" : 1,
        "ssse3" : 1,
        "cnxtid" : 1,
        "sdbg" : 1,
        "fma" : 1,
        "cmpxchg16" : 1,
        "xtpr" : 1,
        "pdcm" : 1,
        "reserved16" : 1,
        "pcid" : 1,
        "dca" : 1,
        "sse4.1" : 1,
        "sse4.2" : 1,
        "x2apic" : 1,
        "movbe" : 1,
        "popcnt" : 1,
        "tsc-deadline" : 1,
        "aes" : 1,
        "xsave" : 1,
        "osxsave" : 1,
        "avx" : 1,
        "f16c" : 1,
        "rdrand" : 1,
        "hypervisor" : 1,
    }


    i = 0
    for j in edx_feats.keys():
        edx_feats[j] = EDX[i]
        i += 1

    i = 0
    for j in ecx_feats.keys():
        ecx_feats[j] = ECX[i]
        i += 1


    file = open("../test_cpuid_bits.txt", "r")
    file.readline()
    ecx = file.readline()
    edx = file.readline()
    file.close()      



    # zero features
    dep_feats = {}
    zero_features(dep_feats, ecx_feats)
    zero_features(dep_feats, edx_feats)

    for feat in dep_feats["zero_features"] :
        remove_tested_feature("features.txt", feat)



    with open("features.txt") as f:
        content = f.read()
        f.seek(0) 
        content = content.split()
        


        test = check_success("../check_result.txt")
        cpuid = get_cpuid_param("/etc/xen/myvm.cfg")
        features_test("/etc/xen/myvm.cfg", cpuid, content[0], test)

        os.system("xl create -c myvm.cfg > /etc/xen/vm_launcher_log.txt")
        launched = check_launch("/etc/xen/myvm.cfg")
         
        if not launched:
            remove_tested_feature("feature.txt", content[0])

        os.system("scp ./script/test-run.sh popo@ip:~")
        os.system("ssh popo@ip")
        os.system("chmod +x ./test-run.sh && bash ./test-run.sh")

        #os.system("chmod +x ./script/test-run.sh && bash ./script/test-run.sh")
        #os.system("shutdown -h now")

