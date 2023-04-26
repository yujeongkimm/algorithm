import sys
n,m=map(int, sys.stdin.readline().split(' '))
arr=sorted(list(map(int, sys.stdin.readline().split(' '))))
selected=[0 for _ in range(m)]
def dfs(cnt):
    if cnt==m:
        for i in selected:
            sys.stdout.write(str(i)+' ')
        sys.stdout.write('\n')
    else:
        for i in range(n):
            if arr[i] in selected:
                continue
            selected[cnt]=arr[i]
            dfs(cnt+1)
            selected[cnt]=0
dfs(0)