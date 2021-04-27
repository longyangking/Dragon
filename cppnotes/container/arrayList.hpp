#ifndef __Array_List
#define __Array_List

template<typename T>
class ArrayList {
    private:
        T* _vals;
        int _length;
        int _size;
    public:
        ArrayList(int length = 10);
        ~ArrayList();
};

#endif