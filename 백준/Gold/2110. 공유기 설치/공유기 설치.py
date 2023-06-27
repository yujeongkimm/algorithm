import sys
n,c=map(int,input().split())
arr=[int(sys.stdin.readline()) for _ in range(n)]
arr.sort()
def binary_search(arr,target):
    start,end=1,arr[-1]-arr[0]  # 공유기 사이에 나올 수 있는 거리의 최소, 최대값
    result=0
    while start<=end:
        mid=(start+end)//2  # 두 공유기 사이 거리
        cnt=1
        tmp=arr[0]  # 제일 앞집에 공유기 설치
        for i in range(1, n):
            if mid+tmp<=arr[i]:
                cnt+=1
                tmp=arr[i]
        if cnt<target:
            end=mid-1
        else:
            result=mid
            start=mid+1
    return result
print(binary_search(arr,c))