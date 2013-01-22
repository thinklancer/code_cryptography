'''
In this project you will implement two encryption/decryption systems, one using AES in CBC mode and another using AES in counter mode (CTR). In both cases the 16-byte encryption IV is chosen at random and is prepended to the ciphertext. For CBC encryption we use the PKCS5 padding scheme discussed in class (13:50). 

While we ask that you implement both encryption and decryption, we will only test the decryption function. In the following questions you are given an AES key and a ciphertext (both are hex encoded) and your goal is to recover the plaintext and enter it in the input boxes provided below. 

For an implementation of AES you may use an existing crypto library such as PyCrypto (Python), Crypto++ (C++), or any other. While it is fine to use the built-in AES functions, we ask that as a learning experience you implement CBC and CTR modes yourself. 
'''

from Crypto.Cipher import AES
from Crypto.Util import Counter

class AEScount:
    def __call__(self):
        return self
    def new(vi):
        return

import sys
# CBC
def qs1(ciphertext):
    key = '140b41b22a29beb4061bda66b6747e14'.decode('hex')
    vi=ciphertext.decode('hex')[:16]
    #'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x001'
    obj = AES.new(key,AES.MODE_CBC,vi)
    return obj.decrypt(ciphertext.decode('hex'))[16:]


# CTR
def qs3(ciphertext):
    key = '36f18357be4dbd77f050515c73fcf9f2'.decode('hex')
    vi = ciphertext.decode('hex')[:16]
    ctr = Counter.new(128,initial_value=long(vi.encode('hex'),16))
    obj = AES.new(key,AES.MODE_CTR,counter=ctr)
    return obj.decrypt(ciphertext.decode('hex')[16:])

if __name__=="__main__":
    if sys.argv[1] == '1':
        print qs1('4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81')
    if sys.argv[1] == '2':
        print qs1('5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253')
    if sys.argv[1] == '3':
        print qs3('69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329')
    if sys.argv[1] == '4':
        print qs3('770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451')
    
