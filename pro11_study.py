g = [map(int,s.split()) for s in open('pro11.txt').readlines()]
print listx

mx = 0
len(g) = row
len(g[0]) = col

for i in range(row):
    for j in range(col-3):
        #right,down
        maxn = max(g[i][j]*g[i+1][j]*g[i+2][j]*g[i+3][j],g[j][i]*g[j+1][i]*g[j+2][i]*g[j+3][i])
        if i in range(row-3):
            maxd = max(g[i][j]*g[i+1][j+1]*g[i+2][j+2]*g[i+3][j+3],g[i][j]*g[i+1][j-1]*g[i+2][j-2]*g[i+3][j-3])
        mx = max(mx,maxn,maxd)

print mx
