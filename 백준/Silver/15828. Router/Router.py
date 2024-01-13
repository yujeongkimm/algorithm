# FIFO queue
# 양의 정수는 패킷 들어옴
# 0 은 라우터가 패킷 하나 처리함
# -1은 입력의 끝
from collections import deque
import sys
n=int(sys.stdin.readline())
queue=deque()

while True:
    p=int(sys.stdin.readline())
    if p==0:
        queue.popleft()
        continue
    if p==-1:
        break
    if len(queue)<n:
        queue.append(p)

if queue:
    print(*queue)
else: print("empty")