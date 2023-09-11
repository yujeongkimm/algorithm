def solution(n, m, section):
    answer = 0
    
    while(len(section)>0):
        current=section[0]  #2
        for i in range(m): #4번반복
            if (current+i)==section[0]:
                section.pop(0)
            if len(section)==0:
                break
        answer+=1
    return answer