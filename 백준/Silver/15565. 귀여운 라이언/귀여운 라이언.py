n,k=map(int,input().split())
arr=list(map(int,input().split()))
l,r=0,0
sum= 0
if arr[0]==1: sum=1
res=1e6
while True:
    if sum<k: # 범위 늘림
        r+=1
        if r==n:
            break
        if arr[r]==1:
            sum+=1
    if sum==k:
        res=min(res,r-l+1)
        if arr[l]==1:
            sum-=1
        l+=1

    if sum>k:  # 범위 줄임
        if arr[l]==1:
            sum-=1
        l+=1
print(-1) if res==1e6 else print(res)