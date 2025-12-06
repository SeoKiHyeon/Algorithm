n, m = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(n)])
w, v = [0] + list(w), [0] + list(v)
INT_MIN = float('-inf')
# Please write your code here.
# m이 총 무게 
# dp[i][j] -> i번 보석 까지 선택했을 때, j까지의 가치   i가 보석 넘버 / j가 무게
# Ex) i가 2일 때,  dp[2][] -> 1,1,1  / dp[1] 에서 2번 보석을 최대 무게까지 저장
# dp[1] 에는 dp[1][7] = 20, dp[1][14] = 40, dp[1][21] = 60
# dp[i][j] -> dp[i-1][j-w[i]] 

dp = [INT_MIN] * (m+1)
dp[0] = 0

for i in range(1, m+1):
    for j in range(n+1):
        if i >= w[j]:
            dp[i] = max(dp[i], dp[i-w[j]] + v[j])

print(max(dp))
