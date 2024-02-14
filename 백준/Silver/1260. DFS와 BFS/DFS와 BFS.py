from collections import deque

n,m,v=map(int,input().split())

arr=[ [] for _ in range(n+1) ]

for _ in range(m):
    a,b=map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in arr:
    i.sort()


def dfs(node):
    # 방문
    visited[node]=True
    print(node, end=' ')

    for i in arr[node]:
        if not visited[i]:
            dfs(i)

def bfs(node):
    queue = deque([node])
    visited[node]=True

    while queue:
        p = queue.popleft()
        print(p, end=' ')

        for i in arr[p]:
            if not visited[i]:
                visited[i]=True
                queue.append(i)

visited=[False]*(n+1)
dfs(v)

print()

visited=[False]*(n+1)
bfs(v)