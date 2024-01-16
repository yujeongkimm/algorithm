while True:
    s=input()
    stack=[]

    flag=True

    if s=='.':
        break

    for char in s:
        if char.isalpha():
            continue
        if char=='[':
            stack.append('[')
        elif char==']':
            if stack and stack[-1]=='[':
                stack.pop()
            else:
                flag=False
                break
        elif char=='(':
            stack.append('(')
        elif char==')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                flag=False
                break

    if stack:
        flag=False
        
    if flag:
        print("yes")
    else: print("no")