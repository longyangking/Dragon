#ifndef __Complex
#define __Complex

class Complex {
    private:
        double _real;
        double _imag;
    public:
        Complex() {};
        Complex(double real, double imag);
        ~Complex() {};

        double real() { return _real; };
        double imag() { return _imag; };
        double abs();
        double angle();

        Complex operator + (Complex z);
        Complex operator - (Complex z); 
        Complex operator * (Complex z);
        Complex operator / (Complex z);
};

#endif