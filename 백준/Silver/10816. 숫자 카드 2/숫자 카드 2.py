import sys
input=sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))
m=int(input())
m_list = list(map(int,input().split()))

a.sort()

def lowerBoundIndex(target):
    lowerBoundIndex=n
    # x 이상인 값 처음 나오는 위치
    l,r=0,n-1
    while l<=r:
        mid=(l+r)//2
        if a[mid] < target:
            l=mid+1
        else:
            r=mid-1
            lowerBoundIndex=mid
    return lowerBoundIndex
    
def upperBoundIndex(target):
    upperBoundIndex=n
    # x 초과인 값 처음 나오는 위치 
    l,r=0, n-1
    while l<=r:
        mid=(l+r)//2
        if a[mid]<=target: # 필요 없는 값 
            l=mid+1
        else:
            r=mid-1
            upperBoundIndex=mid
    return upperBoundIndex

for m in m_list:
    lowerIndex=lowerBoundIndex(m)
    upperIndex=upperBoundIndex(m)
    print(upperIndex-lowerIndex, end=' ')