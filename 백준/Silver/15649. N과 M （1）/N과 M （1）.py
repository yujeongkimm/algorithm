import sys
n, m = map(int, sys.stdin.readline().split(' '))

arr = [0 for _ in range(m)]
def dfs(cnt):
    if cnt == m:
        for i in arr:
            sys.stdout.write(str(i)+' ')
        sys.stdout.write('\n')
    else:
        for i in range(1, n+1):
            if i in arr:
                continue
            arr[cnt] = i
            dfs(cnt+1)
            arr[cnt] = 0

dfs(0)