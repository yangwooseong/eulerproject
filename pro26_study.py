from __future__ import print_function
import math

def primeUnder(n):
    sieve = [True]*n
    lists = [2]
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i] = [False] * (len(sieve[i*i::2*i]))
    return [2] + [p for p in xrange(3,n,2) if sieve[p]]

primes = primeUnder(1000)
for p in primes[::-1]:
    i = 2
    while pow(10,i-1,p) != 1:
        # way faster than pow(10,i-1) % p != 1
        i += 1
    if i == p:
        print('when d is %s,period is %s' %(i,i-1))
        break
