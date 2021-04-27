import numpy as np

class Encryptor:
    def __init__(self, verbose=False):
        self.verbose = verbose

    def MD5(self, s):
        data = str(s)
        n_char = int(512/8) # 64 word
        n_0 = int(448/8) # 56 word
        n_data = len(data)
        n_N = int(n_data/n_char)
        n_R = n_data%n_char

        data_list = list()
        _data = list()
        for i in range(n_data):
            _data.append(data[i])
            if (i+1)%n_char == 0:
                data_list.append(_data)
                _data = list()

        if n_R == 0:
            _data = [" " for _ in range(n_char)]
            data_list.append(_data)
        elif n_R < n_0:
            for i in range(n_0-n_R):
                _data.append(" ")
            data_list.append(_data)
        else:
            for i in range(n_char-n_R):
                _data.append(" ")
            data_list.append(_data)

        if self.verbose:
            print("Preprocessed data:")
            print(data_list)

        A = 0x67452301
        B = 0xefcdab89
        C = 0x98badcfe
        D = 0x10325476

        def F(x,y,z):
            return (x & y)|((~x) & z)

        def G(x,y,z):
            return (x & y)|(y & (~z))

        def H(x,y,z):
            return (x ^ y ^ z)

        def I(x,y,z):
            return y ^ (x | (~z))

        # def ti(i):
        #     return int(4294967296*np.abs(np.sin(i)))
        
        def FF(a,b,c,d,Mj,s,ti):
            