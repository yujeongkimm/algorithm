import sys
sys.setrecursionlimit(10**6)
n,m=map(int,input().split())

nodes=list(map(int,input().split()))

graph=[[] for _ in range(n+1)]
for i, node in enumerate(nodes):
    if i==0:
        continue
    graph[node].append(i+1)

stars=[0]*(n+1)

def dfs(current_node):
    for child in graph[current_node]:
        stars[child]+=stars[current_node]
        dfs(child)


for _ in range(m):
    i,w=map(int,input().split())
     # 내가 받은 칭찬 누적, 한번에 전파. 탐색 횟수 줄이기
    stars[i]+=w

dfs(1)

stars=stars[1:]
print(*stars)