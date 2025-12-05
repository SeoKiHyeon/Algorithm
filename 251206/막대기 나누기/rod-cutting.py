n = int(input())
profit = [0] + list(map(int, input().split()))
INT_MIN = float('-inf')

dp = [INT_MIN] * (n+1) 
dp[0] = 0

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i-j] + profit[j], dp[i])

print(dp[n])


# dp[i] 에는 i 길이 만큼 막대를 사용하고  최대의 수익을 내는 지점
# Ex) dp[3] 은  dp[0] 에서 3짜리 길이 / dp[1]에서 2짜리 길이 / dp[2] 에서 1짜리 길이