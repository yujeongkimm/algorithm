n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
largest = -2147000000

# 각 행, 열 최대값
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += arr[i][j]
        sum2 += arr[j][i]
    if largest < sum1:
        largest = sum1
    if largest < sum2:
        largest = sum2

sum1 = sum2 = 0
# 두 대각선 최대값
for i in range(n):
    sum1 += arr[i][i]
    sum2 += arr[i][n-i-1]
if largest < sum1:
    largest = sum1
if largest < sum2:
    largest = sum2

print(largest)