from __future__ import print_function

import math,time

n = 3
primes = []

while True:
    if all(n % p for p in primes):
        primes.append(n)
    elif not any(n-2*i*i in primes for i in range(1,n)):
        print(n)
        break
    n += 2
    
