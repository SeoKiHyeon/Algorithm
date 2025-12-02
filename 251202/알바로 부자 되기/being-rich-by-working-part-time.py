
N = int(input().strip())
jobs = []

for _ in range(N):
    s, e, p = map(int, input().split())
    jobs.append((s, e, p))

# 끝나는 날 기준으로 정렬
jobs.sort(key=lambda x: x[1])

# dp[i] : jobs[0..i-1] 까지 고려했을 때 얻을 수 있는 최대 수입
dp = [0] * (N + 1)

for i in range(1, N + 1):
    best_price = 0
    for j in range(i-1, 0, -1):
        if jobs[i-1][0] > jobs[j-1][1]:
            best_price = dp[j]
            break
    
    dp[i] = max(dp[i-1], best_price + jobs[i-1][2])


print(dp[N])