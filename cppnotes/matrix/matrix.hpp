#ifndef __Matrix
#define __Matrix

template <typename T>
class Vector {
    private:
        T* _vals;
        int _n;
    public:
        Vector(int n);
        Vector(int n, T* vals);
        ~Vector();

        Vector operator * (Vector vector);
        Vector operator * (Matrix mat);
        Vector operator - (Vector vector);
        Vector operator + (Vector vector);
        Vector transpose();
        Vector conjugate();
        
        Vector norm();
};

template <typename T>
class Matrix {
    private:
        T** _vals;
        int _m, _n;
    public:
        Matrix(int m, int n);
        Matrix(int m, int n, T** vals);
        ~Matrix();

        Matrix operator * (Matrix mat);
        Matrix operator * (Vector vector);
        Matrix operator + (Matrix mat);
        Matrix operator - (Matrix mat);
        Matrix inverse();
        Matrix transpose();
        Matrix conjugate();
        T trace();
        T det();
        Matrix power(double n);
        Matrix eig();
};

#endif