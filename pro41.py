# pandigital prime

from __future__ import print_function

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(number**0.5) + 1, 2):
            if number % current == 0: 
                return False
        return True
    return False

def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number -= 2

def primeUnderN(n):
    sieve = [True]*n
    lists = [2]
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i] = [False] * (len(sieve[i*i::2*i]))
    return [2] + [p for p in xrange(3,n,2) if sieve[p]]

def ispandigital(n):
    d = len(str(n))
    return all(i in str(n) for i in map(str,range(1,d+1)))

N = 7654321
for i in get_primes(N):
    if ispandigital(i):
        print(i)
        break
