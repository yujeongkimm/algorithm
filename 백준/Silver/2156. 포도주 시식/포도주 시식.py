# a, dp : 1-based index
n=int(input())
a=[0]*(n+2)
for i in range(1,n+1):
    a[i]=int(input())

dp=[0]*(n+2)
dp[1]=a[1]
dp[2]=a[1]+a[2]

for i in range(3,n+1):
    dp[i]=max(dp[i-1], a[i]+a[i-1]+dp[i-3], a[i]+dp[i-2])

print(max(dp))