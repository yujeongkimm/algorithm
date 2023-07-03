import sys
n,m=map(int,input().split())
arr=[int(sys.stdin.readline()) for _ in range(n)]
arr.sort()
l,r=0,1
res=sys.maxsize
while l<n and r<n:
    sub=arr[r]-arr[l]
    if sub<m:
        r+=1
    elif sub==m:   # 가장 작은 차이
        res=sub
        break
    elif sub>m:
        res=min(res, sub)
        l+=1

print(res)