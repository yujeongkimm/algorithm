def solution(t, p):
    answer = 0
    len_t, len_p = len(t), len(p)
    for idx in range(0, len_t-len_p+1):
        sliced = t[idx:idx+len_p]
        if int(sliced)<=int(p):
            answer+=1
    return answer