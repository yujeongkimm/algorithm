import sys
sys.setrecursionlimit(10**6)

N,R,Q=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(N+1)]

for _ in range(N-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

node_size=[0]*(N+1)
visited=[False]*(N+1)

def count(currentNode):
    node_size[currentNode]+=1

    visited[currentNode] = True

    for child in graph[currentNode]:
        if not visited[child]:
            count(child)
            node_size[currentNode]+=node_size[child]


count(R)

for _ in range(Q):
    n=int(sys.stdin.readline())
    print(node_size[n])
