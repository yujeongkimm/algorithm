n,k=map(int,input().split())

arr=[]
for i in range(n):
    arr.append(i+1)

idx=0
ans=[]
while len(arr)>0:
    idx=idx+k-1
    if idx>=len(arr):
        idx=idx%len(arr)
    ans.append(str(arr[idx]))
    arr.pop(idx)

print("<", end='')
print(', '.join(ans), end='')
print(">", end='')