from __future__ import print_function

def sumofPrimeUnderN(n):
    s = 0
    primes = []
    if n >= 2:
        s = s + 2
        primes.append(2)
    for p in xrange(3,n+1,2):
           r = 3
           if p == 3:
               s +=3
               primes.append(p)
           while r*r <= p:
               if p % r == 0:
                   break
               r += 2
           if p % r == 0:
               continue 
           primes.append(p)
           s += p
    return s

print (sumofPrimeUnderN(2000000))


