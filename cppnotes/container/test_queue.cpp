#include "./queue.hpp"
#include <iostream>
using namespace std;

int main() {
    Queue<int> q = Queue<int>(10);

    int val1 = 2, val2 = 4;
    q.push(val1);
    q.push(val2);

    int size = q.size();
    int *p = q.vals();
    cout<<"Length is "<<size<<endl;

    cout<<"Pop elements..."<<endl;
    for (int i =0; i<size; i++){
        cout<<q.pop()<<endl;
    }

    return 0;
}