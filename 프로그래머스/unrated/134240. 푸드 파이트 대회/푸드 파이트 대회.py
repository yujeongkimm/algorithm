def solution(food):
    answer = ''
    for i in range(1, len(food)):
        quotient = food[i]//2
        if quotient>0:
            answer+=str(i)*quotient
    reversed_answer = answer[::-1]
    answer = answer + "0" + reversed_answer
    return answer