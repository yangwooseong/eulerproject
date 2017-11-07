from __future__ import print_function
import string

txt = open('pro22.txt').read().rstrip().split(',')
for i in range(len(txt)):
    txt[i] = txt[i][1:-1]

sm = 0
txt.sort()
alphabets = list(string.ascii_uppercase)
for names in txt:
    s = 0
    for symbol in names:
        s += alphabets.index(symbol) + 1
    sm += s * (txt.index(names) + 1)
print(sm)
