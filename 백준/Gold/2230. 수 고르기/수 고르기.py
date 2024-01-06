n,m=map(int,input().split())
arr=[int(input()) for _ in range(n)]
arr.sort()

ans=arr[-1]-arr[0]
j=0
for i in range(n):
    while arr[j]-arr[i]<m:
        if j==n-1:
            break
        j+=1
    if arr[j]-arr[i]>=m:
        ans=min(ans, arr[j]-arr[i])

print(ans)

# import sys
# n,m=map(int,input().split())
# arr=[int(sys.stdin.readline()) for _ in range(n)]
# arr.sort()
# l,r=0,1
# res=sys.maxsize
# while l<n and r<n:
#     sub=arr[r]-arr[l]
#     if sub<m:
#         r+=1
#     elif sub==m:   # 가장 작은 차이
#         res=sub
#         break
#     elif sub>m:
#         res=min(res, sub)
#         l+=1
#
# print(res)