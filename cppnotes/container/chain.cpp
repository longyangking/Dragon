#include "./chain.hpp"
#include <iostream>
using namespace std;

template <typename T>
Node<T>::Node(T val, Node<T>* next) {
    _val = val;
    _next = next;
}

template <typename T>
Node<T>::~Node() {
    //cout<<"Release node: ["<<_val<<"]"<<endl;
    delete _next;
}

template <typename T>
Chain<T>::Chain() {
    _root = NULL;
}

template <typename T>
Chain<T>::~Chain() {
    int length = this->length();
    Node<T> *p = _root;
    Node<T> **list = new Node<T>*[length];
    for (int i=0; i<length; i++){
        list[i] = p;
        p = p->next();
    }
    delete [] list;
}

template <typename T>
void Chain<T>::push(T val) {
    Node<T>* p = new Node<T>(val, _root);
    _root = p;
}

template <typename T>
T Chain<T>::pop() {
    Node<T>* root = _root->next();
    T val = _root->val();
    delete _root;
    _root = root;
    return val;
}

template <typename T>
int Chain<T>::length() {
    int len = 0;
    Node<T>* p = _root;
    while (p) {
        len++;
        p = p->next();
    }
    return len;
}

template <typename T>
void Chain<T>::insert(int index, T val){
    int length = this->length();
    int indexr = length - index;
    Node<T> *p = _root, *pn;
    while (indexr > 0) {
        indexr--;
        p = p->next();
    }
    pn = p->next();
    Node<T>* node = new Node<T>(val, pn);
    p->setnext(node);
}

template <typename T>
void Chain<T>::remove(int index) {
    int length = this->length();
    int indexr = length - index - 1;
    Node<T> *p = _root, *pn;
    while (indexr > 0) {
        indexr--;
        p = p->next();
    }
    pn = p->next();
    p->setnext(pn->next());
}

template <typename T>
void Chain<T>::setval(int index, T val) {
    int length = this->length();
    int indexr = length - index - 1;
    Node<T> *p = _root, *pn;
    while (indexr > 0) {
        indexr--;
        p = p->next();
    }
    pn = p->next();
    pn->setval(val);
}

template <typename T>
void Chain<T>::print() {
    Node<T>* p = _root;
    int index = 0, length = this->length();
    while (p != NULL) {
        index++;
        cout<<(length-index+1)<<": ["<<p->val()<<"]"<<endl;
        p = p->next();
    }
}

template class Node<int>;
template class Node<double>;
template class Chain<int>;
template class Chain<double>;