import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dis, djs = [0, 1, 0, -1], [1, 0, -1, 0]

def dfs(i, j):
    if dp[i][j] != 1:
        return dp[i][j]
    
    for di, dj in zip(dis, djs):
        tmp = 0
        ni, nj = i + di, j + dj
        if ni < 0 or ni >= n or nj < 0 or nj >= n: continue
        if arr[i][j] < arr[ni][nj]:
            tmp += dfs(ni, nj)
        dp[i][j] = max(dp[i][j], 1+tmp)
    return dp[i][j]

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[1] * (n) for _ in range(n)]

for i in range(n):
    for j in range(n):
        dfs(i, j)

ans = float('-inf')
for i in range(n):
    for j in range(n):
        ans = max(dp[i][j], ans)

print(ans)