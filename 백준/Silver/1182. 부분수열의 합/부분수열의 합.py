import sys
n,s = map(int, sys.stdin.readline().split(' '))
arr = list(map(int, sys.stdin.readline().split(' ')))
ans = 0

def dfs(cnt, value):
    global ans
    if cnt==n:
        if value==s:
            ans+=1
    else:
        #include
        dfs(cnt+1, value+arr[cnt])
        #not include
        dfs(cnt+1, value)

dfs(0, 0)
if s==0:
    ans-=1
print(ans)