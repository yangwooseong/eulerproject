from __future__ import print_function

txt = open('pro18.txt')
lists = []
for line in txt:
    line = line.rstrip()
    g = map(int,line.split())
    lists.append(g)

k = None
s = 0

for i in range(len(lists))[::-1]:
    for j in range(len(lists[i])-1):
        if lists[i][j] < lists[i][j+1]:
            lists[i-1][j] += lists[i][j+1]
        else:
            lists[i-1][j] += lists[i][j]

print(lists)
