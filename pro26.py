from __future__ import print_function

def cycleoffrac(div):
    num = 1
    cycle = False
    lists = []
    s = 0
    L = 1000
    
    while num // div == 0:
        num = num * 10
    while s <= 2000 and num != 0 and not cycle:
        p, r = divmod(num,div)
        lists.append(p)
        num = 10 * r
        s += 1
    for i in range(1,L):
        if lists[0:i] == lists[i:2*i] :
            break
    return i

mx = 0

for i in range(2,1000):
    if i % 2 == 0 or i % 5 == 0:
        continue
    if mx < cycleoffrac(i):
        mx = cycleoffrac(i)
        div = i
    
# print(cycleoffrac(243),243)
print(div,mx)
