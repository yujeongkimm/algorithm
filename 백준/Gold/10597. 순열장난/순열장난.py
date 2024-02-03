_input = input()

if len(_input)<=9:
    n=len(_input)
else:
    n= 9 + (len(_input)-9) //2

used=[False]*(n+1)


answer=[]
def recur(index):
    global answer
    if index>=len(_input):
        print(*answer)
        exit()


    # 1자리
    target = int(_input[index])

    if target <= n and not used[target]:
        used[target]=True
        answer.append(target)
        recur(index+1)
        answer.remove(target)
        used[target]=False

    if index+1 >= len(_input):
        return

    # 2자리
    target2 = int(_input[index:index+2])

    if target2 <= n and not used[target2]:
        used[target2] = True
        answer.append(target2)
        recur(index + 2)
        answer.remove(target2)
        used[target2] = False

recur(0)