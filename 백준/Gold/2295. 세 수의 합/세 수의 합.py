# 1. 집합 중 세 수 고른다.
# 2. 세 수의 합이 집합에 있는지 확인한다 a+b+c=x, a+b=x-c
# 3. 2를 만족하는 가장 큰 합을 구한다.

n=int(input())
a=[]
for _ in range(n):
    a.append(int(input()))

sums=[]
for i in range(n):
    for j in range(i,n): # 중복제거
        sums.append(a[i]+a[j])

sums.sort()
def binary_serach(target):
    l,r=0,len(sums)-1
    while l<=r:
        mid=(l+r)//2
        if sums[mid]==target:
            return True
        elif sums[mid]>target:
            r=mid-1
        else:
            l=mid+1
    return False

result=-1
for i in range(n):
    for j in range(n):
        target=a[i]-a[j]
        if binary_serach(target):
            result=max(result,a[i])
print(result)