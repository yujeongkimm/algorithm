#http://boj.kr/7795
import sys
# 이분탐색 => 특정 값의 위치가 궁금할 때
def binary_search(arr, target):
    start, end = 0, len(arr)-1
    res=-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]<target:
            res=mid
            start=mid+1
        else:
            end=mid-1
    return res 


def solve(listA, listB):
    answer=0
    listA.sort()
    listB.sort()
    for a in listA:
        answer += binary_search(listB, a)+ 1
    print(answer)


T=int(sys.stdin.readline())
for _ in range(T):
    numA, numB = map(int, sys.stdin.readline().split())
    listA = list(map(int, sys.stdin.readline().split()))
    listB = list(map(int, sys.stdin.readline().split()))
    solve(listA, listB)