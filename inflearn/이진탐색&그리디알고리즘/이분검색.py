n,m=map(int,input().split())
a=list(map(int, input().split()))

# 이진탐색 기본, 오름차순, 내림차순 정렬
a.sort()
start = 0
end = n-1

while start<=end:
    mid=(start+end)//2
    if a[mid]==m:
        print(mid+1)
        break
    elif m>a[mid]:
        start=mid+1
    else:
        end=mid-1