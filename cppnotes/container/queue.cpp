#include "./queue.hpp"
#include <math.h>

template <typename T>
Queue<T>::Queue(int length) {
    _list = new T[length];
    _length = length;
    _size = 0;
}

template <typename T>
Queue<T>::~Queue() {
    delete []_list;
}

template <typename T>
T Queue<T>::pop() {

    // TODO Exception when no element in the Queue 

    T t = _list[0];
    for (int i = 0; i<_size-1; i++){
        _list[i] = _list[i+1];
    }
    //delete (_list + _size - 1);
    _size --;
    return t;
}

template <typename T>
void Queue<T>::push(T t) {
    if (_size < _length) {
        _list[_size]= t;
        _size ++;
    } else {
        for(int i = 0; i<_length-1; i++){
            _list[i] = _list[i+1];
        }
        _list[_length-1] = t;
    }
}

template <typename T>
T* Queue<T>::vals() {
    return _list;
}

template class Queue<int>;
template class Queue<double>;