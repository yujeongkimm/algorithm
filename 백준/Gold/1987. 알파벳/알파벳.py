r,c=map(int,input().split())
arr=[list(input()) for _ in range(r)]

dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]

alphabet=[0]*26
answer=1
def dfs(x,y,cnt):
    global answer
    answer=max(answer, cnt)


    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        #경계체크
        if 0<=nx<r and 0<=ny<c and alphabet[ord(arr[nx][ny])-65]==0:
            # add
            alphabet[ord(arr[nx][ny])-65]=1
            dfs(nx, ny, cnt+1)
            # remove
            alphabet[ord(arr[nx][ny])-65]=0

alphabet[ord(arr[0][0])-65]=1
dfs(0,0,1)
print(answer)
