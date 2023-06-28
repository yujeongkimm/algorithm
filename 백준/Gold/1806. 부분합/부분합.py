n,s=map(int,input().split())
arr=list(map(int,input().split()))
l,r=0,0
length=100000
S=arr[0]
while True:
    if S >= s:    # 최소 길이 비교, sum, l 갱신
        length=min(length,r-l+1)
        S-=arr[l]
        l+=1
    else:
        r+=1
        if r==n:
            break
        S+=arr[r]
print(0) if length==100000 else print(length)