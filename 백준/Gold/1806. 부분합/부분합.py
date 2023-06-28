n,s=map(int,input().split())
arr=list(map(int,input().split()))
l,r=0,0
sum=arr[0]
length=100000
while True:
    if sum>=s:
        length=min(length,r-l+1)    # 최소길이 갱신
        sum-=arr[l]
        l+=1
    else: # 누적합이 작으면 end 늘림
        r += 1
        if r==n:
            break
        sum+=arr[r]
print(0) if length==100000 else print(length)