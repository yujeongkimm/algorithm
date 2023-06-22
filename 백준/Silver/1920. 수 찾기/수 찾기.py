def binary_search(target, arr):
    start, end = 0, len(arr)-1
    res = 0
    while start<=end:
        mid=(start+end)//2
        if arr[mid]<target:
            start=mid+1
        elif arr[mid]>target:
            end=mid-1
        elif arr[mid]==target:
            res=1
            break
    return res

n = int(input())
listN = list(map(int, input().split()))
m = int(input())
listM = list(map(int, input().split()))
listN.sort()
for target in listM:
    print(binary_search(target, listN))