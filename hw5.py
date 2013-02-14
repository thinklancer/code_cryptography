'''
Your goal this week is to write a program to compute discrete log modulo a prime p. Let g be some element in Z*p and suppose you are given h in Z*p such that h=gx where 1<=x<=2^40. Your goal is to find x. More precisely, the input to your program is p,g,h and the output is x.

The trivial algorithm for this problem is to try all 2^40 possible values of x until the correct one is found, that is until we find an x satisfying h=gx in Zp. This requires 2^40 multiplications. In this project you will implement an algorithm that runs in time roughly sqrt(2^40)=2^20 using a meet in the middle attack. 

Let B=2^20. Since x is less than B^2 we can write the unknown x base B as x=x0B+x1 where x0,x1 are in the range [0,B-1]. Then
    
    h=gx=g^(x0 B+x1)=(g^B)^x0 * g^x1   in Zp.

    By moving the term gx1 to the other side we obtain

          h/g^x1=(g^B)^x0      in Zp.

    The variables in this equation are x0,x1 and everything else is known: you are given g,h and B=220. Since the variables x0 and x1 are now on different sides of the equation we can find a solution using meet in the middle (Lecture 3.3):
    First build a hash table of all possible values of the left hand side h/gx1 for x1=0,1,...,2^20.
    Then for each value x0=0,1,2,...,2^20 check if the right hand side (g^B)^x0 is in this hash table. If so, then you have found a solution (x0,x1) from which you can compute the required x as x=x0B+x1.
    The overall work is about 2^20 multiplications to build the table and another 2^20 lookups in this table.

    Now that we have an algorithm, here is the problem to solve:


    Each of these three numbers is about 153 digits. Find x such that h=gx in Zp.

    To solve this assignment it is best to use an environment that supports multi-precision and modular arithmetic. In Python you could use the gmpy2 or numbthy modules. Both can be used for modular inversion and exponentiation. In C you can use GMP. In Java use a BigInteger class which can perform mod, modPow and modInverse operations.
'''
import pickle
from numbthy import *

p=13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171

g= 11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568

h=3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333

if __name__ == "__main__":
    
    print len(str(p)),len(str(g)),len(str(h))
    print "calculate 2^20 array"
    lhs = [powmod(2,i,p) for i in range(2**20)]
    with open("temp.red","w") as f:
        pickle.dump(lhs,f)
    f.close()
    print "calculate 1/2^20 array"
    lhs = [xgcd(i,p)[1] for i in lhs]
    with open("temp.red","w") as f:
        pickle.dump(lhs,f)
    f.close()
    print "calculate LHS"
    lhs = [h*i%p for i in lhs]
    with open('temp.red','w') as f:
        pickle.dump(lhs,f)
        #lhs=pickle.load(f)
    f.close()
    gb = powmod(g,2**20,p)
    print "start searching ..."
    for i in range(2**20):
        if i % 2**12 == 0:
            print "  finish ",i/2**12,"/256 steps"
        rhs = powmod(gb,i,p)
        if rhs in lhs:
            x1=lhs.index(rhs)
            x0=i
            print x0,x1,x0*2**20+x1
            break
            
