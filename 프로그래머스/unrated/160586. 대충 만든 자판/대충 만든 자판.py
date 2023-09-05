def getPoints(keymap, ch):
    flag = False
    time = 101
    for key in keymap:
        if ch in key:
            time = min(key.index(ch)+1, time)
            flag = True
    if not flag:
        time=-1
    return time


def solution(keymap, targets):
    answer = []
    for target in targets:
        times = 0
        for ch in target: 
            time = getPoints(keymap, ch)
            if time == -1:
                times=-1
                break
            times+=time
        answer.append(times)
    return answer