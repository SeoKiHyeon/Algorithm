import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

from collections import deque

dis, djs = [0, 1, 0, -1], [1, 0, -1, 0]

def bfs():
    global cnt
    while q:
        i, j = q.popleft()

        for di, dj in zip(dis, djs):
            ni, nj = i + di, j + dj
            if ni < 0 or nj < 0 or ni >= n or nj >= m: continue
            if arr[ni][nj] == -1: continue
            if visited[ni][nj] > -1: continue
            visited[ni][nj] = visited[i][j] + 1

            cnt -= 1
            q.append([ni, nj])




m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

q = deque([])
visited = [[-1] * (m) for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append([i, j])
            visited[i][j] = 0
        if arr[i][j] == 0:
            cnt += 1

bfs()

ans = float('-inf')
for i in range(n):
    for j in range(m):
        ans = max(ans, visited[i][j])



if cnt != 0:
    print(-1)
else:
    print(ans)