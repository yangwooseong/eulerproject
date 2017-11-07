# Prime permutations

from __future__ import print_function
import itertools

def primeUnder(n):
    sieve = [True]*n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i] = [False] * (len(sieve[i*i::2*i]))
    return [p for p in xrange(3,n,2) if sieve[p] and p >= 1000]

primes = primeUnder(100000)

for p in primes:
    per = set(int(''.join(i)) for i in itertools.permutations(str(p)))
    per = [i for i in per if i in primes and i > p]
    per.sort()
    if len(per) >= 2:
        #print(p,per)
        for j in per:
            if j+j-p in per:
                print(p,j,j+j-p)
