n, k, b = map(int, input().split())
arr = [0] * (n+1)
sum_arr = [0] * (n+1)


def get_sum(s, e):
    return sum_arr[e] - sum_arr[s-1]

ans = float('inf')

for _ in range(b):
    x = int(input())
    arr[x] = 1

for i in range(1, n+1):
    sum_arr[i] = sum_arr[i-1] + arr[i]

for i in range(1, n-k+2):
    ans = min(ans, get_sum(i, i+k-1))

print(ans)