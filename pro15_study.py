# Lattice paths from (0,0) to (n,n) but do not pass below the diagonal

from __future__ import print_function

def routes(n):
    dp = []
    for i in range(n):
        dp.append([])
        for j in range(n):
            if j <= i:
                dp[i].append(0)
    for i in range(n)[::-1]:
        for j in range(len(dp[i]))[::-1]:
            if i == n-1 :
                if j != n-1:
                    dp[i][j] = 1
                else :
                    dp[i][j] = 0
            else:
                if i == j:
                    dp[i][j] = dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
    return dp


DP = routes(5)
print (DP)
