n, k = map(int, input().split())
cards = list(map(int, input().split()))
list = set()

# 3장 뽑는 모든 경우 수
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            list.add(cards[i] + cards[j] + cards[m])
list = sorted(list, reverse=True)
print(list[2])

# set 자료-> 중복 X
# 헷갈리면 예시 그려서 패턴 찾기
# 중첩 반복문