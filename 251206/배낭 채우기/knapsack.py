n, m = map(int, input().split())

INT_MIN = float('-inf')
weight = [0]
value  = [0]

for i in range(n):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

dp = [[INT_MIN] * (m+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(1, n+1):
    for j in range(m+1):
        if j - weight[i] >= 0:
            dp[i][j] = max(dp[i-1][j-weight[i]] + value[i], dp[i-1][j])
        
        else:
            dp[i][j] = dp[i-1][j]

ans = 0

for j in range(m+1):
    ans = max(ans, dp[n][j])

print(ans)
            
        
        