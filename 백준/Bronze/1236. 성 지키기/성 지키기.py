x,y=map(int,input().split())
a=[]
for i in range(x):
    a.append(list(input()))

row,column=0,0
# 1. 행, 열에 경비원 있는지 확인
for r in range(x):
    for c in range(y):
        if a[r][c]=='X':
            row+=1
            break
for c in range(y):
    for r in range(x):
        if a[r][c]=='X':
            column+=1
            break

# 2. 보호 받지 못하는 행,열 출력
needProtectrow=x-row
needProtectColumn=y-column

# 3. 남은 행, 열 중 큰 숫자 출력
print(max(needProtectrow,needProtectColumn))