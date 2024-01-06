import sys

n,s=map(int,input().split())
arr=list(map(int,input().split()))

ans=sys.maxsize
right_index=0
current_sum=arr[0]

for i in range(n):
    while current_sum<s:
        if right_index==n-1:
            break
        right_index+=1
        current_sum+=arr[right_index]

    if current_sum>=s:
        ans=min(ans, right_index-i+1)

    current_sum-=arr[i]

print(0 if ans==sys.maxsize else ans)

# n,s=map(int,input().split())
# arr=list(map(int,input().split()))
# l,r=0,0
# length=100000
# S=arr[0]
# while True:
#     if S >= s:    # 최소 길이 비교, sum, l 갱신
#         length=min(length,r-l+1)
#         S-=arr[l]
#         l+=1
#     else:
#         r+=1
#         if r==n:
#             break
#         S+=arr[r]
# print(0) if length==100000 else print(length)