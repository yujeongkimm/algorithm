import sys
k,n=map(int,input().split())
arr=[int(sys.stdin.readline()) for _ in range(k)]
arr.sort()

def binary_search(arr,target):
    start,end=1, max(arr) # zeroDivisionError : https://kangfru.tistory.com/11
    global res
    while start<=end:
        ans=0
        mid=(start+end)//2  # 자를 랜선 길이
        for i in arr:
            ans += i//mid
        if ans >= target:
            res=mid
            start=mid+1
        else:
            end=mid-1
binary_search(arr,n)
print(res)