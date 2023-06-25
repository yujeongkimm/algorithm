n=int(input())
arr=list(map(int,input().split()))
m=int(input())
arr.sort()
def binary_search(arr,target):
    start,end=1, max(arr)
    res=0
    while start<=end:
        total=0
        mid=(start+end)//2  # 상한
        for i in arr:
            if i>mid:
                total+=mid
            else:
                total+=i
        if total>target:
            end=mid-1
        else:
            start=mid+1
            res=mid
    return res

print(binary_search(arr,m))