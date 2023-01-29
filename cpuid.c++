#include <bits/stdc++.h>
#include <fstream>

using namespace std;

int main(int argc, char const *argv[])
{
    int32_t eax, ebx, ecx, edx;

    __asm__ __volatile__("mov $0x2, %eax\n\t");

    __asm__ __volatile__("cpuid \n\t");
    __asm__ __volatile__("mov %%eax, %0\n\t":"=r" (eax));
    __asm__ __volatile__("mov %%ebx, %0\n\t":"=r" (ebx));
    __asm__ __volatile__("mov %%ecx, %0\n\t":"=r" (ecx));
    __asm__ __volatile__("mov %%edx, %0\n\t":"=r" (edx));


    string myText;
    ifstream MyReadFile("cpuid_bits.txt");
    getline (MyReadFile, myText);

    if (myText.compare("No modification") != 0){
        ofstream file("cpuid_bits.txt");
        file << "No modification" << endl;
        file << bitset<32>(ecx).to_string() << endl;
        file << bitset<32>(edx).to_string() << endl;
        file.close();
    }
    else{
        ofstream file("test_cpuid_bits.txt");
        file << "Test modification" << endl;
        file << bitset<32>(ecx).to_string() << endl;
        file << bitset<32>(edx).to_string() << endl;
        file.close();
    }
            
        
    
    MyReadFile.close(); 

    // cout << bitset<32>(ecx).to_string() << endl;
    // cout << bitset<32>(edx).to_string() << endl;

    return 0;
}
