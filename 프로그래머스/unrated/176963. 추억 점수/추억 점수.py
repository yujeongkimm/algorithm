def solution(name, yearning, photo):
    answer=[]
    yearning_dict={name:yearning for name, yearning in zip(name,yearning)}
    for arr in photo:
        score=0
        for s_name in arr:
            if s_name in name:
                score+=yearning_dict[s_name]
        answer.append(score)
    return answer