n,m=map(int,input().split())
moneys=[int(input()) for _ in range(n)]
result=0

left,right=max(moneys),sum(moneys)

while left<=right:
    mid=(left+right)//2
    cnt = 1
    leftover=mid
    for money in moneys:
        leftover-=money
        if leftover<0:
            cnt+=1
            leftover=mid-money
    if cnt>m:
        left=mid+1
    else:
        right=mid-1
        result = mid

print(result)