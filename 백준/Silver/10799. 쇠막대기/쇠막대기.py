s=input()
n=len(s)

s=' ' + s
laser_sum=[0]*(n+1)

for i in range(1,n+1):
    laser_sum[i]=laser_sum[i-1]
    if s[i]=='(' and s[i+1]==')':
        laser_sum[i]+=1

stack=[]
ans=0
for i in range(1, n+1):
    if s[i]=='(' and s[i+1]!=')':
        stack.append(i)
    elif s[i]==')' and s[i-1]!='(':
        startIndex=stack.pop()
        ans+= laser_sum[i]-laser_sum[startIndex] +1

print(ans)