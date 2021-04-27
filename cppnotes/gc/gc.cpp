#include "./gc.hpp"

GC::GC() {
    _intpointer = NULL;
    _doublepointer = NULL;
    _charpointer = NULL;
}

GC::~GC() {
    cout<<"Starting to release the Pointers in GC..."<<endl;
    Pointer<int>* p;
    while (_intpointer) {
        p = _intpointer->next;
        delete _intpointer;
        _intpointer = p;
    }
    
    Pointer<double>* pd;
    while (_doublepointer) {
        pd = _doublepointer->next;
        delete _doublepointer;
        _doublepointer = pd;
    }
    Pointer<char*>* pc;
    while (_charpointer) {
        pc = _charpointer->next;
        delete _charpointer;
        _charpointer = pc;
    }
}

int* GC::IntPointer(int val) {
    int *p = new int(val);
    Pointer<int>* pointer = new Pointer<int>();
    pointer->val = val;
    pointer->next = _intpointer; 
    _intpointer = pointer;

    return p;
}

double* GC::DoublePointer(double val) {
    double *p = new double(val);
    Pointer<double>* pointer = new Pointer<double>();
    pointer->val = val;
    pointer->next = _doublepointer; 
    _doublepointer = pointer;

    return p;
}

char* GC::CharPointer(const char* val) {
    char *p = new char(100);
    strcpy(p, val);
    Pointer<char*>* pointer = new Pointer<char*>();
    pointer->val = p;
    pointer->next = _charpointer; 
    _charpointer = pointer;

    return p;
}