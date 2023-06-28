n,k=map(int,input().split())
arr=list(map(int,input().split()))
cur=sum(arr[:k])
ans=cur
for i in range(k,n):
    cur=cur+arr[i]-arr[i-k]
    ans=max(cur,ans)
print(ans)