n,m=map(int,input().split())
s=[]
for _ in range(n):
    s.append(input())

s.sort()

def binary_search(target):
    l,r=0,n-1
    while l<=r:
        mid=(l+r)//2
        if s[mid]==target:
            return True
        elif s[mid]<target:
            l=mid+1
        else:
            r=mid-1

sum=0
for _ in range(m):
    strings=input()
    if binary_search(strings):
        sum+=1

print(sum)