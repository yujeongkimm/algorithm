n,m=map(int,input().split())
listA=list(map(int,input().split()))
listB=list(map(int,input().split()))
a,b=0,0
ans=[]
while a!=n or b!=m:    # a==len(a) and b==len(b)면 while문 탈출
    if n==a:
        ans.append(listB[b])
        b+=1
    elif m==b:
        ans.append(listA[a])
        a+=1
    else:
        if listA[a]>listB[b]:
            ans.append(listB[b])
            b+=1
        else:
            ans.append(listA[a])
            a+=1
print(*ans)