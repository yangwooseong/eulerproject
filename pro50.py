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
        for current in range(3, int(number**0.5) + 1, 2):
            if number % current == 0: 
                return False
        return True
    return False


N = 10**6

primes = primeUnderN(N)
sm = 0
mx = 0
minimum = 21

j = 0
for i in range(len(primes)):
    if sum(primes[i:i+minimum+mx]) >= N:
        #print(primes[i:i+minimum+mx])
        break
    else:
        while sum(primes[i:i+minimum+j]) < N:
            if is_prime(sum(primes[i:i+minimum+j])):
                consecutive = j
                #print(i,minimum+consecutive,primes[i:i+minimum+j])
            j += 1
        j = consecutive
        if mx < consecutive:
            mx = consecutive
            start = i

print(primes[start],primes[start+mx+minimum])
print(sum(primes[start:start+mx+minimum]))

