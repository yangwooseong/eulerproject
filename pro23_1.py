from __future__ import print_function

def divsum(n):
    s = 0
    t = n**0.5
    for i in range(1, int(t)+1):
        if n % i == 0: s += i + n/i
    if t == int(t): s -= t    #correct s if t is a perfect square
    s -= n
    return s

def abundant(n):
    abun = []
    for i in range(1,n):
        if divsum(i) > i:
            abun.append(i)
    return abun

abun = abundant(28124)
abunsum = [False] * 28124

for i in range(len(abun)):
    for j in abun[i:]:
        k = abun[i] + j 
        if k < 28124:
            abunsum[k] = True

s = 0
for i in range(28124):
    if not abunsum[i] :
        s += i

print (s)
