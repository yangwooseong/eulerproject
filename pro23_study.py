from __future__ import print_function

def divsum(n):
    s = 0
    t = n**0.5
    for i in range(1, int(t)+1):
        if n % i == 0: s += i + n/i
    if t == int(t): s -= t    #correct s if t is a perfect square
    s -= n
    return s

L, s = 28123, 0
abn = set()

for i in range(1,L+1):
    if divsum(i) > i:
        abn.append(i)
    if not any ((i-n in abn) for n in abn):
        s += i

print (s)
