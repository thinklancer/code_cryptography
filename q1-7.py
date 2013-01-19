''' 
Suppose you are told that the one time pad encryption of the message "attack at dawn" is 09e1c5f70a65ac519458e7e53f36 (the plaintext letters are encoded as 8-bit ASCII and the given ciphertext is written in hex). What would be the one time pad encryption of the message "attack at dusk" under the same OTP key?
'''

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])


origin1="attack at dawn"
cipher1="09e1c5f70a65ac519458e7e53f36"
origin2="attack at dusk"

ciphered1 = cipher1.decode('hex')
key = strxor(origin1,ciphered1)
ciphered2 = strxor(origin2,key)
print ciphered2.encode('hex')