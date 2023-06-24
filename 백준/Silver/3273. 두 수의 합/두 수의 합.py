n=int(input())
arr=list(map(int,input().split()))
x=int(input())
arr.sort()  # 1 2 3 5 ...
ans=0
for i in range(n):  # i는 인덱스 값
    start, end = i+1, len(arr) - 1  # 중복되는 쌍 피하기 위해 탐색 범위 설정
    target=x-arr[i]
    while start<=end:
        mid=(start+end)//2  # mid는 인덱스 값
        if arr[mid]==target:
            ans+=1
            break
        elif arr[mid]<target:
            start=mid+1
        elif arr[mid]>target:
            end=mid-1
print(ans)