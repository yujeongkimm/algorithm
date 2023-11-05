x=int(input())
n=int(input())
score=[]
name=[-1]*26 # 이름은 대문자 알파벳, 받은 칩 개수 저장, 득표율 5% 이상 참가자 구분

# 1. 전체 참가자의 5% 미만의 득표율 얻는 사람 제외
for _ in range(n):
    staff, vote = tuple(input().split())
    vote = int(vote)
    if vote/x*100 >= 5:
        name[ord(staff)-ord('A')]=0
        for i in range(1,15):
            score.append((staff, vote/i))
# 2. 남은 스태프 득표수를 1로 나눈값, 2로 나눈값, ... 14로 나눈값 구하기
# 3. 점수 집합에서 가장 큰 1~14번째 후보에게 칩 나눠주기
score.sort(key=lambda x:x[1], reverse=True)
for i in range(14):
    n=score[i][0]
    idx=ord(n)-ord('A')
    name[idx]+=1

# 4. 각 스태프가 받은 칩 개수 구하기
for i in range(26):
    if name[i]!=-1: # 득표율 5% 이상
        print(chr(ord('A')+i), name[i])