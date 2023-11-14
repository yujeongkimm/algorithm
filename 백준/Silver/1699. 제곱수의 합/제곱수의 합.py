import sys
input=sys.stdin.readline
n=int(input())

dp=[0]*(n+1)

# 1로 표헌할 수 있는 경우 
for i in range(n+1):
    dp[i]=i

for i in range(1, n+1):
    for j in range(1, i):
        # 제곱수가 i보다 커지면 멈춤 
        if j*j>i:
            break
        dp[i]=min(dp[i], dp[i-j*j] + 1)

print(dp[n])


# https://chanhuiseok.github.io/posts/baek-10/