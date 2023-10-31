# 내 코드에 시간복잡도 문제가 없다면, 입출력 함수 바꾸기
import sys

n=int(sys.stdin.readline()) # 입력받을 개수
a=[0]*100001 # 리스트의 인덱스는 수, 값은 수가 나온 개수
for _ in range(n): #n번만큼 입력, O(N)
    x=int(sys.stdin.readline())
    a[x]+=1

for i in range(100001): #O(10000)
    while a[i]>0: # 1번은 무조건 실행, 원소의 개수 만큼 반복 => 10000 + 원소의 개수 (N)
        print(i)
        a[i]-=1

'''
10번째줄~
O(max(10000,N)

=> O(N)
'''
