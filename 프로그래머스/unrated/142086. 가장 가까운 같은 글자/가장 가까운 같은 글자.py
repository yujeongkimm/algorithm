def solution(s):
    answer = []
    for i in range(len(s)):
        first = s.find(s[i])    # 처음 
        if first == i:  # 처음 나온 문자이면
            answer.append(-1)
        else:   # 몇칸 떨어져있는지
            # 가장 가까운 글자 찾기
            sliced = s[:i]
            reverse = sliced[::-1]
            find = reverse.find(s[i])
            answer.append(find+1)
    return answer