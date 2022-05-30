# 리스트 생성
list = list(range(1, 21))
# 입력 10번 반복
for _ in range(0, 10):
    a, b = map(int, input().split())
    # 카드 역배치
    for n in range((b-a+1)//2):
        list[a-1+n] , list[b-1-n] = list[b-1-n], list[a-1+n]
print(list)