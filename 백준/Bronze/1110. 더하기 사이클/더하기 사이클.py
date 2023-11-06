n=int(input())

# 1. n의 각 자릿수 더하기
def sum_of_digit(n):
    s=0
    num=int(n)
    while num>0:
        s+=num%10
        num=num//10
    return s

# 2. n의 가장 오른쪽 자리 + 1에서 구한 수의 가장 오른쪽 자리를 이어 붙인다
def combine(a,b):
    c=''
    c=str(b)[-1] + str(a)[-1]
    return c


# 3. 원래의 수로 돌아가는 사이클 수 구한다.
ans=0
new=n
while True:
    a=sum_of_digit(new)
    b=combine(a,new)
    new=b
    ans+=1
    if int(b)==n:
        print(ans)
        break