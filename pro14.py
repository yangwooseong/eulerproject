from __future__ import print_function

def collatz(n):
    s = 1
    if n % 2 ==0:
        return collatz(n/2) + 1
    while n != 1:
        if n % 2 ==0:
            n = n/2
        else:
            n = 3*n + 1
        s = s + 1
    return s

mx,mn = 0,0
n = 1
while n <= 1000000:
    if mx < collatz(n):
        mx = collatz(n)
        mn = n
    n += 1

print(mn)
