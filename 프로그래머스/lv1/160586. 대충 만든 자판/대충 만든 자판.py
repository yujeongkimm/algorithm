def solution(keymap, targets):
    answer = []
    for target in targets:
        times=0
        for ch in target:
            time=101
            flag=False
            for key in keymap:
                if ch in key:
                    time=min(key.index(ch)+1, time)
                    flag=True
            if not flag:
                times=-1
                break
            times+=time
        answer.append(times)    
    return answer