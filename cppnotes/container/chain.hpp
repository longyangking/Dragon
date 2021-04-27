#ifndef __Chain
#define __Chain

template <typename T>
class Node {
    private:
        T _val;
        Node<T>* _next;
    public:
        Node(T val, Node<T>* next);
        ~Node();

        void setval(T val) { _val = val; };
        void setnext(Node<T>* p) { _next = p; };
        T val() { return _val; };
        Node<T>* next() { return _next; };        
};

template <typename T>
class Chain {
    private:
        Node<T> * _root;
    public:
        Chain();
        ~Chain();

        void push(T val);
        T pop();
        int length();
        void insert(int index, T val);
        void remove(int index);
        void setval(int index, T val);
        void print();
};

#endif