n = int(input())
dir = [[0,0,0]]
for _ in range(n):
    l, m, r = map(int, input().split())
    dir.append([l,m,r])

dp = [[float('-inf')] * 3 for _ in range(n+1)]

for i in range(3):
    dp[1][i] = dir[1][i]


for i in range(2, n+1):
    for j in range(3):
        for k in range(3):
            if k != j:
                dp[i][j] = max(dp[i][j], dp[i-1][k] + dir[i][j] )

print(max(dp[-1]))