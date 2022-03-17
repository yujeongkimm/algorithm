n = int(input())
scores = list(map(int, input().split()))

# n명의 학생들 평균, sum() 이용
average = round(sum(scores)/n)
# 정수형 가장 큰값? (4byte = 2**32승)
min = 2147000000

# 평균에 가장 가까운 학생
''' 
내 풀이
for score in scores:
    if abs(average-score) <= min:
        min = abs(average-score)
        list.append(score)
list = sorted(list, reverse=True)
print(list)
print(average , scores.index(list[0]) +1)
'''
for idx, x in enumerate(scores):
    value = abs(average - x)
    if value < min:
        min = value
        score = x
        index = idx + 1
    elif value == min:
        if x > score:
            score = x
            index = idx + 1

print(average, index)