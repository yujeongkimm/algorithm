from copy import deepcopy
from collections import deque

import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]
def melt(x,y):
    cnt=0

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<n and 0<=ny<m and arr[nx][ny]==0:
            cnt+=1

    return cnt

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y]=True

    while queue:
        _x, _y = queue.popleft()

        for i in range(4):
            nx=_x+dx[i]
            ny=_y+dy[i]

            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and arr[nx][ny]!=0:
                queue.append((nx,ny))
                visited[nx][ny]=True

answer=1

while True:
    flag=True

    # 전부 녹음
    for i in range(n):
        for j in range(m):
            if arr[i][j]!=0:
                flag=False

    if flag:
        print(0)
        break

    _arr = deepcopy(arr)
    # 빙산 녹음
    for i in range(n):
        for j in range(m):
            if arr[i][j]!=0:
                _arr[i][j] = max(0,arr[i][j]-melt(i,j))

    arr = _arr

    visited= [[False]*m for _ in range(n)]
    piece=0
    # 개수 세기
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j]!=0:
                bfs(i,j)
                piece+=1

    if piece >=2 :
        print(answer)
        break

    answer+=1