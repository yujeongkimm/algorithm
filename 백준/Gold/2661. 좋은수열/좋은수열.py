n=int(input())

arr = []

def check(index):
    # index + 1 . 전체 길이 
    for i in range(1, (index+1)//2+1):
        # 
        if arr[-i:]==arr[-2*i:-i]:
            return False
    return True


def solve(index):
    if index==n:
        for i in range(n):
            print(arr[i], end='')
        exit()

    else:
        for i in range(1,4):
            arr.append(i)

            if check(index):
                solve(index+1)

            arr.pop()

solve(0)
