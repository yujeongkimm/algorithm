def solution(X, Y):
    answer = ''
    for i in (set(X) & set(Y)): #교집합 원소 하나씩 순회
        for j in range( min(X.count(i), Y.count(i) ) ):    #반복횟수
            answer+=i
    answer = sorted(answer, reverse=True)
    answer = "".join(answer)
    if answer=="":
        answer="-1"
    elif answer[0]=="0":
        answer="0"
    return answer