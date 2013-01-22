'''
In this project you will implement two encryption/decryption systems, one using AES in CBC mode and another using AES in counter mode (CTR). In both cases the 16-byte encryption IV is chosen at random and is prepended to the ciphertext. For CBC encryption we use the PKCS5 padding scheme discussed in class (13:50). 

While we ask that you implement both encryption and decryption, we will only test the decryption function. In the following questions you are given an AES key and a ciphertext (both are hex encoded) and your goal is to recover the plaintext and enter it in the input boxes provided below. 

For an implementation of AES you may use an existing crypto library such as PyCrypto (Python), Crypto++ (C++), or any other. While it is fine to use the built-in AES functions, we ask that as a learning experience you implement CBC and CTR modes yourself. 
'''

from Crypto.Cipher import AES
from Crypto.Util import Counter

import sys
# CBC
def qs1():
    key = '140b41b22a29beb4061bda66b6747e14'
    ciphertext='4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'
    vi=ciphertext[0:16]
    #'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x001'
    obj = AES.new(key,AES.MODE_CBC,vi)
    print obj.decrypt(ciphertext)
    return 0

def qs2():
    return 0

# CTR
def qs3():
    key = '36f18357be4dbd77f050515c73fcf9f2'
    ciphertext='69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329'
    ctr = Counter.new(128)
    obj = AES.new(key,AES.MODE_CTR,counter=ctr)
    print obj.decrypt(ciphertext)
    return len(key)


def qs4():
    return 0

if __name__=="__main__":
    if sys.argv[1] == '1':
        print qs1()
    if sys.argv[1] == '2':
        print qs2()
    if sys.argv[1] == '3':
        print qs3()
    if sys.argv[1] == '4':
        print qs4()
    
