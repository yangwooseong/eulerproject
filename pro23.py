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

def multwo(l):
    multwo = []
    for i in l:
        multwo.append(2*i)
    return multwo

lists = abundant(28124)
liststwo = multwo(lists)

s = 0
for i in range(1,28124):
    if i in liststwo:
        continue
    elif i < 945 and i%2 != 0:
        s += i
       # print(i)
    else:
        isSumofAbun = False
        for j in [m for m in lists if m < i]:
            if j == 0:
                continue
            if i-j in lists:
                isSumofAbun = True
                break
        if not isSumofAbun:
           # print(i)
            s += i

print (s)
