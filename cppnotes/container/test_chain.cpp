#include "./chain.hpp"
#include <iostream>
using namespace std;

int main() {
    Chain<int> chain = Chain<int>();
    for (int i = 11; i<=20; i++){
        chain.push(i);
    }
    cout<<"Total length: "<<chain.length()<<endl;
    chain.print();

    cout<<"Set value ---------"<<endl;
    chain.setval(3, 999999);
    chain.print();

    cout<<"Insert value ---------"<<endl;
    chain.insert(5, 888);
    chain.print();

    cout<<"Remove value ---------"<<endl;
    chain.remove(5);
    chain.print();
    
    return 0;
}