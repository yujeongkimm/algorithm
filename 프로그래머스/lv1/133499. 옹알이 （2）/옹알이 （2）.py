def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    for b in babbling:
        for word in words:
            if (word in b) and (word*2 not in b):
                b = b.replace(word, ' ') # 공백
        if len(b.strip())==0:
            answer+=1
    return answer