def solution(dartResult):
    answer = []
    bonus = {
        "S": 1,
        "D": 2,
        "T": 3
    }
    score = ""
    for ch in dartResult:  # ch는 현재 문자 읽어옴
        if ch.isdigit():
            score += ch
        elif ch in bonus:
            answer.append(int(score) ** bonus[ch])
            score = ""  # 초기화
        elif ch=="#":
            answer[-1]*=-1
        elif ch=="*":
            answer[-1]*=2
            if len(answer)>=2:
                answer[-2]*=2
    return sum(answer)