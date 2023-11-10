import sys
input=sys.stdin.readline

n=int(input())
a=[]
for _ in range(n):
    x,y=map(int,input().split())
    a.append((x,y))

# 항상 최적이 되는 선택만 한다, 그리디 
# 1. 종료시간이 빠른 순으로 배치 
# 1-1. 종료시간이 같으면 시작시간이 빠른 순으로 정렬
s=sorted(a, key=lambda x:(x[1], x[0]))

# 2. 가능한 회의 차례대로 진행 
cnt=0
end=0
for i in range(n):
    # 앞회의 끝났다면
    if end<=s[i][0]:
        cnt+=1
        end=s[i][1]
print(cnt)