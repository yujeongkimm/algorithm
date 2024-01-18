s=input()
stack=[]

temp=1
ans=0

for i in range(len(s)):
    if s[i]=='(':
        temp*=2
        stack.append(s[i])

    elif s[i]=='[':
        temp*=3
        stack.append(s[i])

    elif s[i]==']':
        if not stack or stack[-1]=='(':
            ans=0
            break

        if s[i-1]=='[':
            ans+=temp

        temp//=3
        stack.pop()

    elif s[i]==')':
        if not stack or stack[-1]=='[':
            ans=0
            break

        if s[i-1]=='(':
            ans+=temp

        temp//=2
        stack.pop()


if stack:
    print(0)
else: print(ans)

# 분배법칙