from collections import deque
t=int(input())

for _ in range(t):
    n,m=map(int,input().split())
    queue=deque(map(int,input().split()))
    queue=deque((idx,i) for idx, i in enumerate(queue))
    
    count=0
    
    while True:
        if queue[0][1]==max(queue, key=lambda x:x[1])[1]:
            count+=1
            if queue[0][0]==m:
                print(count)
                break
            else:
                queue.popleft()
        else:
            queue.append(queue.popleft())