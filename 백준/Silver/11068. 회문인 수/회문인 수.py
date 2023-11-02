# 1. 2~64진법으로 표현
# 표현한 수 회문인지 확인
def isSame(num, i):
    ans=[]
    while num>0:
        ans.append(num%i)
        num = num // i
    for i in range(len(ans)//2):
        if ans[i]!=ans[-i-1]:
            return False
    return True


n=int(input())
for _ in range(n):
    x=int(input())
    find=False
    for i in range(2,65):
        ans=isSame(x,i)
        if ans:
            find=True
            break

    if find:
        print(1)
    else:
        print(0)

