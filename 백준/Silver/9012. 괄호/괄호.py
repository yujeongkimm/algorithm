t=int(input())
for _ in range(t):
    stack=[]
    ps=input()
    flag=True
    for char in ps:
        if char=='(':
            stack.append('(')
        else:
            if not stack:
                flag=False
                break
            stack.pop()

    if stack: flag=False

    if flag:
        print("YES")
    else: print("NO")