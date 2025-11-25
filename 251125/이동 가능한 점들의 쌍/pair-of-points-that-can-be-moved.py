n, m, p, q = map(int, input().split())

dist = [[float('inf')] * (n+1) for _ in range(n+1)]

for _ in range(m):
    n1, n2, w = map(int, input().split())
    dist[n1][n2] = w

for i in range(1, n+1):
    dist[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

cnt = 0
distance = 0

for _ in range(q):
    a, b = map(int, input().split())

    min_dis = float('inf')
    for i in range(1, p+1):
        min_dis = min(min_dis, dist[a][i]+dist[i][b])
    
    if min_dis == float('inf'):
        continue
    cnt += 1
    distance += min_dis

print(cnt)
print(distance)
    