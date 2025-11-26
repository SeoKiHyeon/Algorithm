n, m = map(int, input().split())

v1, v2, e = map(int, input().split())

dist = [[float('inf')] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
  dist[i][i] = 0

for i in range(m):
  n1, n2, w = map(int, input().split())
  dist[n1][n2] = w
  dist[n2][n1] = w


for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


distance = float('inf')

for k in range(1, n+1):

  distance = min(distance, dist[v1][k] + dist[v2][k] + dist[k][e])

print(distance)