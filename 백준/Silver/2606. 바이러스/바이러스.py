from collections import deque
n=int(input())
m=int(input())
adj=[ [] for _ in range(n+1) ]
for _ in range(m):
    x,y=map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)
    
visited=[0]*(n+1)
def bfs(x):
    queue=deque()
    queue.append(x)
    visited[x]=1
    
    while queue:
        v=queue.popleft()
        for i in adj[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=1
bfs(1)
print(sum(visited)-1)
    