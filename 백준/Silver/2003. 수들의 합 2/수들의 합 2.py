n,m=map(int,input().split())
a=list(map(int,input().split()))

left,right=0,0
sum=a[0]
cnt=0
while True:
    if sum<m:
        right+=1
        if right==n:
            break
        sum+=a[right]
    elif sum>m:
        sum-=a[left]
        left+=1
    elif sum==m:
        sum-=a[left]
        left+=1
        cnt+=1
print(cnt)