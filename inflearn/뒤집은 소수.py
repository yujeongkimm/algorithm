n = int(input())
# nums = list(map(int, input().split()))
nums = [32, 55, 62, 3700, 250]


# 숫자 뒤집음
# 끝자리 0 이면 첫 자리부터 연속된 0 무시
'''
def reverse(x):
    r = reversed(str(x))
    r = ''.join(r)
    r = r.strip('0')
    return int(r)
'''

def reverse(x):
    res = 0
    while x>0:
        t = x%10    # 나머지
        res = res*10+t
        x=x//10
    return res

# 소수인지 확인
def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2+1):
        if x%i == 0:
            return False    # 소수가 아님
    else:
        return True


for num in nums:
    x = reverse(num)
    if isPrime(x):
        print(x, end=' ')