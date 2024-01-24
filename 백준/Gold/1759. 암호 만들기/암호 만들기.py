l,c=map(int,input().split())

encrypt = list(map(str, input().split()))
encrypt.sort()
arr=[]

def validate(arr):
    j,m=0,0
    for ch in arr:
        if ch in ['a', 'e', 'i', 'o', 'u']:
            m+=1
        else:
            j+=1
    return j>=2 and m>=1

def recur(cnt, start):
    if cnt==l:
        # 검증
        if validate(arr):
            print(''.join(arr))
        return

    for i in range(start, c):
        arr.append(encrypt[i])
        recur(cnt+1, i+1)
        arr.pop()

recur(0,0)