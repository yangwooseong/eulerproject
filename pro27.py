from __future__ import print_function
import math

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True

def primeUnderN(n):
    sieve = [True]*n
    lists = [2]
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i] = [False] * (len(sieve[i*i::2*i]))
    return [2] + [p for p in xrange(3,n,2) if sieve[p]]

def quadratic(n,a,b):
    return (n*n + a*n + b)

mx = 0
for b in primeUnderN(1001):
    # a should be odd and |a| < b when n = 1
    for a in range(-b+2,b,2):
        n = 0 
        while is_prime(quadratic(n,a,b)):
            n += 1
            #print(n,a)
        if mx < n:
            mx = n
            mxa = a
            mxb = b

print (mx,mxa,mxb,mxa*mxb)
