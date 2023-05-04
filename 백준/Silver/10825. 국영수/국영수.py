import sys
n = int(sys.stdin.readline())
array = [list(map(str, sys.stdin.readline().split(' '))) for _ in range(n)]
sorted_array = sorted(array, key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for arr in sorted_array:
    sys.stdout.write(arr[0])
    sys.stdout.write('\n')