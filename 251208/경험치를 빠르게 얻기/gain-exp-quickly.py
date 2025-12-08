n, m = map(int, input().split())
exp = [0]
time = [0]
for i in range(n):
    e, t = map(int, input().split())
    exp.append(e)
    time.append(t)

# Please write your code here.
sum_time = sum(time)

dp = [float('-inf')] * sum_time
dp[0] = 0

for i in range(1, n+1):
    for j in range(sum_time-1, 0, -1):
        if j-time[i] >= 0 and dp[j-time[i]] != float('-inf'):
            dp[j] = max(dp[j], dp[j-time[i]] + exp[i])

ans = 0
for i in range(sum_time):
    if dp[i] >= m:
        ans = i
        break

if ans == 0:
    print(-1)
else:
    print(ans)



# n : 퀘스트 개수 / m : 얻어야하는 최소 경험치 
# e -> 획득 경험치 / t : 걸리는 시간  
# -> 최소 시간 출력

# dp[i] -> i라는 경험치를 얻었을 때, 최소 시간이 걸리면 됨
# dp[i] -> i가 시간 / dp[i]가 t