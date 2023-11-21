n,k=map(int,input().split())
coins=[int(input()) for _ in range(n)]
dp=[10001]*(k+1)

for coin in coins:
    if coin<=k:
        dp[coin]=1

for coin in coins:
    for i in range(1,k+1):
        if i-coin>=0:
            dp[i]=min(dp[i], dp[i-coin]+1)

if dp[k]==10001:
    print(-1)
else:
    print(dp[k])