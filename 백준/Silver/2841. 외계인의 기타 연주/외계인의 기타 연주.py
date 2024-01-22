n,p=map(int,input().split())
stack=[ [] for _ in range(7)]

count=0
for _ in range(n):
    a,b=map(int,input().split())

    while stack[a-1]:
        if stack[a-1][-1]>b:
            stack[a-1].pop()
            count+=1
        else:
            break

    if stack[a-1] and b==stack[a-1][-1]:
        continue

    stack[a-1].append(b)
    count+=1

print(count)

