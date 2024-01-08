n,m=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

idx1=idx2=0

ans=[]

while idx1<n and idx2<m:
    if A[idx1]<B[idx2]:
        ans.append(A[idx1])
        idx1+=1
    else:
        ans.append(B[idx2])
        idx2+=1

while idx1<n:
    ans.append(A[idx1])
    idx1+=1
    
while idx2<m:
    ans.append(B[idx2])
    idx2+=1

print(*ans)