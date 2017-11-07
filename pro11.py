text = open('pro11.txt')
lists = []
for line in text:
    line = line.rstrip()
    lists.append(line.split())

for i in range(len(lists)):
    for j in range(len(lists[i])):
        lists[i][j] = int(lists[i][j])

moves = [[1,0],[0,1],[1,1]]

MAX = None
for i in range(len(lists)):
    if i in range(len(lists)-3):
        for j in range(len(lists[i])-3):
            if i == 0:
                print lists[i][j]
            for x,y in moves:
                m,n = i,j
                threeLists =[]
                mul = 1
                for i in range(4):
                    mul = mul * lists[m][n]
                    m += x
                    n += y
                threeLists.append(mul)
            if MAX is None or MAX < max(threeLists):
                MAX = max(threeLists)
    else:
        for j in range(len(lists[i])-3):
            m,n = i,j
            threeLists = []
            mul = 1
            for i in range(4):
                mul = mul * lists[m][n]
                m += 0
                n += 1
            threeLists.append(mul)
            if MAX < max(threeLists):
                print 
                MAX = max(threeLists)

for i in range(3,len(lists)):
    for j in range(3,len(lists)):
        m,n = i,j
        threeLists = []
        mul = 1
        for i in range(4):
            mul = mul * lists[m][n]
            m += -1
            n += -1
            threeLists.append(mul)
        if MAX < max(threeLists):
            MAX = max(threeLists)

print MAX
