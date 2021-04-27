#ifndef __Tree
#define __Tree

template <typename T>
class Node {
    private:
        T _val;
        Node<T>* _left;
        Node<T>* _right;
    public:
        Node(T val, Node<T>* left, Node<T>* right);
        ~Node();

        T getval() {return _val; };
        void setval(T val) {_val = val; };
        Node<T>* getleft() {return _left; };
        Node<T>* getright() {return _right; };
        void setleft(Node<T>* left) {_left = left; };
        void setright(Node<T>* right) {_right = right; };
};

template <typename T>
class Tree {
    private:
        Node<T>* _root;
    public:
        Tree();
        ~Tree();

        Node<T>* getroot() {return _root; };
        void addnode(Node<T>* node);
        void invert();
};

#endif