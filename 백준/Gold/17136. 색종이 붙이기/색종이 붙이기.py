papers = {1:5, 2:5, 3:5, 4:5, 5:5}
arr=[ list(map(int,input().split())) for _ in range(10)]

result=26
def find_next(row,col):
    for r in range(row,10):
        for c in range(col,10):
            if arr[r][c]==1:
                return r,c
    return -1,-1

def fill(row,col,size,color):
    for r in range(row, row+size):
        for c in range(col, col+size):
            arr[r][c]=color

def is_valid(row, col, size):
    if row+size>10 or col+size>10:
        return False
    for r in range(row, row+size):
        for c in range(col, col+size):
            if arr[r][c]==0:
                return False
    return True

def dfs(row,col,cnt):
    global result
    if result <= cnt:
        return

    # 1찾기
    r,c = find_next(row, col)
    if r==-1 and c==-1:
        result=cnt
        return

    # 색종이 붙여가기
    for size in range(1,6):
        if papers[size]==0: continue
        if not is_valid(r,c,size):
            continue
        papers[size]-=1
        fill(r,c,size,0)
        dfs(row, col, cnt+1)
        fill(r,c,size,1)
        papers[size]+=1

dfs(0,0,0)

if result==26:
    print(-1)
else:
    print(result)