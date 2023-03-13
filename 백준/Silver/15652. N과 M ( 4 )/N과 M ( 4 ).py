import sys

n, m = map(int, sys.stdin.readline().split(' '))
arr = [0 for _ in range(m)]


def dfs(cnt):
    if cnt == m:
        for i in arr:
            sys.stdout.write(str(i) + ' ')
        sys.stdout.write('\n')
    else:
        start = 1 if cnt == 0 else arr[cnt - 1]
        for i in range(start, n + 1):
            arr[cnt] = i
            dfs(cnt + 1)
            arr[cnt] = 0


dfs(0)