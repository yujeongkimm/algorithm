n=int(input())
liquid=list(map(int,input().split()))
liquid.sort()

left,right=0,n-1
ans_total=abs(liquid[left]+liquid[right])
ans_left=left
ans_right=right
while left<right:
    total=liquid[left]+liquid[right]
    if abs(total)<ans_total:
        ans_total=abs(total)
        ans_left=left
        ans_right=right
    if total>0:
        right-=1
    else:
        left+=1
print(liquid[ans_left], liquid[ans_right])