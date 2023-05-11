import sys
n=int(sys.stdin.readline())
arr = [[] for _ in range(n+1)]
for _ in range(n):
    coord, color = map(int, sys.stdin.readline().split())
    arr[color].append(coord)

def left(idx, color):
    if idx==0:
        return 100000
    else:
        return arr[color][idx]-arr[color][idx-1]
def right(idx, color):
    if idx==len(arr[color])-1:
        return 100000
    else:
        return arr[color][idx+1]-arr[color][idx]

sum=0
for color in range(n+1):
    arr[color].sort()
    size=len(arr[color])
    for i in range(size):
        val = min(left(i, color), right(i,color))
        sum+=val

print(sum)