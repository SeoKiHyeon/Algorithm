n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]


for k in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

for _ in range(m):
    a, b = map(int, input().split())
    print(arr[a-1][b-1])