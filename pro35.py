from __future__ import print_function

def primeUnderN(n):
    sieve = [True]*n
    lists = [2]
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i] = [False] * (len(sieve[i*i::2*i]))
    return [2] + [p for p in xrange(3,n,2) if sieve[p]]

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(number*0.5 )+ 1, 2):
            if number % current == 0: 
                return False
        return True

def cycle(n):
    s = str(n)
    for i in range(len(s)):
        yield int(s[i:] + s[:i])

N = 1000000
primes = primeUnderN(N)
cycledprimes = set()

for i in primes:
    found = True
    if i == 2:
        cycledprimes.add(i)
    elif i!=2 and all (s in list('13579') for s in str(i)):
        if i not in cycledprimes:
            for j in cycle(i):
                if j not in primes:
                    found = False
                    break
            if found:
                for j in cycle(i):
                    cycledprimes.add(j)

print(len(cycledprimes))
