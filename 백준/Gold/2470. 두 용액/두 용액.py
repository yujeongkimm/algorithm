n=int(input())
a=list(map(int,input().split()))

# -99 -2 -1 4 98
# 1. 정렬
# 2. 가장 왼쪽, 오른쪽 합해서 0이랑 가까운지 확인
# 2-1. 0보다 크면 오른쪽을 줄이기
# 2-2. 0보다 작으면 왼쪽 줄이기
# 2-3. 같으면 리턴

a.sort()

l,r=0,n-1
final=[a[l],a[r]]
ans=abs(a[l]+a[r])
while l<r:
    total=a[l]+a[r]
    if abs(total)<ans:
        ans=abs(total)
        final=[a[l], a[r]]
        if ans==0:
            break
    if total<0:
        l+=1
    else:
        r-=1
print(final[0],final[1])
