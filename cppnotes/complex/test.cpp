#include "complex.hpp"
#include <iostream>
using namespace std;

int main(){
    Complex z1 = Complex(1.0, 1.0);
    Complex z2 = Complex(1.0, 1.0);

    cout<<"Z1 is "<<z1.real() <<"+"<<z1.imag()<<"i"<<endl;
    cout<<"The abs as: "<<z1.abs()<<endl;
    cout<<"The phase as: "<<z1.angle()<<endl;

    cout<<"Z2 is "<<z2.real() <<"+"<<z2.imag()<<"i"<<endl;

    Complex z3;
    z3 = z1 + z2;
    cout<<"Z1 + Z2 = "<<z3.real() <<"+"<<z3.imag()<<"i"<<endl;

    z3 = z1 - z2;
    cout<<"Z1 - Z2 = "<<z3.real() <<"+"<<z3.imag()<<"i"<<endl;

    z3 = z1 * z2;
    cout<<"Z1 * Z2 = "<<z3.real() <<"+"<<z3.imag()<<"i"<<endl;

    z3 = z1 / z2;
    cout<<"Z1 / Z2 = "<<z3.real() <<"+"<<z3.imag()<<"i"<<endl;
    return 0;
}