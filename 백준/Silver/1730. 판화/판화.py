n=int(input())
do=input()
pass_verticle=[[0 for _ in range(n)] for _ in range(n)]
pass_horizontal=[ [0 for _ in range(n)] for _ in range(n)]

# 1.
x,y=0,0
for d in do:
    if d=='D':
        if x+1<n:
            pass_verticle[x][y]=True
            x+=1
            pass_verticle[x][y]=True
    elif d=='R':
        if y+1<n:
            pass_horizontal[x][y]=True
            y+=1
            pass_horizontal[x][y] = True
    elif d=='L':
        if y==0: continue
        pass_horizontal[x][y] = True
        y -= 1
        pass_horizontal[x][y] = True
    elif d=='U':
        if x==0: continue
        pass_verticle[x][y] = True
        x -= 1
        pass_verticle[x][y] = True

# 2. 배열 순회하면서 출력
for i in range(n):
    for j in range(n):
        if pass_horizontal[i][j] and pass_verticle[i][j]:
            print("+", end='')
        elif pass_horizontal[i][j] and not pass_verticle[i][j]:
            print("-", end='')
        elif not pass_horizontal[i][j] and pass_verticle[i][j]:
            print("|", end='')
        elif not pass_horizontal[i][j] and not pass_verticle[i][j]:
            print(".", end='')
    print()