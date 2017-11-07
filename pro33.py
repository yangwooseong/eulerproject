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

for a in range(1,10):
    for c in range(a+1):
        for b in range(1,10):
            g = gcd(10*a+b,10*b+c)
            if b != c and (10*b+c)*a == (10*a+b)*c:
                print(a,b,c)

den = 1
num = 1

for a in range(1,10):
    for c in range(1,10):
        for b in range(c,10):
            if b != a and (10*c+a)*b == (10*a+b)*c:
                print(a,b,c)
                den = den*b
                num = num*c

print(den,num,den/(gcd(den,num)))
                
