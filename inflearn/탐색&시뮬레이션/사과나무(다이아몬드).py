n = int(input())
list =[list(map(int, input().split())) for _ in range(n)]

res = 0
s=e=n//2

for i in range(n):
    for j in range(s, e+1):
        res += list[i][j]
    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1

print(res)

#변수 2개 사용