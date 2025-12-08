n, m = map(int, input().split())
exp = [0]
time = [0]
for i in range(n):
    e, t = map(int, input().split())
    exp.append(e)
    time.append(t)

# Please write your code here.
dp = [float('inf')] * (1000001)
dp[0] = 0

for i in range(1, n+1):
    for j in range(1000000, 0, -1):
        if j-exp[i] >= 0 and dp[j-exp[i]] != float('inf'):
            dp[j] = min(dp[j], dp[j-exp[i]] + time[i])

ans = float('inf')
for i in range(m, 1000001):
    ans = min(dp[i], ans)

if ans == 0:
    print(-1)
else:
    print(ans)


# n : 퀘스트 개수 / m : 얻어야하는 최소 경험치 
# e -> 획득 경험치 / t : 걸리는 시간  
# -> 최소 시간 출력

# dp[i] -> i라는 경험치를 얻었을 때, 최소 시간이 걸리면 됨
# dp[i] -> i가 시간 / dp[i]가 t