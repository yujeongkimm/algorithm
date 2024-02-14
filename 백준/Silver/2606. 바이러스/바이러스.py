n=int(input())
m=int(input())

arr=[ [] for _ in range(n+1) ]

for _ in range(m):
    a,b=map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

count=0

def dfs(node):
    visited[node]=True
    global count
    count+=1

    for i in arr[node]:
        if not visited[i]:
            dfs(i)


visited=[False]*(n+1)
dfs(1)

print(count-1)