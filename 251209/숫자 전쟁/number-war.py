n = int(input())

arr1 = [0] + list(map(int, input().split()))
arr2 = [0] + list(map(int, input().split()))


dp = [[-1] * (n+1) for _ in range(n+1)]
dp[0][0] = 0


for i in range(1, n+1):
    for j in range(1, n+1):
        # 대결
        if dp[i-1][j-1] == -1:
            continue

        if arr1[i] < arr2[j]:
            dp[i][j-1] = max(dp[i][j-1], dp[i-1][j-1])
        if arr1[i] > arr2[j]:
            dp[i-1][j] = max(dp[i-1][j], dp[i-1][j-1] + arr2[j])
        
        dp[i][j] = max(dp[i-1][j-1], dp[i][j])



ans = 0
for i in range(n+1):
    ans = max(ans, dp[i][n], dp[n][i])

print(ans)



# i가 3까지 
# j도 3까지
#     3  2  5
#  2 [0, 0, 0]
#  4 [2, 0, 0]
#  1 [0, 0, 0]

# 버린다 -> 대각선 이동
# 상대 한다 -> 이기면  아래로 이동
#          -> 지면    오른쪽 이동
# dp[i][j] -> dp[i-1][j], dp[i-1][j-1], dp[i][j]






# 카드 더미의 순서대로 내야함
# 대결 , 버리기 둘 모두 남우 입장에서 선택하면 됨
# dp[i][j] -> 남우의 i번째 카드가 상대방의 j번째 카드까지 붙었을 때의 최고 점수

# 1. 대결 ->  dp[i] ->  
# 2. 버리기 