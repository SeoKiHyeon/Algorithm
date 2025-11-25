n, m, p, q = map(int, input().split())

dist = [[[float('inf'), float('inf')] for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    dist[i][i][0] = 0
    if i <= p:
        dist[i][i][1] = 0


for i in range(m):
    n1, n2, w = map(int, input().split())
    if n1 <= p or n2 <= p:
        dist[n1][n2][1] = w
    else:
        dist[n1][n2][0] = w


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):

            nxt1 = dist[i][k][0] + dist[k][j][0]
            if dist[i][j][0] > nxt1:
                dist[i][j][0] = nxt1
            nxt2 = min(
                dist[i][k][1] + dist[k][j][0],
                dist[i][k][0] + dist[k][j][1],
                dist[i][k][1] + dist[k][j][1])
            if dist[i][j][1] > nxt2:
                dist[i][j][1] = nxt2


cnt = 0
distance = 0

for i in range(q):
    a, b = map(int, input().split())

    if dist[a][b][1] != float('inf'):
        cnt += 1
        distance += dist[a][b][1]



print(cnt)
print(distance)