def solution(a, b, n):
    answer = 0
    while n>=a: # 회수할 수 있을 때 만큼, 계속
        get = n//a 
        bring = get * a    # 가져가는 병 개수
        n = n-bring+(get*b) # 남은 병 개수
        answer += get*b
        
    return answer