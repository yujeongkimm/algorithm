n,k=map(int,input().split())
items=[]
for _ in range(n):
    w,v=map(int,input().split())
    items.append((w,v))

dp=[0 for _ in range(k+1)] # 무게i일때 최대 가치값

for item in items:
    w,v=item
    for i in range(k,w-1,-1):
        dp[i]=max(dp[i], v+dp[i-w])
        # dp[i-w]는 이전 표를 참조하기 때문에 i는 내림차순으로 순회
        # 오름차순으로 순회하면 dp[i-w]는 현재 표 참조
print(dp[k])