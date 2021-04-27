#include "./gc.hpp"
#include <iostream>
using namespace std;

int main() {
    GC gc = GC();
    //Pointer<int>* p = new Pointer<int>();
    int* p = gc.IntPointer(10);
    double *pd = gc.DoublePointer(1.234);
    double *pd2 = gc.DoublePointer(524.423);
    char* pc = gc.CharPointer("Hello GC!");

    cout<<"Int value: "<<*p<<endl;
    cout<<"Double value: "<<*pd<<endl;
    cout<<"Char value: "<<pc<<endl;

    return 0;
}