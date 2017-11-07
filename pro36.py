from __future__ import print_function

def binary(n):
    b = ''
    while n != 0:
        b = str(n % 2) + b
        n //= 2
    return b

s = 0

for i in range(1,1000000):
    if str(i) == str(i)[::-1] and binary(i) == binary(i)[::-1]:
        s += i

print(s)
