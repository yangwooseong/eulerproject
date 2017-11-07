# Truncatable primes

from __future__ import print_function
from math import log10

def is_prime(num):
    number = int(num)
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(number**0.5)+1, 2):
            if number % current == 0: 
                return False
        return True
    return False

def truncatable(n):
    for i in range(1,len(str(n))):
        if not is_prime(str(n)[i:]) or not is_prime(str(n)[:i]):
            return False
    return True

def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 2

s = 0
sm = 0
for i in get_primes(13):
    if truncatable(i):
        print(i)
        s += 1
        sm += i
    if s == 11:
        print(sm)
        break
    
