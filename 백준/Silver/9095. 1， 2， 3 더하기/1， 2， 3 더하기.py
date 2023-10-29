n=int(input())
dy=[0 for _ in range(12)] # n<11
dy[1]=1
dy[2]=2
dy[3]=4
for i in range(4,12):
    dy[i]=dy[i-1]+dy[i-2]+dy[i-3]
for i in range(n):
    x=int(input())
    print(dy[x])