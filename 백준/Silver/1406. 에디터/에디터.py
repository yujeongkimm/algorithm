import sys
stack_l=list(input())
stack_r=[]
m=int(input())

for _ in range(m):
    command=sys.stdin.readline().split()
    if command[0]=='L' and stack_l:
        stack_r.append(stack_l.pop())
    elif command[0]=='D' and stack_r:
        stack_l.append(stack_r.pop())
    elif command[0]=='B' and stack_l:
        stack_l.pop()
    elif command[0]=='P':
        stack_l.append(command[1])

print(''.join(stack_l+list(reversed(stack_r))))


'''
시간초과
append() , O(1)
pop(), O(1)
insert(), O(N)
'''
# point=len(stack)
# for _ in range(m):
#     command=list(input().split())
#     if command[0]=='P':
#         stack.insert(point,command[1])
#         point+=1
#
#     elif command[0]=='L':
#         if point>0:
#             point-=1
#
#     elif command[0]=='D':
#         if point<len(stack):
#             point+=1
#
#     else:
#         if point>0:
#             stack.pop(point-1)
#             point-=1
#
# print(''.join(stack))

