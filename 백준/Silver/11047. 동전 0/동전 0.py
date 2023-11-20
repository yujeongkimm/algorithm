n,k=map(int,input().split())
coins=[]
for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)
ans=0
for coin in coins:
    if k>=coin:
        ans+=k//coin
        k%=coin
    if n==0:
        break
print(ans)