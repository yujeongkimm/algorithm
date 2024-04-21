from collections import deque

n,k=map(int,input().split())
MAX=10**5
# 방문 , 시간 함께 기록
visited=[0]*(MAX+1)

def bfs():
    queue=deque()
    queue.append(n)

    while queue:
        _n = queue.popleft()

        if _n==k:
            print(visited[_n])
            break

        for new_n in (_n-1,_n+1, 2*_n):
            if 0<=new_n<=MAX and not visited[new_n]:
                queue.append(new_n)
                visited[new_n]=visited[_n]+1
bfs()