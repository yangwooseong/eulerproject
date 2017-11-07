# sub-string divisibility

from __future__ import print_function
import re

def pandigital(n):
    return all(i in str(n) for i in '1234567890')
          
def subpan(n):
    return len(str(n)) == len(set(str(n)))

lists = []

for i in range(102,1000,17):
    if subpan(i):
        lists.append(str(i))

print(lists)

for i in lists:
    for j in range(10):
        if (str(j) not in i) and (j*100+int(i[:2])) % 11 == 0:
            print(str(j)+i)
        
print(lists)
