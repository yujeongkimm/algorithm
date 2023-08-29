def solution(k, score):
    answer,honor = [], []
    for i in score:
        if len(honor)<k:
            honor.append(i)
        else:
            if i>min(honor):
                honor.pop(0)
                honor.append(i)
        honor.sort()
        answer.append(honor[0])
    return answer