t=int(input())
k=int(input())
coins=[]
for _ in range(k):
    p,n=map(int,input().split())
    coins.append((p,n))
coins.sort()

dp=[0]*(t+1)
dp[0]=1

for coin, cnt in coins: 
    for money in range(t,0,-1):
        for i in range(1,cnt+1):
            if money-coin*i>=0:
                dp[money]=dp[money]+dp[money-coin*i]
print(dp[t])