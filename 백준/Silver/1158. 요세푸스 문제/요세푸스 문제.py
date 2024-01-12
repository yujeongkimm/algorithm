from collections import deque
n,k=map(int,input().split())

queue=deque()

for i in range(n):
    queue.append(i+1)

point=0
ans=[]
while queue:
    for _ in range(k-1):
        queue.append(queue.popleft())
    ans.append(queue.popleft())

print(str(ans).replace('[', '<').replace(']','>'))

#n,k=map(int,input().split())
# arr=[]
# for i in range(n):
#     arr.append(i+1)
#
# idx=0
# ans=[]
# while len(arr)>0:
#     idx=idx+k-1
#     if idx>=len(arr):
#         idx=idx%len(arr)
#     ans.append(str(arr[idx]))
#     arr.pop(idx)
#
# print("<", end='')
# print(', '.join(ans), end='')
# print(">", end='')