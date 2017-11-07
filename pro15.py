from __future__ import print_function

def routes(rows,cols):
    dp = []
    for i in range(rows):
        dp.append([])
        for j in range(cols):
            dp[i].append(0)

    for i in range(rows):
        for j in range(cols):
            if j == 0 and i == 0:
                dp[i][j] = 0
            elif j == 0 or i == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp

DP = routes(21,21)
print (DP)
