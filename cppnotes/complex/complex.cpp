#include "complex.hpp"
#include <math.h>

Complex::Complex(double real, double imag) {
    _real = real;
    _imag = imag;
}

double Complex::abs() {
    double val = sqrt(_real*_real + _imag*_imag);
    return val;
}

double Complex::angle() {
    double val = atan2(_imag, _real);
    return val;
}

Complex Complex::operator+ (Complex z) {
    Complex znew = Complex(_real + z.real(), _imag + z.imag());
    return znew;
}

Complex Complex::operator- (Complex z) {
    Complex znew = Complex(_real - z.real(), _imag - z.imag());
    return znew;
}

Complex Complex::operator* (Complex z){
    double real = _real*z.real() - _imag*z.imag();
    double imag = _real*z.imag() + _imag*z.real();
    Complex znew = Complex(real, imag);
    return znew;
}

Complex Complex::operator/ (Complex z){
    double a = _real, b = _imag;
    double c = z.real(), d = z.imag();

    // TODO Exception for the division by Zero

    double real = (a*c + b*d)/(c*c + d*d);
    double imag = (b*c - a*d)/(c*c + d*d);
    Complex znew = Complex(real, imag);
    return znew;
}