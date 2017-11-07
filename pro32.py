# pandigital products

from __future__ import print_function

pandi = set(map(str,range(1,10)))
pandiset = set()

for i in range(101,879):
    for j in range(12,99):
        if i*j < 10**4:
            u = set(str(i))
            v = set(str(j))
            w = set(str(i*j))
            if len(u) == 3 and len(v) == 2 and len(w) == 4 \
                    and u|v|w == pandi:
                pandiset.add(i*j)

for i in range(1234,4789):
    for j in range(2,9):
         if i*j < 10**4:
            u = set(str(i))
            v = set(str(j))
            w = set(str(i*j))
            if len(u) == 4 and len(w) == 4 \
                    and u|v|w == pandi:
                pandiset.add(i*j)

print(sum(pandiset))
