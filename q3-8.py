from Crypto.Cipher import AES

def AES_encrypt(k, pt):
    encryptor = AES.new(k.decode('hex'), AES.MODE_ECB)
    ct = encryptor.encrypt(pt.decode('hex'))
    return ct.encode('hex')

def AES_decrypt(k, ct):
    encryptor = AES.new(k.decode('hex'), AES.MODE_ECB)
    pt = encryptor.decrypt(ct.decode('hex'))
    return pt.encode('hex')

def f1(x, y):
    ct = AES_encrypt(y, x)
    ct = ct.decode('hex')
    y = y.decode('hex')
    f1 = map(lambda v:"%02.0x" % (ord(v[0])^ord(v[1])), zip(ct, y))
    return "".join(f1)

def f2(x, y):
    ct = AES_encrypt(x, x)
    ct = ct.decode('hex')
    y = y.decode('hex')
    f2 = map(lambda v:"%02.0x" % (ord(v[0])^ord(v[1])), zip(ct, y))
    return "".join(f2)

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])


x1 = '00000000000000000000000000000000'
y1 = 'ffffffffffffffffffffffffffffffff'
y2 = 'cccccccccccccccccccccccccccccccc'
temp =  strxor(strxor(AES_encrypt(y1,x1).decode('hex'),y1.decode('hex')),y2.decode('hex'))
x2 = AES_decrypt(y2,temp.encode('hex'))
print x2

x3 = '00000000000000000000000000000000'
y3 = 'ffffffffffffffffffffffffffffffff'
x4 = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
temp = strxor(f2(x3,y3).decode('hex'),AES_encrypt(x4,x4).decode('hex'))
y4 = temp.encode('hex')
print y4


print f1(x1, y1) == f1(x2, y2)
print f2(x3, y3) == f2(x4, y4)
