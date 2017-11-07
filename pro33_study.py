# pandigital products

from __future__ import print_function

def gcd(a,b):
    # a >= b
    if a < b:
        temp = b
        b = a
        a = temp
    if a % b == 0:
        return b
    else:
        return gcd(b,a % b)

den = 1
num = 1

for a in range(1,10):
    for c in range(a+1,10):
        q,r = divmod(9*a*c,10*a-c)
        if r == 0 and q <= 9:
            num *= a
            den *= c

print(den,num,den/(gcd(den,num)))
                
