def solution(board, moves):
    answer = 0
    stack=[]
    for move in moves:
        for i in range(len(board[0])):
            if board[i][move-1]!=0:
                stack.append(board[i][move-1])
                board[i][move-1]=0
                break
        if len(stack)>=2:
            if stack[-1]==stack[-2]:
                answer+=2
                stack.pop(-1)
                stack.pop(-1)
    return answer