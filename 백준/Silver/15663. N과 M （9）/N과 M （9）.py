import sys
n,m=map(int, sys.stdin.readline().split(' '))
arr = sorted(list(map(int, sys.stdin.readline().split(' '))))
selected = [0 for _ in range(m)]
used = [0 for _ in range(n)]

def dfs(cnt):
    if cnt==m:
        for i in selected:
            sys.stdout.write(str(i)+' ')
        sys.stdout.write('\n')
    else:
        last_cand=0
        for i in range(n):
            if used[i]==1 or last_cand==arr[i]:
                continue
            selected[cnt]=arr[i]
            used[i]=1
            last_cand=arr[i]
            
            dfs(cnt+1)
            selected[cnt]=0
            used[i]=0
dfs(0)