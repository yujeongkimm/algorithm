import sys
n = int(sys.stdin.readline())
arr = [0] * n
for i in range(n):
    arr[i] = int(sys.stdin.readline())
arr.sort()

before = arr[0]
cnt = 1
max_cnt = 1
value = arr[0]

for i in range(1, n):
    if before == arr[i]:
        cnt += 1
    else:
        before = arr[i]
        cnt = 1
    if cnt > max_cnt:
        max_cnt = cnt
        value = arr[i]

print(value)
