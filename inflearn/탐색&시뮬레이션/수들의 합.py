n, m = map(int, input().split())
list = list(map(int, input().split()))
sum = cnt = 0

for i in range(n):
    for j in range(i, n):
        sum+=list[j]
        if sum>m:
            break
        if sum==3:
            cnt+=1
    sum=0
print(cnt)