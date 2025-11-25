n, m, p, q = map(int, input().split())

dist = [[[float('inf'), 0] for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    dist[i][i][0] = 0


for i in range(m):
    n1, n2, w = map(int, input().split())
    if n1 <= p or n2 <= p:
        dist[n1][n2][1] = 1
    dist[n1][n2][0] = w


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][j][0] > dist[i][k][0] + dist[k][j][0]:
                dist[i][j][0] = dist[i][k][0] + dist[k][j][0]
                if dist[i][k][1] == 1 or dist[k][j][1] == 1:
                    dist[i][j][1] = 1

cnt = 0
distance = 0

for i in range(q):
    a, b = map(int, input().split())
    if dist[a][b][1] == 1:
        if dist[a][b][0] != float('inf'):
            cnt += 1
            distance += dist[a][b][0]



print(cnt)
print(distance)