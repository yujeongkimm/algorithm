n=int(input())

def calculateSqrt(n):
    if n==0:
        return 0
    l,r=1,2**32
    sqrt=-1
    while l<=r:
        mid=(l+r)//2
        if mid*mid>=n:
            r=mid-1
            sqrt=mid
        else:
            l=mid+1
    return sqrt

print(calculateSqrt(n))