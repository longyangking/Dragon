#ifndef __Encrypt
#define __Encrypt

class Encryptor {
    private:
        char* __vals;
    public:
        char* MD5(char* content);
        char* SHA1(char* content); 
        char* SHA256(char* content);
        char* SHA512(char* content);
        char* AES(char* content);
        char* DES(char* content);
        char* Base64(char* content);
};

#endif