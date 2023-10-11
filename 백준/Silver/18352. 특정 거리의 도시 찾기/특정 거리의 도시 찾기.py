from collections import deque
import sys
n,m,k,x=map(int,sys.stdin.readline().split())
graph=[ [] for _ in range(n+1) ]
visited= [False] * (n+1)

for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)

answer=[]
distance=[0] * (n+1)
def bfs(start):
    queue=deque()
    queue.append(start)
    visited[start] = True
    distance[start]=0

    while queue:
        v = queue.popleft()
        for i in graph[v]: # 인접노드
            if not visited[i]:
                distance[i]=distance[v]+1 # 거리정보 업데이트
                queue.append(i)
                visited[i]=True
                if distance[i]==k:
                    answer.append(i)
bfs(x)
if len(answer)==0:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i, end='\n')