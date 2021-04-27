#ifndef __GC
#define __GC

#include <iostream>
#include <cstring>
using namespace std;

template <typename T>
class Pointer {
    public:
        T val;
        Pointer<T>* next;

        Pointer() {};
        ~Pointer() {
            cout<<"Release Pointer with val as: "<<val<<endl;
        };
};

template class Pointer<int>;
template class Pointer<double>;
template class Pointer<char*>;

class GC {
    private:
        Pointer<int>* _intpointer;
        Pointer<double>* _doublepointer;
        Pointer<char*>* _charpointer;
    public:
        GC();
        ~GC();

        int* IntPointer(int val);
        //int* IntPointer(int* p);
        double* DoublePointer(double val);
        //double* DoublePointer(double* p);
        char* CharPointer(const char* val);
};

#endif