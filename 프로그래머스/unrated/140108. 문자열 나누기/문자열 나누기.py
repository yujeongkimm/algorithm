def solution(s):
    answer = 0
    first_alpha=""
    alpha_n, dif_alpha_n=0,0
    for alpha in s:
        if first_alpha=="":
            first_alpha=alpha
            alpha_n+=1
            continue
        if alpha==first_alpha:
            alpha_n+=1
        else:
            dif_alpha_n+=1
        if alpha_n==dif_alpha_n:
            answer+=1
            alpha_n, dif_alpha_n=0,0
            first_alpha=""
    if first_alpha!="":
        answer+=1
    return answer