
# sys.stdin = open('input.txt', 'r')
from collections import deque

dis, djs = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]

def bfs(i, j):
    q = deque()
    q.append([i,j])
    visited[i][j] = 1

    while q:
        i, j = q.popleft()

        cnt = 0
        for di, dj in zip(dis, djs):
            ni, nj = i + di, j + dj
            if ni < 0 or nj < 0 or ni >= n or nj >= n: continue
            if arr[ni][nj] == "*":
                cnt += 1
        
        if cnt == 0:
            arr[i][j] = 0
            for di, dj in zip(dis, djs):
                ni, nj = i + di, j + dj
                if ni < 0 or nj < 0 or ni >= n or nj >= n: continue
                if visited[ni][nj] == 1: continue
                visited[ni][nj] = 1
                q.append([ni, nj])
        else:
            arr[i][j] = cnt




T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    ans = 0

    for i in range(n):
        for j in range(n):
            if arr[i][j] == "." and visited[i][j] == 0:   # . 인부분 탐색
                is_bomb = False
                for di, dj in zip(dis, djs):           # 그 점 주변이 폭탄이 0개인지 확인
                    ni, nj = i + di, j + dj
                    if ni < 0 or nj < 0 or ni >= n or nj >= n: continue
                    if arr[ni][nj] == "*":
                        is_bomb = True
                if is_bomb:
                    continue
                else:
                    bfs(i, j)
                    ans += 1
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] == ".":
                ans += 1
    
    print(f"#{tc} {ans}")