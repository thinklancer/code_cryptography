a1=["2d1cfa42","c0b1d266"]
a2=["eea6e3dd","b2146dd0"]
b1=["e86d2de2","e1387ae9"]
b2=["1792d21d","b645c008"]
c1=["9d1a4f78","cb28d863"]
c2=["75e5e3ea","773ec3e6"]
d1=["7c2822eb","fdc48bfb"]
d2=["325032a9","c5e2364b"]


def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def test(a,b):
    return strxor(a.decode('hex'),b.decode('hex'))