from collections import deque
t=int(input())

for _ in range(t):
    p = input()
    n = int(input())
    arr = input()[1:-1].split(',')
    queue=deque(arr)

    isValid=True
    isFlipped=False

    if n==0:
        queue=[]

    for char in p:
        if char=='R':
            isFlipped= not isFlipped
        elif char=='D':
            if not queue:
                isValid=False
                break
            if isFlipped:
                queue.pop()
            else: queue.popleft()

    if isValid:
        if isFlipped:
            queue.reverse()
        print('[' +','.join(queue) + ']')
    else: print("error")