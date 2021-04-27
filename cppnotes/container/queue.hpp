#ifndef __Queue
#define __Queue

template <typename T>
class Queue {
    private:
        int _length;
        int _size;
        T* _list;
    public:
        Queue(int length = 10);
        ~Queue();

        int size() {return _size; };
        int length() {return _length; };
        T pop();
        void push(T t);

        T* vals();
};

#endif