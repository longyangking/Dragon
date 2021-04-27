#include "./encrypt.hpp"

const unsigned int A = 0x67452301;
const unsigned int B = 0xEFCDAB89;
const unsigned int C = 0x98BADCFE;
const unsigned int D = 0x10325476;

#define F(x,y,z) (((x) & (y)) | ((~x) & (z)))
#define G(x,y,z) (((x) & (z)) | ((y) & (~z)))
#define H(x,y,z) ((x) ^ (y) ^ (z))
#define I(x,y,z) ((y) ^ ((x) | (~z)))

#define ROTATE_LEFT(x,n)  (((x) << (n)) | ((x) >> (32 - (n))))