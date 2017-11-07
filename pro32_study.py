# pandigital products

from __future__ import print_function

pandi = set(map(str,range(1,10)))
pandiset = set()

for i in range(2,89):
    start = 1234 if i < 10 else 123
    for j in range(start,10000//i):
        u = list(str(i))
        v = list(str(j))
        w = list(str(i*j))
        if len(u+v+w) == 9 and set(u)|set(v)|set(w) == pandi:
            if i*j not in pandiset:
                pandiset.add(i*j)

print(sum(pandiset))
