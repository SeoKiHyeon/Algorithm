
n, m = map(int, input().split())

dist = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dist[i][i] = 0

for i in range(m):
    n1, n2 = map(int, input().split())
    dist[n1][n2] = 1



for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][k] and dist[k][j]:
                dist[i][j] = 1


for i in range(1, n + 1):
    cnt = 0
    for j in range(1, n + 1):
        if i == j:
            continue
        if dist[i][j] or dist[j][i]: # 둘 중 누가 큰지 알 수 있는 경우라면
            continue                   # 패스합니다.
        cnt += 1
    print(cnt)