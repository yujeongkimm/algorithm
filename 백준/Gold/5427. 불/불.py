from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def is_escape(x,y):
    if x == 0 or y==0 or x == r-1 or y == c-1:
        return True

def lets_escape():

    fireQ = deque()
    myQ = deque()

    for i in range(r):
        for j in range(c):
            if arr[i][j] == '*':
                fireQ.append((i,j))
                fire[i][j] = 1

            elif arr[i][j] == '#':
                fire[i][j] = -1

            elif arr[i][j] == '@':
                visited[i][j] = 1
                myQ.append((i,j))

    # 1. 불 전파
    while fireQ:
        x,y = fireQ.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=r or ny<0 or ny>=c:
                continue

            # 불 이동 가능 > 빈공간
            if fire[nx][ny] == 0 :
                fireQ.append((nx,ny))
                fire[nx][ny] = fire[x][y] + 1

    is_boolean = True
    # 2. 탐색
    while myQ:
        x, y = myQ.popleft()

        if is_escape(x,y):
            is_boolean = False
            print(visited[x][y])
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=r or ny<0 or ny>=c:
                continue

            if visited[nx][ny] !=0:
                continue

            # 이동  가능
            if fire[nx][ny] == 0 or fire[nx][ny] > visited[x][y] +1 :
                visited[nx][ny] = visited[x][y] + 1
                myQ.append((nx,ny))

    if is_boolean:
        print("IMPOSSIBLE")
        return

t=int(input())

for _ in range(t):
    c,r = map(int,input().split())
    arr = [input() for _ in range(r)]
    fire = [[0] * c for _ in range(r)]
    visited = [[0] * c for _ in range(r)]

    lets_escape()