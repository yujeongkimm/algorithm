a,b,c=map(int,input().split())


def power(a,b):
    # 정복
    if b==1:
        return a%c
    # 분할
    half = power(a, b // 2)
    # 해결 
    if b%2 == 0:
        return (half*half)%c
    else:
        return (((half*half)%c)*a)%c

print(power(a,b))