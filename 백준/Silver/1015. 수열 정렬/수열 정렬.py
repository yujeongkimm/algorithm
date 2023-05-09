import sys
n = int(sys.stdin.readline())
arr_a = list(map(int, sys.stdin.readline().split()))
arr_b = sorted(arr_a)
p = [0 for _ in range(n)]

for i in range(n):
    index = arr_b.index(arr_a[i])
    p[i] = index
    arr_b[index] = -1   # 방문처리

for i in range(n):
    sys.stdout.write(str(p[i]) + ' ')