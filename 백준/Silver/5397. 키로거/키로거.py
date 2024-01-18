n=int(input())

for _ in range(n):
    s=input()

    left_stack=[]
    right_stack=[]
    for ch in s:
        if ch=='<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif ch=='>':
            if right_stack:
                left_stack.append(right_stack.pop())
        elif ch=='-':
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(ch)
            
    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))