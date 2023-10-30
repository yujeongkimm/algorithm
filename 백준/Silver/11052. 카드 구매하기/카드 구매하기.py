n=int(input()) # 카드 개수
p=list(map(int,input().split()))
dp=[0]*(n+1)
dp[0]=0
dp[1]=p[0]
for i in range(2, n+1):
    for j in range(1,i+1): #j는 팩, i는 dp결정 
        dp[i]=max(dp[i], p[j-1]+dp[i-j])
print(dp[-1])