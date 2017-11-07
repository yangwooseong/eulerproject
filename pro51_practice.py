# Prime digit replacements

from __future__ import print_function
import sys

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
        number += 2

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

# eliminate primes with distinct digits
for prime in get_primes(56993):
    if len(str(prime)) == len(set(str(prime))):
        continue
    checked = []
    
    if prime not in checked:
        digitsGroup = sameDigits(prime)
        for group in digitsGroup:
            family = replace(prime,group)
            for i in family:
                checked.append(i)
            if len(family) == 9:
                print(family,prime)
                sys.exit()
           
