from __future__ import print_function

def divisors(n):
    divs = []
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            if n**0.5 == n/i:
                divs.append(i)
                continue
            divs.append(i)
            divs.append(n/i)
    return divs

def divsum(n):
    ds = {}
    p = 0
    i = 2
    mul = 1
    while n!= 1:
        if n % i == 0:
            p += 1
            n = n/i
            if n%i != 0:
                ds[i] = p
                p = 0
                i += 1
                continue
        else:
            i += 1
    for k,v in ds.items():
        mul = mul * (k**(v+1)-1)/(k-1)
    return mul

def d(n):
    s = 1
    t = n**0.5
    for i in range(2, int(t)+1):
        if n % i == 0: s += i + n/i
    if t == int(t): s -= t    #correct s if t is a perfect square
    return s

sm = 0
for i in range(2,10000):
    d_i = d(i)
    if i > d(i) and i == d(d_i):
        sm += i + d(i)

print(sm)
