def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(len(score)//m):
        split_score = score[m*i:m*(i+1)]
        answer+=min(split_score)*m
    return answer