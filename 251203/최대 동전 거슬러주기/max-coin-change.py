n, m = map(int, input().split())
arr = list(map(int, input().split()))

dp = [float('-inf')] * (m+1)
dp[0] = 0

for i in range(1, m+1):
    for j in range(n):
        if i >= arr[j]:
            if dp[i-arr[j]] == float('-inf'): continue 
            dp[i] = max(dp[i], dp[i-arr[j]] + 1)

print(dp[m])
