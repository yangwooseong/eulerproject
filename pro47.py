# distinct primes factors

from __future__ import print_function

def primefactors(n):
    p = 2
    factors = set()
    while n % p == 0:
        n /= p
        factors.add(p)
    p = 3
    while n != 1:
        while n % p == 0:
            factors.add(p)
            n /= p
        p += 2
    return factors

N = 4
i = N

found = False

while True:
    if len(primefactors(i)) != N:
        i += N
        found = False
        continue
    else:
        found = True
        for j in range(1,N):
            if len(primefactors(i-j)) != N:
                found = False
                i = i-j+N
                continue
        if found:
            print(i-N+1)
            break
