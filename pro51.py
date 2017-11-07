# Prime digit replacements

from __future__ import print_function
import sys

# return primes in [10**(N-1),10**N)
def primeUnder(N):
    n = 10 ** N
    sieve = [True]*n
    lists = [2]
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i] = [False] * (len(sieve[i*i::2*i]))
    return [p for p in xrange(3,n,2) if sieve[p] and p >= 10**(N-1)]

# more effective version of sameDigits ?
def sameDigits(n):
    n = str(n)
    k = 0
    family = []
    appended = []
    for i in range(len(n)):
        if i not in appended:
            if n[i] in n[i+1:]:
                family.append([i])
                for j in range(i+1,len(n)):
                    if n[i] == n[j]:
                        family[k].append(j)
                        appended.append(j)
                k += 1
    return family

def replace(n,digits):
    n = list(str(n))
    family = []
    for i in range(10):
        if i == 0 and 0 in digits:
            continue
        for digit in digits:
            n[digit] = str(i)
        if is_prime(int(''.join(n))):
            family.append(int(''.join(n)))
    return family

# primes in [10**5, 10**6)
primes = primeUnder(6)

# eliminate primes with distinct digits
for prime in primes:
    if len(str(prime)) == len(set(str(prime))):
        primes.remove(prime)

checked = []

for prime in primes:
    if prime not in checked:
        digitsGroup = sameDigits(prime)
        for group in digitsGroup:
            family = replace(prime,group)
            for i in family:
                checked.append(i)
            if len(family) == 8:
                print(family,prime)
                sys.exit()
           
