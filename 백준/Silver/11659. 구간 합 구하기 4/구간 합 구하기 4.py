import sys
input=sys.stdin.readline

n,m=map(int,input().split())
a=list(map(int,input().split()))
prefix_sum=[0]*(n+1) # 누적합
sum=0
for i in range(n):
    sum+=a[i]
    prefix_sum[i+1]=sum

for _ in range(m):
    f,t=map(int,input().split())
    print(prefix_sum[t]-prefix_sum[f-1])