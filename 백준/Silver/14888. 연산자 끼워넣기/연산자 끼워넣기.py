import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(' ')))
operators = list(map(int, sys.stdin.readline().split(' ')))
min=1e9
max=-1e9

def calculate(operator, operand1, operand2):
    if operator==0:
        return operand1+operand2
    if operator==1:
        return operand1-operand2
    if operator==2:
        return operand1*operand2
    if operator==3:
        if operand1<0:
            return -(-operand1//operand2)
        else: return operand1//operand2
        

def dfs(cnt, value):
    if cnt == n-1:
        global min, max
        min=min if min < value else value
        max=max if max > value else value
    else:
        for i in range(4):
            global operators
            if operators[i] != 0:
                operators[i]-=1
                dfs(cnt+1, calculate(i, value, arr[cnt+1]))
                operators[i]+=1
                
    
dfs(0, arr[0])
print(max)
print(min)