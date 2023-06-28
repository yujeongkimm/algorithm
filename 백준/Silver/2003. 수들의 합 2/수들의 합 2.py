n,m=map(int,input().split())
arr=list(map(int,input().split()))
l,r=0,0
sum=arr[0]
ans=0
while True:
    if sum<m:    # r늘림
        r+=1
        if r==n:
            break
        sum+=arr[r]
    elif sum==m:
        ans+=1
        sum-=arr[l]
        l+=1
    else: # l늘림
        sum-=arr[l]
        l+=1
print(ans)