text = open('pro11.txt')
lists = []
for line in text:
    line = line.rstrip()
    lists.append(line.split())

for i in range(len(lists)):
    for j in range(len(lists[i])):
        lists[i][j] = int(lists[i][j])

listx = [map(int,s.split()) for s in open('pro11.txt').readlines()]
print listx

mx = None

for i in range(len(lists)):
    for j in range(len(lists)):
        #right
        if i in range(len(lists)) and j in range(len(lists)-3):
            row,col = i,j
            mul = 1
            for n in range(4):
                mul = mul * lists[row][col]
                col += 1
            if mx is None and mx < mul:
                mx = mul
        #down
        if i in range(len(lists)-3) and j in range(len(lists)):
            row,col = i,j
            mul = 1
            for n in range(4):
                mul = mul * lists[row][col]
                row += 1
            if mx < mul:
                mx = mul
        #rightdown
        if i in range(len(lists)-3) and j in range(len(lists)-3):
            row,col = i,j
            mul = 1
            for n in range(4):
                mul = mul * lists[row][col]
                row += 1
                col += 1
            if mx < mul:
                mx = mul
        #leftdown
        if i in range(3,len(lists)-3) and j in range(len(lists)-3):
            row,col = i,j
            mul = 1
            for n in range(4):
                mul = mul * lists[row][col]
                row += 1
                col -= 1
            if mx < mul:
                mx = mul

print mx
