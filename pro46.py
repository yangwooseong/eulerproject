from __future__ import print_function

import math,time

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

def get_composite():
    n = 9
    while True:
        if not is_prime(n):
            yield n
        n += 2

found = True

for i in get_composite():
    found = True 
    for j in range(3,i-1,2):
        if is_prime(j) and math.sqrt( (i-j) / 2) % 1 ==0:
            found = False
    if found :
        print(i,j,(i-j)/2)
        break
