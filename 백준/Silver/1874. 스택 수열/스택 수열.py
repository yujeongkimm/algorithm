n=int(input())
stack=[]
ans=[]

next=1
flag=True
for _ in range(n):
    w=int(input())

    # input까지 push한다
    while next<=w:
        stack.append(next)
        next+=1
        ans.append('+')

    # top이 input이면 pop한다
    if stack[-1]==w:
        stack.pop()
        ans.append('-')

    # 아니면 no를 출력한다.
    else:
        flag=False
        break

if flag:
    for i in ans:
        print(i)
else:
    print('NO')

