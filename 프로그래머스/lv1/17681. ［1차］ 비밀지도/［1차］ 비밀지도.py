def solution(n, arr1, arr2):
    answer = []
    for x,y in zip(arr1, arr2):
        answer.append(bin(x|y)[2:].zfill(n))
    print(answer)
    for i in range(n):
        if "1" in answer[i]:
            answer[i] = answer[i].replace("1", "#")
        if "0" in answer[i]:
            answer[i] = answer[i].replace("0", " ")
    return answer