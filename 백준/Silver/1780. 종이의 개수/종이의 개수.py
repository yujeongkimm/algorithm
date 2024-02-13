n=int(input())

arr=[]

for _ in range(n):
    arr.append(list(map(int,input().split())))


_sum1, _sum2, _sum3 = 0,0,0


def recur(x,y,n):
    global _sum1, _sum2, _sum3
    
    check = arr[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != check:
                # 9등분
                temp = n//3

                recur(x,y,temp)
                recur(x,y+temp, temp)
                recur(x,y+ temp*2, temp)
                recur(x+temp, y, temp)
                recur(x+temp, y+temp, temp)
                recur(x+temp, y+ 2*temp, temp)
                recur(x + 2*temp, y, temp)
                recur(x + 2*temp, y+temp, temp)
                recur(x + 2*temp, y + 2*temp, temp)
                return    # 쪼갰으면 기존 탐색 종료 

    if check==-1:
        _sum1+=1
    elif check==0:
        _sum2+=1
    elif check==1:
        _sum3+=1
    return

recur(0,0,n)

print(_sum1)
print(_sum2)
print(_sum3)