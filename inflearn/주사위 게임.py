n = int(input())
# 입력받는거 외우기
# 입력받으면서 로직 처리하기
# sort()해서 숫자 이미 오름차순대로 정렬됨.
max = 0
for i in range(n):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)
    if a == b and b==c:
        val = 10000 + a*1000
    elif a ==b:
        val = 1000 + a*100
    elif b == c:
        val = 1000 + b*100
    else:
        val = c*100
    if val>max:
        max=val

print(max)