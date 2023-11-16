# dp -> i번째 계단까지 올라왔을 때 얻을 수 있는 최대 점수 
# 마지막 계단 반드시 밟는다
# 이전계단에서 올라오는 경우, 전전계단에서 올라오는 경우 

n=int(input())
a=[0]*301
for i in range(1, n+1):
    a[i]=int(input())
    
dp=[0]*301
dp[1]=a[1]
dp[2]=a[1]+a[2]
dp[3]=max(a[3]+a[1], a[3]+a[2])

for i in range(4, n+1):
    dp[i]=max(a[i]+a[i-1]+dp[i-3], a[i]+dp[i-2])
    
print(dp[n])