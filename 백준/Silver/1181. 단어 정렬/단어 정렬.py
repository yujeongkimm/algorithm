n=int(input())
a=[]
for _ in range(n):
    a.append(input())
# 1. 단어 길이 짧은 것부터
# 1-1. 단어 길이 같으면 사전순으로
# 2. 중복된 단어 제거
a=set(a)
a=list(a)
a.sort(key=lambda x:(len(x),x))

for i in a:
    print(i)
