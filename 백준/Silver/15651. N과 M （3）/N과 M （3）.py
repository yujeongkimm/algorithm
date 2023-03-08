import sys
n,m = map(int, sys.stdin.readline().split(' '))

arr = [0 for _ in range(m)]
def dfs(k):
    if k == m:
        for i in arr:
            sys.stdout.write(str(i) + ' ')
        sys.stdout.write('\n')
    else:
        for i in range(1, n+1):
            arr[k] = i
            dfs(k+1)
            
dfs(0)