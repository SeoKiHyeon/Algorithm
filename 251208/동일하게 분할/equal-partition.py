n = int(input())
arr = [0] + list(map(int, input().split()))

m = sum(arr)

dp = [False] * (m+1)
dp[0] = True

for i in range(1, n+1):
    for j in range(m, 0, -1):
        if j-arr[i] >= 0 and dp[j-arr[i]]:
            dp[j] = True


if m % 2 == 0 and dp[m//2]:
    print('Yes')
else:
    print('No')


# m부터 돌려야하나 ?  n부터 돌려야하나 ?
# True, False,
# [True, False, True, False, False, False, False, False, ]
# [True, False, True, False, True, False, False, False, ]
# [True, True, True, True, True, True, False, False, False, False, True, ]
# 


# A와 B에 들어있는 수들의 합이 일치해야함  반드시 1개 이상은 가져야함
# 그럼 한 곳이 전체 합이 반이 되면 됌

# 첫 예시  2 2 1 5
# 합이 5가되면 됌
# dp[i]에 뭐가 들어가야하는 지 모르겠다 -> 다 해본다
# 1. dp[i] << 합이 i가 가능할 때, true, false
# 2. dp[i] << i가 수들 개수 일 때, 즉 i가 4까지인 경우

# 
