# 1000-digit Fibonacci number 

from __future__ import print_function

def fibonacci():
    n = 3
    a,b = 1,1
    while True:
        yield a+b
        temp = a
        a = b
        b = temp + b
               
n = 2

for i in fibonacci():
    n += 1
    if i // (10**999) != 0:
        print(n,i)
        break
