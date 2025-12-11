n, m, k = map(int, input().split())

# Read grid as list of strings since we need character-by-character access
grid = [[""] + list(input()) for _ in range(n)]
grid = [[""] * (m+1)] + grid
# Read k queries as tuples
queries = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
sum_arr = [[[0,0,0] for _ in range(m+1)] for _ in range(n+1)]

if grid[1][1] == 'a':
    sum_arr[1][1][0] = 1
elif grid[1][1] == 'b':
    sum_arr[1][1][1] = 1
elif grid[1][1] == 'c':
    sum_arr[1][1][2] = 1

for i in range(n+1):
    for j in range(m+1):
        na, nb, nc = sum_arr[i-1][j]
        ma, mb, mc = sum_arr[i][j-1]
        la, lb, lc = sum_arr[i-1][j-1]
        if grid[i][j] == 'a':
            sum_arr[i][j][0] = na + ma - la + 1
            sum_arr[i][j][1] = nb + mb - lb 
            sum_arr[i][j][2] = nc + mc - lc 
        elif grid[i][j] == 'b':
            sum_arr[i][j][0] = na + ma - la 
            sum_arr[i][j][1] = nb + mb - lb + 1
            sum_arr[i][j][2] = nc + mc - lc 

        elif grid[i][j] == 'c':
            sum_arr[i][j][0] = na + ma - la 
            sum_arr[i][j][1] = nb + mb - lb 
            sum_arr[i][j][2] = nc + mc - lc + 1

def solved(r1, c1, r2, c2):
    # r2, c1-1 /  r1-1   c2    / r1-1  c1-1
    a, b, c = sum_arr[r2][c2]
    na, nb, nc = sum_arr[r2][c1-1]
    ma, mb, mc = sum_arr[r1-1][c2]
    la, lb, lc = sum_arr[r1-1][c1-1]

    a = a - na - ma + la
    b = b - nb - mb + lb
    c = c - nc - mc + lc

    return a, b, c

for query in queries:

    a, b, c = solved(*query)
    print(a, b, c)