#ifndef __Decrypt
#define __Decrypt

class Decryptor {
    private:
        char* __vals;
    public:
        char* AES(char* content);
        char* DES(char* content);
        char* Base64(char* content);
};

#endif