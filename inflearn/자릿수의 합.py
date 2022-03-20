n = int(input())
digits = list(map(int, input().split()))

'''
# 내 풀이 
# 자연수 자릿수 합
digits = list(input().split())
val = []

def digit_sum(digit):
    s = 0
    for i in range(len(digit)):
        s += int(digit[i])
    val.append(s)


for digit in digits:
    digit_sum(digit)
    
print(digits[val.index(max(val))])
'''

'''
# 풀이(1)
def digit_sum(x):
    s = 0
    while x > 0:
        s += x%10
        x = x//10
    return s

max = -2147000000
for digit in digits:
    s = digit_sum(digit)
    # s의 최대값 찾기
    if s > max:
        max = s
        res = digit
print(res)
'''

# 풀이(2)
def digit_sum(x):
    s = 0
    for i in str(x):
        s += int(i)
    return s

max = -2147000000
for digit in digits:
    s = digit_sum(digit)
    if s > max:
        max = s
        res = digit
print(res)

